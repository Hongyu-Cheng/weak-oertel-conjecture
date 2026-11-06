---
fact_id: daef2580cdfec07b
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: n2-unconditional-level-simplex-depth
depends_on: ["314b32bda8a0b01e","4bd2e6d22487dfef","4e868f774de77608","62f2ec156b347dfe","758103b1282d6b91","b220933817d23295"]
verifier_run: abee9124c07d490f
target_match: null
---

## Statement

Put
\[
c_0:=\frac1{64e},
\qquad
\gamma_d:=\left(\frac d{d+1}\right)^d.
\]

First let \(d\in\mathbb Z_{>0}\), let \(C\subseteq\mathbb R^2\times\mathbb R^d\) be a convex body, and define
\[
C_z:=\{x\in\mathbb R^d:(z,x)\in C\},
\qquad
w_z:=\operatorname{vol}_d(C_z),
\qquad
W:=\sum_{z\in\mathbb Z^2}w_z>0,
\]
\[
S:=C\cap(\mathbb Z^2\times\mathbb R^d).
\]
For \((z,x)\in C\), let
\[
\delta_C(z,x):=
\inf\{\operatorname{vol}_d(C_z\cap J):
J\subseteq\mathbb R^d\text{ is a proper closed halfspace and }x\in J\},
\]
and, for \(z\in\operatorname{proj}_{\mathbb R^2}C\), put
\[
M(z):=\max_{x\in C_z}\delta_C(z,x),
\]
with \(M(z):=0\) off the projection.  For \(p\in S\), set
\[
h_S(p):=
\inf_{\substack{H\subseteq\mathbb R^{2+d}\text{ a closed halfspace}\\p\in H}}
\sum_{z\in\mathbb Z^2}\operatorname{vol}_d(C_z\cap H_z),
\qquad
H_z:=\{x:(z,x)\in H\}.
\]
Then there exists \(p\in S\) such that
\[
h_S(p)
\geq \frac1{256}\sum_{z\in\mathbb Z^2}M(z)
\geq \frac{\gamma_d}{256}W.
\tag{1}
\]
In particular, since \(\gamma_d>1/e\),
\[
h_S(p)>\frac1{256e}W=c_0\,2^{-2}W,
\tag{2}
\]
so the locked weak Oertel assertion holds for every \(n=2\) instance with the absolute constant \(c_0\in(0,1/e)\).

Second, let \(n>2\), let \(d\in\mathbb Z_{>0}\), let \(C\subseteq\mathbb R^n\times\mathbb R^d\) be a convex body, and define \(C_z,w_z,W,S,h_S\) analogously, with \(W>0\).  Let \(1\leq r\leq n\), let \(L\leq\mathbb Z^n\) be a primitive sublattice of rank \(n-r\), let \(a\in\mathbb Z^n\), and put
\[
A:=a+\operatorname{span}_{\mathbb R}L,
\qquad
W_A:=\sum_{z\in A\cap\mathbb Z^n}w_z.
\]
Assume
\[
W_A\geq2^{-r}W.
\tag{3}
\]
Let
\[
D_+:=\{z\in A\cap\mathbb Z^n:w_z>0\},
\qquad
q:=\dim\operatorname{aff}(D_+),
\]
and assume \(q\leq2\).  Then \(q+r\leq n\), and there exists \(p\in S\) such that
\[
h_S(p)\geq c_0\,2^{-n}W.
\tag{4}
\]
This conclusion includes, with separate proofs below, each of the intrinsic-rank cases \(q=2\), \(q=1\), and \(q=0\).

## Proof

All sums over integer fibers below are finite because the relevant convex bodies are compact.

1. The max-depth root profile and one concentrated level.

Let \(P:=\operatorname{proj}_{\mathbb R^2}C\), and write
\[
f(z,x):=\delta_C(z,x)^{1/d},
\qquad
\rho(z):=M(z)^{1/d}.
\]
Allowing all of \(\mathbb R^d\) among the competitors defining \(\delta_C\) does not change the infimum, so the convention here agrees with accepted fact \(4e868f774de77608\).  That fact gives all of the following: every maximum defining \(M(z)\) is attained; \(f\) is jointly concave on \(C\); \(\rho\) is concave and upper semicontinuous on the compact convex set \(P\); and \(M(z)=0\) whenever \(w_z=0\).

Accepted fact \(4bd2e6d22487dfef\), assertion 1, gives the graph-economical comparison
\[
\sum_{z\in\mathbb Z^2}M(z)
\geq\gamma_d\sum_{z\in\mathbb Z^2}w_z
=\gamma_dW>0.
\tag{5}
\]
Apply accepted fact \(62f2ec156b347dfe\) with integer dimension two, exponent \(d\), compact domain \(P\), and concave function \(\rho\).  It supplies a number \(t>0\), attained at a positive lattice value of \(\rho\), such that, for
\[
K:=\{z\in P:\rho(z)\geq t\},
\qquad
D:=K\cap\mathbb Z^2,
\qquad
N:=|D|,
\]
one has
\[
t^dN\geq2^{-3}\sum_{z\in P\cap\mathbb Z^2}\rho(z)^d
=\frac18\sum_{z\in\mathbb Z^2}M(z).
\tag{6}
\]
Here \(D\neq\varnothing\).  Concavity and upper semicontinuity of \(\rho\) make \(K\) compact and convex, so \(D\) is exactly the finite lattice-point set of a planar compact convex set.  Thus no strict-versus-nonstrict level issue occurs.

2. Planar lattice-simplex extraction with the factor \(1/8\).

We prove the following statement used on \(D\): if \(K_0\subseteq\mathbb R^2\) is convex and \(D_0:=K_0\cap\mathbb Z^2\) is finite and nonempty, then there is a lattice simplex \(T\subseteq\operatorname{conv}(D_0)\) of affine dimension \(q\in\{0,1,2\}\) such that
\[
|T\cap\mathbb Z^2|\geq\frac18|D_0|.
\tag{7}
\]
If \(D_0\) has affine dimension zero or one, take \(T=\operatorname{conv}(D_0)\).  It is respectively a lattice point or a lattice segment, and convexity gives
\[
T\cap\mathbb Z^2=D_0,
\tag{8}
\]
so there is no loss in these two cases.

Suppose now that \(D_0\) has affine dimension two, and put \(P_0:=\operatorname{conv}(D_0)\).  Since \(P_0\subseteq K_0\), again
\[
P_0\cap\mathbb Z^2=D_0.
\tag{9}
\]
The polygon \(P_0\) is a nondegenerate lattice polygon.  Choose a maximum-area triangle contained in \(P_0\) whose vertices are vertices of \(P_0\), and call it
\[
T=\operatorname{conv}\{v_0,v_1,v_2\}.
\]
Such a triangle is maximum among all triangles contained in \(P_0\).  Indeed, triangle area is continuous on \(P_0^3\), so a maximum exists.  With two vertices fixed, the area is the absolute value of an affine functional of the third vertex, hence its maximum over the polygon is attained at a vertex.  Replacing the three vertices successively gives a maximizing triple of vertices.  Since every vertex of \(P_0\) belongs to \(D_0\), \(T\) is a lattice triangle.

For \(x\in P_0\), let \(\lambda_0(x),\lambda_1(x),\lambda_2(x)\) be its barycentric coordinates relative to \(T\).  Replacing \(v_i\) by \(x\) produces a triangle contained in \(P_0\) whose area is \(|\lambda_i(x)|\operatorname{area}(T)\).  Maximality of \(T\) therefore gives
\[
|\lambda_i(x)|\leq1
\qquad(x\in P_0,\ i=0,1,2).
\tag{10}
\]
In the affine coordinates \((\lambda_0,\lambda_1)\), with \(\lambda_2=1-\lambda_0-\lambda_1\), the region cut out by (10) is
\[
[-1,1]^2\cap\{0\leq\lambda_0+\lambda_1\leq2\}.
\]
It has area \(2\), whereas the standard barycentric triangle \(\lambda_i\geq0\) has area \(1/2\).  The same affine Jacobian converts both coordinate areas to Euclidean areas.  Hence
\[
\operatorname{area}(P_0)\leq4\operatorname{area}(T).
\tag{11}
\]

We use Pick's formula in its exact form: for a simple lattice polygon \(Q\), if \(I_Q\) and \(B_Q\) are the numbers of lattice points in its interior and on its boundary, then
\[
\operatorname{area}(Q)=I_Q+\frac{B_Q}{2}-1.
\tag{12}
\]
Let \(m:=|P_0\cap\mathbb Z^2|\).  Since \(m=I_{P_0}+B_{P_0}\) and \(B_{P_0}\leq m\), (12) gives
\[
\operatorname{area}(P_0)
=m-\frac{B_{P_0}}2-1
\geq\frac{m-2}{2}.
\tag{13}
\]
Applying (12) also to the lattice triangle \(T\) gives
\[
|T\cap\mathbb Z^2|
=\operatorname{area}(T)+\frac{B_T}{2}+1
\geq\operatorname{area}(T)+1.
\tag{14}
\]
Combining (11), (13), and (14),
\[
|T\cap\mathbb Z^2|
\geq\frac{m-2}{8}+1
=\frac{m+6}{8}
\geq\frac m8.
\tag{15}
\]
This proves (7) in all three ranks.  Apply it to the set \(D\) from part 1.  From now on let
\[
F:=\operatorname{aff}(T),
\qquad
q:=\dim F,
\qquad
D_T:=T\cap\mathbb Z^2.
\]
Then
\[
|D_T|\geq\frac N8,
\tag{16}
\]
and when \(q\leq1\) one in fact has \(|D_T|=N\).

3. A fixed level gives one ambient mixed-depth point, with intrinsic ranks audited separately.

Write the vertices of \(T\) as \(v_0,\ldots,v_q\).  For every \(i\), accepted fact \(4e868f774de77608\) supplies a depth maximizer \(x_i\in C_{v_i}\) such that
\[
\delta_C(v_i,x_i)=M(v_i)\geq t^d.
\tag{17}
\]
Let \(s:F\to\mathbb R^d\) be the affine interpolation satisfying \(s(v_i)=x_i\).  If \(z=\sum_i\lambda_iv_i\in T\), where \(\lambda_i\geq0\) and \(\sum_i\lambda_i=1\), convexity of \(C\) first gives \((z,s(z))\in C\), and the joint concavity of \(f=\delta_C^{1/d}\) from the same accepted fact gives
\[
\delta_C(z,s(z))^{1/d}
\geq\sum_i\lambda_i\delta_C(v_i,x_i)^{1/d}
\geq t.
\tag{18}
\]
Thus the selector uses actual depth maximizers at the vertices, not fiber centroids, and
\[
\delta_C(z,s(z))\geq t^d
\qquad(z\in T).
\tag{19}
\]

Rank \(q=0\).  Here \(T=D_T=\{v_0\}\).  Put \(p:=(v_0,x_0)\).  For any ambient closed halfspace \(H\) containing \(p\), the fiber section \(H_{v_0}\) is either a proper closed halfspace containing \(x_0\) or all of \(\mathbb R^d\).  In the first case the definition of \(\delta_C\) applies; in the second, \(w_{v_0}\geq\delta_C(v_0,x_0)\).  Hence
\[
\sum_{z\in\mathbb Z^2}\operatorname{vol}_d(C_z\cap H_z)
\geq\operatorname{vol}_d(C_{v_0}\cap H_{v_0})
\geq t^d
=2^{-q}t^d|D_T|.
\tag{20}
\]
This also covers a closed halfspace whose boundary contains the whole fiber and loses no boundary mass.

Ranks \(q=1,2\).  Fix \(z_0:=v_0\), and define
\[
\Gamma:=(F-z_0)\cap\mathbb Z^2.
\]
The lattice differences of the vertices span \(F-z_0\), so \(\Gamma\) is a full lattice of rank \(q\).  Choose a \(\mathbb Z\)-basis \(g_1,\ldots,g_q\) of \(\Gamma\), put
\[
Uu:=\sum_{i=1}^qu_ig_i,
\qquad
\Phi(u,x):=(z_0+Uu,x),
\]
and define the restricted body in intrinsic coordinates by
\[
\widehat C:=
\{(u,x)\in\mathbb R^q\times\mathbb R^d:
z_0+Uu\in T,\ (z_0+Uu,x)\in C\}.
\tag{21}
\]
The map \(\Phi\) is an affine bijection from \(\mathbb R^q\times\mathbb R^d\) onto \(F\times\mathbb R^d\), and it maps \(\mathbb Z^q\times\mathbb R^d\) onto \((F\cap\mathbb Z^2)\times\mathbb R^d\).

The set \(\widehat C\) is a convex body in \(\mathbb R^{q+d}\).  Compactness and convexity are immediate.  For full dimensionality, let \(u_i\in\mathbb Z^q\) be the coordinate of \(v_i\).  Equation (17) implies that every vertex fiber has positive \(d\)-volume.  Choose \(a\) in the interior of the fiber over \(u_0\), choose \(a_i\) in the fiber over \(u_i\) for \(1\leq i\leq q\), and choose \(\varepsilon>0\) such that \(a+\varepsilon e_j\) remains in the fiber over \(u_0\) for \(1\leq j\leq d\).  The \(q+d\) differences from \((u_0,a)\) to
\[
(u_i,a_i)\ (1\leq i\leq q),
\qquad
(u_0,a+\varepsilon e_j)\ (1\leq j\leq d)
\]
are linearly independent: their horizontal coordinates first kill the coefficients of the first \(q\) vectors, and their vertical coordinates then kill the rest.  Hence \(\widehat C\) contains a \((q+d)\)-simplex.

The integer positive-mass base support of \(\widehat C\) is exactly
\[
E:=\{u\in\mathbb Z^q:z_0+Uu\in D_T\}.
\tag{22}
\]
Indeed, fibers outside \(T\) are empty, while (19) makes every fiber indexed by \(D_T\) positive-volume.  The affine selector
\[
\widehat s(u):=s(z_0+Uu)
\]
lies in the corresponding fiber for every \(u\in E\), and that fiber is exactly \(C_{z_0+Uu}\).  Therefore its absolute fiber depth in \(\widehat C\) equals its depth in \(C\), and (19) yields
\[
\widehat\Delta
:=\sum_{u\in E}\delta_{\widehat C}(u,\widehat s(u))
\geq t^d|E|
=t^d|D_T|>0.
\tag{23}
\]

Apply accepted fact \(b220933817d23295\) to the convex body \(\widehat C\), integer dimension \(q\), and affine selector \(\widehat s\).  It gives \(u^\star\in E\) such that, with
\[
\widehat p:=(u^\star,\widehat s(u^\star)),
\]
every closed halfspace \(J\subseteq\mathbb R^{q+d}\) containing \(\widehat p\) has restricted mixed volume at least
\[
2^{-q}\widehat\Delta
\geq2^{-q}t^d|D_T|.
\tag{24}
\]

Put \(p:=\Phi(\widehat p)\in S\).  Let \(H\subseteq\mathbb R^{2+d}\) be any closed halfspace containing \(p\).  The pullback
\[
J:=\Phi^{-1}\bigl(H\cap(F\times\mathbb R^d)\bigr)
\tag{25}
\]
is a closed halfspace in \(\mathbb R^{q+d}\) or all of that space; it cannot be empty because it contains \(\widehat p\).  In the whole-space case, (24) is immediate from \(\widehat\Delta\leq\sum_{u\in E}\operatorname{vol}_d(\widehat C_u)\); in the proper case, (24) applies directly.  Because \(\Phi\) is the identity on the continuous coordinate, it preserves every \(d\)-dimensional fiber volume exactly.  Thus
\[
\begin{aligned}
\sum_{z\in\mathbb Z^2}\operatorname{vol}_d(C_z\cap H_z)
&\geq
\sum_{z\in D_T}\operatorname{vol}_d(C_z\cap H_z)\\
&=
\sum_{u\in\mathbb Z^q}\operatorname{vol}_d(\widehat C_u\cap J_u)\\
&\geq2^{-q}t^d|D_T|.
\end{aligned}
\tag{26}
\]
All equalities use closed sections, so boundary mass is retained.  Any nonempty zero-volume fibers of the ambient body outside \(D_T\) contribute zero or a nonnegative amount and cannot weaken the first inequality.  This completes the intrinsic-chart and ambient-transfer audit for ranks one and two.

Combining (20) and (26), in every rank \(q\in\{0,1,2\}\) there is \(p\in S\) satisfying
\[
h_S(p)
\geq2^{-q}t^d|D_T|
\geq\frac14t^d\frac N8
=\frac1{32}t^dN.
\tag{27}
\]
Together with (6), this gives the strong aggregate estimate
\[
h_S(p)
\geq\frac1{256}\sum_{z\in\mathbb Z^2}M(z).
\tag{28}
\]
Combining (28) with (5) proves (1).  Finally,
\[
d\log\left(1+\frac1d\right)<1
\]
implies \(\gamma_d=(1+1/d)^{-d}>e^{-1}\).  This proves (2), and \(0<c_0<1/e\) is immediate.

4. Direct primitive-slice corollary in ranks two, one, and zero.

We now prove the second assertion, reproducing the coordinate reduction and volume audit from accepted fact \(314b32bda8a0b01e\) rather than invoking only its conditional weak-Oertel conclusion.  Primitivity gives
\[
A\cap\mathbb Z^n=a+L.
\tag{29}
\]
By (3), \(W_A>0\), so \(D_+\) is nonempty.  Put
\[
B:=\operatorname{aff}(D_+).
\]
Since \(B\subseteq A\),
\[
0\leq q\leq n-r,
\qquad
q+r\leq n.
\tag{30}
\]
Every lattice fiber indexed by \((A\cap\mathbb Z^n)\setminus B\) has zero \(d\)-volume, because every positive-mass base point is in \(D_+\subseteq B\).  Hence
\[
W_A=\sum_{z\in B\cap\mathbb Z^n}w_z.
\tag{31}
\]

Choose affinely independent \(z_0,\ldots,z_q\in D_+\), with only \(z_0\) when \(q=0\), and define
\[
\Gamma_B:=(B-z_0)\cap\mathbb Z^n.
\]
The differences \(z_i-z_0\) show that \(\Gamma_B\) is a full rank-\(q\) lattice in \(B-z_0\).  Choose a \(\mathbb Z\)-basis \(g_1,\ldots,g_q\), with the empty basis for \(q=0\), and set
\[
U_Bu:=\sum_{i=1}^qu_ig_i,
\qquad
\Psi(u,x):=(z_0+U_Bu,x).
\tag{32}
\]
Then
\[
\Psi(\mathbb Z^q\times\mathbb R^d)
=(B\cap\mathbb Z^n)\times\mathbb R^d.
\tag{33}
\]
Define
\[
C':=\Psi^{-1}\bigl(C\cap(B\times\mathbb R^d)\bigr).
\tag{34}
\]

The set \(C'\) is a convex body in \(\mathbb R^{q+d}\).  To check the only nonautomatic point, full dimensionality, choose an interior point of the positive-volume fiber \(C_{z_0}\), take \(d\) sufficiently small independent vertical perturbations in that fiber, and take one point in each positive-volume fiber \(C_{z_i}\), \(1\leq i\leq q\).  Subtracting the first point gives \(d\) independent vertical vectors and \(q\) vectors with independent horizontal components, hence \(q+d\) independent vectors in \(C\cap(B\times\mathbb R^d)\).  The affine bijection \(\Psi\) preserves this dimension.

Moreover, \(\Psi\) is the identity on the continuous coordinate in each fiber.  It therefore preserves \(d\)-dimensional fiber volume exactly, even though no claim about \((q+d)\)-dimensional Jacobians is needed.  Equations (31) and (33) give
\[
\mathcal H_d\bigl(C'\cap(\mathbb Z^q\times\mathbb R^d)\bigr)
=W_A.
\tag{35}
\]

We now obtain a point \(p'\) of the required restricted depth, separately in all three values of \(q\).

If \(q=2\), apply the first part of this theorem to \(C'\).  There is \(p'\in C'\cap(\mathbb Z^2\times\mathbb R^d)\) with
\[
h_{C'\cap(\mathbb Z^2\times\mathbb R^d)}(p')
\geq\frac{\gamma_d}{256}W_A
>\frac1{256e}W_A
=c_0\,2^{-2}W_A.
\tag{36}
\]

If \(q=1\), accepted fact \(758103b1282d6b91\) gives \(p'\in C'\cap(\mathbb Z\times\mathbb R^d)\) with restricted depth at least
\[
\alpha_dW_A,
\qquad
\alpha_d:=\frac12\left[
\gamma_d-(1-\gamma_d)\log\frac1{1-\gamma_d}
\right].
\tag{37}
\]
For completeness, this accepted constant is much stronger than the one needed here.  Define
\[
Q(u):=u+(1-u)\log(1-u).
\]
Then \(Q(0)=0\) and \(Q'(u)=-\log(1-u)\geq u\) for \(0\leq u<1\).  Consequently
\[
\alpha_d=\frac12Q(\gamma_d)
\geq\frac14\gamma_d^2
>\frac1{4e^2}
>\frac1{128e}
=c_0\,2^{-1},
\tag{38}
\]
where the penultimate inequality only uses \(e<32\).  Thus the same restricted lower bound \(c_0\,2^{-q}W_A\) holds in rank one.

If \(q=0\), the body \(C'\) is the positive-volume fiber \(C_{z_0}\subseteq\mathbb R^d\).  Let \(p'\) be its centroid.  Grünbaum's centroid halfspace inequality gives, for every closed halfspace \(J\subseteq\mathbb R^d\) containing \(p'\),
\[
\operatorname{vol}_d(C'\cap J)
\geq\gamma_d\operatorname{vol}_d(C')
=\gamma_dW_A
>c_0W_A
=c_0\,2^{-q}W_A.
\tag{39}
\]
This is the required fiber-centroid argument in intrinsic rank zero.

Thus in every case \(q=0,1,2\), there is \(p'\in C'\cap(\mathbb Z^q\times\mathbb R^d)\) such that every proper closed halfspace in \(\mathbb R^{q+d}\) containing \(p'\) has restricted mixed volume at least
\[
c_0\,2^{-q}W_A.
\tag{40}
\]
Put \(p:=\Psi(p')\in S\).  For any ambient closed halfspace \(H\subseteq\mathbb R^{n+d}\) containing \(p\), the pullback
\[
J:=\Psi^{-1}\bigl(H\cap(B\times\mathbb R^d)\bigr)
\tag{41}
\]
is a proper closed halfspace or all of \(\mathbb R^{q+d}\), and it contains \(p'\).  If it is proper, (40) applies.  If it is the whole space, its restricted mixed volume is \(W_A\geq c_0\,2^{-q}W_A\).  Fiberwise volume preservation, followed by the zero-volume observation before (31), gives
\[
\begin{aligned}
\sum_{z\in\mathbb Z^n}\operatorname{vol}_d(C_z\cap H_z)
&\geq
\sum_{z\in B\cap\mathbb Z^n}\operatorname{vol}_d(C_z\cap H_z)\\
&=
\sum_{u\in\mathbb Z^q}\operatorname{vol}_d(C'_u\cap J_u)\\
&\geq c_0\,2^{-q}W_A\\
&\geq c_0\,2^{-(q+r)}W\\
&\geq c_0\,2^{-n}W.
\end{aligned}
\tag{42}
\]
The fourth line uses (3), and the last uses (30).  Fibers in \((A\cap\mathbb Z^n)\setminus B\) have zero volume even after intersection with \(H\), while fibers outside the slice contribute nonnegatively.  Hence (42) is an exact ambient transfer, including zero-volume boundary fibers and closed-halfspace boundary mass.  Taking the infimum over all such \(H\) proves (4).

## External sources

Georg Pick, "Geometrisches zur Zahlenlehre," Sitzungsberichte des deutschen naturwissenschaftlich-medicinischen Vereines für Böhmen "Lotos" in Prag, Neue Folge 19 (also catalogued as volume 47) (1899), 311-319, primary-source scan https://www.zobodat.at/pdf/Lotos_47_0311-0319.pdf.  Exact form used: if \(Q\) is a simple polygon in \(\mathbb R^2\) whose vertices lie in \(\mathbb Z^2\), and \(I_Q\) and \(B_Q\) denote its interior and boundary lattice-point counts, then \(\operatorname{area}(Q)=I_Q+B_Q/2-1\).  Applicability: in the only use above, \(P_0\) is a nondegenerate convex lattice polygon because it is the convex hull of a finite rank-two subset of \(\mathbb Z^2\), and \(T\) is a nondegenerate lattice triangle.  Both are simple lattice polygons, and all lattice-point counts in (13)-(15) include boundary points exactly.

Branko Grünbaum, "Partitions of Mass-Distributions and of Convex Bodies by Hyperplanes," Pacific Journal of Mathematics 10(4) (1960), 1257-1261, Theorem 2 and its proof in Section 3, pages 1259-1260, https://doi.org/10.2140/pjm.1960.10.1257, primary-source PDF https://msp.org/pjm/1960/10-4/pjm-v10-n4-p18-p.pdf.  Exact form used: if \(K\subseteq\mathbb R^d\) is a \(d\)-dimensional convex body with centroid \(c(K)\), then every closed halfspace \(J\subseteq\mathbb R^d\) containing \(c(K)\) satisfies \(\operatorname{vol}_d(K\cap J)\geq(d/(d+1))^d\operatorname{vol}_d(K)\).  Applicability: the theorem is invoked directly only in the \(q=0\) rank-drop branch, where (35) gives \(\operatorname{vol}_d(C')=W_A>0\), so \(C'\) is a \(d\)-dimensional convex body, \(p'\) is its centroid, and every proper pullback in (41) is a closed halfspace containing it.  The whole-space pullback is handled separately.  The max-depth aggregate comparison (5) is supplied by accepted fact \(4bd2e6d22487dfef\), rather than by a new external invocation.
