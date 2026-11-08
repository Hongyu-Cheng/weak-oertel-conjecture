---
fact_id: d3c5fb55ec5bc99d
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-smooth-deepest-circuit-quantile-response
depends_on: ["0a03438ff4e94ff8", "1fa8cb387c27b040"]
verifier_run: addc5e30ca152c22
target_match: null
---

## Source

- [a0fdd477aa859374](../candidates/a0fdd477aa859374.json), a0fdd477aa859374:03 §3, (3)–(4), smooth circuit response and universal selection.

## Statement

In the touching deepest-circuit quantile comparison, suppose each selected cap mass has a joint first-order expansion at $(p_0,b_j)$ with shape term $B_j(\delta)$ and threshold derivative $-S_j<0$ (for the unit continuous normal), and the total mass has derivative $M'(\delta)$. The raw circuit cover mass derivative is

$\tau_c'(\delta)=\frac{\sum_j(\rho_j/S_j)B_j(\delta)}{\sum_j \rho_j/S_j}.$

If the old family is a local minimum of actual maximal normalized depth $\beta$, then in every feasible first direction $\delta$ and for every choice of one such circuit at each old deepest base,

$\max_{z\in Z}\big[\tau_{c_z}'(\delta)-\beta M'(\delta)\big]\ge0.$

For an open parameter domain with linear derivatives, every selection of these response functionals, one for each old deepest base, has zero in its convex hull. The same holds if each base's available rows are replaced by their closed convex hull. When there is just one deepest base, each of its available response functionals vanishes identically in this open linear setting.

## Proof

For a given body direction $\delta$ and mass direction $a$, quantile Lipschitz continuity bounds the threshold change by the size of the parameter and mass changes. Substitution into the joint first-order expansion of the identity $F_j(p,Q_j(p,\tau))=\tau$ therefore gives the quantile derivative $(B_j(\delta)-a)/S_j$. The circuit root is locally Lipschitz, so substituting its mass change into the weighted threshold identity gives

$0=\sum_j(\rho_j/S_j)\bigl(B_j(\delta)-\tau_c'(\delta)\bigr).$

The sum of the weights in this expression is strictly positive, giving the formula. The argument works along feasible curves $p(t)=p_0+t\delta+o(t)$, $t\downarrow0$, with the assumed expansions.

At a local minimum, the touching upper comparison must itself be at least $\beta$ along every feasible path. Equivalently $\max_z[\tau_{c_z}(p)-\beta M(p)]\ge0$ there, with each term zero at $p_0$. Differentiating the finite maximum from the right at this tie gives the stated inequality. This uses only the upper comparison and does not differentiate actual maximum depth.

For an open parameter domain with linear derivatives, all directions are feasible. If the finite convex hull of a selected family of linear functionals omits zero, strict separation gives a direction in which every selected row is strictly negative, a contradiction. If rows from the per-base closed convex hulls were all strictly negative in some direction, continuity of evaluation and linearity of each finite convex combination would give one strictly negative original row at each base. That too contradicts the inequality. A singleton selection at a unique deepest base then forces its only selected functional to be zero.
