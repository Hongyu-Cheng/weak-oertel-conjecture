---
fact_id: ebfd6e85ec9d02a4
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-canonical-simplex-facet-affine-neutrality
depends_on: []
verifier_run: 59a96d2e52826a03
target_match: null
---

## Source

- [00208e2b45f0da1a](../candidates/00208e2b45f0da1a.json), 00208e2b45f0da1a:02 §2, (1)–(4), facet moment rigidity.

## Statement

Let $K=\operatorname{conv}(v_0,\ldots,v_d)$ be a $d$-simplex, $d\ge1$, with barycentric coordinates $\lambda_j$. Let $y\in\operatorname{int}K$, $q_j=\lambda_j(y)$, and suppose the own-fiber cuts of a regular ambient circuit are $H_j\cap K=\{x\in K:\lambda_j(x)\ge q_j\}$. Let $\theta_j>0$, $\sum_j\theta_j=1$, and put $W=\sum_j\theta_j\mathbf1_{H_j}$. In an actual regular equal-budget circuit, with unit continuous normals and circuit coefficients $\rho_j$, use $\theta_j=(\rho_j/S_j)/\sum_h(\rho_h/S_h)$ where $S_j>0$ is the total proper section coarea over **all** measured fibers. Regularity excludes positive-area cap/fiber facet coincidences.

Suppose $\beta>0$ and $\int_{F_i}\psi(W-\beta)\,d\mathcal H^{d-1}=0$ for every affine $\psi$ on every facet $F_i$. Then $\beta=\Gamma_d=(d/(d+1))^d$ and $\theta_j=1/(d+1)$ for every $j$. If $d\ge2$, also $y$ is the centroid.

## Proof

On $F_i$ the $i$th cap is empty. For $j\ne i$ it cuts the homothetic facet simplex $q_jv_j+(1-q_j)F_i$, of relative area $(1-q_j)^{d-1}$ and centroid $q_jv_j+(1-q_j)g_i$, where $g_i$ is the centroid of $F_i$. These formulas include the singleton facets in $d=1$ with counting measure. The constant tests give $\sum_{j\ne i}\theta_j(1-q_j)^{d-1}=\beta$. Subtraction between facets gives $\theta_j(1-q_j)^{d-1}=\beta/d$ for every $j$. If $d=1$ this yields equal weights and $\beta=1/2$.

For $d\ge2$ test each coordinate of $x-g_i$. Since the uniform facet moments vanish and each cap area with its weight is the same, this gives $\sum_{j\ne i}q_j(v_j-g_i)=0$. In terms of the affinely independent vertices of $F_i$ this is a relation whose coefficients are $q_j-d^{-1}\sum_{k\ne i}q_k$, with sum zero. They all vanish. Every pair belongs to a common facet when $d\ge2$, so all $q_j$ are equal, hence $q_j=1/(d+1)$. Substituting in the constant-test identity and using $\sum_j\theta_j=1$ gives the uniform weights and $\beta=\Gamma_d$.
