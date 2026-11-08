---
fact_id: ba0f3db1bf4f62c6
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-finite-base-canonical-lift-and-depth-restriction
depends_on: []
verifier_run: eae8fb49bc6042e5
target_match: null
---

## Source

- [c280bb0dcfd30f3d](../candidates/c280bb0dcfd30f3d.json), §§1–3, (1), (4)–(7).
- [dbf3b23d25004153](../candidates/dbf3b23d25004153.json), §4, (6)–(7), and §6, (12) for zero shear.

## Statement

For a nonempty finite set $P$ in a real affine space, call $T\subseteq P$ closed if $T=P\cap\operatorname{conv}(T)$. An anchored representation of $q\in P$ is $q=\sum_{p\in P}\lambda_pp$ with $\lambda_p\ge0$ and $\sum_p\lambda_p=1$. Let $L(P)\subseteq\mathbb R^P$ be the space of scalar functions preserving every such equality. For a basis $1,g_1,\ldots,g_{\ell-1}$ of $L(P)$, the map $\Phi_P(p)=(g_1(p),\ldots,g_{\ell-1}(p))$ is injective, with an affine projection back to $P$. Its image has affine dimension $\ell-1$, preserves exactly the anchored representations and the closed traces, and all representation-preserving functions on $\Phi_P(P)$ are affine restrictions. In particular its relative Helly number equals $h(P)$, the least number of ambient convex sets needed to certify an empty common trace on $P$ from any finite such system.

Fix $d\ge1$. A family of nonempty compact convex sets $K_p\subset\mathbb R^d$ is compatible if $\sum_p\lambda_p K_p\subseteq K_q$ for every anchored representation of $q$. This is equivalent to being the exact sections of the convex hull of their placed fibers at all sites of $P$. For families of positive $d$-volume let $D_P(K)$ be the maximum, over placed fiber points, of the infimum of normalized mass of containing closed halfspaces, using the sum of fiber $d$-volumes. Let $M_T=\sum_{p\in T}|K_p|_d$ for nonempty $T\subseteq P$. Then, with the same retained fibers,
$$
D_P(K)\ \ge\ \frac{M_T}{M_P}\,D_T(K|_T)
\ \ge\ \frac{M_T}{M_P}\,D_{\Phi_T(T)}(K|_T).
$$
Here $T$ has its inherited placement and the last depth uses its own canonical lift. The closed-minor operation followed by canonical lifting, iterated on an initial $P$, produces only lifts of its nonempty closed subsets up to affine equivalence. For a closed $T$, $h(T)\le h(P)$.

## Proof

Restricted affine functions lie in $L(P)$, so the original coordinates are affine combinations of the basis coordinates and $1$. They give the affine projection. A proper affine relation on the image would give a dependence among the basis functions, so the affine span has the stated dimension. Applying each basis function to a representation gives a lifted representation, and projecting any lifted representation gives the converse. The closed traces are therefore the same under relabeling, since membership in the convex hull of a subset is exactly the existence of a representation supported there. Closed traces are exactly the traces of convex sets, since each closed trace is realized by its own convex hull, with the empty trace realized by the empty set. This proves equality of the Helly numbers. Transporting any representation-preserving function back to $P$ puts it in $L(P)$, where its basis expansion gives an affine restriction on the image. The same argument gives an affine equivalence between the images from any two bases.

A point of the hull at $q$ is a convex combination of points in the placed fibers. Grouping by site gives a point of $\sum_p\lambda_p K_p$ for the corresponding anchored representation, using convexity of each $K_p$. Compatibility puts it in $K_q$. Conversely any point in such a Minkowski combination belongs to that hull section, which proves the equivalence. The equalities of representations preserve compatibility on lifting, and restriction retains compatibility because it only uses representations with sources in $T$.

At any retained candidate, each original containing halfspace has raw mass at least its mass on the retained fibers. Every halfspace on the affine hull of the retained placement extends to the ambient affine space, and restricting an original halfspace gives a halfspace on that hull or the whole hull. Including the latter option cannot decrease depth, since it has full mass. Thus the restricted depth uses the same cuts whether the retained placement is embedded or viewed in its own affine hull. Taking the infima over cuts and the maxima over retained candidates gives the first inequality. For the second, the affine map $(\Phi_T(p),x)\mapsto(p,x)$ preserves every retained fiber's mass, and pulls each original containing halfspace back to a containing halfspace or the whole space. The lifted infimum can only be smaller. The maxima exist because within any one fiber, moving the candidate through a distance $s$ changes each through-candidate cut with a unit continuous normal by at most the summed mass of slabs of width $s$ in a common ball. Pure-base cuts do not change. The resulting Lipschitz depth is maximized on each compact fiber.

If $T$ is closed in $P$, every subset of $T$ closed in $T$ is also closed in $P$, since its hull lies in $\operatorname{conv}(T)$. Closedness transports through the canonical lift. Upon restriction the inherited and original anchored representations coincide, so the next lift is affinely equivalent to the canonical lift of that subset of $P$. A minimal family of closed traces on $T$ with empty common trace has witnesses in $T$ after deletion of any one member. The same traces are closed in $P$ and have the same witnesses, giving $h(T)\le h(P)$.
