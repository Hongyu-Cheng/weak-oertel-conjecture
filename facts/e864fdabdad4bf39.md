---
fact_id: e864fdabdad4bf39
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-symmetric-planar-ear-strict-lorentz-rows
depends_on: ["32f76dd9c09dcab2"]
verifier_run: 2ae335fd51fadcc4
target_match: null
---

## Source

- [11020364891cd885](../candidates/11020364891cd885.json), 11020364891cd885:02 §§2–3, (3)–(7), symmetric quadrilateral.

## Statement

For $x,u,v>0$ and $\delta\ge0$ let $K$ be the convex hull of $(2v,-v),(-x,x+u),(-x-\delta,(x+\delta)/2),(-x,-u)$. For the through-origin caps with normals $(1,0),(0,1),(-1,-1)$, write $k=|K|$, $Q_i$ for their areas, and $\sigma_i$ for chord lengths divided by the corresponding normal lengths. Set $M=\sum_iQ_i/\sigma_i$ and $f_i=2\sqrt{kQ_i}/(\sigma_iM)$. Then every row satisfies $f_i+(f_j+f_l)^2/4\le2$ for $\{i,j,l\}=\{1,2,3\}$, with all inequalities strict for $\delta>0$.

## Proof

The determinant-one shear $(X,Y)\mapsto(X,Y+X/2)$ sends the four listed points to $(2v,0),(-x,x/2+u),(-x-\delta,0),(-x,-x/2-u)$. For $\delta>0$ the two diagonals intersect in their interiors, giving a convex quadrilateral in the indicated order; for $\delta=0$ the extra point lies on the old edge. In either case $0$ is interior. The reflection $(X,Y)\mapsto(X,-X-Y)$ preserves cap $1$ and interchanges caps $2,3$; it preserves area and, by differentiation in the scalar threshold, the corresponding coareas.

Let $L=x+2v$ and $B=x+2u$. The triangle with the first, second and fourth vertices has area $LB/2$ and the ear adds $\delta B/2$. The vertical section length and cap $1$ area are $\sigma_1=2vB/L$ and $Q_1=v\sigma_1$. For the old cap $2$ the positive height is $x+u$, and the two intercept fractions from the positive vertex are $(x+u)/(x+u+v)$ and $(x+u)/B$. Its old area is $L(x+u)^2/[2(x+u+v)]$, and the old coarea is $L(x+u)/(x+u+v)$. For the ear apply the finite ear formula with heights $p=x+u$, $w=u$, and tip height $(x+\delta)/2$; at $\delta=0$ simply omit this zero-area ear. This yields
$$
k=(L+\delta)B/2,\quad
\sigma=\sigma_2=\sigma_3=B\left[\frac{v}{x+u+v}+\frac{x+\delta}{x+\delta+2u}\right],\quad
Q_c=Q_2=Q_3=\frac{L(x+u)^2}{2(x+u+v)}+\frac{\delta B}{2}-\frac{\delta u^2}{x+\delta+2u}.
$$
Here the coarea expression uses $L(x+u)/(x+u+v)=B[v/(x+u+v)+x/(x+2u)]$. Set $H_2=2Q_c/\sigma$, so $M=v+H_2$. Directly,
$$
f_1=\sqrt{L(L+\delta)}/M,\qquad f_2=f_3,\qquad f_2^2=2kH_2/(\sigma M^2).
$$

For the sign, put $D=\delta u+2\delta v+\delta x+2uv+ux+2vx+x^2$. Substitution of the area and coarea formulas gives
$$
\begin{aligned}
D H_2={}&\delta^2(u+v+x)+\delta(u^2+2uv+3ux+3vx+2x^2)\\
 &+2u^2v+u^2x+4uvx+2ux^2+2vx^2+x^3.
\end{aligned}
$$
Putting $M=v+H_2$ and multiplying the next identity by $2D^2$ gives the following polynomial factorization (expand using the displayed $DH_2$ and $\sigma=BD/[(x+u+v)(x+\delta+2u)]$):
$$
2M^2-(L+\delta/2)M-\frac{2kH_2}{\sigma}
=\frac{\delta(\delta+2v+x)(u+v+x)}{2D^2}
\left[\delta^2(u+x)+\delta(u^2+3ux+2x^2)+2u^2v+u^2x+2ux^2+x^3\right].
$$
All factors are nonnegative and the bracket is positive. Since $\sqrt{L(L+\delta)}\le L+\delta/2$, division by $M^2>0$ proves $f_1+f_2^2\le2$, strictly if $\delta>0$. Write $r=f_1$ and $s=f_2=f_3$. Then $0<s<\sqrt2$ and $r\le2-s^2$. Both remaining rows follow from
$$
s+(r+s)^2/4\le s+(2-s^2+s)^2/4\le2,\qquad
4\left[2-s-(2-s^2+s)^2/4\right]=(4-s^2)(s-1)^2.
$$
If $\delta>0$ the first inequality is strict since $r<2-s^2$ and $r+s>0$.
