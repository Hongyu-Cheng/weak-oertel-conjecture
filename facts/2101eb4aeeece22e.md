---
fact_id: 2101eb4aeeece22e
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-movable-simplex-lower-diagonal-maximizer
depends_on: ["855dee75ae1183c5", "700febf4b7a92759"]
verifier_run: ee6f9dbe68d88d87
target_match: null
---

## Source

- [44a12d13f3aabab3](../candidates/44a12d13f3aabab3.json), 44a12d13f3aabab3:04 §4, (6), (17) and (17a).

## Statement

Let $n\ge0$ and $d\ge1$, $P\subset\mathbb R^n$ nonempty and finite, $j\in P$, and $r_p>0$. Let $T_d=\operatorname{conv}(0,e_1,\ldots,e_d)$ and give the fibers $\{p\}\times r_pT_d$ their summed ordinary $d$-volume. Suppose $r_p\le r_j+b\cdot(p-j)$ for some $b\in\mathbb R^n$. Then a point maximizing raw mixed halfspace depth over the own fiber $\{j\}\times r_jT_d$ can be chosen at $(j,t\mathbf1)$ with $0<t\le q=r_j/(d+1)$. For $0\le t\le q$, the ordinary raw halfspace depth of $t\mathbf1$ in the own simplex equals $|T_d|(dt)^d$. This amount is also a lower bound for the raw mixed depth at $(j,t\mathbf1)$.

## Proof

For fixed $j$, tighten containing halfspaces to pass through the point. For a nonvertical cap, normalize its continuous normal to Euclidean norm one. Moving the mark by $h\in\mathbb R^d$ changes each fiber threshold by at most $\|h\|_2$. All fibers lie in balls of radius $r_p$ about the origin. By slicing perpendicular to the normal, each resulting difference of cap volumes is at most $\|h\|_2$ times the $(d-1)$-volume of the corresponding ball of radius $r_p$, with the bound one on a zero-dimensional section when $d=1$. Vertical cap masses are constant in the continuous mark. The infimum of this uniformly Lipschitz family is Lipschitz, so a maximum is attained on the compact own fiber.

Each raw-depth superlevel set is convex: a closed halfspace containing a convex combination contains at least one constituent point, so if all constituent depths are at least a level, its mass is at least that level. The permutations of the continuous coordinates are genuine ambient symmetries of the source. Averaging the orbit of a maximizing $y$ therefore gives a maximizer at $(\sum_\ell y_\ell/d)\mathbf1$. If the diagonal parameter is greater than $q$, the upper-diagonal comparison in movable-simplex-through-mark-positive-normal, applied under the given touching majorant, shows that $q$ has at least that depth. At $t=0$ the cap $X_1\le0$ takes zero volume, while the own centroid is an interior point of a positive-volume fiber and hence has positive depth, using an inscribed ball for every nonvertical cap and the whole own fiber for every vertical cap. Thus a maximizing parameter can be taken positive.

For $0<t\le q$ the simplex $((d+1)t)T_d$ lies in the own simplex and has centroid $t\mathbf1$. Its barycentric coordinates are all $1/(d+1)\le1/d$, so 700febf4b7a92759 supplies a lower bound of $(d/(d+1))^d$ times its volume in every containing cap. This is $|T_d|(dt)^d$. The cap $\sum_\ell X_\ell\le dt$ within $r_jT_d$ is exactly $(dt)T_d$, proving the matching ordinary upper bound. At $t=0$ this same cap gives zero. Any ambient cap through or containing $(j,t\mathbf1)$ takes at least the stated amount in its own fiber, including when the own trace is the whole fiber.
