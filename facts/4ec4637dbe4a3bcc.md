---
fact_id: 4ec4637dbe4a3bcc
kind: counterexample
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-lattice-simplex-full-potential-cone-obstruction
depends_on: ["0143817849026887", "68c5513d4b6cae29"]
verifier_run: 81cb5f102f2cc1d6
target_match: null
---

## Source

- [d7fcf9727e1fd83d](../candidates/d7fcf9727e1fd83d.json), d7fcf9727e1fd83d:03 §3, (5)–(8), §4 scope; historical audit d3c738ffa3f1acc6 §§4–5.
- [8e69e6820cd6ee00](../candidates/8e69e6820cd6ee00.json), 8e69e6820cd6ee00:02 §§1–2, facetwise convex-order application, supplied here through 68c5513d4b6cae29.

## Statement

For each $d\ge2$, use the lattice product $C=D\times K$ and the $d+1$ actual critical caps $H_j$ just described in lattice-simplex-product-exact-critical-depth: $D=\operatorname{conv}\{(-1,\ldots,-1),e_1,\ldots,e_d\}$ and $K$ is a $d$-simplex with barycentric functions $\lambda_j$. On the sum $\eta$ of the $\mathcal H^{d-1}$ surface measures of all actual integer fibers, mark each point by the outward unit continuous normal $u$, defined off a null set. Let $W=(d+1)^{-1}\sum_{j=0}^d\mathbf1_{H_j}$. Over all finite nonnegative potentials $\Phi(u,z,x)$ measurable on this marked bundle and convex in $(z,x)$ for each fixed $u$, with finite positive denominator, one has
$
\sup_\Phi\frac{\int\Phi W\,d\eta}{\int\Phi\,d\eta}
=\frac{1+\gamma_d}{d+2}<\gamma_d,\qquad \gamma_d=(d/(d+1))^d .
$
The constant potential attains the supremum. The $d+2$ positive measured fibers have distinct parities and equal masses, so each attains equality in the singleton quota at mass fraction $1/(d+2)$.

## Proof

The same-package lattice-simplex-product-exact-critical-depth proves actual lattice completeness, criticality and equal response weights. In particular on each outer fiber $W=1/(d+1)$, and on the middle fiber $W_0=(d+1)^{-1}\sum_j\mathbf1_{\{\lambda_j\ge1/(d+1)\}}$. The center integral $A=\int_{\partial K}\Phi(u(x),0,x)\,d\mathcal H^{d-1}$ and the sum $T=\sum_{j=0}^d\int_{\partial K}\Phi(u(x),v_j,x)\,d\mathcal H^{d-1}$ use identical physical boundary points and normals on each fiber. Convexity at fixed $(u,x)$ and the barycenter $0=(d+1)^{-1}\sum_jv_j$ give $A\le T/(d+1)$.

On each facet $F$, the normal is constant, so the restriction $f(x)=\Phi(u,0,x)$ is a continuous convex test on $F$ (it is the restriction of a finite convex function on the ambient space). The $d$ nonempty cap pieces of $F$ are the contractions $\alpha F+(1-\alpha)v$ towards its own vertices $v$, where $\alpha=d/(d+1)$; the Jacobian is $\alpha^{d-1}$. Apply 68c5513d4b6cae29 in its parameter with $d$ vertex indices to this facet, using an affine identification with its standard simplex and normalized facet measure. The step $1-\alpha=1/(d+1)$ is within its allowed range $1/d$. Therefore the average of the integrals of $f$ under these $d$ vertex contractions is at most the uncontracted facet integral. Including the cap weight and Jacobian yields
$
\int_F fW_0\,d\mathcal H^{d-1}
\le \frac{d\alpha^{d-1}}{d+1}\int_F f\,d\mathcal H^{d-1}
=\gamma_d\int_F f\,d\mathcal H^{d-1}.
$
The faces meet in surface-null sets; summing yields a middle numerator at most $\gamma_dA$.

The total ratio is at most $[\gamma_d A+T/(d+1)]/(A+T)$. The positive denominator and $A\le T/(d+1)$ imply $T>0$. As a function of $A/T$ the bound is strictly increasing because $\gamma_d>1/(d+1)$ by the strict Bernoulli inequality for $d\ge2$. Its maximum on $[0,1/(d+1)]$ is $(1+\gamma_d)/(d+2)$, which is strictly below $\gamma_d$ by the same comparison. For $\Phi=1$, all fiber surface integrals are equal, and the middle cap-volume fractions on each facet give equality in the displayed facet bound, so the maximum is attained.

The outer parities are the distinct unit vectors and the all-ones vector, and the middle parity is zero, all different for $d\ge2$. Equal volumes therefore saturate all singleton quotas, and for any subset the mass fraction equals its parity count divided by $d+2$. No reassignment of positive weights on this same support can satisfy every strict singleton quota because the fractions sum to one. The normalized depth of this example is strictly larger than $\gamma_d/2^d$: $2^d\ge d+2$ for $d\ge2$, and $(1+\gamma_d)/(d+2)>\gamma_d/(d+2)$.
