---
fact_id: a8cfba4caf85ff82
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: oblique-cap-purification
depends_on: []
verifier_run: 315a135e89e2468a
target_match: null
---

## Statement

Let \(n,d\in\mathbb Z_{>0}\), let \(C\subseteq\mathbb R^{n+d}\) be a convex body, and put
\[
 C_z:=\{x\in\mathbb R^d:(z,x)\in C\},\qquad
 \mu_C(E):=\sum_{z\in\mathbb Z^n}\int_{C_z}{\bf1}_E(z,x)\,dx,
 \qquad W:=\mu_C(C)>0.
\]
For \(0<a\le W\), define \(\mathsf M_a(C)\) to be the set of all points
\[
 \frac1a\int_C p\,g(p)\,d\mu_C(p),
 \qquad 0\le g\le1,\qquad \int_Cg\,d\mu_C=a,
\]
where \(g\) is Borel measurable.  Suppose that
\[
 y=(z_0,x_0)\in\mathsf M_a(C),\qquad z_0\in\mathbb Z^n,
\]
and let
\[
 H=\{p\in\mathbb R^{n+d}:\ell(p)\le\ell(y)\}
\]
be a closed halfspace through \(y\).  Write \(\ell(z,x)=\alpha\cdot z+\beta\cdot x\), and assume \(\beta\ne0\).  Then there are \(\lambda\in\mathbb R^n\) and \(\eta\in\mathbb R\) such that the convex cap
\[
 G:=\{(z,x):\ell(z,x)+\lambda\cdot(z-z_0)\le\eta\},
 \qquad A:=C\cap G
\]
satisfies, with \(A_z:=\{x:(z,x)\in A\}\),
\[
 \mu_C(A)=a,
 \qquad \frac1a\sum_{z\in\mathbb Z^n}z\,\operatorname{vol}_d(A_z)=z_0,
 \qquad \overline y_A:=\frac1a\int_Ap\,d\mu_C(p)\in H.
\]
In fact \(\overline y_A\in A\cap(\mathbb Z^n\times\mathbb R^d)\).  If \(\mu_A(E):=\mu_C(A\cap E)\), then in particular \(\mu_C(H)\ge\mu_A(H)\).

There is also the following precise vertical existential corollary.  Let
\[
 H_0:=\{(z,x):L(z)\le L(z_0)\}
\]
be any vertical closed halfspace through \(y\), with \(L:\mathbb R^n\to\mathbb R\) a nonzero linear functional.  For every \(u\in\mathbb R^d\setminus\{0\}\) and every \(\varepsilon>0\), there are \(\lambda_\varepsilon\in\mathbb R^n\), \(\eta_\varepsilon\in\mathbb R\), and
\[
 A_\varepsilon=C\cap\{(z,x):L(z)+\varepsilon u\cdot x+
 \lambda_\varepsilon\cdot(z-z_0)\le\eta_\varepsilon\}
\]
such that \(\mu_C(A_\varepsilon)=a\), the base coordinate of its mixed centroid is \(z_0\), and, on writing that centroid as \((z_0,\overline x_\varepsilon)\),
\[
 u\cdot\overline x_\varepsilon\le u\cdot x_0,
 \qquad (z_0,\overline x_\varepsilon)\in\partial H_0\subseteq H_0.
\]
This cap is linked to the perturbed nonvertical functional \((z,x)\mapsto L(z)+\varepsilon u\cdot x\), not to the original vertical functional \(L\).  No vertical KKT-cap representation and no limiting assertion as \(\varepsilon\downarrow0\) are claimed.

## Proof

Only finitely many lattice fibers of the compact set \(C\) are nonempty.  Put
\[
 D:=\{z\in\mathbb Z^n:w_z:=\operatorname{vol}_d(C_z)>0\}.
\]
Every fiber outside \(D\) is null for \(\mu_C\) and hence has no effect on any mass, moment, or barycenter below.  For \(z\in D\), the compact convex set \(C_z\) has positive \(d\)-volume and is therefore full dimensional in \(\mathbb R^d\).

We first prove the needed one-fiber lower-tail statement from first principles.  Fix \(z\in D\), write
\[
 f_z(x):=\ell(z,x)=\alpha\cdot z+\beta\cdot x,
 \qquad m_z:=\min_{C_z}f_z,
 \qquad M_z:=\max_{C_z}f_z,
\]
and, for \(0\le t\le w_z\), define
\[
 \phi_z(t):=\inf\left\{\int_{C_z}f_z(x)h(x)\,dx:
 0\le h\le1,\ \int_{C_z}h\,dx=t\right\}.
 \tag{1}
\]
Because \(\beta\ne0\), every level set of \(f_z\) is contained in an affine hyperplane and has \(d\)-volume zero.  The distribution function
\[
 F_z(q):=\operatorname{vol}_d\{x\in C_z:f_z(x)\le q\}
\]
is continuous, equals \(0\) at \(m_z\), equals \(w_z\) at \(M_z\), and is strictly increasing between these two values.  For strictness, if \(m_z<q_1<q_2<M_z\), the open set \(\operatorname{int}(C_z)\cap\{q_1<f_z<q_2\}\) is nonempty after narrowing to any intermediate level, and hence has positive volume.  Continuity follows because the indicators of the sublevel sets converge pointwise away from a null level hyperplane.

Consequently, for every \(0<t<w_z\) there is a unique \(q_z(t)\in(m_z,M_z)\) with \(F_z(q_z(t))=t\).  The indicator
\[
 h_{z,t}:={\bf1}_{\{f_z\le q_z(t)\}}
\]
attains (1).  Indeed, for any admissible \(h\) of the same mass,
\[
 \int_{C_z} f_z(h-h_{z,t})
 =\int_{C_z}(f_z-q_z(t))(h-h_{z,t})\ge0. \tag{2}
\]
On \(\{f_z<q_z(t)\}\), both factors in the last product are nonpositive, while on \(\{f_z>q_z(t)\}\) both are nonnegative; the equality level is null.  At \(t=0\), the closed cap \(\{f_z\le m_z\}\) has zero volume and realizes \(\phi_z(0)=0\); at \(t=w_z\), the full fiber realizes \(\phi_z(w_z)=\int_{C_z}f_z\).

The nested caps just constructed also show that \(\phi_z\) is continuous and convex on \([0,w_z]\).  More precisely, with subgradients understood relative to this closed interval,
\[
 \partial\phi_z(t)=
 \begin{cases}
 (-\infty,m_z],&t=0,\\
 \{q_z(t)\},&0<t<w_z,\\
 [M_z,\infty),&t=w_z.
 \end{cases} \tag{3}
\]
Here is a direct verification.  For an interior \(t\), the function \(h_{z,t}\) globally minimizes
\(\int(f_z-q_z(t))h\) over all \(0\le h\le1\), without a mass constraint.  It follows that, for every \(s\in[0,w_z]\),
\[
 \phi_z(s)-q_z(t)s\ge\phi_z(t)-q_z(t)t. \tag{4}
\]
Thus \(q_z(t)\) is a subgradient.  If \(s>t\), the difference between the two nested minimizing caps has mass \(s-t\) and its \(f_z\)-values lie between \(q_z(t)\) and \(q_z(s)\).  The analogous assertion holds for \(s<t\).  Letting \(s\to t\), using continuity of the inverse of \(F_z\), shows that both one-sided derivatives equal \(q_z(t)\), so the interior subgradient is unique.  At \(0\), the subgradient inequality holds exactly for slopes at most \(m_z\); at \(w_z\), it holds exactly for slopes at least \(M_z\).  This proves (3), including its finite endpoint slopes.  It also proves convexity, because (4) and the endpoint versions give a supporting affine function at every point of the interval.

We next solve the coupled base-moment problem and justify a finite multiplier even when its prescribed moment lies on a proper face.  For each \(z\in D\), set
\[
 v_z:=(1,z-z_0)\in\mathbb R^{n+1},\qquad
 B:=\prod_{z\in D}[0,w_z],\qquad
 T(b):=\sum_{z\in D}b_zv_z,
\]
and put \(c:=(a,0)\).  A density representing \(y\) exists by the definition of \(\mathsf M_a(C)\).  If it is denoted by \(g\), then
\[
 b_z^g:=\int_{C_z}g(z,x)\,dx
\]
belongs to \(B\) and satisfies \(T(b^g)=c\).  Thus \(c\) belongs to the zonotope \(K:=T(B)\), and the exact mass-and-base-moment polytope
\[
 P:=\{b\in B:T(b)=c\} \tag{5}
\]
is nonempty and compact.

Let \(F\) be the minimal face of \(K\) containing \(c\).  Choose an exposing vector \(r\in\mathbb R^{n+1}\) such that
\[
 F=\{k\in K:r\cdot k=\max_{q\in K}r\cdot q\}; \tag{6}
\]
when \(F=K\), take \(r=0\).  Partition \(D\) according to the sign of \(r\cdot v_z\) into \(D_+,D_-,D_0\).  Maximization of \(r\cdot T(b)\) over the box is coordinatewise.  Therefore every \(b\in P\) satisfies
\[
 b_z=w_z\quad(z\in D_+),\qquad b_z=0\quad(z\in D_-). \tag{7}
\]
Moreover, after putting
\[
 c_0:=c-\sum_{z\in D_+}w_zv_z,\qquad
 K_0:=\sum_{z\in D_0}[0,w_z]v_z,
\]
one has \(F=\sum_{D_+}w_zv_z+K_0\), and \(c_0\in\operatorname{relint}K_0\).  Equivalently, after the coordinates forced in (7) are removed, a strict feasible point remains: if \(T_0(t)=\sum_{D_0}t_zv_z\), then
\[
 T_0\left(\prod_{z\in D_0}(0,w_z)\right)=\operatorname{relint}K_0. \tag{8}
\]
For completeness, (8) is the elementary identity that a linear map sends the relative interior of a box onto the relative interior of its image.  If a box point is interior, choose a linear right inverse of \(T_0\) on its range.  Every sufficiently small displacement in that range has a sufficiently small right-inverse displacement that stays inside the box, so the image point is relatively interior.  Conversely, fix an interior point of the box and its image.  A relative-interior image point can be extended a short distance beyond itself on the ray from that fixed image; expressing the original point as a strict convex combination of the extended image and the fixed image gives a preimage in the interior of the box.

Choose \(b^*\in P\) minimizing
\[
 \Phi(b):=\sum_{z\in D}\phi_z(b_z). \tag{9}
\]
Existence follows from compactness and continuity.  We now obtain the multiplier without assuming that \(c\in\operatorname{relint}K\).  On the free coordinates define
\[
 \Psi(t):=\sum_{z\in D_0}\phi_z(t_z),\qquad
 V(u):=\min\{\Psi(t):0\le t_z\le w_z,\ T_0(t)=u\}.
\]
By (7), the forced-coordinate terms in \(\Phi\) are constant on \(P\), so \(b^*_{D_0}\) attains \(V(c_0)\).
The value function \(V\) is convex on \(K_0\) and lower semicontinuous: for a convergent sequence of right-hand sides, compactness gives a convergent subsequence of minimizers, and continuity of \(\Psi\) gives the lower-semicontinuity inequality.  Since \(c_0\in\operatorname{relint}K_0\), there is a finite relative subgradient \(\nu\in\mathbb R^{n+1}\) at \(c_0\):
\[
 V(u)\ge V(c_0)+\nu\cdot(u-c_0)\qquad(u\in K_0). \tag{10}
\]
This last standard finite-dimensional separation step is also immediate directly from the epigraph.  A supporting hyperplane to \(\operatorname{epi}V\) at \((c_0,V(c_0))\), taken relative to \(\operatorname{aff}(K_0)\times\mathbb R\), cannot have zero coefficient on the last coordinate, because then a nonzero functional would support \(K_0\) at its relative-interior point.  The coefficient is negative because the epigraph contains the upward vertical ray, so it can be normalized to \(-1\), yielding (10).  If \(K_0=\{0\}\), take \(\nu=0\).

For every free-coordinate vector \(t\) in its box, (10) gives
\[
 \Psi(t)\ge V(T_0t)
 \ge V(c_0)+\nu\cdot(T_0t-c_0)
 =\Psi(b^*_{D_0})+
 \sum_{z\in D_0}(\nu\cdot v_z)(t_z-b_z^*). \tag{11}
\]
Varying one coordinate at a time and using (3), we obtain
\[
 \nu\cdot v_z\in\partial\phi_z(b_z^*)\qquad(z\in D_0). \tag{12}
\]
All quantities here are finite.  Choose a finite \(s\ge0\) large enough that
\[
 \nu\cdot v_z+s\,r\cdot v_z\ge M_z\quad(z\in D_+),
 \qquad
 \nu\cdot v_z+s\,r\cdot v_z\le m_z\quad(z\in D_-). \tag{13}
\]
Such an \(s\) exists because the relevant coefficients \(r\cdot v_z\) have the displayed strict signs and \(D\) is finite.  Put \(\widehat\nu:=\nu+sr\) and
\[
 q_z:=\widehat\nu\cdot v_z. \tag{14}
\]
For \(z\in D_0\), adding \(sr\) changes nothing.  For \(z\in D_+\), (7), (13), and the full-fiber endpoint in (3) give \(q_z\in\partial\phi_z(w_z)\).  For \(z\in D_-\), they give \(q_z\in\partial\phi_z(0)\).  Hence
\[
 q_z\in\partial\phi_z(b_z^*)\qquad(z\in D). \tag{15}
\]
This is the required finite multiplier statement on an arbitrary face of the moment zonotope.  It also handles \(a=W\): then the mass coordinate exposes the face on which every \(b_z=w_z\), and (13) chooses a finite threshold above every fiber maximum.

Write \(\widehat\nu=(\eta,\rho)\in\mathbb R\times\mathbb R^n\) and set \(\lambda:=-\rho\).  Then
\[
 q_z=\eta-\lambda\cdot(z-z_0). \tag{16}
\]
By (3) and (15), the closed lower cap
\[
 A_z:=C_z\cap\{x:f_z(x)\le q_z\} \tag{17}
\]
has volume exactly \(b_z^*\) and satisfies
\[
 \int_{A_z}f_z(x)\,dx=\phi_z(b_z^*). \tag{18}
\]
Indeed, an interior coordinate uses its unique quantile threshold; if \(b_z^*=0\), then \(q_z\le m_z\) and (17) is empty up to the null minimum-level hyperplane; if \(b_z^*=w_z\), then \(q_z\ge M_z\) and (17) is the full fiber.  Equations (16) and (17) show that these are precisely the lattice fibers of the single adjusted halfspace cap \(A=C\cap G\) in the statement.  The continuous normal of \(G\) is still \(\beta\ne0\).  Hence, on every integer fiber, \(\partial G\) lies in a \(d\)-null affine hyperplane.  There are only finitely many relevant fibers, so \(\mu_C(\partial G)=0\).  Zero-volume fibers remain harmless, including fibers contained in that boundary.

Equations (5), (17), and (18) now give the exact mass and base moment:
\[
 \mu_C(A)=\sum_zb_z^*=a,
 \qquad \sum_z(z-z_0)b_z^*=0. \tag{19}
\]
It remains to locate the mixed centroid.  The representing density \(g\) and the one-fiber minimization (1) imply
\[
 \begin{aligned}
 \int_A\ell(p)\,d\mu_C(p)
 &=\sum_{z\in D}\phi_z(b_z^*)\\
 &\le\sum_{z\in D}\phi_z(b_z^g)\\
 &\le\sum_{z\in D}\int_{C_z}f_z(x)g(z,x)\,dx
 =a\ell(y).
 \end{aligned} \tag{20}
\]
After division by \(a\), this is \(\ell(\overline y_A)\le\ell(y)\), so \(\overline y_A\in H\).  Its base coordinate is \(z_0\) by (19), and hence is integral.  Since \(A\) is compact and convex and \(\overline y_A\) is a barycenter of a probability measure supported on \(A\), one has \(\overline y_A\in A\).  Finally, \(\mu_A(H)=\mu_C(A\cap H)\le\mu_C(H)\) follows from inclusion.

For the vertical corollary, fix \(u\ne0\) and \(\varepsilon>0\), and apply the theorem just proved to
\[
 \ell_\varepsilon(z,x):=L(z)+\varepsilon u\cdot x,
 \qquad
 H_\varepsilon:=\{p:\ell_\varepsilon(p)\le\ell_\varepsilon(y)\}.
\]
Its continuous normal is \(\varepsilon u\ne0\).  The resulting cap has mass \(a\) and base centroid \(z_0\).  If its centroid is \((z_0,\overline x_\varepsilon)\), membership in \(H_\varepsilon\) says
\[
 L(z_0)+\varepsilon u\cdot\overline x_\varepsilon
 \le L(z_0)+\varepsilon u\cdot x_0,
\]
which proves \(u\cdot\overline x_\varepsilon\le u\cdot x_0\).  Its base coordinate is exactly \(z_0\), so it lies on \(\partial H_0\).  The cap's defining functional has continuous component \(\varepsilon u\) and came from optimizing the perturbed objective \(\ell_\varepsilon\); this proves the stated distinction from an unsupported vertical multiplier representation.

## External sources

none
