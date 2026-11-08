---
fact_id: ecdacd6349c968ba
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-finite-plane-section-log-zero-normal
depends_on: ["6d669cc80ae962ed"]
verifier_run: d290ea1cd2824dcd
target_match: null
---

## Source

- [53c44db9ae559bfe](../candidates/53c44db9ae559bfe.json), 53c44db9ae559bfe:02 §§4–6, (9)–(12), tangential slab test and proper-section example.
- [4dd22db8fd75566e](../candidates/4dd22db8fd75566e.json), §6, truncated-triangle parameters used in the distinct collapsing proper-section calibration.

## Statement

In the moving-section setup of the positive-anchor lemma suppose $d\ge2$, $\sup_j\int_{K_j}1/L_j<\infty$, and $L_j=\min_{1\le r\le R}A_{rj}$ on $K_j$, where the finite affine components converge coefficientwise to $A_r(X)=b_r+c_r\cdot X$. If the allocated section-log defect is nonzero, then $\Pi=\{A_r=0\}$ for at least one $r$ with $c_r\ne0$. In particular $u$ is parallel to $c_r$, the entire exposed face $K\cap\Pi$ lies in $\{L=0\}$ and has dimension at most $d-2$, and the limit incidence is inside supporting if $u$ is a positive multiple of $c_r$, outside supporting if it is a negative multiple.

Both orientations are possible even for sections proper at every sufficiently late index. For $a=1/m$, $\eta=2^{-m}$, $K_m=\{x,y\ge0:a\le x+y\le1\}$ and $L_m=x+y-a+\eta$, the section $x+y=a+\eta^2$ has ordinary coarea $a+\eta^2\to0$ for raw normal $(1,1)$, and its negative-log weighted coarea tends to $\log 2$. Reversing the normal or multiplying $L_m$ by positive constants whose logarithms are bounded preserves that limit.

## Proof

Assume no $A_r$ vanishes identically on $\Pi$. For a component whose restriction to $\Pi$ has nonzero tangential gradient, its restriction to $\Pi_j$ has tangential gradient norm at least some $\gamma_r>0$ for all large $j$. On $D_j$, $A_{rj}\ge L_j>0$. The portion of $D_j$ where $A_{rj}<t$ thus lies in an intrinsic slab of width $t/\gamma_r$. Fubini and the common outer radius bound its $(d-1)$-area by a constant times $t$, also when $d-1=1$. If instead the limiting tangential gradient vanishes, the limiting restriction is a constant. For infinitely many nonempty sections it is nonnegative by taking a converging sequence of section points. It is positive by the assumed absence of a zero restriction. Coefficient convergence, bounded section points and convergence of the planes give a uniform positive floor for that component on the current sections. An eventually empty sequence has zero defect.

The finite union of the component sublevel sets therefore has area $O(t)$ for small $t$, uniformly in all large $j$. The layer-cake estimate of the positive-anchor lemma, with the coarea factor bounded by $b_*^{-1}$, shows uniform integrability and hence zero defect. The contrapositive yields a component vanishing on $\Pi$. It cannot vanish identically on the fiber since $L>0$ in the interior. Its zero plane is consequently $\Pi$ and its gradient is parallel to $u$. Since it is nonnegative on $K$ and $L\le A_r$, the entire supporting face is zero. The dimension assertion follows from the inverse-integral part of the positive-anchor lemma. The sign of the proportionality specifies whether the closed halfspace contains the whole fiber or only the zero face. With finitely many sampled bases this argument is applied separately using the actual threshold in each fiber.

For the example put $s=x+y$. Fubini in $(x,s)$ gives $\int_{K_m}1/L_m=\int_a^1 s/(s-a+\eta)\,ds=1-a+(a-\eta)\log((1-a+\eta)/\eta)\le1+\log 2$. The fibers and affine parameters converge as required. The proper section has length $\sqrt2(a+\eta^2)$, and its coarea divides this by $\sqrt2$. The parameter is $\eta(1+\eta)$ on the section. The weighted coarea is therefore $(a+\eta^2)(m\log 2-\log(1+\eta))\to\log 2$, with all points converging to the zero vertex. Reversal preserves the actual coarea. Bounded logarithms of scalar normalizers change the negative-log weight by at most a bounded constant times the vanishing ordinary section mass.
