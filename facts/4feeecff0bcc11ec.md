---
fact_id: 4feeecff0bcc11ec
kind: counterexample
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-pk-w36-coarse-no-heavy-supporting-face
depends_on: []
verifier_run: 8d731f98f2be51ed
target_match: null
---

## Source

- [e306d42187c98e53](../candidates/e306d42187c98e53.json), e306d42187c98e53:05 §6, (16)–(18), hollow rank-two face-mass obstruction.

## Statement

Let $Q=\operatorname{conv}\{(0,0),(2,0),(0,2)\}$ have barycentric coordinates $\lambda_0,\lambda_1,\lambda_2$. For $0<\varepsilon<1$ define the compact convex body in $\mathbb R^2\times\mathbb R^3$
$$
D_\varepsilon=\{(z,x):z\in Q,\ |x_i|\le\varepsilon+(1-\varepsilon)\lambda_i(z),\quad i=0,1,2\}.
$$
It is the hull of its actual mixed trace. The six integer bases are the three vertices and three edge midpoints. Their fiber volumes are $8\varepsilon^2$ and $2\varepsilon(1+\varepsilon)^2$, respectively. The Hausdorff limit $D_0$ is full dimensional, and all six limiting fibers have zero three-dimensional volume. A common fixed block normalization makes the bodies uniformly bounded and puts the unit ball inside each one. With summed coarse volume $M$, each projection edge has mass $M_{\rm edge}$ satisfying $M-2M_{\rm edge}=2\varepsilon(1-\varepsilon)^2>0$. No proper supporting face carries half the prelimit mass. The normalized weak limit puts probability $1/3$ on the uniform law on each edge-midpoint square and zero at the vertex fibers, so no proper supporting face carries more than $1/3$ of that limit law.

## Proof

All width constraints are affine inequalities when written with both signs. The box above $z$ equals the Minkowski combination of the three vertex boxes with coefficients $\lambda_i(z)$, since sums of axis-aligned centered intervals add their half-widths. This proves equality with the hull of the integer vertex fibers and hence with the hull of all actual integer fibers. The integer nonnegative pairs with coordinate sum at most two are $(0,0),(2,0),(0,2),(1,0),(0,1),(1,1)$, with no interior integer point. At a vertex the half-widths are a permutation of $(1,\varepsilon,\varepsilon)$. At an edge midpoint they are a permutation of $((1+\varepsilon)/2,(1+\varepsilon)/2,\varepsilon)$. Multiplying the three side lengths yields the two stated volumes.

The half-widths differ from their values at $\varepsilon=0$ by at most $\varepsilon$, so coordinatewise clamping to the limiting box changes each point by at most $\sqrt3\,\varepsilon$. Also $D_0\subseteq D_\varepsilon$. All three limiting widths are positive at a base interior to $Q$, giving an ambient interior point at its box center, where the inequalities remain strict in a neighborhood. Choose an ambient inball of $D_0$ with positive radius and translate and scale the entire family by its center and radius. This is a block-preserving affine map, and the common outer bound follows from the original bounded projection and widths at most one. At the six integer bases at least one limiting half-width is zero, so the full fiber volumes there vanish.

Each edge contains two vertices and one midpoint. Thus $M=24\varepsilon^2+6\varepsilon(1+\varepsilon)^2$ and $M_{\rm edge}=16\varepsilon^2+2\varepsilon(1+\varepsilon)^2$. Subtracting gives the asserted positive difference. Every proper supporting face is an edge or a vertex, and a vertex lies on an edge. The normalized weights tend to zero at vertices and to $1/3$ at each midpoint. The uniform law on each midpoint box is the pushforward of the uniform law on $[-1,1]^3$ by multiplying the coordinates by its half-widths. These maps converge uniformly to the projection and scaling onto the limiting square, which gives the asserted weak limit by continuity of bounded tests.
