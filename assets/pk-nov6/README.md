# PK November 6 mathematical submissions

Start with [the short contribution guide](../../contributions-PK-nov-6-merge.md).
The [complete submission index](INDEX.md) groups the mathematical notes by topic.
The [intake crosswalk](CROSSWALK.md) tracks the disposition of claims extracted from those notes.

## How this batch fits the shared graph

The existing problem statement, accepted facts, historical verification runs,
and accepted-fact index are preserved. New composite submissions use the existing
candidate schema, with status `pending`, `runs: []`, and contributor label
`PK-research-agent`. The pending-only kind `research-note` identifies a mathematical
note whose individual claims and dependency obligations have not yet been
normalized into accepted graph nodes. This category is not a proof assurance.

Each record retains its scoped definitions, proposed arguments, and limitations.
Some contain several results; some contain a conditional reduction, an auxiliary
counterexample, or an unresolved calculation. Split and independently review
precise claims under [CONTRIBUTING.md](../../CONTRIBUTING.md) before accepting them.
No historical PASS statement has been converted into a new approval.

`depends_on` lists accepted predecessors explicitly used in the edited argument.
`unaccepted_references` links other submissions for review; it is not a list of
accepted premises. `related_facts` records comparisons, not proof dependencies.
An empty dependency list on a pending note does not certify self-containment.
Historical mathematical review comments expose corrections and qualifications;
they have `is_approval: false` and are outside `verifications/`.

## Notation and scope

The locked target uses positive integers n,d, mixed-integer measure H_d, and raw
point depth h_S. For positive total mixed volume W=H_d(S), a normalized point
depth is h_S(y)/W; normalized maximum depth is max_y h_S(y)/W. The notes often
write M for total mass or Q for raw maximum depth, but local definitions always
control: those letters also occur in unrelated scalar formulas.

Historical “OC” means the sharper proposed constant 2^(-n) gamma_d, where
 gamma_d=(d/(d+1))^d. A sharp bound under extra hypotheses is a restricted result,
not a resolution of the shared all-dimensional weak target. Intrinsic H_q results
and n=0/d=0 statements are auxiliary extensions. They do not replace H_d or the
quantifiers in problem_statement.md; its W=0 case remains automatic. Scalar
profile laws, ordinary convex bodies, density-weighted models and smoothed
objectives remain the auxiliary models explicitly defined in their notes.

## Overlap review and provenance

The comparison baseline is recorded in `intake.json`. Existing accepted results
are reused by ID when they cover our argument. Duplicate portions were replaced
by citations while retaining additional constants, prescribed centers, intrinsic
extensions, rigidity conclusions, or exact counterexamples. See
`overlap-review.json` for the supported comparisons and their limits.

Every primary note was indexed against the existing candidates. The closest
matches and selected high-value claims received statement-level comparison.
This is not a claim of mechanically deciding all mathematical equivalences.
Remaining novelty and dependency questions are explicitly part of pending
review; they are not certified new accepted results.

`intake.json` records source digests, edited-candidate digests, supporting-file
digests, and exclusion reasons. Import dates are not discovery or proof dates.
Private process material, prompts, chat exports, handoffs, working memory,
environments, caches, and downloaded reference papers are excluded. Mathematical
review annotations are retained separately from the historical approval protocol.
Original sources remain in the contributor's private workspace; no raw workspace
archive is included here.

## Computations

`computations/` contains supporting Python calculations and numeric/algebraic
witnesses. These include exact certificates and exploratory searches. Their
presence or a successful finite run is not an arbitrary-dimensional proof.
Selected exact checks rerun for this contribution are listed in `checks.json`.

Use a disposable checkout of this repository when running a search, since some
scripts write result files. Run with `assets/pk-nov6/computations/` as the working
directory; keep the sibling candidate files available for note-reading verifiers. Python
3.9 was the historical environment; packages used across the collection are
NumPy, SciPy, SymPy, mpmath, python-flint, and z3-solver. Not every script needs
all of them. See `requirements-computations.txt` for the recorded versions.
Machine-specific dependency paths were removed. Verifiers reading a mathematical
note use the corresponding candidate's proof through `submission_text.py`.

Validate the shared graph and this batch with:

```sh
python3 scripts/check_graph.py
python3 scripts/check_pk_nov6.py
```

These commands check records, references, hashes, and packaging. They do not
approve proofs or certify that the weak Oertel conjecture has been solved.
