---
fact_id: aaeb828dd89b9f5d
kind: counterexample
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-four-interval-midpoint-reflection-counterexample
depends_on: ["af8473f9cd095cf3"]
verifier_run: d5e46037119ec86a
target_match: null
---

## Source

- [1176a6cc970482b9](../candidates/1176a6cc970482b9.json), 1176a6cc970482b9:02 §§1–2, (1)–(5) and depth implication.

## Statement

The polygon $C=\operatorname{conv}\{(0,0),(3,0),(3,3),(2,10),(0,2)\}$ has exactly the integer fibers $I_0=[0,2], I_1=[0,6], I_2=[0,10], I_3=[0,3]$, of total mixed length $M=21$ and concave widths. The midpoint lower bounds $B_j$ and the actual reflection retentions at those midpoints both equal $(2,10,10,3)$, so their maximum is $10< M/2$. With the center allowed to vary over the actual mixed source, the per-base maxima are $(2,10,12,3)$ and the unique global maximizer is $(2,3)$, with retained fraction $12/21=4/7$. The normalized closed-halfspace depth at $(2,3)$ is at least $2/7$.

## Proof

The lower boundary is zero and the upper boundary has consecutive unit-step slopes $4,4,-7$, which give the stated actual fibers and concavity. The midpoint lower-bound formula gives $(2,10,10,3)$ by substitution. At a height $t$ write $f_{a,b}(t)=[\min(a,b,2t,a+b-2t)]_+$ for the intersection length of $[0,a]$ with $2t-[0,b]$, by the interval-overlap formula. The extreme bases have only their own overlaps, with maxima $2$ and $3$. At base $1$ the total is $f_{6,6}+2f_{2,10}$, and at base $2$ it is $f_{10,10}+2f_{6,3}$. Each sum is affine between its breakpoints. Their complete knot values are
$$
\begin{array}{c|l|l}
j& t& R(j,t)\\ \hline
1&0,1,3,5,6&0,6,10,6,0\\
2&0,\tfrac32,3,\tfrac92,5,10&0,9,12,9,10,0 .
\end{array}
$$
For the paired term the knots are the support endpoints and the half lengths of the two intervals. The self term adds its own midpoint. The table gives actual midpoint values and all maxima, including strict uniqueness at $(2,3)$. At that center the reflected intersection has mixed length $12$ and is symmetric about the center. Opposite closed through-center halfspaces have equal retained mass and together cover it. Every containing closed halfspace therefore sees at least $6$ of original mixed length, giving normalized depth at least $6/21$.
