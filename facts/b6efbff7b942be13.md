---
fact_id: b6efbff7b942be13
kind: counterexample
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-square-cone-facet-distance-obstruction
depends_on: ["d73a38134e47a4d2"]
verifier_run: 89dddc482c3170a2
target_match: null
---

## Source

- [e70b63e0e6efe01c](../candidates/e70b63e0e6efe01c.json), e70b63e0e6efe01c:05 §6, (16)–(18), nonsimplicial path calibration.

## Statement

Let $Q=\{(X,Y,T):T\ge|X|,\ T\ge|Y|\}$ and $v_s=(s,0,1)$, $|s|<1$. For the normalized cone Laplace minimum $J_*$,
$$
J_*(v_s)=\min_{-1<t<1}\frac{8(1+st)^3}{(1-t^2)^2},\qquad
J_*(v_0)=8,\qquad J_*(v_{8/13})=\frac{10368}{2197}.
$$
The ratio between the last two path values is $1296/2197$. Any product of distances to three distinct facets has ratio in $\{1365/2197,845/2197,3549/2197\}$ along the same two marks. Thus no fixed proportionality to such a product holds.

## Proof

Reflection in $Y$ and uniqueness of the normalized minimum force the $Y$-coefficient to be zero. For a remaining normal $(b,0,a)$ with $a>|b|$, slicing at height $T$ and integrating gives
$$
J_Q(b,0,a)=\int_0^\infty 2T e^{-aT}\int_{-T}^T e^{-bX}\,dX\,dT
=\frac{8a}{(a^2-b^2)^2}.
$$
For $b\ne0$ evaluate the two exponential integrals separately; at $b=0$ the formula is continuous. Set $t=b/a$; normalization gives $a=1/(1+st)$. The resulting objective diverges at both endpoints. Its logarithmic derivative vanishes when $s t^2+4t+3s=0$. At $s=0$ the minimum is $t=0$; at $s=8/13$ the only critical point in $(-1,1)$ is $t=-1/2$, yielding the stated values. The four fixed facet-distance ratios are $1-s,1+s,1,1$; multiplying any three and inserting $s=8/13$ gives the three listed rational values.
