---
fact_id: 2b3bed05ecbcf74a
kind: lemma
author: "research-agent"
assurance: LLM-verified
subgoal_id: atlas-to-common-full-rank-chart
depends_on: ["179add32aa016da1","1c54f5dc74c15059","be359f8a6c628483","c1e3b8400d5b5b10","f44e38de6bcf9626"]
verifier_run: acd5cee8139a43b1
target_match: null
---

## Statement

Let \(n\geq2\), \(d\geq1\), and let \(C\subseteq\mathbb R^n\times\mathbb R^d\) be a convex body. Retain the canonical notation
\[
 C_z:=\{x:(z,x)\in C\},\qquad
 a_z:=\operatorname{vol}_d(C_z),\qquad
 Z:=\{z\in\mathbb Z^n:a_z>0\},\qquad
 W:=\sum_{z\in Z}a_z>0,
\]
\[
 c_z:=a_z^{-1}\int_{C_z}x\,dx,\qquad
 \gamma_k:=\left(\frac{k}{k+1}\right)^k\quad(k\geq1).
\]
Use the capacities \(M_{\rm off}(C)\) and \(R_{\rm cloud}(C)\) in the exact normalization of accepted facts `179add32aa016da1` and `c1e3b8400d5b5b10`.

For every base parity class \(\xi\), put
\[
 A_\xi:=\sum_{z\equiv\xi\pmod2}a_z,
 \qquad
 M_\xi:=\max_{z\equiv\xi\pmod2}a_z,
 \qquad
 \mathcal G:=\{\xi:A_\xi>0,\ M_\xi\leq A_\xi/4\},
\]
with \(M_\xi=0\) when the class is empty. Define the strong canonical product matching by
\[
 q^\times_{\{u,v\}}:=\frac{\gamma_da_ua_v}{A_\xi}
 \quad(u\ne v,\ u\equiv v\equiv\xi\pmod2),
\]
and set its other entries to zero. Let \(r=(r_e)\) be the positive-overlap submatching of accepted fact `f44e38de6bcf9626`. The properties of \(r\) needed here are exactly
\[
 0\leq r_e\leq\frac12q^\times_e,
 \qquad
 r_e=0\text{ outside }\mathcal G.
\tag{1}
\]
Let \(\vartheta\) be its accepted optimal transverse pairing, or any feasible transverse pairing with the same capacity constraints. Thus a positive pairing has a unique common endpoint, can be labeled
\[
 \sigma=(z;e,f),\qquad e=\{z,a\},\quad f=\{z,b\},
 \qquad \theta_\sigma:=\vartheta_{\{e,f\}}>0,
\]
and
\[
 \sum_{f:\{e,f\}\text{ transverse}}\vartheta_{\{e,f\}}
 \leq r_e.
\tag{2}
\]
Retain the complete original labeled atlas of accepted fact `1c54f5dc74c15059`, with actual midpoint base and actual point
\[
 m_\sigma:=\frac{a+b}{2},\qquad
 X_\sigma:=\frac{x_{e,a}+x_{f,b}}2.
\]
No label or physical source occurrence is discarded below. Write
\[
 P:=\sum_\sigma\theta_\sigma>0.
\]

For an arbitrary subfamily \(\mathscr Q\) of its positive labels, aggregate only equal unordered opposite source pairs:
\[
 \Gamma_g^{\mathscr Q}:=
 \sum_{\substack{\sigma=(z;e,f)\in\mathscr Q\\
                  e=\{z,a\},\ f=\{z,b\},\ g=\{a,b\}}}
 \theta_\sigma,
 \qquad
 P_{\mathscr Q}:=\sum_{\sigma\in\mathscr Q}\theta_\sigma.
\tag{3}
\]
For \(g=\{a,b\}\), put
\[
 m_g:=\frac{a+b}{2},\qquad
 \bar c_g:=\frac{c_a+c_b}{2},
\]
and define, with coincident atoms aggregated,
\[
 \tau_{\mathscr Q}:=
 \sum_g\Gamma_g^{\mathscr Q}\delta_{(m_g,\bar c_g)}.
\tag{4}
\]
Here \(\tau_{\mathscr Q}\) is a centroid measure at the actual atlas bases. Its continuous coordinates are \(\bar c_g\), not \(X_\sigma\); no identification of these two points is claimed.

There is a single exact minimum-unmatched centroid matching \(\lambda^{\mathscr A}\), chosen from the entire atlas before \(\mathscr Q\), such that
\[
 \boxed{
 \Gamma_g^{\mathscr A}\leq\lambda_g^{\mathscr A}
 \quad\text{for every }g,
 \qquad
 0\leq\tau_{\mathscr Q}\leq
 \nu_{\rm off}^{\lambda^{\mathscr A}},
 \qquad
 |\tau_{\mathscr Q}|=P_{\mathscr Q}.}
\tag{5}
\]
The exact minimum-unmatched normalization in (5) has vertex capacities \(b_z:=\gamma_da_z\), as in accepted fact `be359f8a6c628483`. In particular, \(\tau_{\mathscr Q}\) is halfspace-dominated by the mixed-volume measure of \(C\).

If \(P_{\mathscr Q}>0\), define
\[
 \rho_{\mathscr Q}:=
 \dim\operatorname{aff}\{m_\sigma:\sigma\in\mathscr Q\},
 \qquad
 r_{\mathscr Q}^{\rm tgt}:=
 \dim\operatorname{aff}(\operatorname{supp}\tau_{\mathscr Q})
 -\rho_{\mathscr Q}.
\tag{6}
\]
Then
\[
 \boxed{
 M_{\rm off}(C)\geq
 2^{n-\rho_{\mathscr Q}}
 \frac{P_{\mathscr Q}}{r_{\mathscr Q}^{\rm tgt}+1}.}
\tag{7}
\]

For any integral midpoint \(m\), put
\[
 P_{\mathscr Q,m}:=
 \sum_{\substack{\sigma\in\mathscr Q\\m_\sigma=m}}
 \theta_\sigma.
\tag{8}
\]
Whenever \(P_{\mathscr Q,m}>0\), one has \(m\in Z\). Define the nonempty target centroid cloud rank
\[
 r_{\mathscr Q,m}^{\rm tgt}:=
 \dim\operatorname{aff}
 \{\bar c_g:\Gamma_g^{\mathscr Q}>0,\ m_g=m\}.
\tag{9}
\]
Then the sharper collision certificate is
\[
 \boxed{
 R_{\rm cloud}(C)\geq
 \frac{2\gamma_{2d}}{\gamma_d}\,
 2^n\frac{P_{\mathscr Q,m}}
 {r_{\mathscr Q,m}^{\rm tgt}+1}.}
\tag{10}
\]
The coefficient \(2\gamma_{2d}/\gamma_d\) is strictly greater than \(4/e\).

Thus, if for some \(\varepsilon>0\) both terminal capacities are smaller than \(\varepsilon W\), every nonzero subfamily and every occupied target collision class satisfy
\[
 r_{\mathscr Q}^{\rm tgt}+1>
 \frac{2^{n-\rho_{\mathscr Q}}P_{\mathscr Q}}
 {\varepsilon W},
\tag{11}
\]
\[
 r_{\mathscr Q,m}^{\rm tgt}+1>
 \frac{2\gamma_{2d}}{\gamma_d}\,
 \frac{2^nP_{\mathscr Q,m}}{\varepsilon W}.
\tag{12}
\]
These are necessary dispersion conditions at the atlas target bases. They make no assertion that these ranks are bounded or that the original actual points \(X_\sigma\) lie on one affine simplex roof.

## Proof

Accepted fact `f44e38de6bcf9626` gives (1), since its overlap is bounded by its cap-synchronized soft weights and those soft weights are at most \(q^\times_e/2\). The good-class support is the one synchronized in accepted fact `179add32aa016da1`. The full original atlas is the labeled atlas of accepted fact `1c54f5dc74c15059`, because (2) is in particular feasible under the canonical stress loads.

We first prove the degree bound for the squared opposite pairs, retaining every occurrence. For a physical source base \(y\), define
\[
 d_y(\Gamma^{\mathscr Q}):=
 \sum_{g\ni y}\Gamma_g^{\mathscr Q}.
\]
An original label \(\sigma=(z;\{z,a\},\{z,b\})\) contributes once at each of its opposite physical source bases \(a,b\). If it contributes at \(y=a\), charge that occurrence to the source edge \(\{z,y\}\), paired at its other endpoint \(z\). For each fixed source edge, the charged subfamily is a subset of all its pairings, whose total is at most \(r_e\) by (2). Consequently
\[
 d_y(\Gamma^{\mathscr Q})
 \leq\sum_{e\ni y}r_e
 \leq\frac12d_y(q^\times)
 \leq\frac{\gamma_da_y}{2}
 =\frac{b_y}{2}.
\tag{13}
\]
The last product degree bound follows directly from
\[
 d_y(q^\times)
 =\gamma_da_y\frac{A_\xi-a_y}{A_\xi}
 \leq\gamma_da_y
\]
in its parity class. Pairing transversality ensures distinct source edges and hence \(a\ne b\). All three source bases have the same good parity. Thus every positive opposite pair is off-diagonal, same-parity, and supported in a class of \(\mathcal G\). Aggregating equal opposite pairs in (3) changes none of these degree counts, and preserves total mass:
\[
 \sum_g\Gamma_g^{\mathscr Q}=P_{\mathscr Q}.
\tag{14}
\]

We next extend the full opposite-pair matching to an exact host. Set \(\Gamma:=\Gamma^{\mathscr A}\). Fix a good parity class \(\xi\), and write
\[
 B_\xi:=\sum_{z\equiv\xi}b_z=\gamma_dA_\xi,
 \qquad
 \beta_\xi:=\max_{z\equiv\xi}b_z
 =\gamma_dM_\xi\leq\frac{B_\xi}{4}.
\]
Define the residual capacities in this class by
\[
 b'_z:=b_z-d_z(\Gamma).
\]
By (13), \(b'_z\geq b_z/2>0\). If \(B'_\xi:=\sum_{z\equiv\xi}b'_z\), then
\[
 B'_\xi\geq\frac{B_\xi}{2},\qquad
 \max_{z\equiv\xi}b'_z\leq\beta_\xi
 \leq\frac{B_\xi}{4}\leq\frac{B'_\xi}{2}.
\tag{15}
\]
The finite fractional matching construction proved in accepted fact `be359f8a6c628483` applies to these residual capacities. Its minimum-unmatched formula is zero when the largest capacity is at most half their sum. Hence (15) supplies an off-diagonal same-parity matching \(\zeta^\xi\) with
\[
 d_z(\zeta^\xi)=b'_z
 \quad(z\equiv\xi).
\]
Set \(\lambda^{\mathscr A}_g:=\Gamma_g+\zeta^\xi_g\) on this class. It has degrees exactly \(b_z\), dominates \(\Gamma\) edgewise, and has zero unmatched mass. This is the required minimum-unmatched mass for the original capacities because \(\beta_\xi\leq B_\xi/4\).

On each nonempty class outside \(\mathcal G\), the full \(\Gamma\) is zero. Choose the exact minimum-unmatched matching for the original capacities \(b_z\) supplied by the same accepted fact. Empty classes contribute nothing. Combining the choices over all parity classes gives one exact minimum-unmatched centroid matching \(\lambda^{\mathscr A}\) which dominates \(\Gamma\) on every edge. It is chosen from the full atlas and does not depend on the later subfamily.

Because \(0\leq\Gamma_g^{\mathscr Q}\leq\Gamma_g\), edgewise domination gives the measure inequality in (5) after every coincident atom is aggregated. Equations (4) and (14) give its exact mass. Accepted fact `be359f8a6c628483` makes the exact host halfspace-dominated by the mixed-volume measure, so its positive submeasure \(\tau_{\mathscr Q}\) has the same domination.

When \(P_{\mathscr Q}>0\), this measure has nonempty support. Its base support is exactly \(\{m_\sigma:\sigma\in\mathscr Q\}\). Therefore (6) is precisely the intrinsic base rank and continuous residual rank used in the definition of \(M_{\rm off}\) in accepted fact `c1e3b8400d5b5b10`. The single host \(\lambda^{\mathscr A}\) is an admissible exact matching in that supremum, and \(\tau_{\mathscr Q}\) is its admissible nonzero submeasure. Substitution of its mass proves (7).

It remains to prove the sharper collision charge. Fix \(m\) with \(P_{\mathscr Q,m}>0\). Some positive opposite pair \(g=\{a,b\}\) has midpoint \(m\), and both endpoint fibers have positive volume. Each contains an open ball; convexity of \(C\) puts their Minkowski midpoint in \(C_m\), so \(a_m>0\).

For every positive opposite pair in this midpoint slice, (13) gives
\[
 \Gamma_g^{\mathscr Q}
 \leq\min\{d_a(\Gamma^{\mathscr Q}),
            d_b(\Gamma^{\mathscr Q})\}
 \leq\frac{\gamma_d}{2}\min\{a_a,a_b\}.
\tag{16}
\]
Distinct unordered pairs with midpoint \(m\) correspond to distinct unordered reflected pairs \(\{v,-v\}\), where \(a=m+v\), \(b=m-v\), and \(v\ne0\). Take exactly these reflected-pair components, with no central component, in the reflected-centroid-cloud definition of accepted fact `c1e3b8400d5b5b10`. Its cloud points are exactly the \(\bar c_g\) in (9), so its rank is \(r_{\mathscr Q,m}^{\rm tgt}\). Its energy is
\[
 \gamma_{2d}
 \sum_{\substack{g:\Gamma_g^{\mathscr Q}>0\\m_g=m}}
 \min\{a_a,a_b\}
 \geq\frac{2\gamma_{2d}}{\gamma_d}
 \sum_{g:m_g=m}\Gamma_g^{\mathscr Q}
 =\frac{2\gamma_{2d}}{\gamma_d}P_{\mathscr Q,m},
\]
where (16) accounts for the complete aggregated occurrence weight of each reflected pair. The cloud capacity definition proves (10). The elementary inequalities
\[
 \gamma_d\leq\frac12,\qquad
 \gamma_{2d}>e^{-1}
\]
follow respectively from \((1+1/d)^d\geq2\) and \(\log(1+1/(2d))<1/(2d)\). Hence \(2\gamma_{2d}/\gamma_d>4/e\).

Finally, combine (7) and (10) with the two strict terminal-smallness assumptions and rearrange to obtain (11) and (12). No target metronoid masses or depths from different opposite pairs were added. The aggregation in this proof is of matching weights and centroid atoms inside one actual exact host, and the cloud charge uses its accepted reflected-pair energy formula. Neither operation combines incompatible simplex charts or supplies the remaining global simplex extraction.

## External sources

none
