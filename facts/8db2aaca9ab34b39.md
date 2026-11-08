---
fact_id: 8db2aaca9ab34b39
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-pk-w30-radialized-marginal-homothety-covariance
depends_on: []
verifier_run: d334ed8d87818e28
target_match: null
---

## Source

- [181842182f63ac33](../candidates/181842182f63ac33.json), 181842182f63ac33:01 §§1–2 and §5, (1)–(6), homothetic covariance and incompatibility of powers.

## Statement

Let $f$ be a bounded compactly supported log-concave density of mass $W>0$ in $\mathbb R^r$. Assume $c$ is a chosen point for which the star set with radius $\rho_{f,c}(\omega)^r=r\int_0^\infty s^{r-1}f(c+s\omega)\,ds$ is a convex body $L_{f,c}$ with centroid zero. For $a,s>0$ and $b\in\mathbb R^r$, the density $a f((x-b)/s)$ has radial body $a^{1/r}sL_{f,c}$ at $b+sc$ and mass $as^rW$. In any such sampled family, if the marks $b_z+s_zc$ interpolate affinely and the radii $a_z^{1/r}s_z$ interpolate concavely at every anchored convex combination, then the marked radial bodies satisfy the anchored Minkowski inclusions, preserve all original masses and preserve every cap mass through their corresponding mark.

If $f$ is the $r$-dimensional orthogonal marginal of uniform volume on a full-dimensional $N$-body $Q$, with $r<N$, then $sQ$ has marginal radial scale $s^{N/r}$ at $sc$. A positive nonconstant affine scale on a three-site chain therefore gives a compatible source family whose unweighted mass-preserving marked radial bodies fail midpoint inclusion. Rescaling each radial body to scale $s$ changes its ordinary volume to $s^rW$, and a fiber weight $s^{N-r}$ restores the original masses and through-mark cap masses.

## Proof

Substitute the ray variable $s\tau$ into the radial integral for the transformed density at $b+sc$. The integral is $as^r$ times the original, and change of variables in ambient volume gives mass $as^rW$. The dilation preserves centroid zero. By polar integration, the volume of the radial body on a hemisphere is the mass of the density in the corresponding through-mark halfspace, because both are the integral of $\rho^r/r$ on that hemisphere. This includes $r=1$ by counting the two ray directions. A weighted Minkowski combination of marked copies of $L_{f,c}$ has the averaged mark and the averaged scale. A larger scale at the same mark contains it because $0\in L_{f,c}$.

For the uniform projection, its $(N-r)$-dimensional section volumes scale by $s^{N-r}$ at the projected argument divided by $s$. Hence $a=s^{N-r}$ and the computed radial scale is $s^{N/r}$. With $s_0=(s_-+s_+)/2$ and unequal $s_\pm>0$, the source has $s_0Q=(s_-Q+s_+Q)/2$. The marks $s_zc$ are affine, but strict convexity of $s^{N/r}$ makes the endpoint midpoint radial copy strictly larger than the middle copy. Multiplying the radial scales by $s^{-(N-r)/r}$ restores scale $s$, while multiplying the resulting volume measure by $s^{N-r}$ compensates for the ordinary volume scaling.
