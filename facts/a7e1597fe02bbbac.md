---
fact_id: a7e1597fe02bbbac
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-full-parity-volume-root-transport
depends_on: ["5969e97329ff52ae"]
verifier_run: 444eefda2fc6b55e
target_match: null
---

## Source

- [668ad0ef7a63372e](../candidates/668ad0ef7a63372e.json), 668ad0ef7a63372e:04 §4, Minkowski transport, volume roots and equality.
- [d0f838592db846be](../candidates/d0f838592db846be.json), d0f838592db846be:01, Exact orbit and cap consequences, (2).

## Statement

Use the full-parity witness orbits with $A=\pi(C)$ for compact convex $C\subseteq\mathbb R^n\times\mathbb R^d$, $d\ge1$, and write $K_z=C_z$ and $f(z)=|K_z|_d^{1/d}$ on $P$. On a path $z_0=z,\ldots,z_k=p_s$,
$$
2^{-k}K_z+\sum_{j<k}2^{j-k}K_{p_{[z_j]}}\subseteq K_{p_s},
\qquad
f(z)+\sum_{j<k}2^jf(p_{[z_j]})\le 2^k f(p_s).
$$
The inequality allows nonempty zero-volume fibers. If every witness fiber has volume $v_0\ge0$, then every fiber on $P$ has volume at most $v_0$. If $v_0>0$ and the source $K_z$ has volume $v_0$, the used witness fibers and the intermediate fibers are translates of $K_z$, and each intermediate fiber equals its preceding Minkowski midpoint with the corresponding witness fiber.

## Proof

The orbit lemma gives the terminal barycenter $p_s=2^{-k}z+\sum_{j<k}2^{j-k}p_{[z_j]}$. Its coefficients sum to one. Convexity of $C$ gives the stated Minkowski inclusion for arbitrary choices from the component bodies, including independently chosen points when a witness repeats. Brunn–Minkowski for nonempty compact convex sets, iterated over the sum, gives the displayed volume inequality and allows zero $d$-volume. If the witness volume roots equal $v_0^{1/d}$, their dyadic coefficient sum in the inequality is $2^k-1$, proving $f(z)\le v_0^{1/d}$.

Suppose $v_0>0$ and the source attains it. At the first midpoint, Brunn–Minkowski gives volume at least $v_0$, while the global bound just proved gives volume at most $v_0$. Apply this inductively along the path. In each step the two positive-volume endpoint bodies attain Brunn–Minkowski equality, hence are homothetic by its equality case. Their equal volumes make them translates. The actual intermediate body contains their Minkowski midpoint with equal volume and equals it. Indeed, if a point of the larger convex body lay outside the smaller closed one, a nearby interior point of the larger body would have a positive-volume neighborhood disjoint from the smaller. Induction then gives the common translation class for all participating bodies.
