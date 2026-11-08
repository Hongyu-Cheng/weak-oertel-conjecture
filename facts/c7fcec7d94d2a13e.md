---
fact_id: c7fcec7d94d2a13e
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-pk-w35-roofs-partition
depends_on: []
verifier_run: 8e05a19264ff5d8a
target_match: null
---

## Source

- [71864c461210d110](../candidates/71864c461210d110.json), 71864c461210d110:01 §§1–2, (1)–(3).

## Statement

Let $P=\operatorname{conv}(P)\cap\mathbb Z^n$ be nonempty and finite in its inherited lattice, with affine span $\mathbb R^n$. Let $C$ be the canonical hull of its actual positive $d$-dimensional sampled fibers $K_z$, where $d\ge1$. For any nonzero continuous covector $v$, the actual support height $g(t)=h_{C_t}(v)$ on $Q=\operatorname{conv}P$ is the finite concave polyhedral roof with sampled heights $h_z=h_{K_z}(v)$. It has a finite minimum representation by global affine majorants $\ell_j$ whose closed full-dimensional contact cells $Q_j$ cover $Q$. If a sampled $z\in Q_j$ has a $v$-face of positive $\mathcal H^{d-1}$ measure, $v\cdot x=\ell_j(t)$ supports an actual ambient facet of $C$ projecting onto $Q_j$.

There is a partition of $P$ into pieces $P_j$ with $\operatorname{conv}(P_j)\subseteq Q_j$ and $\operatorname{conv}(P_j)\cap\mathbb Z^n=P_j$. For each nonempty piece, the canonical hull of the assigned whole $v$-faces has precisely those faces as its integer traces and has no other integer bases. Thus this partition counts the original sampled $v$-face area exactly, including area at boundary bases. Use counting measure for $d=1$.

## Proof

At a real base $t$, the section of the canonical hull is the union of $\sum_z\lambda_zK_z$ over $\lambda_z\ge0$, $\sum_z\lambda_z=1$ and $\sum_z\lambda_z z=t$. Support maximization gives $g(t)=\max_\lambda\sum_z\lambda_z h_z$, with the maximum attained in the compact coefficient polytope. At sampled bases, actualness gives $g(z)=h_z$. The hypograph of $g$ is the convex hull of $(z,h_z)$ plus the downward ray. It is a polyhedron of dimension $n+1$ in the relative base coordinates and height. The facet inequalities with positive height coefficient give $\ell_j$, while the vertical facets constrain only the domain. Each upper facet projects bijectively onto a full-dimensional closed contact cell. The inequalities represent the upper height at every $t\in Q$, so the cells cover the boundary as well as the interior. This also gives a single upper facet when the data are affine.

The face $F_j=C\cap\{(t,x):v\cdot x=\ell_j(t)\}$ projects onto $Q_j$ because the fiber support is attained. If one sampled face over $Q_j$ has positive area, the kernel of the projection on the direction space of $\operatorname{aff}F_j$ contains $d-1$ independent vertical directions. With its rank-$n$ projection, $\dim F_j=n+d-1$. Its equation gives the upper bound on dimension, and $C$ has full dimension by its rank-$n$ projection and a positive $d$-dimensional fiber. For $d=1$ the vertical dimension in this count is zero.

Choose distinct real $b_j$ and $\epsilon>0$ small enough that $\epsilon\max_{i,j}|b_i-b_j|$ is smaller than every nonzero comparison gap $|\ell_i(z)-\ell_j(z)|$ at sampled $z$, if any such gap exists. At each sampled base the perturbed minimum of $\ell_j+\epsilon b_j$ is unique and chooses an original minimizer. Let $A_j$ be the closed region where the perturbed $j$th piece is minimal and put $P_j=P\cap A_j$. Each $P_j$ lies in the convex cell $Q_j$. Each integer point in $\operatorname{conv}(P_j)$ lies in $P$ by completeness and in $A_j$ by convexity, so is in $P_j$. Empty pieces can be omitted.

Every assigned own face is a nonempty compact set, and convex combinations of points in those faces lie in $F_j$. If such a combination lands at a base of $P_j$, actualness of $K_z$ puts the point in its original own face, since $v\cdot x=\ell_j(z)=h_z$. The assigned own face itself generates that section, proving equality. The unique assignment therefore sums its original $\mathcal H^{d-1}$ area once. Distinct outer normal directions have area-null intersections in a full-dimensional own fiber, since nonparallel hyperplanes intersect in codimension at least two and opposite supporting planes are disjoint.
