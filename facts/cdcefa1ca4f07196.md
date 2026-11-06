---
fact_id: cdcefa1ca4f07196
kind: lemma
author: "research-agent"
assurance: LLM-verified
subgoal_id: triangle-square-star-absorption
depends_on: ["0c5bcff6d676252e","6496cb3b0fd44f9d"]
verifier_run: e2427b874cc9447c
target_match: null
---

## Statement

Retain all objects, assumptions, and notation of accepted fact
0c5bcff6d676252e. In particular, \(r=(r_e)\) is the half-strength
canonical reservoir, \(v=(v_e)\) is its load-minimal dual optimizer,

\[
 \omega_e=h_{D_e}(v_e),
 \qquad
 \chi_e=
 \begin{cases}
  \min\{\omega_e,s_e/16\},&e\in J,\\
  0,&e\notin J,
 \end{cases}
 \qquad
 X=\sum_e\chi_e>\frac Q{200}.
\tag{1}
\]

For every \(\omega_e>0\), put \(u_e=v_e/\omega_e\). Choose the
particular circuit decomposition constructed in the proof of accepted
fact 6496cb3b0fd44f9d. Thus there are \(N<\infty\), coefficients
\(\omega_e^{(j)}\ge0\), and stresses

\[
 v_e^{(j)}=\omega_e^{(j)}u_e
 \qquad(1\le j\le N),
\tag{2}
\]

with the convention \(\omega_e^{(j)}=v_e^{(j)}=0\) when \(\omega_e=0\),
such that

\[
 \sum_{j=1}^N\omega_e^{(j)}=\omega_e,
 \qquad
 \sum_{j=1}^Nv_e^{(j)}=v_e
 \qquad(e),
\tag{3}
\]

\[
 \sum_ev_e^{(j)}=0,
 \qquad
 \sum_ev_e^{(j)}m_e^{\mathsf T}=0,
 \qquad
 \bigl|\operatorname{supp}\omega^{(j)}\bigr|
 \le d(n+1)+1,
\tag{4}
\]

and

\[
 \sum_eh_{L_e}(v_e^{(j)})<0
 \qquad(1\le j\le N).
\tag{5}
\]

Set \(c_e=s_e/16\) on \(J\) and \(c_e=0\) off \(J\). The elementary
coordinatewise clipping inequality does hold:

\[
 \boxed{
 \chi_e
 =\min\left\{\sum_{j=1}^N\omega_e^{(j)},c_e\right\}
 \le\sum_{j=1}^N\min\{\omega_e^{(j)},c_e\}
 \le\omega_e.}
\tag{5a}
\]

The middle coefficients in (5a) need not satisfy the cancellations in
(4). The following proportional marking and circuit envelope preserve
both the full clipped overlap and the cancellations.

Define

\[
 \theta_e:=
 \begin{cases}
  \chi_e/\omega_e,&\omega_e>0,\\
  0,&\omega_e=0,
 \end{cases}
 \qquad
 t_j:=\max\{\theta_e:\omega_e^{(j)}>0\},
\tag{6}
\]

and put

\[
 \eta_e^{(j)}:=t_j\omega_e^{(j)},
 \qquad
 \widehat v_e^{(j)}:=t_jv_e^{(j)},
 \qquad
 \kappa_e^{(j)}:=\theta_e\omega_e^{(j)}.
\tag{7}
\]

Finally, put

\[
 \eta_e:=\sum_{j=1}^N\eta_e^{(j)},
 \qquad
 \widehat v_e:=\sum_{j=1}^N\widehat v_e^{(j)}.
\tag{8}
\]

Then the following coordinatewise lossless marking identities hold:

\[
 \boxed{
  0\le\kappa_e^{(j)}\le\eta_e^{(j)}\le\omega_e^{(j)},
  \qquad
  \sum_{j=1}^N\kappa_e^{(j)}=\chi_e.}
\tag{9}
\]

\[
 \boxed{\chi_e\le\eta_e\le\omega_e\le r_e\qquad(e).}
\tag{10}
\]

In particular,

\[
 \boxed{
  \sum_{j=1}^N\sum_e\kappa_e^{(j)}=X>\frac Q{200},
  \qquad
  \sum_{j=1}^N|\eta^{(j)}|=|\eta|\ge X>\frac Q{200}.}
\tag{11}
\]

Every nonzero packet \(\eta^{(j)}\) is a legal off-diagonal
same-parity fractional matching, supported on at most \(d(n+1)+1\)
edges, and \(\widehat v^{(j)}\) is a saturated balanced stress for that
packet:

\[
 \sum_e\widehat v_e^{(j)}=0,
 \qquad
 \sum_e\widehat v_e^{(j)}m_e^{\mathsf T}=0,
 \qquad
 h_{D_e}(\widehat v_e^{(j)})=\eta_e^{(j)}.
\tag{12}
\]

It is affinely frustrated:

\[
 \boxed{
  \Delta_C(\eta^{(j)})
  \ge-\sum_eh_{L_e}(\widehat v_e^{(j)})>0
  \qquad(t_j>0).}
\tag{13}
\]

Moreover, \(t_j>0\) if and only if the packet contains positive marked
mass, \(\sum_e\kappa_e^{(j)}>0\). Hence every nonzero packet is
anchored by at least one of the actual \(J\)-contacts from (1).

The aggregate \(\eta\) is also a legal matching and \(\widehat v\) is a
balanced saturated stress with

\[
 h_{D_e}(\widehat v_e)=\eta_e,
 \qquad
 \Delta_C(\eta)
 \ge-\sum_eh_{L_e}(\widehat v_e)>0.
\tag{14}
\]

Let \(\ell_e\) be the canonical support-contact midpoint from accepted
facts 6496cb3b0fd44f9d and 0c5bcff6d676252e, and define the full and
marked contact measures of packet \(j\) by

\[
 \Sigma_j:=\frac12\sum_e\eta_e^{(j)}
             \delta_{(m_e,\ell_e)},
 \qquad
 \Xi_j:=\frac12\sum_e\kappa_e^{(j)}
             \delta_{(m_e,\ell_e)}.
\tag{15}
\]

They are carried by
\(C\cap(\mathbb Z^n\times\mathbb R^d)\), satisfy

\[
 0\le\Xi_j\le\Sigma_j,
 \qquad
 \sum_{j=1}^N\Xi_j=\sigma_\chi,
 \qquad
 \sum_{j=1}^N\Sigma_j
 =\frac12\sum_e\eta_e\delta_{(m_e,\ell_e)}
 \le\frac12\sum_e\omega_e\delta_{(m_e,\ell_e)},
\tag{16}
\]

and, for every closed ambient halfspace \(H\),

\[
 \boxed{
  \sum_{j=1}^N\Sigma_j(H)\le\mu_C(H),
  \qquad
  \sum_{j=1}^N\Xi_j(H)\le\mu_C(H).}
\tag{17}
\]

The exact marked mass is

\[
 \boxed{
  \left|\sum_{j=1}^N\Xi_j\right|
  =\frac12\sum_{j,e}\kappa_e^{(j)}
  =\frac X2>\frac Q{400}.}
\tag{18}
\]

Whenever \(\kappa_e^{(j)}>0\), that marked contact is one of the contacts
covered by equations (19)-(20) of accepted fact 0c5bcff6d676252e.
Thus the circuit packetization preserves the entire clipped geometric
overlap, not only its scalar mass.

## Proof

The proof of accepted fact 6496cb3b0fd44f9d obtains its circuit
decomposition by writing

\[
 \Xi_e^{\rm mom}
 :=\bigl(u_e,\operatorname{vec}(u_em_e^{\mathsf T})\bigr)
 \in\mathbb R^{d(n+1)}
\]

and decomposing the nonnegative relation

\[
 \sum_e\omega_e\Xi_e^{\rm mom}=0
\]

into extreme rays of the cone of nonnegative relations. In particular,
the coefficients in that construction sum coordinatewise, giving
(2)-(5), and every \(v_e^{(j)}\) is a nonnegative multiple of the same
vector \(u_e\) on a fixed edge.

For nonnegative \(a_1,\ldots,a_N,c\),
\(\min\{\sum_ja_j,c\}\le\sum_j\min\{a_j,c\}\): if some \(a_j\ge c\)
the right side is at least \(c\), while otherwise the right side equals
\(\sum_ja_j\). Applying this with \(a_j=\omega_e^{(j)}\), using (1) and
(3), proves (5a). Its upper bound follows from
\(\min\{\omega_e^{(j)},c_e\}\le\omega_e^{(j)}\).

Equation (1) gives \(0\le\theta_e\le1\). Hence \(0\le t_j\le1\).
If \(\omega_e^{(j)}>0\), the definition of the maximum in (6) gives
\(\theta_e\le t_j\). Therefore

\[
 0\le\theta_e\omega_e^{(j)}
 \le t_j\omega_e^{(j)}
 \le\omega_e^{(j)},
\]

which is the first part of (9). Coordinatewise summation and (3) give

\[
 \sum_j\kappa_e^{(j)}
 =\theta_e\sum_j\omega_e^{(j)}
 =\theta_e\omega_e
 =\chi_e.
\tag{19}
\]

Similarly,

\[
 \eta_e
 =\sum_jt_j\omega_e^{(j)}
 \ge\theta_e\sum_j\omega_e^{(j)}
 =\chi_e,
 \qquad
 \eta_e\le\sum_j\omega_e^{(j)}=\omega_e.
\tag{20}
\]

Accepted fact 6496cb3b0fd44f9d, applied to the reservoir \(r\), gives
\(\omega\le r\), proving (10). Summing (9)-(10) and using (1) proves
(11). This is the step that avoids any choice of one circuit and any
factor depending on \(N\).

Scaling (4) by \(t_j\) proves the two cancellations in (12), without
changing the support. Positive homogeneity of the support function and
(2) give

\[
 h_{D_e}(\widehat v_e^{(j)})
 =h_{D_e}(t_j\omega_e^{(j)}u_e)
 =t_j\omega_e^{(j)}h_{D_e}(u_e)
 =\eta_e^{(j)}.
\tag{21}
\]

Here \(h_{D_e}(u_e)=1\) by the definition of \(u_e\). Since
\(\eta^{(j)}\le\omega^{(j)}\le\omega\le r\), every packet has the
same-parity support and satisfies the endpoint bounds inherited from
the legal reservoir. Thus it is a legal matching. If \(t_j>0\), positive
homogeneity and (5) give

\[
 \sum_eh_{L_e}(\widehat v_e^{(j)})
 =t_j\sum_eh_{L_e}(v_e^{(j)})<0.
\]

The exact weighted dual formula of accepted fact 6496cb3b0fd44f9d, now
with capacities \(\eta^{(j)}\), proves (13). By (6)-(7), \(t_j>0\)
holds exactly when some
\(\theta_e\omega_e^{(j)}=\kappa_e^{(j)}\) is positive.

Summing (12) over \(j\) proves both aggregate moment cancellations. On
each fixed edge, (2), (7), and (8) give

\[
 \widehat v_e
 =\left(\sum_jt_j\omega_e^{(j)}\right)u_e
 =\eta_eu_e.
\tag{22}
\]

Consequently \(h_{D_e}(\widehat v_e)=\eta_e\). At least one \(t_j\) is
positive because \(X>0\), so summing the strict negative objectives of
the nonzero packets proves (14) by the same dual formula.

For every edge with positive original load, the point \(\ell_e\)
supports \(L_e\) in direction \(u_e\), hence also in every packet
direction \(\widehat v_e^{(j)}\). The reservoir satisfies the strong
endpoint bounds, and accepted fact 6496cb3b0fd44f9d therefore proves
that

\[
 \frac12\sum_e\omega_e\delta_{(m_e,\ell_e)}
\]

is carried by the mixed-integer body and is halfspace-dominated by
\(\mu_C\). Equations (9)-(10) show that every measure in (15), their
sums, and the marked measures are positive submeasures of this canonical
contact measure. Equations (16)-(17) follow. Finally, (19) and (1) give
(18), while positive marked weight implies \(\chi_e>0\), so the
contact-separation conclusions of accepted fact 0c5bcff6d676252e apply.
This completes the proof.

## External sources

none
