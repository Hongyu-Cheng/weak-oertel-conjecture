---
fact_id: 7dd47dfc5d5f73ee
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-binary-nonradial-fixed-cover-exact-depth-descent
depends_on: ["ee8d9a577604402f", "ae578ba00acc8dab", "6769574fc1bd9f8d"]
verifier_run: 8b6aea43c116a0f7
target_match: null
---

## Source

- [8b96bf0ef6c68bc7](../candidates/8b96bf0ef6c68bc7.json), 8b96bf0ef6c68bc7:01 §§1–3, (1)–(4), exact nonradial descent in the binary lift.
- [8b96bf0ef6c68bc7](../candidates/8b96bf0ef6c68bc7.json), 8b96bf0ef6c68bc7:02 §3 final paragraph, fixed-total-mass normalization.
- [8b96bf0ef6c68bc7](../candidates/8b96bf0ef6c68bc7.json), 8b96bf0ef6c68bc7:03 §§4–5, (5)–(6), finite rational witness.

## Statement

For each $n\ge2$ use the binary family of ae578ba00acc8dab with core total mass $M_0=42/25$, old common cap budget $B=6811/8910$, $\Gamma=4/9$, and total $M_n=M_0+(2^n-2)B/\Gamma$. Keep every regular fiber and all its original cap planes fixed. Replace the core by the preceding coordinated unrotation from $t_0=1/10$ to $t<t_0$ sufficiently close, with its indicated common dilation. The resulting convex body has exactly the same integer bases and an inclusion-minimal cover by the same $3(2^n-1)$ caps. The regular budgets remain $B$, the core budgets strictly decrease, and the total mixed mass becomes $M_n+\delta$, where $\delta>0$ is the core gain. The exact raw global maximum stays $B$. Thus the normalized maximum is $B/(M_n+\delta)<B/M_n$.

Applying the common continuous scaling with squared factor $M_n/(M_n+\delta)$, and carrying the caps by that map, restores total mass $M_n$ and makes every selected budget strictly below $B$. The normalized maximum remains the displayed decreased value. The finite rational core witness $t=9/100$ with dilation $1007/1000$ gives $\delta=26115057/10000000000$ and the same conclusions, with normalized maximum
$$
\frac{\Gamma}{2^n-4978/4865+\Gamma\delta/B}>\frac{\Gamma}{2^n}.
$$

## Proof

Use the original binary sites $(z,b)$ and the original caps of ae578ba00acc8dab. Take the convex hull of the unchanged regular generators and the new three core generators at $(0,0),(1,0),(2,0)$. Each coordinate of an integer binary $b$ is extreme among the generators, so all generators contributing to a fiber there have that same $b$. For $b\ne0$ the two endpoint fibers are unchanged. For $b=0$ the new middle is the Minkowski average of the new endpoints by the core theorem. The original base inequalities therefore still give precisely the specified integer census. The spanning base and positive planar fibers give full dimension.

The three continuous supports of each new core fiber are $2L/3$ where $L$ is the common dilation. This follows from the unchanged maximizing vertex values and cyclic symmetry in the core theorem. For the nearby motion $L$ tends to one, and in the rational witness it is $1007/1000<3$. Thus the core supports are strictly below $2$ in both cases. Unchanged regular supports are below $4/3$. Since all cross-group base thresholds in the original menu are at least $2$, each cap still isolates its original assigned fibers. The core masses and the strict private witnesses are exactly those of the core theorem. The regular groups, caps and witnesses are unchanged. This proves exact coverage, inclusion-minimality and the selected masses.

The cover gives the raw upper bound $B$ at every mixed point. There is at least one regular fiber because $n\ge2$. At its centroid, every containing ambient halfspace has mass at least $B$ from its own trace alone, by 6769574fc1bd9f8d at full metronoid mass and by the area choice of the original regular triangle. This proves the exact raw and normalized maxima. The final scaling is a bijective affine map preserving the integer bases, carrying all containing halfspaces with it and multiplying every planar area by its squared scale. Hence it gives the fixed-mass claim and preserves the normalized maximum.

For the rational witness the core theorem gives the displayed $\delta$ and a strict cap drop. The identity $(4/9)M_0/B=4752/4865$ gives the stated normalized value. Since the rational core area is $16826115057/10000000000<6811/1980=2B/\Gamma$, the denominator there is strictly smaller than $2^n$. This proves the last strict inequality.
