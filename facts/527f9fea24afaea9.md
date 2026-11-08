---
fact_id: 527f9fea24afaea9
kind: counterexample
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-partial-schwarz-intrinsic-length-defect
depends_on: []
verifier_run: df4ed3ddfd91547a
target_match: null
---

## Source

- [5f965fa405cfb1cb](../candidates/5f965fa405cfb1cb.json), 5f965fa405cfb1cb:03 §5, two integer segments.

## Statement

In $\mathbb R\times\mathbb R^2$ with continuous coordinates $(v,w)$, let $C$ be the convex hull of $\{0\}\times\{(s,s):|s|\le1\}$ and $\{1\}\times\{(t,0):|t|\le1\}$. It is full-dimensional and its only integer fibers have intrinsic lengths $2\sqrt2$ and $2$. Replacing each real $w$-slice at fixed $(z,v)$ by a centered interval of the same one-dimensional volume gives a convex body whose two integer fibers both have intrinsic length $2$. The normalized intrinsic fiber weights change.

## Proof

The two segment directions $(0,1,1)$ and $(0,1,0)$ together with the base difference $(1,0,0)$ are linearly independent. The projection onto $z$ is $[0,1]$, and each extreme-base fiber is exactly its generating segment. Their Euclidean lengths are $2\sqrt2$ and $2$.

At $0\le z\le1$, write the continuous coordinates as $((1-z)s+zt,(1-z)s)$ with $s,t\in[-1,1]$. Thus the $w$-slice above $(z,v)$ is the interval $[-(1-z),1-z]\cap[v-z,v+z]$ for $|v|\le1$. Its half-length is nonnegative, concave and upper semicontinuous on the rectangle of these $(z,v)$, since the upper endpoint is a minimum of affine functions and the lower endpoint a maximum of affine functions. Centered intervals of these half-lengths therefore form a compact convex body with interior. At $z=0$ and $z=1$ each original nonempty $w$-slice is a singleton, so its replacement is $\{0\}$. Both new integer fibers are $[-1,1]\times\{0\}$.
