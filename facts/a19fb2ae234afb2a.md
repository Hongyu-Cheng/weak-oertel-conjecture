---
fact_id: a19fb2ae234afb2a
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-strict-triangle-signed-row-deficit
depends_on: []
verifier_run: 5337b0806e75b9c4
target_match: null
---

## Source

- [919c51f1d263878e](../candidates/919c51f1d263878e.json), §§1–3, (1)–(10).

## Statement

Let $K$ be a nondegenerate planar triangle, let $y\in\operatorname{int}K$, and let the nonzero spanning normals $v_1,v_2,v_3$ satisfy $\sum_i v_i=0$. Suppose the cap $v_i\cdot(x-y)\ge0$ strictly captures $P_i$ and strictly excludes the other two vertices, with $P_1,P_2,P_3$ distinct. Use indices modulo three. Put $q_i=|K\cap\lbrace v_i\cdot(x-y)\ge0\rbrace|/|K|$, $\sigma_i=\mathcal H^1(K\cap\lbrace v_i\cdot(x-y)=0\rbrace)/\lVert v_i\rVert$, and $\lambda_i=(1/\sigma_i)/\sum_\ell(1/\sigma_\ell)$.

Set $H=\sum_\ell v_\ell\cdot(P_\ell-y)$, $a_i=v_i\cdot(P_i-y)/H$, and $b_{ij}=-v_i\cdot(P_j-y)/H$ for $j\ne i$. All $a_i,b_{ij}$ are positive. With $d_i=b_{i,i+1}-b_{i,i+2}$, $g_i=1-d_{i+1}+d_{i+2}$, and $f_i=2a_i/\sqrt{q_i}$, the identities are
$$
\sum_i a_i=1,\qquad a_j=\sum_{i\ne j} b_{ij},\qquad
q_i=\frac{a_i^2}{(a_i+b_{i,i+1})(a_i+b_{i,i+2})},\qquad f_i=\sqrt{g_i^2-d_i^2},
$$
and
$$
\sum_i f_i\sqrt{q_i}=2,\qquad
\lambda_i=\frac{f_i/\sqrt{q_i}}{\sum_\ell f_\ell/\sqrt{q_\ell}}.
$$
For each $i$, with $\{j,k\}=\{1,2,3\}\setminus\{i\}$, the deficit satisfies
$$
2-f_i-\frac{(f_j+f_k)^2}{4}
=\frac{d_i^2}{g_i+f_i}
 +\frac{(g_jd_k+g_kd_j)^2}{2(g_jg_k+d_jd_k+f_jf_k)}\ge0.
$$
Equality holds precisely when $d_i=0$ and $d_j+d_k=0$, in which case $f_j=f_k$. Equivalently, writing $Q=\sum_\ell\lambda_\ell q_\ell$, the row inequalities are
$$
2\lambda_i\sqrt{q_i}\,Q+
  (\lambda_j\sqrt{q_j}+\lambda_k\sqrt{q_k})^2\le2Q^2 .
$$

## Proof

The normalization gives $\sum_i a_i=1$. The normals sum to zero, so the signed margins in each column sum to zero, giving $a_j=\sum_{i\ne j}b_{ij}$. Set $s_i=b_{i,i+1}+b_{i,i+2}$. Then $\sum_i s_i=1$, and
$$
2a_i+s_i=s_i+(s_{i+1}-d_{i+1})+(s_{i+2}+d_{i+2})=g_i.
$$
In particular $\sum_i g_i=3$ and $g_i>|d_i|$. The cap is a corner triangle whose intercept fractions on the two incident edges are $a_i/(a_i+b_{i,i+1})$ and $a_i/(a_i+b_{i,i+2})$. Their product gives $q_i$. Thus $f_i^2=4(a_i+b_{i,i+1})(a_i+b_{i,i+2})=g_i^2-d_i^2$, and $\sum_i f_i\sqrt{q_i}=2\sum_i a_i=2$.

Fix $i$ and take $j=i+1$, $k=i+2$. The identities $g_j+g_k=3-g_i$ and $(d_j-d_k)^2=(1-g_i)^2$ give
$$
4(2-g_i)-(f_j+f_k)^2
=(g_j+g_k)^2-(d_j-d_k)^2-(f_j+f_k)^2
=2(g_jg_k+d_jd_k-f_jf_k).
$$
Here $g_jg_k+d_jd_k>0$, and
$(g_jg_k+d_jd_k)^2-f_j^2f_k^2=(g_jd_k+g_kd_j)^2$. Rationalizing the last difference proves that it is nonnegative, hence $g_i<2$ since $f_j+f_k>0$. Dividing the displayed identity by four and adding $g_i-f_i=d_i^2/(g_i+f_i)$ gives the deficit formula. Both denominators are positive. For equality the first square forces $d_i=0$. In that case $g_jd_k+g_kd_j=(d_j+d_k)(2-g_i)$, so vanishing of the second square is equivalent to $d_j+d_k=0$. These conditions imply $g_j=g_k$ and $d_j^2=d_k^2$, hence $f_j=f_k$.

The actual corner has area $|K|q_i=\sigma_i H a_i/2$, because its altitude is $Ha_i/\lVert v_i\rVert$. Therefore $1/\sigma_i$ is proportional to $a_i/q_i=f_i/(2\sqrt{q_i})$. Also $Q=\sum_\ell\lambda_\ell q_\ell$ gives $a_i=\lambda_i q_i/Q$ and $f_i=2\lambda_i\sqrt{q_i}/Q$. This substitution gives the row inequalities in chord form.
