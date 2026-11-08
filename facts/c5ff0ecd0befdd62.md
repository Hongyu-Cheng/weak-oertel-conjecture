---
fact_id: c5ff0ecd0befdd62
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-exact-depth-localized-simplex-corner-removals
depends_on: ["53fe12b742a7608d"]
verifier_run: a4d3567e8cd0a181
target_match: null
---

## Source

- [f1516303d16df6d4](../candidates/f1516303d16df6d4.json), §1, (1)–(2), support-localized version.
- [3795aff5f3322d52](../candidates/3795aff5f3322d52.json), §§2–4, flat-corner localization and scalar optimization underlying the support extension.

## Statement

Let $T$ be a full-dimensional $d$-simplex, $d\ge2$, of volume $V$, with barycentric coordinates $\lambda_i$, $0\le i\le d$. Set $m=d+1$, $\Gamma=(d/m)^d$. For a dimension-only $\eta_d\in(0,1/2)$, let $U_i=\{x\in T:\lambda_i(x)>1-\eta_d\}$, and let $K$ be any convex body with $T\setminus\bigcup_i U_i\subset K\subset T$. Write $t_i=|U_i\setminus K|/V$ and $t=\sum_i t_i$.

In a fixed neighborhood of the centroid, the minimum ordinary closed cap volume of $K$ at $y$, divided by $V$, is
$$
\min_i \bigl\{d^d\prod_{j\ne i}\lambda_j(y)-t_i\bigr\}.
$$
The global raw maximum is $DV$, where $D$ is the unique root near $\Gamma$ of
$$
\prod_i(D+t_i)\left(\sum_i(D+t_i)^{-1}\right)^d=d^d.
$$
The unique deepest point has barycentrics $\lambda_i^*=(D+t_i)^{-1}/\sum_j(D+t_j)^{-1}$. The normalized maximum is $D/(1-t)$.

## Proof

Apply an invertible affine map to work in one standard simplex for each $d$. Let $g$ be its centroid. Through-point caps suffice by tightening. The $T$-volume of a through-$y$ cap is continuous jointly in its unit normal and $y$, by bounded convergence off the limiting null hyperplane. By 53fe12b742a7608d the least-cap normals at $g$ are precisely the $m$ positive directions $\nabla\lambda_i$, with cap mass $\Gamma V$. Choose disjoint open normal neighborhoods with compact closures, small enough that all of their through-$g$ caps strictly separate their designated vertex from all the other vertices. The compact complement has a positive cap-volume gap over $\Gamma V$ at $g$. In a sufficiently small fixed neighborhood of $g$, strict separation persists on the closures. The complement retains a uniform positive gap relative to the canonical trials at $y$, by continuity. We can choose $\eta_d$ so small that total missing mass $tV\le m\eta_d^d V$ is smaller than that gap. Thus the minimizing cap normals of $K$ in this neighborhood lie in the designated normal groups. Uniform strict separation, by compactness and continuity of the margins, also makes every cap in the $i$-th group include the entire $U_i$ and exclude all other $U_j$, after decreasing $\eta_d$ if necessary. This uses only that the missing points lie in those corner neighborhoods.

A cap of $T$ in group $i$ has the form $\sum_{j\ne i}c_j\lambda_j(x)\le1$, with $c_j>1$, $\sum_{j\ne i}c_j\lambda_j(y)=1$. Its volume fraction is $\prod_{j\ne i}c_j^{-1}$ by the edge intercept ratios. AM–GM gives a lower bound $d^d\prod_{j\ne i}\lambda_j(y)$ attained at $c_j=1/[d\lambda_j(y)]$. For $y$ sufficiently near $g$ these coefficients are $>1$ and the corresponding direction lies inside the chosen group since it converges to $\nabla\lambda_i$ as $y\to g$. Every such cap loses exactly $t_iV$ from $K$. This gives the claimed local formula.

The continuous through-point cap volumes of $K$ give an upper semicontinuous minimum and hence attainment on compact $K$. The retained centroid has raw depth at least $(\Gamma-t)V$. At any maximizer $y$, the canonical $i$-th through-$y$ cap has $K$-volume at most its $T$-volume $V(1-\lambda_i(y))^d$. Thus every barycentric coordinate is at most $1-(\Gamma-t)^{1/d}$, and the sum constraint supplies lower bounds tending to $1/m$ as $t\downarrow0$. Decrease $\eta_d$ to put every maximizer inside the fixed centroid neighborhood.

The left side of the scalar equation at $t_i=0$ is $m^dD$. The analytic implicit function theorem therefore gives a unique positive root near $\Gamma$, analytic in $(t_i)$ for sufficiently small losses. Put $c=(\sum_i(D+t_i)^{-1})^{-1}$. The resulting coordinates $\lambda_i^*=c/(D+t_i)$ converge uniformly to $1/m$ and thus specify an interior point of the retained central region. The scalar equation gives $d^d\prod_i\lambda_i^*=c$, so all the local cap masses divided by $V$ equal $D$ at this point. For any competitor in the fixed neighborhood achieving at least $D$, put $r_j=\lambda_j(y)/\lambda_j^*$. Each product inequality implies $\sum_{j\ne i}\log r_j\ge0$. Weight these by $1-d\lambda_i^*>0$, which sum to one. The coefficient of $\log r_j$ in the weighted sum is $d\lambda_j^*$, so
$$
0\le d\sum_j\lambda_j^*\log r_j
\le d\log\left(\sum_j\lambda_j^*r_j\right)=0.
$$
Strict logarithmic concavity forces all ratios to be one. This proves uniqueness and the global value, and dividing by $|K|=V(1-t)$ gives the normalized statement.
