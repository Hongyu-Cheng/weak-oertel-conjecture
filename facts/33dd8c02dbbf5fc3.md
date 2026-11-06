---
fact_id: 33dd8c02dbbf5fc3
kind: lemma
author: "research-agent"
assurance: LLM-verified
subgoal_id: approximate-balance-slab-dichotomy
depends_on: ["14f69b717e62350c","314b32bda8a0b01e","64b4d5b346f969ac","981a6c3aa5982216"]
verifier_run: 43fbaccc8d6d4dfa
target_match: null
---

## Statement

Let \(n,d\in\mathbb Z_{>0}\), let \(C\subseteq\mathbb R^{n+d}\) be a convex body, and set
\[
S:=C\cap(\mathbb Z^n\times\mathbb R^d).
\]
For \(z\in\mathbb Z^n\), write
\[
C_z:=\{x\in\mathbb R^d:(z,x)\in C\},\qquad
w_z:=\mathcal H_d(C_z),\qquad
W:=\sum_{z\in\mathbb Z^n}w_z,
\]
and assume \(W>0\). Let \(z_0\) and \(y_0\in\operatorname{int}C_{z_0}\) be the weighted lattice centerpoint and fiberwise depth maximizer supplied by accepted fact `981a6c3aa5982216`, and put
\[
t:=h_S((z_0,y_0)),\qquad
R:=\max\{\|x-y_0\|_2:(z,x)\in S\}.
\]
Thus \(R<\infty\), and every proper closed base halfspace containing \(z_0\) has fiber mass at least \(2^{-n}W\).

For every \(k\in\mathbb Z_{>0}\) and every \(\varepsilon>0\), there are \(k\) possibly repeated ordinary closed halfspaces through \((z_0,y_0)\),
\[
H_j=\{(z,x):
a_j^\top(z-z_0)+b_j^\top(x-y_0)\geq0\},
\qquad 1\leq j\leq k,
\]
whose normals \((a_j,b_j)\) are Euclidean unit vectors, such that
\[
\mu(H_j)\leq t+\varepsilon
\quad(1\leq j\leq k),
\qquad
\left\|\widehat b\right\|_2\leq k^{-1/2},
\]
where
\[
\mu(A):=\sum_{z\in\mathbb Z^n}
\mathcal H_d(\{x\in C_z:(z,x)\in A\}),\qquad
\widehat a:=\frac1k\sum_{j=1}^ka_j,\qquad
\widehat b:=\frac1k\sum_{j=1}^kb_j.
\]
With
\[
\tau:=R\|\widehat b\|_2\leq \frac{R}{\sqrt{k}},
\qquad
U:=\bigcup_{j=1}^kH_j,
\]
one has the exact shifted cover
\[
\{(z,x)\in S:\widehat a^\top(z-z_0)\geq\tau\}
\subseteq U. \tag{1}
\]
Consequently, if
\[
M_{\mathrm{slab}}
:=\sum_{\substack{z\in\mathbb Z^n\\
0\leq\widehat a^\top(z-z_0)<\tau}}w_z,
\]
then
\[
M_{\mathrm{slab}}
\geq 2^{-n}W-\mu(U)
\geq 2^{-n}W-k(t+\varepsilon). \tag{2}
\]
Equivalently, for every \(\theta\in(0,1)\), at least one of the following holds:
\[
\mu(U)\geq\theta2^{-n}W,
\qquad
t\geq\frac{\theta}{k}2^{-n}W-\varepsilon, \tag{3}
\]
or
\[
M_{\mathrm{slab}}>(1-\theta)2^{-n}W. \tag{4}
\]
In particular, if \(t<(\theta/k)2^{-n}W\), then (4) holds for every
\[
0<\varepsilon<
\frac{\theta}{k}2^{-n}W-t
\]
with a possibly \(\varepsilon\)-dependent slab of width parameter
\(\tau\leq R/\sqrt{k}\).

If \(\widehat a\neq0\), the slab in (2) has the invariant normalized description
\[
0\leq e^\top(z-z_0)<\omega,
\qquad
e:=\frac{\widehat a}{\|\widehat a\|_2},
\qquad
\omega:=\frac{R\|\widehat b\|_2}{\|\widehat a\|_2}
\leq\frac{R}{\sqrt{k}\|\widehat a\|_2}. \tag{5}
\]
No rationality of \(e\) is assumed. If \(\widehat a=0\) and
\(\widehat b\neq0\), the shifted set in (1) is empty and the slab is all
of the base support. If \(\widehat a=\widehat b=0\), (1) covers all of
\(S\), the slab is empty, and
\[
t\geq k^{-1}W-\varepsilon. \tag{6}
\]
More generally, if merely \(\widehat b=0\), (1) covers the unshifted
base halfspace through \(z_0\), so
\[
t\geq k^{-1}2^{-n}W-\varepsilon. \tag{7}
\]

For the exact phase audit, suppose \(\widehat a\neq0\), define
\[
\phi:\mathbb Z^n\longrightarrow\mathbb R,\qquad
\phi(u):=\widehat a^\top u,
\qquad
L:=\ker\phi,
\]
and put
\[
q:=\operatorname{rank}_{\mathbb Z}\phi(\mathbb Z^n)
=n-\operatorname{rank}_{\mathbb Z}L.
\]
Then \(1\leq q\leq n\), \(L\) is primitive in \(\mathbb Z^n\), and
every nonempty phase set
\[
\{z\in\mathbb Z^n:\phi(z-z_0)=s\}
\]
is the lattice point set of a primitive affine slice of codimension
\(q\). This remains true for irrational \(\widehat a\), as in the
primitive-kernel mechanism of accepted fact `14f69b717e62350c`.

Let
\[
D:=\{z\in\mathbb Z^n:w_z>0\},\qquad
\Phi:=\{\phi(z-z_0):z\in D,\ 0\leq\phi(z-z_0)<\tau\},
\qquad
N:=|\Phi|.
\]
If \(M_{\mathrm{slab}}>0\), then \(1\leq N<\infty\), the slab mass is a
sum of the masses of \(N\) primitive codimension-\(q\) phase slices,
and one of those slices has mass at least
\[
\frac{M_{\mathrm{slab}}}{N}. \tag{8}
\]
Therefore accepted fact `314b32bda8a0b01e` applies to such a phase
slice, under its stated lower-dimensional induction hypothesis, if
its actual mass is at least \(2^{-q}W\). Neither (4) nor (8) guarantees
this threshold: for every \(1\leq q\leq n\), every \(N\geq1\), and
every \(\theta\in(0,1)\),
\[
\frac{(1-\theta)2^{-n}}{N}<2^{-q}. \tag{9}
\]

Two verifiable phase-collapse conditions are available. First, define
\[
\delta_D(\widehat a):=
\min\bigl(
\{\phi(z-z_0):z\in D,\ \phi(z-z_0)>0\}
\cup\{+\infty\}
\bigr).
\]
If \(0<\tau\leq\delta_D(\widehat a)\), then the charged slab has only
the zero phase, so \(N=1\), all of its positive-mass fibers lie on the
primitive slice
\[
z_0+\operatorname{span}_{\mathbb R}L.
\tag{10}
\]
Its mass is exactly the total mass of that slice.
Second, if the full phase group is discrete,
\[
\phi(\mathbb Z^n)=\Delta\mathbb Z
\qquad(\Delta>0),
\]
then \(q=1\),
\[
N\leq\left\lceil\frac{\tau}{\Delta}\right\rceil,
\tag{11}
\]
and \(0<\tau\leq\Delta\) again forces (10). Equivalently, the discrete
phase condition says
\(\widehat a=\Delta p\) up to sign for a primitive
\(p\in\mathbb Z^n\). These conditions prove primitivity and phase
collapse, but (9) shows that an additional phase-mass estimate is
still necessary.

Accepted fact `64b4d5b346f969ac` does not supply that missing estimate:
it synchronizes rational projection obstructions for nested
continuous fiber-volume level sets under a projection-box hypothesis,
whereas the empirical slab above is defined by one sampled normal and
an arbitrary finite lattice weight profile. In particular it gives
neither a bound on \(N\) for this slab nor a \(2^{-q}W\) lower bound
for one of its phases. Thus no unconditional slab-to-rank-drop step is
asserted here.

## Proof

Fix \(k\geq1\) and \(\varepsilon>0\). Accepted fact
`981a6c3aa5982216` supplies a finite family of unit normals
\[
u_i=(a_i,b_i),\qquad 1\leq i\leq r,
\]
positive weights \(\lambda_i\) summing to one, and ordinary
boundary-through-\((z_0,y_0)\) caps of mass at most \(t+\varepsilon\),
such that
\[
\sum_{i=1}^r\lambda_i b_i=0. \tag{12}
\]
Let \(I_1,\ldots,I_k\) be independent indices with
\(\mathbb P(I_j=i)=\lambda_i\), and set
\[
B_j:=b_{I_j}.
\]
Because every ambient normal is a unit vector, \(\|B_j\|_2\leq1\).
Using (12) and independence,
\[
\begin{aligned}
\mathbb E\left\|
\frac1k\sum_{j=1}^kB_j
\right\|_2^2
&=\frac1{k^2}\sum_{j=1}^k\mathbb E\|B_j\|_2^2
+\frac1{k^2}\sum_{j\neq\ell}
\langle\mathbb EB_j,\mathbb EB_\ell\rangle\\
&\leq\frac1k.
\end{aligned} \tag{13}
\]
Hence at least one realization satisfies
\[
\left\|\frac1k\sum_{j=1}^kB_j\right\|_2\leq k^{-1/2}. \tag{14}
\]
Choose such a realization, allowing repeated indices, and use the
corresponding \(k\) caps as \(H_1,\ldots,H_k\). Their mass bounds are
inherited from the finite family, and (14) is the claimed approximate
balance.

For any \((z,x)\in S\),
\[
\frac1k\sum_{j=1}^k
\bigl(a_j^\top(z-z_0)+b_j^\top(x-y_0)\bigr)
=
\widehat a^\top(z-z_0)+\widehat b^\top(x-y_0). \tag{15}
\]
By the definition of \(R\),
\[
\widehat b^\top(x-y_0)\geq-R\|\widehat b\|_2=-\tau. \tag{16}
\]
If \(\widehat a^\top(z-z_0)\geq\tau\), equations (15) and
(16) show that the average of the \(k\) cap functionals is
nonnegative. They therefore cannot all be strictly negative, so the
point lies in at least one closed cap \(H_j\). This proves (1).

Put
\[
M_0:=\sum_{\widehat a^\top(z-z_0)\geq0}w_z,\qquad
M_+:=\sum_{\widehat a^\top(z-z_0)\geq\tau}w_z.
\]
If \(\widehat a\neq0\), the first set is a proper closed base
halfspace through \(z_0\), so the weighted centerpoint property gives
\(M_0\geq2^{-n}W\). If \(\widehat a=0\), the first set is all of
\(\mathbb R^n\), so \(M_0=W\) and the same lower bound holds. Since
\(\tau\geq0\), the two disjoint conditions
\[
\widehat a^\top(z-z_0)\geq\tau,
\qquad
0\leq\widehat a^\top(z-z_0)<\tau
\]
partition the condition defining \(M_0\). Thus
\[
M_0=M_++M_{\mathrm{slab}}. \tag{17}
\]
The shifted cover gives \(M_+\leq\mu(U)\), while subadditivity and the
cap mass bounds give
\[
\mu(U)\leq\sum_{j=1}^k\mu(H_j)\leq k(t+\varepsilon). \tag{18}
\]
Equations (17) and (18) prove (2).

For \(\theta\in(0,1)\), if
\(\mu(U)\geq\theta2^{-n}W\), then (18) gives (3). Otherwise,
(17), \(M_+\leq\mu(U)\), and \(M_0\geq2^{-n}W\) give (4).
This proves the dichotomy and its consequence when \(t\) is below the
depth threshold. Dividing both inequalities defining the slab by
\(\|\widehat a\|_2\) proves (5). If \(\widehat a=0\), the definitions
give the two stated cases directly. If \(\widehat b=0\), then
\(\tau=0\), the slab is empty, and (1) covers the unshifted base
halfspace. Its mass is at least \(2^{-n}W\), or \(W\) when also
\(\widehat a=0\); combining this with (18) proves (6) and (7).

It remains to justify the phase audit. For nonzero \(\widehat a\), the
image \(\phi(\mathbb Z^n)\) is a nonzero finitely generated
torsion-free abelian group, hence is free of some rank
\(q\in\{1,\ldots,n\}\). The first isomorphism theorem gives
\(\operatorname{rank}L=n-q\). The kernel \(L\) is saturated: if
\(m u\in L\) for \(u\in\mathbb Z^n\) and a nonzero integer \(m\), then
\[
0=\phi(mu)=m\phi(u),
\]
so \(u\in L\). Thus \(L\) is primitive. Equivalently,
\[
\operatorname{span}_{\mathbb R}L\cap\mathbb Z^n=L, \tag{19}
\]
which is the same irrational-normal kernel argument used in accepted
fact `14f69b717e62350c`. If a phase \(s\) is attained, choose
\(u_s\in\mathbb Z^n\) with \(\phi(u_s)=s\). Its lattice points are
\[
z_0+u_s+L
=
\bigl(z_0+u_s+\operatorname{span}_{\mathbb R}L\bigr)
\cap\mathbb Z^n. \tag{20}
\]
This is a primitive affine slice of codimension \(q\), with no
rationality assumption on \(\widehat a\).

The positive-mass support \(D\) is finite because \(C\) is compact.
Partitioning the charged slab points by their values under \(\phi\)
therefore yields the finite set \(\Phi\), and (20) proves that the
slab mass is the sum of \(N\) primitive phase-slice masses. Pigeonhole
gives (8). Accepted fact `314b32bda8a0b01e` requires a codimension
\(q\) primitive slice to have mass at least \(2^{-q}W\), in addition
to its lower-dimensional induction hypothesis. Since
\[
\frac{(1-\theta)2^{-n}}{N}
\leq(1-\theta)2^{-n}
<2^{-n}
\leq2^{-q},
\]
the lower bound from (4), even with \(N=1\), cannot certify that
requirement. This proves (9) and the asserted no-go conclusion.

Because \(D\) is finite, the positive support phase gap
\(\delta_D(\widehat a)\) is well-defined. The strict upper boundary of
the slab shows that \(\tau\leq\delta_D(\widehat a)\) excludes every
positive support phase, proving (10). If
\(\phi(\mathbb Z^n)=\Delta\mathbb Z\), the phases in
\([0,\tau)\) are among
\[
0,\Delta,\ldots,
\left(\left\lceil\frac{\tau}{\Delta}\right\rceil-1\right)\Delta,
\]
which proves (11). A nonzero finitely generated subgroup of
\(\mathbb R\) is discrete exactly when it has rank one; choosing its
positive generator \(\Delta\) writes the coordinate generators of
\(\phi\) as integer multiples of \(\Delta\), with greatest common
divisor one. This is precisely
\(\widehat a=\Delta p\) up to sign for a primitive
\(p\in\mathbb Z^n\). The zero-normal case has
\(L=\mathbb Z^n\) and codimension zero, so it is not a proper
rank-drop slice.

Finally, accepted fact `64b4d5b346f969ac` concerns synchronized
rational projection obstructions for nested continuous level sets and
requires its own projection-box and level-set hypotheses. None of
those hypotheses identifies the empirical phase map \(\phi\), bounds
the number \(N\) of its charged phases, or supplies a dyadically heavy
phase. Accepted fact `14f69b717e62350c` likewise proves primitive
rank recursion only after restriction to an exact pure-base boundary
and explicitly supplies no boundary-heaviness estimate. Therefore the
only valid conversion from the present positive-width slab to accepted
fact `314b32bda8a0b01e` is the conditional one stated after (8).

## External sources

none
