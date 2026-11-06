---
fact_id: ee640ebdfbcb632d
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: oct22-abstract-midpoint-matching-product
depends_on: ["4d36c889dd0a9ba2","a24d667ced0d7e0c"]
verifier_run: 8719fa1e3a604694
target_match: null
---

## Statement

Let \(L\ge1\). For each \(1\le\ell\le L\), let \(n_\ell\ge1\) and let \(A_\ell\subset\mathbb Z^{n_\ell}\) be finite and nonempty. Assume the following three properties separately in every factor:

1. Every coordinatewise parity class contains at most two points of \(A_\ell\).
2. If distinct \(u,v\in A_\ell\) have the same coordinatewise parity, then their midpoint \((u+v)/2\) belongs to \(A_\ell\).
3. Distinct unordered pairs of distinct same-parity points have distinct midpoints.

Choose arbitrary weights \(w_{\ell,x}>0\) on every point of \(A_\ell\). Define the entire original laws, normalizers, product, and ambient dimension by
$$
\begin{aligned}
Z_\ell&=\sum_{x\in A_\ell}w_{\ell,x},\qquad
p_{\ell,x}=\frac{w_{\ell,x}}{Z_\ell},\qquad
P=\bigotimes_{\ell=1}^L p_\ell,\qquad N=\sum_{\ell=1}^L n_\ell,\\
P_{(x_1,\ldots,x_L)}&=\frac{\prod_{\ell=1}^Lw_{\ell,x_\ell}}{\prod_{\ell=1}^L Z_\ell}
\quad((x_1,\ldots,x_L)\in\prod_{\ell=1}^L A_\ell).
\end{aligned}
\tag{1}
$$
Every law is zero outside its displayed support. Require midpoint log concavity on every distinct same-parity pair:
\(p_{\ell,(u+v)/2}\ge\sqrt{p_{\ell,u}p_{\ell,v}}\).
Equivalently, \(w_{\ell,(u+v)/2}\ge\sqrt{w_{\ell,u}w_{\ell,v}}\).

Retain exactly the actual depth and reflected notation of 4d36c889dd0a9ba2 and a24d667ced0d7e0c. Explicitly, for a finite law \(p\) on \(\mathbb Z^n\),
$$
\begin{aligned}
\tau_p(j)&=\inf\lbrace p(\mathcal H):\mathcal H\subseteq\mathbb R^n
 \text{ is a closed halfspace containing }j\rbrace,\\
H_p(j)&=\sum_{v\in\mathbb Z^n}\sqrt{p_{j+v}p_{j-v}},\qquad
b(p)=\sum_jp_jH_p(j)^2,\qquad
\chi(p)=\sum_jp_jH_p(j),\\
M_2(p)&=\sum_jp_j\tau_p(j)^2,\qquad
M_3(p)=\sum_jp_j\tau_p(j)^3.
\end{aligned}
\tag{2}
$$
Both nonzero orientations occur in \(H_p\), while zero occurs once. All halfspaces in (2) are in the original ambient space, including for lower-dimensional supports.

With natural logarithms, set
$$
\begin{aligned}
C_{\mathrm{ch}}&=2^{20},\qquad
G_*=26C_{\mathrm{ch}},\qquad D_*=384G_*^2,\\
c_*&=\frac14\exp\left[-29952
 -16D_*\left(2+12(\log2)^2\right)\right]>0.
\end{aligned}
\tag{3}
$$
Then every original product (1) satisfies
\(M_2(P)\ge c_*4^{-N}\) and \(M_3(P)\ge c_*^{3/2}8^{-N}\).
The constants are independent of all dimensions, supports, weights, and the number of factors. No endpoint is required to have a singleton reflected row. The set of nontrivial rows may be empty, and singleton factor supports are allowed.

## Proof

We first work in one factor and suppress \(\ell\). Write \(n,A,w,Z,p\) for the objects in (1), put \(K=2^n\), and let \(\mathcal J\) be the set of midpoints of distinct same-parity pairs. Each such pair occupies its entire parity class, so its endpoint set is disjoint from the endpoint set of every other pair. The midpoint assumptions imply that every \(j\in\mathcal J\) belongs to \(A\), and that exactly one unordered pair \(\lbrace u_j,v_j\rbrace\) has midpoint \(j\). Hence
$$
R_j:=\lbrace x\in A:2j-x\in A\rbrace
=\begin{cases}
\lbrace u_j,j,v_j\rbrace,&j\in\mathcal J,\\
\lbrace j\rbrace,&j\notin\mathcal J.
\end{cases}
\tag{4}
$$
Indeed any distinct reflected endpoints have equal parity, and every such pair is among those just listed. Thus centers are distinct and endpoint sets are pairwise disjoint, exactly as in the abstract matching hypotheses of 4d36c889dd0a9ba2. An atom may occur once as a center and once as an endpoint; those occurrences are allowed to overlap throughout this proof. Also \(|A|\le2K\).

Our normalization map to the accepted notation is the identity on \(n,A,w,Z,p,\tau,H,b,\chi,M_2,M_3\). For the auxiliary notation of a24d667ced0d7e0c, its block width is replaced by \(n\), its nontrivial-center set by \(\mathcal J\), and \(K=2^n\); the hatted quantities below have the same meanings, now for (4). The atom sums \(A_0,A_{\mathcal S}\) below are not the canonical ratio \(a(p)=\chi(p)/b(p)\). We prove all transferred estimates explicitly, including the replacement for the singleton-endpoint step.

For each \(j\in\mathcal J\), choose either ordering of the endpoints and define
$$
\begin{aligned}
s_j&=\frac{\sqrt{p_{u_j}p_{v_j}}}{p_j}\in(0,1],\qquad
z_j=\frac12\log\frac{p_{v_j}}{p_{u_j}},\qquad
\rho_j=\log(1/s_j)\ge0,\\
\beta_j&=Ks_jp_j^2.
\end{aligned}
\tag{5}
$$
The bound on \(s_j\) is exactly midpoint log concavity. In particular, \(H_p(j)=(1+2s_j)p_j\) on \(\mathcal J\), and \(H_p(x)=p_x\) otherwise.

Fix any subset \(\mathcal S\subseteq\mathcal J\). Retain the full triple row in (4) at centers of \(\mathcal S\), and only the singleton \(\lbrace x\rbrace\) at every other supported center \(x\). Call these symmetric auxiliary sets \(\widehat R_x\), and define
$$
\begin{aligned}
\widehat H(x)&=\sum_{y\in\widehat R_x}\sqrt{p_yp_{2x-y}},\qquad
\widehat b=\sum_{x\in A}p_x\widehat H(x)^2,\qquad
\widehat\chi=\sum_{x\in A}p_x\widehat H(x),\\
\widehat\kappa_x(y)&=\frac{\sqrt{p_yp_{2x-y}}}{\widehat H(x)}
 \quad(y\in\widehat R_x),\qquad
\widehat Y_x(y)=\frac12\log\frac{p_y}{p_{2x-y}},\\
\widehat V_x&=\mathbb E_{\widehat\kappa_x}\widehat Y_x^2,\qquad
\widehat q_x=\frac{p_x\widehat H(x)^2}{\widehat b},\qquad
\widehat\nu=\sum_{x\in A}\widehat q_x\widehat V_x.
\end{aligned}
\tag{6}
$$
Hats always designate auxiliary restricted rows, leaving the full canonical quantities in (2) unchanged. All probabilities in (6) remain \(p_x=w_x/Z\), including when an auxiliary row is reduced to its singleton. Since every row contains its center, \(\widehat b>0\) and all these probability laws are well-defined. Reflection preserves \(\widehat\kappa_x\) and reverses \(\widehat Y_x\), so its score mean is zero.

Put \(A_0=K^2\sum_{x\in A}p_x^3\) and \(A_{\mathcal S}=K^2\widehat b\). The support cardinality bound and the inequalities \(p_x\le\widehat H(x)\le H_p(x)\le3p_x\) give
\(1/4\le A_0\le A_{\mathcal S}\le K^2b(p)\le9A_0\).
The first inequality follows from \(\sum_xp_x^3\ge |A|^{-2}\), by Jensen under the uniform law on \(A\).

For each of the \(K\) parity classes \(\eta\in\lbrace0,1\rbrace^n\), let \(r_\eta=p(\eta+2\mathbb Z^n)\), including zero masses. Define
$$
\begin{aligned}
\mathcal D&=K\sum_\eta r_\eta^2-1
 =\frac1K\sum_\eta(Kr_\eta-1)^2\ge0,\\
\mathcal V_{\mathcal S}&=\sum_{x\in A}p_x(K\widehat H(x)-1)^2,\qquad
\mathcal T_{\mathcal S}=4K\sum_{j\in\mathcal S}s_j(1-s_j)p_j^2,\\
\mathcal E_{\mathcal S}&=\mathcal V_{\mathcal S}+2\mathcal D+\mathcal T_{\mathcal S},\qquad
\beta_{\mathcal S}=\sum_{j\in\mathcal S}\beta_j,\qquad
\zeta_{\mathcal S^c}=K\sum_{j\in\mathcal J\setminus\mathcal S}s_j^2p_j^2.
\end{aligned}
\tag{7}
$$
Here \(\mathcal V_{\mathcal S}\) is a deviation energy, distinct from the row score variances \(\widehat V_x\). Expanding the at-most-two-point parity classes and the selected reflected rows yields
$$
\sum_\eta r_\eta^2=\sum_xp_x^2+2\sum_{j\in\mathcal J}s_j^2p_j^2,
\qquad
\widehat\chi=\sum_xp_x^2+2\sum_{j\in\mathcal S}s_jp_j^2.
\tag{8}
$$
Also \(\mathcal V_{\mathcal S}=A_{\mathcal S}-2K\widehat\chi+1\). Substitution of (8) into (7) therefore proves the exact identity
\(A_{\mathcal S}=1+\mathcal E_{\mathcal S}-4\zeta_{\mathcal S^c}\).

We next prove the new uniform intensity charge
\(\beta_{\mathcal S}\le C_{\mathrm{ch}}\mathcal E_{\mathcal S}\).
For \(x\in A\), put \(t_x=Kp_x\) and let \(\theta_x=s_x\) if \(x\in\mathcal S\), and \(\theta_x=0\) otherwise. Thus \(\widehat H(x)=(1+2\theta_x)p_x\) even when \(x\) is an endpoint of a different selected row. Define the nonnegative scalar energy
$$
\begin{aligned}
\Psi(t,\theta)&=t((1+2\theta)t-1)^2+4\theta(1-\theta)t^2\\
&=t(t-1)^2+4\theta t^3+4\theta^2t^2(t-1)
\quad(t\ge0,\ 0\le\theta\le1).
\end{aligned}
\tag{9}
$$
For \(0\le t\le1\), this is concave as a polynomial in \(\theta\). Its minimum on \([0,1]\) is consequently at an endpoint, with endpoint values \(t(t-1)^2\) and \(t(3t-1)^2\). For \(t\ge1\), both \(\theta\)-dependent coefficients in the second line of (9) are nonnegative, and \((t-1)^2\le(3t-1)^2\). Thus, in all cases,
\(\Psi(t,\theta)\ge t\min\lbrace(t-1)^2,(3t-1)^2\rbrace\).
The exact atom accounting is
\(\sum_{x\in A}\Psi(t_x,\theta_x)=K(\mathcal V_{\mathcal S}+\mathcal T_{\mathcal S})\).

For selected rows with \(s_j\le7/8\), the inequality \(4s_j(1-s_j)\ge s_j/2\) shows that their total \(\beta_j\) is at most \(2\mathcal T_{\mathcal S}\).

For a selected row with \(s=s_j>7/8\), put \(\xi=Kp_j\), \(\upsilon=Kp_{u_j}\), \(\omega=Kp_{v_j}\), and \(d=(\upsilon+\omega-1)^2\). The endpoint product is exactly \(\upsilon\omega=s^2\xi^2\). We claim
$$
s\xi^2\le2^{18}\left(
\Psi(\xi,\theta_j)+\Psi(\upsilon,\theta_{u_j})
 +\Psi(\omega,\theta_{v_j})+d\right).
\tag{10}
$$
At this center, \(\theta_j=s\), so its deviation contribution is \(\xi((1+2s)\xi-1)^2\le\Psi(\xi,\theta_j)\).
If \(\xi\le1/4\), then \((1+2s)\xi\le3/4\), so that deviation is at least \(\xi/16\). Hence \(s\xi^2\le4\Psi(\xi,\theta_j)\).
If \(\xi\ge4/9\), then \((1+2s)\xi-1\ge\xi/2\), using \(1+2s>11/4\). The deviation is at least \(\xi^3/4\ge\xi^2/9\), proving (10) again.

It remains that \(1/4<\xi<4/9\). Then \(\upsilon\omega>49/1024\) and \(s\xi^2<16/81<1/4\). If \(d\ge2^{-12}\), (10) holds directly. Otherwise \(63/64<\upsilon+\omega<65/64\). Both endpoints then lie strictly between \(1/32\) and \(65/64\): each is below the sum, and each exceeds
\((49/1024)/(65/64)=49/1040>1/32\).
Suppose both endpoint energies in (10) were less than \(2^{-20}\). The scalar lower bound after (9), divided by \(\upsilon>1/32\) or \(\omega>1/32\), implies for each endpoint value \(t\) that
\(\min\lbrace(t-1)^2,(3t-1)^2\rbrace<2^{-15}<2^{-14}\).
Therefore each endpoint lies in one of the two intervals
\((127/384,129/384)\) and \((127/128,129/128)\).
If both lie in the first interval, their sum is less than \(43/64<63/64\). Otherwise their sum is greater than \(127/128+127/384=127/96>65/64\). Both conclusions contradict the sum constraint. At least one endpoint energy is therefore at least \(2^{-20}\), and \(s\xi^2<1/4\le2^{18}\max\lbrace\Psi(\upsilon,\theta_{u_j}),\Psi(\omega,\theta_{v_j})\rbrace\). This completes (10), without any information about the endpoints' own rows.

Sum (10) over the selected high-ratio rows and divide by \(K\). Every atom is a center at most once and an endpoint at most once. Thus its \(\Psi\)-energy is charged at most twice, including all overlaps between those two roles. Each source parity belongs to at most one endpoint pair, so the \(d\)-terms are charged at most once and have sum at most \(K\mathcal D\). Together with the low-ratio rows, this gives
$$
\begin{aligned}
\beta_{\mathcal S}
&\le2^{18}\bigl(2(\mathcal V_{\mathcal S}+\mathcal T_{\mathcal S})+\mathcal D\bigr)
 +2\mathcal T_{\mathcal S}\\
&\le2^{20}(\mathcal V_{\mathcal S}+2\mathcal D+\mathcal T_{\mathcal S})
 =C_{\mathrm{ch}}\mathcal E_{\mathcal S}.
\end{aligned}
\tag{11}
$$
The last coefficient comparison uses \(2^{19}+2\le2^{20}\). This proves the required replacement charge.

We also prove the score-price estimate, with the constants of a24d667ced0d7e0c:
$$
\widehat\nu\le96\sum_{j\in\mathcal S}(1+\rho_j^2)\beta_j
 +1152\mathcal V_{\mathcal S}.
\tag{12}
$$
At a selected center, the endpoint formulas \(p_{u_j}=s_jp_je^{-z_j}\), \(p_{v_j}=s_jp_je^{z_j}\) give
\(\widehat V_j=2s_jz_j^2/(1+2s_j)\) and
\(p_j\widehat H(j)^2\widehat V_j=2s_j(1+2s_j)p_j^3z_j^2\).
All other score variances vanish. For one selected row write \(s,z,\rho,\xi,\upsilon,\omega\) as above and put \(G_j=2s(1+2s)\xi^3z^2\).

If \(\max(\xi,\upsilon,\omega)\le2\), then the larger endpoint equals \(s\xi e^{|z|}\le2\), whence \(|z|\le\rho+\log(2/\xi)\). The elementary maximum \(\sup_{t\ge0}t^2e^{-t}=4/e^2\) implies \(\xi\log^2(2/\xi)\le8/e^2<2\). Together with \(\xi\le2\) this yields
$$
G_j\le12s\xi^3\bigl(\rho^2+\log^2(2/\xi)\bigr)
 \le24s\xi^2(1+\rho^2).
\tag{13}
$$
For any \(z\in\mathbb R\), the inequality \(z^2\le2\rho^2+4s^3\cosh(3z)\) also holds. It is immediate if \(|z|\le\rho\). Otherwise write \(|z|=\rho+t\), \(t>0\), and use \((\rho+t)^2\le2\rho^2+2t^2\), \(e^{3t}\ge t^2\), and \(s^3\cosh(3z)\ge e^{3t}/2\). The exponential bound follows, for example, from its nonnegative quadratic Taylor term. Since \(s\rho^2\le4/e^2<1\) and \(\upsilon^3+\omega^3=2s^3\xi^3\cosh(3z)\), a row with \(M=\max(\xi,\upsilon,\omega)>2\) therefore satisfies
$$
G_j\le12s\rho^2\xi^3+12s(\upsilon^3+\omega^3)
 \le12(\xi^3+\upsilon^3+\omega^3)\le36M^3.
\tag{14}
$$
Choose one atom of that row having \(Kp_x=M\). As \(K\widehat H(x)\ge M>2\), its contribution to \(K\mathcal V_{\mathcal S}\) is at least \(M(M-1)^2\ge M^3/4\). Thus (14) is paid by 144 times this atom's deviation contribution. The chosen atom can be charged by at most two rows, once through its center role and once through its endpoint role. Hence summing (14) and dividing by \(K\) costs at most \(288\mathcal V_{\mathcal S}\). Summing (13) and dividing by \(K\) costs at most \(24\sum_{j\in\mathcal S}(1+\rho_j^2)\beta_j\). Finally
\(\widehat\nu=(K^{-1}\sum_{j\in\mathcal S}G_j)/A_{\mathcal S}\), and \(A_{\mathcal S}\ge1/4\). Multiplying the two preceding bounds by four proves (12). Its proof required exactly the two incidence bounds already established for (4).

Suppose now \(A_0<1\). Cauchy--Schwarz under \(p\) gives \(K\sum_xp_x^2\le\sqrt{A_0}<1\), so \(\zeta_{\mathcal S^c}<1\). Since \(A_{\mathcal S}\le9A_0<9\), the exact identity after (8) implies \(0\le\mathcal E_{\mathcal S}<12\). Using also \(A_{\mathcal S}\ge1/4\), we obtain
$$
\begin{aligned}
\log A_{\mathcal S}
&=\log(1+\mathcal E_{\mathcal S})
 -\log\left(1+\frac{4\zeta_{\mathcal S^c}}{A_{\mathcal S}}\right)\\
&\ge\frac{\mathcal E_{\mathcal S}}{1+\mathcal E_{\mathcal S}}
 -16\zeta_{\mathcal S^c}
\ge\frac{\mathcal E_{\mathcal S}}{13}-16\zeta_{\mathcal S^c}\\
&\ge\frac{\mathcal V_{\mathcal S}}{26}
 +\frac{\beta_{\mathcal S}}{G_*}-16\zeta_{\mathcal S^c}.
\end{aligned}
\tag{15}
$$
For the final line, (11) and nonnegativity give
\(\mathcal E_{\mathcal S}\ge(\mathcal V_{\mathcal S}+\beta_{\mathcal S}/C_{\mathrm{ch}})/2\).

We now select the auxiliary rows across all factors. Define \(K_\ell=2^{n_\ell}\) and \(A_{0,\ell}=K_\ell^2\sum_{x\in A_\ell}p_{\ell,x}^3\) from every original factor law. If \(A_{0,\ell}\ge1\), retain only singleton rows in that factor. Then \(K_\ell^2\widehat b_\ell=A_{0,\ell}\ge1\) and \(\widehat\nu_\ell=0\).

For all remaining factors, group their nontrivial rows into global ratio bands
$$
\begin{aligned}
\mathcal B_k&=\lbrace(\ell,j):A_{0,\ell}<1,\ j\in\mathcal J_\ell,
 \ 2^{-k-1}<s_{\ell,j}\le2^{-k}\rbrace,\\
\beta_k&=\sum_{(\ell,j)\in\mathcal B_k}K_\ell s_{\ell,j}p_{\ell,j}^2,
\qquad h_k=1+(k+1)^2(\log2)^2\qquad(k\ge0).
\end{aligned}
\tag{16}
$$
Only finitely many bands contain rows. Select band \(k\) exactly when \(\beta_k\ge D_*h_k\), and retain a full row exactly when its band is selected. This determines a subset \(\mathcal S_\ell\) of each factor's nontrivial centers. Set \(U=\sum_{\ell:A_{0,\ell}<1}\mathcal V_{\mathcal S_\ell}\). Because \(\rho_{\ell,j}<(k+1)\log2\) and \(s_{\ell,j}\le2^{-k}\) in band \(k\), (12) and (15) give
$$
\begin{aligned}
\sum_{\ell=1}^L\log(K_\ell^2\widehat b_\ell)
&\ge\frac U{26}+\frac1{G_*}\sum_{k\text{ selected}}\beta_k
 -16\sum_{k\text{ unselected}}2^{-k}\beta_k,\\
\sum_{\ell=1}^L\widehat\nu_\ell
&\le1152U+96\sum_{k\text{ selected}}h_k\beta_k.
\end{aligned}
\tag{17}
$$
All original atoms and all \(Z_\ell\) remain in these formulas; selection changes only the auxiliary rows.

For completeness, we verify directly the actual product conversion for these selected rows. Fix a supported target \(J=(j_1,\ldots,j_L)\). Set
\(\widehat R_J=\prod_\ell\widehat R_{\ell,j_\ell}\),
\(\widehat\kappa_J=\bigotimes_\ell\widehat\kappa_{\ell,j_\ell}\), and
\(\widehat Y_J(X)=\sum_\ell\widehat Y_{\ell,j_\ell}(x_\ell)\).
Factorization and reflection symmetry give
$$
\begin{aligned}
\widehat H_P(J)&:=\sum_{X\in\widehat R_J}\sqrt{P_XP_{2J-X}}
 =\prod_\ell\widehat H_\ell(j_\ell),\\
P_X&=\widehat H_P(J)\widehat\kappa_J(X)e^{\widehat Y_J(X)}
 \quad(X\in\widehat R_J),\\
\mathbb E_{\widehat\kappa_J}\widehat Y_J&=0,\qquad
\mathbb E_{\widehat\kappa_J}\widehat Y_J^2
 =\sigma_J^2:=\sum_\ell\widehat V_{\ell,j_\ell}.
\end{aligned}
\tag{18}
$$
The first quantity is restricted and need not equal the full \(H_P(J)\). The likelihood identity in the second line uses exactly \(P_X\) and \(\prod_\ell Z_\ell\) from (1).

Every closed halfspace \(\mathcal H\subseteq\mathbb R^N\) containing \(J\) contains at least one endpoint of each distinct pair \(X,2J-X\) in \(\widehat R_J\), as well as the central atom. Summing their original masses over the distinct reflection orbits gives
$$
\begin{aligned}
P(\mathcal H)
&\ge\frac12\sum_{X\in\widehat R_J}\min\lbrace P_X,P_{2J-X}\rbrace\\
&=\frac{\widehat H_P(J)}2\,
 \mathbb E_{\widehat\kappa_J}e^{-|\widehat Y_J|}
\ge\frac{\widehat H_P(J)}2e^{-\sigma_J}.
\end{aligned}
\tag{19}
$$
The factor one half counts each noncentral orbit once and uses only half the available central mass. The last step is Jensen followed by Cauchy--Schwarz, using (18). This is a bound for every original ambient containing closed halfspace, so it remains true after taking the infimum defining \(\tau_P(J)\).

Let \(\widehat q=\bigotimes_\ell\widehat q_\ell\), only as an auxiliary center law. Squaring (19) and averaging with respect to the entire original law \(P\), then applying Jensen and Cauchy--Schwarz, gives
$$
\begin{aligned}
M_2(P)
&\ge\frac14\left(\prod_\ell\widehat b_\ell\right)
 \mathbb E_{\widehat q}e^{-2\sigma_J}\\
&\ge\frac14\left(\prod_\ell\widehat b_\ell\right)
 \exp\left(-2\sqrt{\sum_\ell\widehat\nu_\ell}\right).
\end{aligned}
\tag{20}
$$
Here the exact change of weights is
\(P_J\widehat H_P(J)^2=(\prod_\ell\widehat b_\ell)\prod_\ell\widehat q_{\ell,j_\ell}\), and
\(\mathbb E_{\widehat q}\sigma_J^2=\sum_\ell\widehat\nu_\ell\).
This proves the required restricted conversion with the same meanings as 4d36c889dd0a9ba2, without invoking a new law in place of \(P\).

Since \(\prod_\ell K_\ell^2=4^N\), combining (17) and (20), and using subadditivity of the square root on nonnegative sums, yields
$$
\begin{aligned}
\log(4^NM_2(P))\ge{}&-\log4+\frac U{26}-2\sqrt{1152U}\\
&+\sum_{k\text{ selected}}
 \left(\frac{\beta_k}{G_*}-2\sqrt{96h_k\beta_k}\right)
 -16\sum_{k\text{ unselected}}2^{-k}\beta_k.
\end{aligned}
\tag{21}
$$
Completing the square gives \(U/26-2\sqrt{1152U}\ge-26\cdot1152=-29952\).
If band \(k\) is selected, \(\beta_k\ge384G_*^2h_k\), so squaring two nonnegative sides verifies \(\beta_k/G_*\ge2\sqrt{96h_k\beta_k}\). Each selected summand in (21) is thus nonnegative. For every unselected band, \(\beta_k<D_*h_k\). Finally,
$$
\sum_{k=0}^{\infty}2^{-k}h_k
=2+12(\log2)^2,
\tag{22}
$$
using \(\sum_{k\ge0}2^{-k}=2\) and \(\sum_{k\ge0}(k+1)^22^{-k}=12\). The latter follows by applying \(t\,d/dt+1\) twice to \((1-t)^{-1}\) and setting \(t=1/2\). Consequently (21) is at least
\(-\log4-29952-16D_*(2+12(\log2)^2)=\log c_*\).
This proves \(M_2(P)\ge c_*4^{-N}\).

Jensen under the original product law gives
\(M_3(P)=\mathbb E_P(\tau_P(J)^2)^{3/2}\ge M_2(P)^{3/2}\), proving the stated third-moment bound. Empty sets of nontrivial rows, empty selections, zero scores, and singleton supports all satisfy the same displayed identities; no division by a score variance occurs. The argument used only the stated parity matching and midpoint inequalities, and counted every center/endpoint overlap in (11) and (14). Thus it imposes no singleton-endpoint restriction and proves all assertions.

## External sources

None.
