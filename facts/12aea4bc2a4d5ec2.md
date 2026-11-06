---
fact_id: 12aea4bc2a4d5ec2
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: intake18-fractional-center-rank-depth
depends_on: ["5bd39b316ef3c194","9ee12600178ce4dd"]
verifier_run: a88ac853c1ec42d0
target_match: null
---

## Statement

Let \(C,S,T,\ell_i^\pm\) be an admissible roof body:
\[
C=\{(\mathbf x,\mathbf y):
\mathbf y\in T,\ -\ell_i^-(\mathbf y)\le x_i\le1+\ell_i^+(\mathbf y)\},
\quad S=C\cap(\mathbb Z^n\times\mathbb R^d),
\]
where \(T\) is a compact convex body and the roofs are nonnegative, bounded, upper-semicontinuous, and concave. Define
\[
a_i=\lfloor\ell_i^-\rfloor,\quad b_i=\lfloor\ell_i^+\rfloor,\quad
N_i=a_i+b_i+2,\quad B=\prod_i(N_i-1),\quad M=\int_TB,
\]
\[
f(N)=N(N^2-1)/(N^2+2),\quad F=\prod_if(N_i),
\quad \mathbf m=(\mathbf1+\mathbf b-\mathbf a)/2.
\]
With respect to \(d\)-dimensional Lebesgue measure on \(T\), define
\[
\operatorname{essran}_T(\mathbf m)
:=\left\{\mathbf u\in\mathbb R^n:
\left|\{\mathbf y\in T:\|\mathbf m(\mathbf y)-\mathbf u\|<\varepsilon\}\right|>0
\text{ for every }\varepsilon>0\right\},
\]
and let
\[
r:=\dim\operatorname{aff}(\operatorname{essran}_T(\mathbf m)).
\]
Equivalently, \(r\) is the dimension of the smallest affine subspace of \(\mathbb R^n\) containing \(\mathbf m(\mathbf y)\) for almost every \(\mathbf y\in T\). For \(\mathbf y\in T\), define
\[
\tau_B(\mathbf y):=
\inf_{\substack{L\subseteq\mathbb R^d\text{ a proper closed halfspace}\\
\mathbf y\in L}}
\int_{T\cap L}B(\mathbf z)\,d\mathbf z,
\qquad
\Delta_B:=\max_{\mathbf y\in T}\tau_B(\mathbf y).
\]
Let \(H_*=\max_Sh_S\) for actual closed-halfspace mixed depth.

For every \(0<\alpha<1\),
\[
H_*\ge
\frac{e^{\alpha-1}(3^{1-\alpha}-2^{1-\alpha})}
{144^\alpha(r+1)^\alpha}\int_TF^\alpha. \tag{1}
\]
If all \(N_i\le3\) almost everywhere, then
\[
H_*\ge M/[2500(r+1)^{9/10}]
\ge\Delta_B/[1250(r+1)^{9/10}].
\]
More generally, for an integer \(L\ge3\), set
\[
\alpha_L=\max_{3\le N\le L}
\frac{\log(N-1)}{\log f(N)}<1.
\]
If all \(N_i\le L\), then (1) with \(\alpha=\alpha_L\) has \(\int_TF^\alpha\ge M\).

## Proof

We need a sectionwise counting bound. In an integer box with center \(\mathbf m\), every halfspace containing \(\mathbf m+\mathbf e\), \(|e_i|\le1/2\), contains at least \(\prod_if(N_i)/144\) points.

Here is a direct verification. Fix the favorable endpoint of every two-site coordinate. For \(N\ge3\), a centered uniform interval has variance \(v=(N^2-1)/12\). Change its law by \(1+eX/v\). This nonnegative likelihood gives mean \(e\), variance \(v-e^2\), and centered fourth moment at most \(3(v-e^2)^2\): substituting
\(\kappa=3(3N^2-7)/(5(N^2-1))\) reduces the claim to
\((3-\kappa)(1-4t)+6t^2\ge0\), with \(t=e^2/v\).
Independent sums then have kurtosis at most three, so each side of the mean has probability at least \(1/12\), by interpolation and Cauchy-Schwarz. The likelihood second moment is at most
\((N^2+2)/(N^2-1)\). Cauchy-Schwarz transfers this probability to the original box and proves the count.

Put mass \(F(\mathbf y)d\mathbf y\) at the graph point \((\mathbf m(\mathbf y),\mathbf y)\). Since \(F\ge1\), its center-map essential range has the same affine hull as the Lebesgue essential range used to define \(r\). Its base projection has density \(F\); denote its maximal base depth by \(\Delta_F\). Deleting the \(r\)-dimensional affine span of the centers admits a lift of depth \(\Delta_F/(r+1)\). To verify this projection assertion, intersect all halfspaces of mass greater than \(Z-\Delta_F/(r+1)\) with the prescribed fiber. An infeasible finite family has nonnegative eliminating multipliers supported on at most \(r+1\) inequalities. Their sum produces a projected containing halfspace of mass less than \(\Delta_F\), a contradiction. Compactness gives a common point; a smaller cap would have a heavy complement excluding it.

The lifted point belongs to the convex hull of the graph, which is contained in
\[
-\ell_i^-+1/2\le x_i\le\ell_i^++1/2.
\]
Round its integer-coordinate component to nearest integers. This is feasible in \(C\), and the sectionwise counting bound gives
\[
H_*\ge\Delta_F/[144(r+1)]. \tag{2}
\]

Write \(V=|T|\). Accepted fact 9ee12600178ce4dd, with reference \(V^{-1}\mathbf1_T\) and density \(F\), gives
\[
\Delta_F\ge
\kappa_\alpha
(\int_TF^\alpha)^{1/\alpha}/V^{(1-\alpha)/\alpha}.
\]
Also \(H_*\ge V/e\): fix any core integer vertex and the centroid of \(T\), then restrict each containing ambient halfspace to that full fiber. The log-concave centroid halfspace inequality recorded in the proof and external sources of accepted fact 5bd39b316ef3c194 applies to the uniform law on \(T\).

Thus \(V\le eH_*\). Substitute this into (2), rearrange, and raise to the power \(\alpha\). Since
\(\kappa_\alpha^\alpha=3^{1-\alpha}-2^{1-\alpha}\), this proves (1). The points supplying the two lower bounds on \(H_*\) need not coincide.

For bounded widths, \(f(2)=1\) and \(f(N)>N-1\) for \(N\ge3\), giving the \(\alpha_L\) assertion. When \(N_i\le3\), \(f(3)=24/11\) and
\(24^9>2^{10}11^9\), so \(F^{9/10}\ge B\).
The coefficient in (1) exceeds \(1/2500\), using
\(e^{-1/10}>9/10\),
\(3^{1/10}-2^{1/10}>1/25\),
and \(144^{9/10}<90\).
Finally, \(\Delta_B\le M/2\), proving the stated comparison.

## External sources

None beyond the declared accepted predecessors. The centroid inequality is used in precisely the form recorded by 5bd39b316ef3c194, not its separate entropy theorem with a continuity assumption.
