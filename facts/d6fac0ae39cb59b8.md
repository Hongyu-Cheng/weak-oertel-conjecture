---
fact_id: d6fac0ae39cb59b8
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-pk-w35-density-threshold-derivative
depends_on: []
verifier_run: 3affe00e0c01d04c
target_match: null
---

## Source

- [b5369aed13dad06b](../candidates/b5369aed13dad06b.json), b5369aed13dad06b:04 §3, (3)–(4), threshold derivative of a compact capped transport value.

## Statement

Let $\mathcal D$ be a nonempty weakly compact family of finite nonnegative laws on a compact physical set, all dominated by $B\omega$ for a finite measure $\omega$ and a finite constant $B\ge0$. For finitely many affine $\ell_j$ and real coefficients $c_j$, set $V(t)=\max_{\rho\in\mathcal D}\sum_j c_j\int(\ell_j-t_j)_+\,d\rho$ and let $\mathcal A(t)$ be its maximizers. If $\omega\{\ell_j=t_j\}=0$ for every $j$, then for every direction $v$,
$$
\lim_{\varepsilon\downarrow0}\frac{V(t+\varepsilon v)-V(t)}{\varepsilon}
=\max_{\rho\in\mathcal A(t)}\left[-\sum_j c_jv_j\rho\{\ell_j\ge t_j\}\right].
$$
If a repair identifies the unrestricted and capped optimal values at $t$ and all sufficiently nearby thresholds, the same formula holds for the unrestricted value.

## Proof

For one hinge the pointwise error after subtracting the linear term $-\varepsilon v_j\mathbf1_{\{\ell_j\ge t_j\}}$ is bounded by $|\varepsilon v_j|\mathbf1_{\{|\ell_j-t_j|\le|\varepsilon v_j|\}}$. Integrating gives $o(\varepsilon)$ uniformly by common domination and nullity of the cut. The finite sum therefore has a uniform expansion. Each cap is a continuity set for weak convergence within $\mathcal D$, so the linear term is continuous there.

The objective is continuous in the law and uniformly Lipschitz in the thresholds by the common finite mass bound, giving attained maxima and continuity of $V$. Using a maximizer at $t$ with largest linear term gives the lower bound. For the upper limit, take a weakly convergent subsequence of displaced maximizers along a sequence of positive displacements approaching zero. Its limit maximizes at $t$ by the uniform expansion and continuity of the objective. Subtracting $V(t)$ from the displaced maximum gives at most the corresponding linear term times $\varepsilon$ plus the uniform error, since the same law at $t$ has value at most $V(t)$. Dividing and passing to the subsequence limit proves the upper bound. Equality of the values near $t$ transfers the derivative directly. For nonnegative weights such equality follows if every unrestricted law has a capped convex-order improvement within the same feasible class.
