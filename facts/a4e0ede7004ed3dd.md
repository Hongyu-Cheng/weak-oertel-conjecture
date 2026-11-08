---
fact_id: a4e0ede7004ed3dd
kind: counterexample
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-sharp-homothetic-centroid-displacement-coefficient
depends_on: []
verifier_run: 77f3825e1cf40f54
target_match: null
---

## Source

- [af36a5fc25ebff84](../candidates/af36a5fc25ebff84.json), §4, (9)–(12).

## Statement

Let $d\ge1$, $T=\operatorname{conv}(0,e_1,\ldots,e_d)\subseteq\mathbb R^d$, $g=(1,\ldots,1)/(d+1)$, $K=T-g$, $v=-g$ and $V=|K|$. For $\rho>0,\delta\ge0$ the convex hull of the lifted copies $\rho K$ at bases $-1,1$ and $-\delta v+(\rho+\delta)K$ at base $0$ has precisely those three actual integer fibers. Its middle centroid is $(0,-\delta v)$, with $\gamma_K(-\delta v)=d\delta$, where $\gamma_K$ is the Minkowski gauge.

At $\delta=\rho/d$ a closed halfspace through this centroid captures zero endpoint volume. Hence no constant $D<d$ can replace $d$ in a universal endpoint-volume lower bound of the form $(1-D\delta/\rho)_+^d$ times a positive equal-pair budget, with $(t)_+=\max\{t,0\}$. More generally, for $0\le\delta\le\rho/d$ there is a through-point cap of total endpoint volume $\rho^dV[1-(1-2a)^d]$, where $a=(1-d\delta/\rho)/(d+1)$.

## Proof

Since $v\in K$, convexity gives $\delta v+\rho K\subseteq(\rho+\delta)K$, so $\rho K\subseteq-\delta v+(\rho+\delta)K$. The projection of the hull is $[-1,1]$, so the two endpoint fibers are exposed and unchanged. Every continuous coordinate in the hull belongs to the displayed middle body since it contains both endpoints and is convex. This proves the exact fiber at zero. The hull is full-dimensional by the positive-volume middle and the nonzero endpoint base.

The inequalities defining $K$ are $x_i\ge-1/(d+1)$ and $\sum_i x_i\le1/(d+1)$. For $-\delta v$ the coordinate lower bounds are automatic in all positive dilates of $K$, and the sum inequality first holds at dilation factor $d\delta$. For $\delta=0$ the gauge is zero. This gives the claimed gauge identity.

On $\rho K$ the barycentric coordinate of the vertex $\rho v$ is $\lambda(x)=1/(d+1)-\sum_i x_i/\rho$. At $-\delta v$ this affine form has value $a$. The ambient closed halfspace $\lambda(x)\le a(1+z)$ has boundary through the actual middle centroid and thresholds zero and $2a$ on the endpoints. The zero threshold picks out the opposite facet and has zero $d$-volume. For $0\le t\le1$, the region $\lambda(x)\ge t$ is the simplex homothetic about $\rho v$ with ratio $1-t$, so the endpoint sublevel at $t=2a\in[0,1]$ has volume $\rho^dV[1-(1-2a)^d]$. Boundary levels have zero $d$-volume.

When $\delta=\rho/d$, $a=0$ and the halfspace is $\sum_i x_i\ge\rho/(d+1)$. The endpoint mass is zero, whereas a coefficient $D<d$ would give a positive factor $(1-D/d)^d$. The cap branch specifies the mass of this explicit cap.
