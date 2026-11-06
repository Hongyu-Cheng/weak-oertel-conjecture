---
fact_id: 9d6f430dbb8bce7c
kind: lemma
author: "research-agent"
assurance: LLM-verified
subgoal_id: square-used-unused-hard-dichotomy
depends_on: ["446c8f7967309a83","6bfe50fed9a5540b","d5d5de35c3f25af9"]
verifier_run: 0d51a35884fd4d33
target_match: null
---

## Statement

Retain one common canonical zero-fresh hard instance of accepted facts 6bfe50fed9a5540b and d5d5de35c3f25af9, together with the full degree-weighted square occurrence realization of accepted fact 446c8f7967309a83.  Thus

\[
 C_z:=\{x\in\mathbb R^d:(z,x)\in C\},
 \qquad
 a_z:=\operatorname{vol}_d(C_z),
 \qquad
 I_+:=\{z\in\mathbb Z^n:a_z>0\},
\]

\[
 W:=\sum_{z\in I_+}a_z,
 \qquad
 Q:=\sum_er_e>0,
 \qquad
 d_z(r)\leq\frac{a_z}{4},
\tag{1}
\]

where \(r\) is the half-strength canonical product reservoir.  Let \((\lambda_m)\) be the target loads of the same instance, put \(\Lambda:=\sum_m\lambda_m\), and let \(s^{\mathrm{tar}}\) be the exact minimum-unmatched off-diagonal target matching, with degrees \(d_m:=d_m(s^{\mathrm{tar}})\).  Put

\[
 P_{\mathrm{tar}}:=|s^{\mathrm{tar}}|,
 \qquad
 w_m:=\frac{d_m}{2},
 \qquad
 W_d:=\sum_mw_m=P_{\mathrm{tar}}.
\tag{2}
\]

Let \(\mathcal L^\square\) be the full degree-weighted whole-label set.  Every \(\sigma\in\mathcal L^\square\) has mass \(\theta_\sigma>0\) and a four-entry tagged source multiset \(\mathcal O_\sigma\), with every repeated tag retained.  Put

\[
 \Theta:=\sum_{\sigma\in\mathcal L^\square}\theta_\sigma,
 \qquad
 R_y:=\sum_{\sigma\in\mathcal L^\square}
 \theta_\sigma\operatorname{mult}_y(\mathcal O_\sigma).
\tag{3}
\]

For every simultaneous physical realization by occurrence densities \(f_{\sigma,o}\) of mass \(\theta_\sigma\), define

\[
 F_y:=\sum_{(\sigma,o):y(\sigma,o)=y}f_{\sigma,o},
 \qquad
 U_y:=a_y-\int_{C_y}F_y.
\tag{4}
\]

Then

\[
 \boxed{
 \sum_{y\in I_+}U_y\geq6Q>\frac Q{100}.}
\tag{5}
\]

Consequently the first alternative in the registered subgoal always holds.  This conclusion is unaffected by repeated tagged sources, physical-source reuse, target collisions, target overload, or the choice of the one physical occurrence ledger.

## Proof

Accepted fact 446c8f7967309a83 records the reservoir degree calculation

\[
 2Q=\sum_zd_z(r)
 \leq\frac14\sum_{z\in I_+}a_z
 =\frac W4.
\tag{6}
\]

Thus

\[
 W\geq8Q.
\tag{7}
\]

We next use the actual degree-weighted normalization, rather than only the global occurrence-moment identity.  Accepted fact d5d5de35c3f25af9 gives

\[
 0\leq d_m\leq\lambda_m
\tag{8}
\]

and identifies \(W_d=P_{\mathrm{tar}}\).  Because \(s^{\mathrm{tar}}\) is off-diagonal, each matching edge contributes its weight to two distinct endpoint degrees, so

\[
 2W_d=2P_{\mathrm{tar}}=\sum_md_m\leq\sum_m\lambda_m=\Lambda.
\tag{9}
\]

In accepted fact 6bfe50fed9a5540b, the same target loads are pushed back to an edge family \(b=(b_e)\) satisfying

\[
 0\leq b_e\leq r_e,
 \qquad
 \sum_eb_e=|b|=\Lambda.
\tag{10}
\]

Hence

\[
 \Lambda\leq\sum_er_e=Q,
 \qquad
 W_d\leq\frac Q2.
\tag{11}
\]

The degree-weighted square occurrence ledger in accepted fact d5d5de35c3f25af9 gives

\[
 R_y\leq4w_y
\tag{12}
\]

at every source, with both sides zero outside the degree support.  Reversing the finite sums in (3), every whole label contributes exactly four tagged occurrences.  This remains true for a zero-direction loop, where the repeated source is counted twice, and for arbitrary reuse of one source by different labels.  Therefore

\[
 4\Theta
 =\sum_yR_y
 \leq4\sum_yw_y
 =4W_d
 \leq2Q.
\tag{13}
\]

For the physical realization (4), every occurrence density has its prescribed mass \(\theta_\sigma\).  Thus

\[
 \int_{C_y}F_y=R_y
\tag{14}
\]

for every source, including all multiplicities, and (13) gives

\[
 \sum_{y\in I_+}\int_{C_y}F_y
 =4\Theta\leq2Q.
\tag{15}
\]

Combining (7) and (15) yields

\[
 \sum_{y\in I_+}U_y
 =W-\sum_{y\in I_+}\int_{C_y}F_y
 =W-4\Theta
 \geq8Q-2Q
 =6Q.
\tag{16}
\]

Since \(Q>0\), equation (16) is strictly stronger than the required \(Q/100\) alternative.  No target packing, affine interpolation, marginal-rank comparison, or cycle-space restriction is required.

## External sources

none
