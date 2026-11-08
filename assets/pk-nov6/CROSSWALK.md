# PK intake crosswalk

[crosswalk.json](crosswalk.json) indexes all 1,217 source notes from [intake.json](intake.json). Each note points to records for the mathematical claims it contains. Multiple notes can point to the same claim when their statements agree mathematically. Give the source locator for each appearance and the equivalence argument when adding another source to an existing claim.

- `notes` maps every original candidate ID to its stage and source links. A null value marks a note awaiting triage. `triaged` records a preliminary breakdown. `resolved` records a checked disposition for every claim, including any precise hold.
- `claims` stores the precise statement once, under a stable key of the form `<first-source-id>:<number>`. Each source link has a `section` and a `claim` key. An additional source link for the same claim records a `same_claim_reason`.
- Each claim records a `relation`, a `disposition`, and a mathematical `reason`. `fact_ids` names the accepted facts that cover the claim or the new accepted fact. `related_facts` and optional `related_sources` hold comparisons to accepted facts and original notes. `depends_on` lists accepted results used by the argument, with named external results in `external_dependencies` and exact missing steps in `open_dependencies`.

| Disposition | Meaning |
| --- | --- |
| `reuse_lead` | Preliminary overlap requiring a mathematical comparison. |
| `reused` | The stated argument shows that the linked fact or facts cover the claim. |
| `ready` | A candidate for formal review, with any prerequisite named. |
| `accepted` | An independently reviewed claim entered in `facts/`. |
| `held` | A concrete proof gap, unresolved prerequisite, or unresolved scope comparison is recorded. |
| `context` | A supporting calculation, construction step, or reference. |

Use `equivalent`, `covered`, `specialization`, `extension`, `distinct`, or `unresolved` for the relation. Explain what changes in the hypotheses or conclusion. A similar title or lexical match can motivate a comparison and belongs in `related_facts` until the mathematical implication is checked.

The [pilot report](../../reviews/pk-intake/pilot.md) and batch reports [1](../../reviews/pk-intake/wave01.md), [2](../../reviews/pk-intake/wave02.md), [3](../../reviews/pk-intake/wave03.md), [4](../../reviews/pk-intake/wave04.md), [5](../../reviews/pk-intake/wave05.md), [6](../../reviews/pk-intake/wave06.md), [7](../../reviews/pk-intake/wave07.md), [8](../../reviews/pk-intake/wave08.md), [9](../../reviews/pk-intake/wave09.md), [10](../../reviews/pk-intake/wave10.md), [11](../../reviews/pk-intake/wave11.md), [12](../../reviews/pk-intake/wave12.md), [13](../../reviews/pk-intake/wave13.md), [14](../../reviews/pk-intake/wave14.md), [15](../../reviews/pk-intake/wave15.md), [16](../../reviews/pk-intake/wave16.md), [17](../../reviews/pk-intake/wave17.md), [18](../../reviews/pk-intake/wave18.md), and [19](../../reviews/pk-intake/wave19.md) record independent proof reviews, timing, and rework. Commit checked batches separately on the intake branch and submit the completed intake in one PR.

The [contribution rules](../../CONTRIBUTING.md) govern admission. The original candidate files and historical reviews are preserved. Normalize a new result in a separate candidate and link its sources. Before committing a batch, run:

```sh
python3 scripts/check_graph.py
python3 scripts/check_pk_nov6.py
python3 scripts/check_pk_crosswalk.py
python3 scripts/check_pk_parity_core.py
```
