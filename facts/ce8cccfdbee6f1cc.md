---
fact_id: ce8cccfdbee6f1cc
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: intake10-product-depth-capacity-separation
depends_on: []
verifier_run: 87a39711936d4418
target_match: null
---

## Statement

Let \(p\) be a finitely supported probability law on \(\mathbb Z^n\), extended by zero to all of \(\mathbb Z^n\). For \(\mathbf j\) in its support define
\[
\begin{aligned}
\tau_p(\mathbf j)
&:=\inf\{p(H):H\subseteq\mathbb R^n\text{ is a closed halfspace and }\mathbf j\in H\},\\
M_2(p)&:=\sum_{\mathbf j}p_{\mathbf j}\tau_p(\mathbf j)^2,\\
C_p(\mathbf j)
&:=\inf_{\boldsymbol\theta\in\mathbb R^n}
\sum_{\mathbf x}p_{\mathbf x}e^{\boldsymbol\theta\cdot(\mathbf x-\mathbf j)},\\
B_2(p)&:=\sum_{\mathbf j}p_{\mathbf j}C_p(\mathbf j)^2,\\
H_p(\mathbf j)&:=\sum_{\mathbf v\in\mathbb Z^n}
\sqrt{p_{\mathbf j+\mathbf v}p_{\mathbf j-\mathbf v}},\\
b(p)&:=\sum_{\mathbf j}p_{\mathbf j}H_p(\mathbf j)^2,
\qquad
\chi(p):=\sum_{\mathbf j}p_{\mathbf j}H_p(\mathbf j),
\qquad
a(p):=\frac{\chi(p)}{b(p)}.
\end{aligned}
\]
The displacement sum defining \(H_p\) is oriented: \(\mathbf v\) and \(-\mathbf v\) both occur, while \(\mathbf v=\mathbf0\) occurs once.
The notations used below and in the source material are mapped exactly by
\[
\mathcal M_2=M_2,
\qquad
\mathsf E_p=C_p,
\qquad
\mathcal B_2=B_2.
\]
The quantity \(b(p)\) is the reflected Hellinger second moment and is not, in general, the capacity moment \(B_2(p)\).

The following assertions hold.

(A) For arbitrary finite laws \(p_1,\ldots,p_k\), capacities and reflected masses factor exactly:
\[
C_{\bigotimes_i p_i}(\mathbf j_1,\ldots,\mathbf j_k)
=\prod_i C_{p_i}(\mathbf j_i),
\qquad
H_{\bigotimes_i p_i}(\mathbf j_1,\ldots,\mathbf j_k)
=\prod_i H_{p_i}(\mathbf j_i),
\]
and hence
\[
B_2\!\left(\bigotimes_i p_i\right)=\prod_iB_2(p_i),
\qquad
b\!\left(\bigotimes_i p_i\right)=\prod_i b(p_i).
\]
In particular, for every positive integer \(m\),
\[
B_2(p^{\otimes m})=B_2(p)^m,
\qquad
C_{p^{\otimes m}}(\mathbf j,\ldots,\mathbf j)=C_p(\mathbf j)^m,
\]
so the tensor-power entropy-capacity rate is exactly
\[
\frac1m\log B_2(p^{\otimes m})=\log B_2(p).
\]
Moreover,
\[
\tau_{p\otimes q}(\mathbf j,\mathbf k)
\ge \tau_p(\mathbf j)\tau_q(\mathbf k),
\qquad
M_2(p\otimes q)\ge M_2(p)M_2(q),
\qquad
M_2(p)\le B_2(p).
\]

(B) Let \(p_i\) be an arbitrary finite probability law on \(\mathbb Z^{n_i}\), and put \(b_i=b(p_i)\) and \(a_i=a(p_i)\). Then the following are actual depth-moment bounds and require neither convexity nor log-concavity:
\[
M_2\!\left(\bigotimes_{i=1}^k(p_i\otimes p_i)\right)
\ge
\frac{9}{125}\,
\frac{\prod_{i=1}^k b_i^2}
{1+\sum_{i=1}^k\operatorname{arcosh}(a_i)^2},
\tag{1}
\]
and
\[
M_2\!\left(\bigotimes_{i=1}^k p_i\right)
\ge
\frac{\prod_{i=1}^k b_i}
{16(k+1)^2\left(\sum_{i=1}^k a_i\right)^2}.
\tag{2}
\]

If, in addition, \(p_i\) is positive and log-affine on a complete convex lattice support
\(A_i=Q_i\cap\mathbb Z^{n_i}\), meaning
\(p_{i,\mathbf x}=Z_i^{-1}e^{\boldsymbol\ell_i\cdot\mathbf x}\) on \(A_i\), then
\[
\chi(p_i)=
\sum_{\mathbf c\in\{0,1\}^{n_i}}
p_i(\mathbf c+2\mathbb Z^{n_i})^2
\ge2^{-n_i},
\qquad
b_i\ge4^{-n_i},
\qquad
a_i\le2^{n_i}.
\tag{3}
\]
Thus (1) and (2) are uniform over the shapes and cardinalities of the supports. Explicitly, if
\(N=2\sum_i n_i\) and \(g_i=\log(4^{n_i}b_i)\ge0\), then
\[
4^N M_2\!\left(\bigotimes_i(p_i\otimes p_i)\right)
\ge
\frac{9}{125}\,
\frac{e^{2\sum_i g_i}}
{1+\sum_i\operatorname{arcosh}(2^{n_i})^2},
\tag{4}
\]
whose denominator is at most
\(1+(\log2)^2\sum_i(n_i+1)^2\). Also
\[
M_2\!\left(\bigotimes_i p_i\right)
\ge
\frac{4^{-\sum_i n_i}}
{16(k+1)^2(\sum_i2^{n_i})^2}.
\tag{5}
\]

(C) The following common core gives the exact one-copy separation and will also be used once in the stronger construction. For integers \(d\ge1\), put \(K=2^d\) and
\[
P_d:=\left\{(t,\mathbf x)\in\mathbb R^{d+1}:
-1\le t\le1,\quad
\frac{t-1}{2}\le x_i\le\frac{t+1}{2}\ (1\le i\le d)
\right\}.
\]
Then
\[
D_d:=P_d\cap\mathbb Z^{d+1}
=\{(1,\mathbf u):\mathbf u\in\{0,1\}^d\}
\cup\{\mathbf0\}
\cup\{(-1,-\mathbf u):\mathbf u\in\{0,1\}^d\}.
\tag{6}
\]
The polytope \(P_d\) is a centrally symmetric parallelotope, and all \(2K\) nonzero points in (6) are its vertices. For \(B\ge1\), let
\[
Z=1+K(B+B^{-1}),
\qquad
\pi_{d,B}(t,\mathbf x)=\frac{B^t}{Z}
\quad ((t,\mathbf x)\in D_d),
\qquad
V=K(B^3+B^{-3}).
\]
At every nonzero \(\mathbf v\in D_d\),
\[
\tau_\pi(\mathbf v)=C_\pi(\mathbf v)=H_\pi(\mathbf v)=\pi_{\mathbf v},
\]
whereas at the origin
\[
\tau_\pi(\mathbf0)=\frac{1+K/B}{Z},
\qquad
C_\pi(\mathbf0)=H_\pi(\mathbf0)=\frac{2K+1}{Z}.
\tag{7}
\]
Consequently,
\[
M_2(\pi_{d,B})=\frac{V+(1+K/B)^2}{Z^3},
\qquad
B_2(\pi_{d,B})=b(\pi_{d,B})
=\frac{V+(2K+1)^2}{Z^3}.
\tag{8}
\]

In particular, for an integer \(h\ge1\), take
\[
B=\rho=2^h,
\qquad d=5h,
\qquad K=2^d=\rho^5,
\qquad n=d+1.
\]
This is a positive log-affine law on a complete centrally symmetric lattice parallelotope with exactly \(2^n+1\) lattice points, and
\[
\begin{aligned}
M_2(\pi_{d,\rho})
&=\frac{2\rho^8+2\rho^4+\rho^2+1}
{(\rho^6+\rho^4+1)^3},\\
B_2(\pi_{d,\rho})=b(\pi_{d,\rho})
&=\frac{4\rho^{10}+\rho^8+4\rho^5+\rho^2+1}
{(\rho^6+\rho^4+1)^3}.
\end{aligned}
\tag{9}
\]
Therefore
\[
\frac{M_2(\pi_{d,\rho})}{B_2(\pi_{d,\rho})}
=\frac{M_2(\pi_{d,\rho})}{b(\pi_{d,\rho})}
\sim\frac1{2\rho^2}\longrightarrow0,
\tag{10}
\]
so no positive universal constant converts either \(B_2\) or \(b\) into \(M_2\). Nevertheless,
\[
4^nM_2(\pi_{d,\rho})\longrightarrow8,
\qquad
4^nB_2(\pi_{d,\rho})=4^nb(\pi_{d,\rho})
\sim16\rho^2\longrightarrow\infty,
\tag{11}
\]
so this family stays at the H2 scale.

(D) There is a stronger full-dimensional complete convex log-affine family for which every atom is negligible relative to \(2^{-N}\), every proper face has asymptotic mass at most \(1/2\), and both capacity-to-depth and reflected-moment-to-depth ratios grow exponentially.

For every integer \(k\ge3\), set
\[
m=5k,\quad K=2^m,\quad B=k2^k,\quad R=B^2,\quad L=2R+1,
\quad r=\lceil\log_2k\rceil,\quad s=2^r-1,\quad N_k=m+r+2.
\tag{12}
\]
For each nonzero \(\mathbf u\in\{0,1\}^r\), place a copy of \(P_m\) over \(\mathbf u\), place only \((t,\mathbf x)=(2,\mathbf0)\) over \(\mathbf u=\mathbf0\), take the convex hull in the coordinates \((\mathbf u,t,\mathbf x)\), and take its product with \([-R,R]\) in a final coordinate \(y\). Denote the resulting polytope by \(Q_k\). Its complete lattice support is exactly
\[
\begin{aligned}
A_k={}&\{(\mathbf u,t,\mathbf x,y):
\mathbf u\in\{0,1\}^r\setminus\{\mathbf0\},
\ (t,\mathbf x)\in D_m,
\ y\in\{-R,\ldots,R\}\}\\
&\cup\{(\mathbf0,2,\mathbf0,y):y\in\{-R,\ldots,R\}\}.
\end{aligned}
\tag{13}
\]
Give \(A_k\) the globally log-affine probability law
\[
p_k(\mathbf u,t,\mathbf x,y)
=\frac{B^t}{L(sZ+B^2)},
\qquad
Z=1+K(B+B^{-1}).
\tag{14}
\]

For exact formulas, let \(\lambda_R\) be uniform on \(\{-R,\ldots,R\}\), and for \(-R\le h\le R\) put
\[
a_h=R+1-|h|,
\qquad d_h=2a_h-1.
\]
Define
\[
\begin{aligned}
c_R&:=M_2(\lambda_R)
=\frac{(R+1)^2+R(R+1)(2R+1)/3}{(2R+1)^3},\\
\beta_R&:=b(\lambda_R)
=\frac1{L^3}\sum_{h=-R}^R d_h^2
=\frac13+\frac{2}{3L^2},\\
\gamma_R&:=B_2(\lambda_R).
\end{aligned}
\tag{15}
\]
Then \(\beta_R\le\gamma_R\le1\). Let \(\pi=\pi_{m,B}\),
\(q=\pi\otimes\lambda_R\),
\[
\alpha=\frac{Z}{sZ+B^2},
\qquad
\eta=\frac{B^2}{sZ+B^2},
\qquad s\alpha+\eta=1,
\]
and \(V=K(B^3+B^{-3})\). At a nonzero core vertex \(\mathbf v\) and every \(h\), the exact closed-halfspace depth is
\[
\tau_q(\mathbf v,h)=\pi_{\mathbf v}\frac{a_h}{L},
\tag{16}
\]
and at the core origin it is
\[
\tau_q(\mathbf0,h)=\frac{(K/B)d_h+a_h}{ZL}.
\tag{17}
\]
Consequently,
\[
\begin{aligned}
M_2(q)
&=\frac{Vc_R}{Z^3}
+\frac1{Z^3L^3}\sum_{h=-R}^R\left(\frac KBd_h+a_h\right)^2,\\
B_2(q)&=\frac{V+(2K+1)^2}{Z^3}\,\gamma_R,\\
b(q)&=\frac{V+(2K+1)^2}{Z^3}\,\beta_R,
\end{aligned}
\tag{18}
\]
and the exact fiber decomposition gives
\[
\begin{aligned}
M_2(p_k)&=s\alpha^3M_2(q)+\eta^3c_R,\\
B_2(p_k)&=s\alpha^3B_2(q)+\eta^3\gamma_R,\\
b(p_k)&=s\alpha^3b(q)+\eta^3\beta_R.
\end{aligned}
\tag{19}
\]

As \(k\to\infty\),
\[
\begin{aligned}
M_2(p_k)&\sim\frac1{12s^2K^2},\\
B_2(p_k)&\sim\frac{4\gamma_R}{s^2KB^3},\\
b(p_k)&\sim\frac{4\beta_R}{s^2KB^3},
\end{aligned}
\qquad
4^{N_k}M_2(p_k)\longrightarrow\frac43,
\tag{20}
\]
and
\[
\frac{B_2(p_k)}{M_2(p_k)}
=2^{(2/5+o(1))N_k},
\qquad
\frac{b(p_k)}{M_2(p_k)}
=2^{(2/5+o(1))N_k}.
\tag{21}
\]
Furthermore,
\[
2^{N_k}\max_{\mathbf j\in A_k}p_{k,\mathbf j}\longrightarrow0,
\tag{22}
\]
and
\[
\max\{p_k(F):F\text{ is a proper face of }Q_k\}
\le
\max\left\{
\frac{s+1}{2s}+\varepsilon_k,\frac1L
\right\}
=\frac12+o(1),
\qquad
\varepsilon_k:=1-\frac{sKB}{sZ+B^2}.
\tag{23}
\]
It follows from (21) that for every \(F(N)=2^{o(N)}\), neither
\(M_2(p)\ge B_2(p)/F(N)\) nor \(M_2(p)\ge b(p)/F(N)\) can hold universally, even under (22) and (23).

The still-open H2 assertion is the existence of an absolute \(c>0\) such that
\[
M_2(p)\ge c\,4^{-n}
\]
for every positive log-affine law on every complete convex lattice support in \(\mathbb Z^n\). The normalized actual moments in (11) and (20) tend to \(8\) and \(4/3\), respectively. Hence neither construction disproves H2. The product bounds above also do not prove H2, because their conclusions concern products and the supermultiplicativity inequality cannot be reversed to bound an individual factor.

## Proof

We prove all assertions from the definitions.

1. Elementary tensor identities and comparisons.

For a product target \(\mathbf J=(\mathbf j_1,\ldots,\mathbf j_k)\), the exponential sum separates:
\[
\sum_{\mathbf x_1,\ldots,\mathbf x_k}
\prod_i p_{i,\mathbf x_i}
e^{\sum_i\boldsymbol\theta_i\cdot(\mathbf x_i-\mathbf j_i)}
=\prod_i\left(
\sum_{\mathbf x_i}p_{i,\mathbf x_i}
e^{\boldsymbol\theta_i\cdot(\mathbf x_i-\mathbf j_i)}
\right).
\]
Taking the infimum independently in every \(\boldsymbol\theta_i\) gives
\(C_{\otimes_i p_i}(\mathbf J)=\prod_iC_{p_i}(\mathbf j_i)\). Summing the squared identity against the product target law gives exact factorization of \(B_2\), including all tensor-power formulas in (A).

Likewise, direct summation over the product displacement gives
\[
H_{p\otimes q}(\mathbf j,\mathbf k)
=\sum_{\mathbf v,\mathbf w}
\sqrt{p_{\mathbf j+\mathbf v}q_{\mathbf k+\mathbf w}
p_{\mathbf j-\mathbf v}q_{\mathbf k-\mathbf w}}
=H_p(\mathbf j)H_q(\mathbf k),
\]
and therefore \(b(p\otimes q)=b(p)b(q)\).

For every \(\boldsymbol\theta\), the closed halfspace
\[
\{\mathbf x:\boldsymbol\theta\cdot(\mathbf x-\mathbf j)\ge0\}
\]
contains \(\mathbf j\), and its probability is at most
\(\sum_{\mathbf x}p_{\mathbf x}e^{\boldsymbol\theta\cdot(\mathbf x-\mathbf j)}\). Taking both infima proves \(\tau_p(\mathbf j)\le C_p(\mathbf j)\), hence \(M_2(p)\le B_2(p)\).

For completeness, reflected pairing also gives \(H_p(\mathbf j)\le C_p(\mathbf j)\). Indeed, for each unordered nonzero reflected pair, AM-GM gives
\[
p_{\mathbf j+\mathbf v}e^{\boldsymbol\theta\cdot\mathbf v}
+p_{\mathbf j-\mathbf v}e^{-\boldsymbol\theta\cdot\mathbf v}
\ge2\sqrt{p_{\mathbf j+\mathbf v}p_{\mathbf j-\mathbf v}},
\]
and the central term is \(p_{\mathbf j}\). The exponential sum may contain additional unpaired points, so it is at least \(H_p(\mathbf j)\). Thus \(b(p)\le B_2(p)\).

To prove depth supermultiplicativity, write an arbitrary closed halfspace containing \((\mathbf j,\mathbf k)\) as
\[
\{(\mathbf x,\mathbf y):
\mathbf a\cdot(\mathbf x-\mathbf j)
+\mathbf c\cdot(\mathbf y-\mathbf k)\ge-\delta\}
\]
with \(\delta\ge0\). It contains the Cartesian product of the two closed halfspaces on which the two separate scores are nonnegative. That product has probability at least
\(\tau_p(\mathbf j)\tau_q(\mathbf k)\). Taking the infimum over the original halfspace proves the pointwise inequality; averaging its square proves
\(M_2(p\otimes q)\ge M_2(p)M_2(q)\).

2. Reduction of actual product depth to one scalar sum.

First note that \(0<H_p(\mathbf j)\le1\) on the support. Positivity follows from the zero displacement. Cauchy-Schwarz gives
\[
H_p(\mathbf j)
\le
\left(\sum_{\mathbf v}p_{\mathbf j+\mathbf v}\right)^{1/2}
\left(\sum_{\mathbf v}p_{\mathbf j-\mathbf v}\right)^{1/2}
\le1.
\]
Consequently,
\[
b(p)\le\chi(p)\le\sqrt{b(p)},
\qquad
1\le a(p)\le b(p)^{-1/2}.
\tag{24}
\]

For one factor define a joint experiment by
\[
\mathbb P(J=\mathbf j)=\frac{p_{\mathbf j}H_p(\mathbf j)^2}{b(p)},
\qquad
\mathbb P(V=\mathbf v\mid J=\mathbf j)
=\frac{\sqrt{p_{\mathbf j+\mathbf v}p_{\mathbf j-\mathbf v}}}
{H_p(\mathbf j)},
\]
and
\[
T=\frac12\log\frac{p_{J+V}}{p_{J-V}}.
\tag{25}
\]
Only displacements with both endpoint probabilities positive occur. The conditional displacement law is invariant under \(\mathbf v\mapsto-\mathbf v\), while this replacement sends \(T\) to \(-T\). Thus \(T\) is symmetric and has mean zero.

At each fixed center,
\[
\begin{aligned}
H_p(\mathbf j)\,\mathbb E(\cosh T\mid J=\mathbf j)
&=\frac12\sum_{\mathbf v:\,p_{\mathbf j+\mathbf v}p_{\mathbf j-\mathbf v}>0}
\left(p_{\mathbf j+\mathbf v}+p_{\mathbf j-\mathbf v}\right)\\
&\le1.
\end{aligned}
\]
Averaging with the center distribution in (25) yields
\[
\mathbb E\cosh T\le\frac{\chi(p)}{b(p)}=a(p).
\tag{26}
\]
The function \(f(x)=\operatorname{arcosh}(x)^2\) is increasing and concave on \([1,\infty)\). Indeed, with \(x=\cosh u\),
\[
f''(x)=\frac{2(\sinh u-u\cosh u)}{\sinh^3u}\le0,
\]
with the endpoint understood by continuity. Since
\(T^2=f(\cosh T)\), Jensen's inequality and (26) give
\[
\operatorname{Var}T=\mathbb ET^2
\le\operatorname{arcosh}(a(p))^2.
\tag{27}
\]
Also \(e^{|t|}\le2\cosh t\), so
\[
\mathbb Ee^{|T|}\le2a(p).
\tag{28}
\]

Now take independent experiments (25) for \(p_1,\ldots,p_k\), and let
\(P=\bigotimes_i p_i\). At a fixed product target \(\mathbf J\), set
\[
S_P(\mathbf J)=\sum_{\mathbf V}
\min\{P_{\mathbf J+\mathbf V},P_{\mathbf J-\mathbf V}\}.
\]
Every closed halfspace containing \(\mathbf J\) contains the center and at least one endpoint of each antipodal pair. Since the displayed sum counts every nonzero pair twice and the center once,
\[
\tau_P(\mathbf J)
\ge\frac{S_P(\mathbf J)+P_{\mathbf J}}2
\ge\frac12S_P(\mathbf J).
\tag{29}
\]
The identity
\[
\min\{u,v\}=\sqrt{uv}\exp\left(-\frac12|\log(u/v)|\right)
\]
and factorization of the geometric reflected weights give
\[
S_P(\mathbf J)
=\left(\prod_iH_{p_i}(\mathbf j_i)\right)
\mathbb E\left[
e^{-|\sum_iT_i|}\mid\mathbf J
\right].
\tag{30}
\]
Squaring (29), substituting (30), and averaging over the product target law produces the factor \(\prod_i b_i\). Under the resulting normalized target weights, the centers have exactly the independent distributions in (25). Jensen's inequality for the conditional expectation therefore proves
\[
M_2\!\left(\bigotimes_i p_i\right)
\ge\frac14\left(\prod_i b_i\right)
\left(\mathbb E e^{-|\sum_iT_i|}\right)^2.
\tag{31}
\]
This is a lower bound for actual closed-halfspace depth, not for capacity.

3. The paired and unpaired scalar estimates.

Let \(U'\) be an independent copy of a real random variable \(U\) having variance \(\sigma^2\). We claim
\[
\mathbb Ee^{-|U-U'|}
\ge\frac{6}{5\sqrt5\sqrt{1+\sigma^2}}.
\tag{32}
\]
Let \(E\) be an independent rate-one exponential variable and let \(f\) be the density of \(U+E\). Then
\[
f(t)=\mathbb E[e^{-(t-U)}\mathbf1_{\{t\ge U\}}].
\]
Multiplying two independent copies and integrating from \(\max(U,U')\) to infinity gives the exact identity
\[
\int_{\mathbb R}f(t)^2\,dt
=\frac12\mathbb Ee^{-|U-U'|}.
\tag{33}
\]
The density \(f\) has mean, say, \(\mu\), and variance \(v=1+\sigma^2\). Put
\(R_0=\sqrt{5v}\) and
\(\varphi(t)=(1-(t-\mu)^2/R_0^2)_+\). Pointwise,
\(\varphi(t)\ge1-(t-\mu)^2/R_0^2\), and hence
\[
\int f\varphi\ge1-\frac v{R_0^2}=\frac45,
\qquad
\int\varphi^2=\frac{16R_0}{15}.
\]
Cauchy-Schwarz implies
\[
\int f^2\ge
\frac{(4/5)^2}{16R_0/15}
=\frac{3}{5\sqrt5\sqrt v}.
\]
Together with (33), this proves (32).

Apply (31) to the \(2k\) factors in the paired product. For the two copies of factor \(i\), let the scalar variables be \(T_i,T_i'\). All are independent, and symmetry shows that
\(\sum_i(T_i+T_i')\) has the same law as \(U-U'\), where
\(U=\sum_iT_i\) and \(U'\) is an independent copy. By (27),
\[
\operatorname{Var}U
=\sum_i\operatorname{Var}T_i
\le\sum_i\operatorname{arcosh}(a_i)^2.
\]
Substitution of (32) into (31) gives the constant
\(\frac14(6/(5\sqrt5))^2=9/125\) and proves (1).

For the unpaired bound, represent each symmetric \(T_i\) as
\(T_i=\varepsilon_iR_i\), where \(R_i=|T_i|\) and, conditional on the magnitudes, the signs are independent and fair. Put \(L_0=\max_iR_i\). At least a fraction \(1/(k+1)\) of all sign vectors satisfy
\[
\left|\sum_i\varepsilon_iR_i\right|\le L_0.
\tag{34}
\]
To prove this, for any sign vector successively flip its first \(j\) signs for \(j=0,\ldots,k\). The corresponding sums start at some \(S\), end at \(-S\), and every jump has magnitude at most \(2L_0\). One of these \(k+1\) sums lies in \([-L_0,L_0]\). Choose the first such prefix. The original vector is recovered from the resulting central vector and the prefix length, so this maps all \(2^k\) sign vectors injectively into at most \((k+1)\) copies of the set satisfying (34). This proves the claimed fraction.

Conditioning on the magnitudes, using (34), then Cauchy-Schwarz and (28), gives
\[
\begin{aligned}
\mathbb Ee^{-|\sum_iT_i|}
&\ge\frac{\mathbb Ee^{-L_0}}{k+1}
\ge\frac1{(k+1)\mathbb Ee^{L_0}}\\
&\ge\frac1{(k+1)\sum_i\mathbb Ee^{R_i}}
\ge\frac1{2(k+1)\sum_i a_i}.
\end{aligned}
\]
Putting this in (31) proves (2).

4. Parity calibration for complete log-affine supports.

Assume \(A=Q\cap\mathbb Z^n\) and
\(p_{\mathbf x}=Z^{-1}e^{\boldsymbol\ell\cdot\mathbf x}\) on \(A\). The change of variables
\((\mathbf j,\mathbf v)\mapsto(\mathbf x,\mathbf y)=(\mathbf j+\mathbf v,\mathbf j-\mathbf v)\)
is a bijection between supported reflected triples and ordered pairs
\((\mathbf x,\mathbf y)\in A^2\) of the same coordinatewise parity. Indeed, such a pair has the integer midpoint
\(\mathbf j=(\mathbf x+\mathbf y)/2\), which belongs to \(Q\) by convexity and hence belongs to \(A\) by completeness. Log-affinity gives
\[
p_{\mathbf j}=\sqrt{p_{\mathbf x}p_{\mathbf y}}.
\]
Therefore
\[
\begin{aligned}
\chi(p)
&=\sum_{\mathbf j,\mathbf v}
p_{\mathbf j}\sqrt{p_{\mathbf j+\mathbf v}p_{\mathbf j-\mathbf v}}\\
&=\sum_{\mathbf c\in\{0,1\}^n}
\left(\sum_{\mathbf x\in A\cap(\mathbf c+2\mathbb Z^n)}p_{\mathbf x}\right)^2.
\end{aligned}
\]
The at most \(2^n\) parity-class masses sum to one, so Cauchy-Schwarz gives
\(\chi(p)\ge2^{-n}\). Jensen gives
\(b(p)=\mathbb E_pH_p^2\ge(\mathbb E_pH_p)^2=\chi(p)^2\), and hence
\(b(p)\ge4^{-n}\). Finally
\(a(p)=\chi(p)/b(p)\le1/\chi(p)\le2^n\). This proves (3). Substitution into (1) and (2) gives (4) and (5); the denominator estimate in (4) follows from
\[
\operatorname{arcosh}(2^n)
=\log(2^n+\sqrt{4^n-1})
\le(n+1)\log2.
\]

5. The common three-layer core and the exact simple separation.

The invertible linear map
\[
(t,\mathbf x)\longmapsto(t,2\mathbf x-t\mathbf1)
\]
sends \(P_d\) onto \([-1,1]^{d+1}\). Hence \(P_d\) is a centrally symmetric parallelotope. If \((t,\mathbf x)\in P_d\cap\mathbb Z^{d+1}\), then \(t\in\{-1,0,1\}\). At \(t=1\), every \(x_i\in\{0,1\}\); at \(t=-1\), every \(x_i\in\{-1,0\}\), giving \((-1,-\mathbf u)\); and at \(t=0\), the interval \([-1/2,1/2]\) contains only the integer zero in every coordinate. This proves the complete census (6). Under the displayed linear map, all nonzero points map to cube vertices, so all of them are exposed vertices of \(P_d\).

At an exposed nonzero vertex \(\mathbf v\), a closed exposing halfspace isolates \(\mathbf v\), proving
\(\tau_\pi(\mathbf v)=\pi_{\mathbf v}\). An exposing linear functional, multiplied by a parameter tending to infinity with the suppressing sign, shows
\(C_\pi(\mathbf v)\le\pi_{\mathbf v}\), while the central term in the capacity sum gives the reverse inequality. A nontrivial reflected pair centered at a vertex would express that vertex as the midpoint of two different points of \(P_d\), so none exists; hence
\(H_\pi(\mathbf v)=\pi_{\mathbf v}\).

At the origin, each closed halfspace containing zero contains zero and at least one endpoint of each of the \(K\) antipodal nonzero pairs. Each pair has unnormalized weights \(B\) and \(B^{-1}\). Therefore every such halfspace has mass at least
\((1+K/B)/Z\), and the closed halfspace \(t\le0\) attains this bound. This proves the depth formula in (7).

For reflected mass at zero, the zero displacement contributes \(1/Z\), and each of the \(2K\) oriented nonzero displacements contributes
\(\sqrt{B\cdot B^{-1}}/Z=1/Z\). Thus
\(H_\pi(\mathbf0)=(2K+1)/Z\). For capacity, an arbitrary exponential tilt pairs the unnormalized terms at antipodal points as
\[
Be^{\boldsymbol\theta\cdot\mathbf z}
+B^{-1}e^{-\boldsymbol\theta\cdot\mathbf z}\ge2.
\]
Including the origin gives a lower bound \((2K+1)/Z\). The tilt whose \(t\)-coefficient is \(-\log B\) and whose other coefficients vanish cancels the original weights and attains equality. This proves all of (7). Summing the cubic vertex contributions and the origin contribution gives (8).

For the specialization \(d=5h\), \(B=\rho=2^h\), one has
\(K=\rho^5\),
\(Z=\rho^6+\rho^4+1\), and
\(V=\rho^8+\rho^2\). Substitution in (8) gives (9). Its leading terms give (10). Since
\(4^n=4^{5h+1}=4\rho^{10}\), the same exact formulas give (11). This completes the simple one-copy counterexample without invoking any external census or checker.

6. Exact census and formulas for the stronger construction.

Let \(Q_k^0\) denote the convex hull before taking the final interval product. Its projection to the \(\mathbf u\)-coordinates is \([0,1]^r\). Every integer point in that projection is a Boolean vertex. If a convex combination of generating fibers projects to a fixed Boolean vertex \(\mathbf u\), extremality of that cube vertex forces every term in the combination to come from the fiber over the same \(\mathbf u\). Thus the section over nonzero \(\mathbf u\) is exactly \(P_m\), while the section over zero is exactly \(\{(2,\mathbf0)\}\). Applying the already proved census (6) in each ordinary fiber, and then using
\([-R,R]\cap\mathbb Z=\{-R,\ldots,R\}\), proves (13). Conversely, the generating fiber polytopes and interval are convex hulls of these lattice points, so \(Q_k=\operatorname{conv}(A_k)\). One ordinary fiber supplies \(m+1\) independent core directions, the cube projection supplies \(r\) further directions, and the interval supplies one, so \(Q_k\) is full-dimensional of dimension \(N_k=m+r+2\).

The weight in (14) is the restriction of the global exponential affine function \(B^t=e^{(\log B)t}\). Every ordinary fiber has total unnormalized mass \(LZ\), and the exceptional fiber has total unnormalized mass \(LB^2\), proving the conditional masses \(\alpha\) and \(\eta\).

We next prove (15)--(19). On the uniform interval, the shortest closed ray containing \(h\) has \(a_h=R+1-|h|\) points, so
\(\tau_{\lambda_R}(h)=a_h/L\). Direct summation of its squared depths gives
\[
c_R=\frac{(R+1)^2+2\sum_{j=1}^Rj^2}{L^3}
=\frac{(R+1)^2+R(R+1)(2R+1)/3}{L^3}.
\]
Reflection about \(h\) retains exactly
\(d_h=2(R-|h|)+1=2a_h-1\) interval points, each with geometric weight \(1/L\). Hence
\(H_{\lambda_R}(h)=d_h/L\), and
\[
\beta_R=\frac1{L^3}\sum_{h=-R}^R d_h^2
=\frac13+\frac{2}{3L^2}.
\]
For every exponential tilt at \(h\), the symmetric subinterval of these \(d_h\) points has mean \(h\); Jensen's inequality applied to it gives
\[
C_{\lambda_R}(h)
=\inf_\theta\frac1L\sum_{y=-R}^Re^{\theta(y-h)}
\ge\frac{d_h}{L}.
\]
The zero tilt gives \(C_{\lambda_R}(h)\le1\). Squaring and averaging proves
\(\beta_R\le\gamma_R\le1\).

Fix \(h\) and a nonzero core vertex \(\mathbf v\). Restricting any closed halfspace containing \((\mathbf v,h)\) to the interval line over \(\mathbf v\) gives at least the shorter closed ray, of mass
\(\pi_{\mathbf v}a_h/L\). Conversely, because \(\mathbf v\) is exposed in the core, adding a sufficiently large multiple of a closed exposing inequality isolates that interval line, on which a closed shorter ray attains the bound. This proves (16).

At \((\mathbf0,h)\), reflection gives, for each of the \(K\) outer antipodal columns, exactly \(d_h\) disjoint reflected pairs whose two unnormalized weights are \(B\) and \(B^{-1}\). Every containing closed halfspace selects at least one endpoint from each pair, contributing at least \((K/B)d_h\). Its restriction to the central interval line contains at least \(a_h\) points, including the target, so
\[
\tau_q(\mathbf0,h)\ge\frac{(K/B)d_h+a_h}{ZL}.
\]
For \(h\ge0\), the closed halfspace
\[
2(y-h)-\bigl(2(R-h)+1\bigr)t\ge0
\tag{35}
\]
contains no upper-layer point, exactly the integer heights
\(y=2h-R,\ldots,R\), namely \(d_h\) points, in every lower-layer column, and exactly \(y=h,\ldots,R\), namely \(a_h\) points, in the central column. It therefore attains the lower bound. For \(h<0\), reflect the \(y\)-coordinate in (35). This proves (17) for every interval point, including the endpoints.

Summing (16) over all nonzero core vertices and (17) over the origin gives the first exact identity in (18). The other two follow from the exact tensor factorizations already proved and (8), (15).

Every Boolean base vertex is exposed. Restriction of a containing halfspace to a chosen base fiber gives
\[
\tau_{p_k}(\mathbf u,\mathbf z)
=\alpha\tau_q(\mathbf z)
\quad(\mathbf u\ne\mathbf0),
\qquad
\tau_{p_k}(\mathbf0,2,\mathbf0,h)
=\eta\tau_{\lambda_R}(h).
\tag{36}
\]
Here the lower inequalities follow by restriction. For the reverse inequalities, combine an attaining within-fiber closed halfspace with a sufficiently large multiple of a functional exposing the chosen cube vertex; finiteness of the support makes every other base fiber strictly excluded.

The same restriction gives a lower bound by the conditional capacity. Sending the coefficient of an exposing base functional to infinity suppresses all other fibers and gives the reverse bound. Hence
\[
C_{p_k}(\mathbf u,\mathbf z)=\alpha C_q(\mathbf z)
\quad(\mathbf u\ne\mathbf0),
\qquad
C_{p_k}(\mathbf0,2,\mathbf0,h)=\eta C_{\lambda_R}(h).
\tag{37}
\]
Finally, a Boolean cube vertex cannot be the midpoint of two distinct lattice points whose base coordinates lie in \([0,1]^r\). Therefore every reflected pair centered in one base fiber remains in that same fiber, and
\[
H_{p_k}(\mathbf u,\mathbf z)=\alpha H_q(\mathbf z)
\quad(\mathbf u\ne\mathbf0),
\qquad
H_{p_k}(\mathbf0,2,\mathbf0,h)=\eta H_{\lambda_R}(h).
\tag{38}
\]
In each of (36)--(38), the target probability itself carries one further factor \(\alpha\) or \(\eta\). Squaring and summing proves all three exact cubic decompositions in (19).

7. Asymptotics, atoms, and proper faces.

The parameter choices give the two exact comparisons
\[
\frac K{B^5}=k^{-5}\longrightarrow0,
\qquad
\frac{B^3}{K}=k^3\,2^{-2k}\longrightarrow0.
\tag{39}
\]
Also \(c_R\to1/12\), \(\beta_R\to1/3\), and
\(1/3\le\gamma_R\le1\). Since \(Z\sim KB\) and \(V\sim KB^3\), the first term in the formula for \(M_2(q)\) is asymptotic to \(1/(12K^2)\). Because \(d_h\le2a_h\), its second term is at most
\[
\frac{(2K/B+1)^2c_R}{Z^3}.
\]
The ratio of this upper bound to the first term is
\((2K/B+1)^2/V\sim4K/B^5\), which tends to zero by (39). Thus
\[
M_2(q)\sim\frac1{12K^2}.
\tag{40}
\]
In (8), \((2K+1)^2\sim4K^2\) dominates \(V\) because \(B^3/K\to0\). Hence the remaining identities in (18) give
\[
B_2(q)\sim\frac{4\gamma_R}{KB^3},
\qquad
b(q)\sim\frac{4\beta_R}{KB^3}.
\tag{41}
\]

Furthermore,
\[
\alpha\sim\frac1s,
\qquad
\eta\sim\frac{B}{sK}.
\tag{42}
\]
In the three identities (19), the ratios of the exceptional term to the ordinary-fiber term are bounded, respectively, by constant multiples of
\[
\frac{B^3}{sK},
\qquad
\frac{B^6}{sK^2},
\qquad
\frac{B^6}{sK^2},
\]
all of which tend to zero. Combining (40)--(42) proves the three asymptotics in (20). Since
\[
4^{N_k}=4^{m+r+2}=16(s+1)^2K^2,
\]
the normalized actual moment tends to \(4/3\). Moreover,
\[
\frac{B_2(p_k)}{M_2(p_k)}
\sim48\gamma_R\frac K{B^3},
\qquad
\frac{b(p_k)}{M_2(p_k)}
\sim48\beta_R\frac K{B^3}.
\tag{43}
\]
Here \(K/B^3=4^k/k^3\), while
\(N_k=5k+\lceil\log_2k\rceil+2\), and both \(\gamma_R\) and \(\beta_R\) stay between positive absolute constants and one. Taking base-two logarithms in (43) proves (21), and therefore the claimed failure of every \(2^{o(N)}\) conversion factor.

The largest unnormalized atom in (14) has weight \(B^2\). Thus
\[
2^{N_k}\max_{\mathbf j}p_{k,\mathbf j}
=\frac{4(s+1)KB^2}{L(sZ+B^2)}
\le\frac{2(s+1)}{sB}\longrightarrow0,
\]
which proves (22).

It remains to prove (23). First omit the interval coordinate. The total probability of all upper vertices in all ordinary fibers is
\[
\frac{sKB}{sZ+B^2}=1-\varepsilon_k,
\qquad
\varepsilon_k\longrightarrow0.
\tag{44}
\]
Indeed,
\[
\varepsilon_k
=\frac{s(1+K/B)+B^2}{sZ+B^2},
\]
and after division by \(sKB\), the three terms in its numerator are
\(1/(KB)\), \(1/B^2\), and \(B/(sK)\), all tending to zero.
Consider a proper face of \(Q_k^0\), exposed by a nonzero functional
\[
\mathbf a\cdot\mathbf u+ct+\mathbf v\cdot\mathbf x.
\]
If \(\mathbf v\ne\mathbf0\), then in each upper Boolean \(\mathbf x\)-cube at most half of its \(K\) vertices maximize \(\mathbf v\cdot\mathbf x\). Hence the face contains at most half of the upper mass. If \(\mathbf v=\mathbf0\) and \(\mathbf a\ne\mathbf0\), a level set of \(\mathbf a\cdot\mathbf u\) contains at most \(2^{r-1}\) Boolean vertices: fix every coordinate except one whose coefficient is nonzero, and at most one of its two values can satisfy the level equation. Thus the face meets at most \(2^{r-1}\) complete upper cubes. If \(\mathbf v=\mathbf a=\mathbf0\), then \(c\ne0\). For \(c>0\), the exceptional point at height two excludes all ordinary upper vertices from the maximizing face; for \(c<0\), the ordinary lower vertices exclude them. Treating all mass outside the upper vertices as the error in (44), every proper face of \(Q_k^0\) consequently has probability at most
\[
\frac{2^{r-1}}{2^r-1}+\varepsilon_k
=\frac{s+1}{2s}+\varepsilon_k
=\frac12+o(1).
\tag{45}
\]
A face of \(Q_k^0\times[-R,R]\) whose exposing functional has zero \(y\)-coefficient is governed by (45). If that coefficient is nonzero, the face lies over one interval endpoint and has probability at most \(1/L\). This proves (23).

Equations (11) and (20) are the promised explicit H2 calibration. Both normalized actual moments converge to positive constants, even though (10) and (21) rule out the stated capacity and reflection conversions. Thus all counterexample conclusions concern those conversion mechanisms only, and the unrestricted H2 assertion remains unresolved.

## External sources

none
