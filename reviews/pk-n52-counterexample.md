# Review of the 52-integer-variable counterexample

Accepted fact: [df488edae05a1702](../facts/df488edae05a1702.md).
The [six-page writeup](../output/pdf/oertel-52-integer-variables.pdf) gives a
human-readable, self-contained proof; its
[LaTeX source](../assets/pk-continuation-2026-11/oertel-52-integer-variables.tex)
is included.

The result is a full-dimensional rational polytope with

    n=52, d=274784+2^61=2305843009213968736,
    sup_(y in S) depth_S(y) < 1/(e 2^52).

All nonempty integer fibers have full continuous dimension. This refutes
the particular constant `1/e` and the larger sharp `Gamma_d` constant. It
does not refute the repository's locked assertion that some smaller
positive absolute constant works. It is an intermediate improvement:
the continuous dimension is about 4.3 billion times smaller than in the
previous n=76 example, but remains much larger than a billion variables.

## What changes mathematically

The negative unit fibers are replaced by all nonempty negative Boolean
subsets of four blocks of size 13. Their mass is a binomial sum. An affine
facet envelope proves that overlapping negative subsets do not enlarge the
origin fiber. Every other integer base remains exposed. This increases the
mass surplus enough to reduce both the integer dimension and the common
simplex dimension. The sharper finite-dimensional estimate

    e Gamma_ell < 1+1/(2ell-1)

permits `ell=2^61` with the displayed exact parameters.

## Assurance and audit coverage

Two separate reviewing agents checked the construction and regenerated the
exact certificate. The recorded runs are
[9907fabb6176b207](../verifications/9907fabb6176b207.json) and
[fc9c9c64ab9bffa1](../verifications/fc9c9c64ab9bffa1.json).
The assurance is **LLM-verified**, not human review or Lean verification.
The existing Lean theorem covers the previous n=76 construction only.

| Audit | Checked conclusion |
| --- | --- |
| Lattice | Exact integer support; explicit exposure of every nonzero base; no additional integer points. |
| Actual fibers | Affine inequalities prove the origin fiber is exactly the assigned tetrahedron times box, including all overlapping-subset mixtures. |
| Measure and dimension | All fibers have full dimension and positive finite volume; their finite sum equals standard Euclidean Hausdorff measure. |
| Halfspaces | Four origin cuts cover every origin point. Finite exposing tilts isolate a simplex cap at every other actual point. All cuts are proper and closed. |
| Constants | Exact geometric margins, fourteen outward-rounded power traces, the exponential-series comparison, and the sharper padding estimate. |
| Uniformity | The maximum of two strict bounds controls every point, so the supremum itself is strictly below the target. |
| Dependencies | The accepted proof includes the entire nonstandard geometric lemma. No unproved completion, limiting argument, or conjecture is used. |

The final exposition was separately checked line by line and compiled to
PDF. It defines depth only for positive finite measure and distinguishes
the underlying exact exponentiation invariant from its stored intervals.

## Reproduction

From the repository root:

```sh
python3 assets/pk-continuation-2026-11/check_integer_dimension_52.py > /tmp/n52-certificate.json
cmp /tmp/n52-certificate.json assets/pk-continuation-2026-11/integer-dimension-52-certificate.json
python3 scripts/check_graph.py
```

The certificate program uses only the Python standard library and exact
integer/rational arithmetic. Its output records every rounded power step.
The graph checker checks records and dependency integrity, not mathematics.

The full Boolean-code geometric lemma is reproduced in the accepted proof.
Other exploratory routes are not premises of this theorem and are not
implicitly promoted to accepted facts.
