---
fact_id: af4f4e8d8dbeb0ba
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-uniform-strict-single-vertex-simplex-cut
depends_on: []
verifier_run: a844b3b10a1c4f29
target_match: null
---

## Source

- [c71e38de38f9f3c8](../candidates/c71e38de38f9f3c8.json), c71e38de38f9f3c8:02 §2, (3)–(6).

## Statement

Let $B=\operatorname{conv}(0,e_1,\ldots,e_d)$, $d\ge1$, $N=d+1$, and $\lambda_i$ be its barycentric functions. Suppose $|\lambda_k(y)-1/N|\le1/(2N)$ for every $k$. For any $i$ and $\lVert v\rVert\le1/(8N)$ the margin $\lambda_i(x)-\lambda_i(y)+v\cdot(x-y)$ at vertex $i$ is at least $1/(4N)$ and at every other vertex at most $-1/(4N)$. In particular the same one-vertex sign pattern holds for every through-$y$ cap whose unit normal has distance at most $1/(8N\sqrt d)$ from $\nabla\lambda_i/\lVert\nabla\lambda_i\rVert$.

## Proof

At any vertex the perturbation magnitude is at most $2\lVert v\rVert\le1/(4N)$ since both the vertex and $y$ have norm at most one. The coordinate conditions place $y$ in the interior and bound the unperturbed value from above by $-1/(2N)$ at other vertices and from below by $1-3/(2N)\ge1/(2N)$ at vertex $i$. For a unit normal $u$, multiply by $\lVert\nabla\lambda_i\rVert$, which lies between one and $\sqrt d$. The difference from $\nabla\lambda_i$ has the allowed perturbation norm.
