---
fact_id: 12beddcf16788fff
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-regular-support-face-surface-jacobian
depends_on: []
verifier_run: f43f331c620aaec3
target_match: null
---

## Source

- [316afa5f01281a91](../candidates/316afa5f01281a91.json), §§1–4, 6, 8, (1)–(11).

## Statement

Let $K_-,K_0,K_+\subset\mathbb R^d$ be convex bodies with $(K_-+K_+)/2\subset K_0$. Let $n:U\subset\mathbb R^k\to\mathbb S^{d-1}$ be a $C^2$ injective immersion of rank $k$ on an open set, let $m=d-1-k$, and assume $h_i(t)=h_{K_i}(n(t))$ is $C^2$ for each body. Suppose the actual support faces at $n(t)$ have affine dimension $m$, and their relative interiors give regular boundary patches with the indicated unique normal and ordinary surface measure given by the area Jacobian of the one-to-one affine-face parametrizations below. Use common orthonormal frames $N(t)$ of $\operatorname{im}Dn(t)$ and $E(t)$ of $L(t)=\ker n(t)^{\mathsf T}\cap\ker Dn(t)^{\mathsf T}$ locally. For the canonical perpendicular origins $a_i(t)$ of the affine face hulls and points $X_i(t,s)=a_i(t)+E(t)s$ on those faces, put $R=N^{\mathsf T}Dn$ and $Q_i(t,s)=D^2h_i(t)-\sum_j X_{i,j}(t,s)D^2 n_j(t)$. For $k>0$, the $Q_i$ are positive semidefinite and the actual marked surface densities relative to the common $dt\,ds$ are $J_i=\det Q_i/|\det R|$.

Write $Z=\{t:h_0(t)=(h_-(t)+h_+(t))/2\}$. At Lebesgue-almost every $t\in Z$, and at every point of an open tight chart, $a_0=(a_-+a_+)/2$. For every endpoint face pair at such a parameter, its physical midpoint is $X_0(t,s_0)$ with $s_0=(s_-+s_+)/2$, and $Q_0(t,s_0)=(Q_-(t,s_-)+Q_+(t,s_+))/2$. For $k>0$ this gives
$$
J_0(t,s_0)^{1/k}\ge \frac{J_-(t,s_-)^{1/k}+J_+(t,s_+)^{1/k}}2.
$$
If $m>0$, in particular $J_0(t,s_0)\ge ((J_-(t,s_-)^{-1/m}+J_+(t,s_+)^{-1/m})/2)^{-m}$, with zero on the right if either input is zero. For $m=0$ the conditional densities are singleton masses and $J_0\ge\min(J_-,J_+)$. For $k=0$ the fixed normal has unit Euclidean facet density, including unit endpoint counting mass when $d=1$.

## Proof

For any fixed point $X$ of the actual $i$-th support face at $n(t)$, the nonnegative function $h_i(t')-n(t')\cdot X$ vanishes at $t$. Its value and first derivative give $n^{\mathsf T}X=h_i$ and $Dn^{\mathsf T}X=\nabla h_i$. The common linear system has kernel $L$ and full row rank because $n$ is orthogonal to the rank-$k$ derivative $Dn$. By the dimension hypothesis its solution plane is exactly the actual affine face hull. The minimum-norm solution $a_i$ is linear in $(h_i,\nabla h_i)$ at each $t$ and $C^1$ locally. Local $C^1$ orthonormal frames follow by orthonormalizing local independent columns for the two subspaces. The second derivative of the same nonnegative function at its minimum gives $Q_i\ge0$.

Differentiate the two linear identities along $X_i(t,s)$ for fixed $s$ to obtain $n^{\mathsf T}D_tX_i=0$ and $Dn^{\mathsf T}D_tX_i=Q_i$. Also $D_sX_i=E$. In the orthonormal tangent frame $[N,E]$ the column matrix $[D_tX_i,D_sX_i]$ has blocks $[A_i,0;B_i,I]$ with $A_i=N^{\mathsf T}D_tX_i$. Since $Dn=NR$, $R^{\mathsf T}A_i=Q_i$. Its area Jacobian is $|\det A_i|=\det Q_i/|\det R|$, which equals the ordinary surface density by the chart hypothesis. Both the transverse reference $dt$ and the denominator are common to all three bodies.

The support gap $g=h_0-(h_-+h_+)/2$ is nonnegative on $U$ and has gradient zero at every contact point. Its Hessian vanishes at Lebesgue density points of $Z$. Otherwise this positive semidefinite Hessian would have a strictly positive quadratic form on a cone of directions, and Taylor expansion would exclude from $Z$ a fixed positive fraction of every small ball about the point, contradicting density one. Hence $h_0$ and the endpoint average have equal values, gradients and Hessians at almost every contact. In an open tight chart these equalities hold everywhere by differentiation. Equality of the origins follows from the common linear system. The physical average of any two endpoint face points belongs to $K_0$ by inclusion and has height $h_0(t)$ by contact, so it is on the actual middle face with the claimed coordinate. The formula for $Q_i$ now gives the midpoint matrix identity.

For positive definite $A$ and $B$, conjugate $B$ by $A^{-1/2}$ and denote the eigenvalues by $\lambda_j>0$. Jensen's inequality for $x\mapsto\log(1+e^x)$ applied to $\log\lambda_j$ gives $\prod_j(1+\lambda_j)\ge (1+(\prod_j\lambda_j)^{1/k})^k$. Thus $\det(A+B)^{1/k}\ge\det(A)^{1/k}+\det(B)^{1/k}$, including positive semidefinite matrices by continuity. Apply this to the midpoint identity and the common denominator. The positive-order power mean dominates the geometric mean, which dominates the negative-order mean for $m>0$ and the minimum for $m=0$. When $k=0$, the actual facet lies in a fixed affine hyperplane and orthonormal coordinates give its unit area density directly. In dimension one the fixed normal marks one endpoint of unit counting mass.
