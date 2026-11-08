---
fact_id: d9d8bb5ad9cae2bf
kind: counterexample
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-r4-critical-stress-projected-nonclosure
depends_on: ["cb254ea93a82679e", "7559aec0ef3647a6", "1f0d0be4d3e71529"]
verifier_run: 90ceed5f9da8e389
target_match: null
---

## Source

- [8ac2ff347361aad9](../candidates/8ac2ff347361aad9.json), 8ac2ff347361aad9:03 §3, (3)–(4), fixed-facet exact moments.

## Statement

Take $P=\operatorname{conv}\{(-4,-4),(4,0),(0,4)\}\cap\mathbb Z^2$ and any nondegenerate planar triangle $K$ of centroid $g$ with barycentric functions $\lambda_j$, $j=0,1,2$. Define $\ell(z)=(-z_1-z_2,2z_1-z_2,2z_2-z_1)$ and $W=(1/3)\sum_j\mathbf1_{\{\lambda_j(x)-1/3+\ell_j(z)\ge0\}}$ on the measured boundary of $P\times K$. Let $\eta$ be the sum of facet arclengths marked by the continuous normal, $\beta=40/93$, and $\nu=(W/\beta)\eta$. The three caps are globally critical at $(0,g)$ and have common coarea centroid $(0,g)$. A normal-preserving physical martingale from $\nu$ to $\eta$ exists. On the old facet $\lambda_0=0$ of length $L$, the restriction of $\eta-\nu$ has projected mass coefficient $L(27-31h_z)/120$ at $z$, where $h_z$ counts the thirds of that facet on which $W(z,\cdot)=2/3$. Its projected mass and first moments vanish and its second-moment matrix is $(L/120)\begin{pmatrix}1420&524\\524&1420\end{pmatrix}$. Every such normal-preserving martingale has projected displacement energy $(71/3)L$ on that normal, so none is stationary in the base.

## Proof

The stated geometry, actual depth, cap regularity and section centroids are those of cb254ea93a82679e. For the coupling, on the thirds of the facet $\lambda_0=0$ use the affine parameterization $\lambda_1=(r+s)/3$, $\lambda_2=1-\lambda_1$, with $0<r<1$ and $s=0,1,2$. The rational matrix in 7559aec0ef3647a6 transports the excess high-tier sources to the deficit low-tier targets, at fixed $r$, with row weights $22$ and column weights $9$ and row barycenters in the physical base and tier coordinates. The signed difference of $\nu$ and $\eta$ has coefficients $22/40$ on high tiers and $-9/40$ on low tiers relative to arclength. Multiply the matrix by $1/40$ and the common arclength factor $L\,dr/3$, then add the common part on the diagonal. Its physical row means are preserved by the affine parameterization. The same edge symmetry supplies the coupling on the other facets, separately at each normal.

For each base and tier, the actual cap count is
$$
3W=|\{j:\ell_j(z)>0\}|+
\mathbf1_{\{\ell_1(z)=0,\ s\ge1\}}+
\mathbf1_{\{\ell_2(z)=0,\ s\le1\}}.
$$
This follows because positive integer offsets give full traces, negative integer offsets give empty traces, and zero offsets require the corresponding barycentric value to be at least $1/3$. The omitted endpoints have arclength zero. On the retained bases this count is one or two. Thus the mean profile at $z$ is $1/3+h_z/9$, and
$1-(1/3+h_z/9)/\beta=(27-31h_z)/120$.

For an explicit exact census, at each integer $z_1$ between $-4$ and $4$, loop over $-4\le z_2\le4$ with $\min_j\ell_j(z)\ge-4$. Compute $h_z=\sum_{s=0}^2\mathbf1_{\{3W=2\}}$ by the displayed formula. The sums of $27-31h_z$ times the indicated monomials are as follows.

| $z_1$ | $1$ | $z_1$ | $z_2$ | $z_1^2$ | $z_1z_2$ | $z_2^2$ |
|---:|---:|---:|---:|---:|---:|---:|
| -4 | 27 | -108 | -108 | 432 | 432 | 432 |
| -3 | 54 | -162 | -135 | 486 | 405 | 351 |
| -2 | -47 | 94 | -100 | -188 | 200 | 316 |
| -1 | -20 | 20 | 124 | -20 | -124 | 22 |
| 0 | -28 | 0 | 468 | 0 | 0 | 480 |
| 1 | -20 | -20 | -82 | -20 | -82 | 64 |
| 2 | -47 | -94 | -194 | -188 | -388 | -272 |
| 3 | 54 | 162 | 27 | 486 | 81 | 27 |
| 4 | 27 | 108 | 0 | 432 | 0 | 0 |

Summing the columns gives $(0,0,0,1420,524,1420)$. Any normal-preserving martingale restricts to a martingale on the fixed facet bundle, since the normal is a source mark and is preserved by the transport. Its target is the full restricted $\eta$, so the projected second-moment identity gives its displacement energy as the trace of the matrix, $(2840/120)L=(71/3)L$.
