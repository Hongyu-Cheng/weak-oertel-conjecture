# Independent audit of the simplex-factor compression

Date: 2026-11-07. Reviewed [compress-simplex-factor.md](compress-simplex-factor.md), [compress-certificate.py](compress-certificate.py), and [compress-certificate.json](compress-certificate.json). The inherited tetrahedral geometry was independently checked in [verify-current.md](verify-current.md).

Verdict: the new construction and its strict depth bound are supported by the proof and exact arithmetic. I found no substantive mathematical gap. It gives $n=52$ and $d=1345226000000000003$. This is an independent LLM mathematical review with exact rational computation, not formal verification; the result remains a research note outside the accepted graph.

## Geometric audit

The box was used in the previous origin-fiber proof only through its normalized linear facet inequalities and its scaling law for volume. Both extend to a full-dimensional rational simplex containing zero in its interior.

For the proposed explicit simplex $F=\operatorname{conv}(e_1,\ldots,e_h,-\sum_i e_i)$, its centroid is zero and one exact facet description is

$$
L_0(w)=\sum_i w_i\le1,
\qquad
L_j(w)=\sum_i w_i-(h+1)w_j\le1
\quad(1\le j\le h).
$$

Each listed form is at most $1$ on every vertex and equals $1$ on exactly the opposite facet. For every positive scale $u$, its maximum on $uF$ is $u$. Therefore the claimed affine envelope $L_j(w)\le1+\delta_q\sum_i z_i$ holds on every positive, negative, and origin generator. At $z=0$ it gives exactly $F$. Together with the previously checked tetrahedral envelope, it proves that the actual origin fiber remains $B_0\times F$.

The projection and exposing functionals depend only on the integer bases. Consequently the integer census and every nonzero actual fiber are unchanged except for the replacement of the free factor. Every scale is strictly positive. The origin fiber spans all continuous directions and the positive unit bases span all integer directions, giving full ambient dimension.

The homothetic volume ratios are exactly the same expressions $m$ and $\alpha_r$ as before, with exponent $h$. The four origin cuts ignore $w$, so their coverage and masses $b(27/64+E/4)$ are unchanged.

For a point above a nonzero base $z_0$, the free factor is a positive homothetic copy of $F$. Its largest barycentric coordinate is at least $1/(h+1)$, giving a containing closed cap of relative simplex volume at most $\Gamma_h$. The other three coordinates are unrestricted, so this is also the relative volume in the whole fiber. To make the isolation explicit, let $\lambda$ be this barycentric coordinate, $w_0$ the chosen point's free coordinate, and $\psi$ an integer functional uniquely maximized at $z_0$. Use

$$
\lambda(w)-\lambda(w_0)+M[\psi(z)-\psi(z_0)]\ge0.
$$

At $z_0$ this is precisely the chosen cap. On every other integer fiber, the second term tends uniformly to a strictly negative value as $M\to\infty$, whereas the first term is bounded on its compact free factor. Finitely many bases therefore admit one finite $M$ excluding them all strictly. The continuous normal is nonzero, so this is a proper closed ambient halfspace, even when the cap through a boundary point has zero volume.

All negative-fiber masses are below $(3/32)b$, and every positive-fiber mass is $mb>(3/32)b$. Thus every nonzero-fiber point has a containing cut of mass at most $\Gamma_hmb$. The two strict uniform mass estimates establish a strict bound on the supremum, including all boundary points. The finite union of full-dimensional fibers has the stated intrinsic Hausdorff measure.

## Independent exact arithmetic

The supplied certificate ran successfully and reproduced its saved JSON byte for byte. Its exponentiation uses a valid positive interval invariant: lower products are rounded down and upper products up at every binary multiplication and squaring. The geometric inequalities and the rational comparison with the upper bound on $e$ all hold. In particular, the factorial tail starting at $1/51!$ is strictly below $52/(51\cdot51!)$.

For an independent check, I did not reuse the binary-power routine. Put $x=274778504931/(10^{11}h)$ and define $a_k=\binom hk x^k$, generated exactly by $a_{k+1}=a_k(h-k)x/(k+1)$.

For $(1+x)^h$, the first 121 positive terms give a lower bound. The remaining tail is bounded above by $a_{121}/(1-hx/122)$, since all subsequent ratios are at most $hx/122<1$.

For $(1-rx)^h$, use the alternating binomial expansion through degree 180. From degree 180 onward the term magnitudes strictly decrease, since the ratio $(h-k)rx/(k+1)$ is below one and decreases with $k$. The degree-180 partial sum is an upper bound and subtracting the next term gives a lower bound. This holds for the finite binomial polynomial as well as an infinite alternating series; pairing successive decreasing terms proves the two bounds directly.

These rational bounds independently confirm

$$
\begin{aligned}
1463252115845211/10^{15}&<m<1463252115845212/10^{15},\\
465701482650506/10^{15}&<E<465701482650507/10^{15}.
\end{aligned}
$$

The independent intervals have width below $10^{-140}$ for $m$ and $10^{-43}$ for $E$. The following standard-library computation reproduces the check:

```python
from fractions import Fraction as F
from math import comb

h = 1345226000000000000
x = F(274778504931, 10**11*h)
ds, dt = F(1, 10**24), F(2, 10**24)

def bounds(x, alternating):
    count = 180 if alternating else 120
    term = total = F(1)
    for k in range(1, count+1):
        term = term*(h-k+1)*x/k
        total += (-1 if alternating and k % 2 else 1)*term
    following = term*(h-count)*x/(count+1)
    if alternating:
        assert count % 2 == 0 and following < term
        return total-following, total
    ratio = h*x/(count+2)
    assert 0 < ratio < 1
    return total, total+following/(1-ratio)

lo, hi = bounds(x, False)
mlo, mhi = F(3, 32)*(1+ds)**3*lo, F(3, 32)*(1+ds)**3*hi
Elo = Ehi = F(0)
for r in range(1, 14):
    lo, hi = bounds(r*x, True)
    weight = F(3, 8)*comb(13, r)*(1-r*dt)**3
    Elo += weight*lo
    Ehi += weight*hi
assert F(1463252115845211, 10**15) < mlo < mhi < F(1463252115845212, 10**15)
assert F(465701482650506, 10**15) < Elo < Ehi < F(465701482650507, 10**15)
assert mhi-mlo < F(1, 10**140)
assert Ehi-Elo < F(1, 10**43)
```

The origin-cut margin and the finite-simplex cap margin in the supplied JSON are strictly positive. The estimate $e\Gamma_h<1+1/(2h-1)$ therefore proves the required nonzero-fiber bound without any separate padding dimension.

## Remaining dimension obstruction

The maximal-fiber centroid argument from [verify-current.md](verify-current.md) also applies to these improved masses. With $\Delta=1+E-m$, a strict counterexample retaining this largest-fiber fraction must satisfy $d+1>2^{51}m/\Delta$. Using the new certified endpoints gives

$$
d+1>
\frac{205934427614674440789015134208}{153085425331}
>1.345225563892870788\cdot10^{18}.
$$

The proposed $h$ exceeds this necessary lower bound by a factor below $1.000000325$. Thus the construction is already extremely close to the dimension forced by its mass distribution. The previous support-count obstruction also remains unchanged. Neither observation rules out a different construction with $n,d<100$.

## Additional review of the balanced-family obstruction

I also checked [compress-family-barrier.md](compress-family-barrier.md). Its unconditional conclusion $d\ge228$ is valid for the stated balanced tetrahedron family with the original geometric parameter inequalities, any common full-dimensional free convex body containing zero in its interior, and any common full-dimensional convex padding body. It is not a lower bound for arbitrary mixed-integer counterexamples.

The product estimate $(1-ru)(1+u)^r\le1$ is valid on $0\le u<1/r$. Since $\delta_t>\delta_s$, it gives $\alpha_rm^r\le\theta^{r+1}$ and hence the displayed bound on $E$. For $m\ge1$, the bound on $(1+E)/m$ decreases with $m$. For $\theta\le m\le1$, the proposed upper bound on total mass is convex, because its nonlinear terms are positive multiples of $m^{-r}$. Its value at $m=\theta$ is below $2^{4N}$, and its value at $m=1$ is $2^{4N}+A_N$. Thus the claimed total-to-largest-fiber ratio bound follows. The ratio $A_N/2^{4N}$ decreases with $N$, giving its maximum $9/4096$ at $N=1$.

Applying the ordinary centroid inequality to an actual largest fiber is legitimate and requires no assumption about which cuts might certify a counterexample. The exact $d=227$ comparison uses $x=1/454-1/(3\cdot227^2)$ and

$$
x+x^2/2-9/4096=129233375/97882687770624>0.
$$

I independently recomputed this identity using rational arithmetic. The integral formula for $\log(e\Gamma_d)$ gives both its monotonicity and the strict lower bound by $x$ at $d=227$. Hence every $d\le227$ is excluded.

The stronger conditional conclusion for the supplied four origin cuts is also correct. Combining their exact target inequality with the necessary $E>m-1$ yields $m>11e/[16(4-e)]$ without discarding the finite factor $2^{4N}$. The stated lower approximation to $e$, the exact positive $N=12$ contradiction, and $2^{52}/(2A_{13})>2.7\cdot10^{15}$ all passed separate rational checks. This supports $N\ge13$ and the stated dimension lower bound specifically when those four cuts certify the target.

No accepted fact, candidate, verification record, or graph state was changed by this audit.
