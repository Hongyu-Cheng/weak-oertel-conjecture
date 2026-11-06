---
fact_id: aeaaacd9fdbc5cc5
kind: counterexample
author: "research-agent"
assurance: LLM-verified
subgoal_id: oct21-affine-power-composition-factorial-moment
depends_on: []
verifier_run: d6d5fa30fd784019
target_match: null
---

## Statement

For integers \(m\ge 2\), \(L\ge 1\), and \(D\ge 0\), and \(a\in\mathbb R_{>0}^{m}\), define

$$
\mathcal K_L=\left\lbrace k\in\mathbb Z_{\ge0}^{m}:\sum_{j=0}^{m-1}k_j=L\right\rbrace,
\qquad
Z=\sum_{k\in\mathcal K_L}(a\cdot k)^D,
\qquad
\nu(k)=\frac{(a\cdot k)^D}{Z}.
$$

Let \(K\) have law \(\nu\). For the legal parameters \(m=731\), \(L=2\), \(D=6\), and

$$
a_0=20,\qquad a_1=\cdots=a_{729}=1,\qquad a_{730}=40,
$$

one has

$$
\frac{\mathbb E_\nu[K_0(K_0-1)]}{(\mathbb E_\nu K_0)^2}
=\frac{31443046591184896000000}{13776069530797291879681}>2.
$$

For the same parameters, write \(h_j=\sum_{k\in\mathcal K_2,\ k_0=j}(a\cdot k)^6\) for \(j=0,1,2\), and \(T_r=\sum_{k\in\mathcal K_2,\ k_0\ge r}(a\cdot k)^6\) for \(r=0,1,2\). Then \(ZT_2>T_1^2\) and \(h_0h_2>h_1^2\). Thus both the survival comparison with \(r=s=1\) and marginal logconcavity fail.

More strongly, for every integer \(D\ge1\), take \(L=2\), \(N=3^D\), \(m=N+2\), and

$$
a_0=1,\qquad a_1=\cdots=a_N=\frac1D,\qquad a_{N+1}=2.
$$

The resulting laws satisfy

$$
\frac{\mathbb E_\nu[K_0(K_0-1)]}{(\mathbb E_\nu K_0)^2}
\ge \frac1{18}\left(\frac43\right)^D.
$$

Consequently, for every real \(\mathsf C_{\mathrm{fac}}>0\), some legal law satisfies \(\mathbb E_\nu[K_0(K_0-1)]>\mathsf C_{\mathrm{fac}}(\mathbb E_\nu K_0)^2\).

The aggregate majorant conclusion has the following precise form. Let \(m\ge2\), let

$$
\Delta=\left\lbrace p\in\mathbb R_{\ge0}^{m}:\sum_{i=0}^{m-1}p_i=1\right\rbrace,
\qquad
\mathcal P_2=\left\lbrace\frac{k}{2}:k\in\mathcal K_2\right\rbrace,
$$

and let \(A:\Delta\to\mathbb R_{>0}\) be affine. Let \(d\in\mathbb Z_{>0}\) and \(\delta\ge0\). With natural logarithms and \(0\log0=0\), define

$$
\begin{aligned}
H(p)&=-\sum_{i=0}^{m-1}p_i\log p_i,&
r(p)&=A(p)+\delta H(p),\\
A_{\min}&=\min_{p\in\Delta}A(p)>0,&
\varepsilon&=\left(1+\frac{\delta\log2}{A_{\min}}\right)^d-1,\\
W_{\mathrm{ent}}&=\sum_{p\in\mathcal P_2}r(p)^d,&
J(\psi)&=\sum_{p\in\mathcal P_2}\psi(p)^d.
\end{aligned}
$$

Here \(W_{\mathrm{ent}}\) is the profile's full original power-weight mass, the quantity denoted \(W\) in the entropy-majorant subgoal; every weak composition of \(2\) is counted once. Assume \(\varepsilon\le1/10\). The minimum of \(J(\psi)\) over all affine \(\psi\) satisfying \(\psi(p)\ge r(p)\) at every \(p\in\mathcal P_2\) is attained. Every such minimizer is positive on \(\Delta\) and satisfies

$$
0\le J(\psi)-W_{\mathrm{ent}}\le\varepsilon W_{\mathrm{ent}}.
$$

No coordinate moment hypothesis is imposed.

For the finite \(731\)-coordinate coefficient vector above, set \(d=7\) and \(A(p)=\sum_{i=0}^{730}a_i p_i\). There exists \(\delta_*>0\), with \((1+\delta_*\log2)^7-1\le1/10\), such that for every \(0<\delta<\delta_*\), every optimal affine majorant \(\psi\) induces a law on the full composition support,

$$
\nu_\psi(k)=\frac{\psi(k/2)^6}{\sum_{u\in\mathcal K_2}\psi(u/2)^6},
$$

for which \(\mathbb E_{\nu_\psi}[K_0(K_0-1)]>2(\mathbb E_{\nu_\psi}K_0)^2\). The aggregate conclusion above applies simultaneously with \(\varepsilon=(1+\delta\log2)^7-1\).

More generally, for every \(\mathsf C_{\mathrm{fac}}>0\), some full \(L=2\) profile and positive integer \(d\) have the following property: for all sufficiently small positive \(\delta\), every optimal affine majorant has a derivative-weight law proportional to \(\psi(k/2)^{d-1}\) whose coordinate factorial ratio is greater than \(\mathsf C_{\mathrm{fac}}\). The corresponding \(\varepsilon\) can be made arbitrarily small.

## Proof

First enumerate the entire support for \(L=2\) and a coefficient vector with one distinguished coefficient \(\alpha>0\), \(N\ge1\) coefficients equal to \(\beta>0\), and one coefficient \(\gamma>0\). In other words, \(m=N+2\), \(a_0=\alpha\), \(a_1=\cdots=a_N=\beta\), and \(a_{N+1}=\gamma\). For every integer \(D\ge0\), let \(h_j=\sum_{k\in\mathcal K_2,\ k_0=j}(a\cdot k)^D\).

If \(k_0=0\), both units either lie in the \(N\) coordinates of coefficient \(\beta\), one lies there and the other in the coordinate of coefficient \(\gamma\), or both lie in the latter coordinate. The three numbers of weak compositions are \(\binom{N+1}{2}\), \(N\), and \(1\), respectively. Their scores are \(2\beta\), \(\beta+\gamma\), and \(2\gamma\). If \(k_0=1\), the other unit has \(N\) choices with score \(\alpha+\beta\) and one choice with score \(\alpha+\gamma\). If \(k_0=2\), there is one composition, with score \(2\alpha\). Thus

$$
\begin{aligned}
h_0&=\binom{N+1}{2}(2\beta)^D+N(\beta+\gamma)^D+(2\gamma)^D,\\
h_1&=N(\alpha+\beta)^D+(\alpha+\gamma)^D,\\
h_2&=(2\alpha)^D,\qquad Z=h_0+h_1+h_2.
\end{aligned}
$$

These classes are disjoint and exhaustive. Their total number is \(\binom{N+1}{2}+2N+3=\binom{N+3}{2}=|\mathcal K_2|\). In particular, this calculation uses the full weak-composition support, including repeated units and boundary compositions.

Because \(K_0\in\lbrace0,1,2\rbrace\), the exact moments and survival sums are

$$
\begin{aligned}
\mathbb E_\nu K_0&=\frac{h_1+2h_2}{Z},&
\mathbb E_\nu[K_0(K_0-1)]&=\frac{2h_2}{Z},\\
\frac{\mathbb E_\nu[K_0(K_0-1)]}{(\mathbb E_\nu K_0)^2}
&=\frac{2h_2Z}{(h_1+2h_2)^2},&
(T_0,T_1,T_2)&=(Z,h_1+h_2,h_2).
\end{aligned}
$$

For the first example, substitute \(N=729\), \(\alpha=20\), \(\beta=1\), \(\gamma=40\), and \(D=6\). All coefficients are strictly positive, \(m=N+2=731\ge2\), and the support contains exactly \(\binom{732}{2}=267546\) compositions. The exact section sums and normalizer are

$$
\begin{aligned}
h_0&=\binom{730}{2}\,2^6+729\cdot41^6+80^6
     =3724987021129,\\
h_1&=729\cdot21^6+60^6=109179502209,\\
h_2&=40^6=4096000000,\\
Z&=3838262523338.
\end{aligned}
$$

In particular, \(h_1+2h_2=117371502209\), and exact integer arithmetic gives

$$
\begin{aligned}
h_2Z&=15721523295592448000000,\\
(h_1+2h_2)^2&=13776069530797291879681,\\
h_2Z-(h_1+2h_2)^2&=1945453764795156120319>0.
\end{aligned}
$$

The displayed factorial ratio follows from these exact integers and is strictly greater than \(2\). No floating-point comparison or numerical infeasibility assertion is used.

For survival, \(T_1=h_1+h_2=113275502209\) and \(T_2=h_2\), so

$$
ZT_2-T_1^2=2890183894891284120319>0.
$$

The positive moment gap also directly implies the failure of marginal logconcavity, since

$$
h_2Z-(h_1+2h_2)^2
=h_0h_2-h_1^2-3h_1h_2-3h_2^2>0.
$$

It remains to prove the absence of any finite absolute replacement constant. For each integer \(D\ge1\), substitute \(N=3^D\), \(\alpha=1\), \(\beta=1/D\), and \(\gamma=2\) in the full-support formulas. Every coefficient is strictly positive, and

$$
\begin{aligned}
h_0&=\binom{N+1}{2}\left(\frac2D\right)^D
       +N\left(2+\frac1D\right)^D+4^D\ge N2^D,\\
h_1&=N\left(1+\frac1D\right)^D+3^D
     =N\left(\left(1+\frac1D\right)^D+1\right),\\
h_2&=2^D\le N.
\end{aligned}
$$

The binomial theorem gives the elementary uniform bound

$$
\left(1+\frac1D\right)^D
=\sum_{j=0}^{D}\binom{D}{j}D^{-j}
\le\sum_{j=0}^{D}\frac1{j!}
\le2+\sum_{j=2}^{\infty}\frac1{2^{j-1}}=3.
$$

Here \(\binom{D}{j}D^{-j}\le1/j!\) follows by bounding each factor in the falling product by \(D\), and \(j!\ge2^{j-1}\) for \(j\ge2\). Thus \(h_1\le4N\), \(h_1+2h_2\le6N\), and \(Z\ge h_0\ge N2^D\). Substituting bounds in the correct directions in the exact ratio yields

$$
\begin{aligned}
\frac{\mathbb E_\nu[K_0(K_0-1)]}{(\mathbb E_\nu K_0)^2}
&=\frac{2h_2Z}{(h_1+2h_2)^2}\\
&\ge\frac{2\cdot2^D\cdot N2^D}{(6N)^2}
=\frac{4^D}{18N}
=\frac1{18}\left(\frac43\right)^D.
\end{aligned}
$$

This lower bound diverges. Explicitly, Bernoulli's inequality gives \((4/3)^D\ge1+D/3\), so any integer \(D>54\mathsf C_{\mathrm{fac}}\) makes the ratio greater than \(\mathsf C_{\mathrm{fac}}\). This proves the asserted unboundedness of the coordinate factorial ratio.

We prove the aggregate conclusion directly. The full set \(\mathcal P_2\) consists of the vertices \(e_i\) and the midpoints \((e_i+e_j)/2\) for unordered pairs \(i<j\). Thus \(0\le H(p)\le\log2\) on this set. The affine function \(A+\delta\log2\) is feasible. Every feasible affine \(\psi\) is at least \(A\) at all vertices, hence throughout \(\Delta\). In particular, it is positive. A nonempty objective sublevel is compact in the vertex values of \(\psi\): each vertex contribution \(\psi(e_i)^d\) bounds that value from above, and \(\psi(e_i)\ge A(e_i)>0\) bounds it from below. The finite grid constraints are closed. Therefore a minimum is attained.

Put \(\psi_0=A+\delta\log2\). On the full grid, the entropy bounds imply

$$
\psi_0(p)=r(p)+\delta\bigl(\log2-H(p)\bigr)
\le r(p)+\delta\log2
\le\left(1+\frac{\delta\log2}{A_{\min}}\right)r(p).
$$

Every minimizing majorant \(\psi\) therefore satisfies

$$
W_{\mathrm{ent}}\le J(\psi)
\le J(\psi_0)
\le\left(1+\frac{\delta\log2}{A_{\min}}\right)^d W_{\mathrm{ent}}
=(1+\varepsilon)W_{\mathrm{ent}}.
$$

This proves the stated aggregate bound, including \(\delta=0\), without a coordinate factorial moment or contact condition.

We next show that optimality does not repair the coordinate obstruction. For any fixed \(m,d,A\), let \(\psi\) be any minimizing majorant for entropy coefficient \(\delta>0\). Feasibility gives \(\psi(p)\ge A(p)\), while the feasible comparison \(A+\delta\log2\) gives

$$
\begin{aligned}
0\le\psi(p)^d-A(p)^d
&\le\sum_{u\in\mathcal P_2}\bigl(\psi(u)^d-A(u)^d\bigr)\\
&\le\sum_{u\in\mathcal P_2}
\bigl((A(u)+\delta\log2)^d-A(u)^d\bigr)
=:E_\delta
\end{aligned}
$$

for every \(p\in\mathcal P_2\). The finite sum \(E_\delta\) tends to zero as \(\delta\) tends to zero. Since \(u^d-v^d\ge d v^{d-1}(u-v)\) for \(u\ge v>0\), it follows that

$$
\max_{p\in\mathcal P_2}|\psi(p)-A(p)|
\le\frac{E_\delta}{dA_{\min}^{d-1}}\longrightarrow0.
$$

The bound holds for every minimizer, so this convergence is uniform over all minimizers.

Specialize first to \(d=7\) and the displayed finite coefficient vector, with \(A(p)=\sum_i a_i p_i\). Then \(A_{\min}=1\) and \(A(k/2)^6=2^{-6}(a\cdot k)^6\); hence the law with weights \(A(k/2)^6\) is exactly the finite counterexample law already computed. For any affine \(\psi\) positive on the grid, write \(w_\psi(k)=\psi(k/2)^6\) and define the polynomial in its grid values

$$
\begin{aligned}
G(\psi)={}&\left(\sum_{k\in\mathcal K_2}w_\psi(k)\right)
\left(\sum_{k\in\mathcal K_2}k_0(k_0-1)w_\psi(k)\right)\\
&\quad-2\left(\sum_{k\in\mathcal K_2}k_0w_\psi(k)\right)^2.
\end{aligned}
$$

Failure of the coefficient-\(2\) factorial-moment inequality is exactly \(G(\psi)>0\). The exact finite calculation gives

$$
G(A)=2^{-11}\bigl(h_2Z-(h_1+2h_2)^2\bigr)
=\frac{1945453764795156120319}{2^{11}}>0.
$$

Continuity of this finite polynomial gives a neighborhood of the grid values of \(A\) on which \(G>0\). Uniform convergence of all minimizers to \(A\) puts every minimizer in that neighborhood whenever \(0<\delta<\delta_*\), for some \(\delta_*>0\). Decrease \(\delta_*\) if necessary to make \((1+\delta_*\log2)^7-1\le1/10\). This proves the claimed failure at every optimizer while retaining the aggregate estimate.

Finally fix any \(\mathsf C_{\mathrm{fac}}>0\). Choose \(D\) in the unbounded family so that its proved factorial ratio exceeds \(\mathsf C_{\mathrm{fac}}\), put \(d=D+1\), and set \(A(p)=\sum_i a_i p_i\) using that family's strictly positive coefficients. The derivative weights at \(\delta=0\) are \(A(k/2)^{d-1}=2^{-D}(a\cdot k)^D\), so their normalized law is exactly the chosen family member. Its factorial ratio is continuous in the positive grid values of \(A\), since its mean is positive. The same uniform convergence argument therefore preserves the strict inequality for every optimizer at all sufficiently small positive \(\delta\). For this fixed profile the exact parameter \(\varepsilon=(1+\delta\log2/A_{\min})^d-1\) tends to zero with \(\delta\). This proves the final assertion and the separation between the failed coordinate route and the valid aggregate budget on all these \(L=2\) hosts.

## External sources

None. All claims used above are proved in the packet.
