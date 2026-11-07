# Lead review of twelve auxiliary claims in PR #4

Reviewed on 7 November 2026 against source commit `2ffd469d639402e465de448fb31dd920eaf7f40a`. These twelve files are unchanged from PR #4 at `e5bbd45e3cb073e1c030bcc9e07726881d2af8f0`.

The lead ChatGPT assistant read the complete statements and proofs, checked their nonstandard arguments and boundary cases, and found no substantive gap in the claims listed below. This is direct mathematical model review. It is not human review or proof-assistant certification. The accepted graph's original records are preserved.

## Shared-endpoint credit and higher-arity repair

### [69e7900bfbf7454b](../facts/69e7900bfbf7454b.md)

The threshold identity follows from the actual affine circuit, including the constant term in the continuous affine functional. Every high endpoint contains a homothetic support cap of volume equal to the *total* small-fiber mass. Either one high endpoint pays that whole budget, or every high threshold lies strictly beyond its witness and each distinct small endpoint pays its own credit. Thus reuse of a high endpoint never double counts its physical mass. The positive coefficient required for strictness follows from exclusion of the middle base. The statement's continuous-normal restriction and its separate warning about purely integer cuts are retained.

The candidate includes a draft heading and repeats the statement before its proof. The fact places those same hypotheses in its Statement section. This normalization does not omit a hypothesis.

### [ef6cc6d9e2fd4c8e](../facts/ef6cc6d9e2fd4c8e.md)

The two cones over a section have disjoint interiors and give the stated uniform projection-density bound, including the interval case. Combining that bound with the centroid inequality produces the strict support margin. Actual convexity puts each weighted Minkowski sum in the middle fiber; Brunn-Minkowski gives its volume and additivity of widths bounds the support loss. The preceding shared-endpoint lemma then gives the full retained mass bonus. The small-total-mass assumption pays purely integer cuts.

The displayed dimension-only constants, the retained-subbody variant, and the circuit reservoir on the stated slab bases were also checked. The sum of the listed high bases with the negative base is exactly the required multiple of the target base. These are conditional statements about explicitly supplied actual circuits, not assertions that such circuits always exist.

Its candidate/fact preamble normalization likewise retains every mathematical hypothesis.

## Nonlinear transfer and two-cut consequence

### [f0399a8f0bae48c6](../facts/f0399a8f0bae48c6.md)

For a fixed removed endpoint mass, concavity of the root function places the minimum at an endpoint, and the smaller-volume body is the minimizing endpoint. Brunn-Minkowski applies to the complementary strict caps by inner approximation. The resulting transfer is monotone in the middle cap mass. Distinct physical endpoint bases justify summation. Purely integer cuts contain the middle and at least one whole endpoint per reflected pair, so this case is not omitted. The full-credit threshold and largest-core versus middle-centroid comparison are algebraically valid under their stated assumptions.

### [3e766d73edff42b0](../facts/3e766d73edff42b0.md)

Under the contradiction hypothesis, both small caps are evaluated against the original measure. Each successive middle remainder stays full-dimensional because the second cut passes through its centroid. Convexity preserves the midpoint inclusion of the endpoint remainders, including zero-volume cases. The two removed caps cannot pay the lower bound forced by the remainder volume. The compact upper-level-set argument supplies an actual deterministic middle point.

The equal-endpoint specialization uses the necessary midpoint-volume restriction. Its rational margins and the two comparisons at dimension 50 were checked with exact fractions. The comparison with pending candidate `660db01ed45063dd` was checked against that candidate's displayed formulas; that pending work is not used to prove the new bound. The accepted metronoid input `6769574fc1bd9f8d` was read and includes the full-mass centroid case used here.

## Contact geometry and exact realizations

### [1269c554ca9a41b8](../facts/1269c554ca9a41b8.md)

The local active-cap representation is proved in the appendix rather than assumed from a pending note. Outside the finite base skeleton, a diverging base tilt would partition the finite bases and produce a through-point cap of mass below the depth level. This gives a bounded normalized local constraint family. The interior-ball condition makes the cone of active normals closed and permits the separation argument. Decomposing its continuous-normal dependence into minimal positive circuits yields at most `d+1` caps, with nonzero projected sum because of the same strict interior margin.

The cap derivative requires the explicitly stated zero tangency-section measure. Proper traces admit the two-sided derivative; other allowed traces contribute only a smaller-order slab volume. Differentiating at an active cap determines the entire mixed section centroid, including integer coordinates. The projected-facet obstruction follows from positivity of the circuit coefficients. The strictly convex/nonresonant corollary has the necessary exclusions for integer dimension one and continuous dimension one. No unrestricted regularity of a lattice-free container is inferred.

### [1a16e89734914fc8](../facts/1a16e89734914fc8.md)

The projected lattice census and strict exposure of every nonzero base are exact. For the origin fiber, the base equations account for each negative weight as the sum of the positive-subset weights using that coordinate. The resulting continuous expression is a convex combination of points of the middle body. The spatial assumption, rather than small volume alone, gives the required higher-subset inclusions.

For the constructed cuts, paid indices are suppressed by one sufficiently large finite tilt. Unpaid higher subsets have a strict support gap from the centroid-ball radius. Unit fibers may meet a supporting hyperplane but have zero continuous volume there. The exposed-fiber identity uses a single ordinary cap plus a finite exposing tilt, not an intersection of halfspaces.

The final bad-fan transfer is conditional on a strictly bad fan. Shrinking supplies strict missed-source gaps while retaining the bad margin; replication produces small positive-volume outer balls without altering their total mass. The finite fan covers the origin, and the other fibers have the exact stated ordinary depth. No actual bad fan is asserted in this auxiliary theorem.

## Reflection ledger and canonical directions

### [a93e9443922f47dc](../facts/a93e9443922f47dc.md)

Reflection preserves volume and pairs actual distinct endpoints, proving the lower certificate. Tonelli and the dilation substitution give its exact integral. Translation continuity and compactness give attainment. The explicit triangle construction meets the spatial assumptions of the preceding completion theorem. Its source regions are confined to barycentric coordinates greater than `9/20`, so at most two source types contribute at any point. The rational bound is strictly below `2/5` off the zero-overlap region; the middle centroid attains `2/5`.

This disproves sufficiency of the additive reflection *lower certificate*. It gives no upper bound on actual mixed depth and is not an Oertel counterexample.

### [0a2cae17f9154570](../facts/0a2cae17f9154570.md)

The pair-credit argument respects the affine midpoint threshold and arbitrary integer tilt. The first determinant budget uses row Hadamard and the arithmetic-geometric mean bound on row sums of a column-stochastic matrix. The second uses an existing good row and a determinant-preserving replacement by the all-ones row. The inverted-simplex volume argument supplies that good row under its stated parameter restriction.

Chebyshev and Jensen give the weighted score inequality. The low- and high-dimension parameter estimates were checked, including the monotonicity of the auxiliary exponential function. Continuous strictly decreasing score functions allow one point to satisfy every canonical-direction threshold. The separate one-dimensional argument gives both continuous orientations. The higher-dimensional result continues to concern only the specified canonical directions; it is not promoted to an all-direction theorem.

## Exact scalar cross-checks

A separate standard-library `fractions.Fraction` calculation verified the positive rational margins used in this review, including:

| Comparison | Exact positive margin |
| --- | --- |
| Low-dimensional fan correction above `1/200` | `2371/55800` |
| `79/200 - (7/8)^7` | `120801/52428800` |
| `693^3 - 2^28` | `64377101` |
| Two-cut equal-endpoint polynomial margin | `1165/29282` |
| Reflection-certificate margin below `2/5` | `533/12000` |
| Reflection source-support margin | `1/300` |

Both `(50/51)^50 > 37/100` and `(50/51)^50 < 3/8` were also verified as exact rational comparisons. These finite computations supplement the arguments above; they do not replace the dimension-general proofs.


## Four further auxiliary claims

### [6fbefd0eb6914aa9](../facts/6fbefd0eb6914aa9.md)

For a simplex cut by one halfspace, the vertex list is exhaustive. After row scaling and sign changes, every candidate barycentric determinant becomes a weighted reduced incidence determinant. A nonzero determinant is therefore exactly a spanning tree. Adding a missing root edge and removing the first edge of the old path strictly increases the product, so a maximizing tree retains all surviving positive vertices. Each negative vertex then attaches independently to a maximum-height vertex. This proves both the exact capacity and attainment.

The zero-height case follows by decreasing compact intersections and convergence of maximizing vertex tuples. The centroid capacity uses the appropriate arithmetic-geometric mean inequality with the number of negative heights. The dimension-four scalar obstruction and the joined two-cut example were checked, including the distinction between maximizing among vertices and requiring a simplex to contain an extreme vertex. The latter cannot be retained in a qualifying source in the displayed dimension-four example. None of these auxiliary obstructions is presented as an Oertel counterexample.

### [0352fdc455eb4c54](../facts/0352fdc455eb4c54.md)

The two missed-row inequalities give the stated quadrilateral in barycentric coordinates. Maximizing the triangle determinant at its vertices yields exactly the four displayed capacities. If the only candidate omitting the surviving original vertex were strictly best, it would have area ratio less than the product of the other two center coordinates. That product is strictly below one quarter. This proves the retained-vertex assertion at the required threshold, including equality.

The one-cut capacity formula supplies the double-hit representatives, which retain the two original positive vertices for their hit rows. The full triangle realizes the all-hit pattern. Consequently the seven-pattern replacement preserves each complete strict hit pattern and its weight; it does not combine separately incompatible cut optimizers.

### [bc2e100f7f34422f](../facts/bc2e100f7f34422f.md)

Positive row dependence and the centroid condition place the three positive vertex values in different columns. The quadrilateral capacities rule out qualifying singleton sources, so the total hit fraction is at least two. During the middle-volume increase, the maximum score stays at least one half, while any row that could increase has its endpoint cap score strictly below one half. This proves the monotonicity of the maximum without assuming equal cap costs.

The sector triangles preserve the individual strict patterns at the new volume. After positive row rescaling, interpolation with the canonical Laplacian keeps row and column sums zero and preserves rank by the maximum principle. Its imbalance parameter decreases, so every own-cap score decreases. The displayed surplus is valid within the stated centroid sign cone; the proof does not extend it to arbitrary centers or all halfspaces.

### [b8c4471bc5e549c3](../facts/b8c4471bc5e549c3.md)

Under a hypothesized failure of the target, the largest core centroid forces the aggregate core deficit below the outside mass. The per-parity assumption prevents an outside source with a good partner from having an outside midpoint. Bad-partner and bad-target losses each have the stated separate bound; the latter uses the explicit hypothesis and is not inferred from convexity.

At a retained target the physical endpoints are distinct. Homothetic clipping selects precisely the needed retained mass without changing the actual source, and the depth and volume assumptions of the cited one-sided local-star theorem hold with the displayed constants. Purely integer cuts are paid by the middle fiber. Averaging the separately certified candidate depths yields the claimed strict surplus. The total-smallness corollary correctly eliminates bad targets in the failure regime. This review checks application of the local-star theorem; its proof is separately covered by the continuation reviewer.
