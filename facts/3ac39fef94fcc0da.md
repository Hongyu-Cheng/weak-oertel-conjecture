---
fact_id: 3ac39fef94fcc0da
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: parity-midpoint-domination
depends_on: []
verifier_run: c53df4e747c1410c
target_match: null
---

## Statement

Let \(n,d\in\mathbb Z_{>0}\), let
\[
E:=\mathbb R^{n+d},\qquad
\Lambda:=\mathbb Z^n\times\mathbb R^d,
\]
and let \(C\subseteq E\) be a convex body.  Write
\[
T(p,q):=\frac{p+q}{2}.
\]

First let \(\rho\) be a nonzero positive finite Borel measure carried by
\(S:=C\cap\Lambda\).  For each parity class
\(r\in(\mathbb Z/2\mathbb Z)^n\), let \(\rho_r\) be the restriction of
\(\rho\) to points whose first \(n\) coordinates have parity \(r\), and put
\(m_r:=|\rho_r|\).  Define
\[
\nu_r:=
\begin{cases}
\dfrac{1}{2m_r}\,T_\#(\rho_r\otimes\rho_r),&m_r>0,\\[6pt]
0,&m_r=0,
\end{cases}
\qquad
\nu:=\sum_r\nu_r.
\]
Then:

1. \(|\nu|=|\rho|/2\), and \(\nu\) is carried by \(S\).
2. For every closed halfspace \(H\subseteq E\),
   \[
   \nu(H)\leq\rho(H).
   \]
3. The normalized barycenters of \(\nu\) and \(\rho\) coincide:
   \[
   \frac1{|\nu|}\int_E y\,d\nu(y)
   =
   \frac1{|\rho|}\int_E y\,d\rho(y).
   \]

Second, let \(\mu\) be the unnormalized mixed-volume measure of \(C\).  Thus,
for
\[
C_z:=\{x\in\mathbb R^d:(z,x)\in C\},
\]
let
\[
\mu_z(A):=\operatorname{vol}_d\{x\in C_z:(z,x)\in A\},
\qquad
\mu:=\sum_{z\in\mathbb Z^n}\mu_z,
\]
and write
\[
w_z:=|\mu_z|,\qquad
W:=|\mu|=\sum_z w_z>0,\qquad
M:=\max_z w_z.
\]
For a parity class \(r\), put
\[
W_r:=\sum_{z\equiv r\pmod 2}w_z.
\]
Define the unnormalized ordered off-diagonal same-parity midpoint measure
\[
\eta^\circ
:=
\sum_{r\in(\mathbb Z/2\mathbb Z)^n}
\ \sum_{\substack{z,z'\equiv r\pmod 2\\z\ne z'}}
T_\#(\mu_z\otimes\mu_{z'}).
\]
Both \((z,z')\) and \((z',z)\) occur in this sum.  Then
\(\eta^\circ\) is carried by \(S\), its total mass is exactly
\[
Q^\circ:=|\eta^\circ|
=
\sum_rW_r^2-\sum_z w_z^2,
\]
and
\[
Q^\circ
\geq
2^{-n}W^2-MW.
\]
Moreover, every closed halfspace \(H\subseteq E\) satisfies
\[
\eta^\circ(H)\leq2W\mu(H).
\]

Let \(\delta:=2^{-n}\).  The preceding statements give the following exact
heavy/non-heavy alternatives.

1. If \(M\geq\delta W/2\), there is \(p_\ast\in S\) such that every closed
   halfspace \(H\ni p_\ast\) satisfies
   \[
   \mu(H)\geq\frac{1}{2e}\,\delta W.
   \]
2. If \(M<\delta W/2\), \(\kappa>0\), and \(p\in S\) satisfies
   \[
   \eta^\circ(H)\geq\kappa Q^\circ
   \quad\text{for every closed halfspace }H\ni p,
   \]
   then every such \(H\) satisfies
   \[
   \mu(H)\geq\frac{\kappa}{4}\,\delta W.
   \]

No assertion is made that \(\nu\) or \(\eta^\circ\) has an
absolute-constant-depth point.

## Proof

Because \(C\) is compact, only finitely many integer fibers of \(C\) are
nonempty.  In particular, all sums below are finite, and every measure in the
statement has a finite first moment.

Fix a parity class \(r\) with \(m_r>0\).  The product measure
\(\rho_r\otimes\rho_r\) has mass \(m_r^2\), so
\[
|\nu_r|=\frac{m_r^2}{2m_r}=\frac{m_r}{2}.
\]
The same identity is true with both sides zero when \(m_r=0\).  Summing over
all parity classes gives \(|\nu|=|\rho|/2\).

For \((p,q)\) in the support of
\(\rho_r\otimes\rho_r\), write
\[
p=(z,x),\qquad q=(z',x').
\]
The two base points have the same parity, so
\((z+z')/2\in\mathbb Z^n\).  Convexity of \(C\) gives
\((p+q)/2\in C\).  Thus every \(\nu_r\), including the zero measure for an
empty parity class, is carried by \(S\), and hence so is \(\nu\).

Let \(H\) be a closed halfspace.  For a proper halfspace, choose an affine
functional \(\ell\) such that \(H=\{y:\ell(y)\geq0\}\).  Affineness gives
\[
\ell(T(p,q))=\frac{\ell(p)+\ell(q)}2.
\]
Consequently, if \(T(p,q)\in H\), then at least one of \(p,q\) belongs to
\(H\).  This includes the boundary case \(\ell(T(p,q))=0\), and yields
\[
\mathbf 1_H(T(p,q))
\leq
\mathbf 1_H(p)+\mathbf 1_H(q).
\]
Integrating against the ordered product measure gives
\[
\begin{aligned}
\nu_r(H)
&\leq
\frac1{2m_r}
\left(
m_r\rho_r(H)+m_r\rho_r(H)
\right)\\
&=\rho_r(H).
\end{aligned}
\]
The assertion is trivial for \(m_r=0\), and summing over \(r\) proves
\(\nu(H)\leq\rho(H)\).  Degenerate halfspaces, if allowed, are immediate.

The first moment of \(\nu_r\) is
\[
\begin{aligned}
\int_E y\,d\nu_r(y)
&=
\frac1{2m_r}
\int_E\int_E\frac{p+q}{2}\,d\rho_r(p)\,d\rho_r(q)\\
&=\frac12\int_E p\,d\rho_r(p).
\end{aligned}
\]
This again holds trivially when \(m_r=0\).  Hence
\[
\int_E y\,d\nu(y)=\frac12\int_E y\,d\rho(y).
\]
Together with \(|\nu|=|\rho|/2\), this proves equality of the normalized
barycenters.

We now turn to \(\eta^\circ\).  Its definition uses ordered pairs of distinct
base fibers within each parity class.  Every midpoint in its construction
belongs to \(C\) by convexity and has integer base coordinate by the parity
condition, so \(\eta^\circ\) is carried by \(S\).  Its total mass is
\[
\begin{aligned}
|\eta^\circ|
&=
\sum_r
\sum_{\substack{z,z'\equiv r\pmod2\\z\ne z'}}
w_zw_{z'}\\
&=
\sum_r\left(\sum_{z\equiv r\pmod2}w_z\right)^2
-\sum_z w_z^2\\
&=
\sum_rW_r^2-\sum_z w_z^2.
\end{aligned}
\]
There are exactly \(2^n\) parity classes, including those with zero mass.
Cauchy-Schwarz and the definition of \(M\) give
\[
\sum_rW_r^2\geq2^{-n}\left(\sum_rW_r\right)^2=2^{-n}W^2
\]
and
\[
\sum_z w_z^2\leq M\sum_z w_z=MW.
\]
Subtracting proves
\[
Q^\circ\geq2^{-n}W^2-MW.
\]

For a closed halfspace \(H\), the same endpoint indicator inequality used
above gives, for each ordered pair \(z\ne z'\) in one parity class,
\[
T_\#(\mu_z\otimes\mu_{z'})(H)
\leq
w_{z'}\mu_z(H)+w_z\mu_{z'}(H).
\]
Let
\[
\mu_r(H):=\sum_{z\equiv r\pmod2}\mu_z(H).
\]
Summing the last inequality over all ordered off-diagonal pairs gives
\[
\begin{aligned}
\eta^\circ(H)
&\leq
2\sum_r\sum_{z\equiv r\pmod2}
(W_r-w_z)\mu_z(H)\\
&\leq
2\sum_rW_r\mu_r(H)\\
&\leq
2W\sum_r\mu_r(H)
=2W\mu(H).
\end{aligned}
\]
This proves the transfer inequality, with the diagonal removal visible in the
factor \(W_r-w_z\).

It remains to verify the alternatives.  Suppose first that
\(M\geq\delta W/2\), and choose \(z_\ast\) with \(w_{z_\ast}=M\).  Since
\(W>0\), the fiber \(C_{z_\ast}\) has positive \(d\)-volume and is a
\(d\)-dimensional convex body.  Let \(c_\ast\) be its centroid and set
\(p_\ast:=(z_\ast,c_\ast)\in S\).

Let \(H\ni p_\ast\) be a closed halfspace.  If its continuous normal is zero,
then it contains the entire fiber \(\{z_\ast\}\times C_{z_\ast}\), so
\(\mu(H)\geq M\).  Otherwise, its restriction to that fiber is a closed
halfspace in \(\mathbb R^d\) containing \(c_\ast\).  Grünbaum's centroid
halfspace theorem gives
\[
\mu(H)\geq
\left(\frac d{d+1}\right)^dM
\geq\frac{M}{e}
\geq\frac{1}{2e}\,\delta W.
\]
Here \((d/(d+1))^d\geq e^{-1}\) follows from
\((1+1/d)^d\leq e\).  This proves the heavy-fiber alternative.

Finally suppose \(M<\delta W/2\).  The collision estimate yields
\[
Q^\circ
\geq\delta W^2-MW
>\frac{\delta W^2}{2}.
\]
If \(p\in S\) is \(\kappa\)-deep for \(\eta^\circ\), then for every closed
halfspace \(H\ni p\),
\[
2W\mu(H)
\geq\eta^\circ(H)
\geq\kappa Q^\circ
>\frac{\kappa\delta W^2}{2}.
\]
Therefore
\[
\mu(H)>\frac{\kappa}{4}\delta W,
\]
which in particular implies the asserted non-strict lower bound.  This proves
the non-heavy conditional and completes the theorem.

## External sources

Branko Grünbaum, "Partitions of Mass-Distributions and of Convex Bodies by Hyperplanes," Pacific Journal of Mathematics 10(4) (1960), 1257-1261, Theorem 2 and its proof in Section 3, pp. 1259-1260, https://doi.org/10.2140/pjm.1960.10.1257, primary-source PDF https://msp.org/pjm/1960/10-4/pjm-v10-n4-p18-p.pdf.  Exact form used: if \(K\subseteq\mathbb R^d\) is a convex body with centroid \(c(K)\), then every closed halfspace \(J\subseteq\mathbb R^d\) containing \(c(K)\) satisfies \(\operatorname{vol}_d(K\cap J)\geq(d/(d+1))^d\operatorname{vol}_d(K)\).  Applicability: in the heavy-fiber case, \(w_{z_\ast}>0\) makes \(C_{z_\ast}\) a \(d\)-dimensional convex body, \(c_\ast\) is its centroid, and the restriction of every ambient halfspace with nonzero continuous normal and containing \((z_\ast,c_\ast)\) is a closed halfspace containing \(c_\ast\).
