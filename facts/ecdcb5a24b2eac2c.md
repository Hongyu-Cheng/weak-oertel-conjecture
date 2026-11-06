---
fact_id: ecdcb5a24b2eac2c
kind: lemma
author: "research-agent"
assurance: LLM-verified
subgoal_id: balanced-convolution-grunbaum
depends_on: []
verifier_run: dca9034db74a4b7a
target_match: null
---

## Statement

Let \(n,d\in\mathbb Z_{>0}\), let \(C\subseteq\mathbb R^{n+d}\) be a convex body, and for \(z\in\mathbb Z^n\) define
\[
C_z:=\{x\in\mathbb R^d:(z,x)\in C\},\qquad
w_z:=\operatorname{vol}_d(C_z).
\]
Assume
\[
W:=\sum_{z\in\mathbb Z^n}w_z>0,
\qquad
D:=\{z\in\mathbb Z^n:w_z>0\},
\qquad
\pi_z:=\frac{w_z}{W}\quad(z\in D),
\]
and let \(c_z\) be the centroid of \(C_z\) for \(z\in D\).

Suppose that coefficients \((\eta_z)_{z\in D}\) satisfy
\[
0\leq\eta_z\leq\pi_z,\qquad
\sigma:=\sum_{z\in D}\eta_z>0,\qquad
\sum_{z\in D}\eta_z(z-z_0)=0
\]
for some \(z_0\in\mathbb Z^n\). Put
\[
I:=\{z\in D:\eta_z>0\},\qquad
q_z:=\frac{\eta_z}{\sigma}\quad(z\in I),
\]
\[
x_0:=\sum_{z\in I}q_zc_z,\qquad
p:=(z_0,x_0).
\]
Then \(p\in C\cap(\mathbb Z^n\times\mathbb R^d)\).

Let \(H\) be any closed halfspace whose boundary contains \(p\). For each \(z\in D\), define its captured fiber fraction by
\[
r_z(H):=
\frac{\operatorname{vol}_d\{x\in C_z:(z,x)\in H\}}{w_z}.
\]
Then
\[
1-\prod_{z\in I}\bigl(1-r_z(H)\bigr)\geq\frac1e,
\qquad
\sum_{z\in I}r_z(H)\geq\frac1e.
\]
Consequently, the normalized mixed mass of \(H\) satisfies
\[
\frac1W\sum_{z\in D}
\operatorname{vol}_d\{x\in C_z:(z,x)\in H\}
=\sum_{z\in D}\pi_zr_z(H)
\geq\frac1e\min_{z\in I}\eta_z.
\]
The same normalized-mass bound holds for every closed halfspace containing \(p\), even if its boundary does not contain \(p\).

## Proof

The set \(D\) is finite because the projection of the compact set \(C\) onto \(\mathbb R^n\) is bounded. Since \(\sigma>0\), the active set \(I\) is nonempty, and the numbers \((q_z)_{z\in I}\) are positive and sum to one. The balance condition gives
\[
\sum_{z\in I}q_z z=z_0.
\]
For every \(z\in D\), the positive-volume fiber \(C_z\) is a compact convex subset of \(\mathbb R^d\), and its centroid \(c_z\) belongs to \(C_z\). Hence \((z,c_z)\in C\). Therefore
\[
p
=\sum_{z\in I}q_z(z,c_z)\in C
\]
by convexity. Its first coordinate is the integer point \(z_0\), so
\[
p\in C\cap(\mathbb Z^n\times\mathbb R^d).
\]
This also shows explicitly that fibers of zero \(d\)-volume and coefficients equal to zero play no role in the selected barycenter.

Write the halfspace as
\[
H=
\left\{
(z,x):
a^\top(z-z_0)+b^\top(x-x_0)\geq0
\right\}
\]
for some \((a,b)\in\mathbb R^n\times\mathbb R^d\) with \((a,b)\neq(0,0)\). For every \(z\in I\), independently sample
\[
X_z\sim\operatorname{Unif}(C_z)
\]
and set
\[
Y:=\sum_{z\in I}q_zX_z.
\]
The density of \(X_z\) is \(w_z^{-1}\mathbf 1_{C_z}\), which is log-concave because \(C_z\) is convex. Since \(q_z>0\), the density of \(q_zX_z\) is also log-concave. A finite convolution of log-concave densities is log-concave, so \(Y\) has a log-concave probability density on \(\mathbb R^d\). Moreover,
\[
\mathbb EY
=\sum_{z\in I}q_z\mathbb EX_z
=\sum_{z\in I}q_zc_z
=x_0.
\]

First suppose \(b\neq0\). The log-concave Grünbaum inequality applied to the halfspace
\[
\{y\in\mathbb R^d:b^\top(y-x_0)\geq0\}
\]
through the centroid of \(Y\) yields
\[
\mathbb P\bigl(b^\top(Y-x_0)\geq0\bigr)\geq\frac1e.
\]
For \(z\in I\), let
\[
E_z:=
\left\{
a^\top(z-z_0)+b^\top(X_z-x_0)\geq0
\right\}.
\]
The balance condition implies
\[
\begin{aligned}
b^\top(Y-x_0)
&=\sum_{z\in I}q_zb^\top(X_z-x_0)\\
&=\sum_{z\in I}q_z
\left[
a^\top(z-z_0)+b^\top(X_z-x_0)
\right].
\end{aligned}
\]
If the left side is nonnegative, then at least one bracket on the right is nonnegative, because every \(q_z\) is positive. Thus
\[
\{b^\top(Y-x_0)\geq0\}
\subseteq
\bigcup_{z\in I}E_z.
\]
Also,
\[
\mathbb P(E_z)=r_z(H).
\]
The variables \(X_z\), and hence the events \(E_z\), are independent. It follows that
\[
\frac1e
\leq
\mathbb P\left(\bigcup_{z\in I}E_z\right)
=
1-\prod_{z\in I}\bigl(1-r_z(H)\bigr).
\]

Now suppose \(b=0\). Then \(a\neq0\), and
\[
\sum_{z\in I}q_z a^\top(z-z_0)=0.
\]
Consequently, there is at least one \(z\in I\) with \(a^\top(z-z_0)\geq0\). For this \(z\), the whole fiber \(\{z\}\times C_z\) lies in \(H\), so \(r_z(H)=1\). Hence in this case
\[
1-\prod_{z\in I}\bigl(1-r_z(H)\bigr)=1.
\]
This proves the product inequality for both nonvertical and vertical halfspaces.

For arbitrary numbers \(r_z\in[0,1]\), the union bound for independent events of probabilities \(r_z\) gives
\[
1-\prod_{z\in I}(1-r_z)\leq\sum_{z\in I}r_z.
\]
Therefore
\[
\sum_{z\in I}r_z(H)\geq\frac1e.
\]
Finally, using \(0<\eta_z\leq\pi_z\) on \(I\) and nonnegativity outside \(I\),
\[
\begin{aligned}
\sum_{z\in D}\pi_zr_z(H)
&\geq\sum_{z\in I}\eta_zr_z(H)\\
&\geq
\left(\min_{z\in I}\eta_z\right)
\sum_{z\in I}r_z(H)\\
&\geq\frac1e\min_{z\in I}\eta_z.
\end{aligned}
\]

If a closed halfspace \(H\) contains \(p\) but its boundary does not contain \(p\), translate its boundary parallel toward \(p\) until it passes through \(p\). The resulting closed halfspace \(H'\) contains \(p\) and satisfies \(H'\subseteq H\). Applying the proved estimate to \(H'\) and using monotonicity of mixed mass proves the final assertion.

## External sources

László Lovász and Santosh Vempala, “The Geometry of Logconcave Functions and Sampling Algorithms,” Random Structures & Algorithms 30 (2007), 307–358, https://doi.org/10.1002/rsa.20135, author-hosted primary PDF: https://faculty.cc.gatech.edu/~vempala/papers/logcon.pdf. Theorem 5.1 states that the convolution of two log-concave functions is log-concave; iteration applies because the active set \(I\) is finite and every scaled uniform density above is log-concave. Lemma 5.12 states: if \(f:\mathbb R^d\to\mathbb R_+\) is a log-concave probability density and a halfspace contains its centroid, then its \(f\)-mass is at least \(1/e\). The law of \(Y\) is precisely such a probability density, its centroid is \(x_0\), and the halfspace \(\{y:b^\top(y-x_0)\geq0\}\) contains that centroid, so all hypotheses are satisfied.
