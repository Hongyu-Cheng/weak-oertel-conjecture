# Sharp counterexamples of total dimension 187

This submission supersedes the dimension bounds in
[PR #10](https://github.com/Hongyu-Cheng/weak-oertel-conjecture/pull/10).
It gives explicit rational polytopes with the following dimensions.
Here $\Gamma_d=(d/(d+1))^d$.

| Bound refuted | $n$ | $d$ | Total dimension |
| --- | ---: | ---: | ---: |
| $\Gamma_d/2^n$ | 153 | 34 | **187** |
| $\Gamma_d/2^n$ | 132 | 82 | 214 |
| $\Gamma_d/2^n$ | 129 | 104 | 233 |
| $1/(e2^n)$ | 52 | 1,345,226,000,000,000,003 | 1,345,226,000,000,000,055 |

**The target $n+d<100$ remains unresolved.** The small sharp-bound
examples satisfy the weaker $1/(e2^n)$ bound. None of these results
refutes the repository's locked assertion that some positive absolute
constant works. The proofs are analytic, with exact rational checks and
independent model reviews; they are not Lean-formalized.

## Results and proofs

The [sharp counterexample fact](../../facts/ad3e63c52f083457.md) uses
simplex joins for the positive fibers and larger nonsimplicial negative
sources. Every positive fiber has a simplex cap; each negative fiber is
small enough to isolate in its entirety. The
[complete construction](sharp-triangle-join.md) proves the exact integer
census, all actual fibers, and cuts at every mixed-integer point.
Its worked example is $(132,99)$; Section 6 gives the three improved
tradeoffs above. The maximum depth is exactly
$\Gamma_d m/[(2^n-1)m+1+E]$ for the specified rational $m,E$.

The [compressed $1/e$ counterexample](../../facts/cbe1f4518f7088a7.md)
replaces the free box of the accepted $n=52$ example by a simplex.
This one factor supplies both volume amplification and caps, eliminating
separate padding and lowering the old continuous dimension by about
41.66%. See the [replacement lemma and exact parameters](compress-simplex-factor.md).

The [support-count theorem](../../facts/30b899ae9d94a523.md) proves
maximum depth at least $\Gamma_d/F$ for $F$ positive-volume fibers.
A strict $1/e$ counterexample on the old $n=52$ support therefore needs
$d\ge68,727,866,368$, regardless of fiber shapes. Its
[short proof](support-count-obstruction.md) distinguishes this obstruction
from the sharp-bound and total-dimension objectives.

## Review evidence

The [final publication review](publication-review.md) binds the final
proofs and candidate statements to their hashes. The corresponding
verification records use the repository's `LLM-verified` assurance.
Earlier review notes are retained as history; statements that a result
was outside the fact graph describe its status when those reviews ran.

- Sharp construction: [independent geometry review](alternative-join-audit.md),
  [independent geometry checker](alternative-join-audit-check.py), and
  [separate review of every tradeoff](verify-sharp-pareto.md).
- Compressed construction: [independent review](verify-compressed.md),
  including a different exact binomial-series enclosure.
- Original witness: [independent verification](verify-current.md).
- PR #10: [full review](pr10-review.md) and a
  [standalone rational replay](pr10-independent-n167.py). No substantive
  mathematical gap was found in its $(167,99)$ result; its total dimension
  266 is superseded by the results here.

The [balanced-family obstruction](compress-family-barrier.md) is retained
because the compressed certificate also checks its exact constants.
It is scoped to that construction family and is not a general lower bound
on counterexample dimensions.

## Reproduction

From the repository root, all of the following use the Python standard
library. The sharp checkers regenerate their adjacent JSON certificates.

```sh
python3 research/dimension-reduction-2026-11-07/sharp-triangle-join-check.py
python3 research/dimension-reduction-2026-11-07/sharp-triangle-join-pareto-check.py
python3 research/dimension-reduction-2026-11-07/alternative-join-audit-check.py
python3 research/dimension-reduction-2026-11-07/compress-certificate.py
python3 research/dimension-reduction-2026-11-07/pr10-independent-n167.py
python3 scripts/check_graph.py
python3 scripts/check_pk_parity_core.py
```

The graph checker validates records, links, dependency closure, and
verification hashes. It does not verify mathematics. The new proofs and
certificates are separate from the existing pinned Lean development.
