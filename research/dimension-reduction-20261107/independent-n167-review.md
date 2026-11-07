# Independent model review of the (167,99) construction

Review date: 7 November 2026. Verdict: no mathematical gap found.
This note records the separate low-dimensional geometry reviewer's result;
it is not a human review or a Lean certificate.

Reviewed proof: `sharp-n167-d99.md`.
Reviewed proof SHA-256:
`e0e169a6d758efc89ebab26a101411806ced7a1d7e34e4b9f7d25207dcc8c939`.
The proof was not modified by the reviewer.

The reviewer reran `check_asymmetric_n167.py` and also recomputed the exact
geometry and inequalities independently from the displayed parameters,
without importing that checker. The independent record is
`low_d_audit_n167.json`.

## Checks and conclusions

- The source contraction gives exactly theta_a=m/(1+delta_a)^99, so all
  positive fibers have exactly the same volume mb. Unequal type frequencies
  introduce no hidden total-mass discrepancy.
- The row weights are positive and their weighted normals sum to zero.
  The displayed rational edge intersections, cap ratios, source determinants,
  contracted-source cones and center directions were independently checked.
- At a positive Boolean support of selected type a, the facet-price margin
  is exactly (sum_I delta_type-delta_a)(o_j-10 epsilon)>=0.
- The negative-fiber facet gaps are positive, with minimum approximately
  9.963676496384e-15. The affine inequalities control every balanced
  combination and establish the actual origin fiber.
- The coordinate-extremum census excludes all unlisted negative supports.
  The stated exposing functionals uniquely expose every nonzero listed base.
- The unpaid positive score is epsilon[delta_a-sum_I(1-eta_type)]<0.
  Paid positive supports and both negative cases also have the required
  strict signs. The closed cuts cover every middle point.
- The noncentral fibers are simplices, and their caps can be isolated by
  finite exposing tilts. The resulting bound holds uniformly at every point.
  A positive-fiber centroid gives the matching lower bound.

All four volume margins were independently compared exactly against
8/100000. Their decimal values are recorded in the main certificate and
independent JSON record. The reviewer also independently verified
U_a+V_a<6. The author's checker originally verified only the weaker
sufficient positivity of 3/100-epsilon(U_a+V_a); the explicit stronger
assertion was then added to make its checks match the proof's wording.
No change to the proof or its mathematical parameters was required.

The result is a counterexample to Gamma_99/2^167. The same exact comparison
shows its normalized coefficient exceeds 24/65>1/e, so it does not refute
1/e. Only d<100 is achieved. Neither minimality of n=167 nor the failure
of the weaker universal-constant conjecture is asserted.


## Review amendment: centered exposing functional

The reviewer checked the amended endpoint-cap paragraph in Section 6.
The current proof SHA-256 is
`7e525d6965b25565b0db2ecc65f2ca18db86430c9459704f831af3ff086f4eb3`;
the original reviewed hash above is retained.

The explicit ambient halfspace is now
`a(x)+Q[h(z)-h(z_0)]>=0`, where `a(x)>=0` is the chosen simplex cap
and `h` exposes its integer base `z_0`. This is correct: at `z=z_0`
the additional term is zero, so the cap is unchanged. At every other
integer base the exposing gap is strictly negative; finitely many compact
fibers permit a single finite positive `Q` making all their scores strictly
negative. The cap functional is nonconstant, so the resulting halfspace is
proper and closed. This makes the previously implicit threshold adjustment
explicit. The review verdict is unchanged. No arithmetic was rerun for
this textual amendment.
