---
fact_id: cf17d6bf1aab7a2d
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-regular-singleton-density-affine-nullity
depends_on: ["064f212eedef754c", "dc4933b776585ce0", "10622d8f953f3ff0", "d90ba05577427854", "a56f8711406a3870"]
verifier_run: d7ecc682801789d4
target_match: null
---

## Source

- [a7b11eee1eaaf72e](../candidates/a7b11eee1eaaf72e.json), a7b11eee1eaaf72e:04 §3, (4)–(5), regular singleton dual density.
- [a7b11eee1eaaf72e](../candidates/a7b11eee1eaaf72e.json), a7b11eee1eaaf72e:05 §4, (6)–(8), individual affine nullity.

## Statement

Use the accepted exact energy-only regular buffered cover continuation on a finite lattice-complete positive compatible family. Let $M=\sum_z|K_z|$, $Q=\beta M$ be its old raw buffered maximum, $N=d+1$, $\Sigma$ the old within-fiber covariance, and $g_z$ the ordinary centroid of $K_z$. For group $i$, let the positive weights $\rho_{ij}$ sum to one and the selected continuous covectors satisfy $u_{ij}^{\mathsf T}\Sigma u_{ij}=1$. Write $S_{ij}>0$ for the mixed coarea of its proper sections, $B_i=\sum_j\rho_{ij}/S_{ij}$, and $\theta_{ij}=(\rho_{ij}/S_{ij})/B_i$. Assume every chosen cap has only proper, strict full or empty, or zero-surface-area supporting traces, with a proper own trace. The assigned contact faces are then singletons, with at most $k(P)\le 2^n$ groups. Denote the source by $(p_i,y_i)$, its own projective optimizer by $a_i$, $P_i(X)=1+a_i\cdot(X-y_i)$ on $K_{p_i}$, and its energy by $E_i$. Put $\delta_i=\varepsilon(E_i/M)^{1/N}/B_i$, where $\varepsilon>0$. For any fixed real dual weights $\eta_i$ define
$$
\begin{aligned}
W_i(z,X)&=\sum_j\theta_{ij}\kappa_{ij}(z,X),\\
\Xi_z(X)&=\sum_i\eta_i\left[W_i(z,X)-\beta+
\delta_i\left(\frac{\mathbf1_{z=p_i}P_i(X)^{-N}}{NE_i}
+\frac{\sum_j\rho_{ij}[u_{ij}\cdot(X-g_z)]^2}{2M}
-\frac{N+2}{2NM}\right)\right],
\end{aligned}
$$
where $\kappa_{ij}$ is the physical regular fixed-cap selector and the projective term is used only when $z=p_i$. For any actual bounded signed radial speed $v$, the corresponding linear combination of the normalized budget decrease coefficients multiplied by $M$ is $\sum_z\int_{\partial K_z}\Xi_zv_z\,dS$. Each individual group coefficient vanishes on $v_z(X)=-n_z(X)\cdot(A X+Bz+c)$ for arbitrary common $A,B,c$, where $n_z$ is the old outward unit normal.

## Proof

The fixed change $X'=\Sigma^{-1/2}X$ reduces the old covariance-unit norm to the Euclidean unit norm. The regular selected cap meets the old body boundaries in surface-null cutting traces and has positive total proper coarea. Thus 064f212eedef754c identifies singleton faces and bounds the group count. In original coordinates it gives the section barycenters $\bar z_{ij}=p_i$ and $\bar X_{ij}=y_i-\varepsilon f_i\Sigma u_{ij}$, where $f_i=(E_i/M)^{1/N}$. In fact the Euclidean unit covector after whitening is $\Sigma^{1/2}u_{ij}$, and pulling back the displacement gives $\Sigma u_{ij}$. The balance $\sum_j\rho_{ij}u_{ij}=\varepsilon f_i a_i$ follows by differentiating the weighted old margin at its interior own-fiber zero, using $\nabla_X\log E=Na_i$ from a56f8711406a3870. The quantile representation used in 064f212eedef754c applies to the same source caps: whitening and the fixed mass factor change neither regularity nor the common contact threshold.

Write $D=\sum_z\int v_z\,dS$, $L_{ij}=\sum_z\int \kappa_{ij}v_z\,dS$, $C_i=\int_{\partial K_{p_i}}P_i^{-N}v_{p_i}\,dS$, and $J_i=\sum_z\int_{\partial K_z}\sum_j\rho_{ij}[u_{ij}\cdot(X-g_z)]^2v_z\,dS$. Combining 10622d8f953f3ff0 at its sole contact with dc4933b776585ce0 gives the group response
$$
\Lambda_i(v)=\sum_j\theta_{ij}L_{ij}+\delta_i C_i/(NE_i)+\delta_i J_i/(2M)
-\bigl[\beta+\delta_i(N+2)/(2NM)\bigr]D .
$$
Each kernel is bounded on the old boundaries, since $P_i$ is positive on its compact own fiber. Substituting the four integrals gives the displayed density.

The maps $(z,X)\mapsto(z,(I+tA)X+t(Bz+c))$ are invertible for small signed $t$ and preserve compatible families and base labels. Their signed inward speeds are as stated. Write $V_z(X)=A X+Bz+c$, $V_i=V_{p_i}(y_i)$, and $R_i=\sum_j\rho_{ij}u_{ij}^{\mathsf T}A\Sigma u_{ij}$. The divergence theorem gives $D=-M\,\operatorname{tr}A$. Applied to the captured part of each fiber it gives
$$
L_{ij}=-Q\,\operatorname{tr}A-S_{ij}u_{ij}\cdot(A\bar X_{ij}+B\bar z_{ij}+c),
$$
because the internal cutting boundary has outward unit normal $-u_{ij}/\|u_{ij}\|$. For a strict full trace only the divergence term remains; for an empty trace both terms vanish. A zero-area supporting trace contributes no internal cutting flux. Use the section means above and $\theta_{ij}S_{ij}=\rho_{ij}/B_i$ to obtain $\sum_j\theta_{ij}L_{ij}=-Q\,\operatorname{tr}A-\delta_i(a_i\cdot V_i-R_i)$.

For the energy term, apply the divergence theorem to $P_i^{-N}V_{p_i}$. The escort identities from d90ba05577427854 give $\int P_i^{-N-1}=E_i$ and $\int (X-y_i)P_i^{-N-1}=0$. Hence $C_i/E_i=-\operatorname{tr}A+Na_i\cdot V_i$. The divergence calculation for the centered quadratic gives $J_i=-M\,\operatorname{tr}A-2M R_i$: the centered first moments vanish, $\sum_z\int [u_{ij}\cdot(X-g_z)]^2\,dX=M$ for each covariance-unit covector, and the linear-motion term integrates to $M u_{ij}^{\mathsf T}A\Sigma u_{ij}$. The three correction terms in $\Lambda_i$ now add to $\delta_i(a_i\cdot V_i-R_i)$. The trace terms cancel by $Q=\beta M$, and the resulting $\Lambda_i$ is zero.
