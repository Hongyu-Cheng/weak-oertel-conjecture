---
fact_id: dba5cdade881e9ee
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-positive-set-parity-center
depends_on: []
verifier_run: 07bdd514ca124892
target_match: null
---

## Source

- [27d482de82ed9f88](../candidates/27d482de82ed9f88.json), §3, (7) and maximal-threshold argument.

## Statement

Let $\Lambda=c+L$ be an affine lattice and $P=\operatorname{conv}(P)\cap\Lambda$ be finite and nonempty. Assign each $z\in P$ a positive weight $V_z$, let $V(T)=\sum_{z\in T}V_z$, and put $M=V(P)$. Write $k(T)$ for the number of classes of $T$ modulo $2L$ and $k=k(P)$. Let $h:P\to[0,\infty)$ be nonzero and assume $h((z+z')/2)\ge(h(z)+h(z'))/2$ whenever the midpoint belongs to $P$. Suppose $V(T)\le k(T)M/k$ for every nonempty proper closed minor $T=P\cap\operatorname{conv}(T)$ contained in $\{h=0\}$. Then there is $p\in P$ with $h(p)>0$ such that every closed base halfspace containing $p$ has weight at least $M/k$. Allow the whole-base trace, which is the only containing trace in rank zero.

## Proof

Let $U=\{p\in P:h(p)>0\}$ and $\alpha=M/k$. If the conclusion fails, take one closed cap $\{a_i\ge b_i\}$ of weight strictly less than $\alpha$ at each point of $U$, where $a_i$ is an affine base functional. Choose upper thresholds $B_i>\max(b_i,\max_P a_i)$. In the box $b_i\le c_i\le B_i$, impose the condition that every point of $U$ satisfies $a_i(p)\ge c_i$ for some $i$. The condition is closed because the sets of points and indices are finite. It holds at $c=b$, so there is a feasible choice maximizing $\sum_i c_i$.

For every $i$ with $c_i<B_i$ there is a witness $p_i\in U$ with $a_i(p_i)=c_i$ and $a_j(p_i)<c_j$ for all $j\ne i$. Otherwise the points of $U$ that strictly satisfy all the other inequalities have a positive gap $a_i(p)-c_i$, or there are none. A sufficiently small increase in $c_i$ would then preserve feasibility. Let $r$ be the number of nonsaturated indices. The strict trace $T=\{p\in P:a_i(p)<c_i\ \text{for all }i\}$ lies in $\{h=0\}$ and is closed, because the open intersection defining it is convex. As $U\ne\varnothing$, this trace is proper and $r\ge1$. The $r$ nonsaturated closed caps cover $P\setminus T$ and each has weight strictly less than $\alpha$.

Two witnesses of the same parity would have their midpoint in $P$ by lattice completeness. It would be in $U$ by midpoint concavity and would satisfy all strict inequalities by the exclusive equality patterns. The same contradiction follows from a witness and any point of $T$ in its parity class, because the midpoint value is at least half the positive witness value. Therefore $r+k(T)\le k$, taking $k(\varnothing)=0$. The cap cover gives $M-V(T)<r\alpha\le(k-k(T))\alpha$. For empty $T$ this contradicts $M=k\alpha$, and otherwise it contradicts the quota for $T$. In a minor's inherited affine lattice the congruence classes are precisely the old classes restricted to that minor. If a difference of two sites belongs to $2L$, its half also belongs to the direction space of the minor.
