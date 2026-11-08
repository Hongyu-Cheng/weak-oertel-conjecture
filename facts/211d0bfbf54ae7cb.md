---
fact_id: 211d0bfbf54ae7cb
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-w32-vertical-caps-require-balanced-strict-sides
depends_on: ["87b433dccd2ca6c6"]
verifier_run: 512fc5753f4d702f
target_match: null
---

## Source

- [81d698898b296675](../candidates/81d698898b296675.json), 81d698898b296675:02 Final paragraph, strict-side obstruction.

## Statement

Let an actual mixed-integer body have one integer coordinate and continuous dimension $d\ge1$. At an integer base $j$, let $B$ be its whole fiber and let $\ell,r$ be the total mixed volumes on the strict left and right sides. Let $\eta$ be a finite nonnegative measure on $B$. Suppose that at a mark on this fiber every containing closed ambient halfspace has original mixed volume at least the mass of its fiber trace under $\mathbf1_B\,dx+\eta$. Then $\eta(B)\le\min(\ell,r)$. If additionally $|B|+2\eta(B)$ equals the total original mixed volume, then $\ell=r$. An integer weighted median need not have this balance.

## Proof

The two closed halfspaces with boundaries $z=j$ both contain the mark and all of $B$. Their original masses are $|B|+\ell$ and $|B|+r$ and both surrogate masses are $|B|+\eta(B)$. The domination inequalities give $\eta(B)\le\min(\ell,r)$. The full-mass condition gives $2\eta(B)=\ell+r$, forcing $\ell=r$. For an actual median with unequal strict-side volumes, use the three-fiber body in accepted fact 87b433dccd2ca6c6: its unique weighted median base is $0$, with strict-side mixed areas $2$ and $1/8$.
