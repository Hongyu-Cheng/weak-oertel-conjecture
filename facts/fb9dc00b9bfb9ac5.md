---
fact_id: fb9dc00b9bfb9ac5
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-strict-budget-contact-enlargement
depends_on: ["88a6579e3b48bcdc"]
verifier_run: b64a8491d5d71d81
target_match: null
---

## Source

- [f8f6582d5c261f3e](../candidates/f8f6582d5c261f3e.json), f8f6582d5c261f3e:02 §1, final paragraph, strict-budget lattice-free enlargement.

## Statement

Assume the full-size case $k=N+1$ of the first relaxed contact theorem and $N=n+d$, $n\ge1$. Suppose the original caps each have mixed mass strictly below a common bound, with mixed mass measured on $C\cap(\mathbb Z^n\times\mathbb R^d)$. By an arbitrarily small displacement of the first contact $q$ in the base variables and a sufficiently small further common relaxation, one obtains a bounded full-dimensional complementary simplex contained in $\operatorname{int} C$ and disjoint from $\mathbb Z^n\times\mathbb R^d$. The resulting caps have the original normals and still satisfy the strict bound.

## Proof

The first contact theorem gives $q\in\operatorname{int} C$ and $a_i\cdot q=b_i+\delta_0$ with $\delta_0>0$. Move to a point $q'$ still in $\operatorname{int} C$ whose base is outside $\mathbb Z^n$. Choose the move small enough that all $a_i\cdot q'>b_i$. With new thresholds $b_i'=a_i\cdot q'+h$, $h>0$, the complementary polytope is $q'+hD$, where $D=\{v:a_i\cdot v\le1\ \forall i\}$. The map $v\mapsto(\lambda_i(1-a_i\cdot v)/\sum_j\lambda_j)_i$ bijects $D$ with the standard simplex by the rank and balance of the normals. Thus $D$ is bounded and full-dimensional. The positive distances from $q'$ to the closed lattice cylinder and the complement of $\operatorname{int} C$ allow $h$ small enough for both geometric conditions. Every new cap is a subset of its original cap because $b_i'>b_i$, giving the claimed budget.
