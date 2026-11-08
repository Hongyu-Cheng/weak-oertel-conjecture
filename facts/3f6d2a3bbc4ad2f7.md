---
fact_id: 3f6d2a3bbc4ad2f7
kind: counterexample
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-pk-w34-circuits-no-heavy-null-cover
depends_on: ["630af8966ccf85fb", "2efd8d4a7a3af448"]
verifier_run: b131dd4e700cf2bd
target_match: null
---

## Source

- [23964991b201face](../candidates/23964991b201face.json), 23964991b201face:02 Strict no-heavy one-group variant, including rank d.

## Statement

Let $d\ge2$, let $B$ be the unit ball of volume $V$, and let $0<\varepsilon=r^d<1/2$. Take the convex hull of $[0,1]^2\times B$ and $\{(2,1)\}\times rB$ with summed $d$-volume on integer fibers. Every fiber has mass strictly below one quarter of the total, and the raw mixed maximum is $(1/2+\varepsilon)V$, attained uniquely at $((1,1),0)$. The full-dimensional ambient level-$V$ region lies in the maximal lattice-free split $0\le z_2\le1$ and contains the contact $Y=((1/2,0),0)$. There is a supporting lower group of mass-$V$ caps through $Y$, with null sections on all measured fibers and whole-plane coverage exactly at the bases $z_2\le0$. This holds for a rank-one minimal positive circuit and for a rank-$d$ minimal positive circuit. Any vertical halfspace preserving their lower sampled coverage has mass at least $2V$.

## Proof

This body is the reflection in $z_2=1/2$ of the body in 2efd8d4a7a3af448 at $n=2$, which sends the added base $(2,0)$ to $(2,1)$ and the unique deepest base $(1,0)$ to $(1,1)$. This affine transformation maps closed halfspaces bijectively and preserves the fiber volumes. Therefore that fact gives the exact census, total $(4+\varepsilon)V$, strict no-heavy inequality, and exact unique maximum. In particular its three-base row proof includes all oblique halfspaces.

Adding the small ball preserves every old level-$V$ point, because the measure only increases. Thus the old full-dimensional level set and $Y$ remain. The projection lies in the split since the entire convex body does; the split is maximal by the preceding fact. Use the rank-one lower margins there with $M>3+r$. The extra ball misses both caps strictly since the absolute $z_1$ term is $3$ there and $|u\cdot x|\le r$. The support argument by raising threshold still applies and the caps certify depth exactly $V$ at $Y$.

For rank $d$ use the preceding rank-$d$ margins with $M\ge8d+8$. At the extra base they are at most $r\|u_j\|+(3/2)|a_j|-M<0$, so their masses and section status remain unchanged. The proper cap $w\cdot x-2\|w\|z_2\ge0$ also misses the new ball. Its support gives $w\cdot x\le2\|w\|z_2$ on the new level set. For every independent sign choice the margin $\pm u\cdot x\pm2(z_1-1/2)-4z_2$ takes just one bottom ball in volume, misses the new ball since $r+3-4<0$, and supports the new level set by the same inward-shift argument. Averaging the two signs of the continuous term at each fixed sign of the base term gives $|z_1-1/2|\le2z_2$. Each rank-$d$ margin on the level set is therefore at most $(2\|u_j\|+2|a_j|-M)z_2\le0$ and vanishes at $Y$. The whole-plane coverage set still follows from exactly the same margin identities, and preserving its measured coverage still requires both bottom bases.
