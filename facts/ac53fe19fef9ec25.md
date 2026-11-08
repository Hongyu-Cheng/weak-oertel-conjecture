---
fact_id: ac53fe19fef9ec25
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-compact-physical-martingale-coupling
depends_on: []
verifier_run: 64265289203b5a7b
target_match: null
---

## Source

- [7278f286325c46c7](../candidates/7278f286325c46c7.json), §§1–2, (1)–(3).

## Statement

Let $\nu$ and $\eta$ be compactly supported finite nonnegative Borel measures on $\mathbb R^k$. Write $\nu\preceq_{\rm cx}\eta$ if they have equal mass and $\int\Phi\,d\nu\le\int\Phi\,d\eta$ for every finite continuous convex $\Phi:\mathbb R^k\to\mathbb R$. Then $\nu\preceq_{\rm cx}\eta$ if and only if there is a finite nonnegative coupling $\pi$ with first marginal $\nu$, second marginal $\eta$, and
$$
\int f(x)(y-x)\,d\pi(x,y)=0
$$
for every bounded Borel scalar $f$ on $\mathbb R^k$. The equality is coordinatewise and expresses that the output conditional on the input has mean equal to the input.

## Proof

The zero common mass has the zero coupling. For finite atomic measures write their positive masses as $m_i,n_j$ at $x_i,y_j$. Distance to $D=\operatorname{conv}\{y_j\}$ is a finite continuous convex test, so convex order puts every $x_i$ in $D$. The nonnegative arrays satisfying $\sum_j t_{ij}=m_i$ and $\sum_jt_{ij}y_j=m_ix_i$ therefore form a nonempty compact convex polytope. Let $T$ be its image under the column-sum map. If $n=(n_j)_j\notin T$, strict separation gives a vector $b$ with
$$
\sum_j b_j n_j<\min_{s\in T}\sum_j b_j s_j.
$$
Define $g(x)$ for $x\in D$ as the least $\sum_j\alpha_j b_j$ over all convex representations $x=\sum_j\alpha_j y_j$. Its epigraph over $D$ is the polyhedron $\operatorname{conv}\{(y_j,b_j)\}+\{(0,t):t\ge0\}$. In the affine span of $D$ times $\mathbb R$, its defining inequalities either restrict $x$ alone or give affine lower bounds on the last coordinate, since the epigraph contains the upward ray above every point. At least one lower bound is needed because $g$ is finite. Thus $g$ is the maximum of finitely many affine functions there, including on the boundary of $D$. Extend those functions to the ambient space and take their maximum to obtain a finite continuous convex extension. This includes singleton $D$ by a constant extension. Independent minimization over the rows now gives
$$
\min_{s\in T}\sum_j b_j s_j=\sum_i m_i g(x_i)
\le\sum_j n_j g(y_j)\le\sum_j n_j b_j,
$$
contradicting the separation. This proves finite coupling with the required row moments.

For general compact supports use half-open grid cubes of side $\delta\downarrow0$ in $\mathbb R^k$. Replace the source mass in each nonempty cube by its barycenter, giving $\nu_\delta$. Replace each target point by a probability on the vertices of the closure of its cube with the same mean, using the product of the one-coordinate linear interpolation weights, and integrate these weights against $\eta$ to get $\eta_\delta^+$. These are finite atomic measures, with movements at most $\sqrt{k}\delta$ in a single compact box for $\delta\le1$. Jensen gives $\nu_\delta\preceq_{\rm cx}\nu\preceq_{\rm cx}\eta\preceq_{\rm cx}\eta_\delta^+$, and the displacement bound gives weak convergence of the outer measures to $\nu,\eta$. Use the finite result and take a weakly convergent subsequence of its couplings on the compact product box, all of the same mass. The limit has the prescribed marginals and satisfies the moment equality for continuous tests by weak convergence. For each coordinate, the finite signed measure $B\mapsto\int\mathbf1_B(x)(y_\ell-x_\ell)\,d\pi$ on the box then integrates every continuous function to zero. It is zero, giving the moment equality for every bounded Borel test.

Conversely, disintegrate the coupling over the input in the compact box. For each coordinate the Borel moment equality implies that the conditional mean is $x$ almost everywhere, by uniqueness of conditional expectation. Apply conditional Jensen and integrate. The marginal masses agree because $\pi$ is a coupling.
