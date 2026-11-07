# The balanced tetrahedron family cannot have continuous dimension below 228

Research note, 7 November 2026. This is a proved obstruction for the specific
balanced construction family below, not a lower bound for arbitrary
mixed-integer counterexamples. It is outside the fact graph and is not
Lean-formalized.

Consider the family in [fact df488edae05a1702](../../facts/df488edae05a1702.md),
with four equally sized blocks of $N\geq1$ integer coordinates,
$n=4N$, the centered tetrahedron and its four barycentric cube sources,
and the original geometric parameter inequalities. The free box may be
replaced by any common full-dimensional convex body with zero in its
interior. An arbitrary additional common full-dimensional convex product
factor is allowed.
Write $d$ for the final continuous dimension. Then a counterexample to
$1/(e2^n)$ in this entire family requires $d\geq228$, independently of
which halfspaces are used to establish it.

If one additionally uses the four middle cuts from the accepted
construction to certify every origin-fiber point, then necessarily
$N\geq13$, and the continuous dimension must exceed
$2.7\cdot10^{15}$. Thus adjusting the free dimension, changing its convex
shape, or removing the separate padding cannot reach $n,d<100$ in this
balanced family.

## An upper bound for all negative-fiber masses

Normalize the middle-fiber volume to one, ignoring any common product
factor, and put $\theta=3/32$, $L=2^{4N}$, and
$\delta_s=2s-1$, $\delta_t=1-t$, $\delta_q=2q-1$.
The geometric hypotheses imply
$0<\delta_s<\delta_t$ and $N\delta_t,N\delta_q<1$.
The positive fibers have common mass
$m=\theta(1+\delta_s)^3(1+\delta_q)^h>\theta$.
A negative fiber indexed by a subset of size $r$ has mass
$\alpha_r=\theta(1-r\delta_t)^3(1-r\delta_q)^h$.

For an integer $r\geq1$ and $0\leq u<1/r$,
$(1-ru)(1+u)^r\leq1$. Indeed its logarithmic derivative is
$-r/(1-ru)+r/(1+u)\leq0$, and its value at zero is one.
Applying this with $u=\delta_s,\delta_q$, and using
$\delta_t>\delta_s$, proves
$\alpha_rm^r\leq\theta^{r+1}$.
Therefore the total negative mass satisfies

$$
E=4\sum_{r=1}^N\binom Nr\alpha_r
\leq4\theta\left[\left(1+\frac\theta m\right)^N-1\right].
\tag{1}
$$

The same inequality holds for any choice of the common free convex body:
its volume cancels from all these ratios. Every negative mass is less than
$\theta<m$, so the largest actual fiber has normalized volume
$\max(1,m)$.

## The total-to-largest-fiber ratio

Let $A_N=4\theta[(1+\theta)^N-1]$. The total mass is
$W=(L-1)m+1+E$. We claim

$$
\frac{W}{L\max(1,m)}\leq1+\frac{A_N}{L}.
\tag{2}
$$

For $m\geq1$, substitute (1) into
$W/(Lm)=1-1/L+(1+E)/(Lm)$.
Both $1/m$ and the upper bound in (1) decrease with $m$, so the result
is at most its value at $m=1$, namely $1+A_N/L$.

For $\theta\leq m\leq1$, the upper bound
$(L-1)m+1+4\theta[(1+\theta/m)^N-1]$ is convex in $m$: after
the binomial expansion, all nonlinear terms are positive multiples of
$m^{-r}$. Its maximum on the interval occurs at an endpoint. The value
at $m=1$ is $L+A_N$. At $m=\theta$ the value is
$(L-1)\theta+1+4\theta(2^N-1)<L$, because
$4(2^N-1)\leq L$ and $1+2\theta L<L$ for $L\geq16$.
This proves (2).

With $a=1+\theta$, the ratio of successive $A_N/L$ is
$[a+(a-1)/(a^N-1)]/16\leq(a+1)/16<1$.
It follows that (2) is always at most its $N=1$ value:

$$
\frac{W}{2^n\max(1,m)}\leq1+\frac9{4096}.
\tag{3}
$$

## Actual halfspace-depth obstruction

The ordinary centroid Grünbaum inequality in the largest fiber provides
an actual mixed-integer point whose ambient halfspace depth is at least
$\Gamma_d\max(1,m)/W$, where $\Gamma_d=(d/(d+1))^d$.
An ambient halfspace with nonzero continuous normal retains at least
$\Gamma_d$ of that fiber; one with zero continuous normal contains the
entire fiber. Extra fibers can only increase its mass. Therefore a
$1/(e2^n)$ counterexample requires

$$
e\Gamma_d<\frac{W}{2^n\max(1,m)}\leq1+\frac9{4096}.
\tag{4}
$$

The identity $\log(e\Gamma_d)=\int_0^1t/(d+t)\,dt$ shows that
$e\Gamma_d$ decreases with $d$.
For $d=227$, let $x=1/454-1/(3\cdot227^2)>0$.
Since $1/(227+t)>1/227-t/227^2$ for $t>0$, one has
$\log(e\Gamma_{227})>x$ and hence
$e\Gamma_{227}>1+x+x^2/2$. The exact margin is

$$
x+\frac{x^2}{2}-\frac9{4096}
=\frac{129233375}{97882687770624}>0.
$$

Thus (4) is impossible for every $d\leq227$, proving $d\geq228$.
This argument applies to actual depth, not only the supplied origin-cut
certificate, and covers any extra common convex padding factor.

## Why the advertised four-cut certificate needs at least 52 integer coordinates

Let $\beta=27/64$. Any counterexample needs $W>Lm$, since the positive
fiber centroid has depth at least $\Gamma_dm/W>m/(eW)$.
Equivalently, $E>m-1$.
If the four supplied middle cuts all certify the target, then
$\beta+E/4<W/(eL)$.
Substituting $E>m-1$ into
$eL\beta+(eL/4-1)E<(L-1)m+1$ gives
$m>11e/[16(4-e)]$.

The exponential series gives
$e>\sum_{i=0}^6 1/i!=1957/720>1359/500$.
Consequently $m>m_0=14949/10256$.
For $N\leq12$, the right side of (1) decreases with $m$ and increases
with $N$, while $m-1$ increases. But exact rational arithmetic gives

$$
m_0-1-\frac38\left[\left(1+\frac{3}{32m_0}\right)^{12}-1\right]
=\frac{66098730374909167190347494288801583413879093343423}
{1640882018350513302409882405072444306744378401325056}>0.
$$

This contradicts $E>m-1$, so $N\geq13$.
Since $A_N/2^{4N}$ decreases with $N$, (2) now gives
$e\Gamma_d<1+A_{13}/2^{52}$, where
$A_{13}=(3/8)[(35/32)^{13}-1]$.
Also $e\Gamma_d>1+1/[2(d+1)]$, by the same integral identity and
$\exp(x)>1+x$. Thus
$d+1>2^{52}/(2A_{13})$, hence $d\geq2722291674329078$.

The $N\geq13$ statement is about this specific four-cut certificate.
The unconditional $d\geq228$ statement is about the entire stated balanced
family. Neither statement excludes different lattice supports, unequal
tetrahedron cut levels, or different source shapes. The comparison here is
with $1/e$; an obstruction to the sharp $\Gamma_d$ target would need a
different argument.
