---
fact_id: 339c3fe5bfe0efb2
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-bisected-three-chord-section-weight-bounds
depends_on: []
verifier_run: 566774d219e29a32
target_match: null
---

## Source

- [5147d81ebb25b0cc](../candidates/5147d81ebb25b0cc.json), 5147d81ebb25b0cc:01 Proof §§1–3 (1), (5)–(10), ordinary bisected chords.
- [5147d81ebb25b0cc](../candidates/5147d81ebb25b0cc.json), 5147d81ebb25b0cc:02 Proof §1 (2)–(4) and §4 (11)–(12), sorted cap-profile strengthening.

## Statement

Let $K$ be a planar convex body with $0\in\operatorname{int}K$. Let nonzero normals $v_1,v_2,v_3$ span the plane and sum to zero. Suppose all three chords $K\cap\{v_i\cdot x=0\}$ are bisected at $0$. Define
$$
k=|K|,\quad q_i=|K\cap\{v_i\cdot x\ge0\}|,\quad
\sigma_i=\frac{\mathcal H^1(K\cap\{v_i\cdot x=0\})}{\lVert v_i\rVert},
\qquad
\lambda_i=\frac{\sigma_i^{-1}}{\sum_j\sigma_j^{-1}}.
$$
Suppose $q_i\le c k$ for all $i$, where $0<c<1/2$, and set $\varepsilon=1-2c$. Then $\min_i\lambda_i\ge 1/[1+\sqrt{1+1/(2\varepsilon)}]$. If in addition the sorted cap areas $x\le y\le z$ satisfy $x+y+z/4\le k$, then $\min_i\lambda_i\ge 1/[1+\sqrt{1+3c/(4\varepsilon)}]$. At $c=128/279$ these respective bounds are $1/[1+\sqrt{325/46}]>2/9$ and $1/[1+\sqrt{119/23}]>3/10$.

## Proof

The map $x\mapsto(v_1\cdot x,v_2\cdot x)$ is invertible because a collinear first pair would make all three normals collinear. The transformed normals are $(1,0),(0,1),(-1,-1)$. Its absolute determinant scales all areas by the same factor. It scales every $\sigma_i$ by that factor as well, since the scalar margin $v_i\cdot x$ is unchanged and $\sigma_i$ is the limit as $h\downarrow0$ of the area of the slab $0\le v_i\cdot x\le h$ divided by $h$. This limit follows from continuity of the interior parallel chord lengths of a planar convex body and coarea. The map preserves bisection and the two hypotheses on cap areas. Relabeling and reapplying this normalization allows the six actual ray endpoints to be written as $(\pm A,0),(0,\pm B),\pm(R,-R)$ with $B\ge A,R>0$. The normalized lengths are $2B,2A,2R$, so $\lambda_1$ is a minimum. Put $P=AR$, $S=A+R$, $L=BS+P$ and $X=BS/P$, so $\lambda_1=1/(1+X)$ and $BS-P>0$.

The six triangles with vertex $0$ and consecutive ray endpoints lie in $K$ and have disjoint interiors. Their total area is $L$, so $k\ge L$. Let $Z=K\cap\{y<0,x+y>0\}$ and $D=K\cap\{y\ge0,x+y\le0\}$. The first is missed by the second and third caps, and the second belongs to both. In particular $D$ contains the triangle with vertices $0,(-A,0),(-R,R)$ of area $P/2$. Inclusion-exclusion gives $q_2+q_3=k-|Z|+|D|$, hence $\varepsilon k\le |Z|-|D|\le |Z|-P/2$.

In determinant-one absolute coordinates $(u,v)=(-y,x+y)$ on $Z$, its points have $u,v>0$. The segment from $(u+v,-u)$ to $(0,-B)$ crosses $x+y=0$ at $x=B(u+v)/(B+v)$, at most $R$ by the actual ray endpoint. The segment to $(0,B)$ crosses $y=0$ at $x=B(u+v)/(B+u)$, at most $A$. Thus the reflected coordinates of $Z$ are bounded by the nonnegative-quadrant polygon
$$
B u+(B-R)v\le BR,\qquad (B-A)u+B v\le BA.
$$
The coefficients are nonnegative and the determinant is $BS-P>0$. Its axis vertices are $(R,0),(0,A)$, since the two corresponding actual endpoints obey both constraints and each constraint bounds its respective axis. The other nonzero vertex is the line intersection, allowing a repeated axis vertex. In fact solving the two equalities gives
$$
(u_*,v_*)=\frac{B}{BS-P}\bigl(P+B(R-A),P+B(A-R)\bigr).
$$
Both coordinates are nonnegative by feasibility of the two axis endpoints. The polygon area is $(Rv_*+Au_*)/2=[PBS-B^2(A-R)^2]/[2(BS-P)]$. Subtracting the actual opposite triangle gives
$$
\varepsilon k\le\frac{P^2-B^2(A-R)^2}{2(BS-P)}\le\frac{P^2}{2(BS-P)}.
$$
With $k\ge BS+P$ this yields $X^2\le1+1/(2\varepsilon)$ and the first bound.

For the sorted cap hypothesis, off the source lines every point is in one or two of the caps, since the three margins sum to zero. The total double-capture area $D_{\rm tot}$ is $\sum_iq_i-k$. It contains three of the six core triangles, one from each antipodal pair, so $D_{\rm tot}\ge L/2$. The sorted hypothesis is $\sum_iq_i-(3/4)\max_i q_i\le k$, which gives $D_{\rm tot}\le3ck/4$ and $k\ge 2L/(3c)$. Substituting this improved area bound into the same inequality for $\varepsilon k$ gives $X^2\le1+3c/(4\varepsilon)$. At $c=128/279$, $\varepsilon=23/279$, so the two radicands are $325/46$ and $119/23$. The comparisons with $(7/2)^2$ and $(7/3)^2$ follow from $1300<2254$ and $1071<1127$, respectively.
