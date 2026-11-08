---
fact_id: e1a7a34258ecebfa
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-all-dimensional-larger-positive-scalar-envelope
depends_on: ["361f5ce3d8bf6813", "834bfe0328b6edaa", "c88376a94a8fd722", "f8e5ccdf06e64ddf"]
verifier_run: de30957fbb0e2b0e
target_match: null
---

## Source

- [31dd328861ee872c](../candidates/31dd328861ee872c.json), Theorem and §§1–6, (1)–(15).
- [16db32a020dc6379](../candidates/16db32a020dc6379.json), §3, upper-coordinate boundary.

## Statement

For an integer $m\ge1$ and $0\le x_j\le h<1$ with some $x_j>0$, put $\rho=\prod_j(1-x_j)$, $E=\rho^{-1}-1$, and
$$
L=\left(1-\frac{\sum_j x_j}{E}\right)\prod_j(1+x_j/E),\qquad
R=\rho(E+h)\left[1-\frac{(E+h)\prod_j(h-x_j)}{h^{m+1}}\right].
$$

Then $L\ge R$, with strict inequality whenever all $0<x_j<h<1$.

## Proof

Zero coordinates delete without changing the gap, and the upper-face lemma gives $L-R\ge0$ when some $x_j=h$. For $m=1$ the fixed-product minimizer lemma gives the formula
$$
L-R=\frac{x(h-x)[2h(1-x)+x]}{h^2(1-x)}
$$
for $0<x\le h<1$, which is nonnegative and is positive for $x<h$.

Suppose the theorem has been established for smaller dimensions and the gap takes a negative value in dimension $m\ge2$. Throughout its domain, $E>\sum_jx_j$ follows by expanding $\prod_j (1-x_j)^{-1}$ and using $(1-x_j)^{-1}\ge1+x_j$, with strict inequality in at least one coordinate. Hence $L>0$. Also $R\le\rho(E+h)\le1$ because the product subtracted in $R$ is nonnegative. The infimum of the gap is bounded below by $-1$, so choose a minimizing sequence and take a subsequence in the compact closure $0\le x_j\le h\le1$. The possible boundary limits are as follows.

If all $x_j$ tend to zero then $E$ tends to zero. When $h\to0$, $R\le E+h\to0$, and if $h$ has a positive limit, direct substitution in $R$ gives $R\to0$. Since $L>0$, neither case gives a negative gap limit. If $\rho\to0$, then $E\to\infty$ and $L\to1$, while $R\le1$. If $h\to1$ with $E$ having a positive finite limit, then the subtracted fraction tends to $(E+1)\rho=1$ and $R\to0$. In the remaining boundary cases $h<1$ and $E$ is finite and positive. Continuity, the upper-face lemma, and induction after deleting zero coordinates exclude a negative limit there.

It follows that the negative infimum is attained in the open domain. At its fixed $E,h$ the fixed-product minimizer theorem shows that all coordinates are equal to some $x\in(0,h)$. The pair-stability threshold theorem gives $h\ge h_b>h_c$ at this minimum. On the other hand stationarity in $h$ gives $R'(h)=0$, because $L$ is independent of $h$, and the equal-coordinate critical-location theorem then gives $h<h_c$. The contradiction proves nonnegativity. Any interior equality would be an attained minimum with gap zero, so the same fixed-product reduction, pair-stability threshold and critical-location argument excludes it. This completes the induction and proves strictness.
