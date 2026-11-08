---
fact_id: ca75a0eeed1fa283
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-pk-w34-circuits-triangle-radius-profile
depends_on: ["ba7d50004292d433", "700febf4b7a92759"]
verifier_run: 7725f2c8726f2fe0
target_match: null
---

## Source

- [e7fde0ecffd41ff1](../candidates/e7fde0ecffd41ff1.json), e7fde0ecffd41ff1:02 §4, exact radius profile and strict improvement via alternative active caps.

## Statement

Let $p_1=(1,0)$, $p_2=(0,1)$, $p_3=(-1,-1)$, $T=\operatorname{conv}\{p_1,p_2,p_3\}$, and $\gamma=4/9$. Use the central triangle $T$ at zero and $r_iT$ at $p_i$ for positive radii of mean one. These are actual integer fibers of a convex shared-plane body. Its exact normalized maximum depth is
$$
\frac{\max\{\gamma r_{\max}^2,\ \gamma+r_{\min}^2\}}{1+\sum_i r_i^2}.
$$
In particular the radii $(1-t,1,1+t)$ for $0<t\le1/4$ give $(13/9-2t+t^2)/(4+2t^2)<13/36$. The fixed original three-cap selection increases the cap budget on the expanded outer fiber. An alternative selection critical at $t=0$, with all three caps choosing the shrinking outer fiber, certifies the actual decrease with slack covers for the other outer fibers.

## Proof

The base census is that of ba7d50004292d433. The simplex vertex radii have an affine interpolant $r(z)$ with $r(0)=1$, and the three shared inequalities $u_j\cdot x\ge-r(z)$ for $u_1=(2,-1)$, $u_2=(-1,2)$, $u_3=(-1,-1)$ define precisely the desired positive fibers over $T$. Write $a=|T|$. The ordinary depth at the triangle centroid is $\gamma a$ by 700febf4b7a92759, using its three equal barycentric coordinates $1/3$. Every point has an own cap of at most $\gamma a$: cut at the value of a largest barycentric coordinate, at least $1/3$, so the corresponding homothetic cap has area at most $(2/3)^2a$. The scaled assertions hold on each $r_iT$.

For a closed through-cap at the central centroid, the central contribution is at least $\gamma a$. On the outer sites, use the common smaller triangle $r_{\min}T$ in each. Couple its three uniform points by cycling the barycentric coordinates of one uniform point, as in ba7d50004292d433. Their continuous sum is zero, their base sum is zero, and at least one of the three points lies in the cap. Thus the outer contribution is at least $r_{\min}^2a$. For the upper bound at any central mark, choose an own cap of at most $\gamma a$ and tilt to take the smallest outer fiber and exclude the other two. At each outer base its exact maximum is its ordinary triangle maximum, by the same exposing tilt restricted to isolate that base. These inequalities prove the formula. Tightening to the marked point handles containing caps, and a pure-base through-cap includes the whole central fiber in the lower-bound argument.

For the specified path, $\gamma+r_{\min}^2\ge4/9+9/16>\gamma(5/4)^2\ge\gamma r_{\max}^2$. Direct comparison with $13/36$ reduces to $2t-(5/18)t^2>0$. The original caps $10u_j\cdot z+u_j\cdot x\ge0$ retain strict outer full/empty allocations because $|u_j\cdot x|\le 2(1+t)<10$ on all fibers. The cap selecting $p_3$ has new normalized budget $(\gamma+(1+t)^2)/(4+2t^2)>13/36$. Instead use $10u_1\cdot z+u_j\cdot x\ge0$ for all $j$. They are all critical at the original center, each takes the shrinking outer fiber and the central barycentric cap, and their continuous sum cancels, so they cover the whole central and shrinking planes. At the other outer bases add the isolating circuits of their centroid barycentric caps; all their budgets are bounded by $\gamma r_{\max}^2a$, strictly below the new active budget. Thus this alternative selection covers the full measured set and certifies the stated actual decrease.
