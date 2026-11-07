# PK contributions — November 6, 2026

This guide covers the initial intake and its subsequent research continuation.
The repository's **weak-conjecture target** is unchanged. Initial imported notes
remain pending; new continuation facts have separate independent model reviews.
Historical audits are not new approvals, and model review is not human or
proof-assistant certification.

## Latest continuation: read these first

- **The specific 1/(e*2^n) bound now fails with n=76.** The
  [four-source construction](assets/pk-continuation-2026-11/barycentric-box-source-counterexample.md)
  and its [smaller-padding parameters](assets/pk-continuation-2026-11/integer-dimension-76-counterexample.md)
  give a full-dimensional rational polytope with d=1372131+2^93.
  Every actual mixed-integer point admits a closed ambient halfspace strictly
  below 1/(e*2^76) of the total mass. Barycentric box sources and a common
  continuous simplex factor replace the earlier enormous integer dimension.
  [Fact a5291bca09ba4b1e](facts/a5291bca09ba4b1e.md) has a complete proof,
  exact rational certificates, and independent mathematical review.
  This is not yet Lean-formalized and does not refute the existence of a
  smaller positive universal constant.

- **An explicit counterexample to the sharp constant.** The
  [self-contained proof](assets/pk-continuation-2026-11/direct-rational-sharp-oc-counterexample.md)
  constructs a full-dimensional rational polytope with d=23 and n=3*10^92.
  Every mixed-integer point has a closed ambient halfspace of mass strictly
  below Gamma_23*2^(-n) times the total. It specifies all fibers and proves
  that convexification creates no unintended integer fibers. This is
  [fact 022a26fa5001480a](facts/022a26fa5001480a.md), reviewed independently
  in three separate model runs with exact rational checks. Its
  [Lean formalization](lean/README.md) now certifies the actual body,
  integer fibers, mixed-integer measure, and uniform sharp-bound violation.
  This earlier example alone does not violate 1/(e*2^n).

- **A stronger positive theorem for triangular parity cores.** In d=2,
  a complete parity core of triangular fibers satisfies the sharp bound
  when outside mass is sufficiently small in each parity class, uniformly
  in n. The new [two-scale proof](assets/pk-continuation-2026-11/two-scale-triangle-parity-core-repair.md)
  removes the earlier intermediate-target incoming-load assumption. It uses
  a proved all-direction triangle source center and actual reflected-pair
  payments; the hypotheses on the core are still essential to the theorem.

- **Mechanisms and their exact limits.** The
  [continuation registry](assets/pk-continuation-2026-11/README.md) records the
  local-star, parity, source-capacity, and oblique-cut results. Failed scalar
  bridges are accompanied by exact certificates. The sharp counterexample
  has a direct proof with no dependency on those auxiliary results.

## Initial pending intake: suggested starting points

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
