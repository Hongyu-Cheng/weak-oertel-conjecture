---
fact_id: fef7af6073c73afd
kind: lemma
author: "research-agent"
assurance: LLM-verified
subgoal_id: iy-parity-reduction
depends_on: []
verifier_run: 753b0cd1f3b245ef
target_match: null
---

## Statement

Let \(n,d\in\mathbb Z_{>0}\), let \(A\subseteq\mathbb R^{n+d}\) be compact and convex, and put
\[
A_x:=\{y\in\mathbb R^d:(x,y)\in A\},\qquad
f(x):=\operatorname{vol}_d(A_x)\quad(x\in\mathbb R^n).
\]
Fix \(\epsilon\in\{0,1\}^n\), and define
\[
F(u):=f(\epsilon+2u),\quad
E:=\operatorname{supp}F=\{u\in\mathbb Z^n:F(u)>0\},\quad
M_\epsilon:=\sum_{u\in\mathbb Z^n}F(u),\quad
T:=\sum_{z\in\mathbb Z^n}f(z),\quad
m:=n+d.
\]

The Iglesias--Yepes \(p\)-sum is
\[
S_p(a,b):=(a^p+b^p)^{1/p}\qquad(a,b>0,\ p\in\mathbb R\setminus\{0\}),
\]
with \(S_\infty(a,b)=\max\{a,b\}\), \(S_{-\infty}(a,b)=\min\{a,b\}\), and, importantly,
\[
S_p(a,b):=0\qquad\text{if }ab=0.
\]

Here is the exact reduction used below. For a finite weighted set \((\Lambda,w)\), with \(\Lambda\subseteq\mathbb Z^k\), write
\[
\Lambda(a):=\{x\in\mathbb Z^{k-1}:(x,a)\in\Lambda\}.
\]
For nonempty \(\Lambda\), let
\[
\mu(\Lambda,w):=
\max\mathop{\rm argmax}_{a\in\pi_k(\Lambda)}
\sum_{x\in\Lambda(a)}w(x,a);
\]
thus the largest maximizing last coordinate is chosen. Define
\[
\rho_k^w(\Lambda):=
\begin{cases}
\Lambda\setminus\{\mu(\Lambda,w)\},&k=1,\\
\Lambda\setminus\bigl(\Lambda(\mu(\Lambda,w))\times\{\mu(\Lambda,w)\}\bigr),&k>1,
\end{cases}
\qquad
\rho_k^w(\varnothing):=\varnothing.
\]
Starting with \(E^-_0:=E\), for \(1\leq k<n\) define
\[
E^-_k:=
\bigcup_{\substack{t\in\mathbb Z^{n-k}\\
\Lambda_{k,t}\neq\varnothing}}
\left(\rho_k^{F_{k,t}}(\Lambda_{k,t})\times\{t\}\right),
\]
where
\[
\Lambda_{k,t}:=\{x\in\mathbb Z^k:(x,t)\in E^-_{k-1}\},
\qquad
F_{k,t}(x):=F(x,t).
\]
Then the source reduction is
\[
r_F(E):=\rho_n^F(E^-_{n-1}).
\]
Equivalently, for a weighted \(\Lambda\subseteq\mathbb Z^k\), first form
\(r_{w_a}(\Lambda(a))\) recursively in every last-coordinate slice, where
\(w_a(x):=w(x,a)\), and let
\[
I:=\{a\in\pi_k(\Lambda):r_{w_a}(\Lambda(a))\neq\varnothing\}.
\]
If \(I=\varnothing\), then \(r_w(\Lambda)=\varnothing\). Otherwise, if
\[
\mu_*:=
\max\mathop{\rm argmax}_{a\in I}
\sum_{x\in r_{w_a}(\Lambda(a))}w(x,a),
\]
then
\[
r_w(\Lambda)=
\bigcup_{a\in\pi_k(\Lambda)\setminus\{\mu_*\}}
\left(r_{w_a}(\Lambda(a))\times\{a\}\right),
\tag{R}
\]
with the one-dimensional base case \(r_w(\Lambda)=
\Lambda\setminus\{\mu(\Lambda,w)\}\). Thus the last-coordinate slice having
maximum surviving mass is removed, with the same largest-coordinate tie rule.

With this definition,
\[
2^dT\geq
\left(
\left[\sum_{u\in r_F(E)}F(u)\right]^{1/m}
+M_\epsilon^{1/m}
\right)^m.
\tag{1}
\]
Consequently, writing \(R:=\sum_{u\in r_F(E)}F(u)\),
\[
R\leq\left((2^dT)^{1/m}-M_\epsilon^{1/m}\right)^m.
\tag{2}
\]

The exact deletion certificate is as follows. Put \(E^-_n:=r_F(E)\). For each \(1\leq k\leq n\), and for each nonempty current fiber \(\Lambda_{k,t}\) above (with the tail \(t\) empty when \(k=n\)), set
\[
\mu_k(t):=\mu(\Lambda_{k,t},F_{k,t})
\]
and
\[
D_{k,t}:=
\{u\in E^-_{k-1}:u_{k+1:n}=t,\ u_k=\mu_k(t)\}.
\]
Then
\[
E=r_F(E)\,\dot\cup\!
\mathop{\dot\bigcup}_{k=1}^n\
\mathop{\dot\bigcup}_{t}D_{k,t},
\qquad
M_\epsilon-R=
\sum_{k=1}^n\sum_t\sum_{u\in D_{k,t}}F(u).
\tag{3}
\]
For every \(k,t\), \(D_{k,t}\) is the maximum-\(F\)-mass \(u_k\)-section of the current survivor in that tail:
\[
\sum_{u\in D_{k,t}}F(u)
=
\max_{a\in\pi_k(\Lambda_{k,t})}
\sum_{\substack{u\in E^-_{k-1}\\u_{k+1:n}=t,\ u_k=a}}F(u).
\tag{4}
\]
It lies in the coordinate-affine flat
\[
L_{k,t}:=\{u\in\mathbb R^n:u_k=\mu_k(t),\ u_{k+1:n}=t\},
\tag{5}
\]
of dimension \(k-1\). Here
\(\Lambda_{n,\varnothing}:=E^-_{n-1}\) and
\(F_{n,\varnothing}:=F|_{E^-_{n-1}}\). If
\(c_k:=\mu_k(t)\) and \(c_j:=t_j\) for \(j>k\), then under
\(z=\epsilon+2u\), \(L_{k,t}\) becomes the affine coordinate flat obtained by fixing
\[
z_j=\epsilon_j+2c_j\qquad(k\leq j\leq n)
\]
inside the chosen parity class. The current-fiber flats form the standard coordinate flag tree, and each branch is a nested coordinate flag. Equations (3)--(5), and only these equations, are the legitimate single-color affine-flag bookkeeping: the selected flats and tie choices depend on \(F\), the discarded blocks need not all lie in one nested chain, and (4) concerns current-survivor mass rather than the original mass of a whole affine flat.

## Proof

The projection of compact \(A\) onto \(\mathbb R^n\) is compact. Hence only finitely many \(z\in\mathbb Z^n\) have nonempty \(A_z\), so \(f\) and \(F\) have finite support and all displayed sums are finite. Also \(M_\epsilon\leq T\).

If \(M_\epsilon=0\), then \(E=r_F(E)=\varnothing\), and (1) is \(2^dT\geq0\). Suppose \(M_\epsilon>0\), and first suppose
\[
R:=\sum_{u\in r_F(E)}F(u)>0.
\]
Define nonnegative functions on \(\mathbb R^n\) by
\[
G(x):=f(\epsilon+2x),
\qquad
h(s):=2^d f(\epsilon+s).
\]
Only the values \(G|_E=F|_E\) and \(h|_{E+E}\) will be used.

Fix \(u,v\in E\). Convexity of \(A\) gives
\[
\frac12A_{\epsilon+2u}+\frac12A_{\epsilon+2v}
\subseteq A_{\epsilon+u+v}.
\]
The \(d\)-dimensional Brunn--Minkowski inequality therefore gives
\[
f(\epsilon+u+v)^{1/d}
\geq
\frac12F(u)^{1/d}+\frac12F(v)^{1/d}.
\]
Thus, for \(p=1/d\),
\[
h(u+v)^{1/d}
=2f(\epsilon+u+v)^{1/d}
\geq F(u)^{1/d}+F(v)^{1/d},
\]
or
\[
h(u+v)\geq S_{1/d}(F(u),F(v)).
\tag{6}
\]
There is no hidden zero-input issue in (6), since \(u,v\in E\) imply \(F(u)F(v)>0\).

Apply Iglesias--Yepes Theorem 2.1 in lattice dimension \(n\) with the two finite sets both equal to \(E\), the two input functions both equal to \(G\), and \(p=1/d\). Its output exponent is
\[
q=\frac{p}{np+1}
=\frac{1/d}{n/d+1}
=\frac1{n+d}
=\frac1m.
\]
The theorem and \(R,M_\epsilon>0\) yield
\[
\sum_{s\in E+E}h(s)
\geq
S_{1/m}(R,M_\epsilon)
=\left(R^{1/m}+M_\epsilon^{1/m}\right)^m.
\tag{7}
\]
The theorem sums \(h\) only over the sumset \(E+E\). Since \(s\mapsto\epsilon+s\) injects \(E+E\) into \(\mathbb Z^n\), nonnegativity gives the required comparison
\[
\sum_{s\in E+E}h(s)
=2^d\sum_{s\in E+E}f(\epsilon+s)
\leq2^d\sum_{z\in\mathbb Z^n}f(z)
=2^dT.
\tag{8}
\]
Combining (7) and (8) proves (1) when \(R>0\).

If \(M_\epsilon>0\) but \(R=0\), the source convention gives
\(S_{1/m}(R,M_\epsilon)=0\), not \(M_\epsilon\), so (1) does not follow by replacing the source \(q\)-sum with its positive-input formula. Instead, it follows directly:
\[
2^dT\geq T\geq M_\epsilon
=\left(0^{1/m}+M_\epsilon^{1/m}\right)^m.
\]
This also identifies exactly why the zero case must be separated. Hence (1) holds in all cases. Taking \(m\)-th roots in (1), and using \(M_\epsilon\leq T\), proves (2).

It remains to verify the claimed deletion bookkeeping. By construction,
\[
E^-_0\supseteq E^-_1\supseteq\cdots\supseteq E^-_n=r_F(E).
\]
At stage \(k\), the operation \(\rho_k\) removes, in every nonempty tail fiber \(t\), exactly the section \(D_{k,t}\). The definition of \(\mu\) proves (4), including the source's largest-coordinate tie rule, and the fixed-coordinate description proves (5). Therefore
\[
E^-_{k-1}\setminus E^-_k=\mathop{\dot\bigcup}_tD_{k,t}.
\]
Telescoping these disjoint differences proves the set partition and mass identity (3). The flats in (5) are nodes of the standard coordinate flag tree; mapping by \(z=\epsilon+2u\) gives the asserted parity-class affine flats. Nothing in this construction identifies the choices for two different weights, makes all selected flats a single chain, or turns the current-survivor maximum in (4) into a lower bound for the original mass of one flat. This proves the precise certificate and its stated limitations.

## External sources

David Iglesias and Jesús Yepes Nicolás, “On discrete Borell--Brascamp--Lieb inequalities,” Revista Matemática Iberoamericana 36 (2020), no. 3, 711--722, Theorem 2.1 and equations (2.1)--(2.4). Primary author-hosted paper: https://webs.um.es/jesus.yepes/publicaciones_files/paper_BBL_final_version.pdf . DOI: https://doi.org/10.4171/RMI/1145 .

The exact source theorem is: if \(\mathcal A,\mathcal B\subseteq\mathbb Z^n\) are finite, \(-1/n\leq p\leq\infty\) with \(p\neq0\), and nonnegative \(f_0,g_0,h_0:\mathbb R^n\to\mathbb R_{\geq0}\) satisfy
\[
h_0(x+y)\geq S_p(f_0(x),g_0(y))
\qquad(x\in\mathcal A,\ y\in\mathcal B),
\]
then
\[
\sum_{z\in\mathcal A+\mathcal B}h_0(z)
\geq
S_{p/(np+1)}
\left(
\sum_{x\in r_{f_0}(\mathcal A)}f_0(x),
\sum_{y\in\mathcal B}g_0(y)
\right).
\]
The source defines \(S_p(a,b)=0\) when \(ab=0\), and defines \(r_{f_0}\) by the maximum-section operations and largest-coordinate tie rule reproduced in the statement above. The applicability substitutions are
\[
\mathcal A=\mathcal B=E,\quad
f_0=g_0=G,\quad
h_0=h,\quad
p=1/d,\quad
\frac{p}{np+1}=\frac1{n+d}.
\]
Finite support follows from compactness, the pointwise hypothesis is (6), the source sumset is handled in (8), and the source zero convention is handled separately in the \(R=0\) case.
