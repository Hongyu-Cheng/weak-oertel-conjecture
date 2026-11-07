# Review of the n=76 counterexample to the specific 1/e bound

Accepted fact: [a5291bca09ba4b1e](../facts/a5291bca09ba4b1e.md).
The full proof combines the [four-source construction](../assets/pk-continuation-2026-11/barycentric-box-source-counterexample.md)
with its [smaller-padding parameter choice](../assets/pk-continuation-2026-11/integer-dimension-76-counterexample.md).

The result is an explicit full-dimensional rational polytope with
`n=76`, `d=1372131+2^93`, and

    sup_(y in S) depth_S(y) < 1/(e 2^76).

Every nonempty integer fiber has full continuous dimension. The main note
also proves the result with simpler parameters at `d=1372129+2^94`.
These finite constructions refute the specific constant `1/e` and hence
the larger sharp `Gamma_d` constant. They do not refute the repository's
locked assertion that some smaller positive absolute constant works.

## Review method and scope

A separate mathematical reviewer audited the full proof and both parameter
sets. A source-geometry co-developer cross-reviewed the assembled main proof
and the arithmetic. The latter is supplementary review, not a claim of
independence from the construction. The corresponding records are
[fc2660c15e2e4299](../verifications/fc2660c15e2e4299.json) and
[a6331a0b149a4528](../verifications/a6331a0b149a4528.json).
Both record `LLM-verified` assurance through the fact ledger; neither
constitutes human review or proof-assistant certification.

| Audit | Checked conclusion |
| --- | --- |
| Measure | Finite, positive fiber volumes; their sum equals normalized Euclidean Hausdorff measure; product factors and total mass are exact. |
| Actual points | Every actual point is treated in its own integer fiber; no center rounding or surrogate point is used. |
| Halfspaces | Four proper closed ambient cuts cover the entire origin fiber; finite exposing tilts isolate simplex caps at every other fiber. Boundary cases are included. |
| Lattice | The only integer bases are the cube vertices and negative units. The origin fiber is proved by convex regrouping, and all other bases are exposed. |
| Dimension | The body and every nonempty fiber have full dimension. All dimensions and generating families are finite. |
| Constants | Both exact parameter tables satisfy every geometric inequality and strict scalar margin; the exponential-series and simplex-padding bounds are proved. |
| Circularity | No conjectural centerpoint theorem, source inequality, or completion principle is assumed. |
| Limits and supremum | No limiting body or maximizing point is needed: two uniform upper bounds have a maximum strictly below the target. |
| Arithmetic | The reviewer reproduced both certificates and independently replayed all 42 rounded-power trace rows for the main parameters. The interval enclosure invariant is proved. |

One harmless intermediate display was corrected during review: in the
paid-core estimate the integer contribution is **at most** `-R+k-1`,
with equality possible when `k=1`. The total remains at most `2k-R<0`.
No parameter or conclusion changed.

## Reproduction

From the repository root, run:

```sh
python3 assets/pk-continuation-2026-11/check_barycentric_box_source_counterexample.py
python3 assets/pk-continuation-2026-11/check_integer_dimension_76.py
python3 scripts/check_graph.py
```

The arithmetic programs use only Python integers and `fractions.Fraction`.
They enclose large powers by outward rounding with a proved invariant;
they do not numerically approximate `e` or optimize parameters. The graph
checker validates metadata and dependencies, not the mathematical proof.

The intermediate constructions and amplification barriers are indexed in
the [continuation registry](../assets/pk-continuation-2026-11/README.md).
They remain supporting research notes rather than separate accepted facts.

## Lean scope

The [existing Lean development](../lean/README.md) verifies the earlier
`d=23`, `n=3*10^92` counterexample to the sharp constant. Its build and
standard-axiom audit passed before this contribution. No Lean source is
changed here. In particular, **the n=76 counterexample and the refutation
of the specific 1/e bound are not yet Lean-formalized**.
