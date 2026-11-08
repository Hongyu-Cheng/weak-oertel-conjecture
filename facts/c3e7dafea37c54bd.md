---
fact_id: c3e7dafea37c54bd
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-zero-buffer-rigidity-at-ordinary-minimum
depends_on: ["b22db3535d2a902a", "9583fbdf100e75ef", "43ed87d91b76249c", "55a57b1cf55d0c87", "d90ba05577427854"]
verifier_run: f59020f07451441f
target_match: null
---

## Source

- [cebc39c4f5ccbc96](../candidates/cebc39c4f5ccbc96.json), §5.

## Statement

Let $C$ be an ordinary local minimum of normalized maximum closed-halfspace depth under all actual positive compatible fixed-base Hausdorff perturbations, with finite nonempty real base $P$, $d\ge1$, and total sampled volume $M$. For each $p\in P$, let $h_p$ be a finite nonnegative concave function on $\operatorname{int}K_p$. Assume that for every anchored convex representation $p=\sum_z\lambda_z z$ and all $y_z\in\operatorname{int}K_z$ with $\lambda_z>0$, one has $h_p(\sum_z\lambda_z y_z)\ge\sum_z\lambda_z h_z(y_z)$. Define the physical displacement on caps at $(p,y)$ by $(h_p(y)E_{K_p}(y)/M)^{1/(d+1)}\Gamma(u)$ at own-interior marks and by zero on the own boundary, where $\Gamma$ is a positive definite norm on continuous covectors. Keep pure-base caps unchanged. If the supremum buffered raw depth equals the ordinary raw maximum, then every $h_p$ vanishes on $\operatorname{int}K_p$. If the $h_p$ are defined, nonnegative and concave on the closed fibers, they also vanish on the closed fibers.

## Proof

Ordinary depth attains its maximum by 43ed87d91b76249c. Each ordinary deepest mark is own-interior with positive energy. Indeed a centered inball yields strictly positive depth somewhere, and by 55a57b1cf55d0c87 each compatible own boundary has ordinary depth zero. That fact applies to the actual compatible family and a rank-zero base may be embedded as a singleton in $\mathbb R$. Through-mark caps after this embedding give exactly the original traces. Positivity of energy at an interior mark is d90ba05577427854.

If $h_p$ were positive at an ordinary deepest mark, the strict interior buffer lemma would force the buffered supremum to exceed the ordinary maximum. Thus $h_p$ vanishes at an interior point over each deepest base $p$. A nonnegative concave function with an interior zero is identically zero on its domain. For any given point of the domain, continue the segment through the interior zero a short distance and apply concavity to the resulting convex combination.

For every sampled $z$ on the minimal face $F_p$ of a deepest base $p$, relative interior of $p$ in $F_p$ gives an anchored convex representation of $p$ with a positive coefficient at $z$ (take $z=p$ directly, or continue a short distance in $F_p$ beyond $p$ from $z$). Choose own-interior input marks in every positive-weight fiber. Their combination is interior to $K_p$ by actual compatibility and the Minkowski combination of interior balls. Nonnegativity and the assumed anchored inequality therefore force $h_z$ to vanish at any chosen interior input over $z$. The ordinary deepest-face exhaustion theorem covers all of $P$ by these faces. This proves the conclusion on the interiors, and the same interior-zero argument gives it on any nonnegative concave extensions to the closed fibers.
