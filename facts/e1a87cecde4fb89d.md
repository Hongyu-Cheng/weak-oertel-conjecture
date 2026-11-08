---
fact_id: e1a87cecde4fb89d
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-fixed-body-retained-mass-strict-quasiconcavity
depends_on: ["efa4558174ce60cf", "669858b8fc253d7c"]
verifier_run: a911198f6b46d416
target_match: null
---

## Source

- [38e8cdfda56d1d3d](../candidates/38e8cdfda56d1d3d.json), 38e8cdfda56d1d3d:04 Theorem B, §3, (5), fixed-body strict quasiconcavity.

## Statement

Let $d\ge1$, let $K$ be a convex body in $\mathbb R^d$, and let $T_K(y)$ be the maximal mass of a measurable Lebesgue density $0\le f\le1$ on $K$ with $\int_K(x-y)f(x)\,dx=0$. If $y_1,y_2\in\operatorname{int}K$ are distinct and $0<\lambda<1$, then
$$
T_K((1-\lambda)y_1+\lambda y_2)>\min\{T_K(y_1),T_K(y_2)\}.
$$
Consequently $T_K$ attains its maximum uniquely on every nonempty compact convex subset of $\operatorname{int}K$.

## Proof

By efa4558174ce60cf the optimal densities at the two marks are $\mathbf1_{D_i}$ for unique convex caps of positive mass $T_i=T_K(y_i)$. With $t=\min(T_1,T_2)>0$, put $f_i=(t/T_i)\mathbf1_{D_i}$. Their strict weighted mixture has mass $t$ and barycenter $(1-\lambda)y_1+\lambda y_2$. If the target retained mass were $t$, uniqueness at the target would make this mixture an indicator almost everywhere. A strict convex combination of two numbers in $[0,1]$ equals an endpoint only when both equal that endpoint. Thus the two $f_i$ would be the same density almost everywhere, contradicting their distinct means. Finally 669858b8fc253d7c with a one-body family gives continuity of $T_K^{1/d}$ on $K$. Continuity supplies a maximizer on a nonempty compact convex subset, and the proved inequality excludes two maximizers.
