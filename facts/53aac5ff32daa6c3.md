---
fact_id: 53aac5ff32daa6c3
kind: counterexample
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-five-vertex-uniform-interval-target-domination-obstruction
depends_on: []
verifier_run: 3ec133affca88763
target_match: null
---

## Source

- [064f113a153b1a91](../candidates/064f113a153b1a91.json), 064f113a153b1a91:03 A five-vertex rational obstruction, two oblique caps.

## Statement

Let $C=\operatorname{conv}\{(0,0),(3,0),(3,2),(2,4),(0,2)\}\subset\mathbb R_z\times\mathbb R_x$ and let $\mu$ be its normalized summed integer-fiber length. There is no nondegenerate uniform interval law supported on any of its integer fibers with $\nu(H)\le2\mu(H)$ for every closed ambient halfspace $H$.

## Proof

The lower boundary is zero and the upper boundary joins $(0,2),(2,4),(3,2)$. There are exactly four integer bases $0,1,2,3$, with respective fibers $[0,2],[0,3],[0,4],[0,2]$ and total length $11$. Bases $0,1,3$ are excluded by the containing halfspaces $z\le0,z\le1,z\ge3$, of raw masses $2,5,2$. Each has target mass one at its corresponding base but original mass less than $11/2$.

At base $2$ let the target be uniform on $[l,u]\subset[0,4]$, $l<u$, with CDF $F(t)=\min(1,\max(0,at+b))$, $a=1/(u-l)$ and $b=-l/(u-l)\le0$. The closed cap $x\ge-z/2+7/2$ has fiber lengths $(0,0,3/2,0)$. Its threshold at base $2$ is $5/2$, so domination requires $F(5/2)\ge8/11$. The cap $x\le4z-23/5$ has fiber lengths $(0,0,17/5,2)$ and threshold $17/5$ at base $2$, so domination requires $F(17/5)\le54/55$. Nonvertical boundaries carry zero length. Because $5/2<17/5$ and $F$ is nondecreasing, both CDF values are strictly between zero and one. Hence $(5/2)a+b\ge8/11$ and $(17/5)a+b\le54/55$. With $b\le0$ the first gives $a\ge16/55$, while their difference gives $(9/10)a\le14/55$, or $a\le28/99$. The gap $16/55-28/99=4/495$ is positive, which rules out the remaining base.
