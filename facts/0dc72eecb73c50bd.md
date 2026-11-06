---
fact_id: 0dc72eecb73c50bd
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: oct3ae-optimal-hellinger-center-energy-audit
depends_on: ["488f0a583886b5fc","8660ffca617b9702"]
verifier_run: 2d12eac9cca74192
target_match: null
---

## Statement

Let \(a,b\in\mathbb Z\), \(a\le b\), and \(D=\{a,\ldots,b\}\). Let \(w_j>0\) for \(j\in D\), let \(w_j=0\) off \(D\), and assume \(w_j^2\ge w_{j-1}w_{j+1}\) for every integer \(j\). Use the canonical source weights and normalization
\(W=\sum_{j\in D}w_j\), \(w_{\max}=\max_{j\in D}w_j\), and \(\phi_j=\log(w_{\max}/w_j)\) on \(D\). All logarithms are natural.

The scalar indices \(j,J\) are the \(n=1\) aliases of \(\mathbf I,\mathbf J\) in accepted fact `488f0a583886b5fc`; \(D,W,w_{\max},\phi\) retain that fact's meanings. The source probability alias is \(p_j=w_j/W\), exactly as in accepted fact `8660ffca617b9702`. For an actual complete fiber table, the source measure and total mass remain \(w_j=\mathcal L^d(C_j)\) and \(W=\mathcal H_d(S)\). The locked \(h_S\) remains the unnormalized halfspace depth; none of the Hellinger quantities below is identified with it.

Define

\[
R_J=\sum_{v\in\mathbb Z}\sqrt{w_{J+v}w_{J-v}},
\qquad R=\max_{J\in D}R_J.
\]

These are the exact aliases \(R_J=\mathcal R_J(w)\) and \(R=R_{1/2}(w)\) of accepted fact `8660ffca617b9702`. At a fixed center \(J\in D\), write \(\alpha_J(v)=\min\{w_{J+v},w_{J-v}\}\) and \(\mathcal U_J=\{v:\alpha_J(v)>0\}\). Here \(\alpha_J\) is the accepted fact `488f0a583886b5fc`'s suppressed-center capacity \(\alpha\) with its center \(j=J\), and \(\mathcal U_J\) has that fact's meaning. All displacement sums are oriented and include zero.

On \(\mathcal U_J\), define the displacement probability, curvature gap, and imbalance by

\[
\begin{aligned}
Q_J(v)&=\frac{\sqrt{w_{J+v}w_{J-v}}}{R_J},\\
G_J(v)&=\frac{\phi_{J+v}+\phi_{J-v}}2-\phi_J,\\
A_J(v)&=\frac{\phi_{J+v}-\phi_{J-v}}2.
\end{aligned}
\]

Thus \(Q_J\) is not the source probability \(p\). Also \(2G_J(v)=\Delta_J(v)\) for the canonical curvature \(\Delta\) in accepted fact `488f0a583886b5fc`; \(A_J\) is the newly defined imbalance, not a support set. Expectations below are sums against \(Q_J\) on \(\mathcal U_J\).

For every \(J\in D\) satisfying \(R_J\ge W/2\),

\[
\begin{aligned}
0\le\phi_J&\le2\log4,\\
\mathbb E_{Q_J}\!\left[\exp\!\left(\frac{\phi_{J+v}}4\right)\right]&\le2\sqrt2,\\
\mathbb E_{Q_J}\!\left[G_J(v)^2+A_J(v)^2\right]
&\le\frac{128\sqrt2}{e^2}<32.
\end{aligned}
\]

In particular these inequalities hold at every \(J\in\operatorname{argmax}_{K\in D}R_K\), so the requested common bound holds with \(C=32\). Ties and endpoint atoms are retained.

The actual capacity obeys the exact identity \(\alpha_J(v)=R_JQ_J(v)e^{-|A_J(v)|}\). Consequently every such center also satisfies

\[
\sum_{\substack{v\in\mathcal U_J\\G_J(v)^2+A_J(v)^2\le64}}
\alpha_J(v)
\ge\frac{e^{-8}}2R_J
\ge\frac{e^{-8}}4W.
\]

## Proof

Taking logarithms of log-concavity shows that the successive differences of \(\phi\) are nondecreasing. Hence its piecewise-affine interpolation on \([a,b]\) is convex. In particular \(\phi\ge0\), \(\min_D\phi=0\), and \(\phi_J\le(\phi_{J+v}+\phi_{J-v})/2\) on \(\mathcal U_J\). This also verifies the one-dimensional convex-admissible interpretation in accepted fact `488f0a583886b5fc`. It follows that \(G_J\ge0\).

We first prove an auxiliary mass bound without any maximizing-center assumption. Define the auxiliary tempered weights \(\widetilde w_j=\sqrt{w_{\max}w_j}\), zero off \(D\), and \(\widetilde W=\sum_j\widetilde w_j\). On \(D\), \(\widetilde w_j=w_j e^{\phi_j/2}=w_{\max}e^{-\phi_j/2}\). These auxiliary weights do not replace any canonical source capacity.

Choose any mode \(m\in D\), so \(\phi_m=0\). If \(m+2\ell\in D\), convexity at the midpoint of \(m\) and \(m+2\ell\) gives \(\phi_{m+\ell}\le\phi_{m+2\ell}/2\), and therefore \(\widetilde w_{m+2\ell}\le w_{m+\ell}\). This holds for positive, zero, and negative \(\ell\).

If \(m+2\ell+1\in D\), the point \(m+\ell+1/2\) lies halfway between \(m\) and \(m+2\ell+1\). The two consecutive sites \(m+\ell,m+\ell+1\) lie in \(D\), including when \(\ell<0\). The piecewise-affine interpolation and convexity give

\[
\frac{\phi_{m+\ell}+\phi_{m+\ell+1}}2
\le\frac{\phi_{m+2\ell+1}}2,
\qquad
\widetilde w_{m+2\ell+1}
\le\sqrt{w_{m+\ell}w_{m+\ell+1}}.
\]

The contraction maps in the even and odd classes are each injective. Summing their bounds, then using the arithmetic-geometric mean inequality, proves

\[
\begin{aligned}
\widetilde W
&\le W+\sum_{j=a}^{b-1}\sqrt{w_jw_{j+1}}\\
&\le W+\frac12\sum_{j=a}^{b-1}(w_j+w_{j+1})\\
&=2W-\frac{w_a+w_b}{2}\le2W.
\end{aligned}
\]

When \(a=b\), the adjacent-site sums are empty and the displayed identity still holds. Thus the proof includes singleton supports, finite boundaries, and arbitrary changes of slope.

Now fix \(J\in D\) with \(R_J\ge W/2\). For each reflected pair, convexity gives

\[
\begin{aligned}
\sqrt{w_{J+v}w_{J-v}}
&=w_{\max}\exp\!\left(-\frac{\phi_{J+v}+\phi_{J-v}}2\right)\\
&\le e^{-\phi_J/2}
\sqrt{\widetilde w_{J+v}\widetilde w_{J-v}}.
\end{aligned}
\]

Cauchy-Schwarz over \(\mathcal U_J\) bounds the sum of the final square roots by \(\widetilde W\). Therefore \(W/2\le R_J\le e^{-\phi_J/2}\widetilde W\le2W e^{-\phi_J/2}\). This proves \(\phi_J\le2\log4\) directly from discrete convexity and the required mass condition.

A second Cauchy-Schwarz application proves the endpoint exponential moment:

\[
\begin{aligned}
\mathbb E_{Q_J}\!\left[e^{\phi_{J+v}/4}\right]
&=\frac1{R_J}\sum_{v\in\mathcal U_J}
\sqrt{\bigl(w_{J+v}e^{\phi_{J+v}/2}\bigr)w_{J-v}}\\
&\le\frac{\sqrt{\widetilde W W}}{R_J}
\le2\sqrt2.
\end{aligned}
\]

The two sums in Cauchy-Schwarz run over subsets of the complete source support, so the bounds by \(\widetilde W\) and \(W\) require no extension of \(\phi\) to zero-weight sites.

For every \(t\ge0\), \(t^2\le(64/e^2)e^{t/4}\). Indeed, differentiating \(t^2e^{-t/4}\) shows that its maximum is attained at \(t=8\), with value \(64/e^2\). Hence \(\mathbb E_{Q_J}[\phi_{J+v}^2]\le128\sqrt2/e^2\).

The probability \(Q_J\) is even in \(v\). Expanding the definitions and using this symmetry gives

\[
\begin{aligned}
\mathbb E_{Q_J}[G_J^2+A_J^2]
&=\frac12\mathbb E_{Q_J}\!\left[
(\phi_{J+v}-\phi_J)^2+(\phi_{J-v}-\phi_J)^2\right]\\
&=\mathbb E_{Q_J}[\phi_{J+v}^2]
-2\phi_J\mathbb E_{Q_J}[\phi_{J+v}]+\phi_J^2.
\end{aligned}
\]

Moreover \(\mathbb E_{Q_J}[\phi_{J+v}]=\mathbb E_{Q_J}[(\phi_{J+v}+\phi_{J-v})/2]\ge\phi_J\). Since \(\phi_J\ge0\), the last display is at most \(\mathbb E_{Q_J}[\phi_{J+v}^2]-\phi_J^2\), and hence at most \(128\sqrt2/e^2\). To check the stated simple constant, \(e^2>7\) follows by summing the first five terms of its exponential series, whose sum is seven, and retaining the positive remainder. Also \(\sqrt2<3/2\). Thus \(128\sqrt2/e^2<192/7<32\), while \(2\log4<4<32\).

Accepted fact `8660ffca617b9702`, applied with the exact aliases stated above, gives \(R\ge W/2\). The finite maximum is attained, and every maximizing center consequently satisfies the hypothesis just used. No choice among ties or exclusion of endpoint centers is needed.

For completeness, direct substitution gives

\[
\begin{aligned}
R_JQ_J(v)e^{-|A_J(v)|}
&=w_{\max}\exp\!\left(
-\frac{\phi_{J+v}+\phi_{J-v}}2
-\frac{|\phi_{J+v}-\phi_{J-v}|}2\right)\\
&=w_{\max}e^{-\max\{\phi_{J+v},\phi_{J-v}\}}
=\alpha_J(v).
\end{aligned}
\]

Markov's inequality and the energy bound give \(Q_J\{G_J^2+A_J^2\le64\}\ge1/2\). On this event, \(|A_J|\le8\), so summing the exact capacity identity proves the stated capacity consequence. The cutoff uses a weak inequality and retains all tied atoms.

Two exact calibrations also locate the actual maximizing center. First, let \(D=\{0,\ldots,N\}\) and \(w_j=\rho^j\), with \(N\ge0\) and \(0<\rho<1\), and put \(\lambda=-\log\rho\). Then \(R_J=(2\min\{J,N-J\}+1)\rho^J\). If \(J>N/2\), its reflected center \(N-J\) has the same number of terms and strictly larger weight, so every maximizer satisfies \(J\le\lfloor N/2\rfloor\). If such a maximizer has \(J\ge1\), comparison with \(J-1\) gives \(\lambda\le\log((2J+1)/(2J-1))\le2/(2J-1)\), hence \(\phi_J=\lambda J\le2\). Its \(Q_J\) is uniform on \(\{-J,\ldots,J\}\), with \(G_J=0\) and \(A_J(v)=\lambda v\). Thus its energy is \(\lambda^2J(J+1)/3\le8/3\); here \(2J-1\ge J\) and \((J+1)/J\le2\). If \(J=0\), the energy is zero. If \(\rho=1\), every potential and energy is zero. These conclusions hold regardless of support length and retain maximizing-center ties.

Second, for \((w_0,w_1,w_2)=(1,1,t^2)\) with \(0<t\le1\), the only nontrivial log-concavity condition is \(1\ge t^2\). The centered sums are \(1,1+2t,t^2\), so the unique maximizer is \(J=1\). Its potential is zero. At each of \(v=\pm1\), the energy is \(2(\log t)^2\) and the probability is \(t/(1+2t)\); the central energy is zero. Its expected energy is exactly \(4t(\log t)^2/(1+2t)\), tending to zero as \(t\downarrow0\). Indeed, with \(u=-\log t\), \(u^2e^{-u}\le6/u\) for \(u>0\), by the exponential series. The potentially large tail cost is therefore paid with its exact rare-event probability. Both calibrations are algebraic checks; no numerical calculation is a premise of the universal argument.

## External sources

None. Accepted fact `8660ffca617b9702` supplies the Hellinger half-mass threshold. Accepted fact `488f0a583886b5fc` supplies the canonical table, capacity, curvature, and actual-fiber interpretation. All tempered-mass, center-sublevel, exponential-moment, energy, capacity-consequence, and calibration assertions are proved above.
