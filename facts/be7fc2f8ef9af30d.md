---
fact_id: be7fc2f8ef9af30d
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-simplex-corner-cap-coareas-and-row-variance
depends_on: []
verifier_run: 510e0b5ebd0d9389
target_match: null
---

## Source

- [bbd1a18ecbb9d3f0](../candidates/bbd1a18ecbb9d3f0.json), bbd1a18ecbb9d3f0:01 §§1–2, (1)–(4), and §6, d=1.

## Statement

Let $K$ be a $d$-simplex, $d\ge1$, with vertices $P_i$, $1\le i\le d+1$, and $y\in\operatorname{int}K$. Suppose nonzero spanning normals $v_i$ sum to zero and satisfy $v_i\cdot(P_i-y)>0>v_i\cdot(P_j-y)$ for every $j\ne i$. Set
$$
H=\sum_i v_i\cdot(P_i-y),\qquad
a_i=\frac{v_i\cdot(P_i-y)}H,\qquad b_{ij}=-\frac{v_i\cdot(P_j-y)}H\quad(j\ne i).
$$
Then all these entries are positive, $\sum_i a_i=1$ and $\sum_{i\ne j}b_{ij}=a_j$. If $q_i$ is the volume fraction of the cap with margin $v_i\cdot(x-y)\ge0$ and $\sigma_i$ is the section's $(d-1)$-measure divided by $\|v_i\|$, then
$$
q_i=\frac{a_i^d}{\prod_{j\ne i}(a_i+b_{ij})},\qquad
\sigma_i=\frac{d|K|q_i}{Ha_i}.
$$
With $f_i=d a_i/q_i^{1/d}$ and $g_i=d a_i+\sum_{j\ne i}b_{ij}$, the inverse coareas are proportional to $f_i/q_i^{(d-1)/d}$, $f_i\le g_i$, $\sum_i g_i=d+1$, and
$$
d+1-\sum_i f_i\ge\frac1d\sum_i\ \sum_{\substack{j<k\\j,k\ne i}}\!
  \left(\sqrt{a_i+b_{ij}}-\sqrt{a_i+b_{ik}}\right)^2 .
$$
For $d=1$ the two row values are $f_1=f_2=1$.

## Proof

The sign hypotheses and definition of $H$ give positivity and $\sum_i a_i=1$. The equality $\sum_i v_i=0$ gives $\sum_{i\ne j}b_{ij}=a_j$ by evaluation at $P_j-y$. The corner cut intersects the edge from $P_i$ to $P_j$ at fraction $a_i/(a_i+b_{ij})$ measured from $P_i$. Its volume fraction is the product of these factors by the simplex determinant formula. Its apex is $P_i$ and its base is the section, with height $Ha_i/\|v_i\|$. The pyramid volume identity gives the coarea formula, including $d=1$ where the section is one point. Thus $1/\sigma_i=(H/(d^2|K|)) f_i/q_i^{(d-1)/d}$ with a common proportionality factor.

Write $x_j=a_i+b_{ij}$ for the $d$ entries of row $i$ other than its diagonal. Then $f_i=d(\prod_j x_j)^{1/d}$ and $g_i=\sum_jx_j$. Summing the column identities gives $\sum_i g_i=d+1$. AM–GM on the square roots gives
$$
\sum_jx_j-d\left(\prod_j x_j\right)^{1/d}
\ge\sum_jx_j-\frac{(\sum_j\sqrt{x_j})^2}d
=\frac1d\sum_{j<k}(\sqrt{x_j}-\sqrt{x_k})^2 .
$$
This proves the individual inequality and the summed budget. When $d=1$ the only entry of each row is $a_i+b_{ij}=a_i+a_j=1$.
