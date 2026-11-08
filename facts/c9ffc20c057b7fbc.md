---
fact_id: c9ffc20c057b7fbc
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-exact-contained-ambient-thickening-of-reflection
depends_on: []
verifier_run: a588ede17b809764
target_match: null
---

## Source

- [b90a2673d60a00b3](../candidates/b90a2673d60a00b3.json), b90a2673d60a00b3:05 §7, (10).

## Statement

Let $C\subset\mathbb R^n\times\mathbb R^d$ be an ambient convex body, $\Lambda=\mathbb Z^n\times\mathbb R^d$, and $q=\dim_H(C\cap\Lambda)>0$. Fix an actual $y=(j,c)\in C\cap\Lambda$, put $E=C\cap(2y-C)$ and assume $R=\mathcal H_q(E\cap\Lambda)>0$. There is an ambient convex body $D\subset C$ such that $D\cap\Lambda=E\cap\Lambda$ exactly. Its intrinsic mixed mass is $R$, its full mixed centroid is $y$, and its normalized local closed-halfspace depth there is $1/2$.

## Proof

Write $\pi$ for base projection. The convex set $E$ is centrally symmetric about $y$. Any positive $q$-fiber of $E$ and its reflected counterpart have a Minkowski midpoint of dimension $q$ contained in its own fiber at $j$. If $\pi(E)$ has interior in $\mathbb R^n$, its symmetry puts $j$ in $\operatorname{int}\pi(E)\subseteq\operatorname{int}\pi(C)$. There is then a point of $\operatorname{int}C$ over $j$. To see this, choose an interior point of $C$ and, if its base differs from $j$, extend the line segment from its base through $j$ a little past $j$ within $\pi(C)$. A lift of the endpoint and the original interior point have a strict convex combination over $j$ lying in $\operatorname{int}C$. Thus $C_j$ is $d$-dimensional and $q=d$. The positive $d$-dimensional own fiber of $E$, together with the full-dimensional base projection, implies that $E$ has dimension $n+d$ by projecting its affine direction space.

If $E$ is already full-dimensional, take $D=E$. Otherwise $A=\operatorname{aff}\pi(E)$ is proper. The finitely many integer bases in $\pi(C)\setminus A$ have a positive minimum distance $\delta$ from $A$, and one may choose any $\delta>0$ if there are none. Fix a base hyperplane containing $A$. Interior points of $C$ approach $y$ by strict interpolation from an interior point. Since $\operatorname{int}C$ is open, choose such a nearby interior point whose projection is off the hyperplane, and a small closed ambient ball $B\subset\operatorname{int}C$ about it such that $\pi(B)$ stays strictly on one side of the hyperplane and at distance less than $\delta$ from $A$. Set $D=\operatorname{conv}(E\cup B)$. Convexity of distance to $A$ keeps every projected point of $D$ within distance $\delta$, so every integer base of $D$ is in $A$. A convex combination with positive $B$-weight is strictly on that side of the chosen hyperplane, so over $A$ the hull equals $E$. This proves equality of the full mixed traces.

Their common $\mathcal H_q$ law is reflection invariant and has mass $R$, so its centroid is $y$ and opposite closed through-$y$ caps have equal mass at least $R/2$. A generic through-$y$ plane is null by Fubini over Gaussian normals because $q>0$ and the law has no atom at $y$. This gives the exact normalized local depth.
