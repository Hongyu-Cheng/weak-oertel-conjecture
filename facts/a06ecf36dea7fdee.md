---
fact_id: a06ecf36dea7fdee
kind: counterexample
author: "research-agent"
assurance: LLM-verified
subgoal_id: flat-pair-curvature-aggregation
depends_on: ["92b530e0a2281d6e"]
verifier_run: 7de5d3fb5ca84602
target_match: null
---

## Statement

For \(k\ge1\), let \(\omega_k\) be the \(k\)-dimensional volume of the Euclidean unit ball.  Given \(n,d\ge1\) and \(R>0\), define the convex body
\[
C_R^{n,d}:=\{(\mathbf z,\mathbf x)\in\mathbb R^n\times\mathbb R^d:
\|\mathbf z\|_2+\|\mathbf x\|_2\le R\}.
\]
Its lattice-fiber mass and root profile are
\[
a_R(\mathbf z)=\omega_d(R-\|\mathbf z\|_2)_+^d,
\qquad
g_R(\mathbf z)=a_R(\mathbf z)^{1/d}
=\omega_d^{1/d}(R-\|\mathbf z\|_2)_+,
\]
and put \(W_R:=\sum_{\mathbf z\in\mathbb Z^n}a_R(\mathbf z)\).

Fix a lattice anchor \(\mathbf z_0\) with \(a_R(\mathbf z_0)>0\) and a number \(0<\beta\le1/2\).  Put \(q_\beta=(1-\beta)^{1/d}\).  Call a nonzero displacement \(\mathbf w\in\mathbb Z^n\) eligible when
\[
2g_R(\mathbf z_0)-g_R(\mathbf z_0+\mathbf w)
-g_R(\mathbf z_0-\mathbf w)
\le (1-q_\beta)g_R(\mathbf z_0).
\]
Identify \(\mathbf w\) and \(-\mathbf w\), and define the full eligible-pair score
\[
\mathcal A_R(\mathbf z_0,\beta)
:=
a_R(\mathbf z_0)
+
\sum_{\{\mathbf w,-\mathbf w\}\ {\rm eligible}}
\min\{a_R(\mathbf z_0+\mathbf w),a_R(\mathbf z_0-\mathbf w)\}.
\]
The symmetric two-point sets indexed by distinct terms of this sum are automatically pairwise disjoint.

Let \(c=\log 2\), \(\kappa_d=1-2^{-1/d}\), and, for \(0\le s\le1\), set
\[
A_d(s):=s+\frac{\kappa_d(1-s)}2,
\qquad
B_d(s):=
\left(s\kappa_d(1-s)+\frac{\kappa_d^2(1-s)^2}{4}\right)^{1/2}.
\]
Then
\[
\limsup_{R\to\infty}
\sup_{\substack{\mathbf z_0\in\mathbb Z^n\\a_R(\mathbf z_0)>0}}
\sup_{0<\beta\le1/2}
\frac{\mathcal A_R(\mathbf z_0,\beta)}{W_R}
\le
\sup_{0\le s\le1}
\frac12\binom{n+d}{n}(1-s)^dA_d(s)B_d(s)^{n-1}.
\tag{1}
\]
If \(d\ge n(n+1)/2\), the right-hand side of (1) is at most
\[
U_n:=
\frac{e^{\,1+c/2}}{2n!}\,
c^{(n-1)/2}
\left(\frac{n+1}{2}\right)^{(n+1)/2}
e^{-(n+1)/2},
\tag{2}
\]
and \(2^nU_n\to0\).

Consequently, with \(d_n=n(n+1)/2\), one can choose integers \(R_n\to\infty\) such that
\[
\sup_{\substack{\mathbf z_0\in\mathbb Z^n\\a_{R_n}(\mathbf z_0)>0}}
\sup_{0<\beta\le1/2}
\frac{\mathcal A_{R_n}(\mathbf z_0,\beta)}
{2^{-n}W_{R_n}}
\longrightarrow0.
\tag{3}
\]
For any point \(\mathbf x_0\) in a positive-volume fiber of \(C_{R_n}^{n,d_n}\), its absolute fiber-depth ratio is at most \(1/2\).  Hence (3) applies to the actual value of \(\beta\) occurring in accepted fact `92b530e0a2281d6e`, and to every subfamily of flat pairs allowed by that fact.  In contrast,
\[
h_{C_R^{n,d}\cap(\mathbb Z^n\times\mathbb R^d)}
((\mathbf0,\mathbf0))=\frac12W_R
\tag{4}
\]
for every \(n,d,R\).

## Proof

The function \((\mathbf z,\mathbf x)\mapsto\|\mathbf z\|_2+\|\mathbf x\|_2\) is convex, so \(C_R^{n,d}\) is a full-dimensional convex body.  Its fiber above \(\mathbf z\) is the Euclidean \(d\)-ball of radius \((R-\|\mathbf z\|_2)_+\), which proves the displayed formulas for \(a_R\) and \(g_R\).  On the projection ball, \(R-\|\mathbf z\|_2\) is concave.  Thus this is an in-class root-concave profile realized by one convex body.

For any point in any positive-volume fiber, the two complementary halfspaces through that point have fiber volumes summing to the full fiber volume, because their common boundary is \(d\)-null.  At least one has volume at most half of the fiber.  Therefore every positive absolute fiber-depth ratio satisfies \(\beta\le1/2\).  Since
\[
q_\beta=(1-\beta)^{1/d}\ge2^{-1/d},
\]
every pair eligible for this \(\beta\) also satisfies the more permissive condition obtained by replacing \(1-q_\beta\) by
\(\kappa_d=1-2^{-1/d}\).
The eligible sum is finite: a displacement whose two endpoints both have zero root value cannot be eligible, while there are only finitely many lattice displacements for which at least one endpoint lies in the bounded projection ball.

Fix an anchor, write \(r_0=\|\mathbf z_0\|_2\), and put
\[
r_\pm=\|\mathbf z_0\pm\mathbf w\|_2,
\qquad
\Delta=\kappa_d(R-r_0).
\]
If a pair has positive minimum endpoint mass, then \(r_+,r_-<R\).  Cancelling the common factor \(\omega_d^{1/d}\) in the permissive flatness condition gives exactly
\[
r_++r_--2r_0\le\Delta.
\tag{5}
\]
Thus every positive-contribution eligible displacement lies in
\[
E(\mathbf z_0,\Delta)
:=
\{\mathbf w\in\mathbb R^n:
\|\mathbf z_0+\mathbf w\|_2+\|\mathbf z_0-\mathbf w\|_2
\le2r_0+\Delta\}.
\tag{6}
\]
This is the prolate Euclidean ellipsoid centered at the origin whose major semiaxis, in the direction of \(\mathbf z_0\), and common minor semiaxis are
\[
\mathsf A=r_0+\frac{\Delta}{2},
\qquad
\mathsf B=\left(r_0\Delta+\frac{\Delta^2}{4}\right)^{1/2}.
\tag{7}
\]
The same formulas cover \(r_0=0\), when (6) is a ball.  Indeed, the foci in (6) are \(\pm\mathbf z_0\), the sum of distances is at most \(2\mathsf A\), and
\(\mathsf B^2=\mathsf A^2-r_0^2\).

For every displacement,
\[
\max\{r_+,r_-\}\ge r_0,
\]
as follows from
\(r_+^2+r_-^2=2r_0^2+2\|\mathbf w\|_2^2\).  Hence every pair contribution has the exact form
\[
\min\{a_R(\mathbf z_0+\mathbf w),a_R(\mathbf z_0-\mathbf w)\}
=
\omega_d\bigl(R-\max\{r_+,r_-\}\bigr)_+^d
\le a_R(\mathbf z_0).
\tag{8}
\]
Distinct classes \(\{\mathbf w,-\mathbf w\}\) give disjoint endpoint pairs: an endpoint shared by the pairs for \(\mathbf w\) and \(\mathbf v\) forces \(\mathbf v=\pm\mathbf w\).  Equations (5), (6), and (8) therefore give, uniformly in \(0<\beta\le1/2\),
\[
\mathcal A_R(\mathbf z_0,\beta)
\le
\frac{a_R(\mathbf z_0)}2
\left(\#(E(\mathbf z_0,\Delta)\cap\mathbb Z^n)+1\right).
\tag{9}
\]
Pairs with a zero endpoint contribution do not affect this estimate.

We next compute the large-\(R\) ratio exactly.  Riemann sums and polar coordinates give
\[
\begin{aligned}
\lim_{R\to\infty}\frac{W_R}{R^{n+d}}
&=
\omega_d\int_{\|\mathbf u\|_2\le1}(1-\|\mathbf u\|_2)^d\,d\mathbf u\\
&=
\omega_d\,n\omega_n\,\mathrm B(n,d+1)
=
\omega_d\omega_n\frac{n!\,d!}{(n+d)!}.
\end{aligned}
\tag{10}
\]
Consider any sequence of anchors and pass to a subsequence for which
\(r_0/R\to s\in[0,1]\).  If \(s<1\), then the normalized ellipsoids \(R^{-1}E(\mathbf z_0,\Delta)\) converge, after also passing to a subsequence of their major-axis directions when needed, to a full-dimensional ellipsoid with semiaxes \(A_d(s)\) and \(B_d(s)\).  Standard lattice Riemann sums for convergent convex bodies then give
\[
\lim_{R\to\infty}
\frac{\#(E(\mathbf z_0,\Delta)\cap\mathbb Z^n)}{R^n}
=\omega_n A_d(s)B_d(s)^{n-1}.
\tag{11}
\]
If \(s=1\), the ellipsoid is contained in a Euclidean ball of radius less than \(3R/2\), while
\(a_R(\mathbf z_0)/R^d=\omega_d(1-r_0/R)^d\to0\).  The ratio in (9), divided by (10), therefore tends to zero.  Combining (9), (10), and (11), and using
\[
\frac1{n\mathrm B(n,d+1)}=\binom{n+d}{n},
\]
shows that the limsup along the chosen anchor sequence is at most the expression inside the supremum in (1).  A maximizing-sequence and compactness argument in \(s\in[0,1]\) proves (1).

It remains to bound that expression.  Write \(x=ds\) and \(c=\log2\).  Since
\[
\kappa_d=1-e^{-c/d}\le\frac cd,
\]
we have
\[
A_d(s)\le\frac{x+c/2}{d},
\qquad
B_d(s)^2
\le\frac{c(x+c/4)}{d^2},
\qquad
(1-s)^d\le e^{-x}.
\tag{12}
\]
Moreover, when \(d\ge n(n+1)/2\),
\[
\binom{n+d}{n}
=
\frac{d^n}{n!}\prod_{j=1}^n\left(1+\frac jd\right)
\le
\frac{e\,d^n}{n!}.
\tag{13}
\]
Substituting (12) and (13) into (1), and putting \(y=x+c/2\) and \(p=(n+1)/2\), gives
\[
\begin{aligned}
\frac12\binom{n+d}{n}(1-s)^dA_d(s)B_d(s)^{n-1}
&\le
\frac{e}{2n!}(x+c/2)\,[c(x+c/4)]^{(n-1)/2}e^{-x}\\
&\le
\frac{e^{\,1+c/2}}{2n!}c^{(n-1)/2}y^pe^{-y}\\
&\le
\frac{e^{\,1+c/2}}{2n!}c^{(n-1)/2}p^pe^{-p}
=U_n.
\end{aligned}
\tag{14}
\]
Here the last inequality uses the exact maximum of \(y^pe^{-y}\), attained at \(y=p\); the allowed range \(y\ge c/2\) contains \(p\).

The elementary bound \(n!\ge(n/e)^n\), together with \(n+1\le2n\), yields
\[
2^nU_n
\le
\frac{e^{\,1+c/2}}{2\sqrt c}
\sqrt{\frac ne}
\left(2\sqrt{\frac{ce}{n}}\right)^n,
\tag{15}
\]
which tends to zero.  Taking \(d_n=n(n+1)/2\), equation (1) permits an integer \(R_n\) so large that the left-hand side of (1) is at most \(U_n+2^{-2n}\).  Multiplication by \(2^n\) and (15) prove (3).

Accepted fact `92b530e0a2281d6e` can use only pairs satisfying exactly the eligibility condition above, and its depth consequence multiplies the anchor-plus-pair score by the actual \(\beta\).  Since every such \(\beta\) is at most \(1/2\), (3) rules out a universal \(c\,2^{-n}W_R\) conclusion from that aggregation mechanism alone.

Finally, \(C_R^{n,d}\cap(\mathbb Z^n\times\mathbb R^d)\) and its mixed measure \(\mu\) are centrally symmetric.  If a halfspace \(H\) contains the origin, then \(H\cup(-H)\) is the whole ambient space.  Symmetry gives \(\mu(H)=\mu(-H)\), hence \(2\mu(H)\ge W_R\).  The halfspace \(\{(\mathbf z,\mathbf x):x_1\ge0\}\) bisects every positive-volume Euclidean-ball fiber and has mass exactly \(W_R/2\).  This proves (4) and confirms that the construction obstructs only the flat-pair aggregation route.

## External sources

none
