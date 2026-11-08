---
fact_id: df8f6bc3293dffe2
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-vanishing-buffer-ordinary-boundary-stress
depends_on: ["80c8de4539fbc253", "33dad4b1da4f3ba2", "a56f8711406a3870", "d90ba05577427854"]
verifier_run: 9a5b959749299e76
target_match: null
---

## Source

- [e2b434a53584fe7e](../candidates/e2b434a53584fe7e.json), e2b434a53584fe7e:05 §4, (12), weak boundary stress with a common position-test cone.
- [e2b434a53584fe7e](../candidates/e2b434a53584fe7e.json), e2b434a53584fe7e:04 §4, (8)–(11), correction and finite-body action.

## Statement

Let finitely many sampled positive convex $d$-fibers $K_z^j\subset RB_d$ with a common inball radius $r_b>0$ converge in Hausdorff distance to positive $K_z$. Write $dm_j$ and $dS_j$ for their summed mixed volume and boundary area, with endpoint counting if $d=1$. Let $M_j\ge M_*>0$ and let the pooled within-fiber covariance satisfy $\Sigma_j\ge\lambda_* I$. At each index use the same-coefficient contact data and exact physical density $\Xi_j$ of 80c8de4539fbc253. Assume $\Delta_j>0$, $\Delta_j\le S_{\max}\varepsilon_j$, $\varepsilon_j\downarrow0$, a uniform own ball radius $r_s$ at the positive contact sources, and $L_{j,\max}\le H\varepsilon_j^{-N}$ with $N=d+1$ and $H\ge1$. Write $B_j=-(\Delta_j/(NM_j))\log L_j$, let $S_*,S_{f,*}$ bound the total and individual fiber surface areas, and put $E_*=\kappa_d r_s^d$ for unit ball volume $\kappa_d$. Then, with $W_j$ the exact allocated cap load and $\beta_j$ the buffered maximum,
$$
\int_{\partial S_j}|\Xi_j-(W_j-\beta_j)|\,dS_j\le
\Delta_j\left(\frac{N^{N-1}S_{f,*}}{E_*}+\frac{2R^2S_*}{M_*\lambda_*}+\frac{(N+2)S_*}{2NM_*}\right)
+\int_{\partial S_j}|B_j|\,dS_j.
$$
This is $O(\varepsilon_j(1+\log(1/\varepsilon_j)))$. On every bounded speed $v$ in the same cone, the integral of $(W_j-\beta_j)v$ is at most the displayed bound times $\|v\|_\infty$. Assume moreover $\beta_j\to\beta_0$ and that each fixed globally finite convex function $\Phi(z,X)$ belongs to each common tested cone as an inward speed. Then on a subsequence $W_j dS_j\rightharpoonup w_0 dS_0$, $0\le w_0\le1$, and
$$
\int_{\partial S_0}\Phi(z,X)(w_0-\beta_0)\,dS_0\le0
$$
for every such $\Phi$. Affine tests of both signs give equality of the mass and full first moments of $w_0dS_0$ and $\beta_0dS_0$.

## Proof

The same-coefficient parameter rows from 80c8de4539fbc253, normalized by $\Delta_j$ as $\sigma_i=e_i/\Delta_j$, satisfy 33dad4b1da4f3ba2. Its trace estimate, multiplied by $\Delta_j/(NM_j)$, gives
$$
\int_{\partial S_j}|B_j|\,dS_j\le
\frac{\Delta_j}{Nr_b}\left(2d\log L_{j,\max}+\frac{2R}{r_s}\right).
$$
The optimizing denominator at a source has $P_a\ge1/N$ by a56f8711406a3870. Its energy is at least $E_*$, since every admissible denominator on the source fiber is admissible on the own ball and the center energy of the ball is its volume by d90ba05577427854. Each covariance-unit normal has Euclidean length at most $\lambda_*^{-1/2}$, and $|X-g_z|\le2R$. At regular boundary points $n\cdot(X-o_z)\ge r_b$ for an inball center $o_z$, so Gauss–Green gives $\sum_z|\partial K_z^j|\le d M_j/r_b$ and hence uniform total and individual surface bounds. Using $\sum_{ia}e_{ia}=\sum_i e_i=\Delta_j$ and $\sum_j\rho_{ij}=1$ in the density of 80c8de4539fbc253 gives the three displayed bounds for its projective, covariance and mass terms, respectively. The same density inequality gives the bounded-test error by integration against $v$.

Here the physical boundary measures converge weakly. For each fixed base choose a point interior to the limiting fiber as a common center for that fiber and its tail of approximants, with a smaller common centered inball. Translate it to zero. The convex gauges $p_j,p$ converge uniformly on compact sets by the support-function inclusions between small centered dilations of the limit. At any direction where all gauges are differentiable, $\nabla p_j\to\nabla p$ by the convex supporting inequalities and uniqueness of the limiting gradient. The exceptional directions have spherical measure zero because the gauges are positively homogeneous and differentiable off a Lebesgue-null set. With radial function $r_j(e)=1/p_j(e)$ and outer unit normal $n_j$ at $r_j(e)e$, the radial area formula gives Jacobian $r_j(e)^{d-1}/(n_j\cdot e)$. The denominator is uniformly bounded below by the common centered inradius divided by a common outer radius, and it converges almost everywhere because the normal is the normalized gauge gradient. Thus dominated convergence gives the weak convergence of physical area against every continuous test. In dimension one the two endpoints converge directly. Summing over the finite sampled bases preserves this convergence.

The exact selector satisfies $0\le W_j\le1$ by the nonnegative allocated weights summing to one. Its measures have a weakly converging subsequence on a common compact range, and the weak limit is dominated by $dS_0$ by the area convergence and the prelimit domination. This gives $w_0$. For each fixed finite convex $\Phi$, continuity and boundedness on the common compact range give the claimed limiting inequality from the bounded-test error. The same subsequence works for all such tests because its weak convergence is against every continuous test. Affine functions and their negatives yield the moment equalities.
