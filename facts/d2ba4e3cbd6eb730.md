---
fact_id: d2ba4e3cbd6eb730
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-positive-simplex-row-unique-capacity-threshold
depends_on: ["aef64d0fab6e1fa1"]
verifier_run: 6a0861e3236969bf
target_match: null
---

## Source

- [78b95c208ba2d374](../candidates/78b95c208ba2d374.json), §2, (2)–(4), unique minimum and envelope.

## Statement

Let $d\ge2$, let $U$ be uniform on $\Delta_d$, and put $F_x(t)=\Pr(x\cdot U\le t)$ and $\phi_d(x)=\inf_{t>0:F_x(t)>0}t/F_x(t)^{1/d}$. For every nonconstant $x\in(0,\infty)^{d+1}$ there is a unique minimizing threshold in $(\min_j x_j,\max_j x_j]$. If the minimizing threshold $t$ is proper, meaning $t<\max_j x_j$, it depends continuously on the row near $x$, the capacity is locally $C^1$, and $\nabla\phi_d(x)=F_x(t)^{-1/d}b$ for the actual barycentric centroid $b$ of the section $x\cdot u=t$.

## Proof

Write $a=\min_j x_j>0$ and $m=\max_j x_j$. Since a nonconstant affine form has no atoms under the simplex volume law, $F_x(t)\downarrow0$ as $t\downarrow a$. The ratio tends to infinity there, is continuous on $(a,m]$, and equals $t$ for $t\ge m$. Thus a minimum is attained. For $a\le t\le m$, the function $F_x(t)^{1/d}$ is concave by Brunn–Minkowski applied to nested convex caps, since a Minkowski combination of two caps is contained in the cap at the combined threshold.

If two thresholds minimize, concavity and the minimizing value force $F_x(t)=C t^d$, $C>0$, between them. Choose a nonempty open interval there avoiding the finitely many vertex heights and below $m$. For a $k$-face $I$ with $k\ge1$, let $F_I(t)$ be its normalized captured volume, and for $j\in I$ let $I\setminus j$ denote its opposite face. On this interval
$$
F_{I\setminus j}(t)=F_I(t)+\frac{x_j-t}{k}F_I'(t).
$$
Indeed, the tangent affine field $e_j-u$ has divergence $-k$ on $I$. Its flux through all facets other than $I\setminus j$ is zero. Its outward normal component on $I\setminus j$ is the negative of the altitude from vertex $j$, so the captured facet flux is $-k\operatorname{vol}_k(I)F_{I\setminus j}(t)$. On the cut face its flux is $(x_j-t)\operatorname{vol}_k(I)F_I'(t)$ by the parallel-section volume formula. The divergence theorem gives the identity. For a fully captured or missed face both sides are the same constant, including the vertex indicator when $k=1$.

Induction from the whole simplex now gives $F_I(t)=C(\prod_{j\notin I}x_j)t^{\dim I}$ for every face $I$ on the interval. Each vertex therefore has a strictly positive capture indicator, contrary to $t<m$. This proves uniqueness.

For nearby rows, minimizing thresholds are at most their largest entry and their minimizing ratios stay bounded by those entries. If rows converge to $x$ and their minimizing thresholds converge to $a$, the cap probabilities tend to zero by dominated convergence because $x\cdot U=a$ has probability zero. Since $a>0$, their ratios would diverge. Every subsequential limit is therefore larger than $a$, and by continuity of the cap probability and comparison with each fixed threshold in $(a,m]$, it minimizes the ratio at $x$. This proves convergence to the unique threshold $t$. For a proper $t$ all nearby minimizing thresholds are also proper.

Write $L(x,t)=tF_x(t)^{-1/d}$. By the proper-cut first variation it is jointly $C^1$ nearby. The two minimizing inequalities bound $\phi_d(x+k)-\phi_d(x)$ above by $L(x+k,t)-L(x,t)$ and below by $L(x+k,t_k)-L(x,t_k)$, with $t_k$ the minimizing threshold for $x+k$. Continuity of the row derivative and $t_k\to t$ give differentiability with derivative $L_x(x,t)$. Threshold stationarity gives $t\partial_tF_x(t)=dF_x(t)$, so the proper-cut formula yields $\nabla\phi_d(x)=F_x(t)^{-1/d}b$. The same formula and continuity of the proper minimizing threshold and section moments give local $C^1$ regularity.
