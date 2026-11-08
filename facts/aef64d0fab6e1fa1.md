---
fact_id: aef64d0fab6e1fa1
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-proper-simplex-cut-first-variation
depends_on: []
verifier_run: 6406d15fbe7fdf76
target_match: null
---

## Source

- [78b95c208ba2d374](../candidates/78b95c208ba2d374.json), §1, (1), proper-cut derivatives.

## Statement

Let $d\ge2$, let $U$ be uniform on $\Delta_d=\{u\ge0:\sum_{j=0}^d u_j=1\}$, and set $F_x(t)=\Pr(x\cdot U\le t)$ for $x\in\mathbb R^{d+1}$. For every $\min_j x_j<t<\max_j x_j$, the function $(x,t)\mapsto F_x(t)$ is jointly $C^1$ near $(x,t)$. Let $b$ be the barycentric centroid of the section $S=\Delta_d\cap\{x\cdot u=t\}$ for uniform $(d-1)$-dimensional volume on $S$, and let $n$ be the projection of $x$ onto $\{\sum_j u_j=0\}$. Then
$$
\partial_t F_x(t)=\frac{\operatorname{vol}_{d-1}(S)}
{\operatorname{vol}_{d}(\Delta_d)\lVert n\rVert}>0,
\qquad \partial_{x_j}F_x(t)=-b_j\partial_t F_x(t).
$$
The formula includes a plane through any simplex vertex or lower-dimensional face consistent with properness.

## Proof

In the affine hull of $\Delta_d$ put $e=n/\lVert n\rVert$, write points as $u=y+se$ with $y$ in the old section plane, and integrate along these lines. The simplex intersection on each line is an interval, possibly empty, and the old cut is $s\le0$. Replacing $(x,t)$ by $(x+k,t+h)$ changes the cut endpoint to $(h-k\cdot y)/(\lVert n\rVert+k\cdot e)$. It changes the length captured on any line by at most the magnitude of this displacement. For almost every $y$ in the old section, $s=0$ is strictly interior to the fiber interval, because the proper section meets the simplex interior and its intersection with the simplex boundary is $(d-1)$-volume null. For almost every $y$ outside the old section, $s=0$ has positive distance from the fiber or the fiber is empty.

On a fixed bounded projection containing the simplex, the difference of captured lengths, minus the linear term $(h-k\cdot y)\mathbf 1_S(y)/\lVert n\rVert$, divided by $\lVert(k,h)\rVert$, tends pointwise almost everywhere to zero and is bounded uniformly. Dominated convergence gives the total derivative by integrating the linear term and dividing by $\operatorname{vol}_d(\Delta_d)$. The section contains an open subset of its own plane, giving the strict sign and $b_j>0$ for every $j$.

For continuity, parameterize nearby planes by their graphs over the old one using the same endpoint formula. The graph Jacobians and coordinates converge uniformly on the bounded projection, and the simplex indicators converge except on the null boundary of the old section. Dominated convergence gives continuity of the section volume and first moments, and hence of the displayed derivatives.
