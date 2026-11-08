---
fact_id: dc5eae7ee90a1b73
kind: counterexample
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-tetrahedral-circuit-row-splitting-cost-obstruction
depends_on: ["1462fa9ce6ced54e", "10e60a719885af2c"]
verifier_run: cdb060a3a7d79582
target_match: null
---

## Source

- [63504696488203c3](../candidates/63504696488203c3.json), 63504696488203c3:03 §§3–4, (9)–(10).

## Statement

On a tetrahedron, use a through-interior cap with vertex margins $(p,q,-r,-s)$, where $p,q,r,s>0$. Let $Q$ be its volume fraction, and $S$ its section area divided by whole volume and the normal length. With $N=pq(r+s)+rs(p+q)$, the exact deficit relative to the minimum vertex-splitting cost is
$$
\frac{p+q}{3}-\frac QS=\frac{pq(rs-pq)}{3N}.
$$
In particular on $K=\operatorname{conv}(0,e_1,e_2,e_3)$ at $y=(1/6,1/6,1/6)$, take the balanced spanning normals
$$
v_0=(-1,-5,-6),\quad v_1=(1,0,0),\quad v_2=(0,5,0),\quad v_3=(0,0,6).
$$
The actual normalization $M=\sum_i Q_i/S_i$ is $21/5$. Every positive decomposition of $v_0$ alone into vertex-isolating normals through $y$, retaining the other three rows, increases $M$ by at least $2/15$, attained when zero margins are allowed.

## Proof

Use the arbitrary raw-height part of 1462fa9ce6ced54e, with its strict two-positive/two-negative split and $F=Q$. Its $S$ divides actual section area by $|K|\|v\|$, exactly as here. The affine margin vanishes at $y$ and has gradient $v$, so its raw vertex heights are the stipulated $(p,q,-r,-s)$. The accepted formulas give $S=3(\alpha+\delta)$ and $Q=p(\alpha+\delta)+q^2/((q+s)(q+r))$, where
$$
\alpha=\frac{ps}{(p+r)(p+s)(q+s)},\qquad
\delta=\frac{qr}{(p+r)(q+s)(q+r)}.
$$
Multiplying $\alpha+\delta$ by $(p+r)(p+s)(q+r)(q+s)$ gives $N$. Therefore the deficit equals
$$
\frac{qN-q^2(p+r)(p+s)}{3N}=\frac{pq(rs-pq)}{3N}.
$$

The proposed four normals sum to zero, and the last three are independent, so their balanced dependence is unique and minimal. The first row margins are $(2,1,-3,-4)$, giving $Q_0=13/60$, $S_0=1/4$ and $Q_0/S_0=13/15$. The other three cuts are $x_i\ge1/6$, so each has fraction $(5/6)^3=125/216$. Their apex margins are $5/6,25/6,5$, and the pyramid formula gives $S_i=25/12,5/12,25/72$, respectively. Hence $M=13/15+5/18+25/18+5/3=21/5$.

The vertex-splitting lemma gives a minimum replacement ratio of $(2+1)/3=1$. The excess is therefore at least $1-13/15=2/15$. The two margin vectors $(2,0,-18/7,-24/7)$ and $(0,1,-3/7,-4/7)$ have barycentric mean zero at $(1/2,1/6,1/6,1/6)$, sum to the first row, and have respective unique positive heights two and one, attaining that excess.
