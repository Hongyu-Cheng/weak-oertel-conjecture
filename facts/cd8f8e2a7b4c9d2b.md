---
fact_id: cd8f8e2a7b4c9d2b
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-least-active-tetrahedral-one-hole-incidence
depends_on: ["10916437d7f6301d", "643b08457d03e63b", "5097879468363a7e", "8bdcdcd6e2fa69d9", "1cdceac089be44d8", "63c38ebdb1d43777"]
verifier_run: 78f45c527fdfb2e6
target_match: null
---

## Source

- [58f8bbb67f63ee23](../candidates/58f8bbb67f63ee23.json), §3, (4), one-hole necessary incidence.

## Statement

Let $\phi_3$ be the row capacity $\inf_{t>0:F_x(t)>0}t/F_x(t)^{1/3}$ for $F_x(t)=\Pr(x\cdot U\le t)$ with $U$ uniform on the barycentric tetrahedron. Maximize $\sum_i\omega_i\phi_3(X_i)$ for fixed $\omega_i>0$ over nonnegative $4\times4$ matrices whose column sums equal one. Among the maximizers choose $X$ with the fewest nonzero rows. Suppose it has exactly two strictly positive rows $x,y$, one row $z$ with exactly one zero at column $h$, and one identically zero row.

Then $x,y$ have proper minimizing cuts and share an actual section centroid $b$. One has $b_h>1/3$. Exactly one of the two cuts strictly captures vertex $h$ and the other strictly excludes it. The excluding row has a direction of strictly positive optimized capacity Hessian. Here a vertex $j$ is strictly captured by a row $u$ when $u_j<t_u$ at its minimizing threshold, and strictly excluded when $u_j>t_u$.

## Proof

This global maximum is a local maximum for the square stochastic problem with strictly positive weights, so the accepted full-cut exclusion applies. If either full row attained a full-cut minimum, it would saturate at least three columns, inconsistent with the other full row. Thus both minima are proper. Apply the common section-centroid lemma to the two proper full rows and the boundary multiplier lemma to $z$. They give a common positive probability vector $b$ with $b_j\le1/3$ for $j\ne h$. Define $t_u=b\cdot u$ for $u=x,y,z$, which is the actual minimizing threshold for $x$ and $y$. In particular $t_z>0$. The column sums and $z_h=0$ give
$$
(t_x-x_h)+(t_y-y_h)=-t_z<0.
$$
Thus one of $x,y$ strictly excludes $h$.

For either full row that weakly excludes $h$, the accepted Schur law gives local $C^2$ capacity and at least two strictly captured vertices of its proper minimizing cut. All such vertices have $b_j\le1/3$ because none is $h$. The corrected central-pair lemma therefore gives a positive Hessian direction at that row normalized by its positive threshold. Degree-one homogeneity scales the Hessian back to the actual row by a positive factor, preserving its sign. If $b_h\le1/3$, the same argument gives a positive direction for each full row even if it captures $h$.

The joint positive-index bound applies at the chosen maximum with $k=3$ active rows and $m=4$, and each full row has positive weight. Two rows with positive directions would give $3+1+1\le4$, a contradiction. Hence $b_h>1/3$, and the other full row cannot weakly exclude $h$. It must strictly capture $h$. The strictly excluding row has the positive direction already established.
