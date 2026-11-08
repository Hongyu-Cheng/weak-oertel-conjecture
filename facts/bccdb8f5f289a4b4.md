---
fact_id: bccdb8f5f289a4b4
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-compact-lipschitz-marginal-duality
depends_on: []
verifier_run: 2c9b802b074b068e
target_match: null
---

## Source

- [9c4bb3ca1bcd69e1](../candidates/9c4bb3ca1bcd69e1.json), §2.

## Statement

Let $K_i$ be nonempty compact Euclidean sets, $i=1,\ldots,k$, and let $\gamma_i$ be finite nonnegative Borel measures supported on $K_i$ with common mass $M>0$. Suppose the real-valued cost $c$ on $\prod_i K_i$ is $L_i$-Lipschitz in coordinate $i$. The maximum of $\int c\,d\pi$ over the couplings of the $\gamma_i$ equals the minimum of $\sum_i\int u_i\,d\gamma_i$ over continuous functions $u_i$ on $K_i$ with $\sum_i u_i(x_i)\ge c(x_1,\ldots,x_k)$. Both extrema are attained, and minimizing potentials may be chosen $L_i$-Lipschitz in coordinate $i$. For any minimizing potentials the constraint is equality almost everywhere under every maximizing coupling.

## Proof

The couplings form a nonempty compact set in the weak topology, by the product coupling scaled to mass $M$, compactness of the product space, and closedness of the marginal equalities. The continuous cost attains its maximum. Weak duality follows by integrating the pointwise constraint.

Write $S_i=\operatorname{supp}\gamma_i$. For $\delta>0$, choose a finite maximal $\delta/2$-separated set in each $S_i$. Use Borel Voronoi cells with a fixed tie rule. Each point in a cell is within $\delta$ of its representative, and each cell has positive marginal mass since it contains a relatively open neighborhood of that representative in $S_i$. Collapse the marginals to the representatives. Finite linear programming duality gives optimal arrays and dual numbers on these finite sets. Replace each potential in turn by the maximum of $c-\sum_{j\ne i}u_j$ over the other finite coordinates. Each replacement preserves feasibility and lowers only that potential, hence preserves optimality by weak duality. It makes the replaced potential $L_i$-Lipschitz on its representatives. Add constants of total sum zero to make each of the first $k-1$ potentials zero at one representative. All their oscillations are bounded by $L_i\operatorname{diam}(S_i)$. Complementary slackness, or integration of the nonnegative constraint gap, gives one representative tuple with equality and therefore bounds the last potential as well.

Extend each finite potential to $S_i$ by $u_i(x)=\min_t(u_i(t)+L_i|x-t|)$, with $t$ ranging over its representatives. The extension is equibounded and $L_i$-Lipschitz. On any product tuple the dual constraint can fail by at most $2\delta\sum_iL_i$, by comparison with its representative tuple. Add this quantity to the last potential to make the extensions feasible. The value of the finite primal differs from the original maximum by at most $M\delta\sum_i L_i$: collapse any original coupling to obtain the upper comparison, and lift any finite coupling by the products of normalized restrictions to its component cells to obtain the lower comparison. The extended dual objective differs from the finite dual objective by at most $3M\delta\sum_iL_i$. Taking $\delta\downarrow0$, Arzelà–Ascoli yields uniformly convergent subsequences of the feasible potentials on the supports. Their limits have the stated Lipschitz bounds, are feasible on the product of the supports, and attain the original primal value.

For $K_i$ larger than $S_i$, extend each limiting potential by the same minimum formula over $t\in S_i$. For each tuple $x\in\prod_i K_i$ take a minimizer $t_i\in S_i$ for every coordinate. The sum of the extensions is at least $c(t)+\sum_iL_i|x_i-t_i|\ge c(x)$, and the objective is unchanged. Finally the constraint gap is nonnegative with zero integral under every maximizing coupling, giving the equality assertion.
