---
fact_id: 74ecbee5a0bb3cc0
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-pk-w36-rates-zero-rate
depends_on: ["8eea7c194b7d234f"]
verifier_run: ca7a86b8923f3cb8
target_match: null
---

## Source

- [e90eb0947d2b9feb](../candidates/e90eb0947d2b9feb.json), e90eb0947d2b9feb:06 §8, (14)–(16).

## Statement

Use the hypotheses and actual geometric groups of the positive-rate group kernel. Assume the ordinary limiting boundary logarithm is integrable on $\partial K$. From the same joint limits let $\zeta_i^{\,0}$ and $\beta_G^{\,0}$ be the restrictions of the actual inverse-cell and exterior group measures, respectively, to $\{X:L(X)=0\}$ with every rate retained. Write $\mu_G^{\,0}=\pi_*\beta_G^{\,0}$. Each nonzero $\beta_G^{\,0}$ has the same determined normal $-c_i/\lVert c_i\rVert$ as in the positive-rate theorem. The full kernel, with $U_0=\delta_0$, is
$$
M\sum_{i\in G}\lVert c_i\rVert\zeta_i^{\,0}(dX,ds)=\int_{R\ge0} U_R(ds)\,\mu_G^{\,0}(dX,dR).
$$
In particular $M\sum_{i\in G}\lVert c_i\rVert\zeta_i^{\,0}(dX,\{0\})=\mu_G^{\,0}(dX,\{0\})$.

## Proof

The full joint exterior limit dominates each exterior group limit. Off $\{L=0\}$ it is the ordinary positive logarithmic trace with rate zero. Indeed the unweighted normal-bundle area converges weakly and the weights converge uniformly on each compact subset of $\{L>0\}$. Normal-bundle area convergence here follows by using radial graphs about a common inball center: the gauges converge uniformly on compact sets, their gradients converge at almost every sphere direction by the subgradient inequalities, and the area Jacobian $\rho_j(v)^{d-1}/(n_j(v)\cdot v)$ is uniformly bounded by the outer and inball bounds. Thus the group limit off $\{L=0\}$ is dominated by the integrable ordinary trace. The full inverse limit off $\{L=0\}$ is likewise the ordinary inverse measure at rate zero by bounded local weights and convergence of body indicators. Its integrability follows from Fatou and the inverse-mass bound. All defects of the actual cell and boundary trace $i$ are on $A_i=L=0$ by coefficient convergence.

For $T>0$ use $F_{j,T}=[\ell_j-T]_+$ with $\ell_j=(-\log L_j)_+$. On cell $i$ its gradient is $-\mathbf1_{\{L_j<e^{-T}\}}c_{ij}/A_{ij}$ almost everywhere. Apply Gauss–Green to $\phi F_{j,T}$ on the cells in $G$. Intragroup interfaces cancel by continuity. The intergroup terms tend uniformly to zero as $T\to\infty$ by the intergroup logarithmic tails proved in the group theorem. The bulk test-gradient terms have the same bound from bulk-log uniform integrability.

For the exterior term write $F_{j,T}=q_T(L_j)\ell_j$, where $q_T(s)=[1-T/(-\log s)]_+$ for $0<s<1$, equals one for $s\le0$ and equals zero for $s\ge1$. This is continuous on the common bounded ambient parameter range. First pass $j\to\infty$ by coefficient convergence and weak convergence of the exterior group measures. The coefficient equals one on the defect, while the ordinary term tends to zero as $T\to\infty$ by trace integrability. For the volume term take $T$ tending to infinity through continuity levels for every limiting inverse measure under $L$. The excluded levels are countable, and uniform parameter convergence passes the cutoff at every remaining level. Sending $T\to\infty$ then keeps exactly the full zero-set defects. This proves
$$
-\int\phi n\,d\beta_G^{\,0}=M\sum_{i\in G}c_i\int\phi\,d\zeta_i^{\,0}.
$$

The boundary coarea estimate in the group theorem bounds the whole logarithmic mass in arbitrarily small affine collars away from parallel normals, regardless of the rate. Applied to the weak actual trace limits over $A_i=0$, it forces the same parallelism for $\beta_G^{\,0}$. The common inball again forces the negative sign. If all gradients of a group are zero, all its limiting parameters are positive constants and both defects vanish. Otherwise dot the preceding identity with the common negative unit normal to obtain equality of the spatial marginals of $M\sum_{i\in G}\lVert c_i\rVert\zeta_i^{\,0}$ and $\mu_G^{\,0}$. The positive-rate restrictions are related by the preceding theorem, and $U_R$ preserves each spatial marginal and has zero mass at zero when $R>0$. Subtract the spatial marginals of the positive-rate identities from the full marginals. This gives the displayed equality at zero and proves the full kernel.
