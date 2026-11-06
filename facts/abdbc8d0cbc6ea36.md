---
fact_id: abdbc8d0cbc6ea36
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: hard-branch-labelled-defect-closure
depends_on: ["6b09aae189415c70"]
verifier_run: f53cfa5c79394722
target_match: null
---

## Statement

Let \(n,d\in\mathbb Z_{>0}\), let \(C\subseteq\mathbb R^n\times\mathbb R^d\) be a convex body, and put
\[
 C_z:=\{x\in\mathbb R^d:(z,x)\in C\},
 \qquad
 a_z:=\operatorname{vol}_d(C_z),
\]
\[
 Z:=\{z\in\mathbb Z^n:a_z>0\},
 \qquad
 W:=\sum_{z\in Z}a_z>0,
 \qquad
 G:=\mathfrak C_{\mathrm{core}}(C).
\]
Assume \(G<W/4\). Let \(r=(r_e)\) be the half-strength canonical product reservoir of accepted fact `6b09aae189415c70`, and put
\[
 Q:=|r|=\sum_e r_e>0,
\]
\[
 R:=R_C(r),
\]
using the exact normalization of that accepted fact. Use also its nonnegative capacities \(R_{\mathrm{sel}}(C)\), \(M_{\mathrm{off}}(C)\), and \(R_{\mathrm{cloud}}(C)\), and put
\[
 D:=2^n h_{\max}(C),
 \qquad
 \mathcal A(C):=R+G+R_{\mathrm{sel}}(C)+M_{\mathrm{off}}(C)
 +R_{\mathrm{cloud}}(C)+D.
\]
Then
\[
 \boxed{M_{\mathrm{off}}(C)\ge\frac{Q}{d+1}},
 \qquad
 \boxed{\mathcal A(C)\ge\frac{Q}{d+1}}.
\]
Consequently, if
\[
 \mathcal A(C)<\frac{Q}{100},
\]
then
\[
 \boxed{d\ge 100}.
\]

## Proof

Accepted fact `6b09aae189415c70` defines the reservoir centroid measure
\[
 \bar\nu_r:=\sum_e r_e\,\delta_{(m_e,\bar c_e)}
\]
and proves that every nonzero positive submeasure \(\sigma\le\bar\nu_r\) satisfies
\[
 M_{\mathrm{off}}(C)
 \ge 2^{n-\rho_\sigma}\frac{|\sigma|}{r_\sigma+1},
\tag{1}
\]
where \(\rho_\sigma\) is the affine dimension of the base support and \(r_\sigma\) is its intrinsic continuous residual rank.

Take \(\sigma=\bar\nu_r\). This is an admissible nonzero positive submeasure, and
\[
 |\bar\nu_r|=\sum_e r_e=Q.
\tag{2}
\]
Because its base coordinates \(m_e\) lie in \(\mathbb R^n\),
\[
 \rho_{\bar\nu_r}\le n.
\tag{3}
\]
In the definition of continuous residual rank, the zero affine map on the affine hull of the base support is admissible. All resulting residual vectors \(\bar c_e\) lie in \(\mathbb R^d\), and therefore
\[
 r_{\bar\nu_r}\le d.
\tag{4}
\]
Applying (1) to the full reservoir measure and using (2)--(4) gives
\[
 M_{\mathrm{off}}(C)
 \ge 2^{n-\rho_{\bar\nu_r}}
       \frac{Q}{r_{\bar\nu_r}+1}
 \ge \frac{Q}{d+1}.
\tag{5}
\]
Since \(M_{\mathrm{off}}(C)\) is a nonnegative summand of \(\mathcal A(C)\),
\[
 \mathcal A(C)\ge M_{\mathrm{off}}(C)\ge\frac{Q}{d+1}.
\tag{6}
\]
If \(d\le99\), then (6) yields \(\mathcal A(C)\ge Q/100\), contradicting the strict hypothesis. Hence \(d\ge100\).

## External sources

none
