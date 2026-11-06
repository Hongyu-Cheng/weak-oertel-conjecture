---
fact_id: 9b6e82cf5f0fa2cc
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: intake13-three-layer-h2-equivalence
depends_on: ["2f0204d9d167faa7","e02045d859c5d115"]
verifier_run: 3fa814269ad44b20
target_match: null
---

## Statement

For a finite probability law \(q\) in \(\mathbb R^m\), write

\[
\tau_q(x)=\inf_{\substack{H\subseteq\mathbb R^m\text{ a closed halfspace}\\x\in H}}q(H),
\qquad
M_2(q)=\sum_xq_x\tau_q(x)^2,
\qquad
\Phi_m(q)=4^mM_2(q).
\tag{1}
\]

Fix \(\kappa>0\).  Let \((\mathrm H_\kappa)\) denote the assertion that

\[
\Phi_m(q)\geq\kappa
\tag{2}
\]

for every integer \(m\geq1\) and every complete log-affine law \(q\) on \(A=Q\cap\mathbb Z^m\), where \(Q\subseteq\mathbb R^m\) is compact and convex and \(A\ne\varnothing\).  In the notation of accepted fact 2f0204d9d167faa7, this is exactly (H2) with \(a^2=\kappa\).

Let \((\mathrm T_\kappa^{\mathrm{amb}})\) denote the following three-layer assertion.  For every integer \(N\geq2\), every compact convex \(P\subseteq\mathbb R^N\) whose nonempty finite lattice support

\[
D=P\cap\mathbb Z^N\subseteq\{0,1,2\}\times\mathbb Z^{N-1}
\]

meets all three layers, and every common log-affine probability law \(p\) on \(D\), put

\[
\begin{aligned}
D_i&=\{y\in\mathbb Z^{N-1}:(i,y)\in D\},
&\alpha_i&=\sum_{y\in D_i}p_{(i,y)},
&p_i(y)&=\frac{p_{(i,y)}}{\alpha_i},\\
\psi_i^{\mathrm{amb}}&=4^{N-1}M_2(p_i)
&&&(i&=0,1,2),
\end{aligned}
\tag{3}
\]

where the depths defining \(M_2(p_i)\) are taken in the ambient slice space \(\mathbb R^{N-1}\), whether or not \(D_i\) has affine rank \(N-1\).  Then

\[
\Phi_N(p)\geq
\min\{\kappa,\psi_0^{\mathrm{amb}},\psi_1^{\mathrm{amb}},\psi_2^{\mathrm{amb}}\}.
\tag{4}
\]

For every \(\kappa>0\), assertions \((\mathrm H_\kappa)\) and \((\mathrm T_\kappa^{\mathrm{amb}})\) are equivalent.

More precisely, let \(q\) be any law occurring in \((\mathrm H_\kappa)\), write

\[
q_x=\frac{e^{\theta\cdot x}}{\sum_{z\in A}e^{\theta\cdot z}},
\qquad v=\Phi_m(q)>0,
\tag{5}
\]

and fix an integer \(k\geq3\).  For \(b\in\{0,1\}^k\), let \(\epsilon(b)\in\{0,1\}\) be the parity of \(\sum_jb_j\), and define

\[
\begin{aligned}
\mathcal V_k={}&\{(0,b):\epsilon(b)=0\}\\
&\cup\{(1,b):b\in\{0,1\}^k\setminus\{0\}\}\\
&\cup\{(2,b):\epsilon(b)=1\},
\qquad R_k=\operatorname{conv}\mathcal V_k.
\end{aligned}
\tag{6}
\]

Then

\[
R_k\cap\mathbb Z^{k+1}=\mathcal V_k,
\tag{7}
\]

every member of \(\mathcal V_k\) is an exposed vertex of \(R_k\), and the label sets in each of the three layers affinely span \(\mathbb R^k\).  Their cardinalities and the total cardinality are

\[
n_0=n_2=2^{k-1},
\qquad n_1=2^k-1,
\qquad L_k=|\mathcal V_k|=2^{k+1}-1.
\tag{8}
\]

On

\[
P^{(k)}=R_k\times Q,
\qquad
D^{(k)}=P^{(k)}\cap\mathbb Z^{m+k+1}=\mathcal V_k\times A,
\tag{9}
\]

define the single common log-affine law

\[
p^{(k)}_{(t,b,x)}=\frac{q_x}{L_k}.
\tag{10}
\]

With \(N=m+k+1\), its exact pointwise depths, conditional depths, layer masses, moments, and ambiently normalized moments are

\[
\begin{aligned}
\tau_{p^{(k)}}(t,b,x)&=\frac{\tau_q(x)}{L_k},
&\tau_{p_i^{(k)}}(b,x)&=\frac{\tau_q(x)}{n_i},
&\alpha_i&=\frac{n_i}{L_k},\\
\tau_{p^{(k)}}(i,b,x)&=\alpha_i\tau_{p_i^{(k)}}(b,x),
&M_2(p^{(k)})&=\frac{M_2(q)}{L_k^2},
&M_2(p_i^{(k)})&=\frac{M_2(q)}{n_i^2},\\
\Phi_N(p^{(k)})&=a_kv,
&\psi_0^{\mathrm{amb}}=\psi_2^{\mathrm{amb}}&=4v,
&\psi_1^{\mathrm{amb}}&=b_kv,
\end{aligned}
\tag{11}
\]

where

\[
a_k=\left(\frac{2^{k+1}}{2^{k+1}-1}\right)^2,
\qquad
b_k=\left(\frac{2^k}{2^k-1}\right)^2,
\qquad
1<a_k<b_k<4,
\qquad a_k\longrightarrow1.
\tag{12}
\]

In particular, if the additional middle-layer term is defined by

\[
E(p)=4^N\alpha_1\sum_{y\in D_1}p_1(y)
\left(\tau_p(1,y)^2-\alpha_1^2\tau_{p_1}(y)^2\right),
\tag{13}
\]

then \(E(p^{(k)})=0\), and in fact equality with the conditional contribution holds pointwise in every layer.  Equivalently,

\[
\Phi_N(p^{(k)})
=4\sum_{i=0}^2\alpha_i^3\psi_i^{\mathrm{amb}}.
\tag{14}
\]

If \(\operatorname{aff}A\) has dimension \(m\), then \(D^{(k)}\) has affine dimension \(N\), while each layer has affine dimension \(N-1\).  Let \((\mathrm T_\kappa^{\mathrm{fd},0})\) be (4) restricted to precisely the subclass with full-dimensional support, three full-dimensional slices, and \(E(p)=0\).  Then, for every \(\kappa>0\),

\[
(\mathrm H_\kappa)
\quad\Longleftrightarrow\quad
(\mathrm T_\kappa^{\mathrm{fd},0})
\quad\Longleftrightarrow\quad
(\mathrm T_\kappa^{\mathrm{amb}}).
\tag{15}
\]

Consequently all three assertions have the same best constant

\[
\mathfrak c=
\inf_{\substack{m\geq1\\q\text{ complete log-affine in }\mathbb R^m}}
\Phi_m(q),
\qquad 0\leq\mathfrak c\leq\frac13.
\tag{16}
\]

For every fixed \(\kappa>1/3\), there is a uniform law \(p^{(k)}\) from (6)--(10) whose support and slices are full-dimensional, for which \(E(p^{(k)})=0\) and

\[
\Phi_N(p^{(k)})<
\min\{\kappa,\psi_0^{\mathrm{amb}},\psi_1^{\mathrm{amb}},\psi_2^{\mathrm{amb}}\}.
\tag{17}
\]

The theorem uses the ambient normalization in (3).  If \(r_i=\dim\operatorname{aff}D_i\), the different intrinsic normalization in the open three-layer subgoal is

\[
\psi_i^{\mathrm{int}}=4^{r_i}M_2(p_i),
\qquad
\psi_i^{\mathrm{amb}}=4^{N-1-r_i}\psi_i^{\mathrm{int}}.
\tag{18}
\]

No fixed-\(1/4\) inequality with the intrinsic quantities is asserted here.  On the embedding after passage to intrinsic coordinates all slices have \(r_i=N-1\), so the two normalizations coincide there; thus that open intrinsic-rank assertion would still contain unrestricted \((\mathrm H_{1/4})\).  The positivity statement \(\mathfrak c>0\), and hence existential (H2), remains unproved.

## Proof

First prove (7).  The last \(k\) coordinates of \(R_k\) lie in \([0,1]^k\).  Hence an integer point of \(R_k\) has a Boolean last-coordinate vector \(b\).  If a convex combination of Boolean vectors equals the Boolean vertex \(b\), then every vector with positive coefficient equals \(b\): this follows coordinate by coordinate, since an average of zeros and ones can equal an endpoint only when every term equals that endpoint.  Therefore the vertical section of \(R_k\) over \(b\) is the convex hull of exactly the heights paired with \(b\) in (6).  It is \(\{0\}\) for \(b=0\), \([0,1]\) for nonzero even \(b\), and \([1,2]\) for odd \(b\).  Its integer points are exactly the listed endpoints.  This proves (7), including the exceptional missing point \((1,0)\).

For exposedness, fix \(b\in\{0,1\}^k\) and set

\[
\chi_b(c)=\sum_{j=1}^k(2b_j-1)(c_j-b_j).
\tag{19}
\]

On Boolean vectors, \(\chi_b(b)=0\), while \(\chi_b(c)\leq-1\) for \(c\ne b\).  Given \((t,b)\in\mathcal V_k\), take \(\delta=1\) if \(t\) is the upper endpoint of its vertical section and \(\delta=-1\) if it is the lower endpoint; either sign may be used for the singleton section.  The affine functional

\[
F_{t,b}(s,c)=3\chi_b(c)+\delta(s-t)
\tag{20}
\]

vanishes at \((t,b)\).  At the other endpoint over the same \(b\), if there is one, it equals \(-1\).  At every label with \(c\ne b\), its first term is at most \(-3\), while \(|s-t|\leq2\), so it is strictly negative.  Thus (20) uniquely exposes \((t,b)\).

There are \(2^{k-1}\) Boolean vectors of each parity, which gives (8).  For \(k\geq3\), the even vectors affinely span \(\mathbb R^k\): they contain \(0\) and every \(e_i+e_j\), and for distinct \(i,j,\ell\),

\[
e_i=\frac12\bigl((e_i+e_j)+(e_i+e_\ell)-(e_j+e_\ell)\bigr).
\tag{21}
\]

Flipping one Boolean coordinate is an invertible affine map from the even class onto the odd class, so the odd vectors also affinely span \(\mathbb R^k\).  Finally, \(\{0,1\}^k\setminus\{0\}\) contains \(e_1,\ldots,e_k\) and \(e_1+e_2\); the first \(k\) points have affine hull \(\{x:\sum_jx_j=1\}\), and the last point lies outside it.  Hence the middle label set also affinely spans \(\mathbb R^k\).  A full \(k\)-dimensional layer and any label at a different height show \(\dim R_k=k+1\).

The product identity in (9) follows directly from (7) and \(Q\cap\mathbb Z^m=A\).  Equation (10) is normalized because there are \(L_k\) labels above every \(x\), and it is the restriction of the one common exponential affine weight

\[
(t,b,x)\longmapsto e^{\theta\cdot x};
\tag{22}
\]

there is no independent layer reweighting.  Also
\(\operatorname{conv}(\mathcal V_k\times A)=R_k\times\operatorname{conv}A\), and in layer \(i\) the support hull is the product of the corresponding label hull with \(\operatorname{conv}A\).  The dimension assertions therefore follow from the affine-span calculation above whenever \(\dim\operatorname{aff}A=m\).

We next prove the depth identities rather than infer them from the product form.  Let a finite product law on \(V\times A\) have masses \(r_uq_x\), and suppose \(u\) is exposed in \(\operatorname{conv}V\).  For any ambient closed halfspace containing \((u,x)\), its restriction to the fiber \(\{u\}\times\mathbb R^m\) is a closed halfspace containing \(x\), or the whole fiber.  Its mass from that fiber is therefore at least \(r_u\tau_q(x)\), proving

\[
\tau_{r\otimes q}(u,x)\geq r_u\tau_q(x).
\tag{23}
\]

For the reverse inequality, the depth of a point in a finite law is attained: only finitely many subsets of the support can occur as halfspace intersections, and the mass is constant on each such subset.  Choose an affine inequality \(g(z)\geq0\) attaining \(\tau_q(x)\).  Choose an affine exposing function \(f\) with \(f(u)=0\) and \(f(w)<0\) at every other label.  Since the support is finite, for all sufficiently large \(M\),

\[
g(z)+Mf(w)\geq0
\tag{24}
\]

cuts out the chosen \(q\)-halfspace on the \(u\)-fiber and excludes every supported point on every other fiber.  It is a closed ambient halfspace containing \((u,x)\), of mass \(r_u\tau_q(x)\).  Together with (23), this proves

\[
\tau_{r\otimes q}(u,x)=r_u\tau_q(x).
\tag{25}
\]

Every whole-table label in (6) is exposed by (20), so (25) with \(r_u=1/L_k\) proves the first formula in (11).  Within a fixed layer, (19) exposes every one of its Boolean labels from the other labels in that layer.  Its conditional label law is uniform with mass \(1/n_i\), so a second application of (25) proves the conditional-depth formula.  The layer-mass and pointwise equality formulas in (11) follow at once.

Summing one probability factor and two depth factors gives

\[
\begin{aligned}
M_2(p^{(k)})
&=\sum_{(t,b)\in\mathcal V_k}\sum_{x\in A}
\frac{q_x}{L_k}\left(\frac{\tau_q(x)}{L_k}\right)^2
=\frac{M_2(q)}{L_k^2},\\
M_2(p_i^{(k)})
&=\sum_{b\text{ in layer }i}\sum_{x\in A}
\frac{q_x}{n_i}\left(\frac{\tau_q(x)}{n_i}\right)^2
=\frac{M_2(q)}{n_i^2}.
\end{aligned}
\tag{26}
\]

Here the factor \(L_k\), respectively \(n_i\), comes from summing over labels.  Since \(N=m+k+1\), multiplying (26) by \(4^N\), respectively by the prescribed ambient slice factor \(4^{N-1}=4^{m+k}\), yields

\[
\Phi_N(p^{(k)})
=\frac{4^{k+1}}{L_k^2}\Phi_m(q),
\qquad
\psi_i^{\mathrm{amb}}
=\frac{4^k}{n_i^2}\Phi_m(q).
\tag{27}
\]

Substitution from (8) proves the last line of (11) and (12).  Indeed \(x/(x-1)\) is strictly decreasing for \(x>1\), so \(a_k<b_k\), and both tend to one in the indicated square-root parametrization.  Pointwise equality in (11) makes every summand in (13) zero and also proves (14).

We now prove the equivalence.  If \((\mathrm H_\kappa)\) holds, then every admissible three-layer \(p\) is itself a complete log-affine law in dimension \(N\), so \(\Phi_N(p)\geq\kappa\).  This immediately implies (4), and hence also its restriction \((\mathrm T_\kappa^{\mathrm{fd},0})\).

Conversely, suppose first that \((\mathrm T_\kappa^{\mathrm{amb}})\) holds and take an arbitrary \(q\) in dimension \(m\).  Apply (4) to \(p^{(k)}\).  Equations (11)--(12) give

\[
a_kv\geq\min\{\kappa,4v,b_kv,4v\}
=\min\{\kappa,b_kv\}.
\tag{28}
\]

Because \(a_kv<b_kv\), (28) forces \(a_kv\geq\kappa\): if \(a_kv<\kappa\), both entries in the last minimum would be strictly larger than its left side.  Letting \(k\to\infty\) gives \(v\geq\kappa\).  Since \(q\) was arbitrary, \((\mathrm H_\kappa)\) follows.

It remains to justify that the full-dimensional zero-gain restriction has exactly the same force, including for lower-rank input laws.  First establish the universal \(1/3\) calibration.  For an integer \(s\geq1\), let \(q_s\) be uniform on \(\{0,\ldots,2s-1\}\subset\mathbb Z\).  Closed halfspaces in one dimension are closed rays, so

\[
\tau_{q_s}(j)=\frac{\min\{j+1,2s-j\}}{2s}.
\tag{29}
\]

Each integer \(h\in\{1,\ldots,s\}\) occurs twice among the numerators in (29).  Therefore

\[
\Phi_1(q_s)
=\frac1{s^3}\sum_{h=1}^sh^2
=\frac{(s+1)(2s+1)}{6s^2}
\longrightarrow\frac13.
\tag{30}
\]

These \(q_s\) are full-dimensional complete uniform laws.  For any \(\kappa>1/3\), choose \(s\) with \(v_s:=\Phi_1(q_s)<\kappa\), then choose \(k\geq3\) so large that \(a_kv_s<\kappa\).  The resulting \(p^{(k)}\) is uniform, full-dimensional, has three full-dimensional slices and \(E=0\).  Moreover \(a_k<b_k<4\), so

\[
a_kv_s<\kappa,
\qquad a_kv_s<b_kv_s,
\qquad a_kv_s<4v_s.
\tag{31}
\]

Equations (11) turn (31) into the strict violation (17).  Thus \((\mathrm T_\kappa^{\mathrm{fd},0})\) can hold only when \(\kappa\leq1/3\).

Now assume \((\mathrm T_\kappa^{\mathrm{fd},0})\) and take an arbitrary complete log-affine law \(q\) in ambient dimension \(m\).  If its support has affine rank \(r\geq1\), accepted fact e02045d859c5d115 supplies coordinates in the full affine lattice of the support in which \(q\) becomes a full-dimensional complete log-affine law \(q'\) in dimension \(r\), its halfspace depths and \(M_2\) are unchanged, and

\[
\Phi_m(q)=4^{m-r}\Phi_r(q').
\tag{32}
\]

Apply the construction to \(q'\), now with \(N=r+k+1\).  The resulting table lies in the restricted class, so the already proved argument (28) gives \(\Phi_r(q')\geq\kappa\).  Equation (32) then gives \(\Phi_m(q)\geq\kappa\).  If the support has rank zero, it is a singleton, its depth and \(M_2\) equal one, and \(\Phi_m(q)=4^m\geq4>1/3\geq\kappa\), where the calibration above supplied the last bound on \(\kappa\).  Hence \((\mathrm T_\kappa^{\mathrm{fd},0})\) implies \((\mathrm H_\kappa)\), completing (15).

For a class of nonnegative numbers, the largest universal lower bound is its infimum.  The equivalences just proved therefore give the common value (16), and (30) gives \(\mathfrak c\leq1/3\).  Equation (18) is the definition of the two normalizations together with invariance of depth and \(M_2\) under intrinsic affine-lattice coordinates.  In the full-dimensional construction based on \(q'\), every slice has rank \(N-1\), so the equality of the two normalizations there and the final hardness statement follow.  Nothing in the argument proves \(\mathfrak c>0\) or any particular positive lower bound.

## External sources

None.  The parity support, completeness, exposedness, affine dimensions, product-depth identity, exact moment identities, zero-gain property, equivalence, and uniform \(1/3\) calibration are proved here.  Accepted fact 2f0204d9d167faa7 is used only to identify the exact unrestricted (H2) normalization.  Accepted fact e02045d859c5d115 supplies the already verified intrinsic affine-lattice coordinate reduction, including completeness, log-affinity, depth preservation, and the normalized-moment relation (32).  No claim from the archived source is taken as a premise.
