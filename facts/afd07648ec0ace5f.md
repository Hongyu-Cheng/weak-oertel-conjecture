---
fact_id: afd07648ec0ace5f
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-simultaneous-cap-profile-and-critical-residual-budget
depends_on: ["6684c9103c897998"]
verifier_run: c883d32380b3ddf8
target_match: null
---

## Source

- [c2528b1460a23da4](../candidates/c2528b1460a23da4.json), c2528b1460a23da4:02 §§3–4 (4)–(6), increasing profiles and one baseline.
- [c2528b1460a23da4](../candidates/c2528b1460a23da4.json), c2528b1460a23da4:04 §6 (8), planar critical residual budget.

## Statement

Let $A,B,K\subseteq\mathbb R^d$ be full-dimensional convex bodies with $(A+B)/2\subseteq K$, let $P\subseteq A$ be nonempty compact with $\dim\operatorname{aff}P<d$, and let $v_i\cdot b\le1$ for every $b\in B$ and $i=1,\dots,s$. Write $\sigma_i(x)=\mathbf1_{\{v_i\cdot x<0\}}$ and $\rho_i(a)=\mathbf1_{\{v_i\cdot a<-1\}}$. For every coordinatewise nondecreasing $\Psi:\{0,1\}^s\to[0,\infty)$, the same baseline $P+B$ gives
$$
2^d\int_K\Psi(\sigma)\,dx
\ge \int_{P+B}\Psi(\sigma)\,dx+\int_A\Psi(\rho)\,da.
$$
This includes unions, intersections, and positive excess above a threshold for the number of missed caps. For compact mixed-lattice source sets on one common integer parity class and finite source measure $\mathcal H_q(A)$, with Borel $K$ containing all actual midpoints, the factor is $2^q$, the integrals use $\mathcal H_q$, and the final integral is over $A\setminus\operatorname{aff}P$.

In the planar case with three nonzero spanning normals $v_0+v_1+v_2=0$, suppose the three caps $v_i\cdot x-z\ge0$ each have raw mixed area $Q$ in the actual fibers $A,K,B$ at $-1,0,1$. Put $k=|K|$, $U_i=|A\cap\{v_i\cdot x\ge-1\}|$, and $R_i(A)=A\cap\bigcap_{j\ne i}\{v_j\cdot x<-1\}$. For every such $P$ of affine dimension at most one,
$$
4(2k-3Q+\sum_i U_i)
\ge \sum_i |(P+B)\cap\bigcap_{j\ne i}\{v_j\cdot x<0\}|+\sum_i|R_i(A)|.
$$

## Proof

The hypotheses give $\sigma(a+b)\ge\rho(a)$ coordinatewise for every actual pair. Thus $F=\Psi\circ\sigma$ and $g=\Psi\circ\rho$ meet the weighted transfer's Borel and pointwise conditions with $L=\operatorname{aff}P$. The source on $L$ is null for ambient $d$-volume. Positive midpoint dilation preserves every zero-level incidence and scales the measure by $2^{-d}$, so inclusion in $K$ proves the displayed result. With compact mixed-lattice sources in a common parity class each actual sum has even integer coordinates, the same positive dilation gives the Hausdorff factor $2^{-q}$, and the affine-span exclusion is retained. The OR and AND indicators and $\big(\sum_{i\in I}\sigma_i-\ell\big)_+$ for any chosen $I$ and integer $\ell\ge0$ are increasing functions. Each choice uses the same $P$.

For the planar budget use the excess-count choice $\ell=1$ on all three normals. The $B$ caps are contained in lines $v_i\cdot x=1$ and have area zero. Hence each corresponding middle captured area is $Q-U_i$. Off the three null lines, a point in $K$ misses exactly one or two caps because the normals sum to zero. The integral of its missed-count excess above one equals the total missed count integral minus $k$, namely $2k-3Q+\sum_i U_i$. On $A$, all three strict misses at thresholds $-1$ are impossible by the zero sum, so the excess equals the indicator of the disjoint union of $R_i(A)$. On the baseline, all three strict zero-level misses are likewise impossible and the excess equals the sum of the indicators in the stated baseline. Substitution proves the budget.
