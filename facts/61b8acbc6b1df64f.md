---
fact_id: 61b8acbc6b1df64f
kind: counterexample
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-pk-w31-convex-auxiliary-fiber-correction-fails
depends_on: []
verifier_run: 9620d53b330347a6
target_match: null
---

## Source

- [7d9bc9c2dd92ae95](../candidates/7d9bc9c2dd92ae95.json), 7d9bc9c2dd92ae95:03 §5, auxiliary-volume correction with or without integer exponential tilt.

## Statement

Let $v_0=v_2=1$ and $v_1=2$ be the interval lengths at the three integer bases of $\{(z,x):0\le z\le2,\ 0\le x\le2-|z-1|\}$. For every integer $k>1$, positive integer $r$, and real $a$, there is no convex auxiliary fiber family of compact sets $Q_z\subset\mathbb R^r$ on these bases with volumes proportional to $e^{az}v_z^{1-k}$ by one positive constant. Consequently independent convex factors cannot correct the $k$th-power weights back to the original weights even up to an integer exponential tilt.

## Proof

Let the common proportionality constant be $c>0$. Convexity requires $(Q_0+Q_2)/2\subseteq Q_1$, and all three volumes would be positive. Classical Brunn–Minkowski would give
$$
c^{1/r}e^{a/r}2^{(1-k)/r}=|Q_1|^{1/r}
\ \ge\ \frac{|Q_0|^{1/r}+|Q_2|^{1/r}}2
=c^{1/r}\frac{1+e^{2a/r}}2\ge c^{1/r}e^{a/r}.
$$
This is impossible since $k>1$. The factor requirement is exactly that $v_z^k|Q_z|=c e^{az}v_z$, by multiplication of independent fiber volumes.
