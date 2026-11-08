---
fact_id: e2af48a0a6aef2ec
kind: counterexample
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-single-source-unbounded-global-contact-cost
depends_on: []
verifier_run: 6d9e74ce6235459e
target_match: null
---

## Source

- [6748c967393345b9](../candidates/6748c967393345b9.json), 6748c967393345b9:8 §4, contact-cost limitation.

## Statement

For every integer $m\ge2$ there is a compatible body on a lattice-complete rank-one base with two occupied parities, one prescribed centroid source, and a global projective cut action whose first total mixed-volume loss is exactly $m$ times the prescribed positive first source loss.

## Proof

Take $P=\{0,1,\ldots,m-1\}$ with every fiber $[-1,1]$ and canonical hull $[0,m-1]\times[-1,1]$. Both parities occur. Choose one source at height zero, for example at base zero. Its projective energy parameter is zero, by symmetry and strict convexity of the projective objective on its admissible interval. Explicitly the integral is $2/(1-a^2)$ for $|a|<1$. The centered support in both unit normals is one. The zero base slope is a feasible support slope in both directions, with zero slack everywhere. Take the positive convex tangent extension $f(s)=2-s$ for $s\le1$ and $f(s)=1/s$ for $s\ge1$, whose slopes agree at $1$. The zero denominator base shift makes its argument exactly $1$. The two global cut constraints are exactly $X+\varepsilon\le1$ and $-X+\varepsilon\le1$ for every real base. Every sampled interval is therefore $[-1+\varepsilon,1-\varepsilon]$. The prescribed source loss is $2\varepsilon$ and the actual total loss is $2m\varepsilon$. Their first coefficient ratio is $m$.
