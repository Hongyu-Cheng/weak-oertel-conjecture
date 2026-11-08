---
fact_id: 9bb8ad0f2aef88b0
kind: counterexample
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-probability-simplex-capacity-obstruction
depends_on: ["2863c5c8ec9f05b2"]
verifier_run: 4c180d827240e5cc
target_match: null
---

## Source

- [8095e181b6be7bf1](../candidates/8095e181b6be7bf1.json), §6, probability-simplex construction and rational support witness.
- [2243b639e270d75d](../candidates/2243b639e270d75d.json), Finite rational construction and independent exact verification procedure.
- [1ba0a7307dda1496](../candidates/1ba0a7307dda1496.json), §§1–2, the same continuous simplex-law witness.

## Statement

For $d\ge1$ and $m=d+1$, let $D_d$ consist of all $v\in\mathbb R_+^m$ for which there exists a nonnegative zero-diagonal column-stochastic $m\times m$ matrix $Y$ satisfying $v_i\le \operatorname{GM}_d((Y_{ij})_{j\ne i})$ for every $i$, where $\operatorname{GM}_d$ is the geometric mean of $d$ entries. In dimension $d=2$, there is a random vector $Z\in\Delta_2$ such that, for $a=(200,100,100)/273$ and every $i$,
$$
\inf_{t>0:\Pr(Z_i\le t)>0}\frac{t}{\sqrt{\Pr(Z_i\le t)}}\ge a_i.
$$
But $a\notin D_2$, with $\sum_i a_i^2+2a_1a_2a_3-1=33583/20346417>0$. The polynomial test at $p=(200/273,1,1)$ has value $-142/74529$.

## Proof

Use the archived [rational certificate](../assets/pk-nov6/computations/beta_coupling_exact_certificate_root.json). It lists $399$ positive rational masses $m(i,j,k)$ on triples $0\le i,j,k<200$. Their sum is one, their first-index marginal at $r$ is $(2r+1)/40000$, and the sum of their second- and third-index marginals at $r$ is $2(2r+1)/40000$. Every listed triple satisfies $2(i+1)+(j+1)+(k+1)\le546$. These are exact finite arithmetic identities. To check them, parse the masses as rational numbers, accumulate $m(i,j,k)$ at $i$ in one array and at both $j$ and $k$ in a second array, and compare the two arrays to the displayed targets at every index, checking the support bound for each triple. The archived [rational verifier](../assets/pk-nov6/computations/verify_beta_coupling_certificate_root.py) implements these checks.

Draw a triple according to these masses and independently swap its last two indices with probability $1/2$. The resulting indices $I_1,I_2,I_3$ all have the same exact marginal, and the weighted support bound is preserved. Given the indices, draw $V_q$ on $[I_q/200,(I_q+1)/200]$ with density proportional to $2v$ there. The mass of each bin under density $2v$ on $[0,1]$ is precisely $(2I_q+1)/40000$. Hence every $V_q$ has distribution function $s^2$ on $[0,1]$. The upper endpoint support bounds give $2V_1+V_2+V_3\le273/100$ almost surely.

Put $W_i=a_iV_i$, so $\sum_iW_i\le1$, and set $Z=(W_1+1-\sum_iW_i,W_2,W_3)$. Then $Z\in\Delta_2$ and $Z_i\ge W_i$. In particular $\Pr(Z_i\le t)\le\Pr(W_i\le t)\le (t/a_i)^2$ for every $t>0$. This proves the capacity lower bounds. Substitution into the support polynomial at $p=(200/273,1,1)$ gives $-142/74529$, violating the necessary condition from the support dual. Direct substitution also gives the stated cubic excess. Since $D_2$ is downward, the resulting capacity vector also lies outside $D_2$.
