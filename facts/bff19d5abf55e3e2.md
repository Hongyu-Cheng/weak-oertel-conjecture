---
fact_id: bff19d5abf55e3e2
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-collision-free-two-family-midpoint-volume
depends_on: []
verifier_run: a854729a9d1b42e1
target_match: null
---

## Source

- [87fbc7e80b2767d9](../candidates/87fbc7e80b2767d9.json), 87fbc7e80b2767d9:01 §1, (1), monotone overlap path.

## Statement

Let $n,d\ge1$. Take finite families of measurable sets $A_u,B_v\subseteq\mathbb R^d$ indexed by $u,v\in\mathbb Z^n$, with positive finite volumes and totals $A=\sum_u|A_u|$ and $B=\sum_v|B_v|$. Suppose each $(A_u+B_v)/2$ is measurable, satisfies Brunn--Minkowski, and lies in a measurable set $C_{u+v}$. Then $\sum_w|C_w|\ge\Phi_d(A,B)$, where $\Phi_d(A,B)=2^{-d}(A^{1/d}+B^{1/d})^d$. More precisely, the positive overlaps $\pi_{uv}$ of the consecutive partitions of $[0,1]$ with lengths $|A_u|/A$ and $|B_v|/B$ in lexicographic index order have distinct index sums $u+v$, and $|C_{u+v}|\ge\pi_{uv}\Phi_d(A,B)$ for each positive overlap.

## Proof

Order the two index lists lexicographically. Give each list its consecutive partition of $[0,1]$ using the stated lengths. In the order of their positive overlap intervals, neither index decreases and at least one increases at every change of pair. Lexicographic order is translation invariant, so the sums increase strictly. The overlap lengths sum to one. Since $\pi_{uv}\le |A_u|/A$ and $\pi_{uv}\le|B_v|/B$, Brunn--Minkowski and homogeneity give
$$
|C_{u+v}|\ge 2^{-d}(|A_u|^{1/d}+|B_v|^{1/d})^d\ge\pi_{uv}\Phi_d(A,B).
$$
Sum over the distinct targets. The positive-volume hypotheses are essential for the two normalized partitions.
