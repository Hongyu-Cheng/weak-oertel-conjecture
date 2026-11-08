"""Check coverage, references, and bookkeeping in the PK intake crosswalk."""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "assets" / "pk-nov6"
FINAL = {"accepted", "reused", "held", "context"}
DISPOSITIONS = FINAL | {"ready", "reuse_lead"}
RELATIONS = {"equivalent", "covered", "specialization", "extension", "distinct", "unresolved"}


def read(path):
    return json.loads(path.read_text())


def require(ok, message):
    if not ok:
        raise SystemExit(message)


def has_text(value):
    return isinstance(value, str) and bool(value.strip())


intake = read(DATA / "intake.json")
state = read(ROOT / "state.json")
crosswalk = read(DATA / "crosswalk.json")
notes, claims = crosswalk["notes"], crosswalk["claims"]
source_ids = {record["candidate_id"] for record in intake["records"]}
facts = state["facts"]
require(crosswalk["batch"] == intake["batch"], "Wrong intake batch")
require(len(source_ids) == len(intake["records"]) == 1217, "Wrong intake size")
require(notes.keys() == source_ids, "Crosswalk must cover exactly the original note IDs")

seen_statements = {}
dispositions = Counter()
for key, claim in claims.items():
    source, separator, number = key.partition(":")
    require(source in notes and separator and number.isdigit(), f"Invalid claim key: {key}")
    status = claim["disposition"]
    require(status in DISPOSITIONS and claim["relation"] in RELATIONS, f"Invalid status or relation: {key}")
    require(has_text(claim["statement"]) and has_text(claim["reason"]), f"Missing statement or reason: {key}")
    statement = " ".join(claim["statement"].split())
    require(statement not in seen_statements, f"Duplicate statement: {key} and {seen_statements.get(statement)}")
    seen_statements[statement] = key
    for field in ("fact_ids", "related_facts", "depends_on"):
        values = claim[field]
        require(isinstance(values, list) and len(set(values)) == len(values), f"Invalid {field}: {key}")
        require(set(values) <= facts.keys(), f"Unaccepted {field} reference: {key}")
    for field in ("external_dependencies", "open_dependencies"):
        require(isinstance(claim[field], list) and all(map(has_text, claim[field])), f"Invalid {field}: {key}")
    related_sources = claim.get("related_sources", [])
    require(isinstance(related_sources, list) and set(related_sources) <= notes.keys(),
            f"Invalid related source reference: {key}")

    if status == "accepted":
        require(len(claim["fact_ids"]) == 1 and not claim["open_dependencies"], f"Incomplete acceptance: {key}")
        fact_id = claim["fact_ids"][0]
        candidate_file = ROOT / "candidates" / f"{fact_id}.json"
        candidate = read(candidate_file)
        require(claim["statement"] == candidate["statement"], f"Accepted statement mismatch: {key}")
        require(claim["depends_on"] == facts[fact_id]["depends_on"], f"Accepted dependency mismatch: {key}")
        run = state["runs"][facts[fact_id]["accepted_run"]]
        review = read(ROOT / run["output_file"])
        require(review["candidate_sha256"] == sha256(candidate_file.read_bytes()).hexdigest(),
                f"Review is not bound to candidate: {fact_id}")
        for field in ("statement", "proof"):
            expected = sha256(candidate[field].encode("utf-8")).hexdigest()
            require(review[f"reviewed_{field}_sha256"] == expected, f"Reviewed {field} mismatch: {fact_id}")
        fact_text = (ROOT / "facts" / f"{fact_id}.md").read_text()
        body = candidate["statement"] + "\n\n## Proof\n\n" + candidate["proof"]
        require(fact_text.partition("\n## Statement\n\n")[2] == body, f"Accepted proof mismatch: {fact_id}")
    if status == "reused":
        require(claim["fact_ids"] and not claim["open_dependencies"], f"Incomplete reuse: {key}")
        require(claim["relation"] in {"equivalent", "covered", "specialization"}, f"Missing implication type: {key}")
    if status == "held":
        require(claim["open_dependencies"], f"Held claim lacks a specific gap: {key}")
    if status == "reuse_lead":
        require((claim["related_facts"] or related_sources) and not claim["fact_ids"], f"Invalid reuse lead: {key}")
    dispositions[status] += 1

references = Counter()
owned = set()
stages = Counter()
for note_id, note in notes.items():
    if note is None:
        stages["untriaged"] += 1
        continue
    stage, entries = note["stage"], note["entries"]
    require(stage in {"triaged", "resolved"} and entries, f"Invalid note stage or missing entries: {note_id}")
    require(len({(e["section"], e["claim"]) for e in entries}) == len(entries), f"Repeated source link: {note_id}")
    for entry in entries:
        key = entry["claim"]
        require(key in claims and has_text(entry["section"]), f"Invalid source link: {note_id}")
        if key.partition(":")[0] != note_id:
            require(has_text(entry.get("same_claim_reason")), f"Missing equivalence reason: {note_id} to {key}")
        else:
            owned.add(key)
        if stage == "resolved":
            require(claims[key]["disposition"] in FINAL, f"Unresolved claim in resolved note: {note_id}, {key}")
        references[key] += 1
    stages[stage] += 1

require(references.keys() == claims.keys(), "Unlinked crosswalk claim")
require(owned == claims.keys(), "Claim missing from its first source")
print(f"OK: {sum(stages.values())} source notes, {len(claims)} canonical claims.")
print("Note stages:", ", ".join(f"{k}={stages[k]}" for k in sorted(stages)))
print("Claim dispositions:", ", ".join(f"{k}={dispositions[k]}" for k in sorted(dispositions)))
