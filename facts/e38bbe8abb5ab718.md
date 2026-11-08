---
fact_id: e38bbe8abb5ab718
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-capped-integer-first-moment
depends_on: []
verifier_run: 044135095db3a6df
target_match: null
---

## Source

- [3c669076dab13e6a](../candidates/3c669076dab13e6a.json), §1 (6) and the packing remainder.
- [ad8324f468564d7c](../candidates/ad8324f468564d7c.json), §3 (4) and the sharp filled-site value.

## Statement

Let $h\in\mathbb Z$, $m>0$, and let $(a_i)_{i\le h}$ be finitely supported with $0\le a_i\le m$ and total mass $A$. Write $A=qm+u$ with $q\in\mathbb Z_{\ge0}$ and $0\le u<m$. The largest possible first moment for these $h,m,A$ is
$$
hA-\frac{mq(q-1)}2-qu
=hA-\frac{A^2}{2m}+\frac A2-\frac{u(m-u)}{2m}.
$$
It is attained by putting mass $m$ at $h,h-1,\ldots,h-q+1$, mass $u$ at $h-q$, and zero elsewhere. In particular the first moment is at most $hA-A^2/(2m)+A/2$.

## Proof

Index the masses by distance from $h$, so $v_j=a_{h-j}$ for integers $j\ge0$. Let $b_j$ denote the proposed masses: $b_j=m$ for $0\le j<q$, $b_q=u$, and $b_j=0$ for $j>q$. Both sequences have total mass $A$, so
$$
\sum_{j\ge0}j(v_j-b_j)=\sum_{j\ge0}(j-q)(v_j-b_j)\ge0.
$$
For $j<q$ both factors on the right are nonpositive, for $j>q$ both are nonnegative, and for $j=q$ the product is zero. Thus the minimal distance moment is $\sum_{j\ge0}j b_j=mq(q-1)/2+qu$. The first moment equals $hA$ minus the distance moment. Expanding $A=qm+u$ gives $mq(q-1)/2+qu=A^2/(2m)-A/2+u(m-u)/(2m)$, proving the formula and the bound, including $A=0$.
