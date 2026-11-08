---
fact_id: 2bf2dbb0965eae6e
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-stratified-centers-for-joint-slice-laws
depends_on: ["2beba099308501dc", "151fa708661bd0e3"]
verifier_run: e445986db9bef8e8
target_match: null
---

## Source

- [237f4727836ebab9](../candidates/237f4727836ebab9.json), §§2–4, (5)–(9).

## Statement

Let $n\ge0$, $N\ge1$, and let $\mu=\sum_{z\in P}\delta_z\otimes\mu_z$ for a nonempty finite $P\subset\mathbb Z^n$ and nonzero finite positive compactly supported Borel measures $\mu_z$ on $\mathbb R^D$. Suppose every combination $z=\sum_i\theta_i z_i\in\mathbb Z^n$, with $z_i\in P$, $\theta_i>0$, and $\sum_i\theta_i=1$, has $z\in P$ and satisfies
$$
\mu_z\!\left(\sum_i\theta_i E_i\right)^{1/N}\ge\sum_i\theta_i\mu_{z_i}(E_i)^{1/N}
$$
for every compact positive-mass choice of $E_i$. Partition $P$ into strata of equal support affine dimension and equal support tangent space. For stratum $c$, let $W_c$ be its total mass, $q_c$ its support affine dimension, and $k_c$ the number of its occupied base parities modulo $2\mathbb Z^n$. Write $W=\sum_c W_c$ and $k(P)=\sum_c k_c$.

There is a point in the actual support of $\mu$ whose raw depth, the infimum of $\mu(H)$ over all containing closed ambient halfspaces $H$, is at least
$$
\max_c \frac{W_c}{(q_c+1)k_c}\ \ge\ \frac{W}{\sum_c(q_c+1)k_c}.
$$
In particular, if all $q_c\le1$, and $k_0,k_1$ are the sums of the occupied parity counts over dimensions $0,1$ respectively, then this depth is at least $W/(k_0+2k_1)\ge W/[2k(P)]\ge (N/(N+1))^N W/k(P)$. This includes all laws with $q_c<N$ when $N\in\{1,2\}$.

## Proof

Apply joint-measure-homothetic-domination-and-strata to the stated joint inequality. Each stratum's placed support is the exact integer trace of its compact convex hull, and its integer bases are midpoint closed in each parity. The parity sets of the strata are disjoint. In particular, the stated $k(P)$ equals the number of occupied classes of the entire base.

Apply intrinsic-fiber-helly-with-occupied-parity to the stratum hull with fiber dimension bound $q_c$. Take as its measure the exact restriction $\sum_{z\in P_c}\delta_z\otimes\mu_z$ of the given law. This yields a point in its actual support with depth at least $W_c/[(q_c+1)k_c]$ for that restriction. Every containing halfspace has at least as much mass under $\mu$. Choose a stratum maximizing the displayed ratio. Its value is at least the weighted average with weights $(q_c+1)k_c$, which is the second bound.

For $q_c\le1$ the denominator of that average is $k_0+2k_1\le2k(P)$. Finally $(1+1/N)^N\ge2$ by the binomial expansion. The all-atomic specialization also gives $W/k(P)$ since all $q_c=0$.
