---
fact_id: 4eeaa6f8ed1f9eb3
kind: counterexample
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-pk-w36-coarse-fine-grid-depth-jump
depends_on: ["e4ef1ac154c5d280", "758871f5be736ae1"]
verifier_run: c565b4f8c08e3e79
target_match: null
---

## Source

- [e306d42187c98e53](../candidates/e306d42187c98e53.json), e306d42187c98e53:03 §4, (10)–(12), exact fine-grid lift and depth limit.

## Statement

For each integer $\ell\ge1$ put $\varepsilon=1/\ell$ and $h=1/\ell^2$. Place the triangles $Q_0=\{(v,x):-1\le v\le1,\ |x|\le\varepsilon(v+1)/2\}$ and $Q_1=\{(v,x):-1\le x\le1,\ |v|\le\varepsilon(x+1)/2\}$ at $z=0,1$ and take their convex hull $C_\varepsilon$. Sample this body on $\mathbb Z\times h\mathbb Z\times\mathbb R$ with length weight $h$ per fine fiber. The body is exactly the hull of its sampled trace. Its only nonempty fine fibers at $z=0$ have $v=kh$, $-\ell^2\le k\le\ell^2$, of lengths $\varepsilon(1+kh)$. At $z=1$ they have $v=kh$, $-\ell\le k\le\ell$, of lengths $2-2|k|/\ell$. The two weighted masses are $2/\ell+1/\ell^3$ and $2/\ell$. These normalized fine laws converge weakly to the law of density $(t+1)/4$ on each of $(0,t,0)$ and $(1,0,t)$, $-1\le t\le1$. The maximal normalized closed-halfspace depths of the fine traces tend to $2/9$, while the limiting law has maximum $1/4$ on its mixed support. The discrepancy of normalized fine and coarse cap probabilities at the same $\ell$, uniformly over all closed ambient halfspaces, is at most $1/\ell+1/(4\ell^2)+1/(2\ell^3)\le2/\ell$. The normalized coarse depth lost by rounding the first triangle's centroid to the fine grid is at most $\sqrt2/(2\ell)$ for $\ell\ge2$. After the fixed block map $(z,v,x)\mapsto2\sqrt2(z-1/2,v,x)$ the bodies are between the unit and radius-$3\sqrt2$ balls, and the two base spacings are $2\sqrt2$ and $2\sqrt2/\ell^2$.

## Proof

The only possible coarse sites are $0,1$, where the hull sections are exactly the specified triangles. The fine ranges and lengths follow by solving their inequalities for $x$ at $v=kh$ and include singleton sections of length zero. At $z=0$ the sum of the terms $kh$ cancels, so the weighted sum is $h\varepsilon(2\ell^2+1)=2/\ell+1/\ell^3$. At $z=1$ the sum of $1-|k|/\ell$ over $|k|\le\ell$ is $\ell$, so the weighted sum is $2h\ell=2/\ell$. Every triangle vertex is sampled, since its $v$ coordinate belongs to $\{-1,0,1,-\varepsilon,\varepsilon\}\subset h\mathbb Z$. This proves hull equality. The inverse of the linear coordinate change $(z,k,x)\mapsto(z,hk,x)$ realizes the trace in the standard lattice with two integer coordinates and one continuous coordinate.

The coarse area is $M=4/\ell$, and the sampled weighted mass is $M_f=M+1/\ell^3$. Use the per-set boxed cell estimate in the proof of e4ef1ac154c5d280 with $r=s=1$, $R=1$ and fundamental cell $[-h/2,h/2)$, on the trace of each ambient cut in each triangle. A trace can be a proper closed planar cut, the entire triangle, or empty. All are compact convex subsets of $[-1,1]^2$. The per-fiber absolute error is at most $h(2+h)$. Consequently the normalized discrepancy is at most
$$
\frac{4h+2h^2+1/\ell^3}{M_f}\le\frac1\ell+\frac1{4\ell^2}+\frac1{2\ell^3}\le\frac2\ell.
$$
Here the additional $1/\ell^3$ bounds the error from using the distinct totals, since coarse cap mass is at most $M$.

For weak convergence, apply the same cell sandwich without a cap. In each triangle let $U$ be the union of horizontal length-$h$ cells paired with the sampled vertical intervals. It lies between the erosion and the dilation of the triangle by the horizontal segment $[-h/2,h/2]$ up to null sets. Both operations change each horizontal section length by at most $h$, and the $x$ projection has length at most two. Thus the symmetric difference of $U$ with the triangle has area at most $4h$. Integrating a continuous test against the cell law instead of the sampled law changes the normalized integral by at most its modulus of continuity at $h/2$. Comparing the two cell laws with the two coarse areas costs at most $(8h+1/\ell^3)\lVert\phi\rVert_\infty/M_f$ using their separate normalizations. These errors tend to zero, and 758871f5be736ae1 gives the coarse weak limit and its depth maximum.

The same accepted fact gives the coarse maximum $2/9$ at each $\ell$, achieved at the ordinary centroid of either isolated triangle. The centroid of $Q_0$ is $(1/3,0)$. Its nearest-grid rounding in $v$ is feasible for $\ell\ge2$. To compare depths in the same coarse fiber, shift each through-mark halfspace parallel to itself between the two marks. A nonzero continuous normal may be scaled to unit length and then the change in threshold is at most the distance between the marks. Each planar section along the shifted line has length at most $2\sqrt2$, the diameter of the containing square. Summing both fibers and dividing by $M$ gives the uniform depth Lipschitz bound $\sqrt2\ell$ in that coarse fiber. Pure base cuts have unchanged mass. The rounding distance is at most $h/2$, giving the claimed loss. Taking infima over the same containing ambient cuts bounds the same-point depth discrepancy by the normalized cap discrepancy. All fine marks are coarse-feasible, and the rounded centroid supplies the reverse limiting bound. This proves the fine limit.

Both triangles contain the respective limiting segments, whose hull has the four facet planes $\pm v=1-z$, $\pm x=z$ at distance $1/(2\sqrt2)$ from $(1/2,0,0)$. The box $[0,1]\times[-1,1]^2$ lies within radius $3/2$ of that center. These inclusions give the stated normalization under the fixed map, whose base spacings follow by scaling. An invertible affine map takes closed halfspaces to closed halfspaces and multiplies all fine lengths by a common constant, so normalized depths are invariant.
