---
fact_id: ab9d324f5bcb30fd
kind: lemma
author: "research-agent"
assurance: LLM-verified
subgoal_id: dyadic-stress-frame-aggregation
depends_on: ["036a276c54ec5e66","32aedd8da549416a","6769574fc1bd9f8d","e0dcff96f9b90a96"]
verifier_run: 2647f6c1c5464b4f
target_match: null
---

## Statement

Retain the canonical hard-branch hypotheses, objects, and notation of accepted facts `036a276c54ec5e66`, `32aedd8da549416a`, and `e0dcff96f9b90a96`. Thus \(n,d\in\mathbb Z_{>0}\), \(C\subseteq\mathbb R^n\times\mathbb R^d\) is a convex body, and
\[
 C_y:=\{x\in\mathbb R^d:(y,x)\in C\},
 \qquad
 a_y:=\operatorname{vol}_d(C_y),
 \qquad
 \gamma_d:=\left(\frac d{d+1}\right)^d.
\]
For every positive-volume fiber, put
\[
 \mathcal K_y:=\mathsf M_{a_y/2}(C_y).
\]
For a Borel set \(B\subseteq\mathbb R^{n+d}\), let
\[
 \mu_C(B):=
 \sum_{y\in\mathbb Z^n}
 \operatorname{vol}_d\{x\in C_y:(y,x)\in B\},
\]
and, for \(x\in C_y\), let
\[
 \delta_C(y,x):=
 \inf_{\substack{J\subseteq\mathbb R^d\ \mathrm{closed\ halfspace}\\x\in J}}
 \operatorname{vol}_d(C_y\cap J).
\]

Let \(\mathcal E_{\mathrm{miss}}\) be the fixed endpoint-disjoint same-parity matching of accepted fact `e0dcff96f9b90a96`, with positive weights \(t_E\). If \(E=\{u,w\}\in\mathcal E_{\mathrm{miss}}\), then
\[
 u\ne w,
 \qquad
 u\equiv w\pmod 2,
 \qquad
 0<t_E\leq\frac{a_u}{4},
 \qquad
 0<t_E\leq\frac{a_w}{4}.
\tag{1}
\]
Retain the rescaled internal atlas, its loop subfamily, its positive label weights \(\eta_\sigma\), and its original occurrence contacts from that accepted fact. For an edge \(E=\{u,w\}\), write
\[
 \mathscr L_E:=
 \{\sigma\in\mathscr A_{\mathrm{loop}}:
 e_2(a(\sigma))=E\},
 \qquad
 \ell_E:=\sum_{\sigma\in\mathscr L_E}\eta_\sigma.
\tag{2}
\]
Thus \(\ell_E\) is exactly the numerical loop mass denoted by \(L_E\) in accepted fact `e0dcff96f9b90a96`; the new notation avoids collision with the canonical edge body below. Put
\[
 H_{\mathrm{loop}}:=\sum_{E\in\mathcal E_{\mathrm{miss}}}\ell_E,
 \qquad
 \mathcal E_{\mathrm{loop}}^+:=
 \{E\in\mathcal E_{\mathrm{miss}}:\ell_E>0\}.
\tag{3}
\]
For \(E=\{u,w\}\in\mathcal E_{\mathrm{loop}}^+\), every \(\sigma\in\mathscr L_E\) has opposite endpoint pair \(E\). If \(x_{\sigma,y}\) denotes its original occurrence contact at \(y\in E\), the aggregate points of accepted fact `e0dcff96f9b90a96` satisfy
\[
 \bar x_{E,y}
 =\frac1{\ell_E}
 \sum_{\sigma\in\mathscr L_E}
 \eta_\sigma x_{\sigma,y}
 \qquad(y\in E).
\tag{4}
\]
Define
\[
 m_E:=\frac{u+w}{2},
 \qquad
 Y_E:=\frac{\bar x_{E,u}+\bar x_{E,w}}2,
 \qquad
 \beta_E:=
 \left(\frac{a_u^{1/d}+a_w^{1/d}}2\right)^d,
\tag{5}
\]
and call
\[
 \mathcal L_E:=\frac12(\mathcal K_u+\mathcal K_w)
\tag{6}
\]
the canonical edge body. This \(\mathcal L_E\) is exactly the body denoted by \(L_{uw}\) in accepted fact `32aedd8da549416a`, and it is not the numerical loop mass \(\ell_E\).

Then, for every \(E=\{u,w\}\in\mathcal E_{\mathrm{loop}}^+\),
\[
 \boxed{\bar x_{E,u}\in\mathcal K_u,
 \qquad
 \bar x_{E,w}\in\mathcal K_w,}
\tag{7}
\]
\[
 \boxed{
 Y_E\in\mathcal L_E
 \subseteq\mathsf M_{\beta_E/2}(C_{m_E}),}
\tag{8}
\]
and
\[
 \boxed{
 \delta_C(m_E,Y_E)
 \geq\frac{\gamma_d\beta_E}{2}
 \geq2\gamma_dt_E.}
\tag{9}
\]

The positive measure
\[
 \boxed{
 \nu_{\mathrm{loop}}^t
 :=2\gamma_d
 \sum_{E\in\mathcal E_{\mathrm{loop}}^+}
 t_E\,\delta_{(m_E,Y_E)}}
\tag{10}
\]
is carried by \(C\cap(\mathbb Z^n\times\mathbb R^d)\) and is globally halfspace-dominated:
\[
 \boxed{
 \nu_{\mathrm{loop}}^t(H)\leq\mu_C(H)}
\tag{11}
\]
for every closed ambient halfspace \(H\subseteq\mathbb R^{n+d}\), including after coincident target atoms are aggregated. Its mass satisfies
\[
 \boxed{
 |\nu_{\mathrm{loop}}^t|
 =2\gamma_d
 \sum_{E\in\mathcal E_{\mathrm{loop}}^+}t_E
 \geq2\gamma_dH_{\mathrm{loop}}.}
\tag{12}
\]
Consequently, in the loop branch
\(H_{\mathrm{loop}}\geq H_{\mathrm{cross}}\) of accepted fact `e0dcff96f9b90a96`,
\[
 \boxed{
 |\nu_{\mathrm{loop}}^t|
 >\frac{7\gamma_d}{400}Q.}
\tag{13}
\]

Equations (7)--(13) are edgewise and measure-theoretic. They do not produce one affine map whose value at every \(m_E\) is \(Y_E\), and therefore do not produce a common affine selector for the bodies \(\mathcal L_E\). The guaranteed constant in (13) also remains below the hard threshold, since \(\gamma_d\leq1/2\) gives \(7\gamma_d/400\leq7/800<1/100\). Thus this composition is nonterminal without an additional compatible multi-edge selection or aggregation theorem.

## Proof

Fix \(E=\{u,w\}\in\mathcal E_{\mathrm{loop}}^+\). For each \(y\in E\), accepted fact `e0dcff96f9b90a96` defines
\[
 G_{E,y}:=
 \sum_{\sigma\in\mathscr L_E}\widetilde g_{\sigma,y},
 \qquad
 \bar x_{E,y}:=
 \frac1{\ell_E}\int_{C_y}xG_{E,y}(x)\,dx.
\tag{14}
\]
Every density \(\widetilde g_{\sigma,y}\) has mass \(\eta_\sigma\) and barycenter \(x_{\sigma,y}\). Expanding the first moment in (14) therefore proves (4).

Accepted fact `036a276c54ec5e66` states that every original occurrence contact at the physical endpoint \(y\) belongs to the canonical half-metronoid \(\mathcal K_y\). The coefficients \(\eta_\sigma/\ell_E\) in (4) are positive and sum to one. Since \(\mathcal K_y\) is convex, (4) gives
\[
 \bar x_{E,y}\in\mathcal K_y
 \qquad(y\in E),
\]
which proves (7). Averaging the two endpoint inclusions and using (5)--(6) gives
\[
 Y_E\in\frac12(\mathcal K_u+\mathcal K_w)
 =\mathcal L_E.
\tag{15}
\]

The endpoints \(u,w\) are distinct positive-volume bases of the same parity by (1). Part 1 of accepted fact `32aedd8da549416a` therefore applies to this pair and gives
\[
 \mathcal L_E
 \subseteq\mathsf M_{\beta_E/2}(C_{m_E}).
\tag{16}
\]
This proves (8), and in particular shows that \(a_{m_E}>0\). Applying the metronoid-depth inclusion of accepted fact `6769574fc1bd9f8d` to (8) yields
\[
 \delta_C(m_E,Y_E)
 \geq\gamma_d\frac{\beta_E}{2}.
\tag{17}
\]
The quarter-capacity bounds (1) imply \(a_u,a_w\geq4t_E\), so
\[
 \beta_E^{1/d}
 =\frac{a_u^{1/d}+a_w^{1/d}}2
 \geq(4t_E)^{1/d}.
\tag{18}
\]
Hence \(\beta_E\geq4t_E\). Combining this with (17) proves (9).

We next prove simultaneous domination without summing the target-fiber depth bounds in (9). Let \(H\subseteq\mathbb R^{n+d}\) be a closed ambient halfspace. For every labelled edge \(E=\{u,w\}\in\mathcal E_{\mathrm{loop}}^+\) whose atom \((m_E,Y_E)\) lies in \(H\), at least one of
\[
 (u,\bar x_{E,u}),
 \qquad
 (w,\bar x_{E,w})
\tag{19}
\]
lies in \(H\), because \((m_E,Y_E)\) is their midpoint. Orient \(E\) toward one such endpoint, choosing arbitrarily if both work. Since \(\mathcal E_{\mathrm{miss}}\) is endpoint-disjoint, distinct oriented edges use distinct physical source bases, even when their target midpoints or full target atoms coincide.

Suppose that \(E\) is oriented toward \(y\in E\), and write
\[
 H_y:=\{x\in\mathbb R^d:(y,x)\in H\}.
\tag{20}
\]
By (7), this fiber section contains
\(\bar x_{E,y}\in\mathcal K_y=\mathsf M_{a_y/2}(C_y)\). Accepted fact `6769574fc1bd9f8d` gives
\[
 \operatorname{vol}_d(C_y\cap H_y)
 \geq\frac{\gamma_da_y}{2}
 \geq2\gamma_dt_E,
\tag{21}
\]
where the last inequality is (1). The same accepted fact covers a whole-space fiber section under its improper-halfspace convention; an empty section cannot contain \(\bar x_{E,y}\).

Summing (21) over the distinct oriented source bases gives
\[
 \begin{aligned}
 \nu_{\mathrm{loop}}^t(H)
 &=2\gamma_d
 \sum_{\substack{E\in\mathcal E_{\mathrm{loop}}^+\\(m_E,Y_E)\in H}}
 t_E\\
 &\leq
 \sum_{\text{oriented source bases }y}
 \operatorname{vol}_d(C_y\cap H_y)
 \leq\mu_C(H).
 \end{aligned}
\tag{22}
\]
This proves (11). The proof charges each labelled edge to a distinct endpoint fiber before aggregating target atoms, so it is collision-safe and does not add the numerical midpoint depths in (9). Equation (8), together with the metronoid containment in the underlying convex body from accepted fact `6769574fc1bd9f8d`, shows that every atom of (10) is carried by \(C\cap(\mathbb Z^n\times\mathbb R^d)\).

It remains to prove the mass bounds. For either endpoint \(y\in E\), the endpoint-capacity inequality in accepted fact `e0dcff96f9b90a96` bounds the total weight of all internal labels incident to \(y\) by \(t_E\). The loop family \(\mathscr L_E\) is a subfamily of those labels and has total weight \(\ell_E\), so
\[
 \ell_E\leq t_E.
\tag{23}
\]
Also, every loop label belongs to exactly one \(\mathscr L_E\), whence
\[
 H_{\mathrm{loop}}
 =\sum_{E\in\mathcal E_{\mathrm{loop}}^+}\ell_E.
\tag{24}
\]
Equations (10), (23), and (24) prove (12).

Finally, accepted fact `e0dcff96f9b90a96` gives
\[
 H_{\mathrm{loop}}+H_{\mathrm{cross}}
 >\frac7{400}Q.
\tag{25}
\]
In the loop branch \(H_{\mathrm{loop}}\geq H_{\mathrm{cross}}\), equation (25) implies
\[
 H_{\mathrm{loop}}>\frac7{800}Q.
\tag{26}
\]
Combining (12) and (26) proves the strict inequality (13). The inequality \(\gamma_d\leq1/2\) follows from \((1+1/d)^d\geq2\), and gives the stated numerical non-closure calibration. No step constructs a common affine map across different positive loop edges, so the final limitation follows.

## External sources

none
