---
fact_id: b55aafdaa99f446c
kind: counterexample
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-all-parity-decimations-increase-depth
depends_on: ["aac16ce53722f3a6"]
verifier_run: 35e68f0b60d8957b
target_match: null
---

## Source

- [6e1991cd32bd2796](../candidates/6e1991cd32bd2796.json), 6e1991cd32bd2796:02 §A, all four decimations.

## Statement

Let $P=\operatorname{conv}\{(-3,-1),(3,3),(1,3),(-1,2)\}$. For every $r\in\{0,1\}^2$, the maximum normalized closed-halfspace depth over the lattice sites of $(P-r)/2$, under their uniform counting law, is $1/2$. The corresponding maximum for $P$ is $3/10$. All four decimations therefore strictly increase the maximum, although each original site has weight $1<10/4$.

## Proof

Use the ten-site baseline fact for the original maximum and its four parity classes. The invertible affine map $z\mapsto(z-r)/2$ maps $S\cap(r+2\mathbb Z^2)$ bijectively to the lattice sites of $(P-r)/2$. It preserves the halfspace tests and the uniform normalized law on the restricted support.

Each two-site class has raw maximum one: a containing cut always counts its mark and one can exclude the other site by a linear cut through the mark. In the four-site class $\{s_0,s_2,s_7,s_9\}$, every closed halfspace through or containing $s_2$ captures $s_2$ and at least one of $s_0,s_7$, whose midpoint is $s_2$. The original cut table restricted to this class gives caps of sizes $1,2,1,1$ at $s_0,s_2,s_7,s_9$, respectively. The raw maximum is therefore two. Dividing each class by its own size proves the claim.
