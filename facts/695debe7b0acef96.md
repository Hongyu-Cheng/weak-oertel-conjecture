---
fact_id: 695debe7b0acef96
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-projection-extreme-nonfacet-stress-elimination
depends_on: ["2a4a52bfb9bb6563"]
verifier_run: c6248689c79da07c
target_match: null
---

## Source

- [860152d497c5cff4](../candidates/860152d497c5cff4.json), §§3–4, (4)–(5); §6.

## Statement

Consider a finite compatible family of positive-volume $d$-polytopes, $d\ge2$, at fixed bases. Let $e$ be a vertex of the convex hull of the base set, and let a nontrivial anchored inclusion at a different base have weight $p_e>0$ on $e$. Let $n$ be one of its target facet normals, and suppose the exposed face at $e$ in direction $n$ has dimension at most $d-2$. Enlarge a nearby affine variation chart by adjoining the unilateral truncation of $K_e$ in direction $n$, at reference support deficit $\sigma\ge0$. Use the sufficient first-order compatibility cone that credits the cut by $p_e\sigma$ in this target inequality and each matching outgoing inequality, and discards its support improvement in other directions. If a normalized local stress exists on this enlarged cone, with cap-cover conditions independent of $\sigma$ and nonnegative compatibility and unilateral multipliers, all multipliers with positive credited coefficient of $\sigma$ vanish. In particular the multiplier of the stated target-facet contact vanishes (each active vertex-tuple multiplier, in a finite smooth expansion).

## Proof

After the affine motions, a target facet inequality for an anchored representation is
$$
h_{\rm target}-\sum_w p_w h_{K_w}(n')\ge0,
$$
where $n'$ is the moving target covector in a nearby chart and $h_{\rm target}$ is its transformed offset. It suffices to retain the finitely many extreme non-self representations at each target: every other representation is a convex combination of them, and the support condition is affine in its weights. Before truncation, each such gap is the minimum of the smooth gaps obtained by substituting all source vertex tuples. Near a matching direction $n$, the pulled-back direction at $e$ is $n+O(|p|)$, with $p$ denoting the affine parameters, so the preceding uniform truncation lemma decreases that source support by at least $\sigma-O(|p|\sigma)$. The actual gap is therefore at least its untruncated value plus $p_e\sigma+o(|p|+\sigma)$. If there are multiple indexed cuts, other cuts only decrease source support further. Nonmatching outgoing gaps do not decrease from this cut. Since $e$ is an extreme base, it cannot be the target of a nontrivial convex combination of other bases, so there is no opposing incoming target cost. Strict satisfaction of the credited active linear inequalities yields actual compatibility for sufficiently small positive steps, and inactive inequalities retain their gaps.

The uniform loss lemma bounds total volume and the change in every cap mass by $o(\sigma)$ when adjoining this coordinate. Hence the objective and cap gradient contributions have zero $\sigma$ coordinate, including generalized cap gradients at the base point. More explicitly, the volume of the additional slab removed when a reference support deficit changes from $\sigma_1$ to $\sigma_2$ near zero is bounded by $|\sigma_1-\sigma_2|$ times a constant times $\max(\sigma_1,\sigma_2)^{d-k-1}$, where $k$ is the dimension of the exposed face. The barycentric simplex argument gives this bound by fixing the sum of the $d-f$ off-face coordinates with their positive deficit coefficients, whose density on the truncated simplex is bounded by a constant times the deficit to power $d-f-1$. Affine determinants are locally bounded and restriction to any fixed cap only decreases the loss. This uniform bound also gives zero $\sigma$ components in limiting generalized gradients, with the function extended constantly in $\sigma$ for negative $\sigma$ when needed.

The assumed stress identity in the $\sigma$ coordinate now reads $0=-\sum_\nu c_\nu\eta_\nu-\zeta$, where $c_\nu$ are the credited compatibility coefficients, $\eta_\nu\ge0$ and $\zeta\ge0$ is the unilateral multiplier. Since all $c_\nu\ge0$, any with $c_\nu>0$ forces $\eta_\nu=0$. The same argument applies to every active source vertex tuple under a matching constraint. In the three-fiber case the only nontrivial representation has both endpoint weights $1/2$. For its doubled middle-facet inequality the bonus is $\sum_e\sigma_{e,\ell}$, so all active pair multipliers vanish at a facet with at least one indexed cut.
