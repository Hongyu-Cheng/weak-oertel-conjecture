---
fact_id: e1209ac9a9de7caa
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-seven-base-exact-owned-fiber-local-depth
depends_on: ["e6ed7f0a4aa574cd", "53fe12b742a7608d", "98603e266680b22d"]
verifier_run: d2a49ffca651a203
target_match: null
---

## Source

- [e306f52a74c4defa](../candidates/e306f52a74c4defa.json), §1, (1)–(2), §3, (8)–(10), and §5 census and competitors.
- [501dba519aa398a9](../candidates/501dba519aa398a9.json), §§1–2, (1)–(6), exact shape-independent local and anchor reductions.

## Statement

Let $T=\operatorname{conv}(0,e_1,e_2)$, $V=|T|=1/2$, $g=(1/3,1/3)$, and $\Gamma=4/9$. For $a>0$ and small $t>0$, place $T$ at the four binary bases in two integer dimensions and the same convex body $E_t\subset T$ of area $ta$ at $r_0=(-1,0)$, $p=(-1,1)$ and $p'=(1,-1)$. Their hull has exactly these seven integer fibers and total area $4V+3ta$. Write $q=(0,0)$ and let $A_{7,t}(y)$ be the raw mixed closed-halfspace depth at $(q,y)$. Let $A_{6,t}(y)$ be the corresponding depth after deleting $r_0$ and taking the remaining hull. For unit $u$, let $F_T(y,u)=|T\cap\{u\cdot x\ge u\cdot y\}|$ and let $J_t(u,y)$ be $a$ times the minimum over $s\in\mathbb R$ of the two tail probabilities of the uniform law on $E_t$ at opposite shifts $u\cdot y+s$ and $u\cdot y-s$. Then
$$
A_{6,t}(y)=\min_{\lVert u\rVert=1}\,[F_T(y,u)+tJ_t(u,y)].
$$
For some fixed neighborhood of $g$ in $T$ and all sufficiently small $t$, $A_{7,t}(y)=ta+A_{6,t}(y)$ there. Both local maximizing sets on $q$ are attained, lie within $O(t)$ of $g$ uniformly, and coincide for small $t$. The raw maxima at the other three core bases $(0,1),(1,0),(1,1)$ are $\Gamma V+ta,\Gamma V+ta,\Gamma V$, respectively. Every mark on an added fiber has raw depth at most $ta$.

In particular the result applies to $E_t=\{g+s(1,-1)+tr(-1/2,-1/2):|s|\le L,\ |r+H/2|\le H\}$ with $0<L<1/3$, $H>0$, and $a=4LH$. It has area $ta$ and lies in $\operatorname{int}T$ when $tH/4<1/3-L$ and $3tH/2<1/3$.

## Proof

The base hull is the quadrilateral $-1\le z_1\le1$, $z_2\le1$, $z_1+2z_2\ge-1$. Its integer rows at $z_1=-1,0,1$ contain respectively $z_2\in\{0,1\},\{0,1\},\{-1,0,1\}$. The three added sites uniquely maximize respectively $-2z_1-z_2$, $-z_1+z_2$ and $z_1-2z_2$; their hull fibers remain $E_t$. All continuous coordinates lie in $T$, and a full $T$ is placed at every core site. The total area follows. In the stated strip the determinant of the linear map from $(s,r)$ is $t$ in absolute value and the parameter rectangle has area $4LH$. Its coordinates are positive because $tr\le tH/2$ and $L+tH/4<1/3$. Their sum is $2/3-tr\le 2/3+3tH/2<1$.

The six-base identity and attainment are fact e6ed7f0a4aa574cd, with the two added bodies both $E_t$ and their volume coefficients both $a$. Its proof realizes a minimizing shift $|s|\le D+1$, $D=\operatorname{diam}(T)$, by base coefficients $\beta_1=-K+s/2,\ \beta_2=-K-s/2$ with $K=D+(D+1)/2+1$. In the seven-base family that same cap includes the entire $r_0$ fiber because $-\beta_1\ge D+1$, and excludes the three unwanted core fibers. Therefore $A_{7,t}\le ta+A_{6,t}\le\Gamma V+2ta$ everywhere in $T$. The second inequality follows by testing a canonical own cap with barycentric threshold at least $1/3$ and a saturated shift with cost $a$.

Tighten each containing cap to the through-mark cap. If a nonvertical such cap fails to capture all of $r_0$, its threshold there exceeds $\min_T u\cdot x$. The opposite base $(1,0)$ has the reflected threshold below $2u\cdot y-\min_T u\cdot x$. Thus the own and opposite core costs alone are at least
$$
F_T(y,u)+|T\cap\{u\cdot x\ge 2u\cdot y-\min_T u\cdot x\}|.
$$
Fact 53fe12b742a7608d bounds this sum at $g$ below by $(\Gamma+\rho_2)V$ with $\rho_2>0$. The cap areas are continuous, including at support thresholds, since the boundaries have zero area; compactness of the unit circle gives a fixed neighborhood where the sum exceeds $(\Gamma+\rho_2/2)V$. Pure-base through-caps have mass at least $V$. For small $t$, both costs exceed the constructed upper bound there. Every other through-cap captures all of $r_0$ and has six-base cost at least $A_{6,t}(y)$. This proves the local identity.

The six-base maximum is attained by the predecessor and the seven-base one by upper semicontinuity of depth on compact $T$: for any cap of mass strictly below a given value, move its plane slightly outward to contain a neighborhood of its mark while retaining that strict mass bound by continuity from above. At $g$ both depths are at least $\Gamma V$ from the own triangle, by fact 53fe12b742a7608d (a pure-base cap contains the whole own fiber). The canonical caps with saturated pair cost give, for each barycentric coordinate $\lambda_i$, depth at most $V(1-\lambda_i(y))^2+2ta$ in either family. At a maximizer this implies $\lambda_i(y)\le1/3+O(t)$, and the sum of the three coordinates gives the reverse bound uniformly. Hence all maximizers lie in the neighborhood of the local identity for small $t$, and their sets coincide.

At $(0,1)$ the bases $p,(0,1),(1,1)$ give the collinear three-fiber subset $E_t,T,T$. At $(1,0)$ use $p',(1,0),(1,1)$. The three-fiber centroid lower bound of fact 98603e266680b22d applies to each subset when $ta\le\rho_2 V$, with its base coordinate affinely identified with $-1,0,1$. Restriction of a containing ambient cap to the subset's affine span is either a containing halfspace or the whole subset. This gives lower bound $\Gamma V+ta$ at each centroid. For the matching upper caps subtract twice the base functions $z_1+2(1-z_2)$ and $1-z_1+z_2$, respectively, from $\lambda_i(x)$ and use threshold $1/3$. Each function is zero at its anchor, $-1$ at the designated added base, and at least one on all other sites. Hence the caps take exactly the designated whole $E_t$ and the own canonical cap and cover the anchor fiber over the three $i$. For $(1,1)$ the base function $2-z_1-z_2$ isolates its own canonical caps, and the own triangle bounds its centroid depth below by $\Gamma V$. The exposing pure-base caps on the three added sites have mass $ta$.
