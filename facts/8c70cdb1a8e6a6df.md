---
fact_id: 8c70cdb1a8e6a6df
kind: counterexample
author: "research-agent"
assurance: LLM-verified
subgoal_id: conditioned-high-load-convex-completion-absorption
depends_on: ["6496cb3b0fd44f9d","6e66cd69e25232b7","c81f02314cb34f8b","fc18c3c4832f0bfb"]
verifier_run: d04a4f8ed76440af
target_match: null
---

## Statement

For every integer \(k\geq16\), put
\[
 Y:=\{0,1\}^k,\qquad N:=2^k,\qquad n:=k+3.
\tag{1}
\]
Regard \(\mathbb R^Y\) as the space of real functions on \(Y\), and set
\[
 U:=\operatorname{span}\{\mathbf1,(y\mapsto y_1),\ldots,(y\mapsto y_k)\},
 \qquad V:=U^\perp,
 \qquad d:=\dim V=N-k-1.
\tag{2}
\]
Let \(P_V\) be orthogonal projection onto \(V\), and, for the coordinate vector \(e_y\in\mathbb R^Y\), put
\[
 u_y:=P_Ve_y,
 \qquad
 \theta:=\|u_y\|=\sqrt{1-\frac{k+1}{N}}.
\tag{3}
\]
Choose \(r_0>0\), let \(B:=r_0B_2^d\subseteq V\), put \(a:=\operatorname{vol}_d(B)\), choose
\[
 L:=2r_0\sqrt N,
 \qquad c_y:=Lu_y,
\tag{4}
\]
and define the common convex body
\[
 C_k:=\operatorname{conv}
 \bigcup_{y\in Y}
 \left([0,14]^3\times\{y\}\times(c_y+B)\right)
 \subseteq\mathbb R^n\times V.
\tag{5}
\]

For every integer base \((x,y)\in\{0,\ldots,14\}^3\times Y\), its actual physical fiber is exactly
\[
 (C_k)_{(x,y)}=c_y+B,
 \qquad a_{(x,y)}=a.
\tag{6}
\]
Every parity class is good for the half-strength product formula of accepted fact `c81f02314cb34f8b`.  If \(X_\xi\subseteq\{0,\ldots,14\}^3\) is one of the eight local parity classes and \(N_\xi:=|X_\xi|\), then the literal half-strength product reservoir is
\[
 r_{\{(x,y),(x',y)\}}
 =\frac{a}{4N_\xi}
 \quad
 (x,x'\in X_\xi,\ x\ne x'),
\tag{7}
\]
and zero on every other pair.  Its mass in one \(y\)-slice and its total mass are
\[
 Q_0=\frac a8\sum_{\xi}(N_\xi-1)
 =\frac{3367a}{8},
 \qquad Q=NQ_0.
\tag{8}
\]

For the exact weighted affine-defect problem of accepted fact `6496cb3b0fd44f9d` on this reservoir, the constant primal map \(s_0=0\) and an explicit dual field are optimal.  Every reservoir edge has full load, so the gauge-load-minimal original optimizer satisfies
\[
 \boxed{\omega_e=r_e\quad(e),\qquad \Omega=Q>\frac{99Q}{100}.}
\tag{9}
\]
In fact the maximum exactly affine-retainable reservoir mass obeys
\[
 \boxed{R_{C_k}(r)\leq\frac{k+4}{N}Q.}
\tag{10}
\]

Use the exact target pooling of accepted fact `fc18c3c4832f0bfb`.  For a physical target \(m=(t,y)\), let
\[
 \Omega_m:=\sum_{e:m_e=m}\omega_e,
 \qquad
 \kappa_m:=\sum_{e:m_e=m}\frac{\omega_e}{a/2},
 \qquad
 \chi_m:=\frac1{\max\{1,\kappa_m\}},
 \qquad
 q_m:=\chi_m\Omega_m.
\tag{11}
\]
Then
\[
 \boxed{\kappa_m\leq2,\qquad \chi_m\geq\frac12,
 \qquad q_m\leq\frac a2}
\tag{12}
\]
for every target.  Consequently the pooled total mass
\[
 \widehat\Omega:=\sum_mq_m
\tag{13}
\]
satisfies
\[
 \boxed{\widehat\Omega\geq\frac Q2>\frac{49Q}{100},}
\tag{14}
\]
and every individual target satisfies the strict hard numerical screen
\[
 \boxed{
 \gamma_d2^nq_m
 \leq\gamma_d2^n\frac a2
 <\frac{32}{3367}Q
 <\frac Q{100}.}
\tag{15}
\]
At the central local target \(t_*=(7,7,7)\), one has \(\kappa_{(t_*,y)}>1\).  Hence the congestion charge
\[
 \beta_e:=(1-\chi_{m_e})\omega_e,
 \qquad B_{\mathrm{cong}}:=\sum_e\beta_e
\tag{16}
\]
is nonzero.  Its fresh load-minimal reoptimization under the same exact weighted dual has
\[
 \boxed{\widetilde\omega_e^{\mathrm{cong}}=\beta_e,
 \qquad
 \widetilde\Omega_{\mathrm{cong}}=B_{\mathrm{cong}}>0.}
\tag{17}
\]

There are actual pooled target densities \(g_m^{\mathrm{pool}}\) and actual fresh endpoint densities \(g_z^{\mathrm{fr}}\), in precisely the ownership normalizations of accepted facts `fc18c3c4832f0bfb` and `6e66cd69e25232b7`, such that every positive density in the \(y\)-slice is supported in \(c_y+B\).  Their slice masses are independent of \(y\).  Write
\[
 M_{\mathrm{pool}}:=\sum_m\int g_m^{\mathrm{pool}}
 =\widehat\Omega,
 \qquad
 M_{\mathrm{fr}}:=\sum_z\int g_z^{\mathrm{fr}}
 =2B_{\mathrm{cong}}>0.
\tag{18}
\]
For either family \(\mathcal F\in\{\mathrm{pool},\mathrm{fr}\}\), let \((b_i,g_i)_{i\in I_{\mathcal F}}\) denote its positive physical bases and densities.  If \(0\leq h_i\leq g_i\) are positive retained subdensities and one affine map \(s\) on the affine hull of their bases satisfies
\[
 s(b_i)=
 \frac{\int xh_i(x)\,dx}{\int h_i}
 \qquad(i),
\tag{19}
\]
then
\[
 \boxed{
 \sum_i\int h_i
 \leq\frac{k+4}{2^k}M_{\mathcal F}.}
\tag{20}
\]
In particular, the maximum source-owned affine-section fraction tends to zero for both actual density families.  For every fixed \(c>0\), all sufficiently large \(k\) violate the conclusion \(\sum_i\int h_i\geq cM_{\mathcal F}\), despite (9), (12), (15), (17), and all the actual common-body, product-reservoir, KKT, pooling, and density-ownership interfaces above.

No claim is made that the other global terminal capacities in the full canonical hard ledger are small for \(C_k\).  The counterexample is exact for the proposed implication from near-full load plus all per-target depth/congestion screens and the listed ownership interfaces.

## Proof

The Walsh functions \(\mathbf1,y\mapsto(-1)^{y_j}\) are pairwise orthogonal on \(Y\).  They span the same space as the functions in (2), so the diagonal of the orthogonal projection onto \(U\) is constantly \((k+1)/N\).  This proves (3).  The same projection identities give
\[
 \sum_{y\in Y}u_y=0,
 \qquad
 \sum_{y\in Y}y_ju_y=0
 \quad(1\leq j\leq k).
\tag{21}
\]

The base projection of (5) is \([0,14]^3\times[0,1]^k\).  Fix a vertex \(y\in Y\) of the second factor.  A supporting functional of \([0,1]^k\) exposes exactly that vertex, so the corresponding exposed face of (5) is
\[
 [0,14]^3\times\{y\}\times(c_y+B).
\]
Therefore every fiber over \((x,y)\), with arbitrary \(x\in[0,14]^3\), is exactly \(c_y+B\).  The integer bases are precisely the points in (6), proving that assertion.

For a local parity vector \(\xi\in\{0,1\}^3\), each coordinate of \(X_\xi\) has either eight even choices or seven odd choices.  Thus
\[
 N_\xi\geq7^3=343>4.
\tag{22}
\]
The full base parity also records \(y\), because each coordinate of \(y\) is zero or one.  Hence a full parity class consists exactly of \(X_\xi\times\{y\}\).  Its total fiber mass is \(N_\xi a\), its largest fiber mass is \(a\), and (22) makes it good.  The product formula of accepted fact `c81f02314cb34f8b` is therefore exactly (7).  A complete graph on \(N_\xi\) vertices contributes
\[
 \binom{N_\xi}{2}\frac a{4N_\xi}
 =\frac{a(N_\xi-1)}8.
\]
Because \(\sum_\xi N_\xi=15^3=3375\), summing over the eight colors and then the \(N\) slices proves (8).

Rotational invariance and affine covariance of the metronoid, together with its full dimensionality in accepted fact `6496cb3b0fd44f9d`, give a number \(\varrho\in(0,r_0)\) such that
\[
 \mathsf M_{a/2}(B)=\varrho B_2^d.
\tag{23}
\]
Here the upper inequality is strict: a positive-mass density in the strictly convex ball cannot have its barycenter on \(\partial B\), because equality in a supporting functional would force that density to be supported on a measure-zero exposed point.
Consequently every source half-metronoid, every centered edge gauge body, and every edge target body in the \(y\)-slice are
\[
 \mathcal K_{(x,y)}=c_y+\varrho B_2^d,
 \qquad
 D_e=\varrho B_2^d,
 \qquad
 L_e=c_y+\varrho B_2^d.
\tag{24}
\]
Since
\[
 L\theta
 =2r_0\sqrt{N-k-1}
 >r_0>\varrho,
\tag{25}
\]
the constant affine map \(s_0=0\) misses every \(L_e\), and its weighted affine defect is
\[
 Q\left(\frac{L\theta}{\varrho}-1\right).
\tag{26}
\]

For a reservoir edge in the \(y\)-slice define
\[
 v_e:=-\frac{r_e}{\varrho\theta}u_y.
\tag{27}
\]
Then \(h_{D_e}(v_e)=r_e\).  Let \(\mathcal E_0\) be the common local edge set in one slice and put
\[
 A_0:=\sum_{e\in\mathcal E_0}r_e(m_e)_{\mathrm{loc}}
 \in\mathbb R^3,
\tag{28}
\]
where \((m_e)_{\mathrm{loc}}\) denotes the first three coordinates.  The local reservoir is identical in every slice, so (21) gives
\[
 \sum_ev_e
 =-\frac{Q_0}{\varrho\theta}\sum_yu_y=0,
\tag{29}
\]
\[
 \sum_ev_em_e^{\mathsf T}
 =-\frac1{\varrho\theta}
 \sum_yu_y(A_0,Q_0y)^{\mathsf T}=0.
\tag{30}
\]
Thus (27) is feasible for the exact weighted dual of accepted fact `6496cb3b0fd44f9d`.  Moreover
\[
 h_{L_e}(v_e)
 =\langle v_e,c_y\rangle+h_{D_e}(v_e)
 =-r_e\left(\frac{L\theta}{\varrho}-1\right).
\tag{31}
\]
The negative dual support sum equals (26), so \(s_0\) and (27) are primal-dual optimizers.  Since \(s_0\) misses every edge, the missed-edge saturation conclusion of `6496cb3b0fd44f9d` forces every load-minimal optimizer paired with \(s_0\) to have \(\omega_e=r_e\).  This proves (9).

We also prove (10), because it isolates the same projection mechanism independently of the dual calculation.  Fix an affine map \(s\), and let \(S\subseteq Y\) be the slices in which it hits at least one target body.  For each \(y\in S\), choose one hit target base \(b_y=(t_y,y)\), with \(t_y\in\mathbb R^3\).  Then
\[
 \|s(b_y)-c_y\|\leq\varrho<r_0.
\tag{32}
\]
If \(|S|>k+4\), the points \(b_y\in\mathbb R^{k+3}\) are affinely dependent.  Choose coefficients \(\alpha_y\), supported on \(S\), with
\[
 \sum_y\alpha_y=0,
 \qquad
 \sum_y\alpha_yt_y=0,
 \qquad
 \sum_y\alpha_yy=0,
 \qquad
 \sum_y\alpha_y^2=1.
\tag{33}
\]
The first and third identities put \(\alpha=(\alpha_y)_{y\in Y}\) in \(V\), so
\[
 \left\|\sum_y\alpha_yc_y\right\|
 =L\|P_V\alpha\|=L.
\tag{34}
\]
The full affine dependence in (33) gives \(\sum_y\alpha_ys(b_y)=0\).  Equations (32)-(34) and Cauchy-Schwarz would then give
\[
 L
 \leq r_0\sum_y|\alpha_y|
 \leq r_0\sqrt{|S|}
 \leq r_0\sqrt N,
\]
contrary to (4).  Hence \(|S|\leq k+4\).  Each slice contains reservoir mass \(Q_0\), so an affine map hits at most \((k+4)Q_0\), proving (10).

The contact selected by (27) is unique because the gauge body is a Euclidean ball.  It is independent of the local edge:
\[
 \ell_y:=c_y-\frac{\varrho}{\theta}u_y
 \in c_y+\varrho B_2^d.
\tag{35}
\]
For equal endpoint volumes, the target root mass of accepted fact `fc18c3c4832f0bfb` is
\[
 \vartheta_e
 =2^{-(d+1)}(2a^{1/d})^d
 =\frac a2.
\tag{36}
\]

Fix a local integer target \(t\in\{0,\ldots,14\}^3\).  In color \(\xi\), reflection about \(t\) is the involution \(x\mapsto2t-x\).  Therefore the number \(c_{\xi,t}\) of unordered distinct reflected pairs in \(X_\xi\) is at most \(N_\xi/2\).  Equations (7), (9), and (36) give
\[
 \kappa_{(t,y)}
 =\sum_\xi\frac{c_{\xi,t}}{2N_\xi}
 \leq\frac84=2.
\tag{37}
\]
Also \(\Omega_{(t,y)}=(a/2)\kappa_{(t,y)}\).  If \(\kappa_{(t,y)}\leq1\), then \(q_{(t,y)}=\Omega_{(t,y)}\leq a/2\); if \(\kappa_{(t,y)}>1\), then \(q_{(t,y)}=\Omega_{(t,y)}/\kappa_{(t,y)}=a/2\).  This proves (12), and summing \(q_m\geq\Omega_m/2\) proves (14).  Finally, using \(2^n=8N\) and (8),
\[
 \frac{\gamma_d2^n(a/2)}Q
 =\gamma_d\frac{32}{3367}
 <\frac1{100},
\tag{38}
\]
which proves (15).

At \(t_*=(7,7,7)\), reflection is \(x\mapsto14\mathbf1-x\).  In each of the seven parity classes other than the all-odd class, there is no fixed point and \(N_\xi\) is even, so \(c_{\xi,t_*}=N_\xi/2\).  The all-odd class has \(N_\xi=7^3=343\), one fixed point, and \(c_{\xi,t_*}=171\).  Hence
\[
 \kappa_{(t_*,y)}
 =\frac74+\frac{171}{686}>1.
\tag{39}
\]
This proves \(B_{\mathrm{cong}}>0\).

We verify the fresh reoptimization rather than infer it from a scalar bound.  The local charge pattern \(\beta_e\) depends only on the local target and is identical in every \(y\)-slice.  Let
\[
 B_0:=\sum_{e\in\mathcal E_0}\beta_e>0,
 \qquad
 A_\beta:=\sum_{e\in\mathcal E_0}\beta_e(m_e)_{\mathrm{loc}}.
\tag{40}
\]
On every charged edge in the \(y\)-slice put
\[
 \widetilde v_e:=-\frac{\beta_e}{\varrho\theta}u_y.
\tag{41}
\]
The same calculation as (29)-(30), with \((Q_0,A_0)\) replaced by \((B_0,A_\beta)\), proves both affine moment cancellations.  Equations (24), (31), and (41) show that the dual constraint is saturated and that its value equals the defect of \(s_0\) for the charged matching.  Thus \(s_0\) and (41) are optimal for the fresh problem.  Since \(s_0\) misses every charged target body, missed-edge saturation again forces the load-minimal fresh loads to equal \(\beta_e\).  This proves (17), including strict positivity.

It remains to verify actual density ownership and the affine-section obstruction.  By (23) and (35), choose one half-metronoid witness \(f_y\) on \(c_y+B\) satisfying
\[
 0\leq f_y\leq1,
 \qquad
 \int f_y=\frac a2,
 \qquad
 \int xf_y(x)\,dx=\frac a2\ell_y.
\tag{42}
\]
At a pooled target \(m=(t,y)\), the exact density in accepted fact `fc18c3c4832f0bfb` may be taken to be
\[
 g_m^{\mathrm{pool}}
 :=\chi_m\kappa_m f_y.
\tag{43}
\]
Equations (11), (36), and (37) show that (43) is pointwise at most one, has mass \(q_m\), and has barycenter \(\ell_y\).  It is supported in the actual target fiber \(c_y+B\).

For a physical fresh source \(z=(x,y)\), put
\[
 d_z^{\mathrm{fr}}:=\sum_{e\ni z}\beta_e.
\tag{44}
\]
The reservoir degree formula from (7) gives
\[
 d_z^{\mathrm{fr}}
 \leq d_z(r)
 =\frac a4\left(1-\frac1{N_\xi}\right)
 <\frac a4.
\tag{45}
\]
The fresh endpoint density may therefore be taken to be
\[
 g_z^{\mathrm{fr}}
 :=\frac{2d_z^{\mathrm{fr}}}{a}f_y.
\tag{46}
\]
It is pointwise less than \(1/2\), has mass \(d_z^{\mathrm{fr}}\), barycenter \(\ell_y\), and support in the actual source fiber \(c_y+B\).  Equations (44)-(46) are exactly the simultaneous endpoint-density ownership of accepted fact `6e66cd69e25232b7`.  Double-counting gives total fresh density mass \(2B_{\mathrm{cong}}\).  Since the local constructions are identical for every \(y\), both the pooled and fresh total masses are equally divided among the \(N\) slices.  This proves (18) and all asserted ownership properties.

We prove (20) once for either family.  All its positive bases have the form
\[
 b_i=(x_i,y),
 \qquad x_i\in\mathbb R^3,\quad y\in Y,
\tag{47}
\]
where \(x_i\) is a local midpoint for the pooled family and a local source for the fresh family.  Every corresponding owner density is supported in \(c_y+B\).  Suppose retained positive subdensities and an affine map satisfy (19).  For every retained index in the \(y\)-slice, write
\[
 s(x_i,y)=c_y+e_i,
 \qquad \|e_i\|\leq r_0.
\tag{48}
\]
Let \(S\subseteq Y\) be the set of slices with positive retained mass.  For \(y\in S\), put \(t_i:=\int h_i\), and average within that slice:
\[
 T_y:=\sum_{i:y_i=y}t_i,
 \qquad
 \bar x_y:=\frac1{T_y}\sum_{i:y_i=y}t_ix_i,
 \qquad
 \bar e_y:=\frac1{T_y}\sum_{i:y_i=y}t_ie_i.
\tag{49}
\]
Then \(\|\bar e_y\|\leq r_0\), and affinity gives
\[
 s(\bar x_y,y)=c_y+\bar e_y.
\tag{50}
\]
If \(|S|>k+4\), the points \((\bar x_y,y)\in\mathbb R^{k+3}\) are affinely dependent.  Choose normalized coefficients as in (33), with \(t_y\) replaced by \(\bar x_y\).  They again satisfy \(\alpha\in V\), while affinity and (50) give
\[
 0=\sum_y\alpha_ys(\bar x_y,y)
 =\sum_y\alpha_yc_y+\sum_y\alpha_y\bar e_y.
\tag{51}
\]
Equations (34), (49), and (51) imply
\[
 L
 \leq r_0\sum_y|\alpha_y|
 \leq r_0\sqrt{|S|}
 \leq r_0\sqrt N,
\]
again contradicting (4).  Therefore \(|S|\leq k+4\).  Each slice owns exactly \(M_{\mathcal F}/N\) of the full family, so the retained mass is at most \((k+4)M_{\mathcal F}/N\).  This is (20).  Since \((k+4)/2^k\to0\), no absolute positive source-owned affine-section fraction follows from the interfaces verified above.

## External sources

none
