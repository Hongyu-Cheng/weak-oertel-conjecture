---
fact_id: deaa95bb75702fdc
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-optimized-three-interval-reflection
depends_on: []
verifier_run: 6afb33841d9d8f8f
target_match: null
---

## Source

- [c412d1154d2768ef](../candidates/c412d1154d2768ef.json), c412d1154d2768ef:01 §1 (1) and aligned-endpoint equality.

## Statement

Let $I_-,I_0,I_+$ be intervals of lengths $a,b,c>0$ at three symmetric integer bases, with $(I_-+I_+)/2\subseteq I_0$. At a center $y\in I_0$, sum the own overlap $|I_0\cap(2y-I_0)|$ and the two ordered reflected overlaps of $I_-,I_+$. The maximum of this sum over $y\in I_0$ is at least $\max\{b,2\min(a,c)+\min(b,\max(a,c))\}$. The bound is sharp for every compatible length triple, attained with aligned lower endpoints $I_-=[0,a]$, $I_0=[0,b]$, $I_+=[0,c]$.

## Proof

Translate so that $I_0=[0,b]$. Set $l=\min(a,c)$ and $A=\max(a,c)$. The midpoint interval of the endpoints is $[s,s+(l+A)/2]$ for $0\le s\le b-(l+A)/2$. Each ordered endpoint overlap is at most $l$, and attains $l$ precisely on the plateau $[s+l/2,s+A/2]$: this is the condition that the smaller interval lie in the reflection of the larger. The self-overlap is $2\min(y,b-y)$. Its superlevel set at $q=\min(b,A)$ is $[q/2,b-q/2]$. The right endpoint of the plateau is at least $A/2\ge q/2$, and its left endpoint is at most $b-A/2\le b-q/2$. At a common point the total overlap is at least $2l+q$. At $y=b/2$ the own overlap is $b$.

For aligned lower endpoints $s=0$. If $A\ge b$, then $b/2$ lies on the plateau (compatibility gives $b\ge l$), attaining the termwise upper bound $b+2l$. If $A\le b$, the endpoint total increases with slope $4$ up to $l/2$, equals $2l$ through $A/2$, then falls with slope $-4$ until it is zero and stays zero. The own overlap increases with slope $2$ up to $b/2$ and falls thereafter. Before $A/2$ the total is nondecreasing, and on the falling segment of the endpoint contribution the total strictly decreases. On the zero segment the total is at most $b$. Its maximum is therefore $\max\{b,A+2l\}$, as required.
