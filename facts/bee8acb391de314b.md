---
fact_id: bee8acb391de314b
kind: counterexample
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-three-simplex-compatible-centers-local-budget-gap
depends_on: ["71921ffe0614be8d"]
verifier_run: 15b3cee497441c13
target_match: null
---

## Source

- [6bb486f2aedd17ca](../candidates/6bb486f2aedd17ca.json), 6bb486f2aedd17ca:8 §3, inequality (8), and rational planar instance; additional proof scope: §3, inequality (8), compatibility equation (7), (13), and rational planar instance.

## Statement

Let $T,c,\gamma_d$ be as in the simplex depth deficit lemma and take $d\ge1$ and $2^{-1/d}<\rho<1$. The hull of $\rho T,T,\rho T$ at integer bases $-1,0,1$ has exactly these three integer fibers. Their total $d$-volume is $M=c(1+2\rho^d)$ and each is lighter than $M/2$. For every allowed compatible triple $p_-,p_0,p_+$ with $p_0=(p_-+p_+)/2$, the sum of the unnormalized local halfspace depths satisfies
$$
D_{\rho T}(p_-)+D_T(p_0)+D_{\rho T}(p_+)
\le\gamma_d M-\frac{c\gamma_d(1-\rho)}d.
$$
For $d=2$ and $\rho=3/4$ the bound is $8c/9=\gamma_2 M-c/18$.

## Proof

The bases project to $[-1,1]$, and the endpoint fibers in the hull are their displayed fibers. At base zero every combination of endpoint contributions uses equal endpoint weights, and their average lies in $\rho T\subseteq T$. Combining with a point of $T$ leaves the middle fiber exactly $T$. The volume and nonheavy assertions follow from $2\rho^d>1$. On these bases the compatibility condition is equivalent to the midpoint equation: a representation of an endpoint uses only that endpoint, and a representation of zero has equal endpoint weights.

Put $E_0=\sum_i(p_0)_i-d/(d+1)$, $E_\pm=\sum_i(p_\pm)_i-d\rho/(d+1)$, and $A=d(1-\rho)/(d+1)$. Then $E_0=(E_-+E_+)/2-A$, so $|E_0|+(|E_-|+|E_+|)/2\ge A$. Since $\rho^{d-1}\ge1/2$, the same lower bound holds with weight $\rho^{d-1}$ on the two endpoint errors. Apply the simplex depth deficit lemma at scales $1,\rho,\rho$ and add: the summed deficit is at least $c\gamma_d(d+1)A/d^2=c\gamma_d(1-\rho)/d$. For $d=2,\rho=3/4$, the mass is $17c/8$, the target budget is $17c/18$, and the deficit is at least $c/18$.
