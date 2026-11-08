---
fact_id: aad9166ae6f6cff6
kind: counterexample
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-stationary-mixed-profile-nonconcavity
depends_on: []
verifier_run: b9ac4c748b92f518
target_match: null
---

## Source

- [867dbbe22c30cda2](../candidates/867dbbe22c30cda2.json), 867dbbe22c30cda2:06 §§6–7, disconnected profile and connected all-level centroid obstruction.

## Statement

There exist actual compact convex mixed bodies with $n=1,d=2$ whose positive integer fibers are smooth disks and which have a balanced pair of globally minimizing through-origin caps at a global maximum of normalized depth $1/2$. The mixed parallel-section profile need not be log-concave or have any positive concave power, even with connected positive support, symmetry, unimodality, and the exact ambient section-centroid identity at every level in the positive support.

Two examples are $[-1,1]\times B_2$ with parallel cuts $3z+x_2=t$, and $\{(z,x):|z|\le1,\ \lVert x\rVert+|z|\le2\}$ with cuts $x_2=t$. Here $B_2$ is the unit disk and each profile sums the ordinary lengths in the original integer fibers.

## Proof

Both bodies are centrally symmetric with three positive area fibers at bases $-1,0,1$. Every nonvertical through-origin cap has half the original mass by reflection and the nullity of its boundary in every fiber. A pure-base cap through the origin has at least half by the same symmetry, since its boundary can have positive mass. A parallel inward move reduces any containing cap to a through-origin one. Therefore the origin has normalized depth exactly $1/2$, and no point can have larger depth because an opposite pair of nonvertical through-point caps always has total mass one after normalization. The zero-level cut in each example and its opposite give a balanced pair of actual minimizing normals.

In the first example only the central diameter meets the zero level, so its centroid is the origin. Its exact profile is
$$
P(t)=2\sum_{j=-1}^1\sqrt{(1-(t-3j)^2)_+}.
$$
It has $P(0)=P(3)=2$ and $P(3/2)=0$. These values contradict log-concavity and concavity of every positive power on the convex hull of the positive support.

In the second example the fiber radii are $1,2,1$. At each level $|t|<2$ all chord intervals are centered at $x_1=0$, and the two outer fibers have identical chord lengths, giving full ambient centroid $(0,0,t)$. The profile
$$
P(t)=2\sqrt{(4-t^2)_+}+4\sqrt{(1-t^2)_+}
$$
is even, nonincreasing for $t\ge0$, and positive exactly on $(-2,2)$. But $P(1)^2=12$, while $P(3/4)=\sqrt{55}/2+\sqrt7>6$ and $P(5/4)=\sqrt{39}/2>3$. Thus $P(1)^2<P(3/4)P(5/4)$ at the midpoint of two positive levels. If $P^\alpha$ for $\alpha>0$ were concave, its midpoint arithmetic-mean lower bound would imply the geometric-mean lower bound by AM–GM, contradicting the same calculation.
