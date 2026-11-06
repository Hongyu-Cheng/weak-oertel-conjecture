---
fact_id: 1a42a8cddaada800
kind: lemma
author: "research-agent"
assurance: LLM-verified
subgoal_id: oct3x-single-boundary-facet-original-stock-screen
depends_on: ["6d6fcf377e68c79c","978e8555ec5bac42"]
verifier_run: 9cd94458654f4875
target_match: null
---

## Statement

Let \(n\geq1\) and \(d\geq2\), and put \(q=d-2\). Use orthonormal coordinates \((s,t,\mathbf v)\in\mathbb R\times\mathbb R\times\mathbb R^q\) for the continuous coordinates of the locked problem. Thus the canonical fiber remains \(C_{\mathbf z}:=\{(s,t,\mathbf v):(\mathbf z,s,t,\mathbf v)\in C\}\), with only its continuous coordinates changed. Use the canonical measure and mass from fact 6d6fcf377e68c79c:

\[
\mu_C(A)=\sum_{\mathbf z\in\mathbb Z^n}\int_{C_{\mathbf z}}\mathbf 1_A(\mathbf z,s,t,\mathbf v)\,ds\,dt\,d\mathbf v,
\qquad W=\mu_C(\mathbb R^{n+d})>0.
\]

The measure denoted by \(\mu\) in fact 978e8555ec5bac42 is exactly this \(\mu_C\), not a conditioned or rescaled measure. Here and below \(\Lambda=\mathbb Z^n\times\mathbb R^d\) is the locked mixed-integer set.

Assume \(C\) is a convex polytope body, contained in \(\{t\geq0\}\), and that \(F=C\cap\{t=0\}\) is a facet. Fix an interval \(I=[s_-,s_+]\), with \(s_-<s_+\), a normal height \(\rho>0\), and a tangential center \(\mathbf v_0\). Require that, for some \(\mathbf z_0\in\mathbb Z^n\) and \(s_0\in(s_-,s_+)\), the point \((\mathbf z_0,s_0,0,\mathbf v_0)\) belongs to \(\operatorname{relint}F\). These are explicit one-facet geometric hypotheses; all original fibers satisfy the same supporting inequality \(t\geq0\).

For \(q>0\), choose positive widths \(\varepsilon_1,\ldots,\varepsilon_q\), put \(\mathcal B=[-1/2,1/2]^q\), and write \(E\mathbf u=(\varepsilon_1u_1,\ldots,\varepsilon_qu_q)\). For \(q=0\), \(\mathcal B=\{0\}\subset\mathbb R^0\) has its unit zero-dimensional measure, and \(E\mathbf u=0\). Put \(J=\prod_{i=1}^q\varepsilon_i\), with empty product \(J=1\), and \(K=I\times[0,\rho]\). The actual retained convex node and its original mass are

\[
C^{\mathrm{ret}}=C\cap\{s\in I,\ 0\leq t\leq \rho,\ \mathbf v\in\mathbf v_0+E\mathcal B\},
\qquad W_{\mathrm{ret}}=\mu_C(C^{\mathrm{ret}}).
\]

Let \(\mathcal Z=\operatorname{proj}_{\mathbb R^n}(C)\cap\mathbb Z^n\), which is finite. Define the actual center slices, their mixed two-dimensional measure, and their total mass by

\[
P_{\mathbf z}=\{(s,t)\in K:(s,t,\mathbf v_0)\in C_{\mathbf z}\},
\qquad
\nu(A)=\sum_{\mathbf z\in\mathcal Z}\int_{P_{\mathbf z}}\mathbf 1_A(\mathbf z,s,t)\,ds\,dt,
\qquad T=\nu(\mathbb R^{n+2}).
\]

In particular, \(T\) is the mass of the actual \((s,t)\) center slice, not a limiting slice at \(t=0\). It is positive under the relative-interior hypothesis. The exact density after scaling only the symmetric tangential box is

\[
f_{\mathbf z}(s,t,\mathbf u)=\mathbf 1_{C_{\mathbf z}}(s,t,\mathbf v_0+E\mathbf u)
\quad ((s,t,\mathbf u)\in K\times \mathcal B).
\]

The product reference density is \(\mathbf 1_{P_{\mathbf z}}(s,t)\), independent of \(\mathbf u\), with total mass \(T\). Define its total symmetric-difference discrepancy using the exact original fiber indicators:

\[
D=\sum_{\mathbf z\in\mathcal Z}\int_{K\times \mathcal B}
\left|f_{\mathbf z}(s,t,\mathbf u)-\mathbf 1_{P_{\mathbf z}}(s,t)\right|\,ds\,dt\,d\mathbf u.
\]

Then the following conclusions hold.

There is a point \((\mathbf z^\star,s^\star,t^\star)\), with \((s^\star,t^\star)\in P_{\mathbf z^\star}\), such that every closed halfspace containing this point has \(\nu\)-mass at least \(T/(3\cdot2^n)\). Its lift \(\mathbf y^\star=(\mathbf z^\star,s^\star,t^\star,\mathbf v_0)\) belongs to the actual \(C^{\mathrm{ret}}\cap\Lambda\). Every closed halfspace \(H\ni\mathbf y^\star\) satisfies

\[
\mu_C(H\cap C^{\mathrm{ret}})\ \geq\ J\left(\frac{T}{6\cdot2^n}-D\right),
\qquad
\left|\frac{W_{\mathrm{ret}}}{J}-T\right|\leq D.
\]

Let \(c>0\) and \(L\geq1\), and assume the actual original-stock condition \(W\leq L W_{\mathrm{ret}}\). Put \(\alpha=Lc2^{-n}\). If

\[
\alpha<\frac1{6\cdot2^n},
\qquad
\frac DT<\frac{1/(6\cdot2^n)-\alpha}{1+\alpha},
\]

then no closed halfspace with original charge \(\mu_C(H)\leq c2^{-n}W\) contains \(\mathbf y^\star\). Thus an arbitrary collection of such original caps cannot cover this retained node's mixed points. Here \(L\) bounds the original-to-retained mass ratio; it is not a cap count, and the original charge is not assumed to survive conditioning. More generally, the same conclusion follows for any cap whose actual original charge is at most \(\alpha W_{\mathrm{ret}}\).

There is a finite facet-inequality discrepancy bound. Suppose an exact finite representation of \(C\) is

\[
C=\{(\mathbf x,s,t,\mathbf v):
\mathbf a_j\cdot\mathbf x+b_js+e_jt+\mathbf f_j\cdot\mathbf v\leq g_j,
\quad 1\leq j\leq r\}.
\]

For each \(\mathbf z\in\mathcal Z\), put \(\delta_{\mathbf z j}=g_j-\mathbf a_j\cdot\mathbf z-\mathbf f_j\cdot\mathbf v_0\), and put \(\lambda_j=\tfrac12\sum_{i=1}^q\varepsilon_i|f_{ji}|\). For \(\lambda_j=0\), define \(A_{\mathbf z j}=0\). For \(\lambda_j>0\), define

\[
A_{\mathbf z j}=\operatorname{area}\bigl(K\cap\{|b_js+e_jt-\delta_{\mathbf z j}|\leq\lambda_j\}\bigr).
\]

Then

\[
D\leq\sum_{\mathbf z\in\mathcal Z}\sum_{j=1}^r A_{\mathbf z j}.
\]

For \(\lambda_j>0\), its terms obey the following explicit bounds, where \(|I|=s_+-s_-\):

\[
A_{\mathbf z j}\leq
\begin{cases}
\rho\min\{|I|,\,2\lambda_j/|b_j|\},&b_j\neq0,\\
|I|\,\bigl|[0,\rho]\cap\{t:|e_jt-\delta_{\mathbf z j}|\leq\lambda_j\}\bigr|,&b_j=0,\ e_j\neq0,\\
|I|\rho\,\mathbf 1_{\{|\delta_{\mathbf z j}|\leq\lambda_j\}},&b_j=e_j=0.
\end{cases}
\]

The interval length in the middle line and the expression in the last line are exact slab areas. The sum includes all original integer fibers, including ones with empty or zero-area \(P_{\mathbf z}\). No lower bound for a facet normal is assumed. If the normal coordinate is also rescaled by \(t=\rho\tau\), both \(T\) and \(D\) are divided by \(\rho\), the two-coordinate normal becomes \((b_j,\rho e_j)\), and \(D/T\) is unchanged. For a family of polyhedral nodes with scale-dependent inequalities, the bound uses each node's actual \(b_j,e_j,\mathbf f_j,\delta_{\mathbf z j}\); it makes no assertion that these coefficients are uniform in the scale.

One simpler sufficient geometric certificate is as follows. Suppose \(P_{\mathbf z_0}\) contains \(I_0\times[0,\rho]\) for a subinterval \(I_0\subseteq I\) of length \(\ell>0\), and suppose, for every \(\mathbf z\in\mathcal Z\) and every \(j\) with \(b_j=0\) and \(\lambda_j>0\), that

\[
\operatorname{dist}(\delta_{\mathbf z j},e_j[0,\rho])>\lambda_j.
\]

Then

\[
\frac DT\leq\frac2\ell
\sum_{\mathbf z\in\mathcal Z}\sum_{j:b_j\neq0}\frac{\lambda_j}{|b_j|}.
\]

Consequently the right-hand side being smaller than the discrepancy threshold, together with its original-stock hypothesis, suffices for the all-cap screen. All these margin, prism, and slab conditions refer to the one actual finite node. With rational data in the chosen coordinates, the center slices and slabs are rational polygons, so their areas and this certificate can be evaluated by exact finite rational arithmetic.

Finally, relative-interior centering and shrinking tangential and normal widths alone do not imply \(D/T\to0\) if the facet normals may vary. Specifically, for every rational \(\eta\in(0,1)\), in coordinates \((x,s,t,v)\) with \(n=1,d=3\), the rational polytope

\[
C_\eta=\{ -1/4\leq x\leq1/4,\quad 0\leq s\leq1,\quad
0\leq t\leq1,\quad -\eta s\leq v\leq\eta s\}
\]

has common facet \(t=0\) with \((0,1/2,0,0)\) in its relative interior. Choose \(I=[0,1]\), \(\rho=\eta\), \(v_0=0\), and \(\varepsilon_1=2\eta\). For this actual finite node, \(T=\eta\), \(D=\eta/2\), \(W=\eta\), and \(W_{\mathrm{ret}}=\eta^2\). Thus \(D/T=1/2\) at every scale, and the proposed discrepancy criterion cannot hold for any \(\alpha\geq0\). This is a failure of automatic product approximation and of that sufficient certificate, not a counterexample to the locked conjecture or an assertion that the actual centerpoint has small depth.

## Proof

First, the orthonormal change of continuous coordinates preserves \(d\)-dimensional fiber volume and leaves the integer coordinates untouched, so it preserves the canonical \(C_{\mathbf z},\mu_C,W\). Compactness of \(C\) makes \(\mathcal Z\) finite. The map

\[
\Phi(\mathbf x,s,t,\mathbf u)=(\mathbf x,s,t,\mathbf v_0+E\mathbf u)
\]

is invertible in the continuous coordinates and has fiber-volume Jacobian \(J\). It preserves integer coordinates and sends \(\mathbf u=0\) to the actual central tangential coordinate \(\mathbf v_0\).

We check that \(T>0\). At a relative-interior point of the facet \(F\), every other actual facet inequality of \(C\) is strict. Indeed, if another supporting hyperplane contained such a point, the relative-interior property would force it to contain the affine hull of \(F\), so it would be the same facet hyperplane. In an irredundant facet representation, the only active inequality there is therefore the supporting inequality \(t\geq0\). The finitely many strict inequalities remain strict after sufficiently small changes in \(s\) and sufficiently small positive changes in \(t\), with \(\mathbf x=\mathbf z_0\) and \(\mathbf v=\mathbf v_0\) fixed. Because \(s_0\in(s_-,s_+)\) and \(\rho>0\), this gives a positive-area rectangle inside \(P_{\mathbf z_0}\). Hence \(T>0\). This argument uses an irredundant representation only to justify the geometry; the discrepancy estimate may use any exact finite representation.

Let

\[
C^{(2)}=\{(\mathbf x,s,t):(\mathbf x,s,t,\mathbf v_0)\in C,\ (s,t)\in K\}.
\]

This is a nonempty compact convex subset of \(\mathbb R^{n+2}\), and \(\nu\) is a finite Borel measure supported on \(C^{(2)}\cap(\mathbb Z^n\times\mathbb R^2)\), with mass \(T\). The \(d=2\) Borel centerpoint consequence of accepted fact 6d6fcf377e68c79c gives a point \((\mathbf z^\star,s^\star,t^\star)\in\mathbb Z^n\times\mathbb R^2\) whose every containing closed halfspace has \(\nu\)-mass at least \(T/(3\cdot2^n)>0\).

This point actually belongs to \(C^{(2)}\), even if that set is not a convex body in its ambient dimension. To verify this without any support-attainment assumption, suppose it lies outside \(C^{(2)}\), and choose a nearest point \(p\in C^{(2)}\). Writing \(w=(\mathbf z^\star,s^\star,t^\star)-p\), one has \(w\neq0\) and \(w\cdot(y-p)\leq0\) for every \(y\in C^{(2)}\). The latter follows by considering the squared distance to \(p+\theta(y-p)\) for \(0\leq\theta\leq1\) and its right derivative at \(\theta=0\). Thus the closed halfspace

\[
\{r:w\cdot r\geq w\cdot(\mathbf z^\star,s^\star,t^\star)\}
\]

contains the centerpoint and is disjoint from \(C^{(2)}\), contradicting its positive depth. Consequently \((s^\star,t^\star)\in P_{\mathbf z^\star}\). Since \(0\in \mathcal B\), the lift \(\mathbf y^\star=(\mathbf z^\star,s^\star,t^\star,\mathbf v_0)\) belongs to the actual retained mixed node. This lifting precedes, and does not rely on, any estimate on \(D\).

Consider the product measure \(\nu\otimes d\mathbf u|_{\mathcal B}\) in the coordinates \((\mathbf z,s,t,\mathbf u)\). Its mass is \(T\), since \(|\mathcal B|=1\). Let a closed halfspace through \((\mathbf z^\star,s^\star,t^\star,0)\) be written as

\[
\mathbf a\cdot(\mathbf z-\mathbf z^\star)+b(s-s^\star)
+\gamma(t-t^\star)+\mathbf r\cdot\mathbf u\geq0.
\]

The corresponding base halfspace

\[
\mathbf a\cdot(\mathbf z-\mathbf z^\star)+b(s-s^\star)
+\gamma(t-t^\star)\geq0
\]

has \(\nu\)-mass at least \(T/(3\cdot2^n)\). If its normal is zero, it is the whole space and has mass \(T\), which is at least this bound. On every base point in this halfspace, every \(\mathbf u\in \mathcal B\) with \(\mathbf r\cdot\mathbf u\geq0\) lies in the full halfspace. Reflection \(\mathbf u\mapsto-\mathbf u\) preserves \(\mathcal B\) and its measure, so the measure of this closed half-box is at least \(1/2\). This remains true for \(\mathbf r=0\) and for \(q=0\), when it is the whole box. Fubini's theorem therefore gives product mass at least \(T/(6\cdot2^n)\). Closed boundaries cause no loss: they are included throughout.

For every Borel set in the scaled coordinates, the difference between its exact retained mass divided by \(J\) and its product reference mass has absolute value at most \(D\), directly by integrating the absolute difference of the densities in the definition of \(D\). Applying this first to a through-centerpoint halfspace and then to the whole space gives both claimed mass inequalities. For a closed halfspace merely containing the lifted point, use accepted fact 978e8555ec5bac42 to move its boundary to that point, producing a contained closed halfspace. Equivalently, for \(H=\{x:\mathbf a\cdot x\geq b\}\ni\mathbf y^\star\), the halfspace \(\{x:\mathbf a\cdot x\geq\mathbf a\cdot\mathbf y^\star\}\) is contained in \(H\). The affine inverse image under \(\Phi\) is a halfspace through \((\mathbf z^\star,s^\star,t^\star,0)\), so the same bound follows. This uses the actual original measure, including any mass on integer-fiber boundary hyperplanes.

The strict discrepancy hypothesis is exactly

\[
\frac{T}{6\cdot2^n}-D>\alpha(T+D).
\]

The mass inequalities and \(W_{\mathrm{ret}}\leq J(T+D)\) imply, for every \(H\ni\mathbf y^\star\),

\[
\mu_C(H\cap C^{\mathrm{ret}})
>\alpha J(T+D)
\geq\alpha W_{\mathrm{ret}}.
\]

But a cap with original charge \(\mu_C(H)\leq c2^{-n}W\) would satisfy

\[
\mu_C(H\cap C^{\mathrm{ret}})\leq\mu_C(H)
\leq c2^{-n}W\leq Lc2^{-n}W_{\mathrm{ret}}
=\alpha W_{\mathrm{ret}},
\]

a contradiction. This verifies the all-cap claim without assigning any new charge after restriction, rescaling, or product replacement. The argument also proves the version with the direct original-charge bound \(\alpha W_{\mathrm{ret}}\).

To prove the finite facet estimate, fix \((s,t,\mathbf u)\in K\times \mathcal B\) and \(\mathbf z\in\mathcal Z\). If the two fiber indicators differ, the truth value of at least one of their defining inequalities differs. For such an index \(j\), the two left-minus-right values are

\[
b_js+e_jt-\delta_{\mathbf z j},
\qquad
b_js+e_jt-\delta_{\mathbf z j}+\mathbf f_j\cdot E\mathbf u.
\]

One is positive and the other is nonpositive. It follows that

\[
|b_js+e_jt-\delta_{\mathbf z j}|
\leq|\mathbf f_j\cdot E\mathbf u|
\leq\frac12\sum_i\varepsilon_i|f_{ji}|=\lambda_j.
\]

Such a truth-value change is impossible if \(\lambda_j=0\). The indicator of a discrepancy is therefore bounded by the sum of the slab indicators defining \(A_{\mathbf z j}\) with \(\lambda_j>0\). Integrating over the unit-volume \(\mathcal B\), then over \(K\), and summing over the finite original \(\mathcal Z\) proves the claimed bound. This pointwise proof does not assume that the center fiber exists, has positive area, or persists under tangential displacement. In particular it counts all appearances and disappearances of fibers.

When \(b_j\neq0\), at each fixed \(t\in[0,\rho]\) the permitted \(s\)-slab has length at most \(2\lambda_j/|b_j|\), and its intersection with \(I\) has length at most \(|I|\). Integration in \(t\) proves the first bound. When \(b_j=0\), the condition is independent of \(s\), giving the two exact expressions stated. The common supporting-facet inequality \(t\geq0\) has \(\mathbf f_j=0\), hence \(\lambda_j=0\), and contributes nothing. Substituting \(t=\rho\tau\) verifies the stated transformation of the two-coordinate normals and the factor \(1/\rho\) in both the reference mass and discrepancy. Nothing in the proof replaces actual coefficients by their limits.

Under the simpler margin hypothesis, every slab with \(b_j=0\) and \(\lambda_j>0\) misses \(K\), and all terms with \(\lambda_j=0\) are already zero. The remaining terms sum to at most \(2\rho\sum_{\mathbf z}\sum_{j:b_j\neq0}\lambda_j/|b_j|\). The actual reference prism gives \(T\geq\ell \rho\); division proves the stated ratio estimate. For rational data, the inequalities defining \(P_{\mathbf z}\) and these slabs have rational coefficients. Their finitely many vertices are obtained by solving pairs of rational linear equations, with degenerate cases having zero area. Ordering the vertices and summing the triangle determinant areas gives exact rational areas. Thus this is a finite geometric certificate rather than a floating-point infeasibility or optimality claim.

Finally, verify the calibration family directly. The displayed constraints defining \(C_\eta\) are rational linear inequalities. The body is compact and convex, and has nonempty interior, for example near \(x=0,s=1/2,t=1/2,v=0\). Only the integer fiber \(x=0\) is nonempty. At \((0,1/2,0,0)\), the inequality \(t\geq0\) is tight and every other actual facet inequality is strict, so the point is in the relative interior of the facet \(t=0\). The center slice is precisely \(P_0=[0,1]\times[0,\eta]\), with \(T=\eta\). The scaled tangential box is \(v=2\eta u\), \(u\in[-1/2,1/2]\), and its exact fiber indicator on \(K\times \mathcal B\) is

\[
f_0(s,t,u)=\mathbf 1_{\{2|u|\leq s\}}.
\]

The product indicator is identically one there. Thus the entire discrepancy is an exact loss, and

\[
D=\int_0^\eta\int_{-1/2}^{1/2}\int_0^1
\mathbf 1_{\{s<2|u|\}}\,ds\,du\,dt
=\eta\int_{-1/2}^{1/2}2|u|\,du
=\frac\eta2.
\]

The original triangular \((s,v)\)-section has area \(\int_0^1 2\eta s\,ds=\eta\). Since its original \(t\)-height is one, \(W=\eta\). The transverse crop \([-\eta,\eta]\) already contains that triangle, and the retained \(t\)-height is \(\eta\), so \(W_{\mathrm{ret}}=\eta^2\). Equivalently, \(J=2\eta\) and \(W_{\mathrm{ret}}=J(T-D)=\eta^2\). The two oblique facet inequalities have \((b_j,e_j,f_j)=(-\eta,0,1)\) and \((-\eta,0,-1)\); hence their \(s\)-normal coefficients tend to zero while \(\lambda_j=\eta\), preserving a nonvanishing perturbation-to-normal ratio. Both the normal height and the symmetric tangential width tend to zero, but \(D/T=1/2\) remains fixed. For \(n=1\), the proposed right-hand threshold is at most \(1/12\) when \(\alpha\geq0\), so this discrepancy cannot meet it. Also \(W/W_{\mathrm{ret}}=1/\eta\), displaying why the original-stock condition cannot be inferred from rescaling. These exact calculations concern only this approximation mechanism and do not resolve the locked target.

## External sources

None. The only accepted predecessors used are 6d6fcf377e68c79c for the two-continuous-coordinate Borel centerpoint and 978e8555ec5bac42 for closed-halfspace boundary reduction. All geometry, normalization, discrepancy estimates, original-charge comparisons, and the rational calibration family are proved above.
