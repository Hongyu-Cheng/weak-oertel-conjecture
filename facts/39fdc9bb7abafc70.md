---
fact_id: 39fdc9bb7abafc70
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: zero-fresh-circuitwise-full-dilation-cap-ledger
depends_on: ["1491820ca8e0cf99","6769574fc1bd9f8d","c7c47ab9a769716a"]
verifier_run: 9a930dcfe4fa4ef5
target_match: null
---

## Statement

Let \(n,d\in\mathbb Z_{>0}\), let \(Q>0\), let \(C\subseteq\mathbb R^n\times\mathbb R^d\) be a convex body of positive mixed volume, and write
\[
C_z:=\{x\in\mathbb R^d:(z,x)\in C\},
\qquad
a_z:=\operatorname{vol}_d(C_z),
\qquad
\gamma_d:=\left(\frac d{d+1}\right)^d,
\]
\[
\mu_C(H):=\sum_{z\in\mathbb Z^n}
\operatorname{vol}_d\{x\in C_z:(z,x)\in H\}
\]
for every closed ambient halfspace \(H\). Whenever \(a_z>0\), let \(c_z\) be the centroid of \(C_z\), and put
\[
\mathsf M_s(C_z):=
\left\{
\frac1s\int_{C_z}x\rho(x)\,dx:
0\leq\rho\leq1\ \text{a.e.},\quad \int_{C_z}\rho=s
\right\}
\quad(0<s\leq a_z),
\]
\[
\mathcal K_z:=\mathsf M_{a_z/2}(C_z),
\qquad
D_z:=\mathcal K_z-c_z.
\tag{1}
\]

For finite measures, write \(\nu\preceq_{\mathrm{hs}}\mu\) when
\(\nu(H)\leq\mu(H)\) for every closed ambient halfspace \(H\). For every nonempty compact convex \(K\subseteq\mathbb R^d\), use
\[
h_K(w):=\max_{x\in K}\langle w,x\rangle,
\qquad
F_K(w):=\{x\in K:\langle w,x\rangle=h_K(w)\}.
\]

Retain one complete circuitwise system and one simultaneous contact choice from accepted fact `c7c47ab9a769716a`. Thus \(I\) and \(\mathscr A\) are finite nonempty sets. Every \(j\in I\) has two distinct positive-volume source fibers \(z_j^-\) and \(z_j^+\), the physical target
\[
m_j:=\frac{z_j^-+z_j^+}{2}\in\mathbb Z^n,
\]
and the pair body
\[
L_j:=\frac12(\mathcal K_{z_j^-}+\mathcal K_{z_j^+})
\subseteq\mathsf M_{\vartheta_j}(C_{m_j})
\quad\text{for some }\vartheta_j>0.
\tag{2}
\]
There are positive saturated loads \(q_j^{\mathrm{sat}}>0\) and nonnegative circuit loads \(q_j^\alpha\) such that
\[
\sum_{\alpha\in\mathscr A}q_j^\alpha=q_j^{\mathrm{sat}}
\quad(j\in I),
\qquad
\Omega_b:=\sum_jq_j^{\mathrm{sat}}>
\frac{97}{100}Q,
\tag{3}
\]
\[
\sum_jq_j^{\mathrm{sat}}
\bigl(\mathbf1_{\{z_j^-=z\}}+\mathbf1_{\{z_j^+=z\}}\bigr)
\leq\frac{a_z}{4}
\quad(z\in\mathbb Z^n),
\tag{4}
\]
\[
\sum_{j:m_j=m}\frac{q_j^{\mathrm{sat}}}{\vartheta_j}\leq1
\quad(m\in\mathbb Z^n).
\tag{5}
\]
For every \(\alpha\in\mathscr A\), define
\[
\Omega_\alpha:=\sum_jq_j^\alpha>0,
\qquad
\pi_i^\alpha:=\frac{q_i^\alpha}{\Omega_\alpha}
\quad(i\in I).
\tag{6}
\]
The canonical nonzero directions \(u_i\in\mathbb R^d\) satisfy
\[
\sum_i\pi_i^\alpha=1,
\qquad
\sum_i\pi_i^\alpha u_i=0.
\tag{7}
\]
Fix simultaneously
\[
\ell_i\in F_{L_i}(u_i),
\qquad
p_{ij}\in F_{L_j}(u_i)
\quad(i,j\in I),
\qquad
p_{ii}=\ell_i.
\tag{8}
\]
Put
\[
\Delta_\alpha:=-\sum_jq_j^\alpha h_{L_j}(u_j)>0,
\qquad
\Psi_\alpha:=\sum_jq_j^\alpha
\sum_i\pi_i^\alpha h_{L_j}(u_i)\geq0,
\tag{9}
\]
\[
t_\alpha:=\frac{\Delta_\alpha}
{\Delta_\alpha+\Psi_\alpha}\in(0,1].
\tag{10}
\]
Let \(\mathcal O_\alpha\) and \(\mathcal T_\alpha\) be the stationary and transport quantities of accepted fact `c7c47ab9a769716a`; explicitly, with
\[
a_{ij}^\alpha:=(1-t_\alpha)q_i^\alpha\mathbf1_{\{i=j\}}
+t_\alpha q_i^\alpha\pi_j^\alpha,
\]
they are
\[
\mathcal O_\alpha:=\sum_{i,j}a_{ij}^\alpha
\bigl(h_{L_j}(u_i)-\langle u_i,\ell_j\rangle\bigr),
\qquad
\mathcal T_\alpha:=\sum_{i,j}a_{ij}^\alpha
\langle u_i,\ell_j-\ell_i\rangle,
\tag{11}
\]
and they satisfy
\[
\mathcal O_\alpha=(1-t_\alpha)\Delta_\alpha,
\qquad
\mathcal T_\alpha=t_\alpha\Delta_\alpha,
\qquad
\mathcal O_\alpha+\mathcal T_\alpha=\Delta_\alpha.
\tag{12}
\]
Also set
\[
\Delta^{\mathrm{sat}}:=\sum_\alpha\Delta_\alpha>
\frac{97}{100}\delta_*Q,
\qquad
\delta_*:=\frac{3\log(4/3)}{\log2}-1>0,
\tag{13}
\]
and
\[
r_*:=\frac{\Delta^{\mathrm{sat}}}{\Omega_b},
\qquad
\mathscr G:=\left\{\alpha:
\Delta_\alpha\geq\frac{r_*}{2}\Omega_\alpha\right\}.
\tag{14}
\]
Then
\[
\sum_{\alpha\in\mathscr G}\Delta_\alpha>
\frac12\Delta^{\mathrm{sat}},
\qquad
\frac{\Delta_\alpha}{\Omega_\alpha}>
\frac{95}{194}\delta_*
\quad(\alpha\in\mathscr G).
\tag{15}
\]

For every used physical target, define
\[
E_{\mathrm{circ}}:=\left\{m\in\mathbb Z^n:
\eta_m:=\sum_{j:m_j=m}q_j^{\mathrm{sat}}>0\right\},
\tag{16}
\]
and \(0<\eta_m\leq a_m\) for every \(m\in E_{\mathrm{circ}}\). Put
\[
c_{\alpha j}:=\sum_i\pi_i^\alpha p_{ij},
\qquad
c_m^{\mathrm{circ}}:=\frac1{\eta_m}
\sum_\alpha\sum_{j:m_j=m}q_j^\alpha c_{\alpha j},
\tag{17}
\]
\[
g_{\alpha,ik}^{(j,m)}:=
\frac{t_\alpha q_j^\alpha}{2\eta_m}
\pi_i^\alpha\pi_k^\alpha(p_{ij}-p_{kj}),
\qquad
\widetilde g_{\alpha,ik}^{(j,m)}:=
\frac1{t_\alpha}g_{\alpha,ik}^{(j,m)}
=\frac{q_j^\alpha}{2\eta_m}
\pi_i^\alpha\pi_k^\alpha(p_{ij}-p_{kj}).
\tag{18}
\]
The original and full-box circuitwise switch bodies are
\[
\mathcal Z_m^{\mathrm{circ}}:=c_m^{\mathrm{circ}}
+\sum_\alpha\sum_{j:m_j=m}\sum_{i,k}
[-g_{\alpha,ik}^{(j,m)},g_{\alpha,ik}^{(j,m)}],
\tag{19}
\]
\[
\widetilde{\mathcal Z}_m^{\mathrm{circ}}:=c_m^{\mathrm{circ}}
+\sum_\alpha\sum_{j:m_j=m}\sum_{i,k}
[-\widetilde g_{\alpha,ik}^{(j,m)},
\widetilde g_{\alpha,ik}^{(j,m)}].
\tag{20}
\]
Define the full pooled body
\[
\mathcal P_m:=\frac1{\eta_m}
\sum_{j:m_j=m}q_j^{\mathrm{sat}}L_j.
\tag{21}
\]
Then, simultaneously for all circuits, targets, and contact choices in (8),
\[
\boxed{
\mathcal Z_m^{\mathrm{circ}}
\subseteq\widetilde{\mathcal Z}_m^{\mathrm{circ}}
\subseteq\mathsf M_{\eta_m/2}(C_m)}
\quad(m\in E_{\mathrm{circ}}),
\tag{22}
\]
and
\[
\boxed{
\widetilde{\mathcal Z}_m^{\mathrm{circ}}
\subseteq\mathcal P_m
\subseteq\mathsf M_{\eta_m}(C_m)}
\quad(m\in E_{\mathrm{circ}}).
\tag{23}
\]
The center \(c_m^{\mathrm{circ}}\) in (17) is circuit-weighted. Its definition is distinct from that of the global switch center in accepted fact `1491820ca8e0cf99`, namely
\[
c_m^{\mathrm{sw}}:=\frac1{\eta_m}
\sum_{j:m_j=m}q_j^{\mathrm{sat}}
\sum_i\frac{q_i^{\mathrm{sat}}}{\Omega_b}p_{ij},
\tag{24}
\]
and no equality between \(c_m^{\mathrm{circ}}\) and \(c_m^{\mathrm{sw}}\) is asserted.

Every generator-normal term in the following identity is nonnegative. More strongly, for every circuit subfamily \(\mathscr B\subseteq\mathscr A\),
\[
\boxed{
\sum_{m\in E_{\mathrm{circ}}}\eta_m
\sum_{\alpha\in\mathscr B}\sum_{j:m_j=m}\sum_{i,k}
\left\langle u_i-u_k,
\widetilde g_{\alpha,ik}^{(j,m)}\right\rangle
=\sum_{\alpha\in\mathscr B}\Psi_\alpha.}
\tag{25}
\]
In particular, the exact total full-box stationary energy is
\[
\sum_{m\in E_{\mathrm{circ}}}\eta_m
\sum_\alpha\sum_{j:m_j=m}\sum_{i,k}
\left\langle u_i-u_k,
\widetilde g_{\alpha,ik}^{(j,m)}\right\rangle
=\sum_\alpha\Psi_\alpha
=\sum_\alpha\frac{\mathcal O_\alpha}{t_\alpha}.
\tag{26}
\]

This energy has one simultaneous actual half-cap source ledger. For each \(z\in\mathbb Z^n\) and \(\alpha\in\mathscr A\), put
\[
\beta_z^\alpha:=\sum_jq_j^\alpha
\bigl(\mathbf1_{\{z_j^-=z\}}+\mathbf1_{\{z_j^+=z\}}\bigr),
\qquad
\beta_z:=\sum_\alpha\beta_z^\alpha.
\tag{27}
\]
Then
\[
\beta_z=\sum_jq_j^{\mathrm{sat}}
\bigl(\mathbf1_{\{z_j^-=z\}}+\mathbf1_{\{z_j^+=z\}}\bigr)
\leq\frac{a_z}{4},
\tag{28}
\]
\[
\sum_z\beta_z^\alpha=2\Omega_\alpha,
\qquad
\sum_z\beta_z=2\Omega_b.
\tag{29}
\]
For each \(z\) with \(\beta_z>0\) and each \(i\in I\), choose the threshold \(s_z(u_i)\) for which the actual top cap
\[
A_z(u_i):=\{x\in C_z:\langle u_i,x\rangle\geq s_z(u_i)\}
\]
has volume \(a_z/2\), and put
\[
p_z(u_i):=\frac2{a_z}\int_{A_z(u_i)}x\,dx
\in F_{\mathcal K_z}(u_i).
\tag{30}
\]
For every \(\alpha\), including \(\Psi_\alpha=0\), one has the exact identities
\[
\boxed{
\begin{aligned}
\Psi_\alpha
&=\frac12\sum_{z:\beta_z^\alpha>0}\beta_z^\alpha
\sum_i\pi_i^\alpha h_{D_z}(u_i)\\
&=\frac14\sum_{z:\beta_z^\alpha>0}\beta_z^\alpha
\sum_{i,k}\pi_i^\alpha\pi_k^\alpha
\langle u_i-u_k,p_z(u_i)-p_z(u_k)\rangle\\
&=\sum_{z:\beta_z^\alpha>0}\frac{\beta_z^\alpha}{2a_z}
\sum_{i,k}\pi_i^\alpha\pi_k^\alpha
\int_{A_z(u_i)\triangle A_z(u_k)}
\bigl(
|\langle u_i,x\rangle-s_z(u_i)|
+|\langle u_k,x\rangle-s_z(u_k)|
\bigr)\,dx.
\end{aligned}}
\tag{31}
\]
The same formulas sum exactly over any subfamily \(\mathscr B\), and (28) is the single simultaneous source-cap capacity ledger.

There is also one halfspace-dominated actual source cloud. Define
\[
\nu_{\mathrm{cap}}:=\frac12
\sum_{\alpha\in\mathscr A}
\sum_{z:\beta_z^\alpha>0}\beta_z^\alpha
\sum_i\pi_i^\alpha\delta_{(z,p_z(u_i))}.
\tag{32}
\]
Then \(\nu_{\mathrm{cap}}\) is carried by
\(C\cap(\mathbb Z^n\times\mathbb R^d)\), and
\[
\boxed{4\gamma_d\nu_{\mathrm{cap}}\preceq_{\mathrm{hs}}\mu_C,}
\qquad
\boxed{|\nu_{\mathrm{cap}}|=\Omega_b>
\frac{97}{100}Q.}
\tag{33}
\]

Finally, split the good circuits by
\[
\mathscr G_{\mathcal O}:=
\{\alpha\in\mathscr G:\mathcal O_\alpha\geq\mathcal T_\alpha\},
\qquad
\mathscr G_{\mathcal T}:=\mathscr G\setminus\mathscr G_{\mathcal O}.
\tag{34}
\]
Then the full-box stationary versus transport dichotomy is
\[
\boxed{
\max\left\{
\sum_{\alpha\in\mathscr G_{\mathcal O}}\Psi_\alpha,
\sum_{\alpha\in\mathscr G_{\mathcal T}}\mathcal T_\alpha
\right\}
>\frac16\Delta^{\mathrm{sat}}
>\frac{97}{600}\delta_*Q.}
\tag{35}
\]

A term with \(q_j^\alpha=0\), \(\pi_i^\alpha=0\), or \(\beta_z^\alpha=0\) contributes zero and consumes no density or source capacity. If \(\Psi_\alpha=0\), then \(t_\alpha=1\), the original and full circuit block coincide, and its amplified stationary energy is zero. Repeated physical targets, coincident contacts, equal directions, and vanishing generators cause no extra charge. The factor \(1/t_\alpha\) is the full coefficient interval certified by (22)-(23); no claim is made that no larger dilation could hold in a special instance. The conclusions make no absorption, affine-alignment, arbitrary-separator, residual-rank, or zero-fresh branch-closure claim.

## Proof

All data through (21), the positivity of each \(t_\alpha\), the original half-mass inclusion, the full pooled body, and the good-circuit estimates (13)-(15) are supplied by accepted fact `c7c47ab9a769716a`. Accepted fact `1491820ca8e0cf99` proves the endpoint coefficient collection and actual half-cap symmetrization for the global switch system. We prove that both arguments apply simultaneously and independently to every circuit block, with the circuit center (17).

Fix \(m\in E_{\mathrm{circ}}\). For every \(i,j\in I\) with \(m_j=m\), (2) and (8) give a density
\[
\rho_{ij}:C_m\longrightarrow[0,1]
\]
of mass \(\vartheta_j\) and barycenter \(p_{ij}\). If \(q_j^\alpha>0\), define
\[
f_{\alpha,ij}:=
\frac{q_j^\alpha}{\vartheta_j}\pi_i^\alpha\rho_{ij},
\qquad
F_{\alpha j}:=\sum_i f_{\alpha,ij}.
\tag{36}
\]
If \(q_j^\alpha=0\), set all these densities to zero. Thus
\[
\int f_{\alpha,ij}=q_j^\alpha\pi_i^\alpha,
\qquad
\int x f_{\alpha,ij}(x)\,dx
=q_j^\alpha\pi_i^\alpha p_{ij},
\tag{37}
\]
where both sides are zero when \(\pi_i^\alpha=0\), and
\[
0\leq F_{\alpha j}\leq
\frac{q_j^\alpha}{\vartheta_j}.
\tag{38}
\]
Equations (3) and (5) therefore imply the single simultaneous density budget
\[
\sum_\alpha\sum_{j:m_j=m}F_{\alpha j}
\leq\sum_{j:m_j=m}
\frac{\sum_\alpha q_j^\alpha}{\vartheta_j}
=\sum_{j:m_j=m}
\frac{q_j^{\mathrm{sat}}}{\vartheta_j}
\leq1.
\tag{39}
\]

For every positive block \((\alpha,j)\), choose all parameters
\[
\theta_{ik}^{(\alpha,j)}\in[-1/2,1/2],
\qquad
\lambda_{ik}^{(\alpha,j)}:=1/2+\theta_{ik}^{(\alpha,j)}\in[0,1]
\]
independently, and define
\[
h_{\alpha j}^{\boldsymbol\theta}:=
\sum_{i,k}\left[
(1-\lambda_{ik}^{(\alpha,j)})\frac{\pi_k^\alpha}{2}
f_{\alpha,ij}
+\lambda_{ik}^{(\alpha,j)}\frac{\pi_i^\alpha}{2}
f_{\alpha,kj}
\right].
\tag{40}
\]
Every coefficient is nonnegative. The coefficient of a fixed \(f_{\alpha,ij}\) is at most
\[
\frac12\sum_k\pi_k^\alpha+
\frac12\sum_k\pi_k^\alpha=1,
\]
so
\[
0\leq h_{\alpha j}^{\boldsymbol\theta}\leq F_{\alpha j}.
\tag{41}
\]
Using (37) and \(\sum_i\pi_i^\alpha=1\), direct summation gives
\[
\int h_{\alpha j}^{\boldsymbol\theta}
=\frac{q_j^\alpha}{2},
\tag{42}
\]
and its normalized first moment is
\[
c_{\alpha j}+
\sum_{i,k}\pi_i^\alpha\pi_k^\alpha
\theta_{ik}^{(\alpha,j)}(p_{kj}-p_{ij}).
\tag{43}
\]
Indeed, the constant \(1/2\) part cancels after summing the ordered pairs.

Sum (40) over all positive blocks at \(m\). By (39), (41), and (42), the result is a density between zero and one of total mass
\[
\frac12\sum_\alpha\sum_{j:m_j=m}q_j^\alpha
=\frac{\eta_m}{2}.
\tag{44}
\]
As the parameters vary independently, its normalized first moments are exactly
\[
c_m^{\mathrm{circ}}+
\frac1{\eta_m}\sum_\alpha\sum_{j:m_j=m}q_j^\alpha
\sum_{i,k}\pi_i^\alpha\pi_k^\alpha
[-(p_{ij}-p_{kj})/2,(p_{ij}-p_{kj})/2],
\]
which is (20). This proves the second inclusion in (22). Since \(0<t_\alpha\leq1\), each segment in (19) is contained in the corresponding segment in (20), proving the first inclusion in (22).

We next prove the first inclusion in (23). Let \(x\in\widetilde{\mathcal Z}_m^{\mathrm{circ}}\). There are numbers \(\varepsilon_{\alpha,ik}^{(j)}\in[-1,1]\) such that
\[
\eta_mx=
\sum_\alpha\sum_{j:m_j=m}q_j^\alpha c_{\alpha j}
+\sum_\alpha\sum_{j:m_j=m}\sum_{i,k}
\varepsilon_{\alpha,ik}^{(j)}
\frac{q_j^\alpha}{2}\pi_i^\alpha\pi_k^\alpha
(p_{ij}-p_{kj}).
\tag{45}
\]
For a fixed block \((\alpha,j)\) and \(\ell\in I\), collect the coefficient of \(p_{\ell j}\):
\[
\zeta_{\alpha,\ell j}:=
q_j^\alpha\pi_\ell^\alpha
+\sum_k\varepsilon_{\alpha,\ell k}^{(j)}
\frac{q_j^\alpha}{2}\pi_\ell^\alpha\pi_k^\alpha
-\sum_i\varepsilon_{\alpha,i\ell}^{(j)}
\frac{q_j^\alpha}{2}\pi_i^\alpha\pi_\ell^\alpha.
\tag{46}
\]
The sum of the absolute outgoing and incoming coefficient bounds is
\[
\frac{q_j^\alpha}{2}\pi_\ell^\alpha\sum_k\pi_k^\alpha
+\frac{q_j^\alpha}{2}\pi_\ell^\alpha\sum_i\pi_i^\alpha
=q_j^\alpha\pi_\ell^\alpha.
\]
Hence
\[
\zeta_{\alpha,\ell j}\geq0,
\qquad
\sum_\ell\zeta_{\alpha,\ell j}=q_j^\alpha.
\tag{47}
\]
Thus every positive block in (45) belongs to \(q_j^\alpha L_j\), while a zero block contributes nothing. Summing first over \(\alpha\) and using (3), then over \(j\) at \(m\), proves
\[
\eta_mx\in\sum_{j:m_j=m}q_j^{\mathrm{sat}}L_j,
\]
which is the first inclusion in (23). The second inclusion in (23) is the full pooled-body conclusion of accepted fact `c7c47ab9a769716a`. This coefficient calculation is the circuitwise simultaneous version of the full-factor calculation in accepted fact `1491820ca8e0cf99`; at the endpoint, zero coefficients in (47) remain valid convex coefficients.

For the energy, fix \(\alpha,j,i,k\). Since \(p_{ij}\in F_{L_j}(u_i)\) and \(p_{kj}\in F_{L_j}(u_k)\),
\[
\begin{aligned}
\langle u_i-u_k,p_{ij}-p_{kj}\rangle
&=\langle u_i,p_{ij}-p_{kj}\rangle
+\langle u_k,p_{kj}-p_{ij}\rangle\geq0.
\end{aligned}
\tag{48}
\]
For fixed \(\alpha,j\), (7) and (8) give
\[
\begin{aligned}
&\frac12\sum_{i,k}\pi_i^\alpha\pi_k^\alpha
\langle u_i-u_k,p_{ij}-p_{kj}\rangle\\
&\qquad=\sum_i\pi_i^\alpha h_{L_j}(u_i)
-\left\langle\sum_i\pi_i^\alpha u_i,
\sum_k\pi_k^\alpha p_{kj}\right\rangle
=\sum_i\pi_i^\alpha h_{L_j}(u_i).
\end{aligned}
\tag{49}
\]
Multiplying by \(q_j^\alpha\), summing over \(j\), and using (18) proves (25) for a singleton circuit. Finite summation proves it for every \(\mathscr B\). Moreover, (10) and (12) give
\[
\frac{\mathcal O_\alpha}{t_\alpha}
=\frac{1-t_\alpha}{t_\alpha}\Delta_\alpha
=\Psi_\alpha,
\tag{50}
\]
including \(\Psi_\alpha=0\), because then \(t_\alpha=1\). This proves (26).

We prove the source ledger. By (2) and support-function additivity under Minkowski averaging,
\[
\begin{aligned}
\Psi_\alpha
&=\frac12\sum_z\beta_z^\alpha
\sum_i\pi_i^\alpha h_{\mathcal K_z}(u_i)\\
&=\frac12\sum_z\beta_z^\alpha
\sum_i\pi_i^\alpha h_{D_z}(u_i).
\end{aligned}
\tag{51}
\]
The second equality uses \(\sum_i\pi_i^\alpha u_i=0\), so the centroid translation cancels separately at every source fiber. Equations (3)-(4) prove (28), and the two distinct endpoint occurrences of every label give (29).

Accepted fact `1491820ca8e0cf99` proves for the actual half-caps in (30) the identities
\[
h_{D_z}(u_i)=\langle u_i,p_z(u_i)-c_z\rangle
\tag{52}
\]
and
\[
\begin{aligned}
\langle u_i-u_k,p_z(u_i)-p_z(u_k)\rangle
=\frac2{a_z}\int_{A_z(u_i)\triangle A_z(u_k)}
\bigl(&|\langle u_i,x\rangle-s_z(u_i)|\\
&+|\langle u_k,x\rangle-s_z(u_k)|\bigr)\,dx.
\end{aligned}
\tag{53}
\]
The ordered-pair symmetrization and (7) give
\[
\sum_i\pi_i^\alpha h_{D_z}(u_i)
=\frac12\sum_{i,k}\pi_i^\alpha\pi_k^\alpha
\langle u_i-u_k,p_z(u_i)-p_z(u_k)\rangle.
\tag{54}
\]
Substituting (53)-(54) into (51) proves every line of (31), including all factors. Summing a finite collection of these exact identities proves the subfamily assertion. Terms with zero coefficients vanish before any normalization.

It remains to prove (33). By accepted fact `6769574fc1bd9f8d`, every cap barycenter \(p_z(u_i)\in\mathsf M_{a_z/2}(C_z)\) belongs to \(C_z\) and has halfspace depth at least \(\gamma_da_z/2\) in \(C_z\). Fix a closed ambient halfspace \(H\), and consider one source fiber \(z\). If no atom \((z,p_z(u_i))\) charged by (32) lies in \(H\), then the fiber contribution of \(\nu_{\mathrm{cap}}(H)\) is zero. Otherwise the section of \(H\) in that fiber contains at least one such cap barycenter, and therefore
\[
\operatorname{vol}_d\{x\in C_z:(z,x)\in H\}
\geq\frac{\gamma_da_z}{2}.
\tag{55}
\]
On the other hand, its entire source-cloud mass is
\[
\frac12\sum_\alpha\beta_z^\alpha
\sum_i\pi_i^\alpha=\frac{\beta_z}{2}
\leq\frac{a_z}{8}.
\tag{56}
\]
Thus the contribution of \(4\gamma_d\nu_{\mathrm{cap}}(H)\) in this fiber is at most the right side of (55). Summing over \(z\) proves the domination in (33), with coincident atoms automatically aggregated. Equations (3) and (29) give
\[
|\nu_{\mathrm{cap}}|
=\frac12\sum_{\alpha,z}\beta_z^\alpha
=\sum_\alpha\Omega_\alpha
=\Omega_b,
\]
which proves the mass assertion.

Finally, for \(\alpha\in\mathscr G_{\mathcal O}\), (12) gives \(t_\alpha\leq1/2\), hence
\[
\Psi_\alpha=\frac{1-t_\alpha}{t_\alpha}\Delta_\alpha
\geq\Delta_\alpha.
\tag{57}
\]
For \(\alpha\in\mathscr G_{\mathcal T}\), one has \(t_\alpha>1/2\), hence
\[
\mathcal T_\alpha=t_\alpha\Delta_\alpha
>\frac12\Delta_\alpha.
\tag{58}
\]
Let
\[
A:=\sum_{\alpha\in\mathscr G_{\mathcal O}}\Delta_\alpha,
\qquad
B:=\sum_{\alpha\in\mathscr G_{\mathcal T}}\Delta_\alpha.
\]
If \(S:=\sum_{\mathscr G_{\mathcal O}}\Psi_\alpha\) and \(T:=\sum_{\mathscr G_{\mathcal T}}\mathcal T_\alpha\), then (57)-(58) give \(A\leq S\) and \(B\leq2T\). By (15),
\[
3\max\{S,T\}\geq S+2T\geq A+B
>\frac12\Delta^{\mathrm{sat}}.
\]
This proves the first strict inequality in (35), and (13) proves the second. All arguments used only the common density budgets and exact circuit identities, so they do not supply any of the terminal conclusions expressly excluded in the statement.

## External sources

none
