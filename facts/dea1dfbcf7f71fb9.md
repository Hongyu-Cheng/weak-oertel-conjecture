---
fact_id: dea1dfbcf7f71fb9
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-pk-w34-buffered-small-buffer-facet-alternative
depends_on: ["cf17d6bf1aab7a2d", "d90ba05577427854", "7d294884f0a6d744"]
verifier_run: e882082cfeaed896
target_match: null
---

## Source

- [7c213e6353a4073e](../candidates/7c213e6353a4073e.json), 7c213e6353a4073e:05 §7, (9)–(13), labeled quantitative small-buffer alternative.

## Statement

In the planar regular singleton density of cf17d6bf1aab7a2d take nonnegative weights $\eta_i$ with $\sum_i\eta_i=1$ and support size $s$. Put $\Delta=\sum_i\eta_i\delta_i$ and
$$
S_{\max}=\sqrt{\lambda_{\max}(\Sigma)}
 \sum_z\sup_{\lVert e\rVert=1,t}\mathcal H^1(K_z\cap\{e\cdot X=t\}).
$$
If source fiber $K_{p_i}$ is facetless and its density satisfies all signed convex-potential tests $\int_{\partial K_{p_i}}\Xi\Phi\,ds\le0$, then $\beta\ge\eta_i/2-5\Delta/(6M)$. In particular the single-group bound is $\beta\ge1/2-5\delta_i/(6M)$. Moreover $\Delta\le\varepsilon S_{\max}$. If $s\le k$, $\beta<(4/9)/k$ and $\varepsilon<M/(15k S_{\max})$, any source of maximum weight has a nontrivial line facet or fails the stated tests. If all positive-weight sources are freely tested and facetless, then $\beta\ge1/(2s)-5\Delta/(6M)$.

## Proof

On a facetless source, pk-w34-buffered-planar-facet-convex-order gives $\Xi=0$ almost everywhere. Away from the finitely many proper cap-line boundary intersections and zero-arclength supporting traces, the regular profile is locally constant and the smooth part is continuous, so the density vanishes throughout those arcs. Choose a pair of opposite rays from the interior source $y_i$ with both boundary endpoints on such arcs. The own shifted thresholds are strictly negative relative to $y_i$ since $\varepsilon>0$, $\Gamma(u_{ij})=1$ and $f_i>0$. For each selected own cap at least one of the opposite endpoints has nonnegative unshifted margin relative to $y_i$, hence belongs to the cap. The own profile values at the two endpoints therefore sum to at least $\sum_j\theta_{ij}=1$. At one endpoint $W\ge\eta_i/2$ since the other group profiles are nonnegative. There $0=\Xi=W+G-\beta-5\Delta/(6M)$ with $G\ge0$, giving the claimed bound.

For every selected covector, $1/\lVert u_{ij}\rVert\le\sqrt{\lambda_{\max}(\Sigma)}$ by its covariance-unit normalization. The total proper coarea $S_{ij}$ is therefore at most $S_{\max}$. Since $\sum_j\rho_{ij}=1$, $B_i=\sum_j\rho_{ij}/S_{ij}\ge1/S_{\max}$. Using $f_i\le1$ from d90ba05577427854 gives $\delta_i=\varepsilon f_i/B_i\le\varepsilon S_{\max}$, and averaging gives the same estimate on $\Delta$. A maximum weight is at least $1/s$. If that source were freely tested and facetless under the stated smallness assumptions, then $\beta>1/(2k)-1/(18k)=(4/9)/k$, a contradiction.
