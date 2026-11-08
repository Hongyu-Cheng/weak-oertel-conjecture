---
fact_id: ce6f5ea7607bbbd2
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-parity-midpoint-transport-simultaneous-density-and-cap
depends_on: ["486fe778f838d99d"]
verifier_run: eeb2bb54140d2900
target_match: null
---

## Source

- [9af97e78b545b0b8](../candidates/9af97e78b545b0b8.json), 9af97e78b545b0b8:02 Statement (1)–(2) and §2, (3); §4 scope.

## Statement

Let $C\subset\mathbb R^n\times\mathbb R^d$ be a compact convex body with $n,d\ge1$ and positive mixed volume measure $\mu$. Write $K_z=C_z$, $a_z=|K_z|_d$, and for each positive-mass parity class $r$ write $\mu_r$ for the restriction, $I_r$ for its positive-volume bases, and $M_r=\sum_{z\in I_r}a_z$. Let $p$ be the number of these classes. In class $r$, choose ordered bases $z,w$ independently with probabilities $a_z/M_r,a_w/M_r$, and choose a coupling of the continuous uniform laws on $K_z,K_w$ conditional on those bases. The couplings can be chosen so that the actual ambient midpoint law $\eta_r$, given total mass $M_r$, satisfies
$$
\eta_r\le\mu,\qquad
\int y\,d\eta_r(y)=\int y\,d\mu_r(y),\qquad
\eta_r(H)\le2\mu_r(H)
$$
for every closed ambient halfspace $H$. The pooled law $\eta=\sum_r\eta_r$ has the original mass and centroid, satisfies $\eta\le p\mu\le2^n\mu$, and obeys $\eta(H)\le2\mu(H)$ for all such $H$.

## Proof

For positive-volume compact convex $A,B$ of volumes $a,b$, the transport constructed in accepted fact 486fe778f838d99d pushes the uniform probability on $A$ to that on $B$ and is coupled to its input. Apply its midpoint construction at parameter $1/2$, with containing body $(A+B)/2$. Its midpoint density is bounded by $((a^{1/d}+b^{1/d})/2)^{-d}\le1/\sqrt{ab}$ by the arithmetic–geometric mean inequality. Every positive-volume $K_z$ is such a body.

Use this coupling separately for each ordered pair $(z,w)$ in $I_r^2$. The joint law of mass $M_r$ has both full marginals equal to $\mu_r$. The first base marginal gives mass $a_z$ to $z$ and its continuous marginal is uniform on $K_z$, and the same holds for the second. Taking the midpoint preserves total mass and averages the first moments, giving the stated first moment. Parity gives an integer midpoint base, and convexity places the midpoint in $C$. For a closed halfspace $H$, if a midpoint lies in $H$, at least one endpoint lies in $H$ because the open complement is convex. Integrating the indicator inequality gives $\eta_r(H)\le2\mu_r(H)$, also when a whole boundary fiber is counted.

At a fixed output base $k$, the pair $(z,w)$ with $z+w=2k$ has total mass $a_z a_w/M_r$, so its density there is at most $\sqrt{a_z a_w}/M_r$. The subset of $I_r$ consisting of $z$ with $2k-z\in I_r$ is invariant under $z\mapsto 2k-z$. Cauchy–Schwarz gives
$$
\frac{1}{M_r}\sum_{\substack{z\in I_r\\2k-z\in I_r}}\sqrt{a_z a_{2k-z}}
\le\frac{1}{M_r}\sum_{\substack{z\in I_r\\2k-z\in I_r}}a_z
\le1.
$$
Each term is supported in $K_k$ by convexity. Thus $\eta_r\le\mu$ on the full mixed set. Summing the mass, moment, density and cap conclusions proves the pooled assertions.
