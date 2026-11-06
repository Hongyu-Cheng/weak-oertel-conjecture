---
fact_id: ff5bc0ba02cc86cd
kind: lemma
author: "research-agent"
assurance: LLM-verified
subgoal_id: whole-label-reflected-halfspace-domination
depends_on: ["6769574fc1bd9f8d"]
verifier_run: 4f7b2d080a814876
target_match: null
---

## Statement

Let \(n,d\geq1\), let \(C\subseteq\mathbb R^{n+d}\) be a convex body, and write
\[
 C_z:=\{x\in\mathbb R^d:(z,x)\in C\},
 \qquad
 a_z:=\operatorname{vol}_d(C_z)
 \quad(z\in\mathbb Z^n).
\]
Put \(Z_+:=\{z\in\mathbb Z^n:a_z>0\}\) and
\[
 \gamma_d:=\left(\frac d{d+1}\right)^d.
\]
For a positive-volume convex body \(K\subseteq\mathbb R^d\) and
\(0<t\leq\operatorname{vol}_d(K)\), use the metronoid normalization
\[
 \mathsf M_t(K):=
 \left\{
  \frac1t\int_Kx f(x)\,dx:
  f\in L^\infty(K),\ 0\leq f\leq1\ \text{a.e.},\
  \int_Kf(x)\,dx=t
 \right\}.
\]

Let \(\Sigma\) be a finite set of labels.  Give each \(\sigma\in\Sigma\)
a weight \(\eta_\sigma>0\) and two endpoint occurrences
\(u_\sigma,v_\sigma\in Z_+\) such that
\[
 u_\sigma\equiv v_\sigma\pmod 2.
\]
Endpoints may coincide within a label or across different labels.  Count
occurrences, so a loop \(u_\sigma=v_\sigma=y\) contributes
\(2\eta_\sigma\), and suppose that every \(y\in Z_+\) satisfies
\[
 \ell_y:=\sum_{\sigma\in\Sigma}\eta_\sigma
 \bigl(\mathbf1_{\{u_\sigma=y\}}+
       \mathbf1_{\{v_\sigma=y\}}\bigr)
 \leq\frac{a_y}{4}.
 \tag{1}
\]
For each label put
\[
 m_\sigma:=\frac{u_\sigma+v_\sigma}{2}\in\mathbb Z^n,
 \qquad
 K_\sigma:=\frac12\left(
 \mathsf M_{a_{u_\sigma}/2}(C_{u_\sigma})+
 \mathsf M_{a_{v_\sigma}/2}(C_{v_\sigma})
 \right).
 \tag{2}
\]
Then, for every simultaneous choice \(p_\sigma\in K_\sigma\), all points
\((m_\sigma,p_\sigma)\) belong to
\(C\cap(\mathbb Z^n\times\mathbb R^d)\), and the finite atomic measure
\[
 \nu:=\sum_{\sigma\in\Sigma}
 \eta_\sigma\delta_{(m_\sigma,p_\sigma)}
 \tag{3}
\]
obeys
\[
 \boxed{\quad 2\gamma_d\,\nu\preceq_{\mathrm{hs}}\mu_C.\quad}
 \tag{4}
\]
Here
\[
 \mu_C(H):=
 \sum_{z\in\mathbb Z^n}
 \operatorname{vol}_d\{x\in C_z:(z,x)\in H\}
\]
for every closed halfspace \(H\subseteq\mathbb R^{n+d}\), and (4) means
\[
 2\gamma_d\nu(H)\leq\mu_C(H)
 \qquad\text{for every such }H.
 \tag{5}
\]
The conclusion includes coincident labels, midpoint atoms, and continuous
coordinates: their Dirac masses add with multiplicity in (3).  Zero-volume
fibers are never endpoint fibers, although a midpoint fiber may have zero
\(d\)-volume.

The coefficient \(2\gamma_d\) is the largest coefficient furnished solely
by the half-metronoid certificate in accepted fact
`6769574fc1bd9f8d` and the quarter-cap inequality (1): at an oriented endpoint
those two inputs provide respectively \(\gamma_da_y/2\) units of certified
fiber mass and permit \(a_y/4\) units of label load.  This is an exact
accounting assertion, not a claim that no additional geometric hypothesis
could yield a stronger domination coefficient.

## Proof

If \(\Sigma=\varnothing\), every assertion is immediate.  Fix an arbitrary
simultaneous choice in the nonempty case.  By (2), for every label there are
points
\[
 x_{\sigma,u}\in
 \mathsf M_{a_{u_\sigma}/2}(C_{u_\sigma}),
 \qquad
 x_{\sigma,v}\in
 \mathsf M_{a_{v_\sigma}/2}(C_{v_\sigma})
 \tag{6}
\]
such that
\[
 p_\sigma=\frac{x_{\sigma,u}+x_{\sigma,v}}2.
 \tag{7}
\]
Accepted fact `6769574fc1bd9f8d` says, in particular, that every metronoid
appearing in (6) is contained in its underlying fiber body.  Hence
\((u_\sigma,x_{\sigma,u})\) and
\((v_\sigma,x_{\sigma,v})\) belong to \(C\).  Convexity of \(C\), (7),
and the same-parity hypothesis give
\[
 (m_\sigma,p_\sigma)
 =\frac12\bigl((u_\sigma,x_{\sigma,u})+
               (v_\sigma,x_{\sigma,v})\bigr)
 \in C\cap(\mathbb Z^n\times\mathbb R^d).
 \tag{8}
\]
This also proves support membership when several labels produce the same
point.  In particular, (8) can put an atom in a nonempty lower-dimensional
midpoint fiber; no positive midpoint-fiber volume is being assumed.

Let \(H\subseteq\mathbb R^{n+d}\) be a closed halfspace.  It is enough to
consider labels whose atom in (8) lies in \(H\).  For every such label,
if \(H\) is proper, linearity of a defining affine functional for \(H\) and
(8) imply that at least one of its two endpoint points lies in \(H\).  If the
whole space is admitted as an improper closed halfspace, either endpoint may
instead be used.  Choose one such endpoint occurrence.  This remains true
when the atom is on the boundary of \(H\), and for a loop the two occurrences
are still available even though they have the same lattice coordinate.

For \(y\in Z_+\), let \(I_y(H)\) be the set of labels oriented to an
occurrence at \(y\), and put
\[
 t_y(H):=\sum_{\sigma\in I_y(H)}\eta_\sigma.
 \tag{9}
\]
Each label whose atom is in \(H\) is oriented exactly once.  Therefore
\[
 \sum_{y\in Z_+}t_y(H)=\nu(H).
 \tag{10}
\]
Moreover, orientation uses only endpoint occurrences already counted in
\(\ell_y\), even for loops and repeated endpoints, so (1) gives
\[
 t_y(H)\leq\ell_y\leq\frac{a_y}{4}.
 \tag{11}
\]

Suppose \(t_y(H)>0\), and choose any \(\sigma\in I_y(H)\).  The fiber
section
\[
 H_y:=\{x\in\mathbb R^d:(y,x)\in H\}
\]
is a closed halfspace or the whole space, and it contains the chosen endpoint
point from (6).  Applying the halfspace conclusion of accepted fact
`6769574fc1bd9f8d` with mass \(a_y/2\) gives
\[
 \operatorname{vol}_d(C_y\cap H_y)
 \geq\gamma_d\frac{a_y}{2}
 \geq2\gamma_dt_y(H),
 \tag{12}
\]
where the last inequality is exactly (11).  The accepted result explicitly
includes closed halfspaces through the metronoid point and the whole-space
section, so no boundary or improper-halfspace exception is needed.

The endpoint set used in (9) is finite.  Summing (12) over its distinct
lattice fibers, retaining the nonnegative contributions of all other fibers,
and using (10) yields
\[
 \mu_C(H)
 \geq\sum_{y:t_y(H)>0}
       \operatorname{vol}_d(C_y\cap H_y)
 \geq2\gamma_d\sum_y t_y(H)
 =2\gamma_d\nu(H).
 \tag{13}
\]
This proves (4)-(5).  Crucially, the sum in (13) is over original endpoint
fibers, not midpoint fibers.  Thus repeated midpoints, repeated selected
points, and repeated labels create no pooling or collision loss.

Finally, the numerical ratio supplied at a saturated endpoint by the two
stated inputs is
\[
 \frac{\gamma_da_y/2}{a_y/4}=2\gamma_d.
\]
Consequently no larger coefficient follows from those two inequalities alone,
which proves the stated accounting optimality.

## External sources

none
