---
fact_id: 95dab3d4efaa95c1
kind: counterexample
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-affine-interval-critical-residual-row-gap
depends_on: ["c680a307d3f26cec"]
verifier_run: dc3a4f906834c92e
target_match: null
---

## Source

- [8426c7487ce19740](../candidates/8426c7487ce19740.json), 8426c7487ce19740:02 §5, (6)–(9), exact critical cap menu and every KKT row of the specified cover.

## Statement

Let $C=\{(z,x):|z|\le1,\ |x|\le3/4+z/4\}$. It has three positive integer fibers, of lengths $(1,3/2,2)$ and total $M=9/2$, all strictly smaller than $M/2$. Its unique global deepest mixed point is $(0,0)$, with raw depth $Q=7/4$ and normalized depth $7/18$. Every critical closed containing cap there is $H_\pm(L)=\{\pm x-Lz\ge0\}$ for $L\ge1$, and has residual lengths $(0,3/4,2)$.

The four caps $H_\pm(2)$ and $G_\pm=\{\pm x+4(z-1)\ge0\}$ form a cover with masses at most $Q$. The least one-cap residual obstacle array is $e=(0,3/4,1)$. The program $\min (h_-+h_0+h_+)$ subject to $h\ge e$ and $h_-+h_+\ge2h_0$ has optimum $9/4$. Every primal/KKT choice gives the same terminal row, uniform on the three sites. In that row each critical cap has original residual-root mean $11/12>3/4$ at the source, gap $1/6$, while the whole-fiber comparison is equality and the own captured fraction is $\gamma_1=1/2$.

## Proof

The actual fibers follow from the displayed affine half-width; in particular the middle interval is exactly the endpoint Minkowski midpoint. The accepted three-interval depth profile with endpoint lengths $a=1,b=2$, middle length $U=3/2$ and centered shift zero gives middle maximum $U/2+a=7/4$ at its unique center and endpoint maxima $a/2=1/2$, $b/2=1$. Thus the center is uniquely globally deepest. The nonheaviness and normalized depth follow from the displayed lengths.

For the exact menu, normalize a nonvertical cap through $(0,0)$ to $x+az\ge0$, reflecting $x$ if needed. Its middle mass is $3/4$. With $T_R(t)=|[-R,R]\cap[t,\infty)|$, its outside mass is
$$
T_{1/2}(a)+T_1(-a)=2-[T_1(a)-T_{1/2}(a)]\ge1 .
$$
Equality holds precisely when the tail at $a$ captures both pieces of $[-1,1]\setminus[-1/2,1/2]$ in full length, that is, $a\le-1$. Through-center pure-base caps capture the full middle and at least one endpoint, giving mass at least $5/2$. A nonvertical cap containing the center strictly gains strictly positive middle length over its parallel through-center cap, and cannot lose outside mass. Strictly containing pure-base caps also contain their through-center translates. This proves the claimed complete menu, including $L=1$ with a tangent trace of zero length.

The two $H$ caps cover bases $-1,0$, each of mass $Q$, and the two $G$ caps cover the right fiber, each of mass $1$. Every $G$ misses the first two fibers, and every $H$ misses the right fiber. Taking the smallest residual per site gives $e$. The program has cost at least $3h_0\ge9/4$, attained at $(1/2,3/4,1)$. Thus every optimum satisfies $h_0=3/4$, $h_-+h_+=3/2$. At least one endpoint obstacle is slack, as they sum to $1$. If $t\ge0$ denotes the multiplier of $h_-+h_+\ge2h_0$ and $\lambda_i$ the obstacle multipliers, KKT stationarity gives $\lambda_-=\lambda_+=1-t$ and $\lambda_0=1+2t$. Complementarity at the slack endpoint forces $t=1$, $\lambda_-=\lambda_+=0$, $\lambda_0=3$. These satisfy KKT at the displayed optimum. In the nonnegative barycentric flow, only the center can send mass, sending $t$ to each endpoint, since these are the only two destinations that can balance at zero. The unit source mass at the center remains there, while the incoming $t=1$ at each endpoint terminates there, yielding terminal masses $(1,1,1)$ and hence the uniform row for every KKT choice.

A critical cap has residual lengths $(0,3/4,2)$, giving the gap $11/12-3/4=1/6$. The same uniform row has whole-length mean $(1+3/2+2)/3=3/2$ and the source captures length $3/4$ of $3/2$, as claimed.
