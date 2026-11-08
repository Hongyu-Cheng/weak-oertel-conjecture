---
fact_id: 0bcaaeaec6056a0b
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-clarke-gradient-active-marginal-minimizer
depends_on: []
verifier_run: 7b610b60a8eff092
target_match: null
---

## Source

- [dcde24475c7f190c](../candidates/dcde24475c7f190c.json), dcde24475c7f190c:02 §3, marginal lemma (8).

## Statement

Let $U\subseteq\mathbb R^d$ be open, $P$ a compact subset of a smooth finite-dimensional manifold, and $G$ jointly continuous on $U\times P$, with a locally uniform Lipschitz bound in $y$. Let $h(y)=\min_{p\in P}G(y,p)$. Fix $y_*\in U$. Assume either that every minimizer at $y_*$ lies in the interior of $P$ in a smooth chart where $G$ is jointly locally Lipschitz, or that all $y$ near $y_*$ admit a minimizer in a fixed compact subset of that interior on which such local charts are available. For every limit $g$ of ordinary gradients of $h$ at differentiability points tending to $y_*$, there is a minimizing $p_*$ at $y_*$ with $(g,0)\in\partial_C G(y_*,p_*)$ in a joint chart. The zero is in all parameter coordinates simultaneously.

## Proof

For a locally Lipschitz function $J$ on an open Euclidean set and a point $q$, the Clarke gradient is the intersection over shrinking balls about $q$ of the closed convex hulls of the nearby ordinary gradients. In forming these hulls one can omit any fixed Lebesgue-null set in addition to the nondifferentiability set. To see this, a strict separating directional bound for the gradients off the omitted set gives the same slope bound for $J$ on all line segments in that ball parallel to the separating direction. Integrate the bound on almost every such line by Fubini and the absolute continuity of a Lipschitz function on lines, then pass to all lines by continuity. Differentiating these segment inequalities gives the bound at all differentiability points in the ball. The shrinking-hull description also shows closedness of the graph. A Fréchet subgradient $v$ at $q$ belongs to this intersection: if not, separation gives a direction $w$ and a ball where all ordinary directional derivatives are at most $v\cdot w-\epsilon$ for some $\epsilon>0$. The segment inequality contradicts $J(q+tw)-J(q)\ge t\,v\cdot w+o(t)$ as $t\downarrow0$.

The minimum exists by compactness and $h$ is locally Lipschitz by the uniform bound. Choose differentiability points $y_i\to y_*$ with $\nabla h(y_i)\to g$, and minimizing parameters $p_i$, chosen in the fixed compact interior subset when using the second hypothesis. Pass to a subsequence with $p_i\to p_*$. Continuity makes $p_*$ a minimizer, and eventually the pairs lie in the same joint chart in the interior of $U\times P$. For all nearby $(y,p)$,
$$
G(y,p)-G(y_i,p_i)\ge h(y)-h(y_i)=\nabla h(y_i)\cdot(y-y_i)+o(\lVert y-y_i\rVert).
$$
The error is also $o(\lVert(y-y_i,p-p_i)\rVert)$, giving the Fréchet subgradient $(\nabla h(y_i),0)$ in the joint chart. Its Clarke membership and the closed graph give the claim. Under a smooth change of parameter coordinates the zero remains zero.
