---
fact_id: f23ff6dd60fbbc37
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: lcr-near-contact-halo-reduction
depends_on: ["07009c5047a9f7bb","3d1f63abf09b2abb","8c92d1d2b1a1b7f5"]
verifier_run: 20c767fbb3244edd
target_match: null
---

## Statement

Let \(n,d\in\mathbb Z_{>0}\), let \(C\subseteq\mathbb R^n\times\mathbb R^d\) be a convex body, and put
\[
 C_z:=\{x\in\mathbb R^d:(z,x)\in C\},\qquad
 a_z:=\operatorname{vol}_d(C_z),\qquad
 Z:=\{z\in\mathbb Z^n:a_z>0\},
\]
\[
 W:=W(C):=\sum_{z\in Z}a_z>0,\qquad
 G:=G(C):=\mathfrak C_{\mathrm{core}}(C).
\]
Assume
\[
 0<G<\frac W2.
\tag{1}
\]

Use the free same-parity matching normalization of accepted fact
`8c92d1d2b1a1b7f5`: a free matching is a nonnegative family \(p=(p_e)\) on unordered pairs \(e=\{z,z'\}\subseteq Z\) with \(z\ne z'\) and \(z\equiv z'\pmod 2\), subject to
\[
 d_z(p):=\sum_{e\ni z}p_e\leq\frac{a_z}{2},
 \qquad |p|:=\sum_ep_e.
\tag{2}
\]
Call \(p\) maximum when \(|p|=\mathfrak M_{\mathrm{free}}(C)\).  For a maximum \(p\), extend
\[
 t_z:=2d_z(p)
\tag{3}
\]
by zero to all \(z\in Z\), put \(E_p:=\{z:t_z>0\}\), and set
\[
 T(p):=\sum_{z\in E_p}t_z=4|p|.
\tag{4}
\]
An integral point \(m\in\mathbb Z^n\cap\operatorname{conv}E_p\) is admissible for \(p\) if every proper closed base halfspace \(J\ni m\) satisfies
\[
 \sum_{z\in E_p\cap J}t_z\geq2^{-n}T(p).
\tag{5}
\]

For a maximum \(p\) and an admissible \(m\), form the degree-saturated core from accepted fact `07009c5047a9f7bb`,
\[
 \mathcal K_m(t):=
 \bigcap_{\lambda\in\Lambda_m(E_p)}
 \sum_{z\in E_p}\lambda_z\mathsf M_{t_z}(C_z).
\tag{6}
\]
Whenever this core is empty, let
\[
 \mathcal Q=(r,(w_i,\theta_i,\ell_i)_{i=1}^r)
\tag{7}
\]
range over all support-minimal balanced negative circuit data furnished by `07009c5047a9f7bb`, including every valid choice of its exact affine minorants.  Thus \(2\leq r\leq d+1\), \(w_i\ne0\), \(\theta_i>0\), and the associated individual cap bodies are
\[
 A_i=A_i(p,m,\mathcal Q)
 :=C\cap\{(z,x):\langle w_i,x\rangle\geq\ell_i(z)\}.
\tag{8}
\]
For every strictly positive probability vector
\(\boldsymbol\vartheta=(\vartheta_1,\ldots,\vartheta_r)\), also include the positive same-base reweighting supplied by that fact, whose fibers are
\[
 (B_{\boldsymbol\vartheta})_z
 =\sum_{i=1}^r\vartheta_i(A_i)_z.
\tag{9}
\]
Define \(\mathscr D(C)\) to be the collection of all individual caps (8) and all positive reweightings (9), jointly over every maximum \(p\), every admissible \(m\) for which (6) is empty, and every circuit datum (7).  Define the descendant-retention capacity precisely by
\[
 R_{\mathrm{desc}}(C)
 :=\sup_{B\in\mathscr D(C)}W(B),
 \qquad W(B):=\sum_{z\in\mathbb Z^n}\operatorname{vol}_d(B_z),
\tag{10}
\]
with the convention that the supremum of an empty collection is zero.  The supremum in (10) is not assumed to be attained.

Then the following conclusions hold.

1.  Saturated maximum matching.  There is a maximum free matching \(p\) for which
\[
 U(p):=\{z\in Z:t_z<a_z\}
\tag{11}
\]
contains at most one point in each parity class and
\[
 t_z=a_z\quad(z\in Z\setminus U(p)),
 \qquad
 \sum_{z\in U(p)}a_z\leq G.
\tag{12}
\]
Consequently
\[
 T(p)\geq W-G>0.
\tag{13}
\]
For every maximum matching, an admissible centerpoint exists; under (1), its degree-saturated core (6) is empty.  In particular, \(\mathscr D(C)\) is nonempty, and saturated maximum matchings may be used in (10).

2.  Dimension-free fiber cap loss.  Let \(K\subseteq\mathbb R^d\) be a convex body of volume \(a>0\) and centroid \(c\).  Put
\[
 \widetilde D:=\mathsf M_{a/2}(K)-c.
\tag{14}
\]
For \(w\ne0\) and \(\ell\leq\langle w,c\rangle\), set
\[
 A:=K\cap\{x:\langle w,x\rangle\geq\ell\},
 \qquad
 \sigma:=\langle w,c\rangle-\ell,
 \qquad
 r:=h_{\widetilde D}(w).
\tag{15}
\]
Then, with \(q:=a-\operatorname{vol}_d(A)\),
\[
 q\leq a\min\left\{1,\frac r\sigma\right\},
\tag{16}
\]
where \(r/\sigma:=+\infty\) when \(\sigma=0\).

3.  Optimized near-contact reduction.  Let \(\mathscr H(C)\) consist of every quadruple \((p,m,\mathcal Q,i)\) in which \(p\) is a saturated maximum matching satisfying (12), \(m\) is admissible, \(\mathcal Q\) is a circuit datum (7), and \(1\leq i\leq r\).  For such a quadruple and \(z\in Z\setminus U(p)\), let \(c_z\) be the centroid of \(C_z\) and define
\[
 \sigma_{i,z}:=\langle w_i,c_z\rangle-\ell_i(z),
 \qquad
 r_{i,z}:=
 h_{\mathsf M_{a_z/2}(C_z)-c_z}(w_i).
\tag{17}
\]
These quantities satisfy \(\sigma_{i,z}\geq0\).  For \(\alpha>1\), define
\[
 N_{p,m,\mathcal Q,i}(\alpha)
 :=\sum_{\substack{z\in Z\setminus U(p)\\
 \sigma_{i,z}\leq\alpha r_{i,z}}}a_z,
\tag{18}
\]
and the optimized near-contact mass
\[
 \mathcal N_\alpha(C)
 :=\inf_{(p,m,\mathcal Q,i)\in\mathscr H(C)}
 N_{p,m,\mathcal Q,i}(\alpha).
\tag{19}
\]
The infimum in (19) is not assumed to be attained.  For every \(\alpha>1\),
\[
 \boxed{
 W(C)-R_{\mathrm{desc}}(C)
 \leq
 G(C)+\mathcal N_\alpha(C)+\frac{W(C)}{\alpha}.}
\tag{20}
\]

4.  Consequences.  Let \((C_k)\) be any sequence satisfying (1), with corresponding \(W_k,G_k,R_{\mathrm{desc}}(C_k)\).  If
\[
 \frac{G_k}{W_k}\longrightarrow0
\tag{21}
\]
and there are \(\alpha_k>1\) such that
\[
 \alpha_k\longrightarrow\infty,
 \qquad
 \frac{\mathcal N_{\alpha_k}(C_k)}{W_k}\longrightarrow0,
\tag{22}
\]
then
\[
 \frac{R_{\mathrm{desc}}(C_k)}{W_k}\longrightarrow1.
\tag{23}
\]
More quantitatively, if \(C_1\geq0\) and
\[
 \mathcal N_{W/G}(C)\leq C_1G,
\tag{24}
\]
then
\[
 W-R_{\mathrm{desc}}(C)\leq(C_1+2)G.
\tag{25}
\]

Conversely, fix \(\eta\in(0,1]\).  If
\[
 R_{\mathrm{desc}}(C)\leq(1-\eta)W,
 \qquad
 G\leq\frac{\eta}{6}W,
\tag{26}
\]
then every \((p,m,\mathcal Q,i)\in\mathscr H(C)\) satisfies
\[
 N_{p,m,\mathcal Q,i}(2/\eta)
 \geq\frac{\eta}{3}W.
\tag{27}
\]
In particular,
\[
 \mathcal N_{2/\eta}(C)\geq\frac{\eta}{3}W.
\tag{28}
\]
Thus a fixed-gap failure of descendant retention with \(G/W\to0\) forces a fixed positive physical mass of saturated fibers to lie within \(2/\eta\) half-metronoid support radii of every individual cap boundary arising from every saturated maximum-matching empty-core circuit.

## Proof

The positive lattice-fiber set \(Z\) is finite because the base projection of the compact body \(C\) is compact.

We first construct the saturated maximum matching.  Fix one parity class \(\omega\), and write
\[
 s_z:=\frac{a_z}{2},\qquad
 S_\omega:=\sum_{z\equiv\omega}s_z.
\]
If \(\max_{z\equiv\omega}s_z\leq S_\omega/2\), the circle construction in accepted fact `8c92d1d2b1a1b7f5` gives a maximum matching in this parity class with
\[
 d_z(p)=s_z=\frac{a_z}{2}
\]
at every vertex.  If instead a unique vertex \(z_*\) satisfies
\(s_{z_*}>S_\omega/2\), pair every other vertex completely with \(z_*\).  The resulting matching has
\[
 d_z(p)=s_z\quad(z\ne z_*),
 \qquad
 d_{z_*}(p)=S_\omega-s_{z_*}<s_{z_*},
\]
and accepted fact `8c92d1d2b1a1b7f5` says that its mass is the exact maximum in this parity class.  This also covers a singleton parity class.  Combining the independent parity-class constructions gives a maximum free matching for which \(U(p)\) has at most one member in each of the \(2^n\) parity classes.

We derive the needed one-fiber estimate directly from accepted fact
`3d1f63abf09b2abb`.  Fix \(z\in Z\), take the rank-zero affine subspace
\(A:=\{z\}\), and use the relative complete metronoid-core capacity
\(G_A^{\mathrm{rel}}\) defined in part (21) of that fact.  The only possible
nonempty index set in its defining supremum is \(\{z\}\), and every admissible
mass is at most \(a_z\), so \(G_A^{\mathrm{rel}}\leq a_z\).  Conversely, take
the index set \(\{z\}\), mass \(t_z=a_z\), and center \(m'=z\).  The full-mass
metronoid is the centroid singleton, so its Minkowski core is nonempty, and a
zero-dimensional affine space has no proper relative closed halfspaces.
Therefore this tuple is admissible and
\[
 G_A^{\mathrm{rel}}=a_z.
\]
For this \(A\), one also has \(r=0\) and \(W_A=a_z\).  Part (22) of accepted
fact `3d1f63abf09b2abb` consequently gives
\[
 G\geq
 \min\left\{
 a_z+\frac{W-a_z}{2},\ 2^na_z
 \right\}
 =\min\left\{\frac{W+a_z}{2},\ 2^na_z\right\}.
\tag{29}
\]
Under \(G<W/2\), the first entry in this minimum is strictly larger than
\(G\).  Hence the second entry is at most \(G\), and thus
\[
 a_z\leq2^{-n}G\qquad(z\in Z).
\tag{30}
\]
Therefore
\[
 \sum_{z\in U(p)}a_z
 \leq2^n\max_{z\in Z}a_z
 \leq G,
\]
which proves (12).  Since \(0\leq t_z\leq a_z\) and equality holds off \(U(p)\),
\[
 W-T(p)=\sum_{z\in U(p)}(a_z-t_z)
 \leq\sum_{z\in U(p)}a_z\leq G.
\]
This proves (13), and in particular \(p\ne0\).

Accepted fact `07009c5047a9f7bb` supplies an admissible integral centerpoint for the selected profile of every nonzero maximum matching.  Moreover, the exact free-capacity lower bound in accepted fact `8c92d1d2b1a1b7f5`, together with (30), gives for every maximum matching
\[
 T(p)=4\mathfrak M_{\mathrm{free}}(C)
 \geq W-\sum_{\omega}\max_{z\equiv\omega}a_z
 \geq W-G>G.
\tag{31}
\]
If its degree-saturated core at any admissible centerpoint were nonempty, the nonempty-core branch of accepted fact `07009c5047a9f7bb` would give \(G\geq T(p)\), contradicting (31).  Thus every such core is empty, the circuit branch applies, and \(\mathscr D(C)\) and \(\mathscr H(C)\) are nonempty.  This proves conclusion 1.

We next prove the dimension-free fiber estimate.  Let \(X\) be uniformly distributed on \(K\), and put
\[
 Y:=\langle w,X-c\rangle.
\]
Then \(\mathbb EY=0\), and the hyperplane \(\{Y=0\}\) has zero \(d\)-dimensional volume.  The complement-density argument in accepted fact `8c92d1d2b1a1b7f5` gives
\[
 \widetilde D=-\widetilde D,
 \qquad
 h_{\widetilde D}(w)=h_{\widetilde D}(-w)=r.
\tag{32}
\]
We claim
\[
 \mathbb E[(-Y)_+]\leq r.
\tag{33}
\]
If \(\mathbb P(Y<0)\geq1/2\), choose a half-probability subset of \(\{Y<0\}\) containing the most negative values of \(Y\).  Its negative first moment is at least half the total negative first moment.  Its normalized barycenter is an element of \(\mathsf M_{a/2}(K)\), so the support function in direction \(-w\) and (32) give (33).  If \(\mathbb P(Y<0)<1/2\), then \(\mathbb P(Y>0)>1/2\).  A half-probability subset containing the most positive values has positive first moment at least half the total positive first moment.  Hence the support function in direction \(w\) is at least \(\mathbb E[Y_+]\).  Since \(\mathbb EY=0\),
\[
 \mathbb E[Y_+]=\mathbb E[(-Y)_+],
\]
and (32) again proves (33).  The indicated half-probability subsets exist by a threshold selection; the uniform measure on the full-dimensional convex body \(K\) is nonatomic.

The discarded-volume ratio is
\[
 \frac qa=\mathbb P(Y<-\sigma).
\]
If \(\sigma>0\), then
\[
 \frac qa\,\sigma
 \leq\mathbb E[(-Y)_+]
 \leq r.
\]
Together with the trivial bound \(q\leq a\), this proves (16).  When \(\sigma=0\), the stated convention reduces (16) to the trivial bound.  This proves conclusion 2.

Fix \((p,m,\mathcal Q,i)\in\mathscr H(C)\).  If \(z\notin U(p)\), then \(t_z=a_z>0\), so \(z\in E_p\), and
\[
 \mathsf M_{t_z}(C_z)=\mathsf M_{a_z}(C_z)=\{c_z\}.
\tag{34}
\]
The exact-minorant inequality in accepted fact `07009c5047a9f7bb` therefore gives
\[
 \ell_i(z)\leq h_{\mathsf M_{t_z}(C_z)}(w_i)
 =\langle w_i,c_z\rangle,
\]
which proves \(\sigma_{i,z}\geq0\).  Apply (16) to the cap fiber \((A_i)_z\) at every such saturated fiber.  On exceptional fibers use only the trivial loss bound.  Equations (12), (16), and (17) yield
\[
 \begin{aligned}
 W-W(A_i)
 &\leq
 \sum_{z\in U(p)}a_z
 +\sum_{z\in Z\setminus U(p)}
 a_z\min\left\{1,\frac{r_{i,z}}{\sigma_{i,z}}\right\}\\
 &\leq
 G+\sum_{z\in Z\setminus U(p)}
 a_z\min\left\{1,\frac{r_{i,z}}{\sigma_{i,z}}\right\},
 \end{aligned}
\tag{35}
\]
with the same zero-slack convention as in (16).

For \(\alpha>1\), the terms in (35) on the near-contact set in (18) are at most \(a_z\).  On its complement one has
\(\sigma_{i,z}>\alpha r_{i,z}\), hence
\(r_{i,z}/\sigma_{i,z}<1/\alpha\).  Therefore
\[
 W-W(A_i)
 \leq G+N_{p,m,\mathcal Q,i}(\alpha)+\frac W\alpha.
\tag{36}
\]

Every \(A_i\) in (36) belongs to \(\mathscr D(C)\), so
\[
 R_{\mathrm{desc}}(C)\geq W(A_i)
\tag{37}
\]
for every quadruple in \(\mathscr H(C)\).  Neither the supremum in (10) nor the infimum in (19) needs to be attained.  Indeed, for every \(\varepsilon>0\), choose a quadruple with
\[
 N_{p,m,\mathcal Q,i}(\alpha)
 \leq\mathcal N_\alpha(C)+\varepsilon.
\]
Combining (36)-(37) and then letting \(\varepsilon\downarrow0\) proves (20).

Dividing (20) by \(W_k\) and using (21)-(22) proves
\[
 1-\frac{R_{\mathrm{desc}}(C_k)}{W_k}\longrightarrow0.
\]
Since every descendant is contained in \(C_k\), the ratio on the left side of (23) is at most one, proving (23).  Under (1), \(W/G>2\), so (20) may be applied with \(\alpha=W/G\).  Hypothesis (24) then gives
\[
 W-R_{\mathrm{desc}}(C)
 \leq G+C_1G+G=(C_1+2)G,
\]
which proves (25).

Finally assume (26), and fix an arbitrary quadruple in \(\mathscr H(C)\).  Since its individual cap belongs to \(\mathscr D(C)\),
\[
 W-W(A_i)\geq W-R_{\mathrm{desc}}(C)\geq\eta W.
\tag{38}
\]
Apply (36) with \(\alpha=2/\eta\).  Equations (26)-(38) give
\[
 \begin{aligned}
 N_{p,m,\mathcal Q,i}(2/\eta)
 &\geq \eta W-G-\frac{\eta}{2}W\\
 &\geq\frac{\eta}{3}W.
 \end{aligned}
\]
Because the quadruple was arbitrary, this proves (27), and taking the infimum proves (28).  All conclusions follow.

## External sources

none
