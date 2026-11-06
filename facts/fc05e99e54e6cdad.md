---
fact_id: fc05e99e54e6cdad
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: oct3dw-allheight-positive-source-averaged-noise
depends_on: ["43cb56218b18ec82","9ba4a3963a51edd3"]
verifier_run: 7df57baf4fcd465a
target_match: null
---

## Statement

Let \(m,h,L\) be positive integers with \(L\ge2h\), and put \(K:=\lfloor L/h\rfloor\). On the original support
\[
E_{L,h,m}:=\left\{(\mathbf x,y)\in\mathbb Z_{\ge0}^{m+1}:\sum_{i=1}^m x_i+hy\le L\right\},
\]
let \((\mathbf X,Y)\) have the strictly positive law
\[
p(\mathbf x,y)=\frac{\exp(\beta\sum_i x_i+\theta y)}{\mathcal Z},
\qquad \beta\ge0,\quad\theta\in\mathbb R,
\]
where \(\mathcal Z\) is the sum of these weights over \(E_{L,h,m}\). Suppose the full mean is \((j\mathbf1,1)\), with integer \(j\). Then every \(\mathbf a\in\mathbb R^m\), with
\(N:=\mathbf a\cdot(\mathbf X-\mathbb E[\mathbf X\mid Y])\), satisfies
\[
\mathbb EN^4\le1{,}200{,}000{,}000{,}000\, (\mathbb EN^2)^2.
\]
The constant is independent of \(m,h,L,K,\beta,\theta,j\) and \(\mathbf a\). The statement includes \(m=1\), zero-variance directions, and the zero final budget \(L-hK=0\).

## Proof

We retain the source notation of accepted fact 9ba4a3963a51edd3: \(X_\Sigma:=\sum_iX_i\), \(B_y:=L-hy\), \(A:=B_Y-X_\Sigma\), and \(r:=e^{-\beta}\). The law \(p\) here is the law called \(R\) in accepted fact 43cb56218b18ec82; its variable \(r=e^\beta\) is the reciprocal of our \(r\). Both predecessors' \(E_{L,h,m}\) and transverse partition functions refer to the same complete original budget simplices. We extend their general partition, slack, and composition computations below, rather than applying a three-height source theorem to a larger support.

For nonnegative integers \(s,B\), define
\[
D_m(s):=\binom{s+m-1}{m-1},\qquad
Z_m(B,u):=\sum_{s=0}^B D_m(s)e^{us},\qquad
H_m(B,r):=\sum_{a=0}^B r^aD_m(B-a).
\]
Thus \(Z_m(B,u)\) has exactly the normalization in 43cb56218b18ec82 and 9ba4a3963a51edd3, and \(H_m(B,r)=r^BZ_m(B,\beta)\). The count \(D_m(s)\) follows by placing \(m-1\) separators among \(s\) units. Given \((Y,X_\Sigma)=(y,s)\), \(\mathbf X\) is uniform on the complete compositions of \(s\) into \(m\) parts. Given \(Y=y\), its slack therefore has probabilities
\[
\Pr(A=a\mid Y=y)=\frac{r^aD_m(B_y-a)}{H_m(B_y,r)}
\quad(0\le a\le B_y),\qquad 0\le y\le K.
\tag{1}
\]
These are the original conditional laws, including the point mass when \(B_y=0\).

Positivity at a point with \(x_1>0\) gives \(j>0\), so \(j\ge1\). Positivity at the origin gives \(\mathbb EA>0\). By the full mean,
\(\mathbb EA=L-mj-h\) is an integer, so \(\mathbb EA\ge1\). Consequently
\[
B_1=mj+\mathbb EA\ge m+1,\qquad
B_0\le2B_1,\qquad 0\le B_y\le B_0\quad(0\le y\le K).
\tag{2}
\]
The middle inequality is exactly \(L\ge2h\).

We also have \(1/2\le r\le1\). The upper bound follows from \(\beta\ge0\). If \(r<1\), the successive unnormalized slack ratios in every positive budget satisfy
\[
\frac{r^{a+1}D_m(B-a-1)}{r^aD_m(B-a)}
=r\frac{B-a}{B-a+m-1}\le r\quad(0\le a<B).
\tag{3}
\]
Shifting the sum of masses gives \(\Pr(A\ge k\mid Y=y)\le r^k\). Each support is finite, so summing the tails gives \(\mathbb E[A\mid Y=y]<r/(1-r)\), also when \(B_y=0\). Averaging and using \(\mathbb EA\ge1\) forces \(r>1/2\). When \(r=1\) the asserted bounds are immediate.

We next establish a universal mass bound at the original height one. The budget log-concavity calculation in 43cb56218b18ec82 works for every real \(u\) and every nonnegative budget; here is its verification. Put \(t_s:=D_m(s)e^{us}\). Its successive positive ratios \(t_s/t_{s-1}=e^u(s+m-1)/s\) decrease with \(s\). For \(B\ge1\) and \(1\le i\le B\), this implies \(t_{B+1}t_{i-1}\le t_Bt_i\). Summing gives
\[
t_{B+1}Z_m(B-1,u)\le t_B\sum_{i=1}^Bt_i<t_BZ_m(B,u).
\]
Therefore
\(Z_m(B,u)^2-Z_m(B-1,u)Z_m(B+1,u)=t_BZ_m(B,u)-t_{B+1}Z_m(B-1,u)>0\). In particular its positive successive ratios decrease. Multiplication by \(r^B\) shows the same ratio monotonicity for \(H_m(B,r)\).

Write \(p_y:=\Pr(Y=y)\). These masses are positive for every \(0\le y\le K\), and they are proportional to \(e^{\theta y}Z_m(B_y,\beta)\). Summing the decreasing successive differences of \(\log Z_m(B,\beta)\) across adjacent intervals of length \(h\) gives
\(Z_m(B_y,\beta)^2\ge Z_m(B_{y-1},\beta)Z_m(B_{y+1},\beta)\) for \(1\le y<K\). Thus \((p_y)_{y=0}^K\) is log-concave.

The original mean \(\mathbb EY=1\) gives
\(p_0=\sum_{y=2}^K(y-1)p_y\ge p_2\). Log-concavity at one then gives \(p_2^2\le p_0p_2\le p_1^2\), hence \(p_2\le p_1\). To bound \(p_0\), put \(\rho:=p_1/p_0\). If \(\rho\ge1\), then \(p_0\le p_1\). If \(\rho<1\), log-concavity implies \(p_{y+1}/p_y\le\rho\) throughout the positive support. Shifting sums gives \(\Pr(Y\ge k)\le\rho^k\), so \(1=\mathbb EY\le\rho/(1-\rho)\), and \(\rho\ge1/2\). In either case \(p_0\le2p_1\). Finally Markov's inequality gives \(\Pr(Y\ge3)\le1/3\), whence
\[
\frac23\le p_0+p_1+p_2\le4p_1,
\qquad p_1\ge\frac16.
\tag{4}
\]
This argument uses all original heights; it does not replace their law by a symmetric three-point law.

Let \(A_B\) have the budget-\(B\) slack law in (1), and put \(\mu_B:=\mathbb EA_B\), \(v_B:=\operatorname{Var}A_B\), as in 9ba4a3963a51edd3. To map the notation of 43cb56218b18ec82 explicitly, \(\mu_B\) here equals \(B\) minus its budget-\(B\) total mean \(\mu_B(\beta)\), and \(v_B\) here equals its total variance \(v_B(\beta)\). At height one, its \(v_1\) is our \(v_{B_1}\).

By (3), each positive-budget slack law has decreasing masses and nonincreasing successive mass ratios. We record the scalar estimates used in 9ba4a3963a51edd3, with their proof. Suppose \(T\) has decreasing log-concave positive masses \(u_0,\ldots,u_b\), and let \(\mu:=\mathbb ET\), \(v:=\operatorname{Var}T\). Set \(u_{b+1}:=0\). The weights \(\lambda_n:=(n+1)(u_n-u_{n+1})\), \(0\le n\le b\), are nonnegative, sum to one by telescoping, and express this law as a mixture of uniform laws on \(\{0,\ldots,n\}\). Let \(M\) have masses \(\lambda_n\); it is the mixture index called \(R\) in 9ba4a3963a51edd3, renamed to avoid collision with the source law \(R\) in 43cb56218b18ec82. The uniform-law first and second moments give
\[
\mu=\frac{\mathbb EM}{2},\qquad
v=\frac{\mathbb EM^2}{3}+\frac{\mathbb EM}{6}-\frac{(\mathbb EM)^2}{4}
\ge\frac{\mu^2+\mu}{3}.
\tag{5}
\]

For its tails \(F(k):=\Pr(T\ge k)\), the expression
\(F(k)/u_k=\sum_{\ell=0}^{b-k}u_{k+\ell}/u_k\) decreases with \(k\), since every product of successive mass ratios decreases and the sum loses terms. Thus \(F(k+1)/F(k)=1-u_k/F(k)\) decreases. Products of the tail ratios give \(F(k+\ell)\le F(k)F(\ell)\); when any relevant tail is zero, the inequality is immediate. Take the integer \(t:=\lceil2(\mu+1)\rceil\le3(\mu+1)\). Markov's inequality and the tail product bound give \(F(t)\le1/2\) and \(F(nt)\le2^{-n}\). On \(nt\le T<(n+1)t\), one has \((T+1)^4\le((n+1)t)^4\). Consequently
\[
\mathbb E(T+1)^4\le t^4\sum_{n\ge0}\frac{(n+1)^4}{2^n}
=300t^4\le24300(\mu+1)^4.
\tag{6}
\]
The sum equals 300 by four differentiations of the geometric series.

For \(A_{B_1}\), the first unnormalized ratio is \(rB_1/(B_1+m-1)\ge1/4\), by (2) and \(r\ge1/2\). Its mass at zero is therefore at most \(4/5\), and \(\mu_{B_1}\ge1/5\). Applying (5) gives
\[
(\mu_{B_1}+1)^2\le6(\mu_{B_1}^2+\mu_{B_1})\le18v_{B_1}.
\]
Together with (6), this yields
\[
\mathbb E(A_{B_1}+1)^4\le24300\cdot324\,v_{B_1}^2.
\tag{7}
\]

We now check the original-budget comparisons for every height. The tail identity
\[
\Pr(A_B\ge k)=r^k\frac{H_m(B-k,r)}{H_m(B,r)}\quad(0\le k\le B)
\tag{8}
\]
follows directly by shifting the slack index. The ratio on the right is a product of \(k\) reciprocal successive ratios of \(H_m\). Their monotonicity proved above implies that each such tail increases with \(B\). A budget below \(k\) has zero tail. Hence \(A_B\) is stochastically nondecreasing with \(B\), and
\(\mathbb EA_{B_y}^4\le\mathbb EA_{B_0}^4\) for every \(0\le y\le K\).

To use \(B_0\le2B_1\), normalize at the zero atom by defining
\[
w_B(a):=r^a\frac{D_m(B-a)}{D_m(B)},\qquad
W_B:=\sum_{a=0}^Bw_B(a),\qquad
\Pr(A_B=a)=w_B(a)/W_B.
\]
For \(0\le a\le B\),
\[
\frac{D_m(B-a)}{D_m(B)}=\prod_{i=1}^{m-1}\left(1-\frac{a}{B+i}\right),
\tag{9}
\]
with empty product one when \(m=1\). This increases with \(B\) for fixed \(a\), so \(W_{B_0}\ge W_{B_1}\). If \(2k\le B_0\), then \(k\le B_1\) and \(B_0+i\le2(B_1+i)\). Formula (9), together with \(r^{2k}\le r^k\), gives \(w_{B_0}(2k)\le w_{B_1}(k)\). After normalization,
\(\Pr(A_{B_0}=2k)\le\Pr(A_{B_1}=k)\). Since the budget-\(B_0\) masses decrease, the same upper bound holds for its atom at \(2k+1\) whenever present. Grouping even and odd atoms, and enlarging the sum by any missing endpoint terms, gives
\[
\mathbb EA_{B_0}^4
\le\sum_{k=0}^{B_1}\bigl((2k)^4+(2k+1)^4\bigr)\Pr(A_{B_1}=k)
\le32\mathbb E(A_{B_1}+1)^4.
\tag{10}
\]

For any nonnegative \(T\), the inequality \(|x+y|^4\le8(|x|^4+|y|^4)\) and Jensen's inequality give \(\mathbb E(T-\mathbb ET)^4\le16\mathbb ET^4\). Equations (7)--(10) therefore imply, for every original height including zero-budget endpoints,
\[
\mathbb E(A_{B_y}-\mu_{B_y})^4
\le512\cdot24300\cdot324\,v_{B_1}^2
=4{,}031{,}078{,}400\,v_{B_1}^2.
\]
Put \(V_A:=\mathbb E\operatorname{Var}(A\mid Y)=\sum_{y=0}^Kp_yv_{B_y}\). By (4), \(V_A\ge v_{B_1}/6\). Averaging the preceding bound with the original \(p_y\) yields
\[
\mathbb E(A-\mathbb E[A\mid Y])^4
\le145{,}118{,}822{,}400\,V_A^2.
\tag{11}
\]

Next consider coefficients \(\mathbf b\in\mathbb R^m\) with \(\sum_i b_i=0\), initially for \(m\ge2\). Write \(Q:=\sum_i b_i^2\), \(Q_4:=\sum_i b_i^4\). For a uniform complete composition \(\mathbf C_s\) of a nonnegative integer \(s\) into \(m\) parts, the moment calculation in 9ba4a3963a51edd3 gives
\[
\begin{aligned}
\mathbb E(\mathbf b\cdot\mathbf C_s)^2
&=\frac{s(s+m)}{m(m+1)}Q,\\
\mathbb E(\mathbf b\cdot\mathbf C_s)^4
&=\frac{(s)_{\underline4}}{(m)_{\overline4}}(3Q^2+6Q_4)
+6\frac{(s)_{\underline3}}{(m)_{\overline3}}(Q^2+2Q_4)\\
&\quad+\frac{(s)_{\underline2}}{(m)_{\overline2}}(3Q^2+7Q_4)+\frac{s}{m}Q_4.
\end{aligned}
\tag{12}
\]
Here \((s)_{\underline k}\) and \((m)_{\overline k}\) are falling and rising factorials, with the falling factorial zero when \(k>s\). For completeness, these identities depend only on the composition law, as can be verified by taking \(\mathbf U\) uniform on the real probability simplex and conditionally drawing \(\mathbf C\) multinomial with \(s\) trials. Integration of monomials gives
\(\mathbb E\prod_iU_i^{k_i}=\prod_i k_i!/(m)_{\overline k}\), where \(k=\sum_i k_i\). This follows by iterating the beta integral \(\int_0^1t^a(1-t)^b\,dt=a!b!/(a+b+1)!\), itself proved by integration by parts. Each composition then has mixture probability \(s!(m-1)!/(s+m-1)!=1/D_m(s)\).

Put \(u_\ell:=\sum_i b_i^\ell U_i\). Grouping equal trial indices in the fourth power gives
\[
\mathbb E[(\mathbf b\cdot\mathbf C)^4\mid\mathbf U]
=(s)_{\underline4}u_1^4+6(s)_{\underline3}u_1^2u_2
+3(s)_{\underline2}u_2^2+4(s)_{\underline2}u_1u_3+s u_4.
\]
Using the monomial integral and \(\sum_i b_i=0\) gives
\[
\begin{aligned}
\mathbb Eu_1^2&=Q/(m)_{\overline2},&\mathbb Eu_2&=Q/m,\\
\mathbb Eu_1^4&=(3Q^2+6Q_4)/(m)_{\overline4},&
\mathbb Eu_1^2u_2&=(Q^2+2Q_4)/(m)_{\overline3},\\
\mathbb Eu_2^2&=(Q^2+Q_4)/(m)_{\overline2},&
\mathbb Eu_1u_3&=Q_4/(m)_{\overline2},\qquad\mathbb Eu_4=Q_4/m.
\end{aligned}
\]
Substitution and the two-trial expansion prove (12) for every \(s\), independently of the number of heights.

Since \(Q_4\le Q^2\) and \((s)_{\underline k}/(m)_{\overline k}\le(s/m)^k\), (12) gives
\[
\mathbb E(\mathbf b\cdot\mathbf C_s)^4
\le Q^2\bigl(9(s/m)^4+18(s/m)^3+10(s/m)^2+s/m\bigr).
\]
Every original total satisfies \(s\le B_0\), and \(B_0/m\ge1\) by (2). Thus every displayed power is at most \((B_0/m)^4\). With \(T:=\mathbf b\cdot\mathbf X\), conditioning on \((Y,X_\Sigma)\) and averaging gives
\[
\mathbb ET^4\le38(B_0/m)^4Q^2\le608(B_1/m)^4Q^2.
\tag{13}
\]

The conditional composition mean of \(T\) is zero, so put \(V_C:=\mathbb ET^2\). At \(\beta=0\), the budget-\(B_1\) simplex is uniform; appending its slack produces a uniform complete composition of \(B_1\) into \(m+1\) parts. Its total mean is therefore \(mB_1/(m+1)\). Differentiating the finite partition sum shows that the total mean has derivative equal to its nonnegative variance with respect to the common tilt. Hence the original \(\beta\ge0\) gives \(\mathbb E[X_\Sigma\mid Y=1]\ge mB_1/(m+1)\). Equations (4) and (12), followed by Jensen's inequality, now imply
\[
\begin{aligned}
V_C
&=\frac{Q}{m(m+1)}\mathbb E[X_\Sigma(X_\Sigma+m)]\\
&\ge\frac{Q}{6m(m+1)}\bigl(\mathbb E[X_\Sigma\mid Y=1]\bigr)^2\\
&\ge\frac{QmB_1^2}{6(m+1)^3}
\ge\frac{Q}{48}(B_1/m)^2.
\end{aligned}
\tag{14}
\]
For the last step, \((m/(m+1))^3\ge1/8\). Combining (13) and (14) yields
\[
\mathbb ET^4\le1{,}400{,}832\,V_C^2.
\tag{15}
\]
If \(m=1\), a coefficient vector with zero sum is zero, so (15) holds directly with \(T=V_C=0\).

Finally set \(\bar a:=m^{-1}\sum_i a_i\) and \(b_i:=a_i-\bar a\). Permutation invariance of the original transverse law gives \(\mathbb E[X_i\mid Y]=\mathbb E[X_\Sigma\mid Y]/m\). With \(U:=X_\Sigma-\mathbb E[X_\Sigma\mid Y]\), the original noise decomposes as
\[
N=\bar aU+T,\qquad U=-(A-\mathbb E[A\mid Y]),\qquad
\mathbb EN^2=\bar a^2V_A+V_C.
\tag{16}
\]
The cross term vanishes because \(\mathbb E[T\mid Y,X_\Sigma]=0\), while \(U\) is determined by \((Y,X_\Sigma)\). Applying the fourth-power sum inequality, then (11) and (15), gives
\[
\begin{aligned}
\mathbb EN^4
&\le8\bigl(145{,}118{,}822{,}400\,\bar a^4V_A^2+1{,}400{,}832\,V_C^2\bigr)\\
&\le1{,}160{,}950{,}579{,}200\,(\bar a^2V_A+V_C)^2\\
&\le1{,}200{,}000{,}000{,}000\,(\mathbb EN^2)^2.
\end{aligned}
\]
All height averages used the original \(p_y\). Formula (16) also establishes the zero-variance cases. This proves the asserted estimate for every \(K\ge2\).

## External sources

none
