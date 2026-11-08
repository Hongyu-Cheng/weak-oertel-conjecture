---
fact_id: 40247ac9eabebdb4
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-linear-cap-distance-localized-corner-stability
depends_on: ["c5ff0ecd0befdd62"]
verifier_run: 1021632289fb1483
target_match: null
---

## Source

- [f1516303d16df6d4](../candidates/f1516303d16df6d4.json), §§2–3, (3)–(7).

## Statement

Let $T$ be a full-dimensional $d$-simplex, $d\ge2$, of volume $V$, with barycentric coordinates $\lambda_i$, $0\le i\le d$. Set $m=d+1$, $\Gamma=(d/m)^d$. For a dimension-only $\eta_d\in(0,1/2)$, let $U_i=\{x\in T:\lambda_i(x)>1-\eta_d\}$, and let $K$ be any convex body with $T\setminus\bigcup_i U_i\subset K\subset T$. Write $t_i=|U_i\setminus K|/V$ and $t=\sum_i t_i$.

Write $a_d=\Gamma-1/m>0$, $D(K)$ for normalized ordinary maximum depth, and $d_{\rm cap}(\mu,\nu)=\sup_H|\mu(H)-\nu(H)|$ over closed halfspaces. All uniform measures are probability measures. After choosing $\eta_d$ sufficiently small,
$$
D(K)-\Gamma\ge\frac{a_d t-4t^2/\Gamma}{1-t}.
$$
In particular, if $t\le\Gamma a_d/8$, then $D(K)-\Gamma\ge(a_d/2)t\ge(a_d/2)d_{\rm cap}(\mu_K,\mu_T)\ge(a_d/2)\inf_S d_{\rm cap}(\mu_K,\mu_S)$, where $S$ ranges over full-dimensional simplices. Uniformly in the ratios of the corner losses, $D(K)-\Gamma=a_d t+O_d(t^2)$. A flat single-corner deletion attains $d_{\rm cap}(\mu_K,\mu_T)=t$, so $a_d$ is sharp to first order for missing volume and cap distance from this fixed reference.

For positive $h,k$ sufficiently small, put $Q=\operatorname{conv}(0,e_1,e_2,(1+h-k,k))$ and $S=\operatorname{conv}(0,[1+h/(1-k)]e_1,e_2)$. Then $Q\subset S$ and the relative missing area and fixed-reference cap distance are $\tau=hk/(1+h-k)$. The exact normalized ordinary maximum of $Q$ is
$$
\frac{2(1+\sqrt{1+3\tau})/9-2\tau/3}{1-\tau}
=\frac49+\frac{\tau}{9}-\frac{5\tau^2}{36}+O(\tau^3).
$$
Consequently its ordinary depth excess and cap distance from $S$ have order $hk$.

## Proof

Use the localized ordinary depth formula from the preceding localized-deletion theorem. Since $\Gamma=(1-1/m)^d>1-d/m=1/m$ for $d\ge2$, $a_d>0$. At the test mark set $b_i=t_i-t/m$, $\lambda_i=(1-b_i/\Gamma)/m$. These coordinates sum to one, are positive and near the centroid for small enough $\eta_d$, and belong to $K$ by the support assumption. Also $\sum_i |b_i|\le2t$. Take $t\le\Gamma/4$, possible by reducing $\eta_d$. In the $i$-th product put $x_j=-b_j/\Gamma$ for $j\ne i$, and $s=\sum_{j\ne i}|x_j|\le2t/\Gamma\le1/2$. The magnitude of the product remainder beyond its constant and linear terms is at most
$$
\sum_{q\ge2}s^q/q!\le s^2/[2(1-s)]\le s^2.
$$
The first inequality follows by bounding each elementary symmetric sum of absolute values by $s^q/q!$. Since $\sum_{j\ne i}b_j=-b_i$, the corresponding cap mass fraction of $T$, after the deletion, is at least $\Gamma-t/m-4t^2/\Gamma$, for every $i$. Divide by $1-t$ and subtract $\Gamma$ to obtain the bound. If $t\le\Gamma a_d/8$, its numerator is at least $a_d t/2$. For nested uniform measures, the positive density difference is supported on $K$ and has total mass $t$, and the negative part is supported on $T\setminus K$ with the same total mass. Hence their total variation is exactly $t$. Halfspace tests are a subset of measurable-set tests, and $T$ is one admissible simplex. This gives the remaining comparisons.

For the asymptotic, at $(D,t_i)=(\Gamma,0)$ the partial derivative of the root equation's left side in $D$ is $m^d$, and each partial derivative in $t_i$ is $m^{d-1}$. Indeed at the symmetric input the first derivatives in all arguments $D+t_i$ coincide and sum to $m^d$. Thus analyticity gives $D=\Gamma-t/m+O_d(t^2)$, uniformly in nonnegative losses, and division by $1-t$ gives the claimed coefficient. A flat corner is the trace of a halfspace on $T$, up to a null boundary, and contains zero $K$-mass. It attains distance $t$.

For the explicit planar example, write $b=1+h/(1-k)$. The point $p=(1+h-k,k)=(1-k)b e_1+k e_2$ lies on the edge from $b e_1$ to $e_2$, while $e_1$ lies on the edge from $b e_1$ to zero. The line through $p$ and $e_1$ cuts the single corner at $b e_1$ off $S$, leaving $Q$. The fractions of the two incident edges removed are $(b-1)/b=h/(1+h-k)$ and $k$. Their product is the relative missing area $\tau$. Its cap trace witnesses distance $\tau$ by the total variation identity. The entire removed corner has barycentric coordinate at $b e_1$ at least $1-\max\{h/(1+h-k),k\}$, so for small $h,k$ it falls in the supported regime of the preceding theorem. Set the other two maximizing barycentric coordinates equal to $r$, by the formula there with loss vector $(\tau,0,0)$. Then $D+\tau=4r^2$ and $D=4(1-2r)r$, so $r=(1+\sqrt{1+3\tau})/6$. Substitution gives the displayed exact normalized value and its Taylor expansion. Both quantities have order $hk$ since the denominator in $\tau$ tends to one.
