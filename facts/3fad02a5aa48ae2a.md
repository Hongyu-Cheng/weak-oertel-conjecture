---
fact_id: 3fad02a5aa48ae2a
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-sharp-complete-parity-core
depends_on: ["03bc771bddd39a8a","287cc87c3b427501"]
verifier_run: e3a1236c341391af
target_match: null
---

## Statement

For every $d\ge2$ there exists $\rho_d>0$, independent of $n$, with the following property. Let $n\ge1$ and let $\mathcal C\subset\mathbb R^n\times\mathbb R^d$ be a compact convex body. Put $K_{\mathbf z}=\{\mathbf x:(\mathbf z,\mathbf x)\in\mathcal C\}$. Let $P_0\subset\mathbb Z^n$ contain exactly one representative from each of the $2^n$ parity classes, with $|K_{\mathbf w}|>0$ for every $\mathbf w\in P_0$. Define
$$L=2^n,\qquad V_{\mathbf w}=|K_{\mathbf w}|,\qquad m=\min_{\mathbf w\in P_0}V_{\mathbf w},\qquad E=\sum_{\mathbf z\notin P_0}|K_{\mathbf z}|,\qquad W=\sum_{\mathbf w\in P_0}V_{\mathbf w}+E.$$
If $E\le\rho_d m$, there is $\mathbf p\in\mathcal C\cap(\mathbb Z^n\times\mathbb R^d)$ whose mass in every containing closed ambient halfspace is at least $2^{-n}(d/(d+1))^dW$. Fiber mass is $d$-dimensional volume, so lower-dimensional fibers carry zero mass. One may take $0<\rho_d\le\min\{2^{-d-1},\theta_d\}$, where $\theta_d$ is the constant of accepted fact `287cc87c3b427501`.

No common fiber shape, convex position of $P_0$, or coordinate bound on its representatives is assumed. The small-outside-mass hypothesis is essential to the scope; it is not established for arbitrary bodies, and this argument does not cover $d=1$.

## Proof

Write $\Gamma=(d/(d+1))^d$ and let $\alpha>\Gamma$, $\theta_d>0$ be as in accepted fact `287cc87c3b427501`. Choose $0<\rho_d\le\min\{2^{-d-1},\theta_d\}$. Compactness of the base projection implies that only finitely many integer fibers are nonempty.

**Exact grouping, including null fibers.** For any nonempty outer fiber at $\mathbf p\notin P_0$, let $\mathbf v(\mathbf p)\in P_0$ be its unique same-parity representative, and set $\mathbf w(\mathbf p)=(\mathbf p+\mathbf v(\mathbf p))/2\in\mathbb Z^n$. Choosing any $\mathbf x\in K_{\mathbf p}$, convexity gives $(\mathbf x+K_{\mathbf v(\mathbf p)})/2\subset K_{\mathbf w(\mathbf p)}$. Its volume is at least $2^{-d}m>E$, so this midpoint must lie in $P_0$. This works even if $K_{\mathbf p}$ has zero volume. Every nonempty outer base is therefore $\mathbf p=2\mathbf w-\mathbf v$ with distinct core bases $\mathbf w,\mathbf v$.

The representation is unique: if $2\mathbf w-\mathbf v=2\mathbf w'-\mathbf v'$, then $\mathbf v\equiv\mathbf v'\pmod2$, so the transversal property gives $\mathbf v=\mathbf v'$ and then $\mathbf w=\mathbf w'$. Group positive-volume outer fibers by target $\mathbf w$, and let $E_{\mathbf w}$ be the mass of that group. Then $\sum_{\mathbf w}E_{\mathbf w}=E$. Within one group the partners $\mathbf v=2\mathbf w-\mathbf p$ are distinct and different from $\mathbf w$. Hence the middle fiber, all outer endpoints, and all core partners in that group are distinct actual sources.

If $E=0$, the ordinary centroid of a largest core fiber has mixed depth at least $\Gamma\max V_{\mathbf w}\ge\Gamma W/L$, by fact `03bc771bddd39a8a` and Grünbaum. Suppose $E>0$ and, for contradiction, no actual mixed-integer point achieves $T_*:=\Gamma W/L$. Let $\bar V=L^{-1}\sum V_{\mathbf w}$.

The mixed depth of a point in a core fiber is at least its ordinary absolute depth in that fiber: every containing ambient halfspace traces either a containing continuous halfspace or the whole fiber. Ordinary maximal depth is attained by fact `03bc771bddd39a8a`. Thus failure implies, for every $\mathbf w$,
$$\Gamma V_{\mathbf w}\le D(K_{\mathbf w})V_{\mathbf w}<T_*=\Gamma(\bar V+E/L).$$
Retain one fiber of minimum volume $m$, and sum the strict upper bounds $V_{\mathbf w}<\bar V+E/L$ over the other $L-1$ fibers. This yields
$$\bar V<m+(L-1)E/L,\qquad \max V_{\mathbf w}<m+E,\qquad D(K_{\mathbf w})<\Gamma(1+E/m).$$
Therefore every pair of core volumes has ratio between $(1+\rho_d)^{-1}$ and $1+\rho_d$, and $E_{\mathbf w}/V_{\mathbf w}\le\rho_d$. These estimates contain no factor depending on $L$.

Fix a target group with $E_{\mathbf w}>0$. Take $B=K_{\mathbf w}$, $A_j=K_{\mathbf p}$, and $C_j=K_{\mathbf v(\mathbf p)}$. Convexity gives each midpoint inclusion, and the preceding bounds verify every hypothesis of fact `287cc87c3b427501`. At the point $\mathbf y_{\mathbf w}$ it supplies, any through-$(\mathbf w,\mathbf y_{\mathbf w})$ ambient halfspace with nonzero continuous normal has thresholds $f(\mathbf y_{\mathbf w})+\beta_j$ and $f(\mathbf y_{\mathbf w})-\beta_j$ at each endpoint pair, since their bases average to $\mathbf w$. The lemma allows every list of real offsets, so in particular this actual list induced by one integer normal. Its lower bound is $\Gamma V_{\mathbf w}+\alpha E_{\mathbf w}$. Distinctness established above prevents double counting; unused fibers contribute nonnegative mass. A purely integer through-point cut includes the whole middle fiber and obeys the same bound because $\Gamma+\alpha\theta_d<1$. If $E_{\mathbf w}=0$, use that fiber's ordinary centroid, giving the same bound with zero second term.

The mean of these $L$ actual-point guarantees is
$$\frac{\Gamma\sum_{\mathbf w}V_{\mathbf w}+\alpha E}{L}>\frac{\Gamma W}{L}=T_*.$$
Thus at least one of the constructed points exceeds the assumed unattainable target, a contradiction. This averages lower bounds for different candidate points, not charges to one halfspace.

Finally any containing closed halfspace contains its parallel through-point halfspace. Nonvertical boundary traces have zero $d$-volume on each full-dimensional fiber, while purely integer cuts retain the whole target fiber, including boundary mass. Null outer fibers were used only for the grouping argument and never charged as positive mass. The proof establishes the claimed restricted theorem with $\rho_d$ depending only on $d$.

## External sources

None; the proof is elementary or uses only the declared accepted predecessors.

## Provenance and review method

Atomic normalization of PK contribution `ff31d56304dd901a`. The originals are preserved. Reviewed directly by ChatGPT; the reviewer also edited the normalization. This is `LLM-verified`, not a human review, an independent second-model check, or formal certification. See [the review record](../verifications/e3a1236c341391af.json) and [the scoped review report](../reviews/pk-parity-core-issue2.md).
