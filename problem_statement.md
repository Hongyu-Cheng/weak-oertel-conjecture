# Weak Oertel conjecture for mixed-integer volume

Let \(n,d\in\mathbb{Z}_{>0}\), let \(C\subset\mathbb{R}^{n+d}\) be a convex
body, and define

\[
\Lambda:=\mathbb{Z}^{n}\times\mathbb{R}^{d},
\qquad
S:=C\cap\Lambda.
\]

Assume \(S\neq\varnothing\). For every measurable \(A\subseteq\Lambda\), its
mixed-integer volume is the \(d\)-dimensional Hausdorff measure
\(\mathcal{H}_{d}(A)\), equivalently

\[
\mathcal{H}_{d}(A)
=
\sum_{\mathbf z\in\mathbb{Z}^{n}}
\mathcal{H}_{d}\!\left(
A\cap\bigl(\{\mathbf z\}\times\mathbb{R}^{d}\bigr)
\right).
\]

For \(\mathbf y\in S\), define its halfspace depth by

\[
h_S(\mathbf y)
:=
\inf\left\{
\mathcal{H}_{d}(S\cap H):
H\subseteq\mathbb{R}^{n+d}
\text{ is a closed halfspace and }\mathbf y\in H
\right\}.
\]

## Problem

Prove or disprove the following statement:

There exists an absolute constant \(c_0\in(0,1/e)\) such that, for every
\(n,d\in\mathbb{Z}_{>0}\) and every convex body
\(C\subset\mathbb{R}^{n+d}\) with \(S\neq\varnothing\), there exists
\(\mathbf y^\star\in S\) satisfying

\[
h_S(\mathbf y^\star)
\ge
\frac{c_0}{2^n}\,\mathcal{H}_{d}(S).
\]

Equivalently, every closed halfspace \(H\subseteq\mathbb{R}^{n+d}\) containing
\(\mathbf y^\star\) must satisfy
\(\mathcal{H}_{d}(S\cap H)\ge c_0 2^{-n}\mathcal{H}_{d}(S)\).

The quantifier order is

\[
\exists\,c_0\in(0,1/e)\;
\forall\,n,d\;
\forall\,C\;
\exists\,\mathbf y^\star\in S\;
\forall\,H.
\]

In particular, \(c_0\) is independent of \(n\), \(d\), and \(C\). When
\(\mathcal{H}_{d}(S)=0\), the inequality is automatic for any
\(\mathbf y^\star\in S\); the substantive case is
\(\mathcal{H}_{d}(S)>0\).
