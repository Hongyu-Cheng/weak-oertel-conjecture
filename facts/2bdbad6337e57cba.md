---
fact_id: 2bdbad6337e57cba
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: oct2c-multi-interior-pyramid-hitting
depends_on: ["488f0a583886b5fc"]
verifier_run: 9a46f18c615a4004
target_match: null
---

## Statement

Let \(r\ge1\) and \(k\ge2\) be integers, let \(\Delta_r=\operatorname{conv}\{\mathbf0,\mathbf e_1,\ldots,\mathbf e_r\}\), and put \(Q_r=(r+1)\Delta_r-\mathbf1\). Define \(N_a=|aQ_r\cap\mathbb Z^r|\) for integers \(a\ge0\). Let \(H\ge N_k\) be an integer and set \(P=\operatorname{conv}((\{1\}\times kQ_r)\cup\{(-H,\mathbf0)\})\) and \(D=P\cap\mathbb Z^{r+1}\), with the complete lattice support.

There is a unique \(q\in(0,1)\) for which the original weights \(w_{(x,\mathbf z)}=q^{-x}\), for \((x,\mathbf z)\in D\), satisfy \(\sum_{\mathbf I\in D}w_{\mathbf I}\mathbf I=\mathbf0\). Set all other lattice weights to zero and retain \(W=\sum_{\mathbf I\in D}w_{\mathbf I}\). With \(n=r+1\), the notation \(D,w,w_{\max},\phi,B,\mathcal E_{\mathbf J},G_E,m_{\log}\), and \(\mathcal B_{\log}^{\mathrm{hit}}\) has exactly the meaning in accepted fact 488f0a583886b5fc. In particular, \(w_{\max}=q^{-1}\), \(\phi_{(x,\mathbf z)}=(x-1)\log q\), and \(B=(H+1)\log(1/q)\).

The original mean is the allowed lattice target \(\mathbf0\in D\), and

\[
\max_{L\ge0}\frac{m_{\log}(\mathbf0,L;w)}{1+L}
=m_{\log}(\mathbf0,0;w)
\ge\frac{1}{1032}\frac{W}{2^{r+1}}.
\]

Consequently \(\mathcal B_{\log}^{\mathrm{hit}}(w)\) has this same uniform lower bound. Every cutoff uses the complete original source weights. This statement concerns the prescribed original mean and does not assert a new theorem for arbitrary log-concave tables or the locked mixed-integer conjecture.

## Proof

We first audit the full support and the original mean. The defining inequalities of \(Q_r\) are \(z_i\ge-1\) for \(1\le i\le r\) and \(\sum_i z_i\le1\). At every real \(-H\le x\le1\), the cross-section of \(P\) is exactly \(s_xQ_r\), where \(s_x=k(H+x)/(H+1)\). At an integer \(x\) in this interval, put \(a_x=\lfloor s_x\rfloor\). An integer vector lies in \(s_xQ_r\) if and only if \(z_i\ge-a_x\) for every \(i\) and \(\sum_i z_i\le a_x\). Thus

\[
D=\bigcup_{x=-H}^{1}\bigl(\{x\}\times(a_xQ_r\cap\mathbb Z^r)\bigr),
\qquad a_x=\left\lfloor\frac{k(H+x)}{H+1}\right\rfloor.
\]

All these cross-sections are retained; none is replaced by an axis. For any integer \(a\ge0\), the map \(\mathbf z\mapsto(K_1,\ldots,K_{r+1})\), with \(K_i=z_i+a\) for \(i\le r\) and \(K_{r+1}=a-\sum_i z_i\), is a bijection from \(aQ_r\cap\mathbb Z^r\) to nonnegative integer compositions of \(a(r+1)\) into \(r+1\) coordinates. Hence \(N_a=\binom{a(r+1)+r}{r}\). Permuting the composition coordinates preserves this complete finite set, so each coordinate has arithmetic mean \(a\). The arithmetic mean of every cross-section in its \(\mathbf z\)-coordinates is consequently \(\mathbf0\).

The vectors \(t\mathbf e_1\), for integers \(-k\le t\le k\), lie in \(kQ_r\); therefore \(N_k\ge2k+1\) and \(H+1>k\). It follows that \(a_1=k\), \(a_0=k-1\), and \(0\le a_{-j}\le k-1\) for \(1\le j\le H\). Write \(n_j=N_{a_{-j}}\). Thus \(1\le n_j\le N_{k-1}\), and the entire original first-coordinate moment is

\[
F(q)=\frac{N_k}{q}-\sum_{j=1}^{H}j n_jq^j.
\]

Its derivative is \(F'(q)=-N_k/q^2-\sum_{j=1}^H j^2n_jq^{j-1}<0\). Also \(F(q)\to+\infty\) as \(q\downarrow0\), whereas \(F(1)\le N_k-H(H+1)/2<0\), since \(H\ge N_k\ge5\). Continuity and strict decrease give a unique zero in \((0,1)\). Every transverse moment is zero by the complete cross-section calculation, so this zero makes the full original weighted mean exactly \(\mathbf0\).

The mean equation and the bound on \(n_j\) imply

\[
\frac{N_k}{q}=\sum_{j=1}^Hj n_jq^j
\le N_{k-1}\sum_{j=1}^{\infty}jq^j
=\frac{N_{k-1}q}{(1-q)^2}.
\]

Since \(N_k\ge N_{k-1}>0\), this yields \(q/(1-q)\ge\sqrt{N_k/N_{k-1}}\ge1\), so \(q\ge1/2\). The mass on the strictly negative levels is at most their first-moment magnitude, which equals \(N_k/q\). The zero-level mass is \(N_{k-1}\le N_k/q\). Therefore \(W\le3N_k/q\). Finally,

\[
\frac{N_k}{N_{k-1}}
=\prod_{i=1}^{r}\frac{k(r+1)+i}{(k-1)(r+1)+i}
\le\left(\frac{k}{k-1}\right)^r
\le2^r.
\]

Each factor inequality follows by cross-multiplication, reducing to \((k-1)i\le ki\). Consequently the original zero-level mass satisfies \(N_{k-1}\ge qW/(3\cdot2^r)\ge W/(6\cdot2^r)\).

We next prove a uniform closed-halfspace bound for every complete dilate \(aQ_r\cap\mathbb Z^r\), for every integer \(a\ge1\). Let \(N=r+1\), let \(M=aN\), and let \(\mathbf K=(K_1,\ldots,K_N)\) be uniform on the nonnegative integer compositions of \(M\). These letters are auxiliary scalar dimension and total-degree parameters; they do not change the canonical \(n,d,W\). For a nonzero base normal \(\mathbf v\in\mathbb R^r\), append a zero coordinate to obtain \(\mathbf u=(v_1,\ldots,v_r,0)\), and subtract its coordinate mean to obtain coefficients \(v_i'=u_i-N^{-1}\sum_j u_j\). They sum to zero and are not all zero. Under the composition bijection, \(\mathbf v\cdot\mathbf z=Z:=\sum_i v_i'K_i\). Thus \(\mathbb EZ=0\).

For an integer \(s\ge0\), write \((t)_{\underline s}=\prod_{j=0}^{s-1}(t-j)\) and \((t)^{\overline s}=\prod_{j=0}^{s-1}(t+j)\), with empty products one. Put \(c_s=(M)_{\underline s}/(N)^{\overline s}\) for \(1\le s\le4\); if \(M<s\), this numerator is zero. If nonnegative integers \(b_i\) have sum \(s\), then

\[
\mathbb E\prod_i(K_i)_{\underline{b_i}}=c_s\prod_i b_i!.
\]

Indeed, differentiating the geometric series gives \(\sum_{t\ge0}(t)_{\underline b}T^t=b!T^b/(1-T)^{b+1}\). Multiplying these series, taking the coefficient of \(T^M\), and dividing by the number \(\binom{M+N-1}{N-1}\) of compositions proves the formula. When \(M<s\), both the coefficient and the factorial-moment expectation are zero. For each \(s\), \(0\le c_s\le a^s\). In particular, \(c_1=a\) and \(c_2=a(aN-1)/(N+1)\).

Write \(s_2=\sum_i(v_i')^2>0\) and \(s_4=\sum_i(v_i')^4\le s_2^2\). The second-moment expansion gives

\[
\mathbb EZ^2=(c_1+c_2)s_2
=\frac{aN(a+1)}{N+1}s_2
\ge\frac23a^2s_2.
\]

Here \(N\ge2\). We provide the fourth-moment calculation explicitly. Falling-factorial expansion and the preceding moment formula give, with distinct indices whenever different letters occur,

\[
\begin{aligned}
\mathbb EK_i^4&=c_1+14c_2+36c_3+24c_4,\\
\mathbb EK_i^3K_j&=c_2+6c_3+6c_4,\\
\mathbb EK_i^2K_j^2&=c_2+4c_3+4c_4,\\
\mathbb EK_i^2K_jK_l&=c_3+2c_4,\\
\mathbb EK_iK_jK_lK_h&=c_4.
\end{aligned}
\]

For coefficients with zero sum, direct expansion gives

\[
\begin{aligned}
\sum_{i\ne j}(v_i')^3v_j'&=-s_4,\\
\sum_{i<j}(v_i')^2(v_j')^2&=(s_2^2-s_4)/2,\\
\sum_i\sum_{\substack{j<l\\j,l\ne i}}(v_i')^2v_j'v_l'&=s_4-s_2^2/2,\\
\sum_{i<j<l<h}v_i'v_j'v_l'v_h'&=s_2^2/8-s_4/4.
\end{aligned}
\]

The first identity uses \(\sum_{j\ne i}v_j'=-v_i'\); the second expands \(s_2^2\). For the third, its inner pair sum is \(((v_i')^2-(s_2-(v_i')^2))/2\). The fourth follows by expanding \((\sum_i v_i')^4=0\) and substituting the first three. All identities also hold when there are too few indices for a displayed sum, interpreting that sum as zero. Expanding \(Z^4\) by the five multiplicity patterns \(4\), \(3+1\), \(2+2\), \(2+1+1\), and \(1+1+1+1\), with respective coefficients \(1,4,6,12,24\), therefore gives

\[
\begin{aligned}
\mathbb EZ^4
&=(c_1+7c_2+12c_3+6c_4)s_4
 +(3c_2+6c_3+3c_4)s_2^2\\
&\le38a^4s_2^2
\le\frac{171}{2}(\mathbb EZ^2)^2
\le86(\mathbb EZ^2)^2.
\end{aligned}
\]

The first upper bound uses \(a\ge1\), \(c_s\le a^s\le a^4\), and \(s_4\le s_2^2\). Put \(\sigma^2=\mathbb EZ^2>0\). Hölder's inequality applied to \(|Z|^{2/3}|Z|^{4/3}\) gives \(\mathbb E|Z|\ge\sigma^3/(\mathbb EZ^4)^{1/2}\ge\sigma/\sqrt{86}\). Since \(\mathbb EZ=0\), both \(\mathbb EZ_+\) and \(\mathbb EZ_-\) equal \(\mathbb E|Z|/2\), where \(Z_+=\max\{Z,0\}\) and \(Z_-=\max\{-Z,0\}\). Cauchy-Schwarz bounds these expectations by \(\sigma\sqrt{\mathbb P(Z>0)}\) and \(\sigma\sqrt{\mathbb P(Z<0)}\), respectively. Each strict probability is consequently at least \(1/344\). Every closed halfspace through \(\mathbf0\) in the complete dilate contains its corresponding strict event, so its count is at least \(N_a/344\). Equality atoms are retained throughout. A zero base normal includes the whole slice and also satisfies this bound.

Return to the original complete pyramid. Every closed halfspace through \(\mathbf0\) has a defining inequality \(\beta x+\mathbf v\cdot\mathbf z\ge0\), with \((\beta,\mathbf v)\ne(0,\mathbf0)\). On \(x=0\), this is \(\mathbf v\cdot\mathbf z\ge0\). The entire zero cross-section is \((k-1)Q_r\cap\mathbb Z^r\), its original weights are all exactly one, and \(k-1\ge1\). The proved count bound thus gives original halfspace mass at least \(N_{k-1}/344\), regardless of the sign or magnitude of \(\beta\).

For completeness, the original table is globally extendable: set \(f(x,\mathbf z)=q^{-x}\) on the convex polytope \(P\) and zero elsewhere. This function agrees with all complete lattice weights and zeros and is log-concave. Accepted fact 488f0a583886b5fc therefore applies with exactly the normalization in the statement. Its potential \(\phi\) is affine on \(D\), so every positive barycentric support at every allowed target has \(G_E=0\). In particular, all cutoff families at the original mean coincide, and \(m_{\log}(\mathbf0,L;w)=m_{\log}(\mathbf0,0;w)\) for all \(L\ge0\).

The exact closed lower-halfspace characterization in 488f0a583886b5fc at cutoff zero has atom scores
\(\mathbf b\cdot\mathbf I+t(\phi_{\mathbf0}-\phi_{\mathbf I})=(b_x-t\log q)x+\mathbf b_z\cdot\mathbf z\), with \(t\ge0\). If the resulting base normal vanishes, every original atom is included, with mass \(W\). Every nonzero base normal is available by taking \(t=0\). Hence its minimum is exactly the original closed base-halfspace depth at \(\mathbf0\). This includes all equality atoms and all \(t=0\) normals. The zero-slice bound now gives

\[
\begin{aligned}
\max_{L\ge0}\frac{m_{\log}(\mathbf0,L;w)}{1+L}
&=m_{\log}(\mathbf0,0;w)\\
&\ge\frac{N_{k-1}}{344}
\ge\frac{W}{2064\cdot2^r}
=\frac1{1032}\frac{W}{2^{r+1}}.
\end{aligned}
\]

No source weight was replaced, renormalized, or conditionally tilted; the temporary uniform composition law was used only to count the original weight-one zero slice. The bound holds for every permitted \(r,k,H\), completing the registered whole-family test.

## External sources

None. The only accepted input used is 488f0a583886b5fc for the canonical logarithmic integral hitting formulation and its exact closed-halfspace characterization. The support audit, original-mean equation, adjacent-shell count bound, and uniform composition halfspace estimate are proved above.
