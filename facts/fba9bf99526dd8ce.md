---
fact_id: fba9bf99526dd8ce
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: rigid-label-local-rank-two-core
depends_on: ["036a276c54ec5e66","084a2e888b32fd2d","10f1feebe06e22d0","3d1f63abf09b2abb","3d9c5784847078c7","54f87dbfba03bb81","7b2a94c842113bf3","8aac56c49321466c","dfd25e72c1f45a4e"]
verifier_run: 31d8c49a7c8c441a
target_match: null
---

## Statement

Assume the canonical hard branch and retain the exact objects and normalizations of accepted facts 036a276c54ec5e66, 084a2e888b32fd2d, 10f1feebe06e22d0, 3d1f63abf09b2abb, 3d9c5784847078c7, 54f87dbfba03bb81, 7b2a94c842113bf3, 8aac56c49321466c, and dfd25e72c1f45a4e. Thus \(n,d\in\mathbb Z_{>0}\), \(C\subseteq\mathbb R^n\times\mathbb R^d\) is a convex body,
\[
C_y:=\{x\in\mathbb R^d:(y,x)\in C\},
\qquad
a_y:=\operatorname{vol}_d(C_y),
\qquad
I_+:=\{y\in\mathbb Z^n:a_y>0\},
\]
\[
W:=\sum_{y\in I_+}a_y,
\qquad
G:=\mathfrak C_{\mathrm{core}}(C),
\]
and the canonical hard reservoir scale \(Q>0\) satisfies
\[
G<\frac Q{100},
\qquad
W\geq8Q.
\tag{1}
\]
For \(y\in I_+\), write
\[
c_y:=\frac1{a_y}\int_{C_y}x\,dx.
\tag{2}
\]
For \(0<t\leq a_y\), use the canonical metronoid
\[
\mathsf M_t(C_y):=
\left\{
\frac1t\int_{C_y}x f(x)\,dx:
0\leq f\leq1\ {\rm a.e.},
\quad
\int_{C_y}f=t
\right\}.
\tag{3}
\]

Retain the minimizing quotient-centroid extension, its centroid-bad family \(\mathscr D_c\), and the simultaneous repair sets \(\mathcal F_\sigma\) of accepted fact 54f87dbfba03bb81. Define the rigid family and its mass by
\[
\mathscr U:=
\{\sigma\in\mathscr D_c:\mathcal F_\sigma=\varnothing\},
\qquad
M_{\mathscr U}:=\sum_{\sigma\in\mathscr U}\eta_\sigma.
\tag{4}
\]
Every \(\sigma\in\mathscr U\) retains its actual transverse-atlas representation
\[
\sigma=(z_\sigma;e(\sigma),f(\sigma)),
\qquad
e(\sigma)=\{z_\sigma,a(\sigma)\},
\qquad
f(\sigma)=\{z_\sigma,b(\sigma)\},
\tag{5}
\]
where \(z_\sigma,a(\sigma),b(\sigma)\) have one common parity, the two half-directions
\[
u_\sigma:=\frac{a(\sigma)-z_\sigma}{2},
\qquad
v_\sigma:=\frac{b(\sigma)-z_\sigma}{2}
\tag{6}
\]
are linearly independent integer vectors, and \(\eta_\sigma>0\) is its rescaled whole-label weight.

Fix \(\sigma\in\mathscr U\), abbreviate
\[
z:=z_\sigma,
\qquad
a:=a(\sigma),
\qquad
b:=b(\sigma),
\qquad
\eta:=\eta_\sigma,
\]
and define
\[
\Delta_\sigma:=\operatorname{conv}\{z,a,b\},
\qquad
L_\sigma:=\operatorname{aff}\{z,a,b\},
\qquad
E_\sigma:=\Delta_\sigma\cap\mathbb Z^n,
\qquad
N_\sigma:=|E_\sigma|.
\tag{7}
\]
Then \(L_\sigma\) is a primitive affine lattice subspace of rank two,
\[
\boxed{N_\sigma\geq6,}
\tag{8}
\]
and there is an affine map
\[
s_\sigma:L_\sigma\longrightarrow\mathbb R^d
\tag{9}
\]
such that every actual lattice fiber in the triangle satisfies
\[
\boxed{
s_\sigma(y)\in\mathsf M_{4\eta_\sigma}(C_y)
\qquad(y\in E_\sigma).}
\tag{10}
\]
In particular, all masses in (10) are strictly positive and feasible.

There exist
\[
m_\sigma\in
L_\sigma\cap\mathbb Z^n\cap\operatorname{conv}E_\sigma,
\qquad
p_\sigma\in\mathbb R^d,
\tag{11}
\]
such that every proper relative closed halfspace \(J_{L_\sigma}\subseteq L_\sigma\) containing \(m_\sigma\) satisfies
\[
\sum_{y\in E_\sigma\cap J_{L_\sigma}}4\eta_\sigma
\geq
\frac14\sum_{y\in E_\sigma}4\eta_\sigma,
\tag{12}
\]
and the same point \(p_\sigma\) belongs to every barycentric Minkowski sum
\[
p_\sigma\in
\sum_{y\in E_\sigma}\lambda_y
\mathsf M_{4\eta_\sigma}(C_y)
\qquad
\left(
\lambda\in\Lambda_{m_\sigma}(E_\sigma)
\right),
\tag{13}
\]
where
\[
\Lambda_{m_\sigma}(E_\sigma):=
\left\{
\lambda\in\mathbb R_+^{E_\sigma}:
\sum_y\lambda_y=1,
\quad
\sum_y\lambda_yy=m_\sigma
\right\}.
\tag{14}
\]
Thus (11)-(13) are one actual primitive rank-two relative complete-metronoid-core tuple of exact mass
\[
\boxed{
\tau_\sigma:=4N_\sigma\eta_\sigma\geq24\eta_\sigma.}
\tag{15}
\]

Every such label satisfies the stronger lattice-point-weight screen
\[
\boxed{
N_\sigma\eta_\sigma
<\frac{Q}{100\,2^n},}
\tag{16}
\]
and therefore
\[
\boxed{
\eta_\sigma<\frac{Q}{600\,2^n}.}
\tag{17}
\]
Consequently,
\[
\boxed{
M_{\mathscr U}>\frac Q{4000}
\quad\Longrightarrow\quad
|\mathscr U|>\frac3{20}\,2^n.}
\tag{18}
\]

Finally, for every physical integer base \(y\), define the total rigid-triangle vertex load
\[
\lambda_y^\triangle:=
\sum_{\substack{\sigma\in\mathscr U\\
y\in\{z_\sigma,a(\sigma),b(\sigma)\}}}
\eta_\sigma.
\tag{19}
\]
Then the exact shared-vertex ownership and capacity identities are
\[
\boxed{
0\leq\lambda_y^\triangle\leq\frac{a_y}{4}
\qquad(y\in\mathbb Z^n),}
\tag{20}
\]
\[
\boxed{
\sum_{y\in\mathbb Z^n}\lambda_y^\triangle
=3M_{\mathscr U}.}
\tag{21}
\]
Equations (10)-(21) do not aggregate the local tuples, add their masses, align the maps \(s_\sigma\), or assert a global complete core.

## Proof

Fix \(\sigma\in\mathscr U\) and use the abbreviations following (6). Accepted fact 036a276c54ec5e66 constructs every atlas label from a positive transverse pair of upstream edges. Therefore \(u_\sigma,v_\sigma\in\mathbb Z^n\) are linearly independent. In particular \(n\geq2\), \(z,a,b\) are distinct, and \(L_\sigma=z+V_\sigma\), where
\[
V_\sigma:=\operatorname{span}_{\mathbb R}\{u_\sigma,v_\sigma\}.
\tag{22}
\]
The group \(V_\sigma\cap\mathbb Z^n\) has rank two because it contains the two linearly independent integer vectors \(u_\sigma,v_\sigma\), and it is saturated: if \(q\in\mathbb Z^n\) and \(kq\in V_\sigma\) for one \(k\in\mathbb Z_{>0}\), then \(q=k^{-1}(kq)\in V_\sigma\). Hence \(L_\sigma\) is primitive of rank two.

The six coefficient pairs
\[
(0,0),\quad(1,0),\quad(0,1),\quad
(1,1),\quad(2,0),\quad(0,2)
\]
are distinct. Linear independence of \(u_\sigma,v_\sigma\) therefore makes the six lattice points
\[
z,\quad z+u_\sigma,\quad z+v_\sigma,\quad
z+u_\sigma+v_\sigma,\quad
z+2u_\sigma=a,\quad z+2v_\sigma=b
\tag{23}
\]
pairwise distinct. They all lie in
\[
z+2\operatorname{conv}\{0,u_\sigma,v_\sigma\}
=\Delta_\sigma.
\]
This proves (8).

We next audit the three vertex masses. Accepted fact 54f87dbfba03bb81 gives the opposite-endpoint capacities
\[
\eta\leq\frac{a_a}{4},
\qquad
\eta\leq\frac{a_b}{4}.
\tag{24}
\]
For every upstream edge \(j\), accepted fact 084a2e888b32fd2d gives
\[
\sum_{\substack{\rho\in\mathscr A_{\mathrm{int}}\\
j\in\{e(\rho),f(\rho)\}}}
\eta_\rho
\leq\omega_j.
\tag{25}
\]
Applying (25) to \(e(\sigma)\), or to \(f(\sigma)\), gives
\[
\eta\leq\omega_{e(\sigma)},
\qquad
\eta\leq\omega_{f(\sigma)}.
\tag{26}
\]
The quarter-degree source budget in accepted fact 7b2a94c842113bf3 gives
\[
\sum_{j\ni z}\omega_j\leq\frac{a_z}{4}.
\tag{27}
\]
Equations (24), (26), and (27) prove
\[
0<4\eta\leq a_y
\qquad(y\in\{z,a,b\}).
\tag{28}
\]

For each of these three vertices, the density
\[
f_y:=\frac{4\eta}{a_y}\mathbf1_{C_y}
\tag{29}
\]
lies between zero and one, has mass \(4\eta\), and has normalized barycenter \(c_y\). Thus
\[
c_y\in\mathsf M_{4\eta}(C_y)
\qquad(y\in\{z,a,b\}).
\tag{30}
\]
Because \(z,a,b\) are affinely independent, there is a unique affine map \(s_\sigma:L_\sigma\to\mathbb R^d\) satisfying
\[
s_\sigma(z)=c_z,
\qquad
s_\sigma(a)=c_a,
\qquad
s_\sigma(b)=c_b.
\tag{31}
\]

Let \(y\in E_\sigma\), and let
\[
y=\theta_0z+\theta_1a+\theta_2b,
\qquad
\theta_i\geq0,
\qquad
\theta_0+\theta_1+\theta_2=1
\tag{32}
\]
be its unique barycentric representation in the triangle. Equations (30) say that the three positive-mass root triples
\[
\left(z,c_z,(4\eta)^{1/d}\right),
\quad
\left(a,c_a,(4\eta)^{1/d}\right),
\quad
\left(b,c_b,(4\eta)^{1/d}\right)
\tag{33}
\]
belong to the positive root-metronoid set of accepted fact dfd25e72c1f45a4e. Its positive-mass convexity, applied to (32)-(33), gives
\[
\left(
y,
\theta_0c_z+\theta_1c_a+\theta_2c_b,
(4\eta)^{1/d}
\right)
\]
in the same set. By (31), its middle coordinate is \(s_\sigma(y)\). Therefore
\[
s_\sigma(y)\in\mathsf M_{4\eta}(C_y).
\tag{34}
\]
This proves (10) for every lattice point in \(E_\sigma\), including vertices and boundary points. The root coordinate is strictly positive, so no zero-mass convention or closure point is involved. The triangle is compact, so \(E_\sigma\) is finite.

Apply accepted fact 10f1feebe06e22d0 to the primitive rank-two space \(L_\sigma\), the finite nonempty support \(E_\sigma\), the constant positive feasible masses \(t_y=4\eta\), and the affine map \(s_\sigma\). It gives \(m_\sigma,p_\sigma\) satisfying (11)-(14). The total mass is exactly
\[
\sum_{y\in E_\sigma}4\eta
=4N_\sigma\eta,
\]
and (8) gives the last inequality in (15). This proves the local relative complete-core assertion with actual fibers and one common point for every barycentric representation.

It remains to prove the hard screen, including both possible ambient base dimensions. If \(n=2\), the rank-two affine space \(L_\sigma\) equals \(\mathbb R^2\). The full-rank conclusion of accepted fact 10f1feebe06e22d0 therefore gives
\[
G\geq\tau_\sigma=4N_\sigma\eta_\sigma.
\tag{35}
\]
Combining (35) with (1) gives
\[
N_\sigma\eta_\sigma
<\frac{Q}{400}
=\frac{Q}{100\,2^n},
\]
which is (16) when \(n=2\).

Now suppose \(n>2\), so \(L_\sigma\subsetneq\mathbb R^n\), and put
\[
W_{L_\sigma}:=
\sum_{y\in I_+\cap L_\sigma}a_y.
\tag{36}
\]
The slice \(I_+\cap L_\sigma\) contains the three affinely independent bases \(z,a,b\), so its affine hull is exactly \(L_\sigma\) and has rank two. Apply the support-free rank-two slice theorem of accepted fact 8aac56c49321466c with its affine subspace \(A=L_\sigma\). It gives
\[
G\geq\frac1{64}
\min\{W,2^{n-2}W_{L_\sigma}\}.
\tag{37}
\]
By (1), equation (37) forces
\[
\min\{W,2^{n-2}W_{L_\sigma}\}
<\frac{16}{25}Q.
\tag{38}
\]
Since \(W\geq8Q>16Q/25\), the second entry is the small one:
\[
2^{n-2}W_{L_\sigma}<\frac{16}{25}Q.
\tag{39}
\]
Because \(n\geq3\), equations (1) and (39) give
\[
\frac{W-W_{L_\sigma}}2
>
\frac12\left(8-\frac8{25}\right)Q
=\frac{96}{25}Q
>\frac Q{100}.
\tag{40}
\]

For completeness, apply the exact relative-to-global augmentation of accepted fact 3d1f63abf09b2abb to the actual tuple (11)-(15). That theorem chooses an affine functional vanishing on \(L_\sigma\) and nonzero on \(I_+\setminus L_\sigma\). If \(H_*\) denotes the larger total fiber volume on its two strict sides, then
\[
H_*\geq\frac{W-W_{L_\sigma}}2
\tag{41}
\]
and the tuple's relative \(1/4\) balance gives
\[
G\geq
\min\{\tau_\sigma+H_*,2^{n-2}\tau_\sigma\}.
\tag{42}
\]
The first entry in (42) is greater than \(Q/100\) by (40)-(41), whereas \(G<Q/100\). Hence the second entry must be strictly less than \(Q/100\):
\[
2^{n-2}\tau_\sigma
=2^{n-2}\,4N_\sigma\eta_\sigma
<\frac Q{100}.
\tag{43}
\]
Dividing (43) by \(2^n\) proves (16) for \(n>2\). Thus (16) holds in all cases. Combining it with \(N_\sigma\geq6\) proves (17).

If \(M_{\mathscr U}>Q/4000\), then \(\mathscr U\) is nonempty and finite. Summing the strict pointwise bound (17) gives
\[
\frac Q{4000}
<M_{\mathscr U}
<|\mathscr U|\frac{Q}{600\,2^n}.
\]
Cancellation of \(Q>0\) proves (18).

We finish with the shared-vertex ownership audit. Fix a physical integer base \(y\). If \(y\) is an opposite endpoint of a rigid label, exactly one of that label's two upstream edges is incident to \(y\). If \(y=z_\sigma\) is its common source, both upstream edges are incident to \(y\). Therefore
\[
\lambda_y^\triangle
\leq
\sum_{j\ni y}
\sum_{\substack{\rho\in\mathscr A_{\mathrm{int}}\\
j\in\{e(\rho),f(\rho)\}}}
\eta_\rho.
\tag{44}
\]
The inner sum includes all internal labels, not merely the rigid ones, so no omitted label can invalidate the upper bound. Equations (25) and (27), now at the fixed base \(y\), give
\[
\lambda_y^\triangle
\leq\sum_{j\ni y}\omega_j
\leq\frac{a_y}{4}
\tag{45}
\]
whenever \(\lambda_y^\triangle>0\). If \(\lambda_y^\triangle=0\), (20) is immediate, including when \(a_y=0\). Thus (20) holds for every integer base and includes labels sharing a physical vertex.

Finally, transversality makes \(z_\sigma,a(\sigma),b(\sigma)\) three distinct bases for every label. Each \(\eta_\sigma\) is therefore counted exactly three times when (19) is summed over \(y\). The atlas and \(\mathscr U\) are finite, so the sums may be interchanged, giving
\[
\sum_y\lambda_y^\triangle
=\sum_{\sigma\in\mathscr U}3\eta_\sigma
=3M_{\mathscr U}.
\]
This proves (21). No step combines the supports \(E_\sigma\), the points \(p_\sigma\), or the affine maps \(s_\sigma\); the theorem proves only the stated local tuples and the shared vertex ledger.

## External sources

none
