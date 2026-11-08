---
fact_id: fbc45df3df3e5d78
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-pk-w36-menu-circuit-overlap-geometry
depends_on: []
verifier_run: 5c97f8ca6ef0dfba
target_match: null
---

## Source

- [ebf5465656e86ce1](../candidates/ebf5465656e86ce1.json), ebf5465656e86ce1:01 §1, (1)–(2), exact circuit geometry.

## Statement

Let $d\ge2$ and let $r+1$ nonzero normals $u_j\in\mathbb R^d$ have rank $r$ and a positive dependence $\sum_j\lambda_j u_j=0$, with $\sum_j\lambda_j=1$. For affine margins $L_j(x)=u_j\cdot x+e_j$, put $c=\sum_j\lambda_j e_j\ge0$, $H_j=\{L_j\ge0\}$, $A=\bigcap_j H_j$, and $Ux=(u_j\cdot x)_j$. The $H_j$ cover $\mathbb R^d$. If $c=0$, then $A$ is the nonempty common solution flat $\{L_j=0\ \forall j\}$ with direction $\ker U$. If $c>0$, then $A$ is an $r$-simplex in an affine complement of $\ker U$, plus $\ker U$. Every $y\in A$ gives a closed through-$y$ cover $\{u_j\cdot(x-y)\ge0\}$ of $\mathbb R^d$ contained capwise in the original cover. For $r=d$ and $c>0$,
$$
\operatorname{vol}_d(A)=\frac{c^d}{d!\,|\det(u_1,\ldots,u_d)|\prod_{j=1}^d\lambda_j},
$$
where the displayed normals are determinant rows.

## Proof

The image of $U$ has rank $r$ and is contained in the hyperplane perpendicular to the dependence vector, hence equals it. Therefore the affine map $x\mapsto (\lambda_jL_j(x))_j$ surjects onto the hyperplane $\sum_j t_j=c$ with fibers parallel to $\ker U$. Its nonnegative part is the single point $t=0$ when $c=0$, and the $r$-simplex with vertices at the coordinate points with sole nonzero coordinate $c$ when $c>0$. Restricting the map to an affine complement gives an affine isomorphism with this simplex. The original weighted margin sum is nonnegative everywhere, so at least one original cap contains every point. For each $y\in A$, the margins $u_j\cdot(x-y)$ have weighted sum zero and hence cover the whole space with their closed nonnegative traces. Adding $L_j(y)\ge0$ recovers $L_j(x)$, proving each containment.

When $r=d$, any $d$ of the $d+1$ normals are independent: a dependence supported on only those rows would contradict the one-dimensional relation space spanned by the strictly positive weights. The map to the first $d$ weighted coordinates is then invertible with absolute Jacobian $|\det(u_1,\ldots,u_d)|\prod_{j=1}^d\lambda_j$. Its image of $A$ is the coordinate simplex $t_j\ge0$, $\sum_{j=1}^d t_j\le c$ of volume $c^d/d!$. Dividing by the Jacobian proves the formula.
