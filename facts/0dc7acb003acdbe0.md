---
fact_id: 0dc7acb003acdbe0
kind: theorem
author: "research-agent"
assurance: LLM-verified
subgoal_id: oct3cf-optimized-convex-majorant-excess-on-ternary-roofs
depends_on: ["0bcc51d8cd216cf3","7f8bfa2ea34acc26"]
verifier_run: 1d938f9add6e4305
target_match: null
---

## Statement

For each integer \(m\ge2\), use the exact body and fiber table of accepted fact \(\texttt{7f8bfa2ea34acc26}\):

\[
\begin{aligned}
r_m(\mathbf x)&=1-\frac{3}{4m}\sum_{i=1}^m|x_i|\qquad(\mathbf x\in[-1,1]^m),\\
B_m&=\left\{(\mathbf x,\mathbf y)\in\mathbb R^m\times\mathbb R^m:
\mathbf x\in[-1,1]^m,\ |y_i|\le r_m(\mathbf x)/2\ (1\le i\le m)\right\},\\
u_{\mathbf x}&=u_s=\left(1-\frac{3s}{4m}\right)^m
\quad\left(\mathbf x\in\{-1,0,1\}^m,\ s=|\{i:x_i\ne0\}|\right),\\
W_B&=\sum_{\mathbf x\in\{-1,0,1\}^m}u_{\mathbf x}
=\sum_{s=0}^m\binom ms2^s u_s.
\end{aligned}
\]

Here \(u_{\mathbf x}\) denotes the actual fiber volume, and the table is zero outside \(\{-1,0,1\}^m\). The substitution into accepted fact \(\texttt{0bcc51d8cd216cf3}\) is \(C=B_m\), \(n=d=m\), \(D_+=\{-1,0,1\}^m\), \(w_{\mathbf x}=u_{\mathbf x}\), and \(W=W_B\). Thus \(\gamma_m=(m/(m+1))^m\), \(\theta_m=1-\gamma_m\), and its full convex-majorant excess is

\[
Q_\varphi=\sum_{\mathbf x\in\{-1,0,1\}^m}
\bigl(u_{\mathbf x}-\theta_m\varphi(\mathbf x)^m\bigr)_+,
\]

where \((t)_+=\max\{t,0\}\). For every convex \(\varphi:[-1,1]^m\to(0,\infty)\) satisfying \(\varphi(\mathbf x)^m\ge u_{\mathbf x}\) at every ternary lattice site, each fixed subset of \(\{1,\ldots,m\}\) is the set of nonzero coordinates of at most one site with positive excess. Consequently,

\[
0\le
\sup_{\substack{\varphi:[-1,1]^m\to(0,\infty)\ \mathrm{convex}\\
\varphi(\mathbf x)^m\ge u_{\mathbf x}\ (\mathbf x\in\{-1,0,1\}^m)}}
\frac{Q_\varphi}{W_B}
\le
\frac{\sum_{s=0}^m\binom ms u_s}{\sum_{s=0}^m\binom ms2^s u_s}
\le\left(\frac{28}{29}\right)^m
\longrightarrow0.
\]

No majorization hypothesis is imposed at noninteger points.

## Proof

The body, complete positive integer support, and actual fiber-volume formula are provided by accepted fact \(\texttt{7f8bfa2ea34acc26}\). The displayed substitution identifies the present \(Q_\varphi\) with exactly the full convex-majorant quantity in accepted fact \(\texttt{0bcc51d8cd216cf3}\), including its original continuous-dimension exponent and its coefficient \(\theta_m\). The admissible class is nonempty: the constant function \(\varphi=1\) is positive, convex, and majorizes every lattice root.

We first record a strict one-coordinate root gap. For \(m\ge2\), the binomial theorem gives

\[
\begin{aligned}
(1+1/m)^m&\ge2+\frac{m-1}{2m}\ge\frac94,
&\theta_m&\ge\frac59,\\
\left(1+\frac3{4m}\right)^m
&\ge1+\frac34+\frac{9(m-1)}{32m}\ge\frac{121}{64}.
\end{aligned}
\]

For \(1\le s\le m\), all quantities below are positive, and

\[
\begin{aligned}
\frac{u_{s-1}}{u_s}
&=\left(1+\frac3{4m-3s}\right)^m
\ge\left(1+\frac3{4m}\right)^m
\ge\frac{121}{64},\\
\theta_m u_{s-1}&\ge\frac{605}{576}u_s>u_s.
\end{aligned}
\]

Fix an admissible \(\varphi\). Suppose distinct sites \(\mathbf x,\mathbf x'\) have positive excess and have the same set of \(s\) nonzero coordinates. Necessarily \(s\ge1\). Let \(k\ge1\) be the number of coordinates where their signs differ. Their midpoint \(\mathbf z=(\mathbf x+\mathbf x')/2\) is a ternary lattice site with exactly \(s-k\) nonzero coordinates. Lattice-site majorization and positivity imply \(\varphi(\mathbf z)\ge u_{s-k}^{1/m}\). Positive excess at both endpoints implies \(\varphi(\mathbf x)<\theta_m^{-1/m}u_s^{1/m}\) and the same strict inequality for \(\mathbf x'\). Convexity at this midpoint therefore gives

\[
u_{s-1}^{1/m}
\le u_{s-k}^{1/m}
\le\varphi(\mathbf z)
\le\frac{\varphi(\mathbf x)+\varphi(\mathbf x')}{2}
<\theta_m^{-1/m}u_s^{1/m}.
\]

Raising to the original power \(m\) contradicts \(\theta_m u_{s-1}>u_s\). Hence each nonzero-coordinate set supports at most one positive-excess site. This argument compares every pair of sign patterns with the same support, not just adjacent patterns, so a checkerboard selection cannot evade it. The empty support consists only of \(\mathbf0\). Each excess summand is at most its original weight \(u_s\); there are \(\binom ms\) possible supports of size \(s\). Thus \(Q_\varphi\le\sum_{s=0}^m\binom ms u_s\), uniformly over all admissible convex functions.

It remains to compare this last sum with the full mass, without changing the original probabilities. Let \(X\) have exactly the distribution \(\mathbb P(X=\mathbf x)=u_{\mathbf x}/W_B\) on the ternary support, as in accepted fact \(\texttt{7f8bfa2ea34acc26}\). Define \(f(0)=1\) and \(f(-1)=f(1)=1/2\). Direct summation over sign patterns yields

\[
\mathbb E\prod_{i=1}^m f(X_i)
=\frac{\sum_{s=0}^m\binom ms u_s}{W_B}.
\]

If all coordinates other than \(i\) are fixed, with \(s\) of them nonzero, then \(0\le s\le m-1\) and

\[
\begin{aligned}
\frac{u_{s+1}}{u_s}
&=\left(1-\frac3{4m-3s}\right)^m
\ge\left(\frac{m}{m+3}\right)^m
>e^{-3}>\frac1{27},\\
\mathbb E\bigl[f(X_i)\mid X_j\ (j\ne i)\bigr]
&=\frac{u_s+u_{s+1}}{u_s+2u_{s+1}}
<\frac{28}{29}.
\end{aligned}
\]

For completeness, \(\log(1+t)<t\) for \(t>0\) follows by integrating \((1+t)^{-1}<1\), proving the first strict inequality. Also \(e=2+\sum_{j\ge2}1/j!<2+\sum_{j\ge2}2^{1-j}=3\), proving the second. The conditional expectation bound follows because \((1+t)/(1+2t)\) decreases for \(t>0\) and equals \(28/29\) at \(t=1/27\). Every conditioning event here has positive probability since every ternary weight is positive.

For any nonempty coordinate subset \(J\) and any \(i\in J\), the product \(\prod_{j\in J\setminus\{i\}}f(X_j)\) is nonnegative and depends only on coordinates other than \(i\). Conditioning on all those coordinates and using the preceding bound gives

\[
\mathbb E\prod_{j\in J}f(X_j)
\le\frac{28}{29}\,
\mathbb E\prod_{j\in J\setminus\{i\}}f(X_j).
\]

Iterating to the empty product proves \(\mathbb E\prod_{i=1}^m f(X_i)\le(28/29)^m\). This proves the mass comparison and the uniform supremum bound. Every use of majorization in the proof was at an actual ternary lattice site, including the midpoint \(\mathbf z\); convexity alone supplied the intervening inequality. The normalized upper bound tends to zero, whereas accepted fact \(\texttt{0bcc51d8cd216cf3}\) supplies only a depth lower bound from this excess. No conclusion that the actual depth tends to zero follows.

## External sources

None beyond the two declared accepted predecessors. All new midpoint restrictions and the full-convex uniform estimate are proved above.
