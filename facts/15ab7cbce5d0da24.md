---
fact_id: 15ab7cbce5d0da24
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: intake10-centroid-directional-count
depends_on: []
verifier_run: 962da5777b624c57
target_match: null
---

## Statement

Let \(n\geq1\), let \(A\subset\mathbb Z^n\) be finite and full-dimensional, and suppose

\[
\sum_{\mathbf a\in A}\mathbf a=\mathbf0.
\]

Put \(M=|A|\), \(P=\operatorname{conv}A\), and

\[
B_n=\binom{2n+1}{n}.
\]

For a nonzero real linear functional \(\beta\) on \(\mathbb R^n\), define the selected closed-side interior set and its cardinality by

\[
I_\beta=\operatorname{int}P\cap\mathbb Z^n\cap\{\beta\geq0\},
\qquad
k_\beta=|I_\beta|,
\]

and put

\[
q_\beta=2^{\lceil\log_2 k_\beta\rceil}.
\]

Then \(k_\beta\geq1\). First, there is a full-rank sublattice \(\Gamma\subseteq\mathbb Z^n\), whose quotient is cyclic of power-of-two order \(s=[\mathbb Z^n:\Gamma]\), such that

\[
s\leq q_\beta,
\qquad
\operatorname{int}P\cap\Gamma\cap\{\beta\geq0\}=\{\mathbf0\}.
\tag{1}
\]

Second, more generally, every finite-index sublattice \(\Gamma\subseteq\mathbb Z^n\) of index \(s\) satisfying the exclusion in (1) obeys

\[
M\leq sB_n.
\tag{2}
\]

Consequently,

\[
M\leq q_\beta B_n<2k_\beta B_n.
\tag{3}
\]

No completeness assumption \(A=P\cap\mathbb Z^n\) is needed for (1)--(3).

In particular, let \(P\subset\mathbb R^n\) be a full-dimensional lattice polytope, let \(D=P\cap\mathbb Z^n\), and suppose the arithmetic centroid

\[
\mathbf j=\frac1{|D|}\sum_{\mathbf x\in D}\mathbf x
\]

belongs to \(\mathbb Z^n\). For the uniform probability law \(p_{\mathbf x}=1/|D|\) on \(D\), define

\[
\tau_p(\mathbf j)
=
\inf\left\{
\sum_{\mathbf x\in D\cap H}p_{\mathbf x}:
H\subseteq\mathbb R^n\text{ is a closed halfspace and }\mathbf j\in H
\right\}.
\]

Then

\[
\tau_p(\mathbf j)\geq\frac1{2B_n}
=\frac1{2\binom{2n+1}{n}}.
\tag{4}
\]

The halfspaces and the sets \(\{\beta\geq0\}\) are closed, so every lattice point on their boundary is included. Assertion (1) concerns only the chosen side \(\{\beta\geq0\}\). Applying the theorem to \(-\beta\) gives a separate conclusion for the opposite side, potentially with a different sublattice; no single two-sided exclusion is asserted.

## Proof

First observe that \(\mathbf0\in\operatorname{int}P\). Indeed, zero is the average of all points of \(A\), with every coefficient equal to \(1/M>0\). If zero lay on the boundary of the full-dimensional polytope \(P\), there would be a nonzero supporting linear functional \(\lambda\) with \(\lambda(\mathbf a)\geq0\) for every \(\mathbf a\in A\). The equality \(\sum_{\mathbf a\in A}\lambda(\mathbf a)=0\) would force \(\lambda\) to vanish on all of \(A\), contradicting full dimensionality. Thus zero is an interior lattice point and belongs to \(I_\beta\), proving \(k_\beta\geq1\).

We prove the ray sieve. Every nonzero lattice point has a unique expression \(m\mathbf u\), where \(m\in\mathbb Z_{>0}\) and \(\mathbf u\in\mathbb Z^n\) is primitive and oriented toward that point. On every such oriented ray meeting \(I_\beta\setminus\{\mathbf0\}\), the points of that set are exactly

\[
\mathbf u,2\mathbf u,\ldots,L_{\mathbf u}\mathbf u
\tag{5}
\]

for some positive integer \(L_{\mathbf u}\). To justify the initial-segment assertion, if \(m\mathbf u\in\operatorname{int}P\), then every point of the segment from the interior point zero to the interior point \(m\mathbf u\) is in \(\operatorname{int}P\); the integer multiples \(r\mathbf u\), \(1\leq r\leq m\), also remain in \(\{\beta\geq0\}\). Convexity of the line section and boundedness of \(P\) give (5). These ray segments partition \(I_\beta\setminus\{\mathbf0\}\), so

\[
\sum_{\mathbf u}L_{\mathbf u}=k_\beta-1.
\tag{6}
\]

If \(k_\beta=1\), take \(\Gamma=\mathbb Z^n\). Then \(s=q_\beta=1\) and (1) holds. Assume now that \(k_\beta\geq2\), abbreviate \(q=q_\beta\), and choose \(\mathbf c\) uniformly in \((\mathbb Z/q\mathbb Z)^n\). For every primitive \(\mathbf u\), at least one coordinate of \(\mathbf u\) is odd. Since \(q\) is a power of two, that coordinate is invertible modulo \(q\), and hence \(\mathbf c\mathbin\cdot\mathbf u\) is uniform in \(\mathbb Z/q\mathbb Z\).

The segment (5) meets the kernel of \(\mathbf x\mapsto\mathbf c\mathbin\cdot\mathbf x\pmod q\) exactly when the additive order of \(\mathbf c\mathbin\cdot\mathbf u\) is at most \(L_{\mathbf u}\). Every additive order in \(\mathbb Z/q\mathbb Z\) is a power of two. Since \(L_{\mathbf u}\leq k_\beta-1<q\), put \(r_{\mathbf u}=2^{\lfloor\log_2L_{\mathbf u}\rfloor}\). The elements of additive order at most \(L_{\mathbf u}\) are exactly the kernel of multiplication by \(r_{\mathbf u}\), which has \(r_{\mathbf u}\) elements. Therefore

\[
\mathbb P\left(
\{\mathbf u,\ldots,L_{\mathbf u}\mathbf u\}
\text{ meets the kernel}
\right)
=\frac{r_{\mathbf u}}q
\leq\frac{L_{\mathbf u}}q.
\tag{7}
\]

By (6), the union bound over all occupied rays is at most \((k_\beta-1)/q<1\). Some \(\mathbf c\) therefore avoids every nonzero point of \(I_\beta\). For that choice set

\[
\Gamma=\{\mathbf x\in\mathbb Z^n:
\mathbf c\mathbin\cdot\mathbf x=0\pmod q\}.
\tag{8}
\]

This is a full-rank sublattice. Its quotient is the image of the displayed homomorphism, hence is cyclic, and its index \(s\) divides \(q\). Thus \(s\leq q\), and the choice of \(\mathbf c\) gives exactly (1). Points with \(\beta=0\) were included in the ray census and hence in the exclusion.

It remains to prove the polynomial bound (2). Fix any finite-index \(\Gamma\) of index \(s\) satisfying (1). Let \(\ell>M\) be a prime not dividing \(s\), let \(K=\overline{\mathbb F}_\ell\), and write

\[
R=K[z_1^{\pm1},\ldots,z_n^{\pm1}],
\qquad
V=\operatorname{span}_K\{\mathbf z^{\mathbf a}:\mathbf a\in A\}.
\]

The Laurent monomials are linearly independent, so \(\dim_KV=M\). Let \(\Omega\) be the set of characters of \(\mathbb Z^n/\Gamma\) with values in \(K^\times\). Because \(K\) is algebraically closed and \(\ell\nmid s\), there are exactly \(s\) such characters. Regard each \(\chi\in\Omega\) as the torus point with coordinates \(\chi(\mathbf e_i)\), and let \(\mathfrak m_\chi\) be its maximal ideal in \(R\).

For \(j\geq0\), set

\[
V_j=V\cap\bigcap_{\chi\in\Omega}\mathfrak m_\chi^j.
\tag{9}
\]

At one torus point, the quotient by \(\mathfrak m_\chi^j\) has a basis consisting of the monomials of total degree below \(j\) in the local parameters \(z_i-\chi(\mathbf e_i)\). For \(j\geq1\), its dimension is \(\binom{n+j-1}{n}\). Applying all \(s\) jet maps to \(V\) therefore gives

\[
\dim_KV_j
\geq
\left(M-s\binom{n+j-1}{n}\right)_+.
\tag{10}
\]

The filtration is eventually zero. Indeed, after multiplication by one fixed Laurent monomial, every element of \(V\) becomes a polynomial of some common bounded total degree, and multiplication by that Laurent monomial is a unit at every torus point. A nonzero polynomial of bounded total degree cannot have arbitrarily high order at a torus point.

For nonzero \(f\in V\), define

\[
\nu(f)=\min_{\chi\in\Omega}\max\{j:f\in\mathfrak m_\chi^j\}.
\]

Choose a basis \(f_1,\ldots,f_M\) adapted to the finite descending filtration (9): for every \(j\), the basis vectors with \(\nu(f_i)\geq j\) form a basis of \(V_j\). Hence

\[
\sum_{i=1}^M\nu(f_i)
=\sum_{j\geq1}\dim_KV_j
\geq
L_s(M),
\qquad
L_s(M):=
\sum_{j\geq1}\left(M-s\binom{n+j-1}{n}\right)_+.
\tag{11}
\]

We now make the basis directional. Choose a real linear functional \(\xi\), injective on \(A\), such that

\[
\beta(\mathbf a)<\beta(\mathbf b)
\quad\Longrightarrow\quad
\xi(\mathbf a)<\xi(\mathbf b)
\qquad(\mathbf a,\mathbf b\in A).
\tag{12}
\]

Such a functional is obtained by adding a sufficiently small generic linear perturbation to \(\beta\). Call the least-\(\xi\) exponent in the support of a nonzero element of \(V\) its pivot.

The adapted basis can be changed so that its pivots are distinct while every \(\nu(f_i)\) stays unchanged. If two basis vectors \(f,g\) share a pivot and \(\nu(f)\leq\nu(g)\), subtract the appropriate multiple of \(g\) from \(f\) to cancel that pivot. The replacement remains in \(V_{\nu(f)}\). It cannot enter \(V_{\nu(f)+1}\): the unchanged basis vectors whose levels are at least \(\nu(f)+1\) already span that space, whereas the replacement remains independent of all unchanged basis vectors. Thus its level is still \(\nu(f)\), and its pivot moves strictly later in the finite \(\xi\)-order. The replacement preserves adaptation at every filtration level. Repetition terminates because the sum of the pivot positions strictly increases and is bounded. There are \(M\) distinct pivots in the \(M\)-element set \(A\), so the pivots exhaust \(A\).

Using this basis, define

\[
F=\prod_{i=1}^M f_i\in R.
\tag{13}
\]

The product of the pivot monomials has exponent

\[
\sum_{\mathbf a\in A}\mathbf a=\mathbf0.
\]

Every other selection of one monomial from each factor has strictly larger total \(\xi\)-value, since every selected exponent is no earlier than its factor's pivot and at least one is later. Therefore the constant coefficient of \(F\) is the nonzero product of the pivot coefficients, and every nonconstant exponent in \(\operatorname{supp}F\) has strictly positive \(\xi\)-value.

The ordering (12) supplies the one-sided conclusion. If \(\mathbf a_i\) is any exponent selected from \(f_i\) and \(\mathbf p_i\) is its pivot, minimality of the pivot and (12) imply \(\beta(\mathbf a_i)\geq\beta(\mathbf p_i)\). Hence every exponent \(\sum_i\mathbf a_i\) occurring in the product satisfies

\[
\beta\left(\sum_i\mathbf a_i\right)
\geq
\beta\left(\sum_i\mathbf p_i\right)
=0.
\]

It is also a sum of \(M\) points of \(A\), so

\[
\operatorname{supp}F\subseteq MP\cap\{\beta\geq0\}.
\tag{14}
\]

This includes selections lying on \(\{\beta=0\}\); the generic tie-breaker \(\xi\) establishes uniqueness of the constant contribution without discarding those boundary selections.

For every \(\chi\in\Omega\), each \(f_i\) lies in \(\mathfrak m_\chi^{\nu(f_i)}\). Thus (11) gives

\[
F\in\mathfrak m_\chi^{L_s(M)}
\qquad(\chi\in\Omega).
\tag{15}
\]

Set

\[
t=\left\lfloor\frac{\ell-1}{M}\right\rfloor.
\]

Because \(\ell>M\), one has \(t\geq1\) and \(tM<\ell\). By (14),

\[
\operatorname{supp}F^t\subseteq tMP\cap\{\beta\geq0\}.
\tag{16}
\]

The constant coefficient of \(F^t\) is nonzero: every nonconstant exponent of \(F\) has positive \(\xi\)-value, so the only way to obtain exponent zero in \(F^t\) is to choose the constant term from every factor.

Suppose an exponent in (16) equals \(\ell\boldsymbol\gamma\) for some \(\boldsymbol\gamma\in\Gamma\). Then

\[
\boldsymbol\gamma\in\frac{tM}{\ell}P,
\qquad
\beta(\boldsymbol\gamma)\geq0.
\]

Since \(0\leq tM/\ell<1\) and zero is an interior point of \(P\), the strict contraction \((tM/\ell)P\) is contained in \(\operatorname{int}P\). The exclusion (1) therefore forces \(\boldsymbol\gamma=\mathbf0\). Consequently, under the natural quotient map

\[
\pi_\ell:R\longrightarrow K[\mathbb Z^n/(\ell\Gamma)],
\tag{17}
\]

the identity-class coefficient of \(\pi_\ell(F^t)\) is exactly the nonzero constant coefficient of \(F^t\). In particular,

\[
\pi_\ell(F^t)\neq0.
\tag{18}
\]

We compare (18) with nilpotence. The exact sequence

\[
0\longrightarrow\Gamma/(\ell\Gamma)
\longrightarrow\mathbb Z^n/(\ell\Gamma)
\longrightarrow\mathbb Z^n/\Gamma
\longrightarrow0
\]

has an elementary abelian \(\ell\)-group of rank \(n\) on the left and a group of order \(s\), prime to \(\ell\), on the right. Primary decomposition of the finite abelian middle group gives a direct product of \(\Gamma/(\ell\Gamma)\cong(\mathbb Z/\ell\mathbb Z)^n\) and a complementary group of order \(s\). Over the algebraically closed field \(K\), the group algebra of that complementary group splits into its \(s\) character factors. In characteristic \(\ell\), if \(u_i\) denotes a generator minus one in the \(i\)-th cyclic \(\ell\)-factor, then \((1+u_i)^\ell-1=u_i^\ell\). Therefore

\[
K[\mathbb Z^n/(\ell\Gamma)]
\cong
\prod_{\chi\in\Omega}
K[u_1,\ldots,u_n]/(u_1^\ell,\ldots,u_n^\ell).
\tag{19}
\]

In the factor indexed by \(\chi\), reduction modulo the maximal ideal \((u_1,\ldots,u_n)\) evaluates a Laurent polynomial at the torus point \(\chi\). Hence (15) implies that the image of \(F^t\) in this factor belongs to

\[
(u_1,\ldots,u_n)^{tL_s(M)}.
\tag{20}
\]

The largest possible total degree of a nonzero monomial in a factor of (19) is \(n(\ell-1)\). Equivalently,

\[
(u_1,\ldots,u_n)^{n(\ell-1)+1}=0.
\]

If \(tL_s(M)>n(\ell-1)\), (20) would vanish in every factor, contradicting (18). Thus

\[
tL_s(M)\leq n(\ell-1).
\tag{21}
\]

There are arbitrarily large primes not dividing the fixed integer \(s\). For those primes,

\[
\frac{t}{\ell-1}
=
\frac1{\ell-1}\left\lfloor\frac{\ell-1}{M}\right\rfloor
\longrightarrow\frac1M.
\]

Taking the limit in (21) gives

\[
L_s(M)\leq nM.
\tag{22}
\]

On the other hand, retaining the first \(n+1\) summands in (11), and using \((x)_+\geq x\), yields

\[
\begin{aligned}
L_s(M)
&\geq
\sum_{j=1}^{n+1}
\left(M-s\binom{n+j-1}{n}\right)\\
&=(n+1)M-s\sum_{j=1}^{n+1}\binom{n+j-1}{n}\\
&=(n+1)M-s\binom{2n+1}{n}.
\end{aligned}
\tag{23}
\]

Combining (22) and (23) proves \(M\leq sB_n\), which is (2). For the sieve lattice, \(s\leq q_\beta\), and the definition of the least power of two at least \(k_\beta\) gives \(q_\beta<2k_\beta\), including \(k_\beta=1\). This proves (3). Notice that \(M\leq q_\beta B_n\) is non-strict, while the final comparison with \(2k_\beta B_n\) is strict; no equality case is lost when \(k_\beta\) itself is a power of two, because then \(q_\beta=k_\beta<2k_\beta\). The case \(s=1\) is also covered by (19), where \(\Omega\) has one element and there is one local factor.

We now prove the depth consequence. Translate the complete lattice set by its integral arithmetic centroid:

\[
A=D-\mathbf j,
\qquad
P'=P-\mathbf j.
\]

Then \(A\subset\mathbb Z^n\), \(\sum_{\mathbf a\in A}\mathbf a=0\), and \(A=P'\cap\mathbb Z^n\). Let a nontrivial closed halfspace through \(\mathbf j\) be written as

\[
H_0=\{\mathbf x:\beta(\mathbf x-\mathbf j)\geq0\}
\]

for a nonzero \(\beta\). Completeness ensures that every point counted by \(k_\beta\) is a point of \(A\), so (3) gives

\[
|D\cap H_0|\geq k_\beta>
\frac{|D|}{2B_n}.
\tag{24}
\]

If \(H\) is any nontrivial closed halfspace containing \(\mathbf j\), write it in the same orientation as

\[
H=\{\mathbf x:\beta(\mathbf x-\mathbf j)\geq c\}
\]

with \(c\leq0\). Then the parallel halfspace \(H_0=\{\beta(\mathbf x-\mathbf j)\geq0\}\) is contained in \(H\), so (24) also bounds \(|D\cap H|\). If the whole space is allowed as a degenerate halfspace, its mass is one and the conclusion is immediate. Dividing by \(|D|\) proves (4). Points on either boundary are retained because every inequality is non-strict. The strict inequality in (24) safely implies the stated non-strict bound (4).

Finally, Stirling's formula gives

\[
B_n
=\frac{2n+1}{n+1}\binom{2n}{n}
\sim\frac{2\,4^n}{\sqrt{\pi n}},
\qquad
\frac1{2B_n}
\sim\frac{\sqrt{\pi n}}{4\,4^n}.
\tag{25}
\]

Thus (4) has order \(\sqrt n\,4^{-n}\), and its ratio to \(2^{-n}\) tends to zero. The limitation is structural for an argument that counts only interior lattice points. For the complete centrally symmetric lattice set

\[
D=\{-1,0,1\}^n=[-1,1]^n\cap\mathbb Z^n,
\]

the arithmetic centroid is zero and

\[
\operatorname{int}([-1,1]^n)\cap\mathbb Z^n=\{\mathbf0\}.
\]

Hence \(k_\beta=1\) for every nonzero \(\beta\), while \(|D|=3^n\). No bound of the form \(|D|\leq C2^nk_\beta\) can hold with an absolute \(C\). This example does not disprove a \(2^{-n}\) depth bound, because such a bound may use the many lattice points on the boundary of \(P\). It shows exactly why improving only the present interior-point count cannot supply that scale. The proof above also never claims that \(tMP\) itself avoids nonzero points of \(\ell\Gamma\) on the opposite side; it uses only the directional support inclusion (14). Therefore neither a simultaneous two-sided sieve/count nor the broader centroid theorem follows from this packet.

## External sources

None. Every lattice sieve, filtration, pivot, group-algebra, nilpotence, and depth step used above is proved in the packet; the elementary Stirling asymptotic in (25) is used only to describe the scale of the exact bound (4).
