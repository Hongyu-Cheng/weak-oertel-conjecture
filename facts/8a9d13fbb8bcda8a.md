---
fact_id: 8a9d13fbb8bcda8a
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-finite-barycentric-flow-elimination
depends_on: []
verifier_run: 36d9eff2add78bca
target_match: null
---

## Source

- [8ac2ff347361aad9](../candidates/8ac2ff347361aad9.json), 8ac2ff347361aad9:02 §2, (2), absorption and exact edge traversal.

## Statement

Let $P$ be a finite set of distinct points and let $f_{pq}\ge0$ be finite weights with $\sum_q f_{pq}(q-p)=0$ for every $p$. Define $a_p=\sum_qf_{pq}$, $b_p=\sum_qf_{qp}$, $s_p=(a_p-b_p)_+$, $t_p=(b_p-a_p)_+$, and $m_p=a_p+t_p=b_p+s_p$. Delete zero states and isolated pure loops. A chain injected with mass $s_p$ at $p$, moving from $p$ to $q$ with probability $f_{pq}/m_p$ and stopping at $p$ with probability $t_p/m_p$, is absorbed almost surely. Its terminal law is $t$, its expected remaining edge traversal masses are exactly $f_{pq}$, and the joint starting and terminal points form a martingale coupling. For every finite convex $\phi$ on $\operatorname{conv}P$,
$$
\sum_p(t_p-s_p)\phi(p)=\sum_{p,q}f_{pq}[\phi(q)-\phi(p)]\ge0 .
$$
For $\phi(p)=|p|^2$ the right side equals $\sum_{p,q}f_{pq}|q-p|^2$. The last two sums can include deleted loops, which have zero contribution.

## Proof

For $m_p>0$ the move and stop probabilities sum to one. The barycentric flow assumption makes the conditional mean of the next position, with a stop counted at the current point, equal to $p$. Any closed communicating class with no stopping has only one point. Indeed each coordinate is harmonic on such a finite class, and at a coordinate maximum all positive successors must also maximize it. Irreducibility makes each coordinate constant on the class, and the states are distinct. At the resulting singleton $p$ with positive mass, all outgoing flow is on the pure loop and $t_p=0$. Its loop already contributes $a_p$ to $b_p$, so $b_p=a_p$ and no edge enters from another state. Hence it carries neither injection nor terminal mass. Remove these loops and zero states.

Every remaining state can reach a state with positive stopping probability, since otherwise its finite reachable graph contains a closed nonstopping class. Finiteness gives a common step bound $N$ and probability $\epsilon>0$ of stopping within $N$ steps from each remaining state. The geometric tail gives almost sure absorption and convergence of the Green sum $G=\sum_{k\ge0}T^k$, where $T_{pq}=f_{pq}/m_p$. Regard $m,s$ as row vectors. Incoming weights give $m=s+mT$, and iteration with the geometric bound gives $m=sG$. Starting from $s$, the expected visits before each move or stop thus have masses $m$. Multiplying by the move and stop probabilities gives precisely $f$ and $t$. For each starting state the position process held fixed after absorption has constant expected position by the row barycenter identity. The positions are uniformly bounded, so taking the limit gives the conditional martingale property for the terminal point.

The displayed finite equality is row and column subtraction, using $t_p-s_p=b_p-a_p$. Convex Jensen in each row gives its nonnegativity. For the squared norm, expansion and $\sum_q f_{pq}(q-p)=0$ leave exactly the sum of squared displacements.
