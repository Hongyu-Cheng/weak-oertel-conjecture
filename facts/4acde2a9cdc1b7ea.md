---
fact_id: 4acde2a9cdc1b7ea
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-surface-area-domination-on-contact
depends_on: ["82413ddca5bdb268"]
verifier_run: 0d6d3bc8481cc0df
target_match: null
---

## Source

- [0c3c4405d9ae2dd3](../candidates/0c3c4405d9ae2dd3.json), §1, (1)–(2).

## Statement

Let $L\subseteq K$ be full-dimensional compact convex bodies in $\mathbb R^d$, $d\ge1$, and let $Z=\{u\in\mathbb S^{d-1}:h_L(u)=h_K(u)\}$. Then
$$
S_L|_Z\le S_K|_Z.
$$
For full-dimensional compact convex bodies $A,B,K$ with $M=(A+B)/2\subseteq K$, it follows with $Z=\{h_M=h_K\}$ that
$$
(S_A\wedge S_B)|_Z\le S_K|_Z.
$$
For $d=1$, the area measure is counting measure on the two endpoint normals.

## Proof

For $d\ge2$, let $E\subseteq Z$ be Borel. Each regular $x\in\partial L$ with outer unit normal $u\in E$ lies in the $u$-exposed face of $K$, by inclusion and equality of support values. The nonregular part of $\partial K$ is $\mathcal H^{d-1}$-null, including its intersection with $\partial L$. At every remaining $x$ the unique outer unit normal of $K$ is $u$. Both regular boundary loci and their normal maps are Borel. Indeed, the normal relation is closed, and the set of points with two normals at distance at least $1/m$ is compact for each positive integer $m$. On the regular locus the normal is continuous relative to that locus, by closedness and compactness of the unit sphere. The almost everywhere regularity follows from the local convex Lipschitz graph representation and differentiability almost everywhere. Comparing the two sets of regular points, with the same ambient $\mathcal H^{d-1}$, gives $S_L(E)\le S_K(E)$. For $d=1$ a contacted endpoint has the same sign normal in both intervals.

For the midpoint statement with $d\ge2$, the weighted Minkowski area bound applies to the two full-dimensional bodies, with common measure $S_A\wedge S_B$ and weights $1/2$. Its domination by $S_M$ persists under restriction to $Z$, where the first conclusion applies to $M\subseteq K$. For $d=1$ all three area measures are the same two unit atoms.
