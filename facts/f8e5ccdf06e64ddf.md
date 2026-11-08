---
fact_id: f8e5ccdf06e64ddf
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-two-positive-scalar-envelope-upper-faces
depends_on: ["0758cf3d392ffdb6", "7cae55c49007d765", "716fa7580a098deb"]
verifier_run: b9837fd8ace36bc1
target_match: null
---

## Source

- [16db32a020dc6379](../candidates/16db32a020dc6379.json), §3, (5)–(6), rescaling and upper-face strictness.
- [2e27b7d358779b43](../candidates/2e27b7d358779b43.json), §1, (1)–(2), upper face, deletion and one-coordinate formula.

## Statement

For an integer $m\ge1$ and $0\le x_j\le h<1$ with some $x_j>0$, put $\rho=\prod_j(1-x_j)$, $E=\rho^{-1}-1$, and
$$
L=\left(1-\frac{\sum_j x_j}{E}\right)\prod_j(1+x_j/E),\qquad
R=\rho(E+h)\left[1-\frac{(E+h)\prod_j(h-x_j)}{h^{m+1}}\right].
$$

Also set $Q=\prod_j(1+x_j/E)$, $B=\sum_j x_j/(1-x_j)$, $C=B/(1-\rho)-1$, and $W=(1-h)CQ$.

If some $x_j=h$, both $L\ge R$ and $W\ge R$. On a face with exactly one coordinate equal to $h$, both inequalities are strict if another coordinate is positive and both are equalities if all other coordinates are zero. Deleting zero coordinates preserves both gaps. For $m=1$ and $0<x=x_1\le h<1$, the smaller-omission gap is
$$
W-R=\frac{x(h-x)(1-h)(2h+x-hx)}{h^2(1-x)} .
$$

## Proof

Deleting a zero preserves the product defining $\rho$, both coordinate sums, and $Q$. Its factor $h$ in the definition of $R$ cancels the lost denominator factor $h$. Thus both gaps are unchanged. For the one-coordinate formula substitute $E=x/(1-x)$, $C=E$, $Q=2-x$, and expand over $h^2(1-x)$.

First assume exactly one coordinate equals $h$. Remove any zeros and label the upper coordinate $x_m=h$. Fix $p>q>0$ with $q=p(1-h)$ and take old negative coefficients $-r_j=-q x_j/(h-x_j)$ for $j<m$. Their magnitudes are finite and strictly positive. Add a negative coefficient $-a$ with $a\to\infty$, so the resulting scalar $x_m(a)=ha/(q+a)$ tends to $h$. For either positive omission, the exact section identities give the finite variance gap as $X(a)/h$ times the corresponding scalar gap, where
$$
X(a)=\frac p{p+a}\prod_{j<m}\frac p{p+r_j}.
$$
Thus $aX(a)/h$ tends to a strictly positive finite constant. The scaled section-variance limit, applied with old sum $pY_p+qY_q-\sum_{j<m} r_jY_j$, gives $M(\prod_{i\ne k}\nu_i-P)\ge0$ for omission of $k=p$ or $k=q$ among the old indices. Here $M>0$, $P$ is the old cap probability and $\nu_i$ are its conditional means. The old sum has no atom at zero, so the equality statement of accepted fact 716fa7580a098deb applies to this old cap. If there is any strictly negative old phase, the old coefficients besides the selected positive phase include both signs, and the limit is strictly positive. If there is none, all coefficients of the old sum are positive, so $P=1$ and every $\nu_i=1$. The limit then vanishes. The scalar functions are continuous at the upper-face point because $h<1$ and $E>0$, so the positive scale yields exactly the asserted inequalities and equalities. If several coordinates equal $h$, keep one of them equal to $h$ and approach the point with all the other coordinates strictly below $h$. Continuity there gives the nonstrict conclusions.
