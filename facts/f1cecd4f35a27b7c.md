---
fact_id: f1cecd4f35a27b7c
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-pointed-exposed-face-retained-cap
depends_on: ["d6e28c710623b1e1", "efa4558174ce60cf"]
verifier_run: dade02964f378e4d
target_match: null
---

## Source

- [c8365ce16304e154](../candidates/c8365ce16304e154.json), c8365ce16304e154:03 §3, (10) and the three following proof paragraphs.
- [e70b63e0e6efe01c](../candidates/e70b63e0e6efe01c.json), §7, (19)–(21), exposed-face geometry only.

## Statement

Let $K\subset\mathbb R^m\times\mathbb R^k$ be a compact full-dimensional convex body with exposed $m$-face $K\cap(\mathbb R^m\times\{0\})=F\times\{0\}$. Suppose $Q=\operatorname{cone}(\pi K)$ for the normal projection is closed and pointed, and fix $x\in\operatorname{relint}F$, $v\in\operatorname{int}Q$. Use singleton counting measure if $m=0$. For all sufficiently small $\delta>0$ the mark $(x,\delta v)$ is interior. With $B,a,h,n_v,J_*(v)$ as in the product retained-cap theorem, the maximum dominated mass $T_K$ of the prescribed centroid satisfies
$$
\lim_{\delta\downarrow0}\delta^{-k}T_K(x,\delta v)
=\frac{(k+1)^k}{k!\,k^k}J_*(v)B.
$$
After normal dilation by $\delta^{-1}$, every choice of minimizing hinge parameters converges to $((k+1)a,-k n_v)$, using signed coefficients in the tangent and normal variables. The maximizing indicators converge in $L^1$ with first moments to the product cap, and the normalized densities and tangential marginals converge in $L^1$, the latter to $h^k/B$.

## Proof

Write $K_\delta=\{(z,q):(z,\delta q)\in K\}$ and $D$ for the fixed compact tangential projection. For each $q=s w\in Q$ with $(a',w)\in K$, its section contains $(1-\delta s)F+\delta s a'$ for $\delta s\le1$. At $q=0$ it contains $F$. Each fixed compact subset of $\operatorname{relint}F$ therefore lies in the section for sufficiently small $\delta$. Finitely many such $q$'s whose convex hull contains a small ball about $v$ give a fixed source ball by convexity. At bounded $|q|$, compactness implies that all the tangential coordinates in $K_\delta$ approach $F$ uniformly, since any subsequential limit in the undilated body lies at normal height zero. Thus the indicators converge almost everywhere on $D\times Q$ to the product indicators. This uses the actual projected cone and counts the tangent point with mass one if $m=0$.

By compact retained-cap duality, on each $K_\delta$ the actual maximum mass is the attained minimum hinge objective at $(x,v)$, and each minimizing hinge defines the maximizing cap. The source ball gives a coercive lower bound $c|\theta|$ on the hinge integrals. An affine hinge with zero tangent parameter and any strictly negative dual normal coefficient has bounded positive region on $D\times Q$; testing it bounds the minima above. Along any parameter-convergent subsequence, Fatou bounds the product hinge integral of the limit by the limit inferior. A finite product objective has strictly negative dual normal coefficient by the product theorem, and is at least its minimum. Conversely the fixed product optimum has bounded positive region on $D\times Q$, so its objectives converge by dominated convergence to the product minimum. Product uniqueness gives convergence of every sequence of optimizers. The original mass is multiplied by $\delta^k$ upon undoing dilation.

The limiting negative normal coefficient is strictly dual, so for small $\delta$ every minimizing hinge has positive region in one bounded normal range over $D$. The limiting cutting plane is null. Convergence of the affine parameters and almost-everywhere body convergence give cap indicator convergence there, and bounded support gives $L^1$ and first-moment convergence. The limiting volume is positive, so normalization and marginalization give the asserted density limits.
