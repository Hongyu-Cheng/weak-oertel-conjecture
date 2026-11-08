---
fact_id: 9fadb9e67a905fde
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-intrinsic-mixed-half-depth-rigidity
depends_on: ["d84d740a59312d9a"]
verifier_run: e4f47a007bcaef2e
target_match: null
---

## Source

- [b90a2673d60a00b3](../candidates/b90a2673d60a00b3.json), b90a2673d60a00b3:03 statement items 1–4 and §§3–5, (4)–(9).
- [b90a2673d60a00b3](../candidates/b90a2673d60a00b3.json), b90a2673d60a00b3:04 §6.

## Statement

Let $C\subset\mathbb R^n\times\mathbb R^d$ be compact and convex, let $\Lambda=\mathbb Z^n\times\mathbb R^d$, and suppose $S=C\cap\Lambda$ has Hausdorff dimension $q>0$. Write $\mu=\mathcal H_q|_S$ and $M=\mu(S)>0$. For any actual $y=(j,c)\in S$, the following are equivalent.

1. Every closed ambient halfspace containing $y$ has $\mu$-mass at least $M/2$.
2. The angular pushforward of $\mu$ about $y$ is antipodally invariant.
3. Reflection about $y$ preserves $\mu$.
4. $\mathcal H_q(S\cap(2y-S))=M$.

When these hold, every positive $q$-dimensional fiber has its exact reflected partner, the fiber at $j$ is itself positive and centrally symmetric about $c$, $y$ is the full ambient centroid, and its normalized depth is $1/2$. The conclusions refer to the measured fibers and allow unmatched $\mathcal H_q$-null fibers. For counting measure the implication from half depth to symmetry can fail.

## Proof

The trace is a finite union of compact convex fibers, so $q$ is their largest affine dimension. Since $q>0$ there is no atom at $y$, and the angular half-depth lemma gives the equivalence of 1 and 2 and the exact depth.

Assume 2. Write $K_z=\{x:(z,x)\in C\}$. For each primitive integer direction $v\ne0$, consider opposite rays $j\pm kv$ for integers $k\ge1$. A nonzero integer difference from $j$ has a unique primitive oriented ray and positive integer index. On this pair of rays put $A_k=(K_{j+kv}-c)/k$ and $B_k=(c-K_{j-kv})/k$, with missing fibers empty. Both families are nested in decreasing order because $y$ is in $C$: a point over a farther base $j\pm\ell v$ can be interpolated with $y$ using its weight $k/\ell$ to reach $j\pm kv$. Only finitely many fibers occur.

The angular chart $s\mapsto(v,s)/\lVert(v,s)\rVert$ is a homeomorphism onto the Borel stratum of directions with base component a positive multiple of $v$. Distinct oriented rays have disjoint strata and the own-fiber stratum has base component zero. The chart pulls back the angular restriction on the positive ray to $\sum_k k^q\mathcal H_q|_{A_k}$, by Hausdorff scaling on each original fiber. The antipodal image of the restriction on the negative ray pulls back to the same sum with $B_k$. Thus
$$
\sum_k k^q\mathcal H_q|_{A_k}=\sum_k k^q\mathcal H_q|_{B_k}.
$$

If one sum is zero, both are zero. Otherwise $A_1,B_1$ have dimension $q$ by nesting, and every positive member on each side lies in that side's affine $q$-plane. Different $q$-planes meet in a set of $\mathcal H_q$-measure zero, so equality of the nonzero measures forces the planes to coincide. On this common plane the two densities agree almost everywhere. For each point of the plane, the active indices on each side form a prefix of length $r$, with density $\sum_{k=1}^r k^q$. These prefix sums are strictly increasing. Hence the indicators of $A_k$ and $B_k$ agree almost everywhere for every $k$. For each positive index, the closed convex bodies agree exactly. Indeed, a point of one body outside the other has a neighborhood disjoint from the latter, and interpolating it toward a relative interior ball of the former gives positive volume inside this neighborhood. Therefore $K_{j-kv}=2c-K_{j+kv}$ for every positive fiber away from $j$.

If some positive fiber lies away from $j$, its reflected pair gives a positive $q$-dimensional Minkowski midpoint inside $K_j$ by convexity. In fact that midpoint contains a relative ball about $c$ because it is a translate of half a full-relative-dimensional difference body. If all positive mass already lies at $j$, the own fiber is positive directly. Within its affine direction space, let $\rho(\theta)$ be the radial extent of $K_j-c$ in direction $\theta$, allowing zero. Polar integration shows that the own angular pushforward has density $\rho(\theta)^q/q$ against intrinsic spherical surface measure, with the two-point counting version when $q=1$. Evenness gives $\rho(\theta)=\rho(-\theta)$ almost everywhere and therefore $K_j=2c-K_j$ up to $\mathcal H_q$-null sets. The preceding closed-convex-body argument gives exact equality. This proves 3.

Reflection about an actual integer-base point preserves $\Lambda$ and $\mathcal H_q$. Thus 3 implies 4, and 4 implies 3 by discarding the $\mathcal H_q$-null differences between $S$ and $2y-S$. Symmetry gives 1 because opposite closed through-$y$ caps have equal mass and cover $S$. Compactness gives finite first moments, so symmetry gives centroid $y$.

For the counting exception take $n=1,d=0,C=[0,3]$. The left closed ray at $y=1$ counts two points and the right counts three, so the depth is $1/2$ after normalization. Reflection about $1$ sends $3$ to $-1$ and fails to preserve the counting measure.
