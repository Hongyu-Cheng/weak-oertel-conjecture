---
fact_id: bd0a8fbcb2d1cc47
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-tight-planar-lorentz-triangle-parametrization
depends_on: ["a19fb2ae234afb2a"]
verifier_run: f702ef545d17fe4b
target_match: null
---

## Source

- [cfb017a0e12acfbf](../candidates/cfb017a0e12acfbf.json), §1, (1)–(2).

## Statement

For a planar convex body $K$ containing $0$ in its interior and three nonzero spanning normals $v_1+v_2+v_3=0$, write
$$
k=|K|,\qquad Q_i=|K\cap\{v_i\cdot x\ge0\}|,\qquad
\sigma_i=\mathcal H^1(K\cap v_i^\perp)/\lVert v_i\rVert .
$$
Set $M=\sum_iQ_i/\sigma_i$, $f_i=2\sqrt{kQ_i}/(\sigma_i M)$ and $\Phi_i=f_i+(f_j+f_l)^2/4$ where $\{i,j,l\}=\{1,2,3\}$. A triangle has strict distinct-vertex incidence if cap $i$ contains its vertex $P_i$ in its open halfplane and excludes both other vertices strictly.

Use the normals $(1,0),(0,1),(-1,-1)$. The canonical vertices for row $1$ are
$$
P_1=(2v+w,-v-w),\qquad P_2=(-x,x+s),\qquad P_3=(-x,-s-w),
\qquad x,s,v>0,\quad w\ge0.
$$

Every strict distinct-vertex triangle with $\Phi_1=2$ for these normals has this form after possibly exchanging caps $2$ and $3$ by $(X,Y)\mapsto(X,-X-Y)$. Conversely every displayed choice has strict distinct-vertex incidence and $\Phi_1=2$.

Put $p=2v+w$, $b=x+s$, $c=x+s+w$, $e=s+w$, $L=x+p$, $H=x+s+w+v$ and $B=x+2s+w$. The triangle data are
$$
k=LB/2,\qquad
(Q_1,Q_2,Q_3)=\left(\frac{p^2 B}{2L},\frac{Lb^2}{2H},\frac{Lc^2}{2H}\right),\qquad
(\sigma_1,\sigma_2,\sigma_3)=\left(\frac{pB}{L},\frac{Lb}{H},\frac{Lc}{H}\right).
$$
Thus $M=H$, $f_1=L/H$, $f_2=f_3=\sqrt{B/H}$ and $\Phi_1=2$ because $L+B=2H$.

## Proof

Fact a19fb2ae234afb2a uses $f_i=2a_i/\sqrt{q_i}$, where $q_i=Q_i/k$ and $a_i$ is the positive vertex height divided by the sum of the three positive heights. In the actual triangle $Q_i/\sigma_i$ is half the positive height by the corner area formula, so its $f_i$ agrees with the one here. Its equality conditions in row $1$ are $d_1=0$ and $d_2+d_3=0$. The first gives equal negative first coordinates at $P_2,P_3$. Write $P_1=(p,-r)$, $P_2=(-x,b)$, $P_3=(-x,-e)$. The second condition is $e+p+x-b-2r=0$ by the signed height definitions. Hence with $v=p-r>0$, $s=b-x>0$, one has $e-s=r-v=w$. The indicated coordinate map exchanges the two normals and labels and sends $(s,v,w)$ to $(s+w,v+w,-w)$, with the first two new entries positive by strict incidence. We may therefore choose $w\ge0$.

For the converse, the signs at the three vertices are strict. The triangle is nondegenerate since $L,B>0$. The barycentric weights of zero on the three vertices are $x/L$, $(xr+ep)/(LB)$ and $(bp-xr)/(LB)$ where $r=v+w$. They are positive, the last because $bp-xr=xv+sp>0$. Its area is $LB/2$. In cap $1$ both edges have cut fraction $p/L$ from its positive vertex. In cap $2$ the two fractions from its vertex are $b/H,b/B$, and in cap $3$ they are $c/H,c/B$. These give the cap areas in the statement. Dividing twice each cap area by its positive height $p,b,c$, respectively, gives the stated coareas, and the displayed row values follow.
