"""Validate the shared fact graph using only the Python standard library."""
import hashlib
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
state = json.loads((root / "state.json").read_text())
facts, candidates, runs = (state[k] for k in ("facts", "candidates", "runs"))


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


require(digest(root / state["problem_file"]) == state["problem_sha256"], "Problem hash mismatch")
for directory, records, suffix in (("facts", facts, ".md"), ("candidates", candidates, ".json"), ("verifications", runs, ".json")):
    require({p.stem for p in (root / directory).glob("*" + suffix)} == set(records), f"File/ledger mismatch: {directory}")

for cid, candidate in candidates.items():
    data = json.loads((root / "candidates" / f"{cid}.json").read_text())
    require(data["candidate_id"] == cid, f"Candidate ID mismatch: {cid}")
    for key in ("author", "kind", "depends_on", "subgoal_id", "candidate_schema"):
        require(data[key] == candidate[key], f"Candidate metadata mismatch: {cid}/{key}")
    require(candidate["subgoal_id"] in state["subgoals"], f"Missing subgoal: {cid}")
    require(set(candidate["depends_on"]) <= facts.keys(), f"Missing predecessor: {cid}")
    require(candidate["status"] in {"accepted", "rejected", "pending"}, f"Unknown status: {cid}")
    require((cid in facts) == (candidate["status"] == "accepted"), f"Acceptance mismatch: {cid}")
    for rid in candidate["runs"]:
        require(rid in runs and runs[rid]["candidate_id"] == cid, f"Invalid run link: {cid}/{rid}")

for rid, run in runs.items():
    require(run["output_file"] == f"verifications/{rid}.json", f"Invalid output path: {rid}")
    path = root / run["output_file"]
    data = json.loads(path.read_text())
    require(digest(path) == run["output_sha256"], f"Verification hash mismatch: {rid}")
    require(data["verdict"] == run["verdict"], f"Verdict mismatch: {rid}")
    require(run["status"] == {"APPROVED": "approved", "REJECTED": "rejected"}.get(run["verdict"]), f"Run status mismatch: {rid}")
    require(run["candidate_id"] in candidates and rid in candidates[run["candidate_id"]]["runs"], f"Unlinked run: {rid}")

for fid, fact in facts.items():
    header = (root / "facts" / f"{fid}.md").read_text().split("---\n", 2)[1]
    fields = dict(line.split(": ", 1) for line in header.splitlines() if ": " in line)
    require(fields["fact_id"] == fid and fact["status"] == "accepted", f"Invalid fact: {fid}")
    require(json.loads(fields["depends_on"]) == fact["depends_on"], f"Dependency mismatch: {fid}")
    for key in ("kind", "subgoal_id", "assurance"):
        require(fields[key] == fact[key], f"Fact metadata mismatch: {fid}/{key}")
    for key in ("author", "kind", "subgoal_id", "depends_on", "accepted_run"):
        require(fact[key] == candidates[fid][key], f"Accepted candidate mismatch: {fid}/{key}")
    rid = fact["accepted_run"]
    require(rid in runs and runs[rid]["verdict"] == "APPROVED" and runs[rid]["candidate_id"] == fid, f"Missing approval: {fid}")
    require(fields["verifier_run"] == rid, f"Verifier link mismatch: {fid}")

visiting, depths = set(), {}


def depth(fid):
    require(fid not in visiting, f"Dependency cycle: {fid}")
    if fid not in depths:
        visiting.add(fid)
        depths[fid] = max((depth(dep) + 1 for dep in facts[fid]["depends_on"]), default=0)
        visiting.remove(fid)
    return depths[fid]


for fid in facts:
    depth(fid)
private = re.compile(r"/(?:Users|home|root)/|My Drive|chatgpt\.com/(?:c|share)/|claude\.ai/(?:chat|share)/|codex://|[\w.+-]+@(?:gmail|icloud|jhu)\.(?:com|edu)", re.I)
for path in [root / "state.json", root / "problem_statement.md", *(root / "facts").glob("*.md"), *(root / "candidates").glob("*.json"), *(root / "verifications").glob("*.json")]:
    require(not private.search(path.read_text()), f"Private reference: {path.relative_to(root)}")
print(f"OK: {len(facts)} facts, {len(candidates)} candidates, {len(runs)} verification runs; maximum depth {max(depths.values())}.")
