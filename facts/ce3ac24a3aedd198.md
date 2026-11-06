---
fact_id: ce3ac24a3aedd198
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: cross-color-square-selectable-source-cloud
depends_on: ["17e91caf77284233","6769574fc1bd9f8d","be359f8a6c628483"]
verifier_run: ee44183af58242fb
target_match: null
---

## Statement

Let \(n,d\in\mathbb Z_{>0}\), let
\(C\subseteq\mathbb R^n\times\mathbb R^d\) be a convex body, and write
\[
 C_z:=\{x\in\mathbb R^d:(z,x)\in C\},
 \qquad
 a_z:=\operatorname{vol}_d(C_z)
 \quad(z\in\mathbb Z^n).
\tag{1}
\]
Let
\[
 \varnothing\ne A\subseteq\{y\in\mathbb Z^n:a_y>0\}
\]
be finite, and choose weights
\[
 0<w_y\leq\frac{a_y}{4}
 \qquad(y\in A).
\tag{2}
\]
For each parity class \(\xi\in(\mathbb Z/2\mathbb Z)^n\), set
\[
 A_\xi:=\{y\in A:y\equiv\xi\pmod2\},
 \qquad
 M_\xi:=\sum_{y\in A_\xi}w_y,
\tag{3}
\]
and define
\[
 B_{\xi,m}:=
 \begin{cases}
 \displaystyle
 \frac1{M_\xi}
 \sum_{\substack{(u,v)\in A_\xi\times A_\xi\\u+v=2m}}
 w_uw_v,&M_\xi>0,\\[2ex]
 0,&M_\xi=0,
 \end{cases}
 \qquad m\in\mathbb Z^n.
\tag{4}
\]
For \(M_\xi>0\), let
\[
 \mathcal H_{\xi,m}:=
 \bigl\{[h]:=\{h,-h\}:h\in\mathbb Z^n,
          \ m+h,m-h\in A_\xi\bigr\}.
\tag{5}
\]
Choose one representative \(h\in[h]\) for each orbit, taking \(h=0\)
for \([h]=[0]\), and put
\[
 b_{\xi,m,[h]}:=
 \begin{cases}
 \displaystyle\frac{w_m^2}{M_\xi},&[h]=[0],\\[2ex]
 \displaystyle\frac{2w_{m+h}w_{m-h}}{M_\xi},&[h]\ne[0].
 \end{cases}
\tag{6}
\]
Put
\[
 \alpha_m:=\sum_\zeta B_{\zeta,m},
 \qquad
 B_m^{\max}:=\max_\zeta B_{\zeta,m},
 \qquad
 C_{\mathrm{col}}:=\sum_m(\alpha_m-B_m^{\max}).
\tag{7}
\]
Fix a total order on the parity classes. Let \(\mathcal L_\square\) be
the finite set of positive square labels
\[
 \lambda=(m;\xi,[h];\eta,[k]),
 \qquad \xi<\eta,
\tag{8}
\]
from accepted fact `17e91caf77284233`, where
\([h]\in\mathcal H_{\xi,m}\),
\([k]\in\mathcal H_{\eta,m}\), and
\[
 \theta_\lambda
 :=\frac{2b_{\xi,m,[h]}b_{\eta,m,[k]}}{\alpha_m}>0.
\tag{9}
\]
Retain the four tagged source occurrences, including multiplicity,
\[
 \mathcal O_\lambda=[m+h,m-h,m+k,m-k],
\tag{10}
\]
and define
\[
 D_y:=\sum_{\lambda\in\mathcal L_\square}
 \theta_\lambda\operatorname{mult}_y(\mathcal O_\lambda),
 \qquad
 \Theta_\square:=\sum_{\lambda\in\mathcal L_\square}\theta_\lambda.
\tag{11}
\]
Accepted fact `17e91caf77284233` gives the simultaneous occurrence ledger
and cross-color mass bound
\[
 \boxed{D_y\leq4w_y\leq a_y\quad(y\in A),
 \qquad \Theta_\square\geq C_{\mathrm{col}}.}
\tag{12}
\]

Let
\[
 \gamma_d:=\left(\frac d{d+1}\right)^d.
\tag{13}
\]
For every simultaneous choice
\[
 \mathbf p=(p_y)_{y\in A},
 \qquad
 p_y\in\mathsf M_{4w_y}(C_y)\quad(y\in A),
\tag{14}
\]
where \(\mathsf M_m\) is the metronoid in accepted fact
`6769574fc1bd9f8d`, define, for
\(\lambda=(m;\xi,[h];\eta,[k])\),
\[
 r_\lambda^{(\mathbf p)}
 :=\frac14\bigl(p_{m+h}+p_{m-h}+p_{m+k}+p_{m-k}\bigr),
 \qquad
 P_\lambda^{(\mathbf p)}:=(m,r_\lambda^{(\mathbf p)}),
\tag{15}
\]
with every repeated occurrence in (10) repeated in the sum. Define the
selectable-source square cloud
\[
 \boxed{
 \nu_\square^{(\mathbf p)}
 :=\gamma_d\sum_{\lambda\in\mathcal L_\square}
 \theta_\lambda\delta_{P_\lambda^{(\mathbf p)}}.}
\tag{16}
\]
Then
\[
 \boxed{
 \operatorname{supp}\nu_\square^{(\mathbf p)}
 \subseteq C\cap(\mathbb Z^n\times\mathbb R^d),}
\tag{17}
\]
and, for every closed halfspace \(H\subseteq\mathbb R^{n+d}\),
\[
 \boxed{\nu_\square^{(\mathbf p)}(H)\leq\mu_C(H),}
\tag{18}
\]
where
\[
 \mu_C(E):=
 \sum_{z\in\mathbb Z^n}
 \operatorname{vol}_d\{x\in C_z:(z,x)\in E\}
\tag{19}
\]
for Borel \(E\subseteq\mathbb R^{n+d}\). Its mass is exactly
\[
 \boxed{
 |\nu_\square^{(\mathbf p)}|
 =\gamma_d\Theta_\square
 \geq\gamma_d C_{\mathrm{col}}.}
\tag{20}
\]
These conclusions hold simultaneously for every choice (14), including
labels with repeated source occurrences, arbitrary reuse of one source by
different labels, and coincident cloud atoms.

Assume \(\Theta_\square>0\). Define
\[
 P_\square^{(\mathbf p)}:=\operatorname{supp}\nu_\square^{(\mathbf p)},
 \qquad
 A_\square^{(\mathbf p)}
 :=\operatorname{aff}\operatorname{proj}_{\mathbb R^n}
 (P_\square^{(\mathbf p)}),
 \qquad
 \rho_\square^{(\mathbf p)}:=\dim A_\square^{(\mathbf p)},
\tag{21}
\]
and
\[
 r_\square(\mathbf p):=
 \min_{s:A_\square^{(\mathbf p)}\to\mathbb R^d\ \text{affine}}
 \dim\operatorname{span}
 \{x-s(z):(z,x)\in P_\square^{(\mathbf p)}\}.
\tag{22}
\]
Then there is a point
\(P_\square^\star\in C\cap(\mathbb Z^n\times\mathbb R^d)\)
such that every closed halfspace \(H\ni P_\square^\star\) satisfies
\[
 \mu_C(H)\geq\nu_\square^{(\mathbf p)}(H)
 \geq
 \frac{\gamma_d\Theta_\square}
 {2^{\rho_\square^{(\mathbf p)}}(r_\square(\mathbf p)+1)}.
\tag{23}
\]
Consequently, for
\[
 h_{\max}(C):=
 \sup_{P\in C\cap(\mathbb Z^n\times\mathbb R^d)}
 \inf_{\substack{H\text{ closed halfspace}\\P\in H}}\mu_C(H),
\tag{24}
\]
the residual-rank screen from accepted fact `be359f8a6c628483` gives,
for every simultaneous source choice (14),
\[
 \boxed{
 h_{\max}(C)
 \geq
 \frac{\gamma_d\Theta_\square}
 {2^{\rho_\square^{(\mathbf p)}}(r_\square(\mathbf p)+1)}
 \geq
 \frac{\gamma_d\Theta_\square}
 {2^n(r_\square(\mathbf p)+1)}
 \geq
 \frac{\gamma_d C_{\mathrm{col}}}
 {2^n(r_\square(\mathbf p)+1)}.}
\tag{25}
\]
If \(\Theta_\square=0\), then \(\mathcal L_\square=\varnothing\),
\(\nu_\square^{(\mathbf p)}=0\) for every choice, and (17)--(20) hold;
no support rank is defined and the only resulting depth statement is the
tautology \(h_{\max}(C)\geq0\).

Finally, if
\[
 c_y:=\frac1{a_y}\int_{C_y}x\,dx,
\tag{26}
\]
then \(c_y\in\mathsf M_{4w_y}(C_y)\) for every \(y\in A\). Thus the
centroid choice \(p_y=c_y\) is one specialization of (14), while all
other simultaneous metronoid choices retain the same coefficient and
total mass.

## Proof

Fix a simultaneous choice (14). The inequality \(0<4w_y\leq a_y\)
allows accepted fact `6769574fc1bd9f8d` to be applied to every
positive-volume fiber \(C_y\). It gives
\[
 p_y\in C_y
\tag{27}
\]
and, for every proper closed halfspace \(J\subseteq\mathbb R^d\)
containing \(p_y\), including when \(p_y\in\partial J\),
\[
 \operatorname{vol}_d(C_y\cap J)
 \geq4\gamma_dw_y.
\tag{28}
\]
For each label \(\lambda=(m;\xi,[h];\eta,[k])\), introduce the four
tagged ambient source points
\[
 q_{\lambda,1}:=(m+h,p_{m+h}),\quad
 q_{\lambda,2}:=(m-h,p_{m-h}),\quad
 q_{\lambda,3}:=(m+k,p_{m+k}),\quad
 q_{\lambda,4}:=(m-k,p_{m-k}).
\tag{29}
\]
Equation (27) puts all four points in \(C\), with equal points retained
as distinct tagged occurrences. Their average is
\[
 \frac14\sum_{i=1}^4q_{\lambda,i}
 =(m,r_\lambda^{(\mathbf p)})
 =P_\lambda^{(\mathbf p)}.
\tag{30}
\]
Convexity of \(C\) puts this average in \(C\), and its base coordinate
\(m\) is integral. This proves (17).

Fix a proper closed ambient halfspace
\[
 H=\{(z,x):\langle u,z\rangle+\langle v,x\rangle\geq t\},
 \qquad (u,v)\ne(0,0).
\tag{31}
\]
If \(P_\lambda^{(\mathbf p)}\in H\), then averaging the affine
functional in (31) over (30) shows that at least one tagged point
\(q_{\lambda,i}\) lies in \(H\). This remains true when the cloud atom
lies on \(\partial H\). Orient the label to the first such tagged
occurrence in the order (29). For \(y\in A\), let
\[
 L_{H,y}:=
 \sum_{\substack{\lambda:P_\lambda^{(\mathbf p)}\in H\\
 \text{the selected tag of }\lambda\text{ has source }y}}
 \theta_\lambda.
\tag{32}
\]
Every term is charged to one tagged occurrence counted in (11), so
\[
 0\leq L_{H,y}\leq D_y\leq4w_y.
\tag{33}
\]
This comparison does not identify repeated occurrences: the ledger
counts every tag with its multiplicity, while the orientation charges
at most one tag of a label. Labels sharing a source are all charged to
the same \(D_y\), and labels producing one coincident cloud atom remain
separate summands in (32).

If a tag with source \(y\) is selected, the fiber section
\[
 H_y:=\{x\in\mathbb R^d:(y,x)\in H\}
\tag{34}
\]
contains \(p_y\). If \(v\ne0\), this is a proper closed halfspace, and
(28) applies. If \(v=0\), selection implies \(H_y=\mathbb R^d\), and
then (2) and \(0<\gamma_d\leq1\) give
\[
 \operatorname{vol}_d(C_y\cap H_y)=a_y
 \geq4w_y\geq4\gamma_dw_y.
\tag{35}
\]
Thus, in both cases, (33) gives
\[
 \gamma_dL_{H,y}
 \leq4\gamma_dw_y
 \leq\operatorname{vol}_d(C_y\cap H_y).
\tag{36}
\]
Summing only over sources selected by some label yields
\[
 \begin{aligned}
 \nu_\square^{(\mathbf p)}(H)
 &=\gamma_d
 \sum_{\lambda:P_\lambda^{(\mathbf p)}\in H}\theta_\lambda
 =\gamma_d\sum_{y\in A}L_{H,y}\\
 &\leq\sum_{y\in A}\operatorname{vol}_d(C_y\cap H_y)
 \leq\mu_C(H).
 \end{aligned}
\tag{37}
\]
For the whole-space halfspace, orient every label to its first tag and
repeat (33), (35), and (37). The empty improper halfspace has zero mass
for both measures. Therefore (18) holds for every closed-halfspace
convention, including boundary and whole-fiber cases.

Every coefficient in (16) is nonnegative, so
\[
 |\nu_\square^{(\mathbf p)}|
 =\gamma_d\sum_{\lambda\in\mathcal L_\square}\theta_\lambda
 =\gamma_d\Theta_\square.
\tag{38}
\]
Coincident atoms merely add their coefficients and do not change (38).
The last inequality in (20) is (12). This proves the support,
domination, and mass conclusions for every choice, including the empty
label set.

Suppose \(\Theta_\square>0\). Equation (38) makes
\(\nu_\square^{(\mathbf p)}\) a nonzero positive finite Borel measure
carried by the mixed lattice section, and (18) is exactly the
halfspace-domination hypothesis of the dominated-measure residual
theorem in accepted fact `be359f8a6c628483`. Applying that theorem with
\(\sigma=\nu_\square^{(\mathbf p)}\) proves (23) and the first
inequality in (25). Since \(\rho_\square^{(\mathbf p)}\leq n\), the
second inequality follows; (12) gives the third. If
\(\Theta_\square=0\), all \(\theta_\lambda\) are positive by the
definition of \(\mathcal L_\square\), so that set is empty and the
stated zero-mass conclusions follow.

For the final specialization, the constant density
\[
 f_y:=\frac{4w_y}{a_y}\mathbf1_{C_y}
\tag{39}
\]
lies between zero and one, has mass \(4w_y\), and has normalized
barycenter \(c_y\). Hence \(c_y\in\mathsf M_{4w_y}(C_y)\), proving the
last assertion and completing the proof.

## External sources

none
