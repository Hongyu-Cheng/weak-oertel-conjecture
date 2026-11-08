---
fact_id: fdbeaa0e8c6be579
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-pk-w31-binary-selected-star-physical-escape
depends_on: ["f967ba259d25c184", "5660e9bff8ec5e16", "af5faac906b2cdf7"]
verifier_run: 2eaa8f0c966abb78
target_match: null
---

## Source

- [9b703b460ed5bf2b](../candidates/9b703b460ed5bf2b.json), 9b703b460ed5bf2b:03 §6, binary isolation.
- [30d7d56bee7b8657](../candidates/30d7d56bee7b8657.json), 30d7d56bee7b8657:02 §5, binary isolation.

## Statement

Fix $n,d\ge2$ and $\Gamma_d=(d/(d+1))^d$. At binary coordinate $w=0$ use the symmetric three-fiber star with raw maximum $D$ and fibers $K,K-K,-K$ at $z=-1,0,1$. At each nonzero binary $w\in\{0,1\}^{n-1}$ put a centered $d$-simplex of volume $D/\Gamma_d$ at both $z=0,1$, and take their actual convex hull. It has exactly $2^n+1$ positive integer fibers and initial total mass $2D+(2^n-2)D/\Gamma_d$. There is an inclusion-minimal cover of these fibers by one isolated proper concurrent star group and one isolated canonical centroid group per regular base, for $2^n-1$ groups in total.

Apply either the fixed-cap first-order path for a nonuniform selected star group or either of the joint paths for a canonical group, with all other fibers fixed. The strict isolation margins and the exact integer support persist. The star budgets strictly decrease with the same orders and coefficients as on the isolated star, every regular cap remains exactly at $D$, and actual maximal raw depth stays exactly $D$ while total mass strictly increases with the same gain as on the star.

## Proof

Use the binary hull and isolations from fact f967ba259d25c184 with the same star and regular simplex volumes. Its projection is $\operatorname{conv}([0,1]^n\cup\{-e_1\})$, and any convex representation over a binary $w$ uses only constituents at that same $w$, because each coordinate of $w$ is an extreme value of $[0,1]$. At $w\ne0$ the two endpoints are exact. At $w=0$ the local midpoint slack proved for the selected-star paths preserves the actual three fibers. Thus the integer support and all unmoved fibers remain exact.

For a retained star cap subtract $L\sum_k w_k$ from its margin, with $L$ so large that it misses every regular fiber strictly. This is possible uniformly for all thresholds near the selected $a$ since the regular fibers form a finite compact family and their binary-coordinate sums are at least one. Its trace at $w=0$ is unchanged. For the regular groups use the strictly exposing functional $3\sum_k(2v_k-1)w_k+(2z_0-1)z$ at each $q=(z_0,v)$, $v\ne0$, with its isolating finite tilt from f967ba259d25c184. The functional gap is at least one at every other integer base, and all excluded fibers are compact. The strict cap exclusions persist under each sufficiently small star path, including the moving endpoint. Each regular group therefore keeps its old cap masses $D$.

The star margins sum to zero on $w=0$ at every time, and the canonical regular group covers its own entire plane by its zero sum of margins. Thus the retained cover bounds every depth by $D$. At any unchanged regular centroid, the simplex centroid depth bound used in f967ba259d25c184 gives raw mass at least $D$ in every containing ambient halfspace from its own fiber alone, hence the actual maximum equals $D$. The unperturbed cover is inclusion-minimal: each proper star or canonical regular cap has an own-fiber vertex lying strictly in that cap and outside its other group caps, and all other groups strictly miss that fiber. The same strict exclusions and vertex test persist on these short paths.

On the star there is no mass from any other binary component in the isolated caps. The fixed-cap linear and analytic cubic paths give their respective strict star cap losses and gains, and the canonical quadratic joint path gives the quadratic losses and gains. All other fiber masses are fixed, so these are exactly the gain coefficients of the full body.
