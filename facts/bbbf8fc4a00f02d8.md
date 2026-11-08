---
fact_id: bbbf8fc4a00f02d8
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-variable-barycentric-density-ceiling
depends_on: ["0d017e6c3c14b846", "21fe36cb211350dd"]
verifier_run: 8d036a3252dd78f0
target_match: null
---

## Source

- [93c94ac2c5c85584](../candidates/93c94ac2c5c85584.json), §§1–4.
- [d7f1891e34b3ec5a](../candidates/d7f1891e34b3ec5a.json), §7, positive-dimensional analytic step.

## Statement

Let $n\ge0$, $d\ge1$, and $k\ge1$ be integers. For finite $Q\subset\mathbb R^n$ write $\sigma_Q=\sum_{q\in Q}\delta_q\otimes\mathcal L^d$. Let $P_i\subset\mathbb R^n$ be finite and let $\gamma_i$ be finite nonnegative Borel measures of common mass $M$, supported on compact sets $K_i\subset P_i\times\mathbb R^d$. Suppose $\gamma_i\le f_i\sigma_{P_i}$ for finite nonnegative Borel $f_i$ on $K_i$, extended by zero off $K_i$. Take positive weights $\lambda_i$ with sum one and write $b(w)=\sum_i\lambda_i w_i$, $K=\sum_i\lambda_iK_i$, and $P=\sum_i\lambda_i P_i$. Let $g:K\to[0,\infty]$ be Borel with $\int_K g\,d\sigma_P<\infty$, extended by zero off $K$. Suppose there are Borel $E_i\subset K_i$ of full $\gamma_i$ measure such that for every $w\in\prod_i E_i$ with every $f_i(w_i)>0$,
$$
g(b(w))\ \ge\ \left(\sum_i\lambda_i f_i(w_i)^{-1/d}\right)^{-d}.
$$
For every coupling $\pi_0$ of the $\gamma_i$ there is one coupling $\pi$ of the same marginals such that $b_\#\pi_0\preceq_{\rm cx}b_\#\pi$ and $b_\#\pi\le g\sigma_P$. Convex order tests every finite convex function on $\mathbb R^{n+d}$. If every base tuple occurring in $\prod_i E_i$ with all $f_i(w_i)>0$ has an integer barycenter in its base coordinates, then the selected output is supported on integer bases.

## Proof

If $M=0$ the zero coupling suffices. Suppose $M>0$. Let $\phi$ be smooth and $D^2\phi\ge\varepsilon I$ on $\mathbb R^{n+d}$ for some $\varepsilon>0$. Weak compactness of couplings on $\prod_iK_i$ gives a maximizer $\pi$ of $\int\phi(b(w))\,d\pi(w)$. Put $\rho=b_\#\pi$. The compact inverse endpoint lemma applies to these marginals and this surplus. It gives $F_i(z)=\nabla V_i(\lambda_i\nabla\phi(z))$ with $V_i$ convex, $C^1$, and of globally Lipschitz gradient, and gives $(F_i)_\#\rho=\gamma_i$ and $\sum_i\lambda_i F_i(z)=z$ $\rho$-almost everywhere. By continuity these identities of membership and barycenter extend to every $z$ in $\operatorname{supp}\rho$: $F_i(z)\in K_i$ and $\sum_i\lambda_i F_i(z)=z$.

Fix a nonzero slice $\rho_p$ at $p\in P$ and write $F_i(p,y)=(B_i(y),T_i(y))$ on that slice. These maps are Lipschitz on a ball containing $S=\operatorname{supp}\rho_p$, by local Lipschitzness and compactness of the closed ball. For a compact $D\subset S$ and $q\in P_i$, the sets $D_q=D\cap B_i^{-1}(\{q\})$ and $T_i(D_q)$ are compact. The marginal identity gives $\rho_p(D_q)\le\gamma_i(\{q\}\times T_i(D_q))$. If $D$ is Lebesgue-null, each Lipschitz image $T_i(D_q)$ is Lebesgue-null. Absolute continuity of $\gamma_i$ on each base, summation over $q$, and inner regularity on Borel null sets therefore give $\rho_p=h_p\,\mathcal L^d$.

For general compact $D\subset S$, the weighted Lipschitz area formula gives
$$
\rho_p(D_q)
\le\int_{T_i(D_q)} f_i(q,x)\,dx
\le\int_{D_q} f_i(q,T_i(y))\,|\det DT_i(y)|\,dy.
$$
Indeed the area formula on the domain counts the image multiplicity, at least one on $T_i(D_q)$, with the nonnegative Borel weight $f_i(q,\cdot)$. The formula permits unbounded weights by monotone convergence. The determinant can be set to zero on the null set where the derivative is undefined. Summing the finitely many base strata and taking the supremum over compact subsets of any Borel subset of $S$ gives $h_p(y)\le f_i(F_i(p,y))|\det DT_i(y)|$ almost everywhere on $S$. This last comparison follows by integrating over Borel subsets and holds even if the weighted area integral is infinite on some sets.

Partition $S$ into finitely many joint strata where all $B_i$ are constant. At Lebesgue-almost every point of any stratum the slice maps are differentiable and the stratum has density one. A differentiable function constant on a set of density one at the point has zero derivative there, since a nonzero derivative would exclude a cone of fixed positive relative volume near the point. Apply this to each $B_i$ and to $\sum_i\lambda_i T_i(y)-y$. Thus $D_y F_i=(0,DT_i)$ and $\sum_i\lambda_i DT_i=I_d$ almost everywhere on $S$. The convex-gradient pullback lemma applies with the smooth map $y\mapsto \lambda_i\nabla\phi(p,y)$. With $H=D^2_{yy}\phi(p,y)>0$, it gives that $\lambda_i H DT_i$ is symmetric positive semidefinite, since the off-diagonal Hessian blocks multiply the zero base derivatives. Consequently $C_i=H^{1/2}DT_iH^{-1/2}$ are symmetric positive semidefinite, $\sum_i\lambda_i C_i=I_d$, and $\det C_i=|\det DT_i|$ there.

The marginal identities give $F_i(p,y)\in E_i$ and $f_i(F_i(p,y))>0$ for $\rho_p$-almost every $y$, since $\gamma_i$ charges neither $K_i\setminus E_i$ nor $\{f_i=0\}$. On $\{h_p>0\}$ the same holds Lebesgue-almost everywhere. At those points eigenvalue arithmetic-geometric mean gives
$$
h_p^{1/d}\sum_i\lambda_i f_i(F_i(p,y))^{-1/d}
\le \sum_i\lambda_i(\det C_i)^{1/d}
\le \sum_i\lambda_i\frac{\operatorname{tr}C_i}{d}=1.
$$
Apply the assumed all-tuples inequality to these endpoints, whose weighted average is $(p,y)$, to obtain $h_p\le g(p,\cdot)$ almost everywhere. The inequality is automatic where $h_p=0$. The possible infinity set of $g$ is $\sigma_P$-null by its finite integral and is $\rho$-null by slice absolute continuity. This proves domination for every such surplus maximizer.

Let $\mathcal D$ be the couplings on $\prod_iK_i$ whose output is dominated by the fixed finite measure $g\sigma_P$. It is nonempty by the surplus result with $\phi(z)=|z|^2$. It is convex and weakly compact, since the marginals are fixed and the output inequality is weakly closed by testing nonnegative continuous functions on $K$. Any finite convex $u$ on $\mathbb R^{n+d}$ admits smooth uniformly strongly convex approximants converging uniformly on $K$, by convolution with a smooth nonnegative approximate identity followed by addition of a positive quadratic with coefficient tending to zero. For every approximant its maximum over $\mathcal D$ is at least its value at $\pi_0$. Taking uniform limits gives $\max_{\pi\in\mathcal D}\int u\,d(b_\#\pi)\ge\int u\,d(b_\#\pi_0)$. For finitely many tests the compact convex set of integral difference vectors must intersect the closed nonnegative orthant. Otherwise strict separation gives a nonnegative combination of those tests with maximum difference strictly negative, contradicting the one-test comparison. Compactness and the finite-intersection property now give one coupling satisfying all tests. Any coupling has its tuples in $\prod_i(E_i\cap\{f_i>0\})$ almost everywhere, so the stated base integrality condition gives integer output.
