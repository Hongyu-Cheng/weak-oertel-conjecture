---
fact_id: bec43ccaf3ee11c4
kind: counterexample
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-arbitrary-retained-core-superlevel-obstruction
depends_on: []
verifier_run: 9efd4213d92a83c6
target_match: null
---

## Source

- [6ebae89f6484418b](../candidates/6ebae89f6484418b.json), 6ebae89f6484418b:03 §3, nine-site arbitrary retained-core obstruction.

## Statement

For any integer $d\ge1$ and any compact convex $d$-body $J$ of volume one and centroid zero, consider the actual product $[0,8]\times J$ and retain $w_j^{1/d}J$ at each integer base $0\le j\le8$, with $w_j=1$ at $0,1,4,8$ and $w_j=\varepsilon$ elsewhere, where $0<\varepsilon<1/3$. Define $D_j$ as the minimum of the two closed atomic tail weights at $j$, $R_j=\sum_{h\ge1}\min(w_{j-h},w_{j+h})$ with zero extension, and $F_j=D_j+R_j$. Then $F_2=3+2\varepsilon$, $F_3=2+5\varepsilon$, and $F_4=3+6\varepsilon$, so a superlevel of $F$ contains $2,4$ and omits their integer midpoint $3$. All nonempty actual fibers have volume one and all their maximal centered radii equal one.

## Proof

The smaller closed tails at $2,3,4$ have weights $2+\varepsilon,2+2\varepsilon,2+3\varepsilon$, respectively. The nonzero summands of $R_2$ are $\varepsilon,1$; those of $R_3$ are $\varepsilon,\varepsilon,\varepsilon$; those of $R_4$ are $\varepsilon,\varepsilon,\varepsilon,1$. This gives the stated values and $F_3<F_2<F_4$ since $3\varepsilon<1$. Any level in $(F_3,F_2]$ gives the failure. Since $0\in J$ and $w_j\le1$, the specified dilations lie in the actual fibers. Radius one is attainable everywhere and larger radii violate volume containment. The selected radius sequence is not concave: at $2$ and $4$ its radii are $\varepsilon^{1/d}$ and $1$, while the radius at their midpoint $3$ equals $\varepsilon^{1/d}$, strictly below their mean. Thus neither actual fiber-volume weights nor maximal-core radii yield the displayed disconnected trace.
