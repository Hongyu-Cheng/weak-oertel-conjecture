---
fact_id: aa9f54bdeb89d4eb
kind: counterexample
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-equal-volume-level-sharp-central-enlargement
depends_on: ["388668713cd84c75"]
verifier_run: 9d5288235e6b6901
target_match: null
---

## Source

- [a1e40e6e6a2316e4](../candidates/a1e40e6e6a2316e4.json), a1e40e6e6a2316e4:02 §3, (4), and §5 fixed-radius section.

## Statement

For the square body of the singleton centroid-graph obstruction, fix $0<t<1$. Select any subinterval of length $t$ in each original corner fiber. Every convex set containing their lifts has length at least $1+2t$ in its central fiber at $(1,1)$, and this lower bound is attained by an appropriate choice and convex hull. In particular no convex body can induce such corner choices and have length exactly $t$ at the center. The same obstruction applies to a convex lift at a fixed radius whose horizontal section is required to have precisely these trimmed fibers.

## Proof

Use the four original corner intervals of the singleton centroid-graph obstruction. Each high-corner selected interval has upper endpoint at least $1/2+t$. The midpoint of its two upper endpoints lies over $(1,1)$ and is at least $1/2+t$. The low-corner lower endpoints similarly force a point at most $-1/2-t$ at the same base. Convexity forces the interval between those two points, giving the asserted length.

For sharpness use the two high intervals $[1/2,1/2+t]$ and the two low intervals $[-1/2-t,-1/2]$. At the center the corner representation has equal weights within each diagonal, and the two diagonal totals sum to one. The continuous values of their mixtures stay in $[-1/2-t,1/2+t]$ and include both endpoints. Thus the convex hull of these four lifts has central length exactly $1+2t$. Even if one also selects length-$t$ centered intervals at all edge midpoints and at the center, these stay inside that continuous range, so adding them to the hull does not enlarge the central fiber further. A fixed horizontal section of any convex lift is convex, hence it obeys the same lower bound and cannot have the required central length $t$.

For the particular nested homothetic trims centered on the original fiber centroids, the corner diagonals instead force a central interval $[-1-t/2,1+t/2]$ of length $2+t$, whereas the designated central trim has length $t$.
