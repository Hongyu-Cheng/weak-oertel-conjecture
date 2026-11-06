---
fact_id: 67ade15eb2ffc02c
kind: lemma
author: "research-agent"
assurance: LLM-verified
subgoal_id: n2-anchored-energy-capacity
depends_on: ["aca624dd8874e5a5"]
verifier_run: 761d8e9c10624c1b
target_match: null
---

## Statement

Let \(n,d\in\mathbb Z_{>0}\), let
\(C\subseteq\mathbb R^{n+d}\) be a convex body, and write
\[
C_z:=\{x\in\mathbb R^d:(z,x)\in C\},\qquad
w_z:=\operatorname{vol}_d(C_z),\qquad
W:=\sum_{z\in\mathbb Z^n}w_z>0.
\]
For \(r\in(\mathbb Z/2\mathbb Z)^n\), put
\[
W_r:=\sum_{z\equiv r\pmod2}w_z,\qquad
R_+:=\{r:W_r>0\}.
\]
Let \(\mu_z\) be \(d\)-dimensional Lebesgue measure on
\(\{z\}\times C_z\), let
\[
\mu_r:=\sum_{z\equiv r\pmod2}\mu_z,
\qquad
T(p,q):=\frac{p+q}{2},
\]
and define
\[
K_r:=\frac1{W_r}T_\#(\mu_r\otimes\mu_r)
\quad(r\in R_+),
\qquad
\mathsf A\mu:=2^{-n}\sum_{r\in R_+}K_r.
\]
For \(c\in\mathbb Z^n\), define the base-fiber marginal
\[
\kappa_c:=(\mathsf A\mu)(\{c\}\times\mathbb R^d).
\]
For a closed halfspace \(Q\subseteq\mathbb R^n\), write
\[
w(Q):=\sum_{z\in Q\cap\mathbb Z^n}w_z,\qquad
\kappa(Q):=\sum_{c\in Q\cap\mathbb Z^n}\kappa_c.
\]
Then every closed halfspace \(Q\) satisfies
\[
\kappa(Q)
\geq
2^{-n}\sum_{r\in R_+}
\frac{
\left(
\sum_{\substack{z\in Q\cap\mathbb Z^n\\z\equiv r\pmod2}}w_z
\right)^2
}{W_r}
\geq
2^{-n}\frac{w(Q)^2}{W}.
\tag{1}
\]
Accepted fact `aca624dd8874e5a5` also gives
\[
\sum_{c\in\mathbb Z^n}\kappa_c=2^{-n}W,
\qquad
0\leq\kappa_c\leq w_c
\quad(c\in\mathbb Z^n).
\tag{2}
\]

In particular, suppose \(n=2\) and \(z_0\in\mathbb Z^2\) satisfies
\[
w(Q)\geq\frac W4
\tag{3}
\]
for every proper closed halfspace \(Q\subseteq\mathbb R^2\) containing
\(z_0\).  Then
\[
\kappa(Q)\geq\frac W{64}
\tag{4}
\]
for every such \(Q\).

Here is the exact implication from (4) to the registered anchored
affine-certificate capacity.  Put
\[
D_+:=\{z\in\mathbb Z^2:w_z>0\}.
\]
For every finite nonempty set \(E\subseteq D_+\) satisfying
\[
z_0\in\operatorname{conv}(E),
\qquad
q(E):=\dim\operatorname{aff}(E),
\]
and every affine map
\[
s:\operatorname{aff}(E)\longrightarrow\mathbb R^d
\quad\text{satisfying}\quad
s(z)\in C_z\quad(z\in E),
\]
define its lattice hull
\[
D_E:=\operatorname{conv}(E)\cap\mathbb Z^2.
\]
Convexity of \(C\) then gives \(s(z)\in C_z\) for every \(z\in D_E\).
For \((z,x)\in C\), define the absolute fiber depth
\[
\delta_C(z,x):=
\inf\left\{
\operatorname{vol}_d(C_z\cap J):
J\subseteq\mathbb R^d
\text{ is a proper closed halfspace and }x\in J
\right\}.
\]
If \(q(E)>0\), define
\[
\alpha_{z_0}(E,s):=
\inf_{\substack{
R\subseteq\operatorname{aff}(E)\text{ a proper closed halfspace}\\
z_0\in R}}
\sum_{z\in D_E\cap R}\delta_C(z,s(z)).
\tag{5}
\]
If \(q(E)=0\), the conditions on \(E\) force
\(E=D_E=\{z_0\}\), and define
\[
\alpha_{z_0}(E,s):=\delta_C(z_0,s(z_0)).
\tag{6}
\]
The anchored affine-certificate capacity is
\[
\mathfrak A_{z_0}(C):=
\sup_{E,s}\alpha_{z_0}(E,s),
\tag{7}
\]
where the supremum ranges over precisely the admissible pairs just
defined.

Put
\[
P:=\operatorname{conv}\{c\in\mathbb Z^2:\kappa_c>0\},
\qquad
q:=\dim\operatorname{aff}(P).
\tag{8}
\]
Equation (4) implies \(z_0\in P\).  Suppose there is one affine map
\[
s:\operatorname{aff}(P)\longrightarrow\mathbb R^d
\]
such that
\[
s(c)\in C_c,\qquad
\delta_C(c,s(c))\geq\kappa_c
\quad(c\in P\cap\mathbb Z^2).
\tag{9}
\]
Then
\[
\mathfrak A_{z_0}(C)\geq\frac W{64}.
\tag{10}
\]
More precisely, \(E=\operatorname{vert}(P)\) is an admissible set in
(7), its lattice hull is \(D_E=P\cap\mathbb Z^2\), and
\[
\alpha_{z_0}(E,s)\geq\frac W{64}.
\tag{11}
\]

The following separate statement concerns arbitrary finite abstract
lattice weights and does not assume convex-body realizability.  Let
\(\widehat w=(\widehat w_z)_{z\in\mathbb Z^2}\) be nonnegative, finitely
supported, and nonzero.  Put
\[
\widehat W_r:=\sum_{z\equiv r\pmod2}\widehat w_z.
\]
Its normalized full discrete same-parity midpoint profile is
\[
\widehat\kappa_c:=
\frac14
\sum_{\substack{r\in(\mathbb Z/2\mathbb Z)^2\\\widehat W_r>0}}
\frac1{\widehat W_r}
\sum_{\substack{z\in\mathbb Z^2\\z\equiv r\pmod2}}
\widehat w_z\widehat w_{2c-z}
\quad(c\in\mathbb Z^2).
\tag{12}
\]
Its unnormalized ordered off-diagonal same-parity midpoint profile is
\[
\widehat\xi_c:=
\sum_{r\in(\mathbb Z/2\mathbb Z)^2}
\sum_{\substack{
z,z'\in\mathbb Z^2,\ z\equiv z'\equiv r\pmod2\\
z\neq z',\ z+z'=2c}}
\widehat w_z\widehat w_{z'}
\quad(c\in\mathbb Z^2).
\tag{13}
\]

For every \(0<\varepsilon<1/64\), define an exact profile of this type by
\[
u_+=(1,0),\qquad
u_1=(-1,4),\qquad
u_2=(-5,2),\qquad
u_3=(-1,-4),\qquad
\mathcal K=\{5,7,9,11\},
\]
\[
\widehat w_0=\varepsilon,\qquad
\widehat w_{u_+}=\frac14-\varepsilon,\qquad
\widehat w_{ku_j}=\frac1{16}
\quad(k\in\mathcal K,\ 1\leq j\leq3),
\tag{14}
\]
with all other weights zero.  This profile has total mass \(1\), satisfies
\[
\widehat w_z<\frac14\quad(z\in\mathbb Z^2),
\tag{15}
\]
\[
\sum_{z\in(a+L)\cap\mathbb Z^2}\widehat w_z<\frac12
\tag{16}
\]
for every coset \(a+L\) of every primitive rank-one sublattice
\(L\leq\mathbb Z^2\), satisfies
\[
0\in\operatorname{int}
\operatorname{conv}\{z:\widehat w_z>0\},
\tag{17}
\]
and has closed-halfspace depth exactly \(1/4\) at \(0\).  Its global
ordered off-diagonal same-parity mass satisfies
\[
\widehat Q^\circ
:=
\sum_r\widehat W_r^2-\sum_z\widehat w_z^2
=\frac{57}{64}-\frac32\varepsilon
>\frac{16-e}{256}.
\tag{18}
\]
Nevertheless, the proper closed halfspace
\[
Q_+:=\{(x_1,x_2)\in\mathbb R^2:x_1\geq0\}
\tag{19}
\]
contains \(0\) and satisfies
\[
\sum_{c\in Q_+\cap\mathbb Z^2}\widehat\xi_c=0.
\tag{20}
\]
Thus no positive lower bound for the off-diagonal cap mass in (20) follows
from the finite-weight hypotheses (15)--(18), even though
\(\widehat Q^\circ\) is bounded below by an absolute constant.

For the separately defined normalized full profile (12), the same
halfspace satisfies
\[
\sum_{c\in Q_+\cap\mathbb Z^2}\widehat\kappa_c
=
\frac14\left[
\varepsilon+
\frac{(1/4-\varepsilon)^2}{1-\varepsilon}
\right]
=
\frac1{64}+\frac{9\varepsilon}{64(1-\varepsilon)}.
\tag{21}
\]
Consequently, the \(W/64\) conclusion of (1) is sharp as
\(\varepsilon\downarrow0\) on abstract finite weight profiles satisfying
all of (15)--(18).  The profile (14) is not asserted to be the fiber
profile of a convex body.  Hence (20) refutes only the corresponding
abstract off-diagonal localization assertion; it is not a counterexample
to (10), to the registered convex-body subgoal, or to the locked target.

## Proof

Compactness of \(C\) implies that only finitely many integer fibers have
positive volume.  Fix a closed halfspace \(Q\subseteq\mathbb R^n\), and for
each \(r\in R_+\) put
\[
q_r:=
\sum_{\substack{z\in Q\cap\mathbb Z^n\\z\equiv r\pmod2}}w_z.
\]
If \(z,z'\in Q\), then \((z+z')/2\in Q\) because \(Q\) is convex.
Therefore every pair of points in the restrictions of \(\mu_r\) to base
points in \(Q\) contributes to
\(K_r(Q\times\mathbb R^d)\), including pairs whose midpoint lies on the
closed boundary.  Hence
\[
K_r(Q\times\mathbb R^d)\geq\frac{q_r^2}{W_r}.
\tag{22}
\]
Summing (22) with the factor \(2^{-n}\) proves the first inequality in
(1).  Weighted Cauchy-Schwarz gives
\[
\sum_{r\in R_+}\frac{q_r^2}{W_r}
\geq
\frac{\left(\sum_{r\in R_+}q_r\right)^2}
{\sum_{r\in R_+}W_r}
=\frac{w(Q)^2}{W},
\tag{23}
\]
which proves the second inequality.  Empty parity classes have
\(q_r=0\) and do not enter either sum.

Accepted fact `aca624dd8874e5a5` applies with exactly the definitions above.
It states that \(\mathsf A\mu\) has mass \(2^{-n}W\) and that every target
fiber has mass at most the original fiber volume.  These are exactly the
two assertions in (2), including zero-volume and lower-dimensional fibers.
For \(n=2\), equations (1) and (3) give
\[
\kappa(Q)\geq
\frac14\frac{(W/4)^2}{W}
=\frac W{64},
\]
which proves (4).

We next prove the fully defined affine-lifting implication.  The support of
\(\kappa\) is finite and nonempty by (2), so \(P\) in (8) is a nonempty
lattice polytope.  If \(z_0\notin P\), strict separation from this compact
polytope gives a proper closed halfspace of \(\mathbb R^2\) containing
\(z_0\) and disjoint from \(P\).  Its \(\kappa\)-mass is zero, contradicting
(4).  Thus \(z_0\in P\).

Every vertex of \(P\) belongs to the finite set
\(\{c:\kappa_c>0\}\), so
\[
E:=\operatorname{vert}(P)
\]
is finite and nonempty.  By (2), \(\kappa_c>0\) implies \(w_c>0\).
Therefore \(E\subseteq D_+\).  Also
\[
z_0\in P=\operatorname{conv}(E),\qquad
q(E)=\dim\operatorname{aff}(P)=q,
\]
and
\[
D_E=\operatorname{conv}(E)\cap\mathbb Z^2
=P\cap\mathbb Z^2.
\]
The map in (9) is affine on \(\operatorname{aff}(E)\) and is feasible at
every point of \(E\), so \((E,s)\) satisfies every admissibility condition
in (5)--(7).

Suppose \(q>0\).  Every proper closed halfspace \(R\) of
\(\operatorname{aff}(P)\) containing \(z_0\) is the intersection with
\(\operatorname{aff}(P)\) of a proper closed halfspace \(Q\) of
\(\mathbb R^2\) containing \(z_0\): extend a nonconstant affine functional
defining \(R\) from \(\operatorname{aff}(P)\) to \(\mathbb R^2\).  Since
\(\kappa\) is supported on \(P\), (4) and (9) yield
\[
\begin{aligned}
\sum_{c\in D_E\cap R}\delta_C(c,s(c))
&\geq
\sum_{c\in P\cap R\cap\mathbb Z^2}\kappa_c\\
&=
\sum_{c\in Q\cap\mathbb Z^2}\kappa_c
\geq\frac W{64}.
\end{aligned}
\]
Taking the infimum over \(R\) proves (11) in positive rank.

If \(q=0\), the nonempty polytope \(P\) is one lattice point.  Since
\(z_0\in P\), it is \(P=E=D_E=\{z_0\}\).  Equation (2) gives
\[
\kappa_{z_0}=\sum_c\kappa_c=\frac W4,
\]
and (9) gives
\[
\alpha_{z_0}(E,s)
=\delta_C(z_0,s(z_0))
\geq\kappa_{z_0}
=\frac W4>\frac W{64}.
\]
Thus (11) holds in rank zero as well.  Taking the supremum in (7) proves
(10).

It remains to verify the abstract calibration.  There are twelve points
\(ku_j\) in (14), each of mass \(1/16\), so
\[
\varepsilon+\left(\frac14-\varepsilon\right)
+12\cdot\frac1{16}=1.
\]
The strict singleton inequalities (15) follow from
\(0<\varepsilon<1/64\).

The positive support lies on four distinct lines through the origin, in
the directions \(u_+,u_1,u_2,u_3\).  A line through the origin contains
the anchor and points from at most one of these four directional groups.
Its mass is therefore at most
\[
\max\left\{
\varepsilon+\frac14-\varepsilon,\
\varepsilon+\frac14
\right\}
=\frac14+\varepsilon<\frac12.
\tag{24}
\]
A line not through the origin meets each of the four directional lines in
at most one point.  If it contains \(u_+\), its mass is at most
\[
\left(\frac14-\varepsilon\right)+3\cdot\frac1{16}
=\frac7{16}-\varepsilon<\frac12;
\]
if it does not contain \(u_+\), its mass is at most \(3/16\).
This proves (16) for every affine lattice line, hence for every primitive
rank-one coset.

The three positive support points \(u_+,5u_1,5u_3\) are noncollinear and
satisfy
\[
10u_++5u_1+5u_3=0.
\]
All three coefficients are positive, so \(0\) is in the interior of their
triangle.  This proves (17).

For a proper closed halfspace containing \(0\), moving its boundary to
\(0\) only makes it smaller.  A boundary-through-\(0\) halfspace is
\(\{x:\ell(x)\geq0\}\) for a nonzero linear functional \(\ell\).  Since
\[
2u_++u_1+u_3=0,
\]
the three numbers \(\ell(u_+),\ell(u_1),\ell(u_3)\) cannot all be negative.
The halfspace therefore contains the entire support group on at least one
of these three rays, as well as the anchor on its boundary.  Its mass is at
least
\[
\left(\frac14-\varepsilon\right)+\varepsilon=\frac14.
\]
The halfspace \(Q_+\) contains only \(0\) and \(u_+\) from the positive
support, so its mass is exactly \(1/4\).  This proves exact marginal depth
\(1/4\).

Every nonzero support point has parity \((1,0)\): every multiplier in
\(\mathcal K\) is odd, and each of \(u_+,u_1,u_2,u_3\) has odd first and
even second coordinate.  The anchor has parity \((0,0)\).  Hence
\[
\widehat W_{10}=1-\varepsilon,\qquad
\widehat W_{00}=\varepsilon,
\]
and the other two parity masses vanish.  Direct calculation gives
\[
\begin{aligned}
\widehat Q^\circ
&=(1-\varepsilon)^2+\varepsilon^2\\
&\quad-
\left[
\left(\frac14-\varepsilon\right)^2+\varepsilon^2
+12\left(\frac1{16}\right)^2
\right]\\
&=\frac{57}{64}-\frac32\varepsilon.
\end{aligned}
\]
For \(0<\varepsilon<1/64\), this is greater than \(111/128\), hence greater
than \(1/16\), while
\[
\frac{16-e}{256}<\frac{16}{256}=\frac1{16}.
\]
This proves (18).

The anchor has no distinct partner of its parity.  In parity \((1,0)\), if
neither endpoint is \(u_+\), both first coordinates are at most \(-5\).
If one endpoint is \(u_+\), the other has first coordinate at most \(-5\),
so the sum of their first coordinates is at most \(-4\).  The pair
\((u_+,u_+)\) is diagonal and is excluded from (13).  Thus every
off-diagonal same-parity midpoint has strictly negative first coordinate,
which proves (20).  This is a complete counterexample to the abstract
off-diagonal localization assertion stated immediately after (20).

For the normalized full profile (12), the only pairs with midpoint in
\(Q_+\) are the two diagonal pairs at \(0\) and \(u_+\).  Therefore
\[
\begin{aligned}
\sum_{c\in Q_+\cap\mathbb Z^2}\widehat\kappa_c
&=\frac14\left[
\frac{\varepsilon^2}{\varepsilon}
+
\frac{(1/4-\varepsilon)^2}{1-\varepsilon}
\right]\\
&=\frac14\left[
\varepsilon+
\frac{(1/4-\varepsilon)^2}{1-\varepsilon}
\right]\\
&=\frac1{64}+\frac{9\varepsilon}{64(1-\varepsilon)}.
\end{aligned}
\]
This proves (21).  Letting \(\varepsilon\downarrow0\) proves sharpness and
completes the proof.

## External sources

none
