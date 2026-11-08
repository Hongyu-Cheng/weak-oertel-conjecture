---
fact_id: c19afecc57cdc194
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-paired-tetrahedral-stationary-triangle-and-parallel-quad
depends_on: ["290ddd8516d76865", "edb8f4e5b0dca345"]
verifier_run: 13757cfff7253ea1
target_match: null
---

## Source

- [c9d05a8f728258ce](../candidates/c9d05a8f728258ce.json), Theorem and §§1–4, (1)–(11), prescribed quadrilateral and all available vertex sections.

## Statement

Let $T$ be a tetrahedron and let $y$ have interior barycentric coordinates $(a,a,b,b)$ with $a+b=1/2$. Allow both orientations of the quadrilateral section $\xi_0+\xi_1=2a$ and both orientations of every vertex-isolating section with Euclidean section centroid $y$, allowing vertices on its boundary. For any finite probability weights $\theta_j$ on these closed caps, write $S_j$ for the section area, $u_j$ for the inward unit normal, and $F_j$ for the cap volume divided by $|T|$. If $\sum_j\theta_j S_j u_j=0$, then $\sum_j\theta_j F_j\ge27/64$. Equality is attained when $a=b=1/4$ on the four equal-weight vertex-side caps. The inequality is strict if a quadrilateral orientation has positive weight.

## Proof

Use effective section vectors $q_j=S_ju_j/|T|$. Under an invertible affine map with linear part $L$, these vectors transform by $L^{-\mathsf T}$, and cap fractions are invariant. This follows from the transformation of area vectors by $|\det L|L^{-\mathsf T}$. In particular both balance and the mean are preserved when the tetrahedron vertices are permuted.

Put $U=\nabla(\xi_0+\xi_1)$. Fact 290ddd8516d76865 at $d=3$, $k=2$ gives density $6r(1-r)$ for $r=\xi_0+\xi_1$, so the cap $Q$ with $r\ge2a$ has fraction $F_Q=1-12a^2+16a^3$ and vector $Q_0 U$ with $Q_0=24ab>0$, by coarea at $r=2a$. The section centroid is $y$ because it is fixed by the two pair swaps and belongs to $r=2a$. Reversal gives fraction $1-F_Q$ and vector $-Q_0U$.

By edb8f4e5b0dca345, a vertex-isolating section is available precisely when every other barycentric coordinate is at most $1/3$. As the coordinates occur in equal pairs, either all four exist, which is equivalent to $a,b\le1/3$, or none exists, in which case only $Q$ and its reverse are available and balance gives mean $1/2$. In the former case $a,b\in[1/6,1/3]$. The vertex-side cap fractions are $F_A=27ab^2$ in the first pair and $F_B=27a^2b$ in the second. The same accepted formula gives $q_i=F_i\nabla(3-\sum_{j\ne i}\xi_j/\lambda_j)$ with $\lambda=(a,a,b,b)$. The mean vectors within the two pairs are $AU$ and $-BU$, where
$$
A=\tfrac{27}{2}b(2a-b),\qquad B=\tfrac{27}{2}a(2b-a).
$$
Indeed the sum of the first two raw gradients is $(2/b-1/a)U$, and the second pair is obtained by swapping the roles of $a,b$ and replacing $U$ by $-U$.

Average the weights over the two independent swaps of vertices within each pair. They fix $y$ and the $Q$ orientations, and permute the other allowed caps. By the affine transformation law the balance is retained. The mean is unchanged, and each pair of equal-fraction vertex types now has its mean vector. The positive scalar types (speed, fraction) are $(A,F_A),(B,1-F_B),(Q_0,F_Q)$ and the negative types are $(A,1-F_A),(B,F_B),(Q_0,1-F_Q)$. Any zero-speed type occurs at an endpoint of the parameter range and has fraction $1/2$; set it aside.

A balanced mixture of the remaining types decomposes into balanced pairs. If the probabilities and speeds on the two sides are $p_i,s_i$ and $r_j,t_j$, their total fluxes agree at $L_0=\sum_i p_i s_i=\sum_j r_j t_j$. When $L_0>0$, assign flux $(p_i s_i)(r_j t_j)/L_0$ to each pair $(i,j)$ and divide by the corresponding speed for each side to recover the original probabilities. A pair has mean $(t_j F_i+s_iG_j)/(s_i+t_j)$, where $F_i,G_j$ are its two fractions. If $L_0=0$ only the discarded zero-speed types occur.

The three cap-and-complement pairs have mean $1/2$. The vertex-side pair has mean
$$
R=\frac{BF_A+AF_B}{A+B}=\frac{27a^2b^2}{1-6(a^2+b^2)},
$$
and its reverse has mean $1-R$. Writing $t=ab\in[1/18,1/16]$ gives denominator $12t-1/2>0$. The lower bound $R\ge27/64$ is equivalent to $64(t-1/16)(t-1/8)\ge0$; the upper bound $R\le1/2$ is equivalent to $54(t-1/18)(t-1/6)\le0$. The pair of $Q$ with the second-pair vertex side has mean
$$
f(a)=\frac{BF_Q+Q_0F_B}{B+Q_0},\qquad
f(x)=\frac{9(1-3x+4x^3)}{17-43x}.
$$
By exchanging the pairs the first-pair vertex side and the reverse of $Q$ give $f(b)$. Their reverses give $1-f(a)$ and $1-f(b)$. These are the remaining four pair means, restricted to nonzero speeds as above.

For $1/6\le x\le1/3$ the denominator is positive. The identities
$$
\tfrac12-f(x)=\frac{(1-3x)(24x^2+8x-1)}{2(17-43x)},\qquad
f(x)-\tfrac49=\frac{13-71x+324x^3}{9(17-43x)}
$$
show $4/9<f(x)\le1/2$: the quadratic in the first numerator is increasing and equals one at $1/6$; the cubic in the second has minimum $13-71\sqrt{213}/81>0$ on the nonnegative axis, since $1053^2-71^2\cdot213=35076>0$. Both a mixed pair and its reverse thus have mean strictly greater than $27/64$. A positive quadrilateral weight contributes to at least one pair of strictly larger mean, since $Q_0>0$. Combining all pairs gives the bound. At $a=b=1/4$ the four vertex-side caps have fraction $27/64$ and their effective vectors are a common positive multiple of $\nabla\xi_i$, which sum to zero, proving sharpness.
