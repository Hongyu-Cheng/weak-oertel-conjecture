---
fact_id: c2ed1a4e6f4a7c4d
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: pooled-parity-affine-reflection
depends_on: ["6d6fcf377e68c79c"]
verifier_run: 4d6b03f69b524c72
target_match: null
---

## Statement

Let \(n,d\in\mathbb Z_{>0}\), let
\(C\subseteq\mathbb R^n\times\mathbb R^d\) be a convex body, and put

\[
\Lambda:=\mathbb Z^n\times\mathbb R^d,
\qquad S:=C\cap\Lambda\neq\varnothing.
\]

For \(z\in\mathbb Z^n\), write

\[
C_z:=\{x\in\mathbb R^d:(z,x)\in C\}.
\]

For every Borel set \(A\subseteq\mathbb R^{n+d}\), define

\[
\mu_C(A):=
\sum_{z\in\mathbb Z^n}
\int_{C_z}\mathbf 1_A(z,x)\,dx,
\qquad
W:=\mu_C(\mathbb R^{n+d}).
\]

For \(y\in S\), let

\[
h_S(y):=\inf\{\mu_C(H):H\text{ is a closed halfspace and }y\in H\},
\qquad
h_{\max}(C):=\sup_{y\in S}h_S(y).
\]

Fix an affine map \(s:\mathbb R^n\to\mathbb R^d\).  For every parity class
\(r\in(\mathbb Z/2\mathbb Z)^n\), define the Borel function

\[
F_{r,s}(u):=
\sum_{\substack{z\in\mathbb Z^n\\ z\equiv r\pmod 2}}
\mathbf 1_{C_z-s(z)}(u)
\qquad (u\in\mathbb R^d)
\]

and set

\[
\mathfrak R(s):=
\frac12\sum_{r\in(\mathbb Z/2\mathbb Z)^n}
\int_{\mathbb R^d}
\min\{F_{r,s}(u),F_{r,s}(-u)\}\,du.
\]

Then there is \(y_s\in S\) such that every closed halfspace \(H\ni y_s\)
satisfies

\[
\mu_C(H)\geq 2^{-n}\mathfrak R(s).
\tag{1}
\]

In particular,

\[
h_{\max}(C)\geq 2^{-n}\mathfrak R(s).
\tag{2}
\]

If, for every parity class \(r\), the pooled profile is centrally symmetric
in the measure-theoretic sense

\[
F_{r,s}(u)=F_{r,s}(-u)
\quad\text{for almost every }u\in\mathbb R^d,
\tag{3}
\]

then

\[
h_{\max}(C)\geq 2^{-n-1}W.
\tag{4}
\]

## Proof

Because \(C\) is compact, its projection onto the first \(n\) coordinates is
compact.  Hence

\[
\mathcal Z:=\{z\in\mathbb Z^n:C_z\neq\varnothing\}
\]

is finite.  In particular, all sums defining \(F_{r,s}\) are finite, the
profiles are Borel, and

\[
\sum_r\int_{\mathbb R^d}F_{r,s}(u)\,du
=\sum_{z\in\mathcal Z}|C_z|_d=W.
\tag{5}
\]

It follows that \(0\leq\mathfrak R(s)\leq W/2<\infty\).  If
\(\mathfrak R(s)=0\), choose any \(y_s\in S\).  Every mixed halfspace mass is
nonnegative, so (1) follows.  We therefore assume for the remainder of the
proof that

\[
R:=\mathfrak R(s)>0.
\tag{6}
\]

We first construct the finite-capacity ordered-pair coupling.  For each parity
class \(r\), fix once and for all an enumeration

\[
\mathcal Z_r:=\{z\in\mathcal Z:z\equiv r\pmod2\}
=\{z_{r,1},\ldots,z_{r,N_r}\}.
\]

Put \(D_{r,i}:=C_{z_{r,i}}-s(z_{r,i})\), and for \(u\in\mathbb R^d\) define

\[
a_{r,i}(u):=\mathbf1_{D_{r,i}}(u),
\qquad
b_{r,j}(u):=\mathbf1_{D_{r,j}}(-u),
\]

\[
A_{r,i}(u):=\sum_{k=1}^i a_{r,k}(u),
\qquad
B_{r,j}(u):=\sum_{k=1}^j b_{r,k}(u),
\]

and

\[
\chi_{r,i,j}(u):=
a_{r,i}(u)b_{r,j}(u)
\mathbf1_{\{A_{r,i}(u)=B_{r,j}(u)\}}.
\tag{7}
\]

All these functions are Borel.  Formula (7) matches the \(k\)-th active set
at \(u\) to the \(k\)-th active set at \(-u\).  Thus, pointwise for every
\(u\),

\[
\sum_{i=1}^{N_r}\sum_{j=1}^{N_r}\chi_{r,i,j}(u)
=\min\{F_{r,s}(u),F_{r,s}(-u)\},
\tag{8}
\]

while for every \(i,j\), respectively,

\[
\sum_j\chi_{r,i,j}(u)\leq a_{r,i}(u),
\qquad
\sum_i\chi_{r,i,j}(u)\leq b_{r,j}(u).
\tag{9}
\]

Define endpoint maps

\[
p^+_{r,i}(u):=(z_{r,i},s(z_{r,i})+u),
\qquad
p^-_{r,j}(u):=(z_{r,j},s(z_{r,j})-u).
\tag{10}
\]

For every nonnegative Borel function
\(\Phi:(\mathbb R^{n+d})^2\to[0,\infty]\), define

\[
\int\Phi(p,q)\,d\Pi(p,q)
:=
\frac12\sum_r\sum_{i=1}^{N_r}\sum_{j=1}^{N_r}
\int_{\mathbb R^d}
\chi_{r,i,j}(u)
\Phi\bigl(p^+_{r,i}(u),p^-_{r,j}(u)\bigr)\,du.
\tag{11}
\]

This is a positive finite Borel measure on ordered endpoint pairs: it is a
finite sum of pushforwards of Borel restrictions of Lebesgue measure.  On the
support of each integrand, \(u\in D_{r,i}\) and \(-u\in D_{r,j}\), so both
ordered endpoints in (10) belong to \(S\).  Equations (8) and (11) give

\[
|\Pi|
=\frac12\sum_r\int_{\mathbb R^d}
\min\{F_{r,s}(u),F_{r,s}(-u)\}\,du
=R.
\tag{12}
\]

Let \(\Pi_1,\Pi_2\) be the first and second endpoint marginals of \(\Pi\).
For every nonnegative Borel function
\(\varphi:\mathbb R^{n+d}\to[0,\infty]\), (9) gives

\[
\begin{aligned}
\int\varphi\,d\Pi_1
&=\frac12\sum_{r,i,j}\int
\chi_{r,i,j}(u)\varphi(p^+_{r,i}(u))\,du\\
&\leq\frac12\sum_{r,i}\int
a_{r,i}(u)\varphi(z_{r,i},s(z_{r,i})+u)\,du\\
&=\frac12\int\varphi\,d\mu_C.
\end{aligned}
\tag{13}
\]

Similarly,

\[
\begin{aligned}
\int\varphi\,d\Pi_2
&\leq\frac12\sum_{r,j}\int
b_{r,j}(u)\varphi(z_{r,j},s(z_{r,j})-u)\,du\\
&=\frac12\sum_{r,j}\int_{D_{r,j}}
\varphi(z_{r,j},s(z_{r,j})+v)\,dv\\
&=\frac12\int\varphi\,d\mu_C,
\end{aligned}
\tag{14}
\]

where the middle equality uses \(v=-u\).  Consequently,

\[
\Pi_1+\Pi_2\leq\mu_C
\quad\text{as Borel measures.}
\tag{15}
\]

This is the required endpoint-capacity audit.  At a fixed original endpoint
with deviation \(v\), its first-role density can arise only from the parameter
\(u=v\) and is at most \(1/2\); its second-role density can arise only from
\(u=-v\) and is at most \(1/2\).  Thus the two roles together use its original
fiber density at most once.  This also covers \(v=0\), diagonal pairs, and
endpoints on fiber boundaries.  The factor \(1/2\) in (11), and hence in the
definition of \(\mathfrak R(s)\), is exactly what makes the combined capacity
in (15) equal to one rather than two.

Let

\[
M(p,q):=\frac{p+q}{2},
\qquad
\rho:=M_\#\Pi.
\tag{16}
\]

If \(\chi_{r,i,j}(u)=1\), the bases \(z_{r,i}\) and \(z_{r,j}\) have the same
parity, so

\[
m_{r,i,j}:=\frac{z_{r,i}+z_{r,j}}2\in\mathbb Z^n.
\tag{17}
\]

Writing \(s(z)=Az+b\), the midpoint of the corresponding endpoints is

\[
\begin{aligned}
M\bigl(p^+_{r,i}(u),p^-_{r,j}(u)\bigr)
&=\left(
\frac{z_{r,i}+z_{r,j}}2,
\frac{s(z_{r,i})+u+s(z_{r,j})-u}2
\right)\\
&=(m_{r,i,j},s(m_{r,i,j})).
\end{aligned}
\tag{18}
\]

Both endpoints are in \(C\), including when either is on its boundary.
Convexity of \(C\) therefore puts every midpoint in (18) in \(C\).  Thus
\(\rho\) is a finite atomic measure of mass

\[
|\rho|=|\Pi|=R
\tag{19}
\]

supported on integral-base points of the affine graph

\[
L_s(m):=(m,s(m))
\tag{20}
\]

that lie in \(C\).

We next prove domination for every closed halfspace, without deleting its
boundary.  Let \(H\) be a proper closed halfspace, written as

\[
H=\{x:\ell(x)\geq0\}
\]

for an affine functional \(\ell\).  If \(M(p,q)\in H\), then

\[
0\leq\ell(M(p,q))=\frac{\ell(p)+\ell(q)}2.
\]

It is therefore impossible that both endpoints have strictly negative score.
Hence, pointwise on all ordered pairs,

\[
\mathbf1_H(M(p,q))
\leq\mathbf1_H(p)+\mathbf1_H(q).
\tag{21}
\]

The same inequality is immediate for the whole space.  In particular, (21)
includes the case in which the midpoint is on the boundary of \(H\), and any
endpoint on that boundary is counted because \(H\) is closed.  Integrating
(21) and using (15) yields

\[
\rho(H)
\leq\Pi_1(H)+\Pi_2(H)
\leq\mu_C(H)
\tag{22}
\]

for every closed halfspace \(H\), with no assumption that its boundary is
null for either measure.

Let

\[
\nu:=(\operatorname{pr}_{\mathbb R^n})_\#\rho.
\tag{23}
\]

This is a nonzero finite Borel measure of mass \(R\), supported on a finite
subset of \(\mathbb Z^n\), and \(\rho=(L_s)_\#\nu\).  Apply accepted fact
`6d6fcf377e68c79c` with continuous dimension zero.  There exists
\(m_0\in\mathbb Z^n\) such that every closed base halfspace
\(J\subseteq\mathbb R^n\) containing \(m_0\) satisfies

\[
\nu(J)\geq 2^{-n}R.
\tag{24}
\]

We verify that the graph point over \(m_0\) is feasible.  Let

\[
K:=\operatorname{conv}(\operatorname{supp}\nu).
\]

If \(m_0\notin K\), strict separation from the compact convex set \(K\) gives
a closed base halfspace \(J\) containing \(m_0\) and disjoint from \(K\).
Then \(\nu(J)=0\), contradicting (24) and \(R>0\).  Hence \(m_0\in K\).
Every point \(L_s(m)\) with \(m\in\operatorname{supp}\nu\) belongs to \(C\)
by (18).  Since \(L_s\) is affine and \(C\) is convex,

\[
y_s:=L_s(m_0)
\in L_s(K)
=\operatorname{conv}\bigl(L_s(\operatorname{supp}\nu)\bigr)
\subseteq C.
\tag{25}
\]

Together with \(m_0\in\mathbb Z^n\), this proves \(y_s\in S\).

Finally, let \(H\subseteq\mathbb R^{n+d}\) be any closed halfspace containing
\(y_s\).  Its pullback

\[
J:=L_s^{-1}(H)
\tag{26}
\]

is a closed base halfspace, possibly all of \(\mathbb R^n\), and it contains
\(m_0\).  Since \(\rho=(L_s)_\#\nu\), equations (22), (24), and (26) give

\[
\mu_C(H)
\geq\rho(H)
=\nu(J)
\geq2^{-n}R
=2^{-n}\mathfrak R(s).
\tag{27}
\]

This proves (1) and (2), including vertical halfspaces, nonvertical
halfspaces, degenerate whole-space pullbacks, and positive mass on a
halfspace boundary.

It remains to prove the stated corollary.  Under (3), the minimum in the
definition of \(\mathfrak R(s)\) equals \(F_{r,s}(u)\) almost everywhere for
each \(r\).  Therefore (5) gives

\[
\mathfrak R(s)
=\frac12\sum_r\int_{\mathbb R^d}F_{r,s}(u)\,du
=\frac W2.
\tag{28}
\]

Substitution of (28) into (2) proves (4).

## External sources

none
