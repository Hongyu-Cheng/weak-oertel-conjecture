# Independent audit of the 132-by-99 sharp-bound example

Verdict: the simplified construction in `sharp-triangle-join.md` passes this independent mathematical and exact-arithmetic review. The reviewed parameters are `n=132`, `d=99`, `N=44`, `a=63/100`, `delta=329/10000`, `epsilon=10^(-13)`, with negative subsets of sizes `1,...,30` and negative fibers `G_(j,r)=(1-rDv)T_j`. The conclusion is a strict violation of `Gamma_99/2^132`. Neither a `1/(e2^132)` violation nor both dimensions below 100 has been established. This is an LLM review, not formal verification or an accepted fact-graph entry.

## Source geometry and centers

I independently enumerated the vertices of the planar source using every pair of its five boundary lines. The feasible vertices are exactly `e_0`, `(1,1-a,0)/(2-a)`, `(1,1,1)/3`, and `(1,0,a)/(1+a)`. Determinants of its two triangles, of the selected positive triangle, and of the origin cap give exactly the three volume ratios in the proof. Appending the free identity columns preserves these ratios in dimension 99. The free face is included when the sum of the first three coordinates is zero, so the normalized-triangle argument loses no points.

The proposed center is strictly inside the positive simplex. Writing `Q=1-a+a^2`, its weights on `e_0`, the equal-coordinate triangle point, `(1,0,a)/(1+a)`, and the free vertices are respectively

    epsilon/a,
    3/D-3a epsilon/Q,
    epsilon(2a-1)(1+a)/(aQ),
    1/D for each free vertex.

These weights are positive, sum to one, and reconstruct `p+epsilon(1,-a,-(1-a),0,...,0)/Q` exactly. Its three row scores are `(2epsilon,-epsilon,-epsilon)`. The independent checker verifies all these identities over rational numbers.

## Actual fibers and all-point cuts

The projected integer census is correct even though only negative subsets up to size 30 are generated. Once an integer projection has coordinate `-1`, its representation uses only negative Boolean generators. An integer convex combination of Boolean vectors can only use one identical vector, so no unlisted negative subset is introduced. All nonzero listed bases are uniquely exposed by the given functionals.

The origin proof controls every convex representation, including overlapping negative subsets. In centered coordinates the positive-fiber barycentric minimum is bounded below by `-delta/D-(k-delta)a epsilon/Q`. Adding the affine roof term `kv` leaves exactly `(k-1)delta(1/D-a epsilon/Q)>=0`. On the negative fiber, homothety about the simplex centroid gives `lambda_l>=rv`. Therefore every generator obeys the same affine facet system, and its restriction at integer base zero is precisely `B`. This proves the actual origin fiber equals the prescribed simplex, not merely that the generators meet a sufficient pairwise condition.

For each covering row, a positive subset meeting its paid block has strictly negative total score: the continuous bound is `(1+delta)+2epsilon(k-delta)<k+1`, and the integer bound is less than `-R+k-1`. If the subset misses the block, its score is at most `[k eta-k+delta]epsilon<0`. An unpaid negative fiber has nonpositive continuous row score and strictly negative integer score. A paid negative fiber is wholly included. Thus every origin cut has exactly the mass stated, and the three cuts cover all of the actual origin fiber because their continuous functions sum to zero.

Every positive fiber is an actual 99-simplex, so its largest-barycentric-coordinate cap has relative mass at most `Gamma_99`. Its exposing integer functional isolates that cap with a sufficiently large finite coefficient, including boundary points. Every negative fiber, though nonsimplicial, is exposed and can be isolated in its entirety; its whole mass is below `Gamma_99 M`. An integer-only isolating halfspace may contain its entire fiber on its boundary, which is valid for the stipulated closed halfspaces and is accounted for in the mass.

Full ambient dimension follows from the middle fiber and the positive unit bases. Identifying the centered sum-zero coordinate space with `R^99` by any rational basis yields the claimed rational polytope; the common linear volume conversion cancels in every normalized mass. All nonempty fibers have dimension 99, so the finite fiber-volume sum gives the intended Hausdorff-measure normalization.

## Independent exact checks

`alternative-join-audit-check.py` uses only rational arithmetic. It checks the planar vertices, all three determinants, center reconstruction, the positive facet identity for every `k=1,...,132`, the strict positive-cut inequalities, positivity of all negative scales, and the three required mass margins. They are strictly positive exactly; their decimal values, for orientation only, are

    total surplus:       0.0008855953574570216,
    origin cut margin:   0.000803702148111982,
    negative mass gap:   1.1660699933505152.

The exact checker passed. No mathematical gap was found in the reviewed statement or proof. No existing fact or graph file was altered by this audit.
