---
fact_id: cfd6eac856c3c0a3
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-binary-jensen-filter-height-slice-helly-bound
depends_on: []
verifier_run: 5c46980b59657387
target_match: null
---

## Source

- [a67ad6a5110953aa](../candidates/a67ad6a5110953aa.json), a67ad6a5110953aa:01 §1, (1)–(2) and actual fine sampling.

## Statement

Let $P$ be a finite subset of a real vector space and let $g:P\to\mathbb R^r$ preserve every convex combination whose mean lies in $P$. Write $G=\{(p,g(p)):p\in P\}$. For each $a\in\mathbb Z^r$ let $S_a=G\cap\{u=a\}$ and let $T$ be the nonempty union of the occupied slices, whose indices form $A$. For relative Helly numbers of finite convex traces,
$$
h(T)\le\sum_{a\in A}h(S_a)\le |A|h(P).
$$
If each height coordinate takes at most two values on $T$, then $h(T)\le2^rh(P)$. If $P=\operatorname{conv}(P)\cap\mathbb Z^k$, then $\operatorname{conv}(T)\cap\mathbb Z^{k+r}=T$, in particular for rational $g$. An intrinsic lattice chart uses the inherited integer lattice in the affine hull of $T$.

## Proof

For any subset $Q\subseteq P$, the graph points in the convex hull of the graph over $Q$ correspond exactly to the points of $P\cap\operatorname{conv}Q$. Projection gives one direction and preservation of the anchored combination gives the other. A subset of a finite source is the trace of a convex set exactly when its convex hull has that same source trace. This also holds for the empty trace using the empty convex set. Thus the relative convex-trace families on $P$ and on $G$ are isomorphic, and $h(G)=h(P)$.

For a finite source $F$ and convex set $D$ with $F\cap D\ne\varnothing$, append $D$ to a family whose intersection misses $F\cap D$. A Helly certificate on $F$ then gives at most $h(F)$ members of the original family whose intersection misses $F\cap D$, by discarding $D$ if it was selected. Hence $h(S_a)\le h(G)$ for every occupied affine height slice. For any family whose intersection misses $T$, take one exclusion certificate for each $S_a$ and unite their indices. Its size is at most the sum of the slice Helly numbers. When each coordinate has at most two possible values, there are at most $2^r$ occupied height vectors.

If $(p,a)$ is an integer point of $\operatorname{conv}(T)$, projection puts $p$ in $\operatorname{conv}P\cap\mathbb Z^k=P$. In any representation by members of $T$, the height mean is forced by the anchored condition to equal $g(p)$. Since $a$ is integral, $(p,a)\in T$. The reverse inclusion is immediate. The inherited affine lattice is $\operatorname{aff}(T)\cap\mathbb Z^{k+r}$, which is nonempty and spans the affine hull because $T$ consists of integer points.
