---
fact_id: da814bbdba7c5b71
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: maximal-root-midpoint-envelope
depends_on: ["6769574fc1bd9f8d","be359f8a6c628483","dfd25e72c1f45a4e"]
verifier_run: e54b35400aaa4b39
target_match: null
---

## Statement

Let \(n,d\in\mathbb Z_{>0}\), let \(C\subseteq\mathbb R^n\times\mathbb R^d\) be a convex body, and use the following normalization from accepted fact `be359f8a6c628483`. Put \(\Lambda:=\mathbb Z^n\times\mathbb R^d\), \(S:=C\cap\Lambda\), \(C_z:=\{y\in\mathbb R^d:(z,y)\in C\}\), \(a_z:=\operatorname{vol}_d(C_z)\), \(W:=\sum_{z\in\mathbb Z^n}a_z\), and \(D_+:=\{z\in\mathbb Z^n:a_z>0\}\). For every Borel set \(B\subseteq\mathbb R^{n+d}\), define
\[
\mu_C(B):=\sum_{z\in\mathbb Z^n}
\operatorname{vol}_d\{y\in C_z:(z,y)\in B\}.
\]
For \(p\in S\), let \(h_S(p):=\inf_{H\ni p}\mu_C(H)\), where \(H\) ranges over closed ambient halfspaces, and let \(h_{\max}(C):=\sup_{p\in S}h_S(p)\). These are absolute depths, with no division by \(W\). Put \(\gamma_d:=(d/(d+1))^d\). For \((z,q)\in C\), let \(\delta_C(z,q):=\inf_{L\ni q}\operatorname{vol}_d(C_z\cap L)\), where \(L\subseteq\mathbb R^d\) ranges over proper closed halfspaces.

For bounded measurable \(K\subseteq\mathbb R^d\) and \(t>0\), define
\[
\mathsf M_t(K):=
\left\{\frac1t\int_{\mathbb R^d}y f(y)\,dy:
f\text{ measurable},\ 0\leq f\leq\mathbf1_K\text{ a.e.},\quad
\int_{\mathbb R^d}f(y)\,dy=t\right\}.
\]
This is the metronoid of accepted facts `6769574fc1bd9f8d` and `dfd25e72c1f45a4e`; extending a density on \(K\) by zero identifies their two definitions. Here \(t\) is mass, and \(t^{1/d}\) is the positive lift coordinate in `dfd25e72c1f45a4e`.

Let \(A\subseteq\mathbb Z^n\) be finite and nonempty. For each \(z\in A\), choose \(0<t_z\leq a_z\) and \(q_z\in\mathsf M_{t_z}(C_z)\). Define the set of distinct integral midpoint bases by \(E:=\{m\in\mathbb Z^n:z+z'=2m\text{ for some }z,z'\in A\}\), including diagonal pairs, and define
\[
e_m:=\max_{\substack{z,z'\in A\\z+z'=2m}}
\left(\frac{t_z^{1/d}+t_{z'}^{1/d}}2\right)^d
\qquad(m\in E).
\]
At each \(m\in E\), select one maximizing pair \((z_m,z'_m)\). The maximum is over all pairs at that physical target, without separating their parity classes. Ties are resolved arbitrarily, but all choices are fixed before considering any halfspace. Set \(x_m:=(q_{z_m}+q_{z'_m})/2\), \(p_m:=(m,x_m)\), and \(\sigma:=\gamma_d\sum_{m\in E}e_m\delta_{p_m}\), where \(\delta_{p_m}\) denotes unit point mass.

For every such choice, \(0<e_m\leq a_m\), \(x_m\in\mathsf M_{e_m}(C_m)\), and \(\delta_C(m,x_m)\geq\gamma_de_m\) for all \(m\in E\). In particular, \(E\subseteq D_+\) and \(\sigma\) is a nonzero positive finite measure carried by \(S\), satisfying \(\sigma(H)\leq\mu_C(H)\) for every closed ambient halfspace \(H\). This is halfspace domination, not domination on arbitrary Borel sets. Its mass is \(|\sigma|=\gamma_d\sum_{m\in E}e_m\), with \(\sum_{z\in A}t_z\leq\sum_{m\in E}e_m\leq W\).

Put \(\rho:=\dim\operatorname{aff}A\). Then \(\operatorname{aff}E=\operatorname{aff}A\). Define
\[
\begin{aligned}
r_{\mathrm{src}}&:=
\min_{\substack{s:\operatorname{aff}A\to\mathbb R^d\\s\text{ affine}}}
\dim\operatorname{span}\{q_z-s(z):z\in A\},\\
r_{\mathrm{mid}}&:=
\min_{\substack{s:\operatorname{aff}A\to\mathbb R^d\\s\text{ affine}}}
\dim\operatorname{span}\{x_m-s(m):m\in E\}.
\end{aligned}
\]
Both minima are attained, and \(r_{\mathrm{mid}}\leq r_{\mathrm{src}}\). In the dominated-measure theorem of `be359f8a6c628483`, the present measure has \(A_\sigma=\operatorname{aff}A\), \(\rho_\sigma=\rho\), and \(r_\sigma=r_{\mathrm{mid}}\). The present \(r_{\mathrm{mid}}\) refers to this selected graph, not to the separate product-averaged midpoint measure in that predecessor.

Retain the residual-selector capacity normalization of `be359f8a6c628483`:
\[
R_{\mathrm{sel}}(C):=
\sup\frac{2^{n-\dim\operatorname{aff}F}\sum_{z\in F}w_z}
{1+\dim\operatorname{span}\{v_z-s(z):z\in F\}},
\]
where the supremum ranges over nonempty \(F\subseteq D_+\), points \(v_z\in C_z\), weights \(0<w_z\leq\delta_C(z,v_z)\), and affine maps \(s:\operatorname{aff}F\to\mathbb R^d\). Thus \(F\) and \(v_z\) here are respectively the selector index set and selector points denoted by \(E\) and \(q_z\) in equation (20) of that fact. The envelope gives
\[
R_{\mathrm{sel}}(C)
\geq\frac{\gamma_d2^{n-\rho}\sum_{m\in E}e_m}{r_{\mathrm{mid}}+1}
\geq\frac{\gamma_d2^{n-\rho}\sum_{m\in E}e_m}{r_{\mathrm{src}}+1}.
\]
There is one point \(p^\star\in S\) such that
\[
h_{\max}(C)\geq h_S(p^\star)
\geq\frac{\gamma_d\sum_{m\in E}e_m}{2^\rho(r_{\mathrm{mid}}+1)}
\geq\frac{\gamma_d\sum_{m\in E}e_m}{2^\rho(r_{\mathrm{src}}+1)}.
\]
The same \(p^\star\) satisfies the middle lower bound for every closed halfspace containing it; the point does not depend on that halfspace.

For the full-volume calibration, take \(A=D_+\), \(t_z=a_z\), and \(q_z=c_z:=a_z^{-1}\int_{C_z}y\,dy\). Then \(E=D_+\), \(e_m=a_m\), and \(x_m=c_m\) for every \(m\in D_+\), independently of the maximizing-pair choices. Consequently \(\sigma=\gamma_d\sum_{m\in D_+}a_m\delta_{(m,c_m)}\), \(\sum_{m\in E}e_m=W\), and \(r_{\mathrm{mid}}=r_{\mathrm{src}}\). No universal bounded-residual-rank selection or general weak Oertel conclusion is asserted.

## Proof

Compactness of \(C\) implies that only finitely many integer base fibers meet \(C\), so \(W<\infty\) and \(D_+\) is finite. The hypotheses give \(A\subseteq D_+\), hence \(W>0\). Each source fiber \(C_z\), \(z\in A\), is compact and convex with positive \(d\)-volume, so it is a \(d\)-dimensional convex body. The set \(E\) is finite and contains \(A\), because \((z,z)\) is an admissible pair at \(m=z\). Every defining maximum therefore exists and is positive.

The proof of accepted fact `dfd25e72c1f45a4e` establishes convexity of the positive-mass lift itself before taking its closure: if \(x_i\in\mathsf M_{s_i^d}(C_{z_i})\), \(s_i>0\), and \(0\leq\lambda\leq1\), then \((1-\lambda)x_0+\lambda x_1\in\mathsf M_{((1-\lambda)s_0+\lambda s_1)^d}(C_{(1-\lambda)z_0+\lambda z_1})\). Apply that proved interpolation with its base dimension \(r=n\), endpoint bases \(z_0=z_m\), \(z_1=z'_m\), barycenters \(x_0=q_{z_m}\), \(x_1=q_{z'_m}\), lift coordinates \(s_0=t_{z_m}^{1/d}\), \(s_1=t_{z'_m}^{1/d}\), and \(\lambda=1/2\). These lift coordinates are positive, and the selected pair attains the defining maximum. Thus \(x_m\in\mathsf M_{e_m}(C_m)\), with actual positive-mass membership rather than an inference from closure.

An admissible density representing this membership has integral \(e_m\) and is bounded above by \(\mathbf1_{C_m}\). Integrating proves \(e_m\leq a_m\), so \(C_m\) also is a positive-volume compact convex body. Accepted fact `6769574fc1bd9f8d`, with its mass parameter equal to \(e_m\), gives \(x_m\in C_m\) and \(\operatorname{vol}_d(C_m\cap L)\geq\gamma_de_m\) for every proper closed halfspace \(L\subseteq\mathbb R^d\) containing \(x_m\), including boundary containment. This proves the asserted target metronoid and fiber-depth conclusions.

Fix a proper closed ambient halfspace \(H=\{(z,y):\alpha\cdot z+\beta\cdot y\geq b\}\), with \((\alpha,\beta)\ne(0,0)\), and write \(H_m:=\{y:(m,y)\in H\}\). If \(p_m\in H\) and \(\beta\ne0\), then \(H_m\) is a proper closed halfspace containing \(x_m\), so the preceding depth bound applies. If \(p_m\in H\) and \(\beta=0\), then \(H_m=\mathbb R^d\), and \(\operatorname{vol}_d(C_m\cap H_m)=a_m\geq e_m\geq\gamma_de_m\). Therefore
\[
\begin{aligned}
\sigma(H)
&=\gamma_d\sum_{\substack{m\in E\\p_m\in H}}e_m\\
&\leq\sum_{\substack{m\in E\\p_m\in H}}
\operatorname{vol}_d(C_m\cap H_m)
\leq\mu_C(H).
\end{aligned}
\]
The last sum charges each physical target fiber at most once. No source-pair occurrences are added within a target, including collisions between different parity classes; reuse of a source in different selected pairs causes no repeated target charge. All choices were fixed before \(H\). The whole-space and empty improper halfspaces, if included, satisfy the same inequality because \(e_m\leq a_m\) and \(0<\gamma_d\leq1\). This proves halfspace domination. It does not imply Borel-set domination: each atom has positive \(\sigma\)-mass but zero \(\mu_C\)-mass since \(d\geq1\).

At a diagonal target \(m=z\in A\), the pair \((z,z)\) gives \(e_z\geq t_z\). As \(A\subseteq E\) and all envelope weights are positive, summing these inequalities gives \(\sum_{m\in E}e_m\geq\sum_{z\in A}t_z\). Summing \(e_m\leq a_m\) over distinct targets gives \(\sum_{m\in E}e_m\leq W\). Every midpoint lies in \(\operatorname{aff}A\), while the diagonals give \(A\subseteq E\); hence \(\operatorname{aff}E=\operatorname{aff}A\), with dimension \(\rho\).

Applying `6769574fc1bd9f8d` to the source points and repeating the same one-charge-per-fiber argument shows that \(\gamma_d\sum_{z\in A}t_z\delta_{(z,q_z)}\) is also a nonzero positive finite measure carried by \(S\) and halfspace-dominated by \(\mu_C\). The residual-rank attainment assertion of `be359f8a6c628483` therefore applies to both this source measure and \(\sigma\). Their supports are exactly their finite graphs because all their weights are positive, and their base affine hulls both equal \(\operatorname{aff}A\). This establishes attainment of both displayed minima, including zero-dimensional base or residual cases.

For any affine \(s:\operatorname{aff}A\to\mathbb R^d\), midpoint averaging gives
\[
x_m-s(m)=
\frac{(q_{z_m}-s(z_m))+(q_{z'_m}-s(z'_m))}{2}
\qquad(m\in E).
\]
Thus every target residual belongs to the span of the source residuals for the same map \(s\). Choose a map attaining \(r_{\mathrm{src}}\); minimizing over target maps then yields \(r_{\mathrm{mid}}\leq r_{\mathrm{src}}\). This argument holds for every fixed choice of maximizing pairs and supplies no absolute upper bound for either rank.

Choose an affine map attaining \(r_{\mathrm{mid}}\). In the capacity definition, take the selector index set \(F=E\), selector points \(v_m=x_m\), and weights \(w_m=\gamma_de_m\). The already proved inequalities \(0<w_m\leq\delta_C(m,x_m)\) and \(E\subseteq D_+\) make these admissible selector data. Their base rank is \(\rho\) and their residual rank for the chosen map is \(r_{\mathrm{mid}}\). Substitution gives the first capacity lower bound, and \(r_{\mathrm{mid}}\leq r_{\mathrm{src}}\) gives the second. This uses exactly the normalization in equations (20)-(22) of `be359f8a6c628483`, where \(h_{\max}(C)\geq2^{-n}R_{\mathrm{sel}}(C)\).

To obtain one point with the asserted simultaneous halfspace guarantee, apply the dominated-measure theorem of `be359f8a6c628483` directly to \(\sigma\). All its hypotheses have been checked, and its parameters are \(|\sigma|=\gamma_d\sum_{m\in E}e_m\), \(\rho_\sigma=\rho\), and \(r_\sigma=r_{\mathrm{mid}}\). It yields \(p^\star\in S\) such that every closed ambient halfspace \(H\ni p^\star\) satisfies \(\mu_C(H)\geq\sigma(H)\geq\gamma_d\sum_{m\in E}e_m/[2^\rho(r_{\mathrm{mid}}+1)]\). Taking the infimum over these halfspaces proves the depth bound, and the comparison with \(r_{\mathrm{src}}\) follows again from rank nonincrease.

Finally, suppose the full-volume data are used. For any positive-volume fiber, the density \(\mathbf1_{C_z}\) shows \(c_z\in\mathsf M_{a_z}(C_z)\), so these data are admissible. Feasibility gives \(E\subseteq D_+\), and the diagonals give the reverse inclusion. For \(m\in D_+\), the diagonal pair gives \(e_m\geq a_m\), while feasibility gives \(e_m\leq a_m\); hence \(e_m=a_m\). If \(f\) represents a point of \(\mathsf M_{a_m}(C_m)\), then \(0\leq f\leq1\) on \(C_m\) and \(\int_{C_m}(1-f)=0\), so \(f=1\) almost everywhere on \(C_m\). Therefore \(\mathsf M_{a_m}(C_m)=\{c_m\}\), and membership forces \(x_m=c_m\) for every maximizing-pair choice. The stated measure, total mass, and equality of the two residual ranks now follow from equality of the source and target graphs. This proves the calibration and completes the theorem.

## External sources

none
