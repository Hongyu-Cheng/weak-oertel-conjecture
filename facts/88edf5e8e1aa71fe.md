---
fact_id: 88edf5e8e1aa71fe
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-pk-w34-birth-prescribed-mass-vertex-trims
depends_on: []
verifier_run: 95b2a618fd4db5ca
target_match: null
---

## Source

- [a277c91b06544c90](../candidates/a277c91b06544c90.json), a277c91b06544c90:01 §1 (1)–(3) and §2 (4)–(5), prescribed-mass deletion and slab interaction.

## Statement

Let $C$ be the hull of positive $d$-polytopes lifted at finitely many bases $P$, $d\ge1$, and suppose they are its actual sections at $P$. Let $V$ be a finite nonempty set of distinct exposed vertices of $C$, with exposing affine functions $\ell_v$ uniquely maximized at $v=(p_v,x_v)$ with value $h_v$. Let $W_v$ be the tangent cone of the $p_v$-fiber at $x_v$, based at the origin, and set
$$
B_v=\{w\in W_v:-\ell_{v,\mathrm{cont}}(w)\le1\},\qquad a_v=|B_v|>0,
$$
where $\ell_{v,\mathrm{cont}}$ is the linear continuous part. Given a probability vector $\lambda$ on $V$, intersect $C$ with $\ell_v\le h_v-t_v$ for each $\lambda_v>0$, where $t_v=(\varepsilon\lambda_v/a_v)^{1/d}$. For all sufficiently small $\varepsilon>0$, uniformly over $\lambda$, the resulting convex body has positive actual fibers on $P$, converging to the old fibers, and its removed mixed mass is exactly $\varepsilon$. Its disjoint removed pieces have masses $\varepsilon\lambda_v$ and equal $\{p_v\}\times(x_v+t_v B_v)$ up to null boundaries.

For any fixed finite family of nonvertical ambient caps with unit continuous normals $u_j$, the fraction of the removed $v$-piece in cap $j$ is $\iota_{jv}=1$ or $0$ at strict inside or outside vertices, and $\iota_{jv}=|B_v\cap\{u_j\cdot w\ge0\}|/a_v$ at a vertex on the cap boundary. Thus the total removed cap mass is exactly $\varepsilon\sum_v\lambda_v\iota_{jv}$. For $d\ge2$ the removed mass in any width-$O(\varepsilon)$ slab about a selected cap boundary is $O(\varepsilon^{2-1/d})$, uniformly over $\lambda$. In dimension one the interaction is zero for small $\varepsilon$ whenever the selected cap boundary avoids the trimmed vertices.

## Proof

An extreme point of the convex hull of finitely many compact convex fibers belongs to one of the generators, since every term of positive weight in a representation of the point must coincide with it. Strict exposure gives a positive support gap on every other fiber and implies that the exposing continuous part is negative on every nonzero ray of $W_v$. This follows because a short nonzero segment on each such ray is feasible at the polytope vertex. Hence $B_v$ is bounded and has positive volume. The incident fiber facets give the inequalities of $W_v$ and the nonincident ones have strictly positive slack at $x_v$. In the cap neighborhood the latter inequalities are inactive for small $t_v$, yielding exactly $x_v+t_v B_v$ up to the boundary of the exposing plane. The radii of these neighborhoods are $O(t_v)$. Because $t_v\le(\varepsilon/a_v)^{1/d}$, they are disjoint uniformly for distinct $v$ when $\varepsilon$ is small, including vertices in one fiber. Each cut is on the same ambient body, so the resulting sections are compatible. For convergence, an interior point in each old fiber has strict slack in all exposing planes. Each fixed strict homothet of its old fiber toward that point is retained for all small $\varepsilon$. Such homothets approach the old fiber and retain a fixed interior ball. This also proves that the same bases remain occupied.

Cap signs are eventually fixed on each removed piece when its vertex has a nonzero margin. At a coincident vertex the base is fixed and the cap restricts exactly to $u_j\cdot w\ge0$ under the rescaling. For the interaction bound, a slab of width $O(\varepsilon)$ in the unit continuous direction meets the $v$-piece in volume at most its width times the $(d-1)$-dimensional volume of that piece's projection, which is $O(\varepsilon t_v^{d-1})$. Summing finitely many such estimates gives the uniform stated bound. When a vertex avoids the old boundary, its removed piece is disjoint from the slab for small $\varepsilon$, also in dimension one.
