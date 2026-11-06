---
fact_id: d1c92fee58caca38
kind: lemma
author: "research-agent"
assurance: LLM-verified
subgoal_id: oct3du-unequal-heavy-normal-band-arithmetic
depends_on: ["01a4100542206b94","609407d6db81b18b"]
verifier_run: 5c49328735814bf0
target_match: null
---

## Statement

Let \(m,h_1,h_2,L\) be positive integers with \(L\ge\max\{h_1,h_2\}\), and let \(\lambda\in\mathbb R\). Put \(g_{\rm ar}=\gcd(h_1,h_2)\), \(a=h_1/g_{\rm ar}\), \(b=h_2/g_{\rm ar}\), and \(Q=\lfloor L/g_{\rm ar}\rfloor\). Let
\[
D=\{(\mathbf x,y_1,y_2)\in\mathbb Z_{\ge0}^{m+2}:
          \textstyle\sum_i x_i+h_1y_1+h_2y_2\le L\},
\qquad
p(\mathbf x,y_1,y_2)=\frac{e^{\lambda(h_1y_1+h_2y_2)}}{\mathcal Z},
\]
where \(\mathcal Z\) is the sum of the displayed numerator over the whole original support \(D\). Define \(n(q)=|\{(y_1,y_2)\in\mathbb Z_{\ge0}^2:ay_1+by_2=q\}|\) and \(F_m(T)=\binom{T+m}{m}\) for integers \(T\ge0\). Thus
\(\mathcal Z=\sum_{q=0}^Q n(q)F_m(L-g_{\rm ar}q)e^{\lambda g_{\rm ar}q}\), with all original atoms and all residues included.

For integers \(0\le q_0\le q_1\le Q\) with \(n(q_0),n(q_1)>0\), define \(N_{q_0,q_1}=\sum_{q=q_0}^{q_1}n(q)\) and
\[
\eta_{q_0,q_1}
=\frac{F_m(L-g_{\rm ar}q_1)N_{q_0,q_1}}{\mathcal Z}
\begin{cases}
e^{\lambda g_{\rm ar}q_0},&\lambda\ge0,\\
e^{\lambda g_{\rm ar}q_1},&\lambda<0.
\end{cases}
\]
Let \(\eta_*\) be the maximum of these coefficients, and put \(H_0=\sum_{i=1}^m(L+i)^{-1}\). Then
\[
\lambda\le0\quad\Longrightarrow\quad
\eta_*\ge\frac{(1-e^{-1})^3}{e+1},
\qquad
0\le\lambda\le H_0\quad\Longrightarrow\quad
\eta_*\ge\frac{1}{8(m+1)^2}.
\tag{1}
\]
In particular, \(\eta_*\ge1/[8(m+1)^2]\) whenever \(\lambda\le H_0\).

Use the actual closed-halfspace depth \(\tau_p\) and its original-root moment \(M_3(p)=\sum_{\mathbf z\in D}p(\mathbf z)\tau_p(\mathbf z)^3\) exactly as defined in 01a4100542206b94, with its ambient dimension \(N=m+2\) and its moment exponent equal to \(3\). Let \(g>1\) be the rank-gain constant of 609407d6db81b18b and put \(g_0=\min\{2,g^{3/2}\}\). For every \(\lambda\le H_0\),
\[
M_3(p)\ge
\frac{g_0^m}{32\cdot8^4(m+1)^8}\,8^{-(m+2)}
\ge
\frac{1}{32\cdot8^4g_0}
       \left(\frac{\log g_0}{8}\right)^8\,8^{-(m+2)}.
\tag{2}
\]
These inequalities use the unchanged original probability \(\mathcal Z^{-1}e^{\lambda(h_1y_1+h_2y_2)}\) at each root.

The exact period description is as follows. Put \(P=ab\). For each \(r\in\{0,\ldots,P-1\}\), let \(0\le c<b\), \(0\le d<a\) be the unique pair with \(ac+bd\equiv r\pmod P\), and write \(ac+bd=r+P\delta_r\). Then \(\delta_r\in\{0,1\}\), and, for every integer \(t\ge0\),
\[
n(Pt+r)=t+1-\delta_r,\qquad n(q+P)=n(q)+1.
\tag{3}
\]
Thus \(n(q)\) is either \(\lfloor q/P\rfloor\) or \(\lfloor q/P\rfloor+1\), including its first-period zeros.

Nevertheless, define the full top-cap count
\(A_Q(R)=|\{(y_1,y_2)\in\mathbb Z_{\ge0}^2:Q-R\le ay_1+by_2\le Q\}|\).
For every integer \(r\ge1\), the coprime unequal weights \(a=6r\), \(b=6r+1\), and \(Q=18r^2\) satisfy
\[
A_Q(2r)=1,\qquad A_Q(4r)=r+1.
\tag{4}
\]
All these heights lie below \(ab\). Consequently no absolute constant can make \(A_Q(2R)\le C A_Q(R)\) hold for every such exposed normal cap. Formula (4) does not assert that \(\eta_*\) tends to zero.

## Proof

We first verify the normalization and arithmetic from the original support. For each heavy pair \((y_1,y_2)\) of height \(g_{\rm ar}q\), the light-coordinate support is \(\Delta_{L-g_{\rm ar}q,m}=\{\mathbf x\in\mathbb Z_{\ge0}^m:\sum_i x_i\le L-g_{\rm ar}q\}\). Adjoining its nonnegative slack makes its points compositions of \(L-g_{\rm ar}q\) into \(m+1\) coordinates. Their number is \(F_m(L-g_{\rm ar}q)\). The atom weight depends only on the heavy height. Summing this weight over all heavy pairs and all light points proves the stated exact expression for \(\mathcal Z\).

Every heavy pair has a unique decomposition \(y_1=c+bj_1\), \(y_2=d+aj_2\), with \(0\le c<b\), \(0\le d<a\), and \(j_1,j_2\ge0\). Its normal height is \(q=ac+bd+ab(j_1+j_2)\). If two remainder pairs have the same height modulo \(ab\), reduction modulo \(b\) and coprimality give equality of their \(c\)'s, and reduction modulo \(a\) gives equality of their \(d\)'s. There are \(ab\) remainder pairs, so they give all residues bijectively. Moreover, \(0\le ac+bd\le2ab-a-b<2ab\), proving \(\delta_r\in\{0,1\}\). At height \(Pt+r\), the remaining equation is \(j_1+j_2=t-\delta_r\). It has \(t-\delta_r+1\) solutions when the right side is nonnegative, and no solutions when \(t=0,\delta_r=1\). In the latter case the same formula is zero. This proves (3). It proves the normalization using every residue, rather than normalizing separately on a chosen remainder pair.

For the coefficient estimates, it is convenient to use physical height. For every real \(s\ge0\), put
\(B(s)=|\{(y_1,y_2)\in\mathbb Z_{\ge0}^2:h_1y_1+h_2y_2\le s\}|\).
This includes every occupied primitive normal height up to \(s/g_{\rm ar}\).
For an integer \(k\ge1\), the coordinatewise map
\((y_1,y_2)\mapsto(\lfloor y_1/k\rfloor,\lfloor y_2/k\rfloor)\)
takes the set counted by \(B(ks)\) into the set counted by \(B(s)\). Each image has at most \(k^2\) preimages. Hence
\[
B(ks)\le k^2 B(s)\qquad(k\in\mathbb Z_{\ge1},\ s\ge0).
\tag{5}
\]
This is an origin-centered count estimate; it is not used for a cap centered at the top height.

Extend \(F_m(T)\) to real \(T\ge0\) by the product \(F_m(T)=\prod_{i=1}^m(T+i)/i\). This extension equals the original binomial count at integer \(T\). On \(0\le s\le L\), set \(f(s)=F_m(L-s)e^{\lambda s}\). Then
\[
(\log f)'(s)=\lambda-\sum_{i=1}^m\frac{1}{L-s+i},
\qquad
(\log f)''(s)=-\sum_{i=1}^m\frac{1}{(L-s+i)^2}<0.
\tag{6}
\]
These identities concern the one-variable continuous product, not an asserted log-concavity of the projected lattice height table \(n(q)f(g_{\rm ar}q)\).

Suppose first that \(\lambda\le0\). The function \(f\) is strictly decreasing. If \(f(L)\le f(0)/e\), choose the unique \(R\in(0,L]\) with \(f(R)=f(0)/e\). Otherwise put \(R=L\). In both cases \(f(s)\ge f(0)/e\) for \(0\le s\le R\). If \(R<L\), concavity of \(\log f\) implies
\[
f(s)\le f(0)e^{-s/R}\qquad(R\le s\le L).
\tag{7}
\]
Indeed the chord slope from \(0\) to any \(s\ge R\) is no larger than the chord slope from \(0\) to \(R\), which equals \(-1/R\).

Let \(g_{\rm ar}q_1\) be the largest occupied physical height at most \(R\), and take \(q_0=0\). Such a height exists because the origin is occupied. The complete band has \(N_{0,q_1}=B(R)\), and its coefficient is \(B(R)f(g_{\rm ar}q_1)/\mathcal Z\). The band endpoints are occupied, as required. The part of the original sum with height at most \(R\) is at most \(f(0)B(R)\). For each integer \(j\ge1\), the part whose height lies in \((jR,(j+1)R]\) is at most \(f(0)e^{-j}B((j+1)R)\), by (7). If \(R=L\), these latter parts are empty, so the same upper bound remains valid. Applying (5) with \(k=j+1\) gives
\[
\mathcal Z
\le f(0)B(R)\sum_{j=0}^\infty(j+1)^2e^{-j}
=f(0)B(R)\frac{1+e^{-1}}{(1-e^{-1})^3}.
\tag{8}
\]
Here points at exactly \(jR\) belong to the preceding closed interval, so no boundary mass is lost. Since \(f(g_{\rm ar}q_1)\ge f(0)/e\), (8) proves the first bound of (1).

Now suppose \(0\le\lambda\le H_0\). Formula (6) shows that \(f\) is nonincreasing, since the reciprocal sum in (6) is at least \(H_0\). Thus \(\mathcal Z\le F_m(L)B(L)\). Put \(R=L/[2(m+1)]\), choose the largest occupied height \(g_{\rm ar}q_1\le R\), and again take \(q_0=0\). The positive-tilt minimum exponential on this complete band is exactly one. Furthermore,
\[
\frac{F_m(L-g_{\rm ar}q_1)}{F_m(L)}
\ge\frac{F_m(L-R)}{F_m(L)}
=\prod_{i=1}^m\left(1-\frac{R}{L+i}\right)
\ge\left(1-\frac{R}{L+1}\right)^m
\ge1-\frac{mR}{L+1}\ge\frac12.
\tag{9}
\]
The penultimate inequality is the elementary Bernoulli inequality. Apply (5) with the integer \(k=2(m+1)\), for which \(kR=L\). It follows that
\[
\eta_{0,q_1}
=\frac{F_m(L-g_{\rm ar}q_1)B(R)}{\mathcal Z}
\ge\frac12\frac{B(R)}{B(L)}
\ge\frac{1}{8(m+1)^2}.
\tag{10}
\]
This proves the second bound of (1). Also \(2<e<3\) implies \((1-e^{-1})^3/(e+1)>1/32\), and \(1/32\ge1/[8(m+1)^2]\) for \(m\ge1\). Hence the combined bound in (1) holds for every \(\lambda\le H_0\).

We next derive (2) independently for the complete original bands. Fix any admissible \(q_0,q_1\), and put \(T=L-g_{\rm ar}q_1\). Use the heavy support in original coordinates,
\[
E_{q_0,q_1}
=\{(y_1,y_2)\in\mathbb Z_{\ge0}^2:
          q_0\le ay_1+by_2\le q_1\}.
\]
Its cardinality is \(N_{q_0,q_1}\). It is the full integer-point set of the bounded convex region cut out by its displayed linear inequalities. Its convex hull lies in this region, so \(E_{q_0,q_1}=\operatorname{conv}(E_{q_0,q_1})\cap\mathbb Z^2\). This argument includes lower-dimensional bands, missing projected heights, and every residue. The product \(\Delta_{T,m}\times E_{q_0,q_1}\) is contained in the whole original \(D\).

Let \(u_{T,m}\) and \(u_E\) be the uniform probability laws on these two factors. Write \(U=u_{T,m}\otimes u_E\), extended by zero off the product. Every product atom has mass \(1/[F_m(T)N_{q_0,q_1}]\). By the original exponential weights and their minimum over the complete band,
\(p\ge\eta_{q_0,q_1}U\) pointwise, using the original \(\mathcal Z\).

We verify the needed moment bound for the transverse factor. For \(T\ge2\), apply 609407d6db81b18b with its rank \(r=m\), its dilation parameter \(m=T\), and its vector tilt zero. The notation map is explicit: its composition root is \((T-\sum_i j_i,j_1,\ldots,j_m)\), and its reflected count equals
\(K_{\mathbf j}=|\{\mathbf x\in\Delta_{T,m}:2\mathbf j-\mathbf x\in\Delta_{T,m}\}|\).
With \(\mathsf H_{\mathbf j}=K_{\mathbf j}/F_m(T)\), the accepted conclusion gives
\(\mathbb E_{u_{T,m}}\mathsf H^2\ge g^m4^{-m}\).
Every actual closed cap containing \(\mathbf j\) contains at least one endpoint of each reflected pair about \(\mathbf j\), as well as the root. Consequently \(\tau_{u_{T,m}}(\mathbf j)\ge\mathsf H_{\mathbf j}/2\). Jensen's inequality gives
\[
M_3(u_{T,m})
\ge\frac18\mathbb E\mathsf H^3
\ge\frac18(\mathbb E\mathsf H^2)^{3/2}
\ge\frac18g_0^m8^{-m}.
\tag{11}
\]
For \(T=0\) the factor is a singleton of depth one, and (11) follows. For \(T=1\), its \(m+1\) simplex vertices each have depth \(1/(m+1)\), so \(M_3=(m+1)^{-3}\). The inequality \((m+1)^3\le2\cdot4^m\) holds at \(m=1\) and is preserved by induction because \(((m+2)/(m+1))^3\le27/8<4\). Together with \(g_0\le2\), it proves (11) also for \(T=1\).

The uniform law \(u_E\) satisfies midpoint dominance. Apply 01a4100542206b94 with its ambient dimension \(N=2\) and its moment exponent \(q=3\). Its allowance for lower-dimensional complete supports applies here. The accepted conclusion is \(M_3(u_E)\ge\frac14\,8^{-2}\).

For an actual closed halfspace through a product root \((\mathbf j,\mathbf y)\), write its inequality as
\(\boldsymbol\alpha\cdot(\mathbf X-\mathbf j)+\boldsymbol\beta\cdot(\mathbf Y-\mathbf y)\ge0\).
The events that the two individual terms are nonnegative have intersection contained in this halfspace. Their probabilities are at least their respective component depths, and they are independent under \(U\). If one coefficient block vanishes, its event has probability one. Any containing halfspace can first have its boundary moved to the root without increasing its mass. Thus the actual product depth is at least the product of component depths, and
\[
M_3(U)\ge M_3(u_{T,m})M_3(u_E)
\ge\frac{g_0^m}{32}\,8^{-(m+2)}.
\tag{12}
\]
Pointwise domination gives \(\tau_p(\mathbf z)\ge\eta_{q_0,q_1}\tau_U(\mathbf z)\) at every product root. Keeping its original root weight \(p(\mathbf z)\ge\eta_{q_0,q_1}U(\mathbf z)\), and retaining all other original roots as nonnegative contributions, gives
\[
M_3(p)\ge\eta_{q_0,q_1}^{\,4}M_3(U)
\ge\frac{\eta_{q_0,q_1}^{\,4}g_0^m}{32}\,8^{-(m+2)}.
\tag{13}
\]
This proves the band comparison for all tilts, without assuming the coefficient bound outside (1). Inserting (1) gives the first inequality of (2). Finally, apply \(e^z\ge z\) to \(z=(m+1)\log g_0/8\) and raise to the eighth power. This yields
\(g_0^m/(m+1)^8\ge g_0^{-1}(\log g_0/8)^8\), proving the second inequality of (2).

It remains to prove the exact obstruction (4). Here use \(h_1=a=6r\), \(h_2=b=6r+1\), \(L=Q=18r^2\), and \(K=3r\), so \(Q=aK\). For a heavy pair with total degree \(d=y_1+y_2\), its normal height is \(q=ad+y_2\). If \(d\ge K+1\), its height exceeds \(Q\). If \(d=K\), the only pair with height at most \(Q\) has \(y_2=0\), and it has height exactly \(Q\). If \(d\le K-2\), then
\(q\le a(K-2)+(K-2)=Q-9r-2<Q-4r\).
Thus both top caps in (4) can contain only the top pair and pairs of degree \(K-1\). For degree \(K-1\), write \(0\le y_2\le3r-1\); the height is \(Q-6r+y_2\), with residual gap \(6r-y_2\in[3r+1,6r]\). None lies in the width-\(2r\) cap. Exactly those with \(2r\le y_2\le3r-1\) lie in the width-\(4r\) cap, and there are \(r\) such pairs. This proves (4). The weights are coprime and unequal, and \(Q=18r^2<ab=36r^2+6r\), as claimed.

The first nontrivial heavy cluster in this family is the complete occupied strip with normal heights in \([Q-6r,Q-3r-1]\), whereas the exposed slice is the singleton at \(Q\); the interval between them is empty. A next geometry to test for \(\lambda>H_0\) is a separate exposed slice and first occupied strip after a gap, each measured at its own scale. Replacing this geometry by a uniform doubling bound centered at \(Q\) is invalid. Neither (3) nor (4) decides the polynomial coefficient question for \(\lambda>H_0\).

## External sources

None.
