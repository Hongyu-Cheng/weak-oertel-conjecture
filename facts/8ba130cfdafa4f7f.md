---
fact_id: 8ba130cfdafa4f7f
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: oct21-high-activity-rank-pinning
depends_on: ["e22a3fb7e52192e9"]
verifier_run: 4983befa6c2d4bd9
target_match: null
---

## Statement

Let \(k\ge1\) and \(0\le r_{\max}\le\lfloor k/2\rfloor\) be integers. For \(\mathbf x\in\mathbb R^k\), write \(T_{\mathrm{sum}}(\mathbf x):=\sum_{i=1}^k x_i\). Let \(t_1,\ldots,t_k\) be finite real numbers satisfying \(t_i\ge2k/(r_{\max}+1)\) for every \(i\). Set \(N:=k+1\), \(\beta_i:=-\log t_i\), and

$$
\begin{aligned}
D&:=\left\lbrace\mathbf x\in\lbrace0,1,2\rbrace^k:
 T_{\mathrm{sum}}(\mathbf x)\le k,\quad
 \#\lbrace i:x_i=2\rbrace\le r_{\max}\right\rbrace,\\
A&:=D\times\lbrace0\rbrace\subseteq\mathbb R^N,\qquad
w_{\mathbf x}:=e^{-\beta\cdot\mathbf x}=\prod_{i=1}^k t_i^{x_i},\\
Z&:=\sum_{\mathbf x\in D}w_{\mathbf x},\qquad
p_{(\mathbf x,0)}:=\frac{w_{\mathbf x}}{Z}.
\end{aligned}
$$

For \(\mathbf z\in A\), define the actual original ambient depth and its cubic average by

$$
\begin{aligned}
\tau_p(\mathbf z)&:=
\inf_{\substack{H\ni\mathbf z\\
H=\lbrace\mathbf u\in\mathbb R^N:\mathbf a\cdot\mathbf u\ge b\rbrace,
\ \mathbf a\ne\mathbf0}}
\sum_{\mathbf u\in A\cap H}p_{\mathbf u},\\
M_3(p)&:=\sum_{\mathbf z\in A}p_{\mathbf z}\tau_p(\mathbf z)^3.
\end{aligned}
$$

For each integer \(0\le s\le k\), put \(D_s:=\lbrace\mathbf x\in D:T_{\mathrm{sum}}(\mathbf x)=s\rbrace\) and \(Z_s:=\sum_{\mathbf x\in D_s}w_{\mathbf x}\). Let \(\alpha:=Z_k/Z\) and \(c:=e^{-7/24}/(12\sqrt{6\pi})\), the exact constant from accepted fact \(\texttt{e22a3fb7e52192e9}\). Then

$$
\begin{aligned}
Z_s&\le\tfrac12 Z_{s+1}\qquad(0\le s<k),\\
\alpha&\ge\frac1{2-2^{-k}}>\frac12,\\
M_3(p)&\ge\alpha^4c^3\,8^{-k}
\ge\frac{c^3}{16}\,8^{-k}
=\frac{e^{-7/8}}{3456(6\pi)^{3/2}}\,8^{-N}.
\end{aligned}
$$

The last constant is independent of \(k,r_{\max}\), and all the activities. In particular the conclusion holds whenever \(r_{\max}\ge k/4\) and every \(t_i\ge8\). The present \(k,N\) are the spatial and auxiliary ambient dimensions of this finite affine-law model, and do not replace the locked problem's \(n,d\). Its mixed-integer set \(S\) and reserved constant \(c_0\) are not redefined here.

## Proof

All weights are positive. In particular, \(\mathbf1=(1,\ldots,1)\) lies in \(D_k\), so \(Z_k>0\) and \(Z>0\). Write \(t_{\min}:=\min_{1\le i\le k}t_i\).

Fix an integer \(s\) with \(0\le s<k\). Join \(\mathbf x\in D_s\) to \(\mathbf y\in D_{s+1}\) when \(\mathbf y=\mathbf x+\mathbf e_i\) for some coordinate \(i\), where \(\mathbf e_i\) is the \(i\)-th coordinate unit vector. We first show that every \(\mathbf x\in D_s\) has at least \(r_{\max}+1\) such upper neighbors.

Let \(r:=\#\lbrace i:x_i=2\rbrace\), and let \(z\) be the number of its zero coordinates. The number of ones is \(s-2r\), so \(z=k+r-s\). If \(r=r_{\max}\), increasing any zero coordinate to one preserves the two count and raises the total to \(s+1\le k\). Thus it yields a point of \(D_{s+1}\), and the number of these choices is \(z=k+r_{\max}-s\ge r_{\max}+1\). If \(r<r_{\max}\), every coordinate that is not two can be increased: a zero becomes one without changing the two count, and a one becomes two with new two count at most \(r_{\max}\). Each resulting point is ternary with total \(s+1\le k\). There are \(k-r\ge k-r_{\max}+1\ge r_{\max}+1\) choices, where the last inequality uses \(2r_{\max}\le k\). Distinct coordinates give distinct upper neighbors.

Conversely, an upper point \(\mathbf y\in D_{s+1}\) has at most \(k\) incoming edges, because an edge in coordinate \(i\) determines its lower endpoint uniquely as \(\mathbf y-\mathbf e_i\). Let \(\mathcal E_s\) be the set of these edges, represented by their lower endpoint and coordinate. Across an edge in coordinate \(i\), the original weight ratio is \(w_{\mathbf x+\mathbf e_i}/w_{\mathbf x}=t_i\). Summing upper-endpoint weights over the edges, first by lower and then by upper endpoints, gives

$$
\begin{aligned}
t_{\min}(r_{\max}+1)Z_s
&\le\sum_{(\mathbf x,i)\in\mathcal E_s}w_{\mathbf x+\mathbf e_i}\\
&=\sum_{\mathbf y\in D_{s+1}}w_{\mathbf y}
 \#\lbrace(\mathbf x,i)\in\mathcal E_s:
 \mathbf x+\mathbf e_i=\mathbf y\rbrace
\le kZ_{s+1}.
\end{aligned}
$$

Since \(t_{\min}\ge2k/(r_{\max}+1)\), this proves \(Z_s\le Z_{s+1}/2\). Iterating yields \(Z_{k-j}\le2^{-j}Z_k\) for every integer \(0\le j\le k\). Every point of \(D\) has an integer total between zero and \(k\); hence

$$
Z=\sum_{s=0}^k Z_s
\le Z_k\sum_{j=0}^k2^{-j}
=(2-2^{-k})Z_k,
\qquad
\alpha=\frac{Z_k}{Z}\ge\frac1{2-2^{-k}}>\frac12.
$$

We now apply the accepted fixed-total bound, checking the support and normalization explicitly. Define

$$
P_k:=\left\lbrace\mathbf x\in[0,2]^k:
T_{\mathrm{sum}}(\mathbf x)=k,\quad
\sum_{i=1}^k\max\lbrace x_i-1,0\rbrace\le r_{\max}
\right\rbrace.
$$

The function \(\sum_i\max\lbrace x_i-1,0\rbrace\) is convex, so \(P_k\) is convex. Its defining constraints are invariant under every coordinate permutation. At a ternary integer point the displayed sum counts exactly the coordinates equal to two. Therefore \(P_k\cap\mathbb Z^k=D_k\), and this set is nonempty by the point \(\mathbf1\).

Set \(A_k:=D_k\times\lbrace0\rbrace\) and let \(q\) be the conditional law of \(p\) on \(A_k\), namely \(q_{(\mathbf x,0)}:=w_{\mathbf x}/Z_k\) for \(\mathbf x\in D_k\). Define \(\tau_q\) and \(M_3(q)\) by the same ambient-halfspace and cubic-average formulas as above, with support \(A_k\) and probabilities \(q\).

Apply accepted fact \(\texttt{e22a3fb7e52192e9}\) with one block: its \(G=1\), \(I_1=\lbrace1,\ldots,k\rbrace\), \(k_1=k\), \(s_1=k\), and \(P=P_k\). Its \(k,\beta,w_{\mathbf x}\), and auxiliary ambient dimension \(N=k+1\) equal the present ones. Its support symbols \(D,A\) map exactly to the present \(D_k,A_k\); its normalizer \(Z\) maps to \(Z_k\); and its law \(p\), depth \(\tau_p\), and moment \(M_3(p)\) map exactly to \(q,\tau_q\), and \(M_3(q)\). The constant \(c\) is unchanged. In particular all containing closed halfspaces in the same \(\mathbb R^N\), including pure height normals, occur in its depth definition. The convexity, permutation invariance, fixed total, nonemptiness, and arbitrary real-field hypotheses have all been verified. The accepted theorem consequently gives \(M_3(q)\ge c^3 8^{-k}\).

For every \(\mathbf z\in A_k\) and every closed ambient halfspace \(H\) containing \(\mathbf z\), the original law satisfies

$$
\sum_{\mathbf u\in A\cap H}p_{\mathbf u}
\ge\sum_{\mathbf u\in A_k\cap H}p_{\mathbf u}
=\alpha\sum_{\mathbf u\in A_k\cap H}q_{\mathbf u}
\ge\alpha\tau_q(\mathbf z).
$$

Taking the infimum over all these original containing halfspaces proves \(\tau_p(\mathbf z)\ge\alpha\tau_q(\mathbf z)\). The original sampling probability at such an atom is also \(p_{\mathbf z}=\alpha q_{\mathbf z}\). All moment terms are nonnegative, so retaining just those atoms gives

$$
\begin{aligned}
M_3(p)
&\ge\sum_{\mathbf z\in A_k}\alpha q_{\mathbf z}
 (\alpha\tau_q(\mathbf z))^3
=\alpha^4M_3(q)\\
&\ge\alpha^4c^3\,8^{-k}
\ge\frac{c^3}{16}\,8^{-k}
=\frac{e^{-7/8}}{3456(6\pi)^{3/2}}\,8^{-(k+1)}.
\end{aligned}
$$

Thus the original normalization \(Z\) is retained in both the sampling probabilities and all original halfspace masses; conditioning incurs precisely the displayed fourth-power mass factor. The adjacent-rank argument includes \(r_{\max}=0\): then its first case always applies and supplies at least one zero coordinate whenever \(s<k\). In particular \(k=1\) has \(r_{\max}=0\), so it is included. The top layer can be a singleton, as it is when \(r_{\max}=0\); the accepted theorem permits that case and lower-dimensional supports. Finally, if \(r_{\max}\ge k/4\), then \(2k/(r_{\max}+1)\le8\), so every activity at least \(8\) satisfies the required threshold.

## External sources

None. The only imported result is the exact fixed-total original ambient \(M_3\) inequality of accepted fact \(\texttt{e22a3fb7e52192e9}\), with its complete parameter and normalization map stated above. The adjacent-rank estimate, top-layer mass, convex-support realization, and transfer to the original law are proved here.
