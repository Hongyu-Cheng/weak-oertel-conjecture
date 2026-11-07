# Lean verification of the sharp-bound counterexample

The final theorem is
[`SharpOC.Counterexample.sharp_oc_counterexample`](SharpOC/Counterexample.lean).
It proves the counterexample in the full-dimensional mixed-integer-volume
formulation, with continuous dimension **23** and integer dimension
**3 × 10^92**. The construction is the one in the
[direct rational counterexample note](../assets/pk-continuation-2026-11/direct-rational-sharp-oc-counterexample.md).

This project formalizes only that counterexample and the lemmas it needs.
It does not assert a counterexample to the weak absolute-constant conjecture.

## What the theorem proves

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

The complete build and final axiom checks passed on 7 November 2026.
The final theorem depends only on the standard axioms `propext`,
`Classical.choice`, and `Quot.sound`. No admitted proofs, extra axioms, or
native-evaluation proof shortcuts are used. The build currently reports
non-fatal style/deprecation warnings from several modules.

See [the audit](AUDIT.md) for the precise statement and measure checks.
The existing fact graph's historical review records have not been relabeled
or rewritten by this addition.

## Proof map

| Modules | Checked content |
|---|---|
| `Constants`, `FamilyCombinatorics` | Exact rational margins, cardinalities, source selection, and paid-index sums |
| `SourceGeometry`, `MiddleSimplex` | Chain simplices, determinant-to-volume bridge, centered middle simplex, and exact half-volume cuts |
| `SourceContainment`, `AffineSimplex`, `SourceBasis` | Actual source fibers, Minkowski containments, their volumes and full affine bases |
| `LatticeGeometry`, `BodyGeometry`, `ConcreteBody` | Complete integer census, exact origin and exposed fibers, compactness and nonempty interior |
| `SimplexCaps`, `Halfspaces`, `MiddleCuts` | Simplex cap volumes, finite isolation of exposed fibers, and all middle-fiber cuts |
| `MixedIntegerMeasure`, `CounterexampleMass` | Actual infinite fiber sum reduced to the proved finite support, total mass, and uniform small-cut bound |
| `Counterexample` | Complete existential counterexample and direct strict violation |
