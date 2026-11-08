---
fact_id: cb4b0dae6cd6a2e7
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-finite-interval-chain-rational-piecewise-affine-depth
depends_on: []
verifier_run: 9618a9bf2e78a472
target_match: null
---

## Source

- [942427a6ff06c7e1](../candidates/942427a6ff06c7e1.json), Proof §6, finite rational chamber reduction.

## Statement

At fixed consecutive integer bases $0,\ldots,N$, on the compatible endpoint domain of positive interval fibers $[l_i,h_i]$, the maximum raw actual closed-halfspace depth is a continuous piecewise-affine function of all endpoints, with finitely many cells and rational coefficients.

## Proof

For $N=0$ the maximum is half the width. Otherwise fix $p$ and $y\in[l_p,h_p]$. For the upper orientation use the clamp expression
$$
F(t)=\sum_i\min\{h_i-l_i,\max(0,h_i-y-t(i-p))\}.
$$
For the lower orientation use $M-F(t)$, where $M=\sum_i(h_i-l_i)$. They are affine in $t$ between the finitely many knot slopes $(l_i-y)/(i-p),(h_i-y)/(i-p)$ for $i\ne p$, with constant far tails. Their separate minima $U(y),L(y)$ are therefore finite minima of continuous piecewise-affine functions of $y$ and the endpoints with rational coefficients. One may also include the two tail values as explicit candidates. The far-tilt caps keep exactly the outside side fibers of the corresponding through-point pure base cap and only the proper own subinterval, so pure base caps cannot lower the minimum $\min(U,L)$. Translation to a through-point boundary treats every other containing cap.

As $y$ increases in its own interval, every upper-oriented candidate at fixed tilt loses at least the own length change and every lower-oriented one gains at least that much. Taking their infima preserves these bounds, so $U$ strictly decreases and $L$ strictly increases, each at rate at least one in absolute value. At $y=l_p$, a supporting line to the convex piecewise-linear lower roof gives lower mass zero, so $L(l_p)=0$. At $y=h_p$ use a supporting line above the concave upper roof to get $U(h_p)=0$. At extreme bases these supporting slopes can be chosen as finite one-sided roof slopes. The other minimum at each endpoint is at least the positive own width. Thus the unique crossing lies in the open own interval and maximizes $\min(U,L)$.

Subdivide the feasible joint $(y,\text{endpoints})$-domain into the finitely many closed affine cells of both functions. On each cell with crossing points, the equation $U=L$ solves for $y$ by an affine formula with a nonzero rational slope coefficient. If a cell has empty interior in the $y$-direction, use the formula from an adjacent full-dimensional clamp/minimum cell, whose affine function extends continuously to the shared boundary. Equivalently one can use a finite rational polyhedral refinement of the joint formula on the full domain of ordered endpoints and $l_p\le y\le h_p$; the slope bounds hold for all ordered endpoints before imposing compatibility. Substituting the crossing formula into its cell inequalities gives a rational polyhedral chamber in the endpoint space. These finitely many chambers cover the compatible endpoint domain and agree on overlaps by uniqueness. Their crossing values therefore give a continuous finite piecewise-affine restricted maximum. The maximum over the finite set of bases preserves those properties.
