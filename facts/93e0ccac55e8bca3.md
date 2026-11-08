---
fact_id: 93e0ccac55e8bca3
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-pk-w35-normality-attained-span-source-tensor
depends_on: ["a18f97a10c2efb27", "c343c9f3dc96957e", "ddc04d4ca485357e"]
verifier_run: 89e9c8e435783e8b
target_match: null
---

## Source

- [da91e18223378a53](../candidates/da91e18223378a53.json), da91e18223378a53:03 §§4–5, (5)–(12), conditional full source tensor.
- [da91e18223378a53](../candidates/da91e18223378a53.json), da91e18223378a53:01 §§1–3, (1)–(2), selected normal span.
- [da91e18223378a53](../candidates/da91e18223378a53.json), da91e18223378a53:02 §§1, 3–5, (3)–(12), objective-one stress and tensor.
- [b488285aaeabe80d](../candidates/b488285aaeabe80d.json), b488285aaeabe80d:03 §§4–5, (5)–(14), generic framed budget stress.
- [2d0fea5cdbf7c841](../candidates/2d0fea5cdbf7c841.json), 2d0fea5cdbf7c841:05 §6, generic budget objective-one stress and exact sensitivity.

## Statement

Fix $n\ge0,d\ge1$, a finite nonempty $P\subset\mathbb Z^n$, positive full-dimensional polytopes $K_z\subset\mathbb R^d$, summed fiber volume $\mu$ of total mass $M$, and $N$ caps with freely variable coefficients $L_i=a_i\cdot z+u_i\cdot x-b_i$, $\|u_i\|=1$. Require their closed nonnegative sides to cover the entire continuous space over each $z\in P$, with masses $c_i\le\tau M$. Let $v(\tau)$ minimize $\sum_i\Psi_i$ where $\Psi_i=\int (L_i)_+\,d\mu$. On the interior of its feasible domain $v$ is $C^1$ except at finitely many budgets. At every regular interior budget, from any minimizer one can choose an attained representative by replacing only dispensable zero-source-mass caps, with the same count and with $0\in\operatorname{int}_V\operatorname{conv}\lbrace u_i\rbrace $ for $V=\operatorname{span}\lbrace u_i\rbrace $.

At this representative there are nonnegative active budget and coverage multipliers $r_i,\eta_z$ with objective coefficient one and $M\sum_i r_i=-v'(\tau)$. The cap moments $Z_i,X_i$ are integrals of $z,x$ over the actual cap trace. Let $S_i,Z_i^s,X_i^s$ be zeroth and first moments of one consistent effective coarea measure for cap $i$, with density in $[0,1]$ on its actual source sections and density one on proper sections almost everywhere. Put $W_i=c_i+r_iS_i$, $B_i=Z_i+r_iZ_i^s$, and $Y_i=X_i+r_iX_i^s$. For each $\eta_z>0$, there is a finitely supported probability measure $\nu_z$ on active whole-space saddle pairs $(x,\lambda)\in V\times\Delta_N$, with $\sum_i\lambda_i u_i=0$, $L_i(z,x)\le0$ and $\lambda_iL_i(z,x)=0$. Then
$$
W_i=\sum_z\eta_z\int\lambda_i\,d\nu_z,\quad
B_i=\sum_z\eta_z z\int\lambda_i\,d\nu_z,\quad
P_VY_i-\sum_z\eta_z\int\lambda_i x\,d\nu_z=\Psi_i u_i,
$$
where zero multiplier terms are omitted. In the full ambient continuous space,
$$
\sum_i W_i u_i=0,\qquad \sum_i u_i B_i^T=0,\qquad
\sum_i W_i=\sum_z\eta_z,\qquad
\sum_iY_i u_i^T=\sum_i\Psi_i u_i u_i^T\succeq0.
$$
The trace of the last matrix is $v(\tau)$. The positive-source-mass normals positively span their own linear span. The contacts in $V$ need not belong to the source fibers.

## Proof

Apply a18f97a10c2efb27 with all normals variable. It gives fixed-count attainment and a balanced probability certificate at each base. In an attained minimizer let $F$ be the minimal face of the convex hull of the normals containing zero. A supporting affine functional, chosen zero on $F$ and positive on the other listed normals, annihilates every balanced relation and forces its outside weights to vanish. If $F$ is the whole hull there are no outside normals. Thus caps with normals in $F$ alone cover every plane, by the same certificates. An outside cap of positive hinge could be replaced by a source-empty cap, strictly improving the objective with the same count. Thus outside caps have zero hinge and therefore zero mass, because their planes are source-null. Replace them by source-empty caps with unit normals in $V=\operatorname{span}F$, zero tilt and sufficiently large finite offsets. The span has positive dimension because a face of dimension zero is a vertex and cannot be zero here. Since $0\in\operatorname{relint} F$, the selected representative has the asserted relative interior property.

Near this representative use smooth sphere coordinates for $v_i\in V$ and common rotation coordinates $R$ near the identity, with $u_i=Rv_i$. The local convex hull of the $v_i$ contains a fixed relative ball of radius $\epsilon>0$ about zero. Therefore the maximum margin on $V$ is at least $\epsilon |x|-T_z$ with locally bounded $T_z$. All minimizing contacts of $F_z=\min_{x\in V}\max_i(a_i\cdot z+v_i\cdot x-b_i)$ lie strictly inside one fixed large cube in $V$, uniformly locally. This gives local Lipschitz continuity by uniform comparison of margins on the cube. Whole-space coverage is exactly $F_z\ge0$ and is independent of $R$, by projection and common rotation. Replacing every $b_i$ by $b_i-G$ for $G=\max(0,\max_z(-F_z))$ restores coverage exactly with chart displacement $\sqrt N G$. The repair need not itself preserve the original budget.

For polytopal source fibers the masses and moments of a clipped polytope are semialgebraic functions of the cap coefficients. Indeed the possible vertices solve finitely many linear systems, with rational coordinates on their nonsingular determinant strata. Feasibility, incidence and simplex determinant signs give finitely many semialgebraic triangulation strata, on which simplex volumes and first moments give rational formulas, including zero for lower-dimensional clips. The hinge is the affine margin integrated using these moments. The balanced certificate from a18f97a10c2efb27 expresses coverage by real quantification, so Tarski–Seidenberg applies to the attained minimum graph by quantifying feasible parameters and excluding any smaller value. The domain is upward closed, the value nonincreasing, and one-variable semialgebraic $C^1$ decomposition gives a finite exceptional set in its interior.

Write $s=\max_i c_i/M$. If $s=\tau$ at the minimizer, the function $\sum_i\Psi_i-v(s)$ is locally Lipschitz there by regularity of $v$ and the local slab bound for each nonvertical cap mass. It is nonnegative on nearby whole-space covers by the unrestricted value's definition, and vanishes at the minimizer. Add $B\sqrt N G$ for a local Lipschitz constant $B$ of this function. Offset repair shows the sum has an unconstrained local minimum in the product chart. If $s<\tau$ at the minimizer, monotonicity and its feasibility at lower nearby budgets imply $v'(\tau)=0$. All nearby parameters are then within budget, and the same repair applied to the hinge alone gives an unconstrained local minimum of the penalized hinge, with zero budget multipliers.

By Clarke's Fermat rule and the sum, smooth-composition and finite maximum inclusions, stationarity of the penalized function has hinge coefficient one. In the binding case its budget terms are a convex combination of active cap-mass gradients times $-v'(\tau)/M$, giving the stated $r_i$; in either case the coverage terms are a nonnegative combination of negative gradients for the active $F_z$ from the maximum defining $G$. The proof of c343c9f3dc96957e gives the full physical cap-mass Clarke gradient representation by a single dominated measure on the actual section, including supporting coincidences. Smooth composition pulls back that same gradient to the individual sphere and common rotation variables. The hinge has ordinary gradient $(Z_i,X_i,-c_i)$ by dominated differentiation, since the margin plane is source-null.

To represent a coverage gradient, identify the fixed cube in $V$ with a full-dimensional cube in $\mathbb R^{\dim V}$ and use ddc04d4ca485357e on that cube, then pull back the covectors to the sphere chart. Its finite saddle features give a probability measure $\nu_z$. All primal minimizers are interior to the cube, so the normal-cone condition in that fact gives $\sum_i\lambda_i v_i=0$ at active constraints. The active maximum is zero, giving the asserted sign and complementarity. At the representative $R=I$. The coverage derivative in the common rotation variables is zero.

The free offset and tilt stationarity equations give the displayed identities for $W_i$ and $B_i$. In the individual normal stationarity equation the projected continuous vector is parallel to $u_i$. Pair it with $u_i$. The equalities $u_i\cdot X_i=\Psi_i+b_i c_i-a_i\cdot Z_i$, $u_i\cdot X_i^s=b_iS_i-a_i\cdot Z_i^s$, and $u_i\cdot x=b_i-a_i\cdot z$ whenever $\lambda_i>0$ cancel all offset and tilt terms using the first two equations. The resulting scalar is $\Psi_i$, proving the projected equation. Summing the offset and tilt equations with the appropriate $u_i$ factors gives the two zero forces by saddle balance, and summing offsets alone gives the total multiplier identity.

Set $T=\sum_iY_i u_i^T$ and $Q=\sum_i\Psi_i u_i u_i^T$. The projected equations give $P_VT=Q$ because the contact terms sum to $\sum_z\eta_z\int x(\sum_i\lambda_i u_i)^T\,d\nu_z=0$. Also $T=TP_V$. Common rotations with velocity $\dot u_i=A u_i$ for every skew-symmetric $A$ yield $\sum_iY_i\cdot A u_i=0$. Thus $T$ is orthogonal to all skew-symmetric matrices and hence symmetric. It follows that $T=P_VT=Q$, and the trace is the attained hinge. A feasible budget is positive by the source union bound. Budget complementarity implies $W_i>0$ exactly when $c_i>0$. The zero force with strictly positive weights on these normals implies zero is in the relative interior of their convex hull, hence they positively span their own linear span.
