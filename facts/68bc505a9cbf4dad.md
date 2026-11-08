---
fact_id: 68bc505a9cbf4dad
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-pk-w33-individual-fan-rotating-cap-centroids
depends_on: ["2ed51dd7d9c37042", "7a5ea4f8a4c5094c", "b1708c647f27b1f2", "55a57b1cf55d0c87"]
verifier_run: 4d3f6afc4630ed13
target_match: null
---

## Source

- [cda9653e9d3e6d40](../candidates/cda9653e9d3e6d40.json), cda9653e9d3e6d40:04 §§4–5, common full centroid and continuous-rank distinction.
- [cda9653e9d3e6d40](../candidates/cda9653e9d3e6d40.json), cda9653e9d3e6d40:01 §§1 and 5, admissible rotations and positive weight reparameterization.
- [cda9653e9d3e6d40](../candidates/cda9653e9d3e6d40.json), cda9653e9d3e6d40:02 §2, coincident swept-prism terms and moment compactness.
- [cda9653e9d3e6d40](../candidates/cda9653e9d3e6d40.json), cda9653e9d3e6d40:03 §§3–4, closed stress cone and all three moment equations.

## Statement

At an attained all-positive minimum of normalized mixed closed-halfspace depth $\beta>0$ in the fixed lattice-complete nonhollow projection, bounded individual-facet class of 2ed51dd7d9c37042, use its compressed assigned cover with at most $2^n$ deepest-origin circuits and separate slack local circuits on the other bases. Let $M$ be the total mixed volume. Within its restricted compatible individual-fan support chart, permit the affine cap coefficients $(v_{ij},u_{ij},b_{ij})$ of every selected occurrence to vary subject to the fixed positive circuit weights $\rho_{ij}$, $\sum_j\rho_{ij}u_{ij}=0$ and the assigned inequalities $C_{ip}=\sum_j\rho_{ij}(v_{ij}\cdot p-b_{ij})\ge0$. The initial continuous normals are unit, and the moving ones need only be nonzero.

There is one joint objective-one stress with nonnegative cap multipliers $\lambda_{ij}$ zero on slack budgets and nonnegative assigned multipliers $\eta_{ip}$ zero on strict coverage rows. Its cap covectors use full proper section measure and a common measurable allocation on each coincident facet for the body and the section. On an inside facet a body subdensity $\theta$ gives section subdensity $1-\theta$, and on an outside facet both receive $\theta$. Use counting measure when $d=1$. Let $S_{ij},Z_{ij},X_{ij}$ be the total mass and base and continuous first moments of each resulting full mixed section measure. For $t_i=\sum_p\eta_{ip}$ there are vectors $q_i$ with
$$
\lambda_{ij}S_{ij}=\rho_{ij}t_i,\qquad
\lambda_{ij}Z_{ij}=\rho_{ij}\sum_p\eta_{ip}p,\qquad
\lambda_{ij}X_{ij}=\rho_{ij}q_i,\qquad
\sum_{i,j}\lambda_{ij}=1/\beta.
$$
For each stressed group $t_i>0$, all its cap multipliers are positive and the effective sections have one common full centroid on every group plane, with coordinates $(\sum_p\eta_{ip}p/t_i,q_i/t_i)$. Its continuous coordinate differs from the continuous coordinate of the $\eta$-weighted average of any assigned globally deepest marks by an element of $\bigcap_j\ker u_{ij}$. If the continuous rank is $d$, the two points coincide and their normalized ambient depth is exactly $\beta$. For lower rank the asserted comparison is modulo this common kernel.

## Proof

Use the actual circuit selection and restricted individual-fan chart established in the proof of 2ed51dd7d9c37042. Its hypotheses are the same fixed base and bounded individual-facet minimization with all fibers positive. The chart is a finite-dimensional support subspace with finitely many homogeneous support-convexity and compatibility rows. Write $A_0$ for the active rows. Every $\delta h$ with $A_0\delta h\ge0$ is realized by a short support line with the same original facet normals, and common erosion is realized with speed $-1$ on every old facet. The cap-budget comparison used there remains valid with varying $u$ once the balance equations are imposed: on the plane over $p$, the weighted cap margin is exactly $C_{ip}$. Thus any nearby competitor of larger mass $M'$ meeting all budgets $\beta M$ has normalized depth at most $\beta M/M'<\beta$. Its positive central fiber can be rescaled to the prescribed volume by common continuous dilation, preserving depth and individual facet counts.

Add the linear equations $\sum_j\rho_{ij}\delta u_{ij}=0$ to the exact radial cone of that chart and the active assigned inequalities $DC_{ip}\ge0$. Every direction of this polyhedral cone $D$ is realized by short affine steps in the body support values and cap coefficients, since the remaining rows have strict slack. The original circuit rank $k_i-1$ persists: a nonzero minor stays nonzero and the fixed dependence bounds the rank above. A nearby positive weight vector $\rho'_{ij}$ with possibly changed normals and margins can equivalently be represented with weights $\rho_{ij}$ by multiplying each occurrence's new margin by $\rho'_{ij}/\rho_{ij}$. This preserves the halfspaces and all weighted projected margins. It is an occurrence-wise parameterization with raw moving normals. If one original label were required to be shared between groups, independent rescalings and rotations across those occurrences would not be supplied by this chart.

The objective derivative $L_0=DM$ is the linear sum of old facet areas times their support speeds. The strip proof of 7a5ea4f8a4c5094c applies locally to each fiber with one body owner per facet. The support chart keeps the original facet list, and the cap's initially unit continuous normal gives margin speed $\tau_{ij}(z,x)=\delta v_{ij}\cdot z+\delta u_{ij}\cdot x-\delta b_{ij}$. On a coincident facet with outward body speed $r$, the actual density is $\min(r,\tau_{ij})$ inside and $\max(r+\tau_{ij},0)$ outside. Its branch depends on $x$. A covector uses a common body subdensity $\theta$ for that facet and section subdensity $1-\theta$ inside or $\theta$ outside. Off coincidence the body density is the strict cap bit and a proper section contributes ordinary area. This gives for every cap a compact convex set $G_{ij}$ of linear covectors whose support function bounds its actual derivative. Indeed the measurable pointwise branches give some covector in that set on each direction, and the needed finite moments of measures dominated by a fixed compact facet measure are compact under weak convergence. All allocations for one cap covector are shared between its shape term and the coefficients of its cap variables.

The erosion direction $e\in D$ has no cap velocities. Every active cap contains a relatively open positive-area old boundary patch strictly inside, because a positive-volume cut has a strictly positive maximum margin and a facet incident to a maximizing vertex contains such a patch. On that patch every covector has contribution given by speed $-1$, and all other erosion terms are nonpositive. Thus each active $G_{ij}$ is uniformly strictly negative on $e$. The convex cone $\sum_{\rm active}\mathbb R_+G_{ij}+D^\circ$ is closed, where $D^\circ$ consists of covectors nonpositive on $D$. Along a convergent sequence in this sum cone, evaluation at $e$ bounds the sum of nonnegative cap coefficients, since the polar terms are also nonpositive there. Compactness gives convergence of a subsequence of cap parts, and then the polar parts converge in the closed polar. If $L_0$ were outside the cone, strict separation would give a direction in $D$ where $L_0>0$ and all active cap covectors are nonpositive. A small addition of $e$ keeps $L_0>0$ and makes every active cap covector strictly negative. A small actual radial step then increases total volume and meets all the old budgets, using continuity for slack budgets. This contradicts the cover comparison.

By polyhedral polarity the resulting identity has the form
$$
L_0=\sum_{i,j}\lambda_{ij}g_{ij}-\sum_{i,p}\eta_{ip}DC_{ip}
-\gamma^{\mathsf T}A_0-\sum_i q_i\cdot D\!\left(\sum_j\rho_{ij}u_{ij}\right),
$$
where $g_{ij}\in G_{ij}$, $\lambda,\eta,\gamma$ are nonnegative and use only the active caps or active rows, and the equality multipliers $q_i$ are free. Evaluating on the free occurrence threshold and base and continuous coefficient coordinates in the ambient chart yields the three moment equations, since the cap coefficients in those coordinates are $-S_{ij},Z_{ij},X_{ij}$. A slack group has $\lambda_{ij}=0$ and therefore $t_i=0$. In a deepest-origin group each $S_{ij}>0$ because of the proper own section at its interior origin. Thus $t_i>0$ forces every $\lambda_{ij}>0$ in that group.

For the normalization dilate every body in the continuous coordinates by the same factor and multiply all cap $(v_{ij},b_{ij})$ by that factor with $u_{ij}$ fixed. The active homogeneous support and coverage rows and circuit equations vanish on its velocity. The coincident speeds satisfy $r=\tau_{ij}$ inside and $r=-\tau_{ij}$ outside, so all allocations give the exact volume derivative on that velocity. The identity reads $dM=\sum_{ij}\lambda_{ij}d\mu(H_{ij})$, and all positively stressed caps have mass $\beta M$.

For $t_i>0$ divide the three equations. The common centroid of measures supported in the actual closed body and on their respective planes lies in that body and on every plane. The base coordinates of the centroid and transported mark average agree. Apply b1708c647f27b1f2 to the assigned deepest marks, which are interior by the positive-depth characterization in 55a57b1cf55d0c87. Its hypotheses hold because the same original assigned weights give nonnegative weighted margin at each such base and all group caps have mass $\beta M$. The average therefore lies on every group plane and has normalized ambient depth $\beta$. Subtracting the plane equations gives that the difference of the continuous coordinates lies in every $\ker u_{ij}$. This is zero in rank $d$.
