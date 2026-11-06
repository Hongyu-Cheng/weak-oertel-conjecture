# Contributing

Use a branch and pull request for a new result, a correction, or a change to the graph. Use an issue to claim a subgoal or discuss a gap, quoting the relevant fact IDs and exact mathematical statement. Check the current facts before adopting a historical subgoal as an assignment.

## New results

1. State the hypotheses, conclusion, and relation to the problem in `problem_statement.md`. Give the full proof and list every accepted predecessor in `depends_on`. A counterexample must say exactly which intermediate assertion it refutes.
2. Add a uniquely named JSON file under `candidates/` and its entry in `state.json`, initially with status `pending`. Follow an existing candidate's fields. Use a fresh 16-character hexadecimal ID and keep it stable.
3. Have a separate reviewer examine the proof and the applicability of its predecessors. Record the verdict, gaps, and reviewer corrections under `verifications/` with a fresh run ID, then add the run to the ledger. Identify the review method honestly; model approval is `LLM-verified`.
4. Only an approved candidate can enter `facts/`. Add the fact file and matching ledger entry, link its approving run, and update the candidate status. Rejected and pending work remains outside `facts/`.
5. Update the fact index and, when relevant, the highlights. Run `python3 scripts/check_graph.py` before submitting the pull request.

Use a consistent contributor label in the candidate and fact metadata. The initial snapshot's `research-agent` label replaces private agent identifiers and does not identify a human author. Do not silently replace an accepted proof after review: submit the revised proof as a new candidate and explain which earlier claim it corrects or supersedes. If a flaw affects existing dependents, discuss and resolve that dependency chain in the same pull request before treating those results as accepted again.

Keep private prompts, chat exports, personal settings, credentials, machine paths, and local automation files out of the repository. Cite a paper by title and a stable public link when available. Unshared research notes are provenance, not accepted premises. Share this private repository through GitHub collaborator access.

## Integrity checks

The checker validates the graph's records and links; it does not verify mathematics. Each run's `output_sha256` is the SHA-256 digest of its verification JSON file. `problem_sha256` is the digest of the problem file. Keep these hashes synchronized when adding a record. A new conjecture or a changed target needs an explicit discussion; do not silently edit the problem statement.
