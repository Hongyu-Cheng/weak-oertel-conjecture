---
fact_id: 5cebfce93303cec1
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: oct3er-divisible-anchor-arbitrary-score-depth
depends_on: ["ac02a0ffd389f816"]
verifier_run: 3215ce691eba4bf7
target_match: null
---

## Statement

Let \(n\ge1\) be an integer, let \(a_i>0\) and \(L\ge0\) be real, and let \(\theta_i\in\mathbb R\) for \(1\le i\le n\). Define the complete original support and its original probabilities by
\[
D=\{z\in\mathbb Z_{\ge0}^n:\sum_{i=1}^n a_i z_i\le L\},\qquad
Z=\sum_{z\in D}e^{\theta\cdot z},\qquad
p_z=e^{\theta\cdot z}/Z.
\]
For \(j\in D\), define \(\tau_p(j)\) as the infimum of \(p(H\cap D)\) over all closed halfspaces \(H\subseteq\mathbb R^n\) containing \(j\), and define \(M_3(p)=\sum_{j\in D}p_j\tau_p(j)^3\). These are exactly the original-probability depth and moment conventions of accepted fact `ac02a0ffd389f816`.

Assume either that every \(\theta_i\le0\), or that there is an index \(h\in\{1,\ldots,n\}\) satisfying
\[
\theta_h>0,\qquad
\frac{\theta_h}{a_h}\ge\frac{\theta_i}{a_i}\quad(1\le i\le n),\qquad
\frac{a_i}{a_h}\in\mathbb Z_{>0}\quad(i\ne h),\qquad
Q:=\frac{L}{a_h}\in\mathbb Z_{\ge0}.
\]
Thus, in particular, the result applies to the registered integer-resource inputs whose positive maximum score-per-cost anchor divides all costs and the capacity.

Use exactly the absolute constants of accepted fact `ac02a0ffd389f816`, with natural logarithms:
\[
\begin{aligned}
\alpha&=(8/27)^{3/2},&\gamma&=2048,&
b&=20+\log(48\gamma^4),\\
c&=e^{-(20+b)}/128,&B&=\gamma b+144,&
\delta&=\log(8\alpha)>0,\\
N&=\left\lceil\max\{1,(B/\delta)^2\}\right\rceil,&
\kappa_0&=\min\{c,1/(64\cdot8^N)\}>0.
\end{aligned}
\]
Then the full original law satisfies both
\[
M_3(p)\ge c\,e^{-B\sqrt n}\alpha^n,
\qquad
M_3(p)\ge\kappa_0\,8^{-n}.
\tag{1}
\]
Every boundary atom remains included. No conditioning or selection changes the support, the original normalizer, or the original root probabilities in (1).

In particular, for every integer \(n\ge1\), every integer \(L\ge0\), and every finite real vector \(\theta\in\mathbb R^n\), the original log-affine law on the unit-cost simplex \(D=\{z\in\mathbb Z_{\ge0}^n:\sum_i z_i\le L\}\) satisfies (1).

## Proof

The original support is finite because \(0\le z_i\le L/a_i\), and it contains zero. Thus \(0<Z<\infty\). If every \(\theta_i\le0\), apply accepted fact `ac02a0ffd389f816` with its \(n,a_i,\theta_i,D,Z,p,\tau_p,M_3\) identical to those here and its capacity \(R\) aliased to the present \(L\). Its two conclusions are exactly (1), including \(L=0\).

Assume the stated anchor exists. Set \(I=\{1,\ldots,n\}\setminus\{h\}\), always ordered increasingly, and set \(r=(r_i)_{i\in I}\), with \(r_i=a_i/a_h\in\mathbb Z_{>0}\). Use an \(n\)-coordinate vector \(y=((y_i)_{i\in I},s)\), with the slack coordinate last, and define the affine map on the entire ambient space by
\[
T_h(z)=((z_i)_{i\in I},s),\qquad
s=Q-z_h-\sum_{i\in I}r_i z_i.
\tag{2}
\]
Its inverse on the entire ambient space is
\[
z_i=y_i\quad(i\in I),\qquad
z_h=Q-\sum_{i\in I}r_i y_i-s.
\tag{3}
\]
In input order \(((z_i)_{i\in I},z_h)\), the linear part of (2) is
\[
\begin{pmatrix}I_{n-1}&0\\-r^{\mathsf T}&-1\end{pmatrix},
\tag{4}
\]
with determinant \(-1\). Returning to the original input order changes this determinant only by a sign. Its coefficients and the coefficients of its inverse are integers, and its translation has the sole possibly nonzero coordinate \(Q\), also an integer. Hence \(T_h\) is an affine unimodular bijection of \(\mathbb Z^n\). For \(n=1\), the empty-coordinate convention makes (2) the map \(z_h\mapsto Q-z_h\), and (4) the matrix \((-1)\), so the same conclusion holds.

Define the complete transformed support by
\[
\widetilde D=\left\{((y_i)_{i\in I},s)\in\mathbb Z_{\ge0}^n:
\sum_{i\in I}r_i y_i+s\le Q\right\}.
\tag{5}
\]
If \(z\in D\), division of its original weak resource inequality by \(a_h>0\) gives \(z_h+\sum_{i\in I}r_i z_i\le Q\). Consequently the slack in (2) is a nonnegative integer, and \(\sum_{i\in I}r_i y_i+s=Q-z_h\le Q\). Thus \(T_h(z)\in\widetilde D\). Conversely, if \(y\in\widetilde D\), formula (3) gives a nonnegative integer \(z_h\), keeps every other coordinate nonnegative and integral, and gives
\[
\sum_{i=1}^n a_i z_i=a_h(Q-s)\le a_h Q=L.
\tag{6}
\]
Thus \(T_h^{-1}(y)\in D\). The global inverse formulas prove the exact bijection \(T_h(D)=\widetilde D\).

The same argument with real nonnegative coordinates identifies the two closed resource polytopes. In particular, the original saturated resource face \(\sum_i a_i z_i=L\) maps to \(s=0\), the original anchor face \(z_h=0\) maps to \(\sum_{i\in I}r_i y_i+s=Q\), and every other coordinate face \(z_i=0\) maps to \(y_i=0\). All intersections of these faces are included because every inequality used is weak. No boundary is discarded, even if \(Q=0\) or some coordinates are forced to zero on the lattice support. When \(Q=0\), both supports are the singleton zero and the same map remains valid.

Define the transformed resource and score vectors, in the same coordinate order as \(y\), by
\[
\widetilde a=((r_i)_{i\in I},1),\qquad
\widetilde\theta=((\theta_i-\theta_h r_i)_{i\in I},-\theta_h).
\tag{7}
\]
All transformed resource coefficients are positive. The maximal score-per-cost condition gives \(\theta_i\le\theta_h a_i/a_h=\theta_h r_i\) for every \(i\in I\), so every coordinate of \(\widetilde\theta\) is nonpositive; ties are permitted. The slack score is strictly negative. Substitution of (3) gives the exact score identity
\[
\theta\cdot z
=\theta_h Q+\sum_{i\in I}(\theta_i-\theta_h r_i)y_i-\theta_h s
=\theta_h Q+\widetilde\theta\cdot T_h(z).
\tag{8}
\]
Let \(\widetilde Z=\sum_{y\in\widetilde D}e^{\widetilde\theta\cdot y}\) and \(\widetilde p_y=e^{\widetilde\theta\cdot y}/\widetilde Z\). Summing (8) over the exact support bijection, and then cancelling its constant term, gives
\[
Z=e^{\theta_h Q}\widetilde Z,
\qquad
p_z=\frac{e^{\theta_h Q}e^{\widetilde\theta\cdot T_h(z)}}
{e^{\theta_h Q}\widetilde Z}
=\widetilde p_{T_h(z)}.
\tag{9}
\]
Thus \(\widetilde p\) is the exact pushforward of the full original law. Formula (9) retains the original normalizer \(Z\) and every original atom probability; the auxiliary decreasing normalizer is related to it by an equality, not an estimate.

Write \(T_h(z)=A_h z+t_h\) for its invertible linear part and translation. If a proper closed halfspace has form \(H=\{z:u\cdot z\ge v\}\), where \(u\ne0\), then its affine image is exactly
\[
T_h(H)=\{y:(A_h^{-\mathsf T}u)\cdot y
\ge v+(A_h^{-\mathsf T}u)\cdot t_h\}.
\tag{10}
\]
The image normal is nonzero by invertibility. Thus (10) is a proper closed halfspace, with every equality point retained. Conversely the inverse map sends every proper closed halfspace in the transformed space to a proper closed halfspace in the original space. These two maps biject the containing halfspaces for \(j\) and \(T_h(j)\). If the halfspace convention also allows the whole space, it maps to itself and has mass one, so it does not affect this conclusion.

For each such halfspace, the support bijection and (9) give
\(p(H\cap D)=\widetilde p(T_h(H)\cap\widetilde D)\). Taking the infimum over the bijected containing closed halfspaces proves the exact depth identity \(\tau_p(j)=\tau_{\widetilde p}(T_h(j))\) for every original root \(j\in D\). Summing with the same original probabilities gives
\[
M_3(p)
=\sum_{j\in D}\widetilde p_{T_h(j)}
\tau_{\widetilde p}(T_h(j))^3
=\sum_{y\in\widetilde D}\widetilde p_y\tau_{\widetilde p}(y)^3
=M_3(\widetilde p).
\tag{11}
\]

Apply accepted fact `ac02a0ffd389f816` with its dimension \(n\) unchanged, its resource vector \(a\) aliased to \(\widetilde a\), its capacity \(R\) aliased to \(Q\), its score vector \(\theta\) aliased to \(\widetilde\theta\), its support \(D\) aliased to \(\widetilde D\), and its \(Z,p,\tau_p,M_3\) aliased respectively to \(\widetilde Z,\widetilde p,\tau_{\widetilde p},M_3(\widetilde p)\). Equations (5) and (7) check every hypothesis: this is a complete nonnegative integer one-resource support with positive resource coefficients, nonnegative capacity, and nonpositive finite scores. Its constants \(\alpha,\gamma,b,c,B,\delta,N,\kappa_0\) are exactly those stated above. It supplies both bounds in (1) for \(M_3(\widetilde p)\); equality (11) proves both for the full original \(M_3(p)\), without dimension, residue, probability, or volume loss.

Finally, for unit costs and integer \(L\ge0\), if all scores are nonpositive the first branch applies. Otherwise choose any index \(h\) attaining \(\max_i\theta_i>0\). It has maximal score-per-cost, every ratio \(a_i/a_h=1\), and \(Q=L\) is a nonnegative integer. The anchor branch therefore proves (1) for every arbitrary finite real score vector on the stated unit-cost simplex, in every \(n\ge1\).

## External sources

none
