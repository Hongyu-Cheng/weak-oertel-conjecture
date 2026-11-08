---
fact_id: edb8f4e5b0dca345
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-simplex-vertex-section-balance-formula
depends_on: []
verifier_run: fd3a63fd130646ba
target_match: null
---

## Source

- [1f45640ee74685ef](../candidates/1f45640ee74685ef.json), §1, (1)–(4), vertex section data and unique weights.

## Statement

Let $T$ be a $d$-simplex, $d\ge2$, and let $y$ have interior barycentric coordinates $\lambda_i>0$ for $0\le i\le d$. A plane with actual section centroid $y$ and only vertex $i$ strictly on its cap side exists exactly when $\lambda_j\le1/d$ for every $j\ne i$, and is unique in that orientation. It meets the edge from $i$ to $j$ at parameter $d\lambda_j$, allowing an endpoint. Its cap fraction is $f_i=d^d\prod_{j\ne i}\lambda_j$. For varying barycentrics $\xi$, put $u_i=\nabla(d-\sum_{j\ne i}\xi_j/\lambda_j)$, with gradient taken in the affine hull. The inward unit normal multiplied by section area and divided by $|T|$ is $f_i u_i$.

If all $\lambda_i\le1/d$, set $t_i=1-d\lambda_i$ and $D=\sum_i\lambda_i t_i=1-d\sum_i\lambda_i^2>0$. The effective section vectors have rank $d$. The unique nonnegative probability weights on the vertex-side caps with $\sum_i\theta_i f_i u_i=0$ are $\theta_i=\lambda_i t_i/D$. Their mean cap fraction is
$$
F_d=\frac{d^d\prod_i\lambda_i}{D}
=\frac{\prod_i(1-t_i)}{2\sum_{i<j}t_i t_j}.
$$

## Proof

The edge intersection from $i$ to $j$ is $(1-r_j)v_i+r_jv_j$ for $0<r_j\le1$, and these $d$ points form the section simplex. Its $j$-th centroid coordinate for $j\ne i$ is $r_j/d$, giving $r_j=d\lambda_j$. Conversely if those parameters are at most one, the margin $d-\sum_{j\ne i}\xi_j/\lambda_j$ gives exactly this section and has only vertex $i$ strictly positive. The cap simplex has volume fraction $\prod_{j\ne i}r_j=f_i$ by the edge determinant. It is a pyramid over the section with height $d/\lVert u_i\rVert$, so its volume is section area divided by $\lVert u_i\rVert$. This argument also works for endpoint intersections. Multiplying by the inward unit normal gives the normalized effective vector $f_i u_i$.

In a relation $\sum_i a_i u_i=0$, let $a=\sum_i a_i$. The only relation among the barycentric gradients is their sum, so $(a-a_j)/\lambda_j$ is independent of $j$. Summing $a-a_j$ over $j$ shows that this constant is $da$. Thus $a_j=a(1-d\lambda_j)=at_j$; conversely these coefficients give a relation. All $t_i$ are nonnegative and sum to one, so $D>0$. Apply the relation to $a_i=\theta_i f_i$, use $f_i\lambda_i=d^d\prod_j\lambda_j$, and normalize $\sum_i\theta_i=1$. This gives $\theta_i=\lambda_i t_i/D$, including any zero weights, and the first mean formula. Since $dD=\sum_i (1-t_i)t_i=2\sum_{i<j}t_i t_j$, the second follows.
