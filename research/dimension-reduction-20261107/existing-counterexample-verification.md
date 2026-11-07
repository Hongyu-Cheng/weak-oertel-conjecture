# Direct verification of the starting counterexamples

Checked on 7 November 2026. The initial source snapshot was main
`5cc4e76e3823c6622819fa77c2a7bf4c1586dba0`; main subsequently advanced to
`635ad260847e3a986502dd54cb465a614e77ce5b` through the integration audit.
The mathematical n=52 witness was unchanged by that update.

## Scope and verdict

The lead assistant read the complete proof of accepted fact
`df488edae05a1702` and the earlier direct sharp construction, replayed their
exact arithmetic, and found no mathematical gap in the n=52 argument.
The n=52 example refutes the particular constant 1/e, and hence also the
larger sharp constant Gamma_d. It does not refute the repository's target
of some smaller positive absolute constant independent of n and d.

This is a mathematical review and executable exact-arithmetic replay.
The lead did not rerun Lean during this dimension-reduction task. The
repository's n=76 and original d=23 formalizations have their own recorded
Lean audit; the n=52 result and the new dimension-reduction results should
not be described as Lean-formalized.

## Geometry checked directly

1. The positive cube and block-negative Boolean generators have exactly
   the stated integer projection. At any integer coordinate -1, convexity
   forces every used generator to have that coordinate -1; the remaining
   integer coordinates then force the same Boolean subset. Every nonzero
   listed base is exposed by the stated signed small-coefficient functional.
2. The origin fiber is exactly B0 times the free box. The four barycentric
   lower inequalities and both inequalities for every box coordinate hold
   on every generator. At the zero base they define precisely the prescribed
   middle fiber. This handles overlapping negative subsets and arbitrary
   balanced convex combinations, rather than only pairwise midpoints.
3. The affine constants in the negative fiber formula are correct:
   t_r-(t_r+r-1)=1-r. For a nonselected barycentric coordinate its minimum
   is r(delta_t/4+t epsilon); for the selected coordinate it is
   1/4-3rt epsilon. These give exactly the two required facet inequalities.
4. Each middle cut strictly excludes all positive Boolean fibers, strictly
   excludes all negative fibers outside its paid block, and includes every
   negative fiber in its paid block. Its middle cap has fraction 27/64.
   The four middle cuts cover all middle points because their continuous
   defining functions sum to zero. Closed boundaries are handled correctly.
5. The total fiber volume is b[(2^52-1)m+1+E]. All noncentral fibers are
   exposed and have volume at most mb before padding. A simplex cap can be
   isolated at one such base by a sufficiently large *finite* exposing tilt.
6. The common simplex factor has dimension 2^61. The bound
   e Gamma_ell < 1+1/(2ell-1) follows from
   log(e Gamma_ell)=integral_0^1 t/(ell+t) dt < 1/(2ell)
   and exp(x)<1/(1-x). Together with the exact surplus and middle-cut
   margins this supplies one strict uniform bound for every point.
7. All actual fibers have the full stated continuous dimension. The finite
   fiber-volume sum agrees with standard-normalized Hausdorff measure on
   their disjoint Euclidean affine subspaces.

## Executed checks

All assertions in the following source programs passed:

- `assets/pk-continuation-2026-11/check_integer_dimension_52.py`;
- `assets/pk-continuation-2026-11/check_integer_dimension_76.py`;
- `assets/pk-continuation-2026-11/check_direct_rational_sharp_oc_counterexample.py`.

The fresh n=52 and n=76 results and direct-source certificate are stored in
this directory. A wrapper initially assumed that the direct d=23 script
printed JSON, while that script prints a text verdict and saves a JSON
report. The wrapper was corrected to collect its `report` object; the
underlying mathematical assertions had passed on both executions.

The newly merged `scripts/check_one_over_e_independently.py` was also run.
It uses rational log/exp Taylor enclosures, separately from the original
binary-power interval implementation. It passed all three recorded cases:
n=76 original, n=76 improved, and n=52. Its output is
`independent-existing-witness-replay.json`. In particular its certified
n=52 relative gap is greater than 1.4749400343e-19.

The n=52 powers are enclosed using only integer rounding and rational
arithmetic; the independent replay uses a different exact enclosure method.
The enormous dimensions therefore do not arise from a floating-point
roundoff error. They arise from the small effective-count surplus and the
finite-dimensional gap between Gamma_ell and 1/e.
