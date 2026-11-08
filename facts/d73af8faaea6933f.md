---
fact_id: d73af8faaea6933f
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-four-monotone-triangle-fiber-centroid
depends_on: ["4d628efe7673ce2d", "6f616779219fd76c", "9a3bf974682e425a", "b39ecb342488b802"]
verifier_run: 4968e2a2913f5bc2
target_match: null
---

## Source

- [680d45e380747dc3](../candidates/680d45e380747dc3.json), Opening and §§2–4 (4)–(11), with §1 as a separate dependency.

## Statement

Let $T=\operatorname{conv}(0,e_1,e_2)\subset\mathbb R^2$, $V=|T|$, and let $C\subset\mathbb R\times\mathbb R^2$ be a convex body with integer fibers $C_k=r_kT$ at $k=0,1,2,3$ and empty integer fibers elsewhere. Assume the radii are positive and concave, so $2r_1\ge r_0+r_2$ and $2r_2\ge r_1+r_3$, and that they are monotone. Set $S=C\cap(\mathbb Z\times\mathbb R^2)$ and $M=V\sum_{k=0}^3r_k^2$. Define $h_S(y)$ as the infimum of the mixed area of $S\cap H$ over all closed ambient halfspaces $H$ containing $y$.

If $r_0\le r_1\le r_2\le r_3$, choose $j=3$ when $r_3^2\ge\frac12\sum_{k=0}^3r_k^2$ and choose $j=2$ otherwise. Then the actual centroid $y=(j,r_j/3,r_j/3)$ satisfies $h_S(y)\ge(2/9)M$. For $r_0\ge r_1\ge r_2\ge r_3$, reflect the rule: choose $j=0$ when $r_0^2\ge\frac12\sum_{k=0}^3r_k^2$ and choose $j=1$ otherwise. More generally, for fibers $v_0+kv_1+L(r_kT)$ with a fixed invertible planar linear map $L$ and fixed $v_0,v_1\in\mathbb R^2$, the same rule chooses the base and gives the same normalized bound at that fiber's actual centroid.

## Proof

**Actual fibers and the two choices.** For positive common-vertex triangle radii at consecutive integer bases, convexity requires the two stated midpoint inequalities by applying it to points $(k,r_ke_1)$. Conversely, the piecewise-affine interpolant $r(z)$ on $[0,3]$ is positive and concave under those inequalities. The set $\lbrace(z,x):0\le z\le3,\ x\in r(z)T\rbrace$ is a compact convex body with nonempty interior. It is convex because $r(z)T$ is described by $x_1,x_2\ge0$ and $x_1+x_2\le r(z)$. On each unit base interval, every point $(z,r(z)u)$, $u\in T$, is the corresponding convex combination of the two lifted points with the same $u$. Thus this body is the convex hull of the prescribed fibers and has exactly those integer fibers. The depth for any body with the prescribed integer fibers depends only on their mixed area measure.

Work in the nondecreasing orientation and put $\Gamma=4/9$. Each fiber centroid is the average of its three vertices. If $r_3^2\ge\frac12\sum_k r_k^2$, its area is at least $M/2$. Apply the heavy-fiber clause of 4d628efe7673ce2d, assertion (3), to the actual positive-area terminal fiber of this convex body, with planar area $Vr_3^2$ and total mixed area $M$. That clause gives $h_S(3,r_3/3,r_3/3)\ge \Gamma M/2$, also at equality in the heavy test.

Otherwise divide the planar coordinates and radii by $r_2$. This multiplies all areas, including the total and every cap mass, by $r_2^{-2}$. Write the resulting radii as $(a,b,1,R)$. They satisfy
$$
0<a\le b\le1\le R,\qquad 2b\ge a+1,\qquad R\le2-b,\qquad R^2<a^2+b^2+1 .
$$
In particular $b\ge1/2$. The chosen centroid is $(2,1/3,1/3)$. The affine majorant $1+(R-1)(k-2)$ equals the normalized radius at $k=2,3$, is at least $b$ at $k=1$ by $R\le2-b$, and is at least $a$ at $k=0$ by $3-2R\ge2b-1\ge a$.

**Shared normal and tilt.** Apply 6f616779219fd76c with $n=1$, $d=2$, bases $0,1,2,3$, anchor $2$, these four positive radii, and the displayed touching majorant. Every closed ambient halfspace containing the centroid has a replacement through the centroid with no larger mass on each fiber. Its planar normal $w$ has nonnegative entries of sum one, and its single real tilt $\beta$ gives thresholds
$$
1/3+2\beta,\quad 1/3+\beta,\quad 1/3,\quad 1/3-\beta .
$$
The comparison includes a purely base-normal cap: the accepted reduction keeps the strictly included fibers whole and the strictly excluded fibers empty and takes a subset of each whole boundary fiber. The compactification in 9a3bf974682e425a applies with $q=1/3$ and the same positive radii and bases. Its clipping radius is $R-1/3$, since the off-anchor distance-one term at the last base is $R-1/3\ge2/3$ and the other terms are at most $2/3$. Clipping to this interval preserves every fiber mass for every $w$. We prove the scalar lower bound on all of $\mathbb R$. With $P_r$ from the positive-normal triangle cap envelope, the replacement cap's mass divided by $V$ is bounded below by the sum of the four envelope values. The tilt is shared; minimizing $w$ separately to obtain these values only lowers this sum.

**Two scalar estimates.** For $1/2\le b\le1$ and $1/6\le x\le1/3$ we have
$$
P_b(x)+P_1(2/3-x)\ge\Gamma b^2 .
\tag{1}
$$
Indeed, $Q(x)=P_1(2/3-x)=-8x^2+(20/3)x-8/9$ on this interval. For fixed $b$, let $F(x)=P_b(x)+Q(x)-\Gamma b^2$. Before $x=b/2$, its two possible quadratic pieces have negative quadratic coefficients and matching first derivatives at $x=b/3$, so $F$ is concave there. After $b/2$ it is also concave, since $P_b(x)=0$ there. It suffices to check $1/6$, $1/3$, and $b/2$ when $b/2\le1/3$. At these points, respectively,
$$
\begin{aligned}
F(1/6)&=\frac{(2b-1)(10b-1)}{36}\ge0,\\
F(1/3)&\ge\frac49(1-b^2)\ge0,\\
F(b/2)&=\frac{2(1-b)(11b-4)}9\ge0 .
\end{aligned}
$$
The first line uses $1/6\le b/3$, and the last line is used for $1/2\le b\le2/3$. This proves (1).

For every $R\ge1$ and $1/3\le t\le1/2$,
$$
P_R(t)-P_1(t)\ge\frac23(R^2-1)\ge\frac{\Gamma}{2}(R^2-1).
\tag{2}
$$
As the radius $r$ varies from $1$ to $R$, we have $r\ge2t$. In the branch $2t\le r\le3t$, the derivative in the radius is $4t\ge4r/3$. For $r\ge3t$ it is $2(r-t)\ge4r/3$. The formulas are continuous at the interface, so integrating gives (2), including the supporting threshold $r=1$, $t=1/2$ and the equality case $R=1$.

**All real tilts.** The following comparison uses only $0<a\le b\le1\le R$, $2b\ge a+1$, and $R^2<a^2+b^2+1$. Its target is $\frac{\Gamma}{2}(a^2+b^2+1+R^2)$.

- For $\beta\ge0$, the own threshold is $1/3$ and the last threshold is at most $1/3\le R/3$. Their two envelope values contribute at least $\Gamma(1+R^2)$, which is sufficient because $a^2+b^2\le1+R^2$.
- For $\beta\le-1/6$, the first threshold is at most zero, so its envelope is the full area divided by $V$, namely $a^2$. The second threshold is at most $1/6\le b/3$. Together with the own fiber this gives $a^2+\Gamma b^2+\Gamma\ge\Gamma(a^2+b^2+1)>\frac{\Gamma}{2}(a^2+b^2+1+R^2)$. The strict inequality uses the nonheavy hypothesis.
- For $-1/6\le\beta\le0$, put $x=1/3+\beta$. The second and fourth thresholds are $x\in[1/6,1/3]$ and $2/3-x\in[1/3,1/2]$. Discard the nonnegative first term. By (1) and (2), the remaining sum is at least
$$
\Gamma+\Gamma b^2+\frac{\Gamma}{2}(R^2-1)
=\frac{\Gamma}{2}(1+2b^2+R^2)
\ge\frac{\Gamma}{2}(a^2+b^2+1+R^2).
$$
The last step uses $a\le b$.

The ranges cover all tilts with their endpoints. Multiplying by $V$ and undoing the planar scaling proves the depth bound at the specified actual centroid. The weak order inequalities allow repeated radii, and equality in the heavy test was covered in the first choice. The reflection $(z,x)\mapsto(3-z,x)$ permutes the integer fibers and preserves all cap masses. The invertible affine map $(z,x)\mapsto(z,v_0+zv_1+Lx)$ takes halfspaces to halfspaces and sends each centroid to the actual centroid of its image fiber. It multiplies each planar area, each mixed cap mass, and the total mixed area by $|\det L|$, which proves the normalized assertion after this map.
