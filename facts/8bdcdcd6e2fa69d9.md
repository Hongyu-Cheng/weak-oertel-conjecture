---
fact_id: 8bdcdcd6e2fa69d9
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-simplex-capacity-threshold-schur-complement
depends_on: ["aef64d0fab6e1fa1", "d2ba4e3cbd6eb730", "3e6e1eb15d927db8", "511d89569241b0d6"]
verifier_run: ae4ed9a87a4dec39
target_match: null
---

## Source

- [a5d3d44181ebed82](../candidates/a5d3d44181ebed82.json), §§2, 4, 4a, (3)–(7), (9)–(15).

## Statement

Let $d\ge2$, and let a strictly positive row $x$ have a proper minimizing threshold for the uniform-simplex capacity $\phi_d(x)=\inf_{t>0:F_x(t)>0}t/F_x(t)^{1/d}$, where $F_x(t)=\Pr(x\cdot U\le t)$. Rescale the row and threshold so that this threshold equals $1$. Write $\mathbf 1=(1,\ldots,1)$, $c=\mathbf 1-x$, $V=\sum_jc_jE_j$ for independent unit exponentials, $P=P(c)=\Pr(V\ge0)$, $g=\nabla P(c)$, and $H=\nabla^2P(c)$. Set $\eta=H\mathbf 1$, $B=d(d-1)P-\mathbf 1^\mathsf{T}H\mathbf 1$, and $K=P^{-1/d}/(dP)$. Then the minimizing section strictly captures at least two vertices, $\mathbf 1^\mathsf{T}g=dP$, and
$$
B=d(d-1)[P+f_V'(0)]>0 .
$$
The capacity is locally $C^2$ and
$$
\nabla^2\phi_d(x)
=K\left[\frac{d+1}{dP}gg^\mathsf{T}-H-\frac{(\eta-dg)(\eta-dg)^\mathsf{T}}{B}\right].
$$
In particular, for $g\cdot v=0$ and any real $s$,
$$
(v+s\mathbf 1)^\mathsf{T}\nabla^2\phi_d(x)(v+s\mathbf 1)
=-K\left[v^\mathsf{T}Hv+\frac{(\eta\cdot v-sdP)^2}{B}\right].
$$

## Proof

Properness gives coefficients of both signs. The independent gamma representation $V=G(c\cdot U)$, with $G$ of shape $d+1$, gives $f_V(0)=f_{c\cdot U}(0)/d$ using the bounded projection density and its continuity at zero, as in the joint cap derivative lemma. The same identity applies when there is only one positive phase: conditioning on the other phases gives a continuous density at zero because there is a strictly negative coefficient, and the proper-cut first variation gives continuity of the projection density there. Threshold stationarity for $L(x,t)=tF_x(t)^{-1/d}$ gives $\partial_t F_x(1)=dF_x(1)=dP$. By the projection identity this means $f_V(0)=P$.

If only $c_p>0$, write $Y=-\sum_{c_j<0}c_jE_j>0$ almost surely. Conditioning gives $P=\mathbb E[e^{-Y/c_p}]$ and $f_V(0)=P/c_p$, so stationarity requires $c_p=1$, contrary to $x_p>0$. There are therefore at least two positive coefficients and one negative. The joint cap derivative lemma applies, and gives $\mathbf 1^\mathsf{T}g=dP$. Accepted fact 511d89569241b0d6 gives the positive $C^1$ log-concave density $f=f_V$.

Put $\ell=f'(0)/f(0)$. Log-concavity gives $f(z)\le f(0)e^{\ell z}$ for $z\ge0$. Since $\int_0^\infty f(z)\,dz=P=f(0)$, $\ell<-1$ is impossible. If $\ell=-1$, equality of the integrals and continuity force equality in the bound for all $z\ge0$. Every positive $c_j$ is strictly below one, so one can choose $\lambda>1$ with $\lambda c_j<1$ for all $j$. Independence gives the finite moment $\mathbb E[e^{\lambda V}]=\prod_j(1-\lambda c_j)^{-1}$, which the putative rate-one tail would make infinite. Hence $f'(0)>-P$.

Write $f_L$ for the density of $c\cdot U$. Shifting $c$ by $s\mathbf 1$ shifts $c\cdot U$ by $s$, so $\mathbf 1^\mathsf{T}H\mathbf 1=-f_L'(0)$, and joint $C^2$ gives $C^1$ regularity of $f_L$ near zero. Differentiating the gamma mixture at zero gives
$$
f_V'(0)=f_L'(0)\mathbb E[G^{-2}]=\frac{f_L'(0)}{d(d-1)}.
$$
For justification, write $f_V(z)=\mathbb E[G^{-1} f_L(z/G)]$ near zero and split the difference quotient at $G=|z|/\delta$ where $f_L$ is $C^1$ on $[-\delta,\delta]$. The boundedness of $f_L$ and the gamma density $O(G^d)$ make the small-$G$ part $O(|z|^{d-1})$. On the remaining part, the difference quotient is bounded by a constant times $G^{-2}$, integrable for $d\ge2$. Dominated convergence proves the derivative formula. Therefore $B=d(d-1)[P+f_V'(0)]>0$.

Now $F_x(t)=P(t\mathbf 1-x)$ and $L(x,t)=tP(t\mathbf 1-x)^{-1/d}$. Differentiation before optimization at $t=1$ gives
$$
L_{xx}=K[(d+1)gg^\mathsf{T}/(dP)-H],\qquad
L_{xt}=K(\eta-dg),\qquad L_{tt}=KB.
$$
Here threshold stationarity and $\mathbf 1^\mathsf{T}g=dP$ have been used. The implicit-function theorem at the strict threshold minimum yields a local $C^1$ critical-threshold function. The unique-threshold lemma gives convergence of nearby minimizers to this proper threshold, so the implicit branch is the actual optimizing threshold. Differentiating the envelope gradient yields the Hessian $L_{xx}-L_{xt}L_{tt}^{-1}L_{tx}$. Substituting $\mathbf 1^\mathsf{T}g=dP$ and $\mathbf 1^\mathsf{T}H\mathbf 1=d(d-1)P-B$ into its quadratic form on $v+s\mathbf 1$ and collecting terms gives the displayed square. In particular the common-shift direction has strictly negative value $-Kd^2P^2/B$.
