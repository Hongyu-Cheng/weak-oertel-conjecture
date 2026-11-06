---
fact_id: e6cf877c81ebffb9
kind: lemma
author: "research-agent"
assurance: LLM-verified
subgoal_id: synchronized-greedy-basis-simplex-localization
depends_on: ["27024aed67e77532","6769574fc1bd9f8d","6bfe50fed9a5540b","8aac56c49321466c","be359f8a6c628483","dfd25e72c1f45a4e"]
verifier_run: 7a78434b3eaf4581
target_match: null
---

## Statement

Retain one common canonical instance of accepted facts `27024aed67e77532`, `6bfe50fed9a5540b`, `6769574fc1bd9f8d`, `be359f8a6c628483`, `8aac56c49321466c`, and `dfd25e72c1f45a4e`.  Thus \(n,d\in\mathbb Z_{>0}\), \(C\subseteq\mathbb R^n\times\mathbb R^d\) is the common convex body, and
\[
 C_y:=\{x\in\mathbb R^d:(y,x)\in C\},
 \qquad
 a_y:=\operatorname{vol}_d(C_y),
 \qquad
 \gamma_d:=\left(\frac d{d+1}\right)^d.
\tag{1}
\]
Let \(\mu_C\) be its mixed-volume measure, let
\[
 G:=\mathfrak C_{\mathrm{core}}(C),
 \qquad
 D:=2^nh_{\max}(C),
\tag{2}
\]
and let \(r=(r_e)\) be the full half-strength canonical product reservoir, recomputed from all actual positive integer fibers, with
\[
 Q:=\sum_er_e>0.
\tag{3}
\]
For every positive canonical edge \(e=\{u,v\}\), use
\[
 m_e:=\frac{u+v}{2},
 \qquad
 \mathcal K_y:=\mathsf M_{a_y/2}(C_y),
 \qquad
 L_e:=\frac12(\mathcal K_u+\mathcal K_v),
\tag{4}
\]
\[
 \vartheta_e
 :=2^{-(d+1)}
 \left(a_u^{1/d}+a_v^{1/d}\right)^d.
\tag{5}
\]

Retain the intact label family of Alternative 1 in accepted fact `27024aed67e77532`.  Every label \(\sigma\) has two distinct physical opposite endpoints \(a(\sigma),b(\sigma)\), original retained weight \(\widehat\theta_\sigma>0\), endpoint atlas loads
\[
 w_y=
 \sum_{\sigma:\,y\in\{a(\sigma),b(\sigma)\}}
 \widehat\theta_\sigma,
\tag{6}
\]
and completion ratios
\[
 q_y:=\min\left\{1,\frac{\beta_y^b}{w_y}\right\}.
\tag{7}
\]
Define the whole-label thinning and its total mass by
\[
 \eta_\sigma:=\widehat\theta_\sigma
 \min\{q_{a(\sigma)},q_{b(\sigma)}\},
 \qquad
 P_\cap:=\sum_\sigma\eta_\sigma.
\tag{8}
\]
Assume intact Alternative 1, so
\[
 P_\cap\geq\frac Q{800}>0.
\tag{9}
\]

Retain from accepted fact `6bfe50fed9a5540b` the genuinely recomputed completed submatching \(b\), its fresh gauge-load-minimal KKT load \(\omega^b\), and its physical endpoint loads and points:
\[
 0\leq\omega_e^b\leq b_e\leq r_e,
 \qquad
 \beta_y^b:=\sum_{e\ni y}\omega_e^b,
\tag{10}
\]
\[
 p_y^b\in
 \mathcal K_y\cap\mathsf M_{\beta_y^b}(C_y)
 \qquad(\beta_y^b>0).
\tag{11}
\]
The fresh target congestion inequality is
\[
 \sum_{e:m_e=m}\frac{\omega_e^b}{\vartheta_e}\leq1
 \qquad(m\in\mathbb Z^n).
\tag{12}
\]

Put
\[
 d_y^\eta
 :=\sum_{\sigma:\,y\in\{a(\sigma),b(\sigma)\}}
 \eta_\sigma.
\tag{13}
\]
Then there is a subload \(\tau=(\tau_e)\) satisfying
\[
 \boxed{0\leq\tau_e\leq\omega_e^b\leq b_e\leq r_e,}
 \qquad
 \boxed{|\tau|:=\sum_e\tau_e\geq P_\cap.}
\tag{14}
\]

For every edge with \(\tau_e>0\), put
\[
 \ell_e^b:=\frac{p_u^b+p_v^b}{2}
 \qquad(e=\{u,v\}).
\tag{15}
\]
For every physical target \(m\), put
\[
 t_m:=\sum_{e:m_e=m}\tau_e.
\tag{16}
\]
When \(t_m>0\), there is one point
\[
 q_m:=\frac1{t_m}
 \sum_{e:m_e=m}\tau_e\ell_e^b
\tag{17}
\]
with one jointly pooled representing density such that
\[
 \boxed{q_m\in\mathsf M_{t_m}(C_m).}
\tag{18}
\]
In particular, all physical target collisions in (16) are aggregated before a metronoid membership is asserted, and
\[
 \boxed{\sum_mt_m=|\tau|\geq P_\cap.}
\tag{19}
\]

The atomic measure
\[
 \nu_\tau
 :=\gamma_d\sum_{m:t_m>0}
 t_m\delta_{(m,q_m)}
\tag{20}
\]
is carried by \(C\cap(\mathbb Z^n\times\mathbb R^d)\), and every closed ambient halfspace \(H\) satisfies
\[
 \boxed{\nu_\tau(H)\leq\mu_C(H).}
\tag{21}
\]
Its exact mass is
\[
 \boxed{|\nu_\tau|=\gamma_d|\tau|
 \geq\gamma_dP_\cap.}
\tag{22}
\]

Let
\[
 A_\tau:=\operatorname{aff}\{m:t_m>0\},
 \qquad
 \rho_\tau:=\dim A_\tau,
\tag{23}
\]
and define its intrinsic continuous residual rank by
\[
 r_\tau
 :=\min_{s:A_\tau\to\mathbb R^d\ \mathrm{affine}}
 \dim\operatorname{span}
 \{q_m-s(m):t_m>0\}.
\tag{24}
\]
Then
\[
 \boxed{
 D\geq\gamma_d|\tau|
 \frac{2^{n-\rho_\tau}}{r_\tau+1}
 \geq\gamma_dP_\cap
 \frac{2^{n-\rho_\tau}}{r_\tau+1}.}
\tag{25}
\]

Finally, for every affine subspace \(A\subseteq\mathbb R^n\) with \(\dim A\leq2\), put
\[
 T_A:=\sum_{m\in A}t_m.
\tag{26}
\]
Then
\[
 \boxed{G\geq\frac{T_A}{64}.}
\tag{27}
\]
Consequently,
\[
 \boxed{
 \rho_\tau\leq2
 \quad\Longrightarrow\quad
 G\geq\frac{|\tau|}{64}
 \geq\frac{P_\cap}{64}.}
\tag{28}
\]
No rank-free terminal is asserted when \(\rho_\tau\geq3\).

## Proof

First aggregate every physical source collision.  From (6)--(8),
\[
 \begin{aligned}
 d_y^\eta
 &\leq
 \min\left\{q_y\sum_{\sigma:\,y\in\{a(\sigma),b(\sigma)\}}
 \widehat\theta_\sigma,
 \sum_{\sigma:\,y\in\{a(\sigma),b(\sigma)\}}
 \widehat\theta_\sigma\right\}\\
 &=q_yw_y
 =\min\{w_y,\beta_y^b\}
 \leq\beta_y^b.
 \end{aligned}
\tag{29}
\]
Here the first displayed minimum merely records that
\(\min\{q_{a(\sigma)},q_{b(\sigma)}\}\leq q_y\leq1\) for every label occurrence at \(y\).  Also, because the two physical endpoints of every label are distinct,
\[
 \sum_yd_y^\eta=2\sum_\sigma\eta_\sigma=2P_\cap.
\tag{30}
\]
These are exactly the collision-aggregated overlap consequences of accepted fact `27024aed67e77532`.

We construct \(\tau\) by a finite edge-end allocation.  For every label occurrence \((\sigma,y)\), choose nonnegative numbers
\[
 \lambda_{\sigma,y,e}
 \qquad(e\ni y)
\tag{31}
\]
such that
\[
 \sum_{e\ni y}\lambda_{\sigma,y,e}=\eta_\sigma
\tag{32}
\]
and, for every edge-end incidence \((y,e)\),
\[
 \sum_{\sigma:\,y\in\{a(\sigma),b(\sigma)\}}
 \lambda_{\sigma,y,e}\leq\omega_e^b.
\tag{33}
\]
This is possible independently at every physical endpoint: by (29), the total demand \(d_y^\eta\) is at most the total incident bin capacity
\(\sum_{e\ni y}\omega_e^b=\beta_y^b\).  Greedily fill the finitely many bins until all finitely many demands are exhausted.

For \(e=\{u,v\}\), define
\[
 L_{u,e}:=
 \sum_{\sigma:\,u\in\{a(\sigma),b(\sigma)\}}
 \lambda_{\sigma,u,e},
 \qquad
 L_{v,e}:=
 \sum_{\sigma:\,v\in\{a(\sigma),b(\sigma)\}}
 \lambda_{\sigma,v,e},
\tag{34}
\]
and set
\[
 \tau_e:=\max\{L_{u,e},L_{v,e}\}.
\tag{35}
\]
Equation (33) proves the coordinatewise bounds in (14).  Moreover,
\[
 \begin{aligned}
 2|\tau|
 &=2\sum_e\tau_e\\
 &\geq\sum_{e=\{u,v\}}(L_{u,e}+L_{v,e})\\
 &=\sum_y\sum_{e\ni y}L_{y,e}
 =\sum_yd_y^\eta
 =2P_\cap,
 \end{aligned}
\tag{36}
\]
where (32) and (30) give the last two equalities.  This proves all of (14).  The maximum in (35), rather than a sum of the two edge-end allocations, is the no-reuse step.

If \(\tau_e>0\), then \(\omega_e^b>0\), so both endpoints of \(e\) have positive \(\beta^b\) and the two points in (15) exist.  By (11),
\[
 p_u^b\in\mathsf M_{a_u/2}(C_u),
 \qquad
 p_v^b\in\mathsf M_{a_v/2}(C_v).
\tag{37}
\]
The positive-root interpolation of accepted fact `dfd25e72c1f45a4e`, in exactly the canonical normalization retained in accepted fact `6bfe50fed9a5540b`, gives
\[
 \ell_e^b\in L_e
 \subseteq\mathsf M_{\vartheta_e}(C_{m_e}).
\tag{38}
\]
Choose a representing density \(f_e\) for this membership, so
\[
 0\leq f_e\leq1,
 \qquad
 \int_{C_{m_e}}f_e=\vartheta_e,
 \qquad
 \int_{C_{m_e}}x f_e(x)\,dx
 =\vartheta_e\ell_e^b.
\tag{39}
\]

Fix one physical target \(m\), and define the single pooled density
\[
 g_m:=\sum_{e:m_e=m}
 \frac{\tau_e}{\vartheta_e}f_e.
\tag{40}
\]
Equations (12) and (14) give the pointwise inequality
\[
 0\leq g_m
 \leq\sum_{e:m_e=m}\frac{\tau_e}{\vartheta_e}
 \leq\sum_{e:m_e=m}\frac{\omega_e^b}{\vartheta_e}
 \leq1.
\tag{41}
\]
Equations (16), (17), (39), and (40) give
\[
 \int_{C_m}g_m=t_m,
 \qquad
 \int_{C_m}xg_m(x)\,dx=t_mq_m.
\tag{42}
\]
Thus (40) is one joint representing density for all edges colliding at \(m\), which proves (18).  Summing (16) over the distinct physical targets proves (19).

We prove the halfspace domination.  Fix a closed ambient halfspace \(H\).  If an atom \((m,q_m)\) of (20) belongs to \(H\), its fiber section
\[
 H_m:=\{x\in\mathbb R^d:(m,x)\in H\}
\tag{43}
\]
is a closed halfspace containing \(q_m\), or it is the whole space.  Accepted fact `6769574fc1bd9f8d`, applied to (18), gives
\[
 \operatorname{vol}_d(C_m\cap H_m)
 \geq\gamma_dt_m.
\tag{44}
\]
The same inequality is immediate in the whole-space case.  Sum (44) over the distinct physical target bases whose atoms lie in \(H\), and discard all other nonnegative fiber contributions.  This proves (21).  Equations (19)--(20) give (22).

Apply the dominated-measure residual theorem of accepted fact `be359f8a6c628483` to \(\nu_\tau\).  Its intrinsic ranks are exactly (23)--(24), so
\[
 h_{\max}(C)
 \geq\frac{|\nu_\tau|}
 {2^{\rho_\tau}(r_\tau+1)}.
\tag{45}
\]
Multiply (45) by \(2^n\), then use (22).  This proves (25).

It remains to prove the rank-at-most-two slice statement.  Fix an affine subspace \(A\subseteq\mathbb R^n\) with \(\dim A\leq2\).  If \(T_A=0\), (27) follows from \(G\geq0\).  Assume \(T_A>0\), put
\[
 I_+:=\{z\in\mathbb Z^n:a_z>0\},
 \qquad
 W:=\sum_{z\in I_+}a_z,
 \qquad
 W_A:=\sum_{z\in I_+\cap A}a_z,
\tag{46}
\]
and let
\[
 B:=\operatorname{aff}(I_+\cap A),
 \qquad
 q:=\dim B\leq2.
\tag{47}
\]
Membership (18) implies \(a_m\geq t_m\) whenever \(t_m>0\).  Therefore
\[
 W_A\geq\sum_{m\in A}t_m=T_A,
 \qquad
 W\geq W_A\geq T_A.
\tag{48}
\]
The support-free rank-at-most-two complete-core theorem of accepted fact `8aac56c49321466c` gives
\[
 G\geq\frac1{64}
 \min\{W,2^{n-q}W_A\}.
\tag{49}
\]
Because \(q\leq n\), equations (48)--(49) imply
\[
 G\geq\frac{T_A}{64},
\]
which is (27).  If \(\rho_\tau\leq2\), take \(A=A_\tau\).  Equations (19), (23), and (27) then give (28).  This proves every asserted conclusion.

## External sources

none
