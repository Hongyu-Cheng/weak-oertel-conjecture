---
fact_id: fa0d66edea26e81a
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-eight-triangle-chain-critical-depth-value
depends_on: []
verifier_run: 888c888da44d639d
target_match: null
---

## Source

- [ad88f967d6335089](../candidates/ad88f967d6335089.json), ad88f967d6335089:08 §4, paragraph following (12), separate eight-triangle witness.
- [d4522420ea2ebef1](../candidates/d4522420ea2ebef1.json), d4522420ea2ebef1:02 §§1–4, (1)–(11), exact value portion only.

## Statement

Let $T$ be an area-one triangle with centroid $g$ and barycentric functions $\lambda_i$, and let $C=[0,7]\times T$ have summed area on its eight integer fibers. The maximum raw depth is $112/33$, attained at $(3,g)$ and $(4,g)$. In particular the three closed caps $\lambda_i(x)-(2/33)(z-3)\ge1/3$ attain the minimum at $(3,g)$, and their reflections in $z=7/2$ attain it at $(4,g)$. All eight cuts of each such cap are proper, and the normalized value is $14/33$.

## Proof

At $(3,g)$ a pure-base through-point cap has mass at least four. For every nonzero continuous coefficient, center the continuous functional at $g$, order its vertex heights and rescale its minimum to $-1$. The ordered heights are $-1,t,1-t$, where $-1\le t\le1/2$. The threshold at base $z$ is $L(z-3)$ for some real $L$. With $F_t$ denoting upper-tail area, the raw mass is $G(t,L)=\sum_{k=-3}^{4}F_t(kL)$. For $-1<t<1/2$, the four successive branches of $F_t(s)$ are $1$, $1-(s+1)^2/[(t+1)(2-t)]$, $(1-t-s)^2/[(2-t)(1-2t)]$, and $0$, with breakpoints $-1,t,1-t$. These are obtained by the ratios on the two edges of the captured or omitted corner triangle. Closed boundary lines have zero area. At either endpoint of the $t$ range the nonempty branches have the same formulas by direct corner ratios. Pairing the terms $-3,\ldots,3$ gives $G(t,L)\ge G(t,|L|)$ for negative $L$ by monotonicity of the remaining tail. For $L\ge2$ the value is $3+F_t(0)\ge31/9$. Indeed for $-1\le t\le0$ subtracting $4/9$ from the upper-branch formula for $F_t(0)$ has numerator $(1+t)^2$ over the positive denominator $9(2-t)(1-2t)$, and for $0\le t\le1/2$ the lower-branch formula gives at least $1/2$.

For $-1<t<1/2$, $0\le L\le2$, the exact rational partition and degree-three Bernstein coefficient data are in [the eight-fiber certificate](../assets/pk-nov6/computations/triangle-eight-fiber-depth-exact-certificate.json), with [exact replay](../assets/pk-nov6/computations/verify_triangle_eight_depth_exact_certificate.py). Here is the sign argument and the checks that certify the entire domain. Put $D=(t+1)(2-t)(1-2t)$ and $P=33DG-112D$. On each listed polygon, the signs of $kL+1$, $kL-t$, and $kL-(1-t)$ at its vertices fix a common branch for each $k=-3,\ldots,4$ throughout the polygon. The four possible contributions to $DG$ are $D$, $D-(kL+1)^2(1-2t)$, $(1-t-kL)^2(t+1)$, and $0$. Summing gives the listed polynomial. The all-upper cell gives the identity $P=(t+1)[12(11L+t-1)^2+28(t+1)^2]$. On the other cells substitute $(t,L)=A+u(B-A)+v(C-A)$ on each listed triangle. If the result is $\sum p_{ab}u^av^b$, its degree-three Bernstein coefficient at $(i,j)$ is $\sum_{a\le i,\ b\le j}p_{ab}\binom ia\binom jb/[\binom3{a+b}\binom{a+b}a]$. This follows by expressing each monomial in the basis $3!u^iv^j(1-u-v)^{3-i-j}/[i!j!(3-i-j)!]$. Every one of the 420 recomputed coefficients is nonnegative, which gives $P\ge0$ on all 42 triangles. The exact cover checks are containment, disjoint interiors via zero pairwise intersection area, and equality of areas at both levels (triangles within each polygon, and 35 polygons within the rectangle of area three). The finite unions are closed, so equality of areas precludes any missing point in the relevant full-dimensional polygon or rectangle. Consequently $G\ge112/33$ throughout the open $t$ strip.

For $t=-1$, the only nonsaturated tail is $(2-s)^2/9$. On the five successive $L$ intervals cut at $0,1/3,1/2,2/3,1,2$, sum the saturated constants and active quadratics and minimize on the closed interval. The exact minima are $112/33,157/45,94/27,94/27,31/9$, respectively. The first quadratic is $(44L^2-16L+32)/9$ and attains its minimum at $2/11$. For $t=1/2$ the nonsaturated tail is $1-4(s+1)^2/9$. Its sum is concave on each interval between the breakpoints $0,1/8,1/6,1/4,1/3,1/2,1$, so check their values, respectively $40/9,133/36,287/81,125/36,95/27,31/9,32/9$. Beyond one it is constant at $32/9$. Thus the lower bound includes both endpoint directions and all real tilts. Moving a containing cap to a parallel through-point cap only decreases mass, so the through-point lower bound proves depth at $(3,g)$. In the canonical $t=-1,L=2/11$ directions the centered continuous functional is $3\lambda_i-1$, yielding the caps in the statement. Their thresholds lie strictly between zero and one on every sampled base. Reflection proves the result at $(4,g)$.

For any mark on a nonmiddle base, choose a barycentric coordinate at least $1/3$ and use its upper cap through that mark. Tilt to exclude the farther side of bases and retain at most two whole fibers on the nearer side. The own cap has area at most $4/9$, so the raw depth is at most $22/9$. At a middle base shift the corresponding displayed cap in the coordinate that is at least $1/3$ to the actual mark. This gives mass at most $112/33$. Thus the two center values are global maxima.
