---
fact_id: d07b9afdcf6b86f6
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-pk-w34-variation-concurrent-upper-volume-tightening
depends_on: []
verifier_run: 1f39c316b8d1e0a4
target_match: null
---

## Source

- [d2f8ecd6d2f1309c](../candidates/d2f8ecd6d2f1309c.json), d2f8ecd6d2f1309c:01 The reduction, assertions 1–4 and common-level proof.
- [d2f8ecd6d2f1309c](../candidates/d2f8ecd6d2f1309c.json), d2f8ecd6d2f1309c:02 Consequence for overlap inequalities, transfer and proper-cap equality.

## Statement

Let $K\subset\mathbb R^d$ be a convex body of volume $V$. Let the nonzero normals $u_i$, $1\le i\le m$, have rank $m-1$ and a dependence $\sum_i\rho_i u_i=0$ with every $\rho_i>0$. Suppose the closed caps $H_i=\{x:u_i\cdot x\ge b_i\}$ cover $\mathbb R^d$ and every $A_i=|K\cap H_i|$ is in $(0,V)$. There is a unique $t_*\in(0,\max_i A_i]$ at which moving the thresholds to give volumes $A_i'=\min(A_i,t_*)$ makes the planes concurrent. These caps are contained in the originals, remain proper, and cover $\mathbb R^d$. For every real $r<m$,
$$
\sum_i A_i'-r\min_i A_i'\le \sum_i A_i-r\min_i A_i,
$$
strictly if the original planes were not concurrent.

In particular, for $0\le r\le m-1$, a bound $\sum_i A_i-V\ge r\min_i A_i$ for every concurrent proper cover of $K$ with the given normals implies the bound for all whole-space closed covers with those normals, including zero and full caps. Equality for an original proper cover requires concurrency. The coefficient $r=m-1/\gamma_d$ with $m=d+1$ and $\gamma_d=(d/(d+1))^d$ lies in this range.

## Proof

The map $U:x\mapsto(u_i\cdot x)_i$ has image $\rho^\perp$ by its rank and the dependence. The original closed cover is equivalent to $\rho\cdot b\le0$. If this inequality holds, no vector in the image is strictly below $b$ in all coordinates. If it fails, $b-c(1,\ldots,1)$ with $c=(\rho\cdot b)/\sum_i\rho_i>0$ belongs to the image and is strictly below $b$. Concurrency is exactly $\rho\cdot b=0$.

In each direction the cap volume is continuous in the threshold because hyperplanes have zero volume, and strictly decreases across the full support interval. Indeed every open slab between two distinct thresholds in that interval meets the body interior and contains positive body volume. Thus the proper mass inverse $Q_i:(0,V)\to(\min_K u_i\cdot x,\max_K u_i\cdot x)$ is continuous, strictly decreasing, and tends to the upper support level at mass zero. For $0<t\le\max_i A_i$, the sum $\sum_i\rho_i Q_i(\min(A_i,t))$ is continuous and strictly decreasing in $t$, since a largest original mass changes strictly on this range. At the largest original mass the sum is nonpositive by the cover condition. As $t\downarrow0$ it tends to $\sum_i\rho_i h_K(u_i)>0$: an interior point has strictly smaller height than every $h_K(u_i)$, and its weighted height sum is zero. Thus the unique root has positive mass. At the root all thresholds are at least their original values, and the image characterization gives concurrency and coverage.

Write $a=\min_i A_i$. For $t\ge a$ the functional of the new volumes equals $\sum_i\min(A_i,t)-ra$, strictly increasing on $[a,\max_i A_i]$ whenever that interval is nondegenerate. For $0<t\le a$ it equals $(m-r)t$, strictly increasing as well, and the values agree at $a$. This gives the displayed comparison. The root equals the largest original mass exactly when the original planes were concurrent.

The comparison transfers the hypothesized bound to proper covers and gives its stated equality condition. A zero cap makes the desired inequality the union bound. If one cap has full mass $V$, subtract that mass. The other $m-1$ masses sum to at least $(m-1)\min_i A_i$. For the specified coefficient, $1\le 1/\gamma_d\le d+1$: equality on the upper side holds for $d=1$, and for $d\ge2$ the binomial estimate gives $(1+1/d)^d<e<3\le d+1$.
