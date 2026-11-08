---
fact_id: abb6c0fd2ba74ca0
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-parity-witness-forest-affine-anchor-incidence
depends_on: []
verifier_run: 873c98c7027ff9f1
target_match: null
---

## Source

- [d0f838592db846be](../candidates/d0f838592db846be.json), d0f838592db846be:02 Exact orbit and cap consequences, displayed transport T_z and following paragraph; :01 termination portion only.

## Statement

Let $C\subset\mathbb R^{n+d}$ be compact convex and let $J$ be its nonempty lattice projection, meaning the integer bases with nonempty fiber $K_z$. Choose $p_r\in J$ in each parity $r\bmod 2$, and suppose $\operatorname{conv}\{p_r\}\cap\mathbb Z^n=\{p_r\}$. For each root choose $g_r\in K_{p_r}$. Put $z_0=z\in J$, $z_{j+1}=(z_j+p_{[z_j]})/2$, where $[z_j]$ denotes the parity of $z_j$, and stop when $z_k=p_s$. This happens in finitely many steps. For every $x\in K_z$, the point
$$
T_z(x)=2^{-k}x+\sum_{j<k}2^{j-k}g_{[z_j]}
$$
belongs to $K_{p_s}$. For every closed ambient halfspace containing $(p_s,T_z(x))$, it contains $(z,x)$ or at least one of the anchors $(p_{[z_j]},g_{[z_j]})$ used on this path.

## Proof

The map sends $J$ into itself since the midpoint has integer base and the projected body is convex. Write $Q=\operatorname{conv}\{p_r\}$. For a nearest $q\in Q$ to $z_j$, the point $(q+p_{[z_j]})/2$ is in $Q$. Hence each step reduces distance to $Q$ by at least a factor two. The finite set $J$ has a positive minimum among any nonzero distances to $Q$, so the orbit reaches $Q\cap J=\{p_r\}$ and then is fixed.

Iterating the base recurrence yields $p_s=2^{-k}z+\sum_{j<k}2^{j-k}p_{[z_j]}$. The coefficients are positive and sum to one, including the case $k=0$ when the sum is empty. Thus $(p_s,T_z(x))$ is the same convex combination of lifted source and anchor points and belongs to $C$. An affine margin has at the combination the same convex combination of the source and anchor margins. If all of those margins were negative, the resulting margin would also be negative.
