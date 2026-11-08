# Lean verification of mixed-integer counterexamples

## Counterexample of total dimension 17

[`SharpOC.Selector17.sharp_oc_counterexample`](SharpOC/Selector17Counterexample.lean)
constructs a compact, full-dimensional convex body with $n=12$ and $d=5$
and positive finite mixed-integer mass. One uniform $0<r<(5/6)^5/2^{12}$
bounds the normalized mass of a proper closed halfspace containing each
mixed-integer point. Exterior points are covered by strict separation.

Lean checks the signed support census, every actual fiber, all cap and
body masses, and the strict comparison. The
[geometric proof and exact replay](../research/sharp-dimension-17/README.md)
give the rational construction.

| Modules | Verified content |
| --- | --- |
| Selector17Arithmetic, Selector17Bases, Selector17Lattice | Exact margins, signed base census, and exposure |
| Selector17Sources, Selector17SourceGeometry, Selector17Cap, SelectorSlabVolume | Source simplices and truncated cap volumes |
| Selector17Near, Selector17Body | Simplex neighbors, affine radius bound, and actual fibers |
| Selector17Cuts, Selector17Mass, Selector17Counterexample | Cut and body masses, uniform strict bound, and total dimension |

## Counterexample of total dimension 19

[`SharpOC.Selector.sharp_oc_counterexample`](SharpOC/SelectorCounterexample.lean)
constructs a compact, full-dimensional convex body with $n=14$ and $d=5$
and positive finite mixed-integer mass. It gives one uniform
$0<r<(5/6)^5/2^{14}$ such that every mixed-integer point belongs to a
proper closed halfspace of normalized mass at most $r$.

The proof identifies all $17{,}770$ nonempty integer fibers and computes
the actual sum of their Lebesgue volumes. It computes the masses of the
three cuts that cover the origin and the small fibers and of the
isolated simplex caps that cover the large fibers. Exterior points are
covered by strict separation. The [geometric proof](../research/sharp-dimension-19/README.md)
gives a rational polytope and the exact parameters.

| Modules | Verified content |
| --- | --- |
| SelectorArithmetic, SelectorBases | Exact counts and rational margins |
| SelectorLattice, SelectorRoof, SelectorBody | Exposure, integer census, exact fibers, and full dimension |
| SelectorSources | Simplex sources, containment, and relative volumes |
| SelectorMeasure, SelectorCuts, SelectorMass | Actual mixed-integer mass and covering halfspaces |
| SelectorCounterexample | Uniform strict bound and total dimension |

## Counterexample to the specific 1/e bound

[`SharpOC.BoxCounterexample.one_over_e_counterexample`](SharpOC/BoxMeasure.lean)
proves an unconditional counterexample with **n=76** and
**d=1372131+2^93**. It supplies an actual compact convex body with nonempty
ambient interior, containing the origin, whose nonempty integer fibers all
have full continuous dimension. Its actual mixed-integer Lebesgue mass is
positive and finite.

There is one positive real number `r < 1/(exp(1)*2^76)` such that every actual
mixed-integer point in the body belongs to a proper closed ambient halfspace
whose normalized mass is at most `r`. This uniform bound directly gives a
strict bound on the supremum of all point depths. It refutes the specific
constant `1/e`, and therefore also the larger sharp `Gamma_d` constant. It
makes no claim against the existence of a smaller positive universal constant.

The proof verifies the complete lattice census, exact fiber and cut volumes,
common simplex padding, and strict rational margins. The enormous powers are
handled by proved outward-rounded interval certificates, not floating-point
arithmetic or enumeration. [The formal audit](ONE_OVER_E_AUDIT.md) gives the
proof map, precise measure scope, and reproducibility details. The final
theorem is imported by `SharpOC.lean` and checked by `CheckAxioms.lean`.

## Earlier sharp-bound counterexample

The earlier final theorem is
[`SharpOC.Counterexample.sharp_oc_counterexample`](SharpOC/Counterexample.lean).
It proves the counterexample in the full-dimensional mixed-integer-volume
formulation, with continuous dimension **23** and integer dimension
**3 × 10^92**. The construction is the one in the
[direct rational counterexample note](../assets/pk-continuation-2026-11/direct-rational-sharp-oc-counterexample.md).

This theorem alone violates the sharp constant, not the specific `1/e` bound.

## What the earlier theorem proves

There is a compact convex body `C` with nonempty ambient interior, containing
the origin, whose nonempty integer fibers all have nonempty 23-dimensional
interior. Define its mixed-integer mass by the actual sum over **all** integer
coordinates:

```text
mixedIntegerMass D = ∑' z : IntegerCoordinate → ℤ,
                       volume {x | (cast z, x) ∈ D}.
```

This mass is positive and finite for `C`. There is one positive real number
`r < (23/24)^23 / 2^n` such that **every** mixed-integer point of `C` belongs
to a proper closed ambient halfspace whose normalized mass is at most `r`.
The theorem includes oblique halfspaces and closed boundaries. Its uniform
bound implies the strict bound on the supremum of halfspace depths, without
assuming that a deepest point exists.

[`sharp_oc_strict_violation`](SharpOC/Counterexample.lean) also states the
unnormalized strict inequality directly for every candidate center.
The integer-coordinate index is `Fin 3 × Fin (10000^23)`;
[`integerDimension_eq`](SharpOC/Constants.lean) checks the displayed dimension
exactly. All cardinalities are treated symbolically; the proof does not
enumerate that many coordinates or fibers.

The formal measure is counting measure over integer bases times ordinary
Lebesgue measure on `Fin 23 → ℝ`. This is the mixed-integer-volume version of
the sharp assertion. The final theorem does not additionally formalize the
identification with normalized Euclidean Hausdorff measure, or the rationality
of the polytope's vertices. Neither is an extra hypothesis in the verified
counterexample theorem. In particular, the default norm on Lean's finite
function space is not silently identified with the Euclidean norm.

## Reproduce the verification

The project pins Lean **4.34.1** and mathlib commit
`d13f23b723b8a846827a245b89c10fc7d3f11612`. With the Lean toolchain available:

```sh
cd lean
lake exe cache get
lake build
lake env lean CheckAxioms.lean
```

`CheckAxioms.lean` checks the final theorems for the counterexamples above
and their supporting results.
The final theorems depend only on the standard axioms `propext`,
`Classical.choice`, and `Quot.sound`. The build reports non-fatal style
and deprecation warnings from several modules.

See the [1/e audit](ONE_OVER_E_AUDIT.md) and [earlier sharp-bound audit](AUDIT.md)
for the precise statements and measure checks.
The existing fact graph's historical review records have not been relabeled
or rewritten by this addition.

## Earlier proof map

| Modules | Checked content |
|---|---|
| `Constants`, `FamilyCombinatorics` | Exact rational margins, cardinalities, source selection, and paid-index sums |
| `SourceGeometry`, `MiddleSimplex` | Chain simplices, determinant-to-volume bridge, centered middle simplex, and exact half-volume cuts |
| `SourceContainment`, `AffineSimplex`, `SourceBasis` | Actual source fibers, Minkowski containments, their volumes and full affine bases |
| `LatticeGeometry`, `BodyGeometry`, `ConcreteBody` | Complete integer census, exact origin and exposed fibers, compactness and nonempty interior |
| `SimplexCaps`, `Halfspaces`, `MiddleCuts` | Simplex cap volumes, finite isolation of exposed fibers, and all middle-fiber cuts |
| `MixedIntegerMeasure`, `CounterexampleMass` | Actual infinite fiber sum reduced to the proved finite support, total mass, and uniform small-cut bound |
| `Counterexample` | Complete existential counterexample and direct strict violation |
