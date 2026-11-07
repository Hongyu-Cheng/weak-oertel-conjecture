# PK contributions — November 6, 2026

This batch shares our partial work toward the sharp Oertel bound, adapted to this
repository's **weak-conjecture target**. The accepted fact graph and problem
statement are unchanged. The additions are **pending mathematical submissions**:
results, conditional arguments, obstructions, and supporting computations, with
known qualifications preserved. Historical audits are not new approvals.

## Suggested starting points

- **A fixed-support obstruction, and an explicit escape by creating fibers.**
  [Five interval fibers](candidates/dcd790485c83acdc.json) with widths (13,11,9,7,5)
  have normalized maximum depth 11/30 and form a strict local minimum under compatible
  endpoint changes on fixed support, modulo affine changes of the center graph and
  positive fiber scaling. Adding two zero-mass fibers and growing them at coordinated
  rates gives an actual strictly lower depth. This distinguishes fixed-support
  deformation from support augmentation; it is not a universal descent theorem.

- **When a new fiber can be added without changing the old ones.**
  [The preserving-extension test](candidates/f66dcff3eb3e1f03.json) expresses
  compatibility through finitely many extreme barycentric representations.
  A four-interval example shows that a global cap cover does not ensure such an
  extension exists. [Mass-parametrized birth formulas](candidates/8b9ef51c1503d49a.json)
  track covariance and smoothed cap responses under explicit compatibility assumptions.

- **Profile localization and exact scalar subproblems.**
  [Finite-knot inverse-arm replacement](candidates/a260044e1f85011a.json) preserves the
  cap, coarea, and moment records at finitely prescribed slopes in the
  horizontal-tangent homothetic-profile problem. The [affine-cone
  inequality](candidates/6146c77d1d7c5e08.json), [planar affine-frustum
  dual](candidates/d28e829ed5b07592.json), and [all-dimensional lower frustum
  dual](candidates/c7808043ad51b327.json) supply exact auxiliary inequalities. The last
  is only a lower dual; these notes do not close the general-profile or mixed-integer
  argument.

- **Signed variation versus nonnegative capacity.**
  In the attained positive-width outward-smoothed model with d=2, [replicated triangle
  guards](candidates/b4250d3425f93191.json) obstruct a proposed nonnegative-field
  payment mechanism and show that the universal individual-source best-menu floor 1/3 is
  sharp when integer dimension varies. [Signed affine
  rebates](candidates/a78d27235a5a2dff.json) escape that particular obstruction in the
  same specified model. These constrain deformation strategies and do not contradict
  either conjecture.

- **Density repair with precise limitations.**
  [Variable-density barycentric selection](candidates/93c94ac2c5c85584.json) preserves
  the specified marginals while controlling output density. [Intrinsic parity
  repair](candidates/1972e280d049f336.json) also preserves endpoint parity submarginals
  and, in its marked version, the old conditional midpoint means given mark and parity;
  it does not preserve conditional endpoint laws. Convex order alone does not give
  halfspace order or a common mixed-integer center.

- **Geometric estimates and a restricted sharp regime.**
  For d>=2, [the simplex roof inequality](candidates/5e5b642b770e6623.json) gives a
  sharp directional roof-integral bound at fixed subbody volume. For n>=1,d>=2, [small
  mass outside a complete parity core](candidates/ff31d56304dd901a.json) gives the sharp
  Oertel bound when the outside mass is at most rho_d times the smallest chosen
  core-fiber volume, where rho_d>0 is independent of n. It does not establish that
  hypothesis for arbitrary bodies.

## Navigation and overlap handling

The [full topic index](assets/pk-nov6/INDEX.md) covers the remaining submissions;
[intake conventions](assets/pk-nov6/README.md) explain notation, review status,
dependencies, computations, and provenance. Mathematical corrections from older
reviews are linked to the affected candidates.

We reuse existing graph results for depth attainment, barycentric transport,
median reflection, graph Helly bounds, and equal-volume fibers. Covered arguments
were omitted or replaced by citations; additional refinements were retained.
The [overlap report](assets/pk-nov6/overlap-review.json) records these comparisons
and distinguishes detailed mathematical review from broader retrieval screening.
Novelty and dependency questions in the remaining intake still need review
before any claim enters `facts/`.
