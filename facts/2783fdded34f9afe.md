---
fact_id: 2783fdded34f9afe
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-three-active-caps-source-parity-vacancy
depends_on: ["a83339dae406ffd6", "6769574fc1bd9f8d"]
verifier_run: 0a670c383c98bcf1
target_match: null
---

## Source

- [b02f449107e522a5](../candidates/b02f449107e522a5.json), b02f449107e522a5:01 Statement and §§1–4 (1)–(4).

## Statement

Let $d\ge4$ and let $T$ be a $d$-simplex of volume $V$ with barycentric coordinates $\lambda_0,\ldots,\lambda_d$. Set $D_\delta=\{x\in T:\sum_{i=2}^d\lambda_i(x)\le\delta\}$ for $0<\delta<1/(d+1)$. Let $C\subset\mathbb R\times\mathbb R^d$ be a compact convex body with $K_{-1}=D_\delta$, $K_0=T$, and all nonempty sampled fibers of positive $d$-volume. Use pure uniform outward smoothing with width $h\Gamma(u)$, where $\Gamma$ is the actual pooled within-fiber covariance norm and $0<h<1/(1000d)$. Suppose a deepest mark $Y_0=(0,y_0)$ has proper own core and there are three actual active caps with affine margins $a_i z+f_i(x)$, $i=2,3,4$, such that $f_i(y_0)=0$ and
$$
\sup_T|f_i-(\lambda_i-1/(d+1))|\le 1/[20(d+1)].
$$
Assume they miss $D_\delta$ in the smoothed sense and have zero transition-strip coarea on every outside fiber. Then base zero is the only deepest integer base.

## Proof

For any affine functional, the fiber minimum is a convex function of the real base on the projection interval, and the maximum is concave, by taking convex combinations of minimizing or maximizing points. Every barycentric coordinate has minimum zero on each of $D_\delta,T$. Thus all fibers at real bases $z\ge0$ lie in $T$. The sum $R=\sum_{i=2}^d\lambda_i$ has minima zero at both bases and maxima $\delta,1$ at bases $-1,0$. If a sampled base less than $-1$ existed, the projection would contain $-2$. There the minimum would be nonnegative and the maximum at most $2\delta-1<0$, a contradiction.

The normalized volume of $D_\delta$ is $d(d-1)\int_0^\delta r^{d-2}(1-r)\,dr=d\delta^{d-1}-(d-1)\delta^d$. Indeed in standard barycentric coordinates the $d-1$ nonnegative coordinates with sum $R=r$ give section weight proportional to $r^{d-2}$ and the two remaining coordinates give factor $1-r$, with the constant fixed by integration over $[0,1]$. Hence $|D_\delta|/V<d/5^{d-1}\le4/125$. The middle simplex centroid has raw smooth depth at least $\gamma_d V$, where $\gamma_d=(d/(d+1))^d$, because its ordinary own-fiber centroid caps have that lower bound by 6769574fc1bd9f8d, smoothing only adds mass, and a pure-base cap includes the whole own fiber. The elementary bounds $8/3<e<11/4$ follow by summing through $1/3!$ and bounding the remaining terms by $(1/24)/(1-1/5)$. In particular $\gamma_d>1/e>4/11$, so the exposed pure-base cap of mass $|D_\delta|$ excludes deepestness at base $-1$.

If a deepest mark existed at any positive integer base, interpolate with $Y_0$ to obtain a feasible mark at base one. Its depth is at least the deepest value. For each nonvertical normal, mass is nonincreasing in the threshold, and the interpolated threshold is at most the larger of the two original ones. Both original masses are at least the deepest value, so this inequality holds at the interpolated mark. The same monotonicity argument applies to pure-base caps with closed boundaries. Thus base one would have a deepest mark.

At any selected cap the proper own core gives positive strip coarea. For its covariance-unit normal $N=(a,u)$ the derivative of the mass in the threshold is strictly negative at $c=N\cdot Y_0$. Thus a distinct deepest mark cannot have larger threshold for this cap. If its threshold were equal, the same normalized cap would be minimizing at both marks. The first variation of a83339dae406ffd6 at zero buffer gives $m-SY=A(0,\nabla\Gamma(u))$, where $S=\int\psi(q)\,d\mu/h>0$, $m=\int W\psi(q)\,d\mu/h$, $A=\int q\psi(q)\,d\mu$ and $q=(N\cdot W-c)/h$. Here $\psi$ is the indicator of the open ramp strip in normalized coordinates. The normalized cap has exactly the same data at both marks, so both marks would coincide. Consequently every selected cap has strictly negative margin at the putative mark on base one. Its zero outside strip coarea forces the integrand to be constant zero or one on the whole positive-volume convex fiber, by continuity and connectedness, and the strict margin excludes one.

Write $\epsilon=1/[20(d+1)]$ and $w_i=h\Gamma(\nabla f_i)>0$. The positive rescaling of a cap's normal changes its width by the same factor and leaves its integrand unchanged. The two whole misses give $\max_{D_\delta} f_i-a_i\le-w_i$ and $\max_{K_1}f_i+a_i\le-w_i$. A vertex of $T$ with index $0$ belongs to $D_\delta$, so $\max_{D_\delta}f_i\ge-1/(d+1)-\epsilon$. Using $K_1\subseteq T$ and the uniform closeness, one gets $\lambda_i\le b=21/[10(d+1)]$ on $K_1$ for $i=2,3,4$. Since $b\le21/50<1/2$, a real fiber at $2$ would have maximum of $\lambda_2$ at most $2b-1<0$ by concavity, contradicting its nonnegative minimum. If any sampled base above one existed, the projection would contain $2$. Thus base one would be exposed.

The simplex volumes of one event $\lambda_i>b$ and of the intersection of two such events are respectively $(1-b)^dV$ and $(1-2b)^dV$, by translation and dilation in barycentric coordinates. Inclusion-exclusion, omitting the subtraction of the triple intersection in the complement formula, gives
$$
|K_1|/V\le 1-3(1-b)^d+3(1-2b)^d.
$$
For $c\ge2$ the function $F_c(x)=(1-c/(x+1))^x$ is increasing on $x+1>c$. With $t=1/(x+1)$ its logarithmic derivative is
$$
\log(1-ct)+\frac{ct(1-t)}{1-ct}
=\sum_{k\ge2}c^{k-1}\bigl[c(1-1/k)-1\bigr]t^k\ge0.
$$
With $c=21/10$ this yields $(1-b)^d\ge(29/50)^4$. Also $(1-2b)^d\le(1-4/(d+1))^d<e^{-4}<1/50$. For the strict exponential bound use $\log(1-s)\le-s-s^2/2$ with $s=4/(d+1)$, giving exponent at most $-4d/(d+1)-8d/(d+1)^2<-4$. The bound $e>8/3$ gives $e^4>50$. It follows that $|K_1|/V\le1-3(29/50)^4+3/50=4503157/6250000$.

For any mark $y\in K_1$, consider the two opposite continuous directions of $\lambda_2$. Their own-fiber smoothed masses sum to at most $|K_1|$ plus the $T$-volume of the slab $|\lambda_2-\lambda_2(y)|\le w$, where $w=h\Gamma(\nabla\lambda_2)$. All original fibers, including $D_\delta$, lie in $T$. Thus $\lambda_2$ has variance at most $1/4$ on each, and the pooled within-fiber variance gives $w\le h/2$. The $\lambda_2$ marginal under volume on $T$ has density $d(1-s)^{d-1}V$ on $[0,1]$, by the same one-coordinate homothety. The slab volume is at most $2dwV\le dhV$. At least one direction therefore has own-fiber mass at most $|K_1|/2+dhV/2$. Because base one is exposed, one finite sufficiently large base tilt makes this cap miss every other sampled fiber, including its smoothing strip. Its mass is strictly less than
$$
\left(\frac{4503157}{12500000}+\frac1{2000}\right)V<\frac4{11}V<\gamma_d V,
$$
using $4/11-4503157/12500000=465273/137500000>1/2000$. This contradicts deepestness at base one and proves the assertion.
