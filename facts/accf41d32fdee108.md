---
fact_id: accf41d32fdee108
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-uniform-finite-cap-envelope
depends_on: []
verifier_run: e973c380113129c0
target_match: null
---

## Source

- [92662e9a8e20fd35](../candidates/92662e9a8e20fd35.json), 92662e9a8e20fd35:01 §1, (1)–(5).

## Statement

Let $K\subset\mathbb R^d$ be compact, $y_0\in\operatorname{int}K$, and $F_j(y,s)$ be finitely many continuous real functions on $K$ times a neighborhood of $0$, $C^1$ near $(y_0,0)$. Suppose $F_j(y_0,0)=Q$, $\nabla_yF_j(y_0,0)=-g_j$, and $\max_j g_j\cdot v\ge c\|v\|$ for every $v$, for $c>0$. Put $f=\min_jF_j$ and $b_j=\partial_s F_j(y_0,0)$. On a common neighborhood assume each first-order Taylor remainder is bounded by $(\|v\|+|s|)\omega(\|v\|+|s|)$, for a nondecreasing $\omega$ with $\omega(r)\to0$ as $r\downarrow0$. Suppose $\sup_K|F_j(y,s)-F_j(y,0)|\le B|s|$, $B>0$, and take a radius $r_0$ inside the common Taylor neighborhood such that $\omega(r_0)\le c/2$ and $\sup_{K\cap\{\|y-y_0\|\ge r_0\}} f(y,0)\le Q-\eta$ for $\eta>0$. For sufficiently small $s\ge0$, every maximizer $y_s$ of $f(\cdot,s)$ satisfies $\|y_s-y_0\|\le4Bs/c$. For any probabilities $\theta_j$ with $\sum_j\theta_jg_j=0$, the maximum is at most $Q+s\sum_j\theta_j b_j+As\omega(As)$, where $A=1+4B/c$. If $\omega(r)\le Lr$ the error is at most $LA^2s^2$. The bounds and the smallness conditions are uniform when the stated data and neighborhood sizes are uniform.

## Proof

The gradient and remainder bounds give $f(y,0)\le Q-(c/2)\|y-y_0\|$ within radius $r_0$. The time bound also holds for the minimum of the branches. Testing $y_0$ gives a new maximum at least $Q-Bs$. If $2Bs<\eta$ a maximizer cannot lie outside radius $r_0$. The local drop and time bound then give $(c/2)\|y_s-y_0\|\le2Bs$. At this point the minimum is no larger than the weighted average with weights $\theta_j$; in the averaged Taylor expansion the linear displacement term cancels and the error is bounded by $As\omega(As)$ since $\|y_s-y_0\|+s\le As$. Take $s$ small enough that these arguments remain within the common Taylor neighborhood. The quadratic error under the stated bound on $\omega$ follows by substitution.
