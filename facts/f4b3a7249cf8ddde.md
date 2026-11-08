---
fact_id: f4b3a7249cf8ddde
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-pk-w35-centers-simplex-orbit-floor
depends_on: ["155691fc3768c06f"]
verifier_run: 57078b100d6d6212
target_match: null
---

## Source

- [f803303a19217c7c](../candidates/f803303a19217c7c.json), f803303a19217c7c:01 Opening (1)–(2), §§1–2.

## Statement

Let $P\subset\mathbb R^n$ be finite and nonempty, let $K\subset\mathbb R^d$ be a full-dimensional simplex with centroid zero, $d\ge1$, and let $K_p=c_p+r_pK$, $r_p>0$, be compatible at the sampled bases. Here compatibility means $\sum_p\lambda_p K_p\subseteq K_j$ for every convex representation $j=\sum_p\lambda_p p$ of a sampled base. Fix a vertex $v_0$ and set $T=K-v_0$. For a sampled base $j$ and $Z\in K$, let $D_j(Z)$ be the raw closed-halfspace depth of $(j,r_j(Z-v_0))$ in the fixed family with fibers $r_pT$. If $G$ is the linear group of vertex permutations of $K$, then
$$
\operatorname{depth}_{\rm actual}(j,c_j+r_jZ)\ \ge\ \min_{A\in G}D_j(AZ),
\qquad
\max_{Z\in K}\min_{A\in G}D_j(AZ)=D_j(0).
$$
The orbit minimum uses at most $d+1$ values, one for each possible designated vertex. Both depths sum ordinary $d$-volume across the sampled fibers.

## Proof

Fix an ambient through-mark cap and write its margin as $\beta\cdot(p-j)+u\cdot(x-c_j-r_jZ)$. If $u\ne0$, take a minimizing vertex $v$ of $u\cdot x$ on $K$ and let $a=-u\cdot v>0$, since the centroid is interior. The accepted support-slope lemma 155691fc3768c06f applies at $j$ to the compatible sampled fibers with direction $-u/\|u\|$. Using their support functions and multiplying the touching upper estimate by $-\|u\|$ gives some $b\in\mathbb R^n$ with
$$
u\cdot(c_p-c_j)\ge a(r_p-r_j)+b\cdot(p-j)
\qquad(p\in P).
$$
This applies also at deficient base rank. At a fiber point $x=c_p+r_pX$, $X\in K$, the actual margin is therefore at least
$$
(\beta+b)\cdot(p-j)+a(r_p-r_j)+r_pu\cdot X-r_ju\cdot Z.
$$
This is the exact margin at the comparison point $x'=(r_j-r_p)v+r_pX$ in the cap $(\beta+b)\cdot(p-j)+u\cdot(x'-r_jZ)\ge0$ through $(j,r_jZ)$. Both parameterizations have the same volume Jacobian $r_p^d$, so this comparison cap has at most the actual cap mass.

Choose $A\in G$ with $Av_0=v$. The map $x'\mapsto A^{-1}(x'-r_jv)$ takes the comparison family to the fibers $r_pT$ and takes its mark to $(j,r_j(A^{-1}Z-v_0))$. Since $A$ preserves $K$, $|\det A|=1$ and the map preserves fiber volumes. It takes the comparison cap to a genuine closed ambient cap, whose mass is at least $D_j(A^{-1}Z)$. For a pure base through-cap the masses agree in the actual and fixed families and the cap contains every point at base $j$, so its mass also bounds the orbit minimum. Moving any general containing cap to pass through the mark can only decrease its mass. This proves the first inequality.

If two maps send $v_0$ to the same $v$, they differ on the right by a vertex permutation fixing $v_0$. Such a permutation preserves every $r_pT$ and all depths in the fixed family, so it gives the same value at the corresponding inverse image of $Z$. Thus only the $d+1$ choices of $v$ can contribute distinct values.

For quasiconcavity of $D_j$, any closed halfspace containing a convex combination of lifted marks at $j$ contains at least one mark in that combination, by affinity of the defining margin. Its mass is therefore at least the minimum of their depths. The mean of the points $AZ$ over $A\in G$ is zero, because averaging the permuted barycentric coordinates makes every coordinate equal to $1/(d+1)$. Hence $D_j(0)\ge\min_A D_j(AZ)$ for every $Z$, with equality at $Z=0$. This proves the optimized identity and its attainment.
