# Formal audit: the specific 1/e bound

The unconditional theorem
[`SharpOC.BoxCounterexample.one_over_e_counterexample`](SharpOC/BoxMeasure.lean)
certifies a counterexample with integer dimension **76** and continuous
dimension **1372131+2^93**. This is the smaller-padding parameter choice in
[fact a5291bca09ba4b1e](../facts/a5291bca09ba4b1e.md).

## Exact final statement

The theorem provides an actual compact convex body `C` with nonempty ambient
interior, containing the origin. It proves that the actual mixed-integer mass

```text
mixedIntegerMass D = ∑' z : IntegerCoordinate → ℤ,
                       volume {x | (cast z, x) ∈ D}
```

is positive and finite for `C`. Every nonempty integer fiber has nonempty
interior in the whole continuous coordinate space. There is one real number
`0 < r < 1/(exp(1)*2^76)` such that, for every integer vector `z` and continuous
vector `x` with `(cast z,x) ∈ C`, there are an ambient continuous linear
functional `F ≠ 0` and a real threshold `t` satisfying

```text
t ≤ F (cast z,x)
mixedIntegerMass (C ∩ {p | t ≤ F p}) / mixedIntegerMass C ≤ r.
```

The displayed real-valued ratio uses `ENNReal.toReal` after proving positivity
and finiteness. Cut masses are finite by containment in `C`. Thus the theorem
neither divides by zero nor uses `toReal` at infinity to manufacture a bound.
The fixed `r` also bounds the supremum of all point depths strictly below the
target; existence of a deepest point is not required.

## Dependency map and checks

| Modules | Verified content |
| --- | --- |
| `BoxParameters`, `BoxPowerCertificates`, `BoxArithmetic` | Exact rational parameters, outward-rounded rational power certificates, positive mass defect, origin-cut margin, and the strict finite simplex-padding bound |
| `TetrahedronVolume`, `BoxSources` | Ordinary tetrahedron volume; barycentric box sources; all required interiors, source volumes, closed cap volumes, and grouped containment for all source types |
| `BoxFree`, `BoxFamily` | Free-coordinate boxes, their grouped containment, 76 integer coordinates in four groups of 19, selected source types, exactly 19 paid outer fibers |
| `BoxBody` | Actual convex hull; compactness, convexity, ambient interior; exhaustive integer-base census; exact origin and exposed fibers; every nonempty fiber full-dimensional |
| `BoxCuts` | Four nonzero ambient linear cuts cover the origin fiber, strictly exclude every other cube fiber, and include precisely the paid outer fibers |
| `BoxPadding` | Actual product with a full-dimensional simplex; nonzero ambient exposed-fiber cuts; exact closed cap-volume factor |
| `BoxMeasure` | Actual all-integer measure reduced using the proved census; positive finite total; exact cut masses; one uniform all-point bound; final theorem and numeric dimensions |

The coordinate index `Fin 4 × Fin 19` is a finite presentation of the ordinary
76-dimensional integer lattice. Continuous product coordinates have total
dimension `3+1372128+2^93`. Integer coordinates are never changed by a
non-lattice-preserving transformation. The extra simplex is a genuine common
continuous factor, not an average over surrogate fibers or centers.

The origin fiber is checked by regrouping every convex representation;
convexification cannot silently enlarge it. Every other integer base is
exposed and has its assigned fiber. The census is an iff about all integer
vectors. It is not an assumption that the listed fibers are the only ones.

The cuts are closed halfspaces of the full ambient space. Their normals may
couple integer and continuous coordinates. The origin cuts include complete
paid fibers; no boundary mass is discarded. Simplex caps are proved using
exact closed-set homotheties, and the finite exposing tilt excludes all other
fibers strictly. Each actual mixed-integer point is covered deterministically.

## Constants and certificate generation

Write `m` for the common nonzero cube-fiber volume divided by the origin-fiber
volume, and `alpha` for the analogous outer-fiber ratio. The proved bounds are

```text
1458094201550/10^12 < m     < 1458094201551/10^12
   6027739233/10^12 < alpha <    6027739234/10^12
m/2^17 < 1+76*alpha-m
27/64+19*alpha < m/exp(1).
```

For `ell=2^93`, the proof shows
`exp(1)*(ell/(ell+1))^ell < 1+1/ell` and compares this directly with the
strict positive mass defect. No limit or asymptotic estimate replaces the
finite-dimensional inequality. The final numerator is the maximum of the
two bounds, so strictness holds uniformly over all candidate centers.

[`generate_box_power_certificate.py`](../scripts/generate_box_power_certificate.py)
reproduces `BoxPowerCertificates.lean`. Its output is checked by Lean's kernel;
the Python generator is not trusted. Each rational interval product and its
rounding direction is proved using ordinary Lean tactics. There are no
`native_decide` steps. The final axiom check recursively detects any unproved
or nonstandard dependency, including one in a generated certificate.

## Measure scope

The verified measure is counting measure over integer bases times canonical
Lebesgue measure on the continuous real coordinates. It is the
full-dimensional mixed-integer-volume formulation of the
[problem statement](../problem_statement.md). The final
statement does not additionally formalize an identification with normalized
Euclidean Hausdorff measure, or the rationality of the polytope's vertices.
Neither is an extra hypothesis needed for this counterexample. In particular,
Lean's default sup norm is not silently substituted for the Euclidean metric
in a Hausdorff measure identity.

## Reproduction and review

The project pins Lean 4.34.1 and mathlib commit
`d13f23b723b8a846827a245b89c10fc7d3f11612`. From `lean/`, run:

```sh
lake build
lake env lean CheckAxioms.lean
```

Both commands passed on 7 November 2026. The final theorem and key interfaces
depend only on `propext`, `Classical.choice`, and `Quot.sound`.
`CheckAxioms.lean` rejects every other axiom. Independent agent audits of the
assembled theorem checked the actual body and measure, quantifiers, dimensions,
closed cuts, strict constant, and recursive axiom output. This records machine
verification and model audits, not human review.

The fact's proof and its model-review records are unchanged; the Lean proof
is an additional check. It refutes the particular constant
`1/e` (and hence the sharp `Gamma_d` constant), not the existence of some
smaller positive absolute constant in the repository's weak conjecture.
