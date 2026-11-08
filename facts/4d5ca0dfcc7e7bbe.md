---
fact_id: 4d5ca0dfcc7e7bbe
kind: counterexample
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-w32-opposite-offsets-one-endpoint-credit
depends_on: ["d90ba05577427854", "6769574fc1bd9f8d"]
verifier_run: 671fd0953e10456d
target_match: null
---

## Source

- [3208a2842914cf02](../candidates/3208a2842914cf02.json), 3208a2842914cf02:03 §3, (3), sharp endpoint sum.

## Statement

Fix $d\ge2$ and $V>0$. Consider actual endpoint fibers at integer bases $-1,1$, each of ordinary volume $V$, with interior marks of projective energy $V$. For a closed ambient halfspace given by an affine margin at least zero, assume that its signed evaluations at the two lifted marks are $-1,+1$, respectively. The sharp infimum of the sum of its captured endpoint $d$-volumes is $\Gamma_d V$, where $\Gamma_d=(d/(d+1))^d$. This infimum remains sharp when the actual middle fiber is the Minkowski midpoint, without fixing that fiber's geometry.

## Proof

Accepted fact d90ba05577427854 implies each mark is its fiber's ordinary centroid. The positively evaluated endpoint has a containing trace and therefore contributes at least $\Gamma_d V$ by accepted fact 6769574fc1bd9f8d with full retained mass $V$; the other endpoint contributes nonnegative volume.

For sharpness, take a centered $d$-simplex of volume $V$ whose height in one coordinate $x_1$ ranges from $-1$ on its base to $d$ at its apex. This normalization is possible because the centroid is the average of the vertices, and the transverse coordinates can be rescaled to prescribe the volume. For $L>1$ define $A$ and $B_L$ by multiplying $x_1$ by $1/(2d)$ and by $L$, respectively, and in each case using the reciprocal factor in a second coordinate to preserve volume. These are centered and both have energy $V$ at zero by d90ba05577427854. The convex hull of the two lifted endpoints has them as its extreme slices and its slice at base zero is exactly $(A+B_L)/2$, since the total weights at the two bases must be $1/2$ there. All marks may be taken at zero.

For the ambient cap $x_1+z\ge0$ the two marked evaluations are $-1,+1$. The left trace is empty because $x_1\le1/2$ on $A$. The right trace is the apex cap $x_1\ge-1$ in $B_L$, whose height range is $[-L,Ld]$. Homothety about the apex gives its volume as
$$
V\left(\frac{d+1/L}{d+1}\right)^d\longrightarrow\Gamma_d V.
$$
The lower bound and this sequence prove the infimum.
