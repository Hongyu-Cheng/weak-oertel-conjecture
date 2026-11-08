# Independent review of PR #10

Reviewed on 7 November 2026 at commit
`f0c26255a21ced3ccec7266754371ca00bf5872a`. The PR snapshot was kept
unchanged. No GitHub action or graph-state change was made.

**No substantive mathematical gap was found.** The asymmetric construction
proves the sharp-bound counterexample at $(n,d)=(167,99)$, with total
dimension 266. It does not meet the current target $n+d<100$. The existing
local $(153,34)$ certificate already has smaller total dimension, 187.
The most useful addition from the PR is its asymmetric fan and exact
equalization of positive-fiber volumes.

## Scope and exact replay

The review read `CONTRIBUTING.md`, both complete simplex-join proofs,
the improved $n=52$ proof, the support obstruction, and the complete
generalized geometric lemma in accepted fact `df488edae05a1702`.
It checked the new proof arguments directly rather than treating existing
review verdicts as premises.

The six reproduction commands listed in the PR README were run on a
scratch copy, because several checkers overwrite adjacent JSON files.
Every command exited successfully.

| Checker | Reproduced result |
| --- | --- |
| `check_asymmetric_n167.py` | Exact geometry and scalar predicates pass |
| `check_sharp_join.py` | Original symmetric parameters pass |
| `join_audit_checker.py` | 1,035,123 exact predicates, including 57,288 positive-middle cases, pass |
| `check_improved_n52.py` | Rational parameter improvement passes |
| `check_improved_n52_independently.py` | Independent rational Taylor enclosure passes |
| `check_support_obstruction.py` | Exact obstruction premises pass |

`scripts/check_graph.py` also passed: 1,280 facts, 2,574 candidates and
1,340 verification runs. This establishes graph consistency, not proof
correctness. The three new graph submissions remain pending.

Four regenerated certificates were byte-for-byte identical to the PR
versions. The regenerated `join_audit_results.json` differed only in
`proof_sha256`: the stored file binds the earlier proof, while the amended
proof has SHA-256
`808b048e91aed89f99d4979caa7edfd25d5f0e9aeecf1facc6499bd6521b605a`.
The PR explicitly documents that amendment in `join_audit.md`, lines
131--139. The rerun now verifies that the arithmetic is unchanged. This
is a documented provenance distinction, not a mathematical defect.

The main asymmetric proof has SHA-256
`7e525d6965b25565b0db2ecc65f2ca18db86430c9459704f831af3ff086f4eb3`.
A separate direct transcription of its displayed rational parameters,
without importing either submitted checker, independently verified the
normal dependence, edge intersections, source determinants, contractions,
center directions, cone signs, origin-facet gaps and scalar inequalities.
Its decimal summaries are only for orientation:

| Quantity | Value |
| --- | ---: |
| $1+E-m$ | $0.00008676473469794835$ |
| Smallest of the three middle-cut margins | $0.00008593378807605921$ |
| Smallest negative origin-facet gap | $9.963676496384\cdot10^{-15}$ |
| Relative deficit from the sharp bound | $1.4036636073474688\cdot10^{-55}$ |

All acceptance comparisons used rational arithmetic, including the
strict lower bound $8/100000$ for the four mass margins.
The self-contained direct transcription is preserved as
[pr10-independent-n167.py](pr10-independent-n167.py), with its concise
[replay output](pr10-independent-n167.json). Run it with
`uv run pr10-independent-n167.py` from this directory; it uses only the
Python standard library. Its printed decimal values are summaries of
the exact rational assertions in the checker.

## Proof obligations independently checked

The coordinate-extremum argument excludes unlisted integer bases even
though negative subsets are truncated at size 30. A coordinate equal to
$-1$ forces every participating generator to be negative and to contain
that coordinate; each remaining integer coordinate then forces inclusion
or exclusion in every participating subset. The exposing functionals
uniquely expose every nonzero listed base, so all those actual fibers are
their prescribed fibers.

The affine facet prices correctly handle unequal types. At a positive
support $I$ of selected type $a$, the remaining lower bound is
$(\sum_{i\in I}\delta_{\operatorname{type}(i)}-\delta_a)
(o_j-10\varepsilon)\geq0$. At a negative support, the remaining bound is
$r[(\delta'_a-\delta_a)o_j-10(2-\delta_a-\delta'_a)\varepsilon]>0$.
These inequalities hold on the entire convex hull and establish that
the actual origin fiber equals the prescribed simplex. They do not rely
on regrouping overlapping subsets.

All four middle-cut incidence cases have the stated strict signs.
The identity $\sum_a f_a=0$ covers every point of the middle fiber,
including boundaries. At a noncentral simplex point, a barycentric
coordinate at least $1/100$ supplies the required cap. The centered
exposing tilt $a(x)+Q[h(z)-h(z_0)]\geq0$ preserves that cap and excludes
all other compact fibers for one finite $Q$. The mass bound is uniform,
so the argument proves a strict inequality for the supremum. The
positive-fiber centroid gives the claimed matching lower bound.

The improved $n=52$ specialization satisfies every hypothesis of the
accepted geometric lemma. Its continuous dimension is
$1,350,000,000,002,747,789$. The independent Taylor replay gives a positive
relative violation of at least approximately $1.07514\cdot10^{-21}$
against $1/(e2^{52})$. This is valid but irrelevant to the new total
dimension target.

The support obstruction and the equal-block sufficient-inequality
barrier are correctly scoped to the $1/e$ target. They do **not** exclude
a sharp $\Gamma_d/2^n$ counterexample with $n+d<100$ and must not be used
as such an obstruction.

## Reusable extension: asymmetric full negative cones

The rational contraction is useful independently of the PR's final
parameters. If the maximal source triangle has ratio
$\theta_a^{\max}$, contracting one ray at the common point sets its
ratio exactly to $\theta_a=m/(1+\delta_a)^d$. All positive fibers then
have exactly equal volume $m$, even with unequal block sizes and dilation
parameters. This avoids an exponentially amplified error in their total
mass.

The PR uses the same simplex $T_a$ for positive and negative fibers.
One can retain these positive simplices and replace the negative source
by the larger body
$P_a=B\cap\bigcap_{j\ne a}\{f_j\leq0\}$, taking
$G_{a,r}=(1-r\delta'_a)P_a-r t_a c_a$.
The origin-facet argument uses only $P_a\subseteq B$, and the cut-sign
argument uses only the missed-row maxima and the own-row minimum, which
are still zero. Thus both arguments survive unchanged.

Writing $\vartheta_a=|P_a|/|B|$, the new negative mass is
$E_a=\vartheta_a\sum_r\binom{N_a}{r}(1-r\delta'_a)^d$.
These negative fibers need not be simplices. Their exposed bases permit
isolating each whole fiber, so it suffices to check
$\vartheta_a(1-\delta'_a)^d<\Gamma_d m$ instead of constructing internal
caps. The same positive-simplex caps still handle positive fibers.

For the PR's exact planar fan, independent edge-intersection and area
calculations give:

| Type | Maximal positive triangle ratio | Full negative cone ratio | Enlargement |
| --- | ---: | ---: | ---: |
| 0 | 0.1381003827 | 0.2126282505 | 1.5396644552 |
| 1 | 0.1381535577 | 0.2120096140 | 1.5345939514 |
| 2 | 0.1395429340 | 0.2149279228 | 1.5402279182 |

This combines the PR's asymmetric equalization with the use of larger
negative fibers in the existing local construction. It is not a new certified
dimension pair: increasing negative mass also increases the middle-cut
cost, so the scalar parameters and block sizes must be reoptimized.
Neither the PR's failed local searches nor this extension proves any
global minimum or resolves $n+d<100$.
