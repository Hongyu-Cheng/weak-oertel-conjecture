---
fact_id: ee6af6fed42c205f
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-pk-w35-roofs-cover-midpoint
depends_on: []
verifier_run: 7591df43c595357c
target_match: null
---

## Source

- [92518b410f30446b](../candidates/92518b410f30446b.json), 92518b410f30446b:01 §§1–2, hypotheses 1–2.

## Statement

Let $A,B,K$ be full-dimensional compact convex bodies in $\mathbb R^d$ with $(A+B)/2\subseteq K$. Let finitely many closed halfspaces $H_i$ cover $K$, with both endpoint caps of positive $d$-volume for every $i$. If
$$
|K\cap H_i|^{1/d}=\frac{|A\cap H_i|^{1/d}+|B\cap H_i|^{1/d}}{2}
$$
for every $i$, then $K=(A+B)/2$ and $K\cap H_i=((A\cap H_i)+(B\cap H_i))/2$ for every $i$. Halfspaces through a common point whose normals admit a positive dependence supply such a cover.

## Proof

Let $D=(A+B)/2$. For each $i$ the Minkowski midpoint of the endpoint caps lies in $D\cap H_i\subseteq K\cap H_i$ by convexity. Brunn–Minkowski on the positive endpoint caps and the assumed equality give the same positive volume to the two ends of this inclusion chain. A proper compact convex subset of a full-dimensional compact convex body has strictly smaller volume. Indeed, separate an outside point from the closed subset and move it a small distance toward an interior point of the larger body, then take a small interior ball still beyond the separating plane. Thus all three cap sets coincide. Their union gives $K\subseteq D$ and the original containment gives equality. For through-point halfspaces with a positive dependence, the margins cannot all be strictly negative because their positively weighted sum is zero. This proves the cover assertion.
