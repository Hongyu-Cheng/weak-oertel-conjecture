# Why the current n=52 support cannot give a small-dimensional 1/e example

This obstruction applies to **every choice of convex fibers on the same
integer support**, not merely the particular rational parameters.

Let a mixed-integer convex body have F positive-volume integer fibers of
common continuous dimension d, total volume W, and largest fiber volume M.
The ordinary centroid of a largest fiber belongs to the actual mixed-integer
set. Every ambient containing halfspace retains at least Gamma_d M from
that fiber, where Gamma_d=(d/(d+1))^d. Since M/W>=1/F,

\[
 D(C):=\sup_{\mathbf y}\operatorname{depth}(\mathbf y)
 \ge\Gamma_d\frac{M}{W}\ge\frac{\Gamma_d}{F}.
\]

Consequently a strict violation of 1/(e2^n) requires
\(F/2^n>e\Gamma_d\). The exact identity

\[
 \log(e\Gamma_d)=\int_0^1\frac{t}{d+t}\,dt>\frac1{2(d+1)}
\]

and exp(x)>1+x imply
\(e\Gamma_d>1+1/[2(d+1)]\). Thus if F<=2^n+L, a necessary condition is

\[
 d+1>\frac{2^{n-1}}{L}.
\]

For the current support, n=52 and
L=4(2^13-1)=32764. Therefore

\[
 d+1>\frac{2^{51}}{32764}
 =\frac{562949953421312}{8191}
 =68727866368+\frac{1024}{8191},
 \qquad d\ge68\,727\,866\,368.
\]

In particular d<100 is impossible with this support, even if every fiber
shape and every volume parameter is redesigned. This does not rule out
different supports or a low-dimensional counterexample to the sharp
Gamma_d/2^n bound. It also does not prove any unrestricted low-dimensional
Oertel theorem.

The elementary largest-fiber argument is also recorded in the repository's
`assets/pk-continuation-2026-11/weak-counterexample-amplification-exploration.md`.
The calculation above specializes it to the later Boolean-block support.

## The current sufficient inequalities also require n>=52

The independent n=52 reviewer identified a second obstruction, which is
specific to the present equal-block construction and its proof strategy.
Write theta=3/32, beta=27/64, delta_s=2s-1, delta_t=1-t>delta_s, and
delta_q=2q-1. For every retained subset size r, AM-GM gives
\((1-rx)(1+x)^r\le1\) whenever x>=0 and rx<1: the r+1 factors have
arithmetic mean one. Consequently

\[
 \alpha_r m^r<\theta^{r+1},\qquad
 E<4\theta\left[\left(1+\frac\theta m\right)^N-1\right].
\]

Here \(m=\theta(1+\delta_s)^3(1+\delta_q)^h\) and
\(\alpha_r=\theta(1-r\delta_t)^3(1-r\delta_q)^h\).
The strictness follows already from delta_t>delta_s>0.

The two sufficient inequalities used in the current proof,
\(E>m-1\) and \(\beta+E/4<m/e\), imply

\[
 m>\frac{11e}{16(4-e)}>
 m_0:=\frac{1205611}{826864}.
\]

For the last comparison use the exact lower bound
\(e>\sum_{j=0}^8 1/j!=109601/40320\). The function of m on the
right side of the upper bound for E is decreasing. For N<=12, exact
rational arithmetic gives

\[
 E<4\theta\left[\left(1+\frac\theta{m_0}\right)^{12}-1\right]
 <\frac{417120}{10^6}<\frac{458052}{10^6}<m_0-1<m-1,
\]

a contradiction. Thus N>=13, or n>=52, is necessary for **this pair of
sufficient inequalities**. This is not a lower bound on the integer
dimension of arbitrary counterexamples.

For comparison, a support-only calculation rules out d<=99 for every
N>=4 in the same Boolean-block support family: the excess fiber count
\(4(2^N-1)/2^{4N}\) decreases with N and is at most 60/65536 at N=4,
whereas the exact bound
\((109601/40320)(99/100)^{99}>201/200\) shows
\(e\Gamma_d>1+1/200\) for d<=99. The two obstructions identify why
optimizing the existing parameters cannot achieve the requested range.
