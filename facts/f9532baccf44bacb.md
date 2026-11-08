---
fact_id: f9532baccf44bacb
kind: counterexample
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-ordinary-and-paired-simplex-container-obstruction
depends_on: ["f07bbd26b4981214", "6a7d56e450b3126f"]
verifier_run: aefddc6db8083ff5
target_match: null
---

## Source

- [a585520b0a2a14db](../candidates/a585520b0a2a14db.json), a585520b0a2a14db:02 Theorem items 1–3, §§1–3, especially (2)–(5), (13)–(14).

## Statement

Fix an integer $d\ge2$ and a real $0<\varepsilon\le1/16$. Let $T=\operatorname{conv}(0,e_1,\ldots,e_d)$, $V=1/d!$, $\Gamma=(d/(d+1))^d$, and set $a=1+\varepsilon^2$ and
$$
A=\{x:x_i\ge0,\ \varepsilon\le\textstyle\sum_i x_i\le1\},\qquad
B=\varepsilon^2T,\qquad P=\{x:x_i\le a,\ \textstyle\sum_i x_i\ge\varepsilon\}.
$$
The hull of the lifts of $A,P/2,B$ at bases $0,1,2$ has exactly those three positive integer fibers $K_j$. For a continuous convex body $K$, write $D(K)$ for the maximum normalized ordinary depth. Write $D_{\rm pair}(K)$ for the maximum over $y\in K$ of the infimum over nonzero $u$ and $s\ge0$ of
$$
\frac{|K\cap\{u\cdot(x-y)\ge s\}|+|K\cap\{u\cdot(x-y)\ge-s\}|}{2|K|}.
$$
Define $\delta_{\rm ord}(K)=|K|(D(K)-\Gamma)$ and $\delta_{\rm pair}(K)=|K|(D_{\rm pair}(K)-\Gamma)$. Then
$$
0\le \sum_j\delta_{\rm pair}(K_j)\le\sum_j\delta_{\rm ord}(K_j)\le\Gamma\varepsilon^d V.
$$
Every choice of enclosing $d$-simplex for each actual integer fiber, convexified at the same bases, adds at least $\varepsilon V/(16d^2)$ of actual mixed $d$-volume. For either positive deficit sum the ratio of added mass to that sum is at least $\varepsilon^{1-d}/(16d^2\Gamma)$. Consequently no finite constant bounds the added mass by either deficit sum, even at fixed $d$.

## Proof

The set $P$ is the reflection under $x\mapsto a\mathbf1-x$ of a simplex of ratio $da-\varepsilon$. Each coordinate of $A+B$ is at most $a$, and its coordinate sum is at least $\varepsilon$, so $A+B\subseteq P$. The outer lifts are preserved as extreme base fibers. At base one a convex combination of the lifts is a mixture of a point in $P/2$ and one in $(A+B)/2$, which is again in $P/2$. The projection is $[0,2]$, and the full-dimensional continuous endpoint fibers give ambient interior. Thus all sampled fibers are exactly the stated ones. Their volumes are $V(1-\varepsilon^d)$, $2^{-d}V(da-\varepsilon)^d$ and $V\varepsilon^{2d}$.

Each cap volume is continuous in the center for a fixed nonzero normal and shift by dominated convergence, since a proper hyperplane has zero volume. Both depth functions are infima of such continuous functions and hence are upper semicontinuous, so their maxima on a compact fiber exist. By 6a7d56e450b3126f the ordinary and paired depths at the centroid of every fiber are at least $\Gamma$, the ordinary statement following by taking $s=0$. Taking $s=0$ in the paired infimum at any point also gives $D_{\rm pair}(K)\le D(K)$. At each point of a simplex, a largest barycentric coordinate is at least $1/(d+1)$, so its through-point vertex cap has volume at most $\Gamma$ times the simplex volume. Both deficits therefore vanish for $P/2$ and $B$. Since $A\subset T$, the same vertex caps of $T$ give $|A|D(A)\le\Gamma V$. This gives the deficit inequalities.

For arbitrary enclosing simplices $R_j\supseteq K_j$, let $K'_j$ denote the actual fibers of the hull of their lifts. Its endpoint fibers are $R_0$ and $R_2$. Since $0\in B\subseteq R_2$, the midpoint fiber contains $R_0/2$, and it also contains $P/2$ by inclusion. Thus $L=2K'_1$ is compact and convex and contains $P$ and $R_0$. The nested-simplex excess bound applied to $R_0,L$ proves the lower bound on the sum of the excesses at zero and one. The excess at two is nonnegative. The ratio follows by division when the deficit is positive, and a zero deficit already contradicts any finite proposed upper bound because the cost is positive. For positive deficits the lower ratio bound diverges as $\varepsilon\downarrow0$.
