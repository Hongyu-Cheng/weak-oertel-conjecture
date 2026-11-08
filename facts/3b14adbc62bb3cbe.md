---
fact_id: 3b14adbc62bb3cbe
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-pk-w34-birth-raw-depth-nested-mass-loss
depends_on: ["978e8555ec5bac42"]
verifier_run: 1113aa3f54fe245a
target_match: null
---

## Source

- [a57c113e8e14cc38](../candidates/a57c113e8e14cc38.json), a57c113e8e14cc38:02 §2, (2)–(4).

## Statement

For compact convex bodies $D\subseteq C$ in $\mathbb R^{n+d}$ with positive mixed $d$-volumes $M_D,M_C$ on $\mathbb Z^n\times\mathbb R^d$, let $A_E$ and $\beta_E=A_E/M_E$ denote the maximum raw and normalized closed-halfspace depths on the integer trace of $E$. For $\delta=M_C-M_D$,
$$
0\le A_C-A_D\le\delta,\qquad
\max\!\left(0,\frac{M_C\beta_C-\delta}{M_C-\delta}\right)\le\beta_D
\le\min\!\left(1,\frac{M_C\beta_C}{M_C-\delta}\right),\qquad
\frac{M_D}{M_C}\beta_D\le\beta_C\le\frac{M_D\beta_D+\delta}{M_C}.
$$

## Proof

Extend both raw depth functions to the same full lattice product by taking the infimum of the corresponding cap mass over all closed halfspaces containing the point. For every such halfspace, its $C$-mass is at least its $D$-mass and at most its $D$-mass plus $\delta$, because the two measures are restrictions of the same mixed measure. The same two inequalities hold after taking infima, pointwise on the whole lattice product. A point outside a compact convex body belongs to a closed halfspace disjoint from that body by strict separation and therefore has raw depth zero. Taking suprema on the common domain gives the first bounds, with the maxima attained on the original traces by the depth attainment lemma. Substitute $A_E=M_E\beta_E$ and use $0\le\beta_D\le1$ for the remaining bounds.
