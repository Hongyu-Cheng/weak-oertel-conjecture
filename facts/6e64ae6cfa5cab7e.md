---
fact_id: 6e64ae6cfa5cab7e
kind: lemma
author: "research-agent"
assurance: LLM-verified
subgoal_id: trimmed-zonoid-coupled-sum-inclusion
depends_on: []
verifier_run: 0a8316e2ac944ba3
target_match: null
---

## Statement

Let \((\Omega,\mathcal A,\mathbb P)\) be a probability space, let \(d,k\in\mathbb Z_{>0}\), let \(X_1,\ldots,X_k\in L^1(\Omega;\mathbb R^d)\), let \(\lambda_1,\ldots,\lambda_k\ge 0\) satisfy \(\sum_{i=1}^k\lambda_i=1\), and let \(0<\alpha\le 1\). For every \(X\in L^1(\Omega;\mathbb R^d)\), define
\[
\mathcal F_\alpha:=\{f\in L^\infty(\Omega):0\le f\le 1\ \mathbb P\text{-a.s.},\ \mathbb E f=\alpha\}
\]
and
\[
Z_\alpha(X):=\left\{\alpha^{-1}\mathbb E[fX]:f\in\mathcal F_\alpha\right\}.
\]
Then \(Z_\alpha(X)\) is nonempty, compact, and convex.

More precisely, for every \(u\in\mathbb R^d\), writing \(Y=u^{\mathsf T}X\), its support function is the exact upper-tail average
\[
h_{Z_\alpha(X)}(u)
=\sup_{f\in\mathcal F_\alpha}\frac1\alpha\mathbb E[fY]
=\inf_{t\in\mathbb R}\left\{t+\frac1\alpha\mathbb E[(Y-t)_+]\right\}.
\]
If \(0<\alpha<1\), let \(F_Y(t)=\mathbb P(Y\le t)\), let
\[
q:=\inf\{t\in\mathbb R:F_Y(t)\ge 1-\alpha\},
\qquad
a:=\mathbb P(Y>q),
\]
and set \(\theta=(\alpha-a)/\mathbb P(Y=q)\) when \(\mathbb P(Y=q)>0\), and \(\theta=0\) otherwise. Then \(0\le\theta\le1\), the supremum is attained by
\[
f_*=\mathbf 1_{\{Y>q\}}+\theta\mathbf 1_{\{Y=q\}},
\]
and the common value is
\[
\frac1\alpha\left(\mathbb E[Y\mathbf 1_{\{Y>q\}}]+q(\alpha-a)\right)
=q+\frac1\alpha\mathbb E[(Y-q)_+].
\]
Thus an atom at the threshold is taken in exactly the fraction needed to make the selected mass \(\alpha\). Equivalently, if \(Q_Y(s):=\inf\{t:F_Y(t)\ge s\}\) for \(0<s<1\), then for every \(0<\alpha\le1\),
\[
h_{Z_\alpha(X)}(u)=\frac1\alpha\int_{1-\alpha}^1Q_Y(s)\,ds.
\]
For \(\alpha=1\), these formulas mean
\[
h_{Z_1(X)}(u)=\mathbb E Y
=\inf_{t\in\mathbb R}\{t+\mathbb E[(Y-t)_+]\}
=\int_0^1Q_Y(s)\,ds;
\]
the infimum need not be attained at a finite \(t\).

Finally, for the given joint coupling on \(\Omega\),
\[
Z_\alpha\!\left(\sum_{i=1}^k\lambda_iX_i\right)
\subseteq
\sum_{i=1}^k\lambda_iZ_\alpha(X_i).
\]

## Proof

The constant function \(f\equiv\alpha\) belongs to \(\mathcal F_\alpha\), so \(Z_\alpha(X)\) is nonempty. The set \(\mathcal F_\alpha\) is convex. It is also weak-star compact in \(L^\infty(\mathbb P)=(L^1(\mathbb P))^*\): it is a weak-star closed subset of the weak-star compact unit ball, because the order constraints \(0\le f\le1\) and the equation \(\mathbb Ef=\alpha\) are weak-star closed. Since every coordinate of \(X\) lies in \(L^1(\mathbb P)\), the map
\[
f\longmapsto\alpha^{-1}\mathbb E[fX]\in\mathbb R^d
\]
is weak-star continuous and linear. Its image \(Z_\alpha(X)\) is therefore compact and convex.

Fix \(u\in\mathbb R^d\) and put \(Y=u^{\mathsf T}X\in L^1\). By the definition of a support function,
\[
h_{Z_\alpha(X)}(u)=\sup_{f\in\mathcal F_\alpha}\frac1\alpha\mathbb E[fY].
\]
For every \(f\in\mathcal F_\alpha\) and \(t\in\mathbb R\), the pointwise inequalities \(0\le f\le1\) give
\[
f(Y-t)\le(Y-t)_+.
\]
Consequently,
\[
\frac1\alpha\mathbb E[fY]
\le t+\frac1\alpha\mathbb E[(Y-t)_+].
\]
Taking first the supremum over \(f\) and then the infimum over \(t\) proves one inequality in the support formula.

Assume first that \(0<\alpha<1\). The quantile \(q\) in the statement is finite. Right continuity of \(F_Y\) and the definition of \(q\) give
\[
\mathbb P(Y>q)\le\alpha\le\mathbb P(Y\ge q).
\]
Thus \(a\le\alpha\le a+\mathbb P(Y=q)\). If \(\mathbb P(Y=q)=0\), these inequalities force \(a=\alpha\); otherwise they show \(0\le\theta\le1\). Hence the stated \(f_*\) satisfies \(0\le f_*\le1\) and \(\mathbb Ef_*=\alpha\). Moreover,
\[
\begin{aligned}
\frac1\alpha\mathbb E[f_*Y]
&=\frac1\alpha\left(\mathbb E[Y\mathbf 1_{\{Y>q\}}]+q(\alpha-a)\right)\\
&=q+\frac1\alpha\mathbb E[(Y-q)_+].
\end{aligned}
\]
The right side is the preceding upper bound evaluated at \(t=q\). Therefore the supremum and infimum are equal, both displayed upper-tail formulas are exact, and \(f_*\) attains the supremum even when the threshold is an atom.

For completeness, let \(U\) be uniform on \((0,1)\) on an auxiliary probability space. The generalized inverse satisfies \(Q_Y(U)\stackrel{d}=Y\). With \(q=Q_Y(1-\alpha)\), one has \(Q_Y(s)=q\) for almost every \(s\in(1-\alpha,F_Y(q)]\), while \(Q_Y(s)>q\) for almost every \(s\in(F_Y(q),1)\). It follows that
\[
\begin{aligned}
\int_{1-\alpha}^1Q_Y(s)\,ds
&=q\bigl(F_Y(q)-(1-\alpha)\bigr)
  +\int_{F_Y(q)}^1Q_Y(s)\,ds\\
&=q(\alpha-a)+\mathbb E[Y\mathbf 1_{\{Y>q\}}],
\end{aligned}
\]
which proves the quantile-integral form for \(0<\alpha<1\).

If \(\alpha=1\), every \(f\in\mathcal F_1\) equals \(1\) almost surely, so the support function is \(\mathbb EY\). For each \(t\in\mathbb R\),
\[
t+\mathbb E[(Y-t)_+]
=\mathbb E[\max\{Y,t\}]
=\mathbb EY+\mathbb E[(t-Y)_+]
\ge\mathbb EY.
\]
As \(t\to-\infty\), \((t-Y)_+\to0\) pointwise, and for every \(t\le0\) one has \((t-Y)_+\le Y^-\), so dominated convergence gives equality after taking the infimum. Also \(Q_Y(U)\stackrel d=Y\) and \(Y\in L^1\), hence \(Q_Y\in L^1(0,1)\) and \(\int_0^1Q_Y(s)\,ds=\mathbb EY\). This proves every support formula, including \(\alpha=1\).

It remains to prove the coupled-sum inclusion. Put \(S=\sum_{i=1}^k\lambda_iX_i\) and \(Y_i=u^{\mathsf T}X_i\). For every \(u\in\mathbb R^d\), using the same admissible trimming weight on the given joint probability space gives
\[
\begin{aligned}
h_{Z_\alpha(S)}(u)
&=\sup_{f\in\mathcal F_\alpha}
  \sum_{i=1}^k\lambda_i\frac1\alpha\mathbb E[fY_i]\\
&\le\sum_{i=1}^k\lambda_i
  \sup_{g_i\in\mathcal F_\alpha}\frac1\alpha\mathbb E[g_iY_i]\\
&=\sum_{i=1}^k\lambda_i h_{Z_\alpha(X_i)}(u)\\
&=h_{\sum_{i=1}^k\lambda_iZ_\alpha(X_i)}(u).
\end{aligned}
\]
Both sides of the desired inclusion are compact convex sets. A compact convex set \(A\) is contained in a compact convex set \(B\) whenever \(h_A(u)\le h_B(u)\) for every \(u\), by strict separation of any point of \(A\setminus B\). The support-function inequality therefore proves
\[
Z_\alpha\!\left(\sum_{i=1}^k\lambda_iX_i\right)
\subseteq\sum_{i=1}^k\lambda_iZ_\alpha(X_i),
\]
for the arbitrary given coupling.

## External sources

none
