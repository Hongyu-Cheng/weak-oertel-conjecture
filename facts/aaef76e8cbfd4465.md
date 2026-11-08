---
fact_id: aaef76e8cbfd4465
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-sharp-simplex-product-residual-covariance-stress
depends_on: ["12b88d92b390d9db", "baee8ddaa588aef0"]
verifier_run: 296bf739d6fc6ab6
target_match: null
---

## Source

- [a5bd7e36a76479fe](../candidates/a5bd7e36a76479fe.json), a5bd7e36a76479fe:02 §§3–5, (2)–(5).

## Statement

Let $K\subset\mathbb R^d$ be a positive $d$-simplex, $d\ge1$, with volume $v$, centroid $g$ and uniform covariance $\Sigma_K$. Put $S=\{0,1\}^n\times K$ for $n\ge0$, with summed mass $M=2^nv$. Among covers by $2^n(d+1)$ closed caps with continuous normals normalized by the residual covariance, the minimum feasible normalized cap-mass budget is $\gamma_d/2^n$, where $\gamma_d=(d/(d+1))^d$. Isolated canonical centroid caps give a normal hinge stress at that budget with objective multiplier one and all budget multipliers zero. The total hinge at that cover is $M\gamma_d\sqrt{d(d+2)}$.

More generally consider any canonical centroid vertex cap of a simplex fiber, with barycentric gradient $\beta_i$ and centered vertex $w_i$. Suppose its positively weighted contacts lie at the own centroid and the cap has zero actual mass on all other fibers, with zero multiplied section moments from those fibers. Under any fixed positive definite normalization $\Sigma$, the remaining continuous cap balance for a positive objective multiplier requires
$$
\frac{w_i}{d+1}
=\frac{d\,\Sigma\beta_i}{(d+1)^2\,\beta_i^\top\Sigma\beta_i}.
$$
The displayed compatibility holds for all $d+1$ types exactly when $\Sigma$ is a positive scalar multiple of $\Sigma_K$.

## Proof

Let $\lambda_j$ be the barycentric coordinates and $\beta_j=\nabla\lambda_j$. The standard simplex monomial integrals give $\mathbb E[\lambda_i\lambda_j]=(1+\mathbf1_{i=j})/((d+1)(d+2))$ for uniform probability. For example the integral of $\prod_j\lambda_j^{k_j}$ divided by volume is $d!\prod_j k_j!/(d+\sum_j k_j)!$ by iterated one-variable beta integration. Expanding $X-g=\sum_j\lambda_jw_j$ and using $\sum_jw_j=0$ gives $\Sigma_K=\sum_j w_jw_j^\top/((d+1)(d+2))$. Since $\beta_i\cdot w_j=\mathbf1_{i=j}-1/(d+1)$, one gets
$$
\Sigma_K\beta_i=\frac{w_i}{(d+1)(d+2)},\qquad
\beta_i^\top\Sigma_K\beta_i=\frac{d}{(d+1)^2(d+2)}=:\kappa^2 .
$$
A canonical cap has cut $\lambda_i\ge1/(d+1)$, mass $c=\gamma_d v$, and centroid displacement $w_i/(d+1)$, by homothety about vertex $i$ at scale $d/(d+1)$. Its normalized own margin is $(\lambda_i-1/(d+1))/\kappa$, so its hinge divided by $c$ is $d/((d+1)^2\kappa)=\sqrt{d(d+2)}/(d+1)$. These identities give $c(w_i/(d+1))=\Psi_i\Sigma_K(\beta_i/\kappa)$ for an isolated canonical cap.

Independence of the product coordinates gives residual covariance $\Sigma_K$. A cap containing any fiber centroid has mass at least $c$ by the through-centroid cap bound of baee8ddaa588aef0, moving a containing cut to the centroid if necessary. For each $p\in\{0,1\}^n$, define the affine function $q_p(z)=\sum_k[(1-p_k)z_k+p_k(1-z_k)]$, zero at $p$ and at least one at every other binary base. Use the cap margins $(\lambda_i-1/(d+1)-2q_p)/\kappa$ for all $p,i$. They strictly miss every other source fiber and cover all continuous space at their own base since the barycentric coordinates sum to one. The budget is attained. At this budget, a cap containing a centroid is through it, because shifting a strictly containing plane removes a positive-volume slab. The equality case of baee8ddaa588aef0 forces a canonical type, spending the entire budget on that fiber. A cap missing the centroid misses a neighborhood. If type $i$ is absent at a centroid, a sufficiently small barycentric move increasing coordinate $i$ and decreasing every other coordinate misses every cap. Thus all types occur, and the prescribed count leaves exactly the local canonical caps. The same argument works with $n=0$ and no tilt. It follows that the hinge value of the explicit cover is also the hinge value of every cover at the sharp budget and count, since each cap contributes only its canonical own hinge.

For the explicit isolated cover set $\alpha_0=1$, $r_i=0$, and at each base take the centroid and uniform weights on its own $d+1$ types. Their continuous weighted normal is zero because the normalizing factors agree and $\sum_i\beta_i=0$. Their average margin on that fiber is identically zero, which makes the coverage constraint active and gives the saddle contact and the zero continuous normal in its normal cone. Take $\eta_z=(d+1)c$. The cap mass and base balances now hold directly. The centroid displacement identity above gives the covariance-normalized continuous balance, with sphere multipliers $-\Psi_i$. The total hinge over $2^n(d+1)$ caps is the stated value.

For a general normalization $\Sigma$, the canonical cap has continuous normal $\beta_i/\sqrt{\beta_i^\top\Sigma\beta_i}$. Its own section at $\lambda_i=1/(d+1)$ has centroid $g$, as is seen by averaging the $d$ points where this section meets the apex edges. The mass balance subtracts off the contact and own section terms from the continuous balance. The other fibers have zero cap mass and hence zero hinge contribution. Their multiplied section moments vanish by assumption. Thus the balance leaves $c w_i/(d+1)=\Psi_i\Sigma u_i$ after canceling a positive objective multiplier. The hinge-to-mass ratio with $\kappa$ replaced by $\sqrt{\beta_i^\top\Sigma\beta_i}$ gives the displayed equation.

Let $T=\Sigma_K^{-1/2}\Sigma\Sigma_K^{-1/2}$ and $v_i=\Sigma_K^{1/2}\beta_i$. The compatibility identity and the formula for $\Sigma_K\beta_i$ say that each $v_i$ is an eigenvector of $T$. Their mutual inner products are $-1/((d+1)^2(d+2))$ for distinct indices. A symmetric matrix has orthogonal eigenspaces for distinct eigenvalues, so all these eigenvalues agree. The gradients span $\mathbb R^d$ because barycentric coordinates determine the point, and hence $T$ is scalar. Conversely a positive scalar factor cancels from the compatibility identity, which holds for $\Sigma_K$.
