---
fact_id: f4ac60fcb8b27be5
kind: counterexample
author: "research-agent"
assurance: LLM-verified
subgoal_id: packed-unconditioned-transference-no-go
depends_on: ["51ff186e1aaeaa85","6769574fc1bd9f8d","ae0161dd5d4ea672","bb1db0d4237156aa","ca3ef8792d78322a","ebc478d91566cb69"]
verifier_run: d6e0c0be210a4f36
target_match: null
---

## Statement

For a compact full-dimensional convex body
\(C\subseteq\mathbb R^n\times\mathbb R^d\), write

\[
C_z:=\{x:(z,x)\in C\},\qquad
a_z:=\operatorname{vol}_d(C_z),\qquad
D_+(C):=\{z\in\mathbb Z^n:a_z>0\},
\]

\[
W(C):=\sum_{z\in\mathbb Z^n}a_z,
\qquad
\mu_C(A):=\sum_{z\in\mathbb Z^n}
\operatorname{vol}_d\{x\in C_z:(z,x)\in A\}.
\]

For \(p\in C\cap(\mathbb Z^n\times\mathbb R^d)\), put

\[
h_C(p):=\inf\{\mu_C(H):H\text{ is a closed ambient halfspace and }p\in H\}.
\]

For a \(d\)-dimensional convex body \(K\) and
\(0<t\leq\operatorname{vol}_d(K)\), let

\[
\mathsf M_t(K):=
\left\{
\frac1t\int_Kx f(x)\,dx:
0\leq f\leq1\text{ a.e.},\ \int_Kf\,dx=t
\right\}.
\]

For \(m\in\mathbb Z^n\cap\operatorname{conv}D_+(C)\), define

\[
\Lambda_m(D_+(C)):=
\left\{\lambda\in\mathbb R_+^{D_+(C)}:
\sum_z\lambda_z=1,\ \sum_z\lambda_zz=m\right\}
\]

and its half-mass complete core by

\[
\mathcal K_m^{1/2}(C):=
\bigcap_{\lambda\in\Lambda_m(D_+(C))}
\sum_{z\in D_+(C)}
\lambda_z\mathsf M_{a_z/2}(C_z).
\tag{1}
\]

Call \(m\) an allowed weighted centerpoint if every proper closed base
halfspace \(J\subseteq\mathbb R^n\) containing \(m\) satisfies

\[
\sum_{z\in D_+(C)\cap J}a_z\geq 2^{-n}W(C).
\tag{2}
\]

When \(\mathcal K_m^{1/2}(C)=\varnothing\), use the following exact meaning
of a legal empty-branch circuit and descendant.  For \(z\in D_+(C)\), put

\[
D_z:=\mathsf M_{a_z/2}(C_z),
\qquad
h_z(v):=\max_{x\in D_z}\langle v,x\rangle,
\]

\[
\phi_m(v):=
\min_{\lambda\in\Lambda_m(D_+(C))}
\sum_z\lambda_zh_z(v).
\]

A legal support-minimal circuit consists of nonzero
\(v_1,\ldots,v_r\in\mathbb R^d\) and positive
\(\theta_1,\ldots,\theta_r\) such that

\[
\sum_i\theta_i=1,
\qquad
\sum_i\theta_iv_i=0,
\qquad
\sum_i\theta_i\phi_m(v_i)<0,
\tag{2a}
\]

with \(r\) minimal among all data satisfying (2a).  Its legal affine
minorants are affine functions \(\ell_i:\mathbb R^n\to\mathbb R\) with

\[
\ell_i(z)\leq h_z(v_i)\quad(z\in D_+(C)),
\qquad
\ell_i(m)=\phi_m(v_i).
\tag{2b}
\]

They define

\[
G_i:=\{(z,x):\langle v_i,x\rangle\geq\ell_i(z)\},
\qquad A_i:=C\cap G_i,
\]

and the resulting common descendant is the weighted same-base image

\[
B:=\left\{
\left(z,\sum_i\theta_ix_i\right):
(z,x_i)\in A_i\text{ for every }i
\right\}.
\tag{2c}
\]

These are exactly the legal data and descendant of accepted fact
`51ff186e1aaeaa85`.

Use the fully optimized complete-core capacity
\(G(C):=\mathfrak C_{\mathrm{core}}(C)\) of accepted fact
`ae0161dd5d4ea672`: it is the supremum of
\(\sum_{z\in E}t_z\) over all nonempty
\(E\subseteq D_+(C)\), all \(0<t_z\leq a_z\), and all
\(m\in\mathbb Z^n\cap\operatorname{conv}E\) for which

\[
\bigcap_{\lambda\in\Lambda_m(E)}
\sum_{z\in E}\lambda_z\mathsf M_{t_z}(C_z)\neq\varnothing
\tag{3}
\]

and

\[
\sum_{z\in E\cap J}t_z
\geq2^{-n}\sum_{z\in E}t_z
\tag{4}
\]

for every proper closed base halfspace \(J\ni m\).

There is an explicit sequence of convex bodies

\[
C_k\subseteq\mathbb R^{n_k}\times\mathbb R^{d_k},
\qquad k\geq2,
\]

with total mixed masses \(W_k>0\), target masses
\(a_k^*:=2^{-n_k}W_k\), and numbers

\[
\varepsilon_k\leq\frac{2k+1}{k(k+1)}\longrightarrow0,
\tag{5}
\]

having all of the following properties.

1.  The complete list of allowed weighted centerpoints is

\[
\{m_k,r_k\}.
\tag{6}
\]

Their half-mass cores satisfy

\[
\mathcal K_{m_k}^{1/2}(C_k)=\varnothing,
\qquad
\mathcal K_{r_k}^{1/2}(C_k)\neq\varnothing.
\tag{7}
\]

Thus every legal empty-core choice uses \(m_k\), and such choices exist.

2.  Put \(\beta:=1/(2e)\).  Fix any legal support-minimal balanced-cap
circuit at \(m_k\), any legal exact affine minorants and positive balance
weights, and the resulting common convex descendant
\(B\subseteq C_k\) from accepted fact `51ff186e1aaeaa85`.  Then compatible
selected-state pairs exist.  Moreover, for every pair of positive measures
\((\nu_B,\nu_R)\) satisfying

\[
0\leq\nu_B\leq\mu_B,
\qquad
0\leq\nu_R\leq\mu_{C_k}-\nu_B,
\tag{8}
\]

\[
|\nu_B|=\beta a_k^*,
\qquad
|\nu_R|=(1-\beta)a_k^*,
\tag{9}
\]

\[
\int z\,d\nu_B=\beta a_k^*m_k,
\qquad
\int z\,d\nu_R=(1-\beta)a_k^*m_k,
\tag{10}
\]

the three normalized barycenters

\[
y_B:=\overline\nu_B,
\qquad
y_R:=\overline\nu_R,
\qquad
y:=\overline{\nu_B+\nu_R}
\tag{11}
\]

satisfy

\[
\max\{h_{C_k}(y_B),h_{C_k}(y),h_{C_k}(y_R)\}
\leq\varepsilon_k a_k^*.
\tag{12}
\]

The bound (12) is simultaneous over every circuit, every affine-minorant
and balance-weight choice, every resulting descendant, and every compatible
pair.  Hence no absolute \(c_{\mathrm{pack}}>0\) can give an unconditioned
lower bound \(c_{\mathrm{pack}}2^{-n}W\) for one of these three canonical
points in every legal empty branch.

3.  The same bodies have

\[
G(C_k)=W_k.
\tag{13}
\]

More precisely, their reservoir-fiber masses \(V_k\) satisfy

\[
\frac{V_k}{W_k}\longrightarrow1.
\tag{14}
\]

Therefore this sequence is maximally excluded by any small-complete-core
hypothesis.  In particular, it is not a counterexample to weak Oertel;
accepted fact `ae0161dd5d4ea672` in fact gives

\[
h_{\max}(C_k)\geq
\left(\frac{k}{k+1}\right)^k2^{-n_k}W_k.
\tag{15}
\]

## Proof

We construct the sequence.  The shallow-face component is the construction
certified in accepted fact `bb1db0d4237156aa`, with notation changed only to
avoid using one symbol for both a continuous vector space and a lattice
support.

Fix \(k\geq2\).  Let

\[
U_k:=\left\{u\in\mathbb R^{k+1}:\sum_{j=1}^{k+1}u_j=0\right\}
\]

with its Euclidean structure, and identify \(U_k\) isometrically with
\(\mathbb R^k\).  Put

\[
b_i:=\sqrt{\frac{k+1}{k}}
\left(e_i-\frac{\mathbf1}{k+1}\right)
\quad(1\leq i\leq k+1).
\]

Then

\[
\sum_{i=1}^{k+1}b_i=0,
\qquad
\|b_i\|_2=1,
\qquad
\langle b_i,b_j\rangle=-\frac1k\quad(i\neq j).
\tag{16}
\]

Let

\[
\Delta_k:=\operatorname{conv}\{b_1,\ldots,b_{k+1}\},
\qquad R_k:=k+1,
\]

let \(\mathbb B_k\subset U_k\) be the Euclidean unit ball, and write

\[
v_k:=\operatorname{vol}_k(\mathbb B_k),
\qquad
A_k:=\frac{\operatorname{vol}_k(R_k\Delta_k+\mathbb B_k)}{v_k}.
\tag{17}
\]

Because \(0\in\Delta_k\subseteq\mathbb B_k\),

\[
1\leq A_k\leq(k+2)^k.
\tag{18}
\]

Set

\[
M_k:=(k+2)^k,
\qquad
L_k:=k(M_k+2),
\qquad
q_k:=(k+1)L_k.
\tag{19}
\]

Index the standard basis of \(\mathbb R^{q_k}\) by
\(\epsilon_{i,\ell}\), where
\(1\leq i\leq k+1\) and \(1\leq\ell\leq L_k\), and define

\[
P_k:=\operatorname{conv}
\left\{
(\sigma\epsilon_{i,\ell},R_kb_i):
1\leq i\leq k+1,\ 1\leq\ell\leq L_k,
\ \sigma\in\{-1,1\}
\right\},
\]

\[
F_k:=P_k+(\{0\}\times\mathbb B_k)
\subseteq\mathbb R^{q_k}\times U_k.
\tag{20}
\]

The base-direction differences of the displayed generators span
\(\mathbb R^{q_k}\times\{0\}\); their same-color midpoints have continuous
coordinates \(R_kb_i\), whose differences span \(U_k\).  Thus \(F_k\) is
compact, convex, and full-dimensional.  Its base projection and its lattice
fibers are

\[
\operatorname{proj}F_k=
\{z\in\mathbb R^{q_k}:\|z\|_1\leq1\},
\tag{21}
\]

\[
(F_k)_0=R_k\Delta_k+\mathbb B_k,
\qquad
(F_k)_{\pm\epsilon_{i,\ell}}=R_kb_i+\mathbb B_k,
\tag{22}
\]

and there are no other lattice fibers.  In particular their volumes are
\(A_kv_k\) and \(v_k\), respectively.  These exact assertions also follow
from accepted fact `bb1db0d4237156aa`: an integral point of the
crosspolytope in (21) is (0) or one of its signed coordinate vertices;
at a vertex the fiber is forced to be the indicated summand, while equality
of the positive and negative coordinate coefficients at base (0) gives
the full convex hull \(R_k\Delta_k\).

For every \(x\in(F_k)_0\), (16) gives an index \(i\) with
\(\langle b_i,x\rangle\geq0\).  If \(j\neq i\) and
\(y\in R_kb_j+\mathbb B_k\), then

\[
\langle b_i,y-x\rangle
\leq R_k\langle b_i,b_j\rangle+1
-\langle b_i,x\rangle
\leq-\frac1k<0.
\tag{23}
\]

Consequently the halfspace
\(\{y:\langle b_i,y-x\rangle\geq0\}\) misses all remote fibers except the
\(2L_k\) fibers of color \(i\).  Put

\[
T_k:=(A_k+2L_k)v_k,
\qquad
a_k^*:=(A_k+q_k)v_k.
\tag{24}
\]

The ratio is

\[
\frac{T_k}{a_k^*}
=\frac{A_k+2L_k}{A_k+q_k}
\leq\frac{2k+1}{k(k+1)}=:\varepsilon_k.
\tag{25}
\]

Indeed, \(A_k\leq M_k\) gives

\[
A_k+2L_k
\leq M_k+2k(M_k+2)
\leq(2k+1)(M_k+2),
\]

whereas
\(A_k+q_k\geq q_k=k(k+1)(M_k+2)\).

We now add one exposed reservoir coordinate \(s\).  Put

\[
n_k:=q_k+1,
\qquad d_k:=k,
\]

\[
V_k:=
\left[2^{q_k+1}(A_k+q_k)-(A_k+2q_k)\right]v_k,
\tag{26}
\]

\[
\rho_k:=\left(\frac{V_k}{v_k}\right)^{1/k},
\qquad
K_k:=\rho_k\mathbb B_k.
\tag{27}
\]

Since \(A_k+2q_k<2(A_k+q_k)\), (26) is positive.  Define

\[
C_k:=\operatorname{conv}\left(
\{((z,0),x):(z,x)\in F_k\}
\cup
\{((0,-1),x):x\in K_k\}
\right)
\subseteq\mathbb R^{q_k+1}\times U_k.
\tag{28}
\]

The body is compact and convex.  The first set is full-dimensional in the
hyperplane \(s=0\), and the second set contains points with \(s=-1\), so
\(C_k\) is full-dimensional in \(\mathbb R^{n_k+d_k}\).

Its base projection is

\[
\Pi_k=
\{(z,s):-1\leq s\leq0,\ \|z\|_1\leq1+s\}.
\tag{29}
\]

If \((z,s)\in\Pi_k\cap\mathbb Z^{q_k+1}\), then \(s\in\{-1,0\}\).
At \(s=-1\) one has \(z=0\), while at \(s=0\), (21) applies.  Hence, with

\[
m_k:=(0,0),
\qquad r_k:=(0,-1),
\]

the positive lattice support is

\[
D_{+,k}:=D_+(C_k)
=\{m_k,r_k\}
\cup\{(\pm\epsilon_{i,\ell},0)},
\tag{30}
\]

and the fibers are exactly

\[
(C_k)_{r_k}=K_k,
\qquad
(C_k)_{m_k}=R_k\Delta_k+\mathbb B_k,
\qquad
(C_k)_{(\pm\epsilon_{i,\ell},0)}=R_kb_i+\mathbb B_k.
\tag{31}
\]

There is no enlargement at the two integral \(s\)-levels in the convex hull:
at \(s=0\) a convex combination uses only the first set in (28), and at
\(s=-1\) it uses only the reservoir set.  Thus, if
\(a^{(k)}_\zeta:=\operatorname{vol}_k((C_k)_\zeta)\), then

\[
a^{(k)}_{r_k}=V_k,
\quad
a^{(k)}_{m_k}=A_kv_k,
\quad
a^{(k)}_{(\pm\epsilon_{i,\ell},0)}=v_k.
\tag{32}
\]

The total mass is

\[
W_k=V_k+(A_k+2q_k)v_k
=2^{q_k+1}(A_k+q_k)v_k,
\tag{33}
\]

so the quantity \(a_k^*\) defined in (24) is indeed

\[
a_k^*=2^{-n_k}W_k.
\tag{34}
\]

We determine all allowed centerpoints.  Let \(J\) be a proper closed base
halfspace containing \(m_k\).  If it contains \(r_k\), its mass is at least
\(V_k>a_k^*\), because

\[
\frac{V_k}{a_k^*}
=2^{q_k+1}-\frac{A_k+2q_k}{A_k+q_k}
>2^{q_k+1}-2>1.
\tag{35}
\]

If \(J\) excludes \(r_k\), its trace on \(s=0\) is either the whole face
base or a closed halfspace containing (0).  Such a trace contains the
central point and at least one member of every antipodal pair, hence mass at
least \((A_k+q_k)v_k=a_k^*\).  This lower bound is attained by

\[
J=\{(z,s):\langle u,z\rangle+s\geq0\},
\tag{36}
\]

where every coordinate of \(u\) is nonzero.  Thus \(m_k\) is allowed.

Every proper base halfspace containing \(r_k\) contains the reservoir
fiber, so (35) makes \(r_k\) allowed.  On the other hand, for a remote point
\((\sigma\epsilon_{i,\ell},0)\), the proper closed base halfspace

\[
\{(z,s):\sigma z_{i,\ell}\geq1\}
\tag{37}
\]

contains no other positive lattice fiber and therefore has mass
\(v_k<a_k^*\).  Equation (29) shows that there are no other lattice points
in the base projection.  This proves (6).

We next compute the two half-mass cores.  Since \(r_k\) is the unique support
point with \(s=-1\), applying the \(s\)-coordinate to a barycentric
representation gives

\[
\Lambda_{r_k}(D_{+,k})=\{\delta_{r_k}\}.
\tag{38}
\]

Consequently

\[
\mathcal K_{r_k}^{1/2}(C_k)=\mathsf M_{V_k/2}(K_k)\neq\varnothing
\tag{39}
\]

by accepted fact `6769574fc1bd9f8d`.

For \(m_k\), fix one \(\ell\) for each color \(i\) and use the barycentric
representation

\[
\lambda^{i,\ell}:=
\frac12\delta_{(\epsilon_{i,\ell},0)}
+\frac12\delta_{(-\epsilon_{i,\ell},0)}.
\tag{40}
\]

Its Minkowski sum in (1) is

\[
D_i=
\mathsf M_{v_k/2}(R_kb_i+\mathbb B_k)
=R_kb_i+\mathsf M_{v_k/2}(\mathbb B_k)
\subseteq R_kb_i+\mathbb B_k.
\tag{41}
\]

Here the average of a nonempty convex set with itself is itself, translation
commutes with the defining integral of a metronoid, and metronoids lie in
their underlying convex bodies, all as in accepted fact
`6769574fc1bd9f8d`.  For \(i\neq j\),

\[
\|R_kb_i-R_kb_j\|
=R_k\sqrt{2-2\langle b_i,b_j\rangle}
=(k+1)\sqrt{2+\frac2k}>2.
\tag{42}
\]

Thus the two containing unit balls in (41) are disjoint, and

\[
\mathcal K_{m_k}^{1/2}(C_k)
\subseteq D_i\cap D_j=\varnothing.
\tag{43}
\]

This proves (7).  The equivalence between empty half-mass core and the
existence of a negative balanced-cap certificate in accepted fact
`ebc478d91566cb69` now proves that legal empty-branch circuits exist at
\(m_k\) and do not exist at \(r_k\).  Together with (6), every legal
empty-branch tuple therefore uses \(m_k\).

We prove a pointwise depth bound on that whole target fiber.  Fix
\(x\in(C_k)_{m_k}\), choose \(i\) as in (23), and put

\[
\kappa_{i,x}:=
1+\max_{y\in K_k}|\langle b_i,y-x\rangle|.
\]

The closed ambient halfspace

\[
H_{i,x}:=
\left\{((z,s),y):
\langle b_i,y-x\rangle+\kappa_{i,x}s\geq0
\right\}
\tag{44}
\]

contains \((m_k,x)\) on its boundary.  At \(s=-1\), every \(y\in K_k\)
satisfies

\[
\langle b_i,y-x\rangle-\kappa_{i,x}\leq-1,
\]

so the reservoir fiber is strictly excluded.  At \(s=0\), (23) strictly
excludes every remote fiber of color \(j\neq i\).  The halfspace can meet
only the central fiber and the \(2L_k\) remote fibers of color \(i\).
Only the integer levels \(s=-1,0\) contribute to mixed measure, so

\[
\mu_{C_k}(H_{i,x})\leq(A_k+2L_k)v_k=T_k.
\]

Its boundary has zero \(k\)-volume in every face fiber, because there the
boundary is a nontrivial affine hyperplane in \(U_k\); it misses the
reservoir strictly.  Hence there is no boundary convention issue, and in
particular

\[
h_{C_k}(m_k,x)\leq T_k\leq\varepsilon_k a_k^*
\quad\text{for every }x\in(C_k)_{m_k}.
\tag{45}
\]

Now fix any of the legal empty-branch choices quantified in the statement.
We verify directly that the uniform descendant bounds packaged in accepted
fact `51ff186e1aaeaa85` apply to every such legal choice, rather than to one
preferred circuit.  For each \(i\) and \(\zeta\in D_{+,k}\), compactness of
\(D_\zeta\) supplies a support maximizer in \(D_\zeta\).  The minorant
inequality (2b) puts that maximizer in the cap \((G_i)_\zeta\).  Accepted
fact `6769574fc1bd9f8d`, at selected mass
\(a^{(k)}_\zeta/2\), therefore gives

\[
\operatorname{vol}_k((A_i)_\zeta)
\geq\frac{\gamma_k}{2}a^{(k)}_\zeta.
\]

Every weighted average of points of the same fiber lies in that fiber of
\(C_k\), so convexity gives \(B\subseteq C_k\).  Weighted
Brunn--Minkowski applied to the fiber identity
\(B_\zeta=\sum_i\theta_i(A_i)_\zeta\) now gives

\[
B\subseteq C_k,
\qquad
\operatorname{vol}_k(B_\zeta)
\geq\frac{\gamma_k}{2}a^{(k)}_\zeta
\quad(\zeta\in D_{+,k}),
\tag{46}
\]

where

\[
\gamma_k:=\left(\frac{k}{k+1}\right)^k>e^{-1}.
\]

Thus \(\beta=1/(2e)<\gamma_k/2\), and accepted fact
`ca3ef8792d78322a` proves that compatible pairs satisfying (8)--(10) exist
for every such descendant.

Take any compatible pair, not merely one selected by that existence proof.
Every positive lattice fiber has reservoir coordinate \(s=-1\) or \(s=0\).
The \(s\)-components of the two moment identities (10) are zero.  Positivity
therefore forces

\[
\nu_B((C_k)_{r_k})=0,
\qquad
\nu_R((C_k)_{r_k})=0.
\tag{47}
\]

The normalized barycenter of \(\nu_B\) belongs to the compact convex set
\(B\subseteq C_k\), and the normalized barycenter of \(\nu_R\) belongs to
\(C_k\).  Their base coordinates are \(m_k\) by (10).  The same is true of
their convex combination \(y\).  Therefore

\[
y_B,y,y_R\in\{m_k\}\times(C_k)_{m_k}.
\tag{48}
\]

Apply (45) separately to the three points.  This proves (12), uniformly over
all of the choices, and (5) shows that its normalized right side tends to
zero.  Given an asserted universal \(c_{\mathrm{pack}}>0\), taking \(k\)
with \(\varepsilon_k<c_{\mathrm{pack}}\) contradicts the asserted
unconditioned transference bound.

It remains to compute the optimized global core.  Use in (3)--(4) the full
support \(E=D_{+,k}\), the full profile

\[
t_\zeta:=a^{(k)}_\zeta,
\]

and the base point \(m=r_k\).  By (38), the core (3) is

\[
\mathsf M_{V_k}(K_k),
\]

which is the reservoir centroid singleton and is nonempty: since
\(V_k=\operatorname{vol}_k(K_k)\), every admissible density has
\(1-f\geq0\) with integral zero and hence equals \(1\) almost everywhere.
Every proper closed base halfspace containing \(r_k\) has full-profile mass at least
\(V_k>a_k^*=2^{-n_k}W_k\) by (35).  Thus (4) holds and this admissible
profile has total mass \(W_k\).  The definition in accepted fact
`ae0161dd5d4ea672` gives \(G(C_k)\geq W_k\).  Conversely every admissible
profile has \(t_\zeta\leq a^{(k)}_\zeta\), so its total mass is at most
\(W_k\).  This proves (13).

Finally, (26) and (33) give

\[
\frac{V_k}{W_k}
=1-\frac{A_k+2q_k}{2^{q_k+1}(A_k+q_k)}.
\]

Because \(A_k+2q_k<2(A_k+q_k)\),

\[
1-2^{-q_k}<\frac{V_k}{W_k}<1,
\]

which proves (14).  Applying the master bound of accepted fact
`ae0161dd5d4ea672` to (13) yields (15), completing the proof and the exact
scope audit of the counterexample.

## External sources

none
