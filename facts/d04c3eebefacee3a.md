---
fact_id: d04c3eebefacee3a
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-pk-w33-compatible-birth-pooled-covariance-response
depends_on: []
verifier_run: efee28bd44407323
target_match: null
---

## Source

- [8b9ef51c1503d49a](../candidates/8b9ef51c1503d49a.json), 8b9ef51c1503d49a:03 §§2–3, (3)–(7).

## Statement

Let an actual complete convex birth preserve a finite family of old positive-volume $d$-fibers of total mixed volume $M>0$ and measure $\mu$, where $d\ge1$. Assume the only additional sampled fibers are $x_q+\varepsilon^{1/d}D_q$ at new bases $q$, with compact convex bodies $D_q$, $m_q=|D_q|$ and $\sum_q m_q=1$. Let $\nu=\sum_q m_q\delta_{(q,x_q)}$. Let $\Sigma_\varepsilon$ be the covariance pooled within individual fibers, i.e. the sum of their centered second moments divided by total mixed mass. With $\Sigma=\Sigma_0$, one has
$$
\Sigma_\varepsilon=\frac{M\Sigma+\varepsilon^{1+2/d}\sum_q m_q\operatorname{Cov}(D_q)}{M+\varepsilon},
\qquad
\Sigma'_+(0)=-\frac{\Sigma}{M}.
$$
In particular $\Gamma_\varepsilon(u)=\sqrt{u^{\mathsf T}\Sigma_\varepsilon u}$ has right derivative $-\Gamma_0(u)/(2M)$ at zero, uniformly on compact subsets of nonzero normals.

Fix a cap with margin $a\cdot(z-p)+u\cdot(x-y)$, $u\ne0$, scaled so $\Gamma_0(u)=1$, and a smoothing parameter $h>0$. Set $f(z,x)=[a\cdot(z-p)+u\cdot(x-y)]/h$, $\Psi(s)=\min(1,\max(0,1+s))$ and $A=\int f\mathbf1_{\{-1<f<0\}}\,d\mu$. The right derivative of the actual raw mass of the cap with profile $\Psi(f/\Gamma_\varepsilon(u))$ is $\int\Psi(f)\,d\nu+A/(2M)$, where $A\le0$. The born-fiber contribution is $\varepsilon\int\Psi(f)\,d\nu+o(\varepsilon)$ uniformly on finite normal menus and compact neighborhoods of their continuous marks.

## Proof

The centroid of a new fiber is $x_q+\varepsilon^{1/d}g_{D_q}$, where $g_{D_q}$ is the centroid of $D_q$. Translation cancels in centering. Changing variables in that fiber gives a factor $\varepsilon$ in volume and $\varepsilon^{2/d}$ in the centered second moment. The old numerator is $M\Sigma$, and the total is $M+\varepsilon$, which proves the covariance identity and its derivative. The old positive-volume fibers give $\Sigma$ positive definite, so Taylor expansion of the square root gives $\Gamma_\varepsilon(u)=\Gamma_0(u)(1-\varepsilon/(2M))+o(\varepsilon)$ uniformly on the stated normal sets.

The old contribution is $\int\Psi(f/\Gamma_\varepsilon(u))\,d\mu$. On each old fiber the two kink planes $f=-1,0$ are volume-null because $u\ne0$. The integrand difference quotients are bounded on the compact sampled support by Lipschitz continuity of $\Psi$ and the width expansion. Dominated convergence yields $A/(2M)$. For the new contribution, pull the integrals back to the fixed sets $D_q$. On each such set the argument of $\Psi$ differs from $f(q,x_q)$ by $O(\varepsilon^{1/d}/h)+O(\varepsilon)$ for fixed $h$, uniformly over the asserted menus and mark neighborhoods. The same Lipschitz bound therefore gives the claimed first-order mass. Adding the two contributions proves the formula.
