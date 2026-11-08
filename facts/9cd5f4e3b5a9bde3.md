---
fact_id: 9cd5f4e3b5a9bde3
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-pk-intake-exact-helly-cost-of-the-nine-point-rank-obstruction
depends_on: ["1124d408b8e60579", "bee3cc8e50a0dcea", "3d5f56b513c21fc4"]
verifier_run: dee3a970f0379e2a
target_match: null
---

## Source

- [c7ae7f430666e631](../candidates/c7ae7f430666e631.json), c7ae7f430666e631:02 §3, (7)–(8).

## Statement

Let $P$ be the lattice set of the convex hull of $a=(0,0,1)$, $b=(0,0,3)$, $d=(0,2,1)$, $f=(1,2,0)$ and $h=(2,0,0)$, and put $P_1=P\setminus\{f\}$. Then the relative Helly numbers for finite convex families are $h(P_1)=5$, $h(\{f\})=1$ and $h(P)=6$. For any finite nonempty site set $S$, its relative Helly number is the largest cardinality of a nonempty $W\subset S$ for which
$$
S\cap\bigcap_{w\in W}\operatorname{conv}(W\setminus\{w\})=\varnothing.
$$
Here $\operatorname{conv}(\varnothing)=\varnothing$.

## Proof

In a minimal finite infeasible family $C_1,\ldots,C_m$ relative to $S$, choose a witness $w_i\in S$ after deleting each $C_i$. Each witness lies outside its deleted set and in every other one, so the witnesses are distinct. For $W=\{w_1,\ldots,w_m\}$, each deletion hull $\operatorname{conv}(W\setminus\{w_i\})$ lies in $C_i$. This proves one direction of the criterion. Conversely, when the displayed intersection misses $S$, its deletion hulls form an infeasible family, and removing the hull indexed by $w$ leaves $w$ in all the others. This proves the criterion, including singletons.

By the finite-set witness lemma proved in bee3cc8e50a0dcea, for a finite set $S$ the relative Helly number is at most the largest size of an empty vertex set, meaning a subset $W$ whose points are vertices of its hull and for which $S\cap\operatorname{conv}(W)=W$. Apply this to the eight-point component given by the preceding nine-point dependence-rank counterexample. An empty vertex set there cannot contain both endpoints of any of the pairs $ab,ad,bd,eh$: the respective midpoints $e,j,t,v$ belong to $P_1$, and if included would not be vertices, while if excluded they would violate emptiness. Thus at most one of $a,b,d$ is chosen and at most one of $e,h$ is chosen, leaving at most five of the eight points. For the reverse inequality let $W=\{a,e,j,t,v\}$. Its face at $y=0$ is the noncollinear triangle $a,e,v$ and at $y=1$ its face is the segment $j,t$, so all five are vertices. The omitted sites $b,d,h$ are excluded by their coordinates $z=3,y=2,x=2$, respectively, beyond the corresponding coordinate maxima on $W$. Hence $W$ is an empty vertex set; its deletion hulls satisfy the criterion, giving $h(P_1)=5$.

The relative Helly number on a singleton is one. The computed components are exactly the anchored components to which the Helly additivity theorem 3d5f56b513c21fc4 applies, so $h(P)=5+1=6$.
