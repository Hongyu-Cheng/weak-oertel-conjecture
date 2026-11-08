---
fact_id: 2b1d1b6b1f3c7eeb
kind: counterexample
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-pk-w34-reflection-rectangular-center-obstruction
depends_on: []
verifier_run: 7976e9f85a0d0f9c
target_match: null
---

## Source

- [5e107e24de91c307](../candidates/5e107e24de91c307.json), 5e107e24de91c307:01 §§1–2 (1)–(3), including binary and continuous products.
- [5e107e24de91c307](../candidates/5e107e24de91c307.json), 5e107e24de91c307:09 §9 (18), both bounds.

## Statement

Let $B=[-1/2,1/2]^2$, $A=B/10$, and $K=(11/20)B+[0,279/220]e_1$. They are the exact integer fibers of their lifted convex hull at bases $-1,0,1$. Each fiber is centrally symmetric and has area below $M/2$, where $M=201/100$ is their summed area. At the three respective fiber symmetry centers the raw mixed depths are at most $1/200,1/2,1/2$, all below $M/4=201/400$. The right center has raw depth exactly $1/2>\Gamma_2 M/2=67/150$. Products with a volume-one continuous box and a binary integer cube give a failure of the symmetry-center rule at $M_{\rm total}/2^{n+1}=201/400$ for every $n\ge1,d\ge2$, with an actual mark of raw depth at least $1/2$.

In the original planar-fiber body the unrestricted maximum raw depth is exactly $101/200$, attained at $(0,5/8,0)$. It exceeds $M/4$ by $1/400$. All caps use original mixed volume and are closed.

## Proof

Write $H=11/20$, $l=-11/40$, $h=679/440$, so $K=[l,h]\times[-H/2,H/2]$. Its area is $H(h-l)=1$, and its center is $(279/440,0)$. The endpoint areas are $1/100,1$ and both centers are zero. The midpoint $(A+B)/2=(11/20)B$ lies in $K$, so equal endpoint weights in a convex combination at base zero yield exactly the stated middle fiber. The endpoint fibers are exact by extremality and the base projection is $[-1,1]$. These fibers have interior and the ambient hull is full-dimensional.

The cut $x_1\ge279/440$ captures half of $K$ and no endpoints since $279/440>1/2$. The cuts $x_1-2(z+1)\ge0$ and $x_1+2(z-1)\ge0$ at the respective endpoints bisect their own fibers and exclude both other fibers because $h<2$. Every cap containing the right center captures at least half its own area. This gives the claimed depths and the center graph is nonaffine. Adding a unit continuous box leaves the displayed caps' masses unchanged. Adding $[0,1]^{n-1}$ in integer coordinates gives $2^{n-1}$ sampled blocks and multiplies $M$ by that factor. To retain the same bad cap at the center of any chosen block, add a sufficiently large positive multiple of an affine base functional zero at that binary vertex and strictly negative at every other. The finite set of blocks and bounded continuous coordinates ensure that this excludes every other block. The right symmetry center in any block still has own contribution at least $1/2$. The sharp target for these padded bodies is $\Gamma_d M/2\le67/150$ since $(1+1/d)^d$ increases with $d$ (by differentiation of its logarithm as a real function).

For the unrestricted upper bound in the original body, at any $(0,x,y)$ in the middle fiber use the cap $-X+bz\ge-x$ with $b$ sufficiently negative, where $X$ is the first continuous coordinate. This cap captures all of $A$ and excludes $B$, for total $G(x)=H(x-l)+1/100$. If $x\le1/2$ this is at most $349/800<101/200$. If $x>1/2$, the additional option $X\ge x$ has mass $F(x)=H(h-x)$, all from $K$. Since $F(x)+G(x)=101/100$, one of them costs at most $101/200$. At an endpoint any ordinary cap through the point can be isolated by an exposing signed tilt in $z$, which excludes the other bounded fibers. Two opposite ordinary caps through the point sum to the endpoint's area, so depth there is at most $1/2$.

For the lower bound at $(0,5/8,0)$, first consider any nonzero continuous normal $u=(u_1,u_2)$. The middle trace tests a point $1/110$ to the left of the center. Each horizontal line of $K$ has interval length, and translating the threshold by $1/110$ along that line changes the captured length by at most $1/110$. Integration gives own mass at least $1/2-H/110=99/200$. For $u_1\ge0$ the translation only increases that mass. The endpoint traces have thresholds whose average is $(5/8)u_1$. For any $v$ with $v-A\subset B$ and $u\cdot v\ge(5/4)u_1$, each pair $X\in A,v-X\in B$ has nonnegative sum of its two cap margins, so integration over $A$ gives endpoint mass at least $1/100$. For $u_1\le0$ take $v=0$ to obtain total at least $101/200$. For $u_1>0$, the allowed shifts $v$ with $v-A\subset B$ form the square $[-9/20,9/20]^2$. Its support value is at least $(5/4)u_1$ if $r=|u_2|/u_1\ge16/9$, so the total in that range is at least $1/2+1/100$. For $r<16/9<36/11$, the threshold $5/8-(u_2/u_1)Y$ lies inside $[l,h]$ for all $Y\in[-H/2,H/2]$, since $(36/11)H/2=5/8-l\le h-5/8$. Integrating the captured lengths gives own mass exactly $H(h-5/8)=101/200$. A purely integer through-mark cap contains the whole middle fiber. Any containing cap contains its parallel through-mark cap, and $X\ge5/8$ attains the bound.
