---
fact_id: dc42e04c0bfdf6d0
kind: lemma
author: "research-agent"
assurance: LLM-verified
subgoal_id: dyadic-stress-frame-aggregation
depends_on: ["2fe46f47d19112ea","a3986a5e951b789b","bf0d5c250b8f688c"]
verifier_run: dc98cf479b5c4339
target_match: null
---

## Statement

Retain the canonical hard-branch objects and notation of accepted facts 2fe46f47d19112ea, a3986a5e951b789b, and bf0d5c250b8f688c. Thus
\[
 n\geq 2,\qquad d\geq 1,\qquad
 \gamma_d:=\left(\frac d{d+1}\right)^d,\qquad
 D:=2^n h_{\max}(C)<\frac Q{100},
\tag{1}
\]
where \(Q>0\). Fix a missed dyadic edge
\[
 e_0=\{u,w\}\in\mathcal E_{\mathrm{miss}},
 \qquad t_0:=t_{e_0}>0.
\tag{2}
\]
Let \(\sigma_0,\ldots,\sigma_{N-1}\) be any distinct rescaled internal atlas labels forming a downstream one-edge star at \(e_0\): the two opposite endpoints of \(\sigma_j\) are \(a_j,b_j\), where
\[
 a_j\in\{u,w\},\qquad b_j\notin\{u,w\},
\tag{3}
\]
and its rescaled weight is \(\eta_j>0\). Put
\[
 H_\star:=\sum_{j=0}^{N-1}\eta_j.
\tag{4}
\]
Then
\[
 \boxed{H_\star\leq 2t_0<\frac{Q}{200\,2^n}.}
\tag{5}
\]

In particular, apply (5) to any \(N=n\) star satisfying all the additional distinct-edge and product-chart rank hypotheses of accepted fact a3986a5e951b789b. Its universal selected-mass conclusion is
\[
 D\geq 2\gamma_d H_\star.
\tag{6}
\]
For (6) by itself to contradict the hard inequality in (1), it would be necessary that
\[
 H_\star\geq\frac{Q}{200\gamma_d}.
\tag{7}
\]
But the two thresholds are separated by
\[
 H_\star<\frac{Q}{200\,2^n}
 \leq\frac Q{800}
 <\frac Q{100}
 \leq\frac{Q}{200\gamma_d}.
\tag{8}
\]
Consequently, no invocation of the universal mass bound (6) for a single downstream edge can be terminal. This includes every star whose column simplex has no nonvertex lattice point, because in that case accepted fact a3986a5e951b789b gives exact packet energy \(2\gamma_dH_\star\).

For completeness, let \(\mathcal B_\eta\) be the exact barycentric lattice energy of a star in accepted fact a3986a5e951b789b, so that its exact packet energy is \(2\gamma_d\mathcal B_\eta\) and \(\mathcal B_\eta\geq H_\star\). A terminal use of this stronger exact formula would require
\[
 \mathcal B_\eta\geq\frac{Q}{200\gamma_d},
\tag{9}
\]
and hence, by (5), the genuinely new amplification estimate
\[
 \boxed{
 \mathcal B_\eta-H_\star
 >\frac Q{200}
 \left(\frac1{\gamma_d}-\frac1{2^n}\right).}
\tag{10}
\]
The accepted endpoint-capacity facts do not provide (10). Therefore the precise conclusion is that accepted fact a3986a5e951b789b is not a terminal one-star theorem under the currently accepted mass information. It can become terminal only after a new theorem proving the independent lattice-point amplification (10), or after a genuinely new multi-star aggregation mechanism.

## Proof

For \(y\in\{u,w\}\), let
\[
 J_y:=\{j:a_j=y\}.
\tag{11}
\]
Because (3) assigns exactly one endpoint of each selected label to \(\{u,w\}\), the two sets \(J_u,J_w\) partition \(\{0,\ldots,N-1\}\). Every label indexed by \(J_y\) is an internal label incident to the physical endpoint \(y\). The exact downstream endpoint-capacity inequality (13) of accepted fact 2fe46f47d19112ea therefore gives
\[
 \sum_{j\in J_y}\eta_j
 \leq
 \sum_{\substack{\sigma\in\mathscr A_{\mathrm{int}}\\
 y\in\{a(\sigma),b(\sigma)\}}}\eta_\sigma
 \leq t_{e_2(y)}=t_0.
\tag{12}
\]
Here \(e_2(u)=e_2(w)=e_0\), because the retained dyadic matching is endpoint-disjoint. Summing (12) for \(y=u,w\) proves
\[
 H_\star
 =\sum_{j\in J_u}\eta_j+
  \sum_{j\in J_w}\eta_j
 \leq2t_0.
\tag{13}
\]
The canonical strict dyadic cap (4) of accepted fact bf0d5c250b8f688c is
\[
 t_0<\frac{Q}{400\,2^n}.
\tag{14}
\]
Equations (13) and (14) prove (5).

We next compare the thresholds without numerical approximation. The binomial theorem gives
\[
 \frac1{\gamma_d}
 =\left(1+\frac1d\right)^d
 \geq 1+d\frac1d=2,
\tag{15}
\]
so \(\gamma_d\leq1/2\). Together with \(n\geq2\), this proves every comparison in (8).

Accepted fact a3986a5e951b789b gives (6) for every star satisfying its full hypotheses. The two inequalities \(D<Q/100\) and \(D\geq2\gamma_dH_\star\) can be numerically inconsistent on the strength of the latter lower bound only if
\[
 2\gamma_dH_\star\geq\frac Q{100},
\tag{16}
\]
which is exactly (7). Equations (5) and (8) show that (16) is impossible. If the column simplex has no nonvertex lattice point, the exact-energy equality in accepted fact a3986a5e951b789b makes (6) the full packet conclusion, so that case is also nonterminal.

In the general column-simplex case, the same accepted fact instead gives
\[
 D\geq2\gamma_d\mathcal B_\eta,
 \qquad \mathcal B_\eta\geq H_\star.
\tag{17}
\]
This stronger lower bound contradicts (1) only if (9) holds. Subtracting the strict upper bound in (5) from (9) gives (10). Positivity of additional lattice-point summands alone supplies no quantitative lower bound of the size in (10). Hence the current accepted facts rule out terminality from one-star selected mass, while leaving (10) as a separate new mechanism rather than silently treating it as proved. This completes the calibration.

## External sources

none
