---
fact_id: 64dce6befc6ee430
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: triangle-square-star-absorption
depends_on: ["07889c9b4686d8b4","6b09aae189415c70","7ec63df101c30343","be359f8a6c628483","e2263a787ace07a4"]
verifier_run: 1ed5abce3dc042e5
target_match: null
---

## Statement

Let \(n,d\in\mathbb Z_{>0}\), let \(C\subseteq\mathbb R^n\times\mathbb R^d\) be a convex body, and use the exact canonical hypotheses, objects, and normalizations of accepted facts `6b09aae189415c70` and `7ec63df101c30343`. In particular, let \(Q>0\) be the half-strength canonical product-reservoir mass, let \(R\), \(G\), \(R_{\mathrm{sel}}(C)\), \(M_{\mathrm{off}}(C)\), \(R_{\mathrm{cloud}}(C)\), and
\[
 D:=2^nh_{\max}(C)
\]
be the canonical nonnegative capacities, and put
\[
 \mathcal A(C):=R+G+R_{\mathrm{sel}}(C)+M_{\mathrm{off}}(C)
 +R_{\mathrm{cloud}}(C)+D.
\]
Assume
\[
 \mathcal A(C)<\frac Q{100},
 \qquad I\ge O,
\tag{1}
\]
where \(I,O\) are the canonical within-label and labelled-output defects.

Under (1), accepted fact `6b09aae189415c70` gives \(I>Q/4\), so the actual \(I\)-triangle objects of accepted fact `7ec63df101c30343` are defined. Let \(s_e\) be the canonical retained matching weights, let \(\mathcal E_I\) be the family of \(I\)-bad opposite edges, let \(t_e\) be their actual opposite-edge triangle masses, and let \(\mathcal B\) be the exceptional edge family satisfying
\[
 \sum_{e\in\mathcal B}s_e\le G,
 \qquad t_e\ge\frac18s_e\quad(e\notin\mathcal B).
\tag{2}
\]
For a physical target \(c\), put
\[
 T_c:=\sum_\xi
 \sum_{\substack{e\subseteq\xi,\ m_e=c\\e\in\mathcal E_I}}t_e,
 \qquad E:=\{c\in\mathbb Z^n:T_c>0\},
 \qquad \Theta_I:=\sum_{c\in E}T_c.
\tag{3}
\]
Assume
\[
 \dim\operatorname{aff}(E)=2.
\tag{4}
\]
At every \(c\in E\), choose a retained parity label \(\xi(c)\) maximizing the corresponding labelled mass, put
\[
 q_c:=q_{\xi(c),c}^{\circ},
\]
and define, exactly as in accepted fact `e2263a787ace07a4`,
\[
 r_E:=
 \min_{a:\operatorname{aff}(E)\to\mathbb R^d\ {\rm affine}}
 \dim\operatorname{span}\{q_c-a(c):c\in E\}.
\tag{5}
\]

Put
\[
 J:=\{e\in\mathcal E_I\setminus\mathcal B:s_e>0\},
 \qquad S:=\sum_{e\in J}s_e.
\tag{6}
\]
Then \(S>0\). For every reservoir edge \(e=\{u,v\}\), retain the canonical notation
\[
 m_e:=\frac{u+v}{2},
 \qquad \bar c_e:=\frac{c_u+c_v}{2},
 \qquad F_e^\flat:=\frac{p_u^\flat+p_v^\flat}{2}.
\tag{7}
\]
Define the actual restricted measures
\[
 \sigma_M:=\sum_{e\in J}\frac{s_e}{16}\,
 \delta_{(m_e,\bar c_e)},
 \qquad
 \sigma_F:=\gamma_d\sum_{e\in J}s_e\,
 \delta_{(m_e,F_e^\flat)},
 \qquad
 \gamma_d:=\left(\frac d{d+1}\right)^d,
\tag{8}
\]
and define their intrinsic continuous residual ranks by
\[
 r_M:=
 \min_{a:\operatorname{aff}\{m_e:e\in J\}\to\mathbb R^d\ {\rm affine}}
 \dim\operatorname{span}\{\bar c_e-a(m_e):e\in J\},
\tag{9}
\]
\[
 r_F:=
 \min_{a:\operatorname{aff}\{m_e:e\in J\}\to\mathbb R^d\ {\rm affine}}
 \dim\operatorname{span}\{F_e^\flat-a(m_e):e\in J\}.
\tag{10}
\]
Then, with
\[
 K_I:=
 \frac{\gamma_d}{8(r_E+1)}
 +\frac{2^{n-6}}{r_M+1}
 +\max\left\{
 \frac{\gamma_d}{8(r_E+1)},
 \frac{\gamma_d2^{n-2}}{r_F+1}
 \right\},
\tag{11}
\]
every configuration satisfying (1)--(10) obeys the strict joint escape
\[
 \boxed{K_I<\frac{971}{45056}.}
\tag{12}
\]
Consequently,
\[
 \boxed{r_E\ge4,}
 \qquad
 \boxed{r_M+1>\frac{704\,2^n}{971},}
 \qquad
 \boxed{r_F+1>\frac{4096\,2^n}{971}.}
\tag{13}
\]
No exclusion of the target-rank-two \(I\)-dominant branch is asserted when all three strict conditions in (12)--(13) hold.

## Proof

All cited objects in (1)--(10) have the same meanings and normalizations as in the declared predecessors. Accepted fact `6b09aae189415c70` gives the hard alternative
\[
 \max\{I,O\}>\frac Q4.
\]
Since \(I\ge O\), this gives \(I>Q/4\). It also gives the exact defect estimate
\[
 I+O\ge
 \frac{11}{16}Q-\frac{67}{4}R-\frac{51}{128}G.
\tag{14}
\]
Because \(I\ge O\), equation (14) implies
\[
 I\ge
 \frac{11}{32}Q-\frac{67}{8}R-\frac{51}{256}G.
\tag{15}
\]
By the definition of \(I\), one has \(I=\sum_{e\in\mathcal E_I}s_e\). Hence (2) and (6) give
\[
 S\ge I-G
 \ge
 \frac{11}{32}Q-\frac{67}{8}R-\frac{307}{256}G.
\tag{16}
\]
In particular, the nonnegativity of all summands of \(\mathcal A(C)\), together with (1), gives \(R,G<Q/100\), so already \(S\ge I-G>0\).

For every \(e\in J\), equation (2) gives \(t_e\ge s_e/8\). Therefore
\[
 \Theta_I=\sum_{e\in\mathcal E_I}t_e
 \ge\sum_{e\in J}t_e
 \ge\frac S8.
\tag{17}
\]
The set \(E\) in (3) is the complete positive physical target support. By (4), its affine hull is a target plane, and the occupied-fiber rank inside that plane is exactly two because \(E\) itself spans it. The rank-two target-slice estimate of accepted fact `07889c9b4686d8b4` thus gives
\[
 \Theta_I\le16G.
\tag{18}
\]
Combining (17) and (18),
\[
 G\ge\frac S{128}.
\tag{19}
\]

We next charge three distinct canonical capacity summands. The heaviest-label selector theorem `e2263a787ace07a4`, applied to the complete support \(E\) of affine rank two, gives
\[
 R_{\mathrm{sel}}(C)
 \ge\frac{\gamma_d}{r_E+1}\Theta_I
 \ge\frac{\gamma_d}{8(r_E+1)}S.
\tag{20}
\]
The same accepted fact gives
\[
 D\ge R_{\mathrm{sel}}(C).
\tag{21}
\]

Every \(e\in J\) has \(t_e>0\), so \(m_e\in E\). Thus the common base affine rank of the measures in (8) is at most two. Accepted fact `6b09aae189415c70` gives \(s_e/16\le r_e\) for every retained edge and makes every positive submeasure of
\[
 \bar\nu_r:=\sum_er_e\delta_{(m_e,\bar c_e)}
\]
admissible in its reservoir-centroid visibility estimate. Hence \(\sigma_M\le\bar\nu_r\), \(|\sigma_M|=S/16\), and
\[
 M_{\mathrm{off}}(C)
 \ge 2^{n-2}\frac{S/16}{r_M+1}
 =\frac{2^{n-6}}{r_M+1}S.
\tag{22}
\]

Accepted fact `6b09aae189415c70` also proves that the full positive measure
\[
 \gamma_d\sum_es_e\delta_{(m_e,F_e^\flat)}
\]
is halfspace-dominated by the mixed-volume measure of \(C\). Its positive restriction \(\sigma_F\) is therefore halfspace-dominated as well. It has mass \(\gamma_dS\), base affine rank at most two, and continuous residual rank \(r_F\). The dominated-measure residual theorem `be359f8a6c628483` gives
\[
 h_{\max}(C)
 \ge\frac{\gamma_dS}{4(r_F+1)},
 \qquad
 D\ge\frac{\gamma_d2^{n-2}}{r_F+1}S.
\tag{23}
\]

Equations (20)--(23) use exact max-versus-sum accounting. The summands \(R_{\mathrm{sel}}(C)\), \(M_{\mathrm{off}}(C)\), and \(D\) are distinct terms of \(\mathcal A(C)\). The selector lower bound is charged once to \(R_{\mathrm{sel}}(C)\); the restricted centroid lower bound is charged once to \(M_{\mathrm{off}}(C)\); and for \(D\) one takes the maximum of its selector and restricted edge-point lower bounds. No second \(M_{\mathrm{off}}(C)\) estimate, no cloud term, and no star term is added. Therefore (11) and (20)--(23) imply
\[
 \mathcal A(C)
 \ge R+G+R_{\mathrm{sel}}(C)+M_{\mathrm{off}}(C)+D
 \ge R+G+K_IS.
\tag{24}
\]

It remains to certify the exact threshold in (12). Normalize
\[
 r:=\frac RQ,
 \qquad g:=\frac GQ,
 \qquad s:=\frac SQ.
\tag{25}
\]
Equations (16) and (19) become
\[
 s+\frac{67}{8}r+\frac{307}{256}g\ge\frac{11}{32},
 \qquad g-\frac{s}{128}\ge0.
\tag{26}
\]
Put
\[
 K_0:=\frac{971}{45056},
 \qquad \lambda:=\frac8{275},
 \qquad \mu:=\frac{8493}{8800}.
\tag{27}
\]
The following is an exact identity:
\[
 \begin{aligned}
 r+g+K_0s
 ={}&\lambda\left(
 s+\frac{67}{8}r+\frac{307}{256}g
 \right)
 +\mu\left(g-\frac{s}{128}\right)
 +\frac{208}{275}r.
 \end{aligned}
\tag{28}
\]
Indeed,
\[
 \lambda\frac{307}{256}+\mu=1,
 \qquad
 \lambda-\frac\mu{128}=\frac{971}{45056},
 \qquad
 \lambda\frac{67}{8}+\frac{208}{275}=1.
\tag{29}
\]
All multipliers in (28) are nonnegative. Since \(r\ge0\), equations (26)--(28) give
\[
 r+g+K_0s
 \ge\frac8{275}\frac{11}{32}
 =\frac1{100}.
\tag{30}
\]
If \(K_I\ge K_0\), then (24), (25), and \(s>0\) yield
\[
 \frac{\mathcal A(C)}Q
 \ge r+g+K_Is
 \ge r+g+K_0s
 \ge\frac1{100},
\]
contrary to (1). This proves the strict inequality (12).

For completeness, we derive all three rank consequences without using any later rank-screen theorem. The binomial theorem gives
\[
 \left(1+\frac1d\right)^d
 <\sum_{j=0}^{\infty}\frac1{j!}.
\]
Moreover, since the successive ratios in the factorial tail starting at \(1/4!\) are at most \(1/5\),
\[
 \sum_{j=0}^{\infty}\frac1{j!}
 \le\frac83+\frac{1/24}{1-1/5}
 =\frac{87}{32}<\frac{11}{4}.
\]
Consequently
\[
 \gamma_d>\frac4{11}.
\tag{31}
\]
The maximum in (11) is at least its first entry, so
\[
 K_I\ge\frac{\gamma_d}{4(r_E+1)}.
\tag{32}
\]
If \(r_E\le3\), equations (31)--(32) give
\[
 K_I>\frac1{44}
 =\frac{1024}{45056}
 >\frac{971}{45056},
\]
contradicting (12). Hence \(r_E\ge4\).

Each nonnegative term in (11) is strictly smaller than \(K_0\). In particular,
\[
 \frac{2^{n-6}}{r_M+1}<\frac{971}{45056},
\]
which rearranges to
\[
 r_M+1>\frac{45056\,2^{n-6}}{971}
 =\frac{704\,2^n}{971}.
\tag{33}
\]
Likewise,
\[
 \frac{\gamma_d2^{n-2}}{r_F+1}<\frac{971}{45056}.
\]
Using (31) and rearranging gives
\[
 r_F+1>
 \frac{4}{11}\frac{45056\,2^{n-2}}{971}
 =\frac{4096\,2^n}{971}.
\tag{34}
\]
Equations (32)--(34) prove (13), and the proof makes no claim that configurations above these rank thresholds are impossible.

## External sources

none
