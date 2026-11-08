---
fact_id: 791fbc4b9a8effbd
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-pk-w34-lifts-one-base-continuous-count-minorant
depends_on: []
verifier_run: 8ecb4c30dbe35848
target_match: null
---

## Source

- [d8f7a4409a9bdcfe](../candidates/d8f7a4409a9bdcfe.json), d8f7a4409a9bdcfe:01 §2, (3)–(6), the pointed mixed marginal and its continuous minorant.

## Statement

Let $C\subset\mathbb R\times\mathbb R^d$ be a compact convex body, with fibers $C_z$. Suppose $D$ is a $d$-dimensional convex body, $y(z)$ is affine, $\ell>0$ is constant, all nonempty $C_z$ lie in $y(z)+\ell D$, and $C_z=y(z)+\ell D$ on a real interval containing at least three integers. Under the fiber chart $\xi=(x-y(z))/\ell$, the continuous-coordinate projection of mixed volume has density $f(\xi)=\ell^d m(\xi)\mathbf1_D(\xi)$, where $m(\xi)$ is the number of integers in the real base section over $\xi$ in the chart. If $L(\xi)$ is that section's length, the bounded compactly supported density $g=(3/4)\ell^d L\mathbf1_D$ is upper semicontinuous and concave on $D$, with $f/2\le g\le f$ pointwise and $\int g\ge(\int f)/2$.

## Proof

The affine change of variables gives one compact convex set $T$ with projection $D$ and real base section $I_\xi=\{z:(z,\xi)\in T\}$ for each $\xi\in D$. It is a compact interval containing the specified interval, so $m(\xi)=|I_\xi\cap\mathbb Z|\ge3$. Its first and last included integers are $m-1$ apart, and each end of $I_\xi$ lies less than one unit beyond the corresponding included integer. Consequently $m-1\le L\le m+1$. Each counted original fiber contributes the same Jacobian $\ell^d$, so Fubini with counting measure gives the asserted density $f$.

Convexity gives $(1-t)I_\xi+tI_\eta\subseteq I_{(1-t)\xi+t\eta}$, and interval lengths add under this operation. Thus $L$ is concave on $D$. Along any convergent sequence in $D$, pass to a subsequence realizing the upper limit of the lengths and then to convergent endpoints in the bounded base projection; compactness puts the limiting endpoints in the target section. This proves upper semicontinuity, which extends to the density by zero outside the closed $D$. Finally $(3/4)(m-1)\ge m/2$ and $(3/4)(m+1)\le m$ when $m\ge3$. These inequalities give the pointwise sandwich and the mass bound.
