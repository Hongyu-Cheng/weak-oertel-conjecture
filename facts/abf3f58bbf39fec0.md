---
fact_id: abf3f58bbf39fec0
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-ordinary-cubic-tight-triangle-strict-ear-derivative
depends_on: ["30b8893e87b71b65", "1b85130a86bb0f82", "e27a258b6ac11bb2"]
verifier_run: 3f8f9e5e9018c8e6
target_match: null
---

## Source

- [3d7872ba08080216](../candidates/3d7872ba08080216.json), §§5–6, (9)–(11), substitution and strict derivative at every interior peak.

## Statement

Let $T$ be a nondegenerate triangle with fixed interior point $y$ and nonzero spanning normals $v_i$ summing to zero. Assume the through-source caps strictly isolate distinct vertices $P_i$ and $\Psi(T)=4$, where $\Psi=\sum_i f_i^2+\prod_i f_i$, $f_i=2\sqrt{kQ_i}/(\sigma_i\sum_jQ_j/\sigma_j)$, $k$ is area, $Q_i$ are cap areas and $\sigma_i$ are coarea chord lengths. Fix any edge $P(t)=(1-t)P_i+tP_j$ and an outward vector $w$ with $|\det(P_j-P_i,w)|=1$. For every fixed $0<\theta<1$ and $\eta>0$, the right derivative of $\Psi(\operatorname{conv}(T\cup\{P(\theta)+\varepsilon\eta w\}))$ at $\varepsilon=0$ is strictly negative. For the unit-height ear $\eta=1$, the derivative is bounded above by a strictly negative number on any fixed compact subinterval of peak positions in $(0,1)$. The conclusion includes the two cut-crossing peak positions.

## Proof

Use the exact cubic edge-variation and ear criterion for the present strict incidence and $\Psi=4$. Let $H=\sum_\ell v_\ell\cdot(P_\ell-y)$, $a_\ell=v_\ell\cdot(P_\ell-y)/H$, and $L_{\ell m}=v_\ell\cdot(P_\ell-P_m)/H$. The vertex-cap and cycle formulas of the ordinary circumellipse characterization give $f_\ell^2=4L_{\ell m}L_{\ell n}$ for distinct $\ell,m,n$ and equality of the two cycle products. Balance of the vertex-margin columns gives
$$
L_{is}+L_{js}=1,\quad L_{ji}+L_{si}=1,\quad L_{ij}+L_{sj}=1.
$$
Indeed, if $b_{\ell m}=-v_\ell\cdot(P_m-y)/H$, then $L_{\ell m}=a_\ell+b_{\ell m}$ and $\sum_{\ell\ne m}b_{\ell m}=a_m$, with $\sum_m a_m=1$.

Put $p=L_{ij}$, $q=L_{ji}$, $D=p+q-2pq$, $F=p(1-q)/D$, and $G=q(1-p)/D$. The displayed sums and strict drops give $p,q,F,G\in(0,1)$ and $F+G=1$. The cycle equation $pL_{js}(1-q)=qL_{is}(1-p)$ yields $L_{is}=F$ and $L_{js}=G$. Consequently
$$
f_i^2=4pF,\quad f_j^2=4qG,\quad f_s^2=4(1-p)(1-q),\quad
P:=\prod_\ell f_\ell=\frac{8pq(1-p)(1-q)}{D}.
$$
For $C=8+P$ and $E_\ell=2f_\ell^2+P$, substitution gives $C=8(p+q-pq)(1-pq)/D$, $E_i/C=p(1-q)/(1-pq)$ and $E_j/C=q(1-p)/(1-pq)$.

Set $U=a_i/p$, $V=a_j/q$, and $r=FG(1-p)(1-q)/(1-pq)$. Then $b=U$ and $a=1-V$ are the two crossings in the edge criterion. Thus $0<U,V<1$, $U+V-1>0$, and $0<r<FG$ because $(1-pq)-(1-p)(1-q)=D>0$. The intercept formula gives $T_i=\sqrt{k/Q_i}=f_i/(2a_i)$. Using the formulas for $E_i/C$ and $f_i^2$ in the unique-area coefficient gives
$$
\frac{\alpha_i}{C/(2k)}
=1+\frac{E_i f_i^2}{4C a_i^2}-\frac{f_i^2}{2a_i}
=\frac{(U-F)^2+r}{U^2}.
$$
For the last equality the coefficient of $U^{-2}$ before completing the square is $F(1-q)/(1-pq)=F^2+r$. Interchanging $p,q$ and $F,G$ gives $\alpha_j/(C/(2k))=((V-G)^2+r)/V^2$. Call these two normalized coefficients $A,B$; then $\beta_s/(C/(2k))=A+B-1$ by the edge-variation formula.

The strict scalar ear inequality applies at $U,V,F,r$ because $G=1-F$. Multiply it by $C/(2k)>0$ and use $a=1-V$, $1-b=1-U$ and $b-a=U+V-1$. The result is the strict version of the exact ear criterion. Therefore all unit-height triangular ear derivatives are negative. The actual convex hull has precisely this scaled triangular roof for sufficiently small positive $\varepsilon$ at fixed $\theta$, since the new tip remains inside the other two edge halfplanes. Positive rescaling gives the assertion for $\eta>0$. The Green potential formula is continuous in $\theta\in(0,1)$ and dividing by $\theta(1-\theta)>0$ preserves continuity. Compactness gives the uniform strictly negative bound claimed.
