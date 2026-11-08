---
fact_id: 21aaea6df3e4e5ea
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-convex-fiber-euclidean-tube-weak-limit
depends_on: []
verifier_run: 6ed8c52a8df69ef9
target_match: null
---

## Source

- [9854c663e6eb01b8](../candidates/9854c663e6eb01b8.json), 9854c663e6eb01b8:02 §2, tube weak limit and orthogonal-section integral.

## Statement

Let $K$ be a nonempty compact convex subset of $\mathbb R^d$ of affine dimension $r$. Let $B_j$ be the Euclidean unit ball in dimension $j$ and $\kappa_j$ its volume, with $\kappa_0=1$. Then
$$
\varepsilon^{-(d-r)}\mathbf1_{K+\varepsilon B_d}\,dx
\;\rightharpoonup\;\kappa_{d-r}\mathcal H^r|_K
\qquad(\varepsilon\downarrow0).
$$
The Hausdorff measures are normalized to agree with Euclidean volume on their affine subspaces, including counting measure in dimension zero.

## Proof

Translate $\operatorname{aff}K$ to its direction space $L$ and split $\mathbb R^d=L\oplus L^\perp$ orthogonally. At perpendicular coordinate $\varepsilon s$ with $s\in B_{d-r}$, the section in $L$ is exactly $K+\varepsilon\sqrt{1-\lVert s\rVert^2} B_r$. For a bounded continuous test function $f$, rescaling the perpendicular integral gives
$$
\varepsilon^{-(d-r)}\int_{K+\varepsilon B_d} f(x)\,dx
=\int_{B_{d-r}}\int_{K+\varepsilon\sqrt{1-\lVert s\rVert^2} B_r}
 f(v+\varepsilon s)\,d\mathcal H^r(v)\,ds.
$$
All sets lie in a fixed compact neighborhood for small $\varepsilon$. Uniform continuity lets us replace $f(v+\varepsilon s)$ by $f(v)$ with a uniformly vanishing error under the bounded-volume integrals. The excess parallel volume above $K$ is at most $\mathcal H^r((K+\varepsilon B_r)\setminus K)$, which tends to zero by continuity from above for the compact parallel sets. The remaining integral is $\kappa_{d-r}\int_K f\,d\mathcal H^r$. The same product identity applies when a factor has dimension zero, using its one-point counting measure.
