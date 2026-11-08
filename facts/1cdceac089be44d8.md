---
fact_id: 1cdceac089be44d8
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-simplex-capacity-corrected-central-pair
depends_on: ["3e6e1eb15d927db8", "8bdcdcd6e2fa69d9", "27d3881f8bfc290c"]
verifier_run: 2453c42184a72bb6
target_match: null
---

## Source

- [a5d3d44181ebed82](../candidates/a5d3d44181ebed82.json), §§2–4, (6)–(8), (12), corrected direction.

## Statement

Let $d\ge2$ and let a strictly positive row $x$ have a proper minimizing threshold for the uniform-simplex capacity $\phi_d$. Normalize its threshold to one, let $c=\mathbf 1-x$, and set $P(c)=\Pr(\sum_j c_jE_j\ge0)$ for independent unit exponentials, $H=\nabla^2P(c)$, and $b$ equal to the actual barycentric section centroid. Suppose $c_i,c_j>0$ at distinct indices with $b_i,b_j\le1/d$. Put
$$
v=d b_j e_i-d b_i e_j,\qquad
w=v+\frac{\mathbf 1^\mathsf{T}Hv}{dP(c)}\mathbf 1.
$$
Then $w^\mathsf{T}\nabla^2\phi_d(x)w=-P(c)^{-1/d}v^\mathsf{T}Hv/(dP(c))>0$. Other margins may be zero and the two captured heights may coincide.

## Proof

The joint cap derivative lemma and threshold stationarity give $\nabla P(c)=dP(c)b$, so $v$ is tangent to $b\cdot c=0$. The centroid lies on the cut and, because the cut is proper, is interior to the simplex. Thus the cap is stationary among oriented planes through the point with barycentrics $b$. Apply the positive-pair calculation in accepted fact 27d3881f8bfc290c to this stationary cap: its exact pair vector is $v$, the required two barycentric coordinates are at most $1/d$, and the chosen vertices are strictly captured. That calculation gives $v^\mathsf{T}Hv<0$, including the equal-margin limit and other zero margins. The optimized-capacity square formula with $s=\mathbf 1^\mathsf{T}Hv/(dP(c))$ cancels the threshold penalty and proves the conclusion. Together with the strictly negative common-shift quadratic value in that formula, this supplies both signs at such a row.
