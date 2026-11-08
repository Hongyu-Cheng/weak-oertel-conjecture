---
fact_id: 2cedfd9dfe672cb5
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-four-interval-unweighted-buffer-power-tie-breaking
depends_on: []
verifier_run: 8607b5abbab82062
target_match: null
---

## Source

- [3101206ec4580190](../candidates/3101206ec4580190.json), §5, unweighted exponent calibration.
- [1298c8ea2c6ec3df](../candidates/1298c8ea2c6ec3df.json), §§1–3, exact four-interval all-source calibration at r=1/2.
- [75dd33535e246a34](../candidates/75dd33535e246a34.json), §§1–3, convex interval roofs and complete ordinary clipping tables.

## Statement

Let the interval fibers at bases $0,1,2,3$ be
$$
K_0=[47/50,26/25],\quad K_1=[-11/10,1],\quad K_2=[-23/25,23/25],\quad K_3=[-9/100,9/100].
$$
Use original length on the four fibers, with total length $M=211/50$ and within-fiber variance $\Sigma=1937167/6330000$. The ordinary maximum raw depth is $Q=11/10$, attained exactly at $(1,0),(2,0)$.

For a nonnegative shift $\delta_p(y)$ at a source $(p,y)$, define shifted depth as the infimum of the masses of the nonvertical caps
$$
x\ge y+t(z-p)-\delta_p(y),\qquad x\le y+t(z-p)+\delta_p(y)\qquad(t\in\mathbb R)
$$
and the unshifted closed pure-base caps containing $p$. If $\delta_p(y)\le1/10000$ at all sources and $\delta_i$ is Lipschitz with constant strictly below one on $|y|\le1/1000$ for $i=1,2$, the exact shifted depths at the two marks are $Q+\delta_i(0)$, and all maximizers are precisely the marks with the largest $\delta_i(0)$.

In particular, use ordinary projective energy $E_p(y)$ in each interval and $\delta_p(y)=\varepsilon\sqrt{\Sigma}(E_p(y)/M)^r$ with $0<r\le1$ and $0<\varepsilon\le1/10000$. The marked energies are $E_1(0)=44/21$ and $E_2(0)=46/25$. Hence the exact global raw maximum is $Q+\varepsilon\sqrt{\Sigma}(44/(21M))^r$, attained only at $(1,0)$. At this mark the projective covector is $-1/22$ and the weighted transformed resultant of the regular active pair, with weights balancing the source derivatives, is nonzero if $r\ne1/2$.

## Proof

The successive increments of the lower endpoints are $-51/25,9/50,83/100$, and those of the upper endpoints are $-1/25,-2/25,-83/100$. The respective affine interpolations are convex and concave and define an actual convex body with precisely these sampled fibers. The lengths are $1/10,21/10,46/25,9/50$, giving $M$ and $\Sigma=(\sum_p|K_p|^3)/(12M)$.

For the two marks $(p,0)$, $p=1,2$, write $[l_z,u_z]=K_z$. The ordinary upper-oriented cap mass is
$$
F_p(t)=\sum_{z=0}^3 \min\{u_z-l_z,[u_z-t(z-p)]_+\},
$$
and its reverse has mass $M-F_p(t)$. The values at all clipping breakpoints, with constant outer tails, are
| $p$ | Breakpoints $t$ in increasing order | Values of $F_p$ |
| --- | --- | --- |
| $1$ | $-26/25,-47/50,-23/25,-9/200,9/200,23/25$ | $151/50,78/25,78/25,449/200,79/40,11/10$ |
| $2$ | $-1,-13/25,-47/100,-9/100,9/100,11/10$ | $11/10,79/50,173/100,211/100,211/100,78/25$ |

The entries follow by substituting the ratios $l_z/(z-p),u_z/(z-p)$ for $z\ne p$. Between them the profile is affine. Thus every nonvertical cap through either mark has mass at least $Q$, and the smallest closed pure-base masses there are $11/5$ and $101/50$. A nonnegative shift adds exactly $\delta_p(0)$ to the own interval mass at either mark and cannot reduce another contribution. This gives the shifted lower bound, including the pure-base caps.

At base $1$, the margins $x-(z-1)$ and $-x-(93/100)(z-1)$ have original cap mass $Q$. The first strictly captures $K_0$ and strictly misses $K_2,K_3$, and the second strictly misses all other intervals. At base $2$ the margins $\pm x+2(z-2)$ have mass $Q$, strictly capture $K_3$ and strictly miss $K_0,K_1$. The smallest exterior status margin of these four caps is $1/100$, by direct evaluation of the endpoint margins. Enlarging the appropriate caps by $\delta_p(0)$ therefore adds exactly that shift and gives the matching marked values.

Write $\eta=1/1000$. For $|y|\le\eta$ in an inner fiber the source translation plus shift has absolute size at most $\eta+1/10000<1/100$, so both caps of its pair keep all external statuses and the own cuts remain proper. Choosing the orientation facing $y$ gives an upper bound $Q-|y|+\delta_p(y)$, which is strictly below $Q+\delta_p(0)$ if $y\ne0$. For $|y|\ge\eta$ in an inner fiber one of the same ordinary caps tightened by $\eta$ contains $(p,y)$, still has the old external statuses, and has mass $Q-\eta$. The corresponding ordinary cap through the source can only have smaller mass. At an outer base a steep tilt isolates its own interval, with ordinary depth at most $9/100$. Any cap enlargement by $\delta_p(y)$ adds at most $4\delta_p(y)$ to a through-source nonvertical cap mass, since the captured length in each interval is $1$-Lipschitz in the threshold. Pure-base caps do not change. Hence outside the two neighborhoods shifted depth is at most $\max\{Q-\eta,9/100\}+4/10000<Q$. These arguments also apply to identically zero shifts, proving the ordinary claim.

For an interval of length $V$ and midpoint $m$, energy at $y$ is $V-4(y-m)^2/V$. To see this at an interior point, the projective map sends the two translated endpoints $l-y,u-y$ to their quotients by $1+a(l-y),1+a(u-y)$ respectively. The image length is $V$ divided by the product of these denominators, by direct subtraction or integration of the one-dimensional Jacobian. The product is a quadratic in $a$ with its maximum in the positive-denominator interval. Substitution gives $4(y-l)(u-y)/V$, which extends by zero at endpoints. For the two inner intervals, substitution gives the stated mark energies and $E_i(y)>1$, $|E_i'(y)|<1$ on $|y|\le\eta$. Since $E_p(y)\le|K_p|<M$ and $\Sigma<1$, the shifts are at most $\varepsilon$. On the inner neighborhoods $|\delta_i'(y)|=\varepsilon\sqrt{\Sigma}\,r(E_i/M)^r|E_i'|/E_i<\varepsilon$. The shift criterion applies and $E_1(0)>E_2(0)$ gives the strict winner for all stated $r$.

The optimizing quadratic at $(1,0)$ has vertex $a=-1/22$, and $E_1'(0)/E_1(0)=2a$. The regular active pair there has continuous normals $\pm1$. Its positive weights can be chosen to sum to one with difference $\delta_1'(0)=2r\,\delta_1(0)a$, since $|\delta_1'(0)|<1$. The projective map sends the continuous normal $u$ to $u-\delta_1(0)a$, by multiplying the transformed margin by the positive inverse denominator. Thus the weighted resultant is $(2r-1)\delta_1(0)a$, as asserted.
