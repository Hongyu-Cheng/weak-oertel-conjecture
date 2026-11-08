---
fact_id: 2ffde1a50c63bcad
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-uniform-face-contact-row-likelihood
depends_on: []
verifier_run: acced90678d31929
target_match: null
---

## Source

- [5dc06bb8226350eb](../candidates/5dc06bb8226350eb.json), 5dc06bb8226350eb:02 §4, (11)–(13).
- [5dc06bb8226350eb](../candidates/5dc06bb8226350eb.json), 5dc06bb8226350eb:05 §8, (19)–(20).

## Statement

Let actual compatible convex $d$-fibers over a fixed finite real base $P$ be contained in $RB_d$. At a mark $Y=(p,y)$ with $B(y,r_s)\subset K_p$, let $L\ge0$ be concave on the canonical hull and $A\ge L$ an affine majorant with $A(Y)=L_i=L(Y)>0$. Let $\rho$ be a probability on the sampled fibers with mean $Y$ and $\int L\,d\rho=L_i$. For each $u\in P\cap F_p$ fix an anchored representation of $p$ with positive weight at $u$ and let $t_*>0$ be the minimum of these weights. Then $\rho$ is supported over $F_p$, $L=A$ $\rho$-almost everywhere, and $d\bar\rho=(L/L_i)d\rho$ is a probability with
$$
\frac{d\bar\rho}{d\rho}\le C_0=\frac{r_s+2R}{t_*r_s}\quad \rho\text{-almost everywhere},
\qquad 0\le D(\bar\rho\|\rho)\le\log C_0.
$$
Any probability-weighted average of rows satisfying a common $C_0$ has the same entropy bound.

## Proof

An affine exposer of $F_p$ that is zero there and strictly positive on other sampled bases has zero $\rho$-mean because the base barycenter is $p$. Thus $\rho$ lives over $F_p$. Also $A$ is nonnegative throughout the hull and $\int (A-L)\,d\rho=A(Y)-L_i=0$, so $A=L$ almost everywhere in the row.

For each $u\in P\cap F_p$, the anchored representation exists because $p\in\operatorname{relint}F_p$. Extend the segment from $u$ through $p$ within the face and express the other endpoint by its vertices, or use weight one when $u=p$. For each $X\in K_u$ the representation with arbitrary other fiber points gives a point $X'$ in $K_p$ with $A(p,X')\ge t_*A(u,X)$. Extend from $X'$ through $y$ to the opposite point of the source inball. The resulting interpolation uses a coefficient at least $r_s/(r_s+2R)$ at $X'$ and the other value is nonnegative. If $X'=y$, use the coefficient one. Therefore $A(u,X)\le C_0 A(Y)$ throughout the face fibers. This gives the ratio bound because $A=L$ on the row. The $L$-moment makes $\bar\rho$ a probability. The upper entropy bound follows by integrating $\log(L/L_i)\le\log C_0$ against $\bar\rho$, with the usual zero-density convention, and the lower bound by Jensen for $s\log s$ under $\rho$. Probability-weighted averaging preserves both bounds.
