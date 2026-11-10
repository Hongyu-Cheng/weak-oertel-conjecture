# Formal counterexample audit

The result checked here is a counterexample to the **sharp** mixed-integer
Grünbaum bound, with continuous dimension `23` and integer dimension
`3 * 10^92`. It does not refute the weaker absolute-constant conjecture.

The final theorem is
[`SharpOC.Counterexample.sharp_oc_counterexample`](SharpOC/Counterexample.lean).
It supplies a compact, convex body with nonempty ambient interior, containing
the origin, and a positive real number `r < (23/24)^23 / 2^integerDimension`.
For **every actual mixed-integer point** in the body, it supplies a nonzero
ambient continuous linear functional and a closed halfspace containing that
point whose normalized mixed-integer mass is at most `r`.
[`sharp_oc_strict_violation`](SharpOC/Counterexample.lean) also gives the strict
unnormalized violation directly.

## Source-level checks

| Issue | Checked proof interface |
| --- | --- |
| Actual convex body | [`body_is_convex_body`](SharpOC/ConcreteBody.lean) proves compactness, convexity, and nonempty interior for the constructed convex hull. |
| No extra or enlarged integer fibers | [`origin_fiber_exact`, `fiber_exact`, and `integer_point_mem_body_iff`](SharpOC/ConcreteBody.lean) prove exact fibers and the complete integer-base census. The origin argument explicitly regroups all convex combinations. |
| Genuine Lebesgue volume | [`volume_chartSimplex`](SharpOC/SourceGeometry.lean) proves the determinant formula in 23 coordinates. [`SourceContainment`](SharpOC/SourceContainment.lean) proves the actual source, contraction, scaling, and translation volumes. |
| Equal core masses | [`K_real_volume`](SharpOC/CounterexampleMass.lean) proves that every nonzero cube fiber has the same mass `M`; the middle and outer fibers retain their distinct, explicitly computed masses. |
| Every ambient halfspace direction allowed | [`exposed_simplex_fiber_sum_mass`](SharpOC/Halfspaces.lean) lifts a simplex cap to an actual nonzero ambient continuous linear functional, strictly excluding every other fiber. No restriction to vertical or horizontal cuts is made. |
| Closed-boundary mass | [`positive_cap_volume`](SharpOC/MiddleSimplex.lean) proves exact half-volume using a measure-preserving barycentric transposition and zero volume of the nonzero functional's kernel. Endpoint caps use exact closed-set homothety identities in [`SimplexCaps`](SharpOC/SimplexCaps.lean). |
| Every candidate center | [`every_fiber_point_small_cut`](SharpOC/CounterexampleMass.lean) covers every indexed fiber; [`point_has_small_halfspace`](SharpOC/Counterexample.lean) passes through the integer-base census to every actual point. |
| Exact total and cut accounting | [`totalMass_eq`, `middle_cut_mass`](SharpOC/CounterexampleMass.lean), and [`mixedIntegerMass_body_cut_toReal`](SharpOC/MixedIntegerMeasure.lean) prove the formulas. Finiteness is established before converting extended nonnegative reals to reals. |
| Exact strict constant | [`strict_depth_ratio`](SharpOC/Constants.lean) and [`depthBound_lt_sharp`](SharpOC/Counterexample.lean) use exact rational inequalities, with no numerical approximation. |

The coordinate type is `Fin 3 × Fin copies`, of the proved cardinality
`integerDimension`; this is a finite coordinate presentation of the integer
lattice. Transformations in the source-volume calculations act on continuous
coordinates. They do not silently change the integer lattice. All nonempty
integer fibers are proved to have nonempty 23-dimensional interior.

## Measure scope and limits

`mixedIntegerMass D` is defined as the sum, over **all** integer base vectors,
of the canonical 23-dimensional Lebesgue measures of the corresponding slices
of `D`. The reduction to finitely many fibers is a theorem, not a definition
that ignores other slices. This is the full-dimensional mixed-integer-volume
formulation of the conjecture.

The default norm on the Lean coordinate functions is the sup norm. The volume
used is canonical Lebesgue volume, not Hausdorff measure for that norm. The
formalization does not claim an identification with normalized Euclidean
Hausdorff measure. The construction uses rational coordinates, but a separate
formal theorem asserting rationality or rational polyhedrality is not included.
Neither additional statement is needed for the mixed-integer-volume theorem.

## Reproduction and logical dependencies

With the pinned toolchain and dependencies installed, run from this directory:

```sh
lake build
lake env lean CheckAxioms.lean
```

[`CheckAxioms.lean`](CheckAxioms.lean) recursively checks the final theorem and
key interfaces. The only permitted axioms are Lean's standard `propext`,
`Classical.choice`, and `Quot.sound`; the check rejects a dependency on `sorry`,
custom axioms, or native evaluation axioms. A model audit of the source found no
unproved geometric assumptions, circular appeal to the conjecture, or
substitution of abstract mass hypotheses for the constructed body.
