---
fact_id: cbbc6cf5cdc1604e
kind: counterexample
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-critical-cap-noncoverage-on-three-nonheavy-disks
depends_on: ["dec855d1498a4e64"]
verifier_run: 7271dcd713e28fa3
target_match: null
---

## Source

- [0c18dc829db98d22](../candidates/0c18dc829db98d22.json), 0c18dc829db98d22:03 §6, (4)–(5).

## Statement

Let $T$ be a centered disk of area one and radius $\rho$. The convex hull of $A=T/2$, $K=T$, and $B=11T/10$ lifted to bases $-1,0,1$ has exactly these three integer fibers. With summed planar area the total mass is $M=123/50$, and the three masses $1/4,1,121/100$ are strictly below $M/2$. The unique global maximizer of ordinary raw closed-halfspace depth is $(0,0)$ and its depth is $3/4$. The complete critical menu is
$$
u\cdot x+\alpha z\ge0,\qquad u\ne0,\qquad \alpha\le-(11\rho/10)\lVert u\rVert .
$$
It covers exactly $A$, $K$, and $\partial B$ on their respective fibers. Thus it omits relative mixed area $121/246$ even though every cap has a proper own cut and all its supporting traces have zero $\mathcal H^1$ measure.

## Proof

The endpoint Minkowski average is $4T/5\subset K$. Any convex combination of lifted points at base zero with nonzero endpoint coefficients is a convex combination of that average and middle points, because the coefficients of the two endpoint bases coincide. Thus the middle fiber is exactly $K$ and the endpoint fibers are unchanged. The base interval contains only the three stated integer sites. The mass and strict quotas follow from the squares of the homothety scales.

A nonvertical cap through the middle center has the displayed margin with arbitrary $\alpha$. Its central area is $1/2$. Let $A_{\rm cap}$ and $B_{\rm cap}$ denote its endpoint traces. Reflection takes $A\setminus A_{\rm cap}$ to the intersection of $-A$ with the halfspace of $B_{\rm cap}$, up to a null line. Since $-A\subset\operatorname{int}B$,
$$
|A_{\rm cap}|+|B_{\rm cap}|=|A|+|B_{\rm cap}\setminus(-A)|.
$$
If $B_{\rm cap}$ has positive area, its cutoff is strictly below the support value of $B$. The support value of $-A$ is strictly below that of $B$ in the same direction, so there is a positive-area cap of $B$ strictly above both the cutoff and the smaller support value. Thus the excess vanishes exactly when $B_{\rm cap}$ has zero area, or $\alpha\le-(11\rho/10)\lVert u\rVert$. The inequality forces a strictly full $A$ trace. A purely base cap containing the center takes all of $K$, and any strict containing offset of a nonvertical cap increases its own central mass by a positive slab. This proves the depth and exhausts the critical menu.

At a noncentral mark in $K$, choose its outward radial through-cap and take a finite sufficiently negative base tilt to include all of $A$ and strictly miss $B$. Its own area is strictly smaller than $1/2$, so the total is strictly smaller than $3/4$. Each endpoint is exposed. By dec855d1498a4e64 applied to the sum of the three compact disk-volume measures on this singleton exposed face, its maximum is the disk's ordinary half-volume, namely $1/8$ at $-1$ and $121/200$ at $1$, both strictly below $3/4$. This proves uniqueness. The menu contains every direction on $K$ and its permitted tangency cut at $B$ meets $B$ in a single boundary point. All boundary points are realized by their outward normal, so the union and the ratio $(121/100)/(123/50)=121/246$ follow.
