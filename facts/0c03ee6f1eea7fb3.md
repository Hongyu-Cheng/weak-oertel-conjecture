---
fact_id: 0c03ee6f1eea7fb3
kind: counterexample
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-integer-exponential-tilt-centroid-selector-obstruction
depends_on: []
verifier_run: 3588b39fff17e5d2
target_match: null
---

## Source

- [a3a3b42ddbc25ef5](../candidates/a3a3b42ddbc25ef5.json), a3a3b42ddbc25ef5:01 Unnumbered proof, polygon lists K0–K2, mean m(r), and caps H0,H1,H2.

## Statement

There is a compact full-dimensional convex body in $\mathbb R\times\mathbb R^2$ with three positive integer fibers such that every barycenter in the closure of its integer-coordinate exponential-tilt barycenters that has an integer base coordinate has original normalized mixed halfspace depth strictly less than $2/9$. Thus the selector that weights original mixed volume by $\exp(a z)$, for $a\in\mathbb R$ and including its limit barycenters, can fail the sharp mixed bound.

## Proof

Use the following counterclockwise vertex lists for the planar polygons at $z=0,1,2$, respectively:

    K0: (-218,-194), (-150,-410), (176,-362), (82,104)
    K1: (-228,332), (-160,-218), (-125,-326), (-76,-342),
        (87,-318), (40,-85), (-198,484)
    K2: (-100,-242), (-2,-274), (-80,-196)

For an oriented edge $p\to q$ use the cross product $(q-p)\times(v-p)$. In each polygon the minimum over its edges and nonincident vertices is respectively $73680,3784,5148$, all positive, proving the convex orientation. At the twelve pairwise midpoints of endpoint vertices, the minima of the seven middle-edge expressions in listed order are $(550,0,0,0,0,0,26988)$. Therefore the full endpoint Minkowski midpoint lies in $K_1$, since it is the hull of those midpoint generators. In the lifted hull the extreme fibers are exact, and at base one the two endpoint weights in any combination agree. This makes the middle fiber exactly $K_1$. There are no further integer bases, and a positive area fiber and a point at another base give full dimension.

For consecutive planar vertices $p_i,p_{i+1}$ with $t_i=p_i\times p_{i+1}$, the area is $\sum_i t_i/2$ and the centroid is $\sum_i(p_i+p_{i+1})t_i/(3\sum_i t_i)$. These give the original areas $A_0=120746,\ A_1=252101/2,\ A_2=2574$, total $T=498741/2$, and centroids
$$
c_0=(-1858520/181119,-36756476/181119),\quad
c_1=(-68744575/756303,-4718035/252101),\quad
c_2=(-182/3,-712/3).
$$
Put $r=e^a>0$. The tilted base probabilities are proportional to $A_z r^z$. The derivative of their mean with respect to $\log r$ is the strictly positive variance of $z$. The base mean increases from zero to two, so its sole integral value at finite tilt is one, occurring exactly when $r^2=A_0/A_2$. The corresponding continuous mean is
$$
v(r)=\frac{A_0(c_0+c_2)+A_1r c_1}{2A_0+A_1 r}.
$$
At $r\downarrow0$ and $r\uparrow\infty$ the limits are $(0,c_0)$ and $(2,c_2)$, respectively. Continuity in the compactified parameter interval shows these and $(1,v(r))$ are all the integral-base candidates in the closure.

For the finite candidate, $A_0/A_2<49$ and the numerator of $v_x(r)+79$ has negative slope $A_1(c_{1,x}+79)<0$. Its value at $r=7$ is positive since $v_x(7)+79=105118/6743073>0$. Thus the candidate lies in $H_1=\{x+255z\ge176\}$. This cap cuts a zero-area face at $z=0$ and contains all of $K_2$ since $\min_{K_2}x=-100>-334$. At $z=1$, intersecting the polygon edges with $x=-79$ gives vertices $(-79,-16710/49),(-76,-342),(87,-318),(40,-85),(-79,399/2)$. Their shoelace area is $10222729/196$. Adding $A_2$ and dividing by $T$ gives $10727233/48876618<2/9$.

For $(0,c_0)$ take $H_0=\{x+3y-2000z\ge-112127948/181119\}$, with equality at that candidate. The maximal scores on $K_1,K_2$ are $-746,-4668$, strictly below its threshold. On $K_0$ only the vertex $(82,104)$ has score above the threshold. Intersect its two incident edges with the boundary to obtain the other two triangle vertices $(9153660707/59044794,-15235790585/59044794)$ and $(-6218941858/36042681,-16094519794/108128043)$. The determinant area divided by $T$ is $353119997339753853217/1592080527583076149611<2/9$.

For $(2,c_2)$ use $H_2=\{-x-y+10000z\ge20298\}$. The maxima on $K_0,K_1$ are $560,10451$, so both are excluded. On $K_2$ the score $-x-y$ is $342$ at the retained vertex and $276$ at both others, with threshold $298$ at the centroid. The triangle above the threshold has linear ratio $(342-298)/(342-276)=2/3$ to $K_2$. Hence its mass ratio is $(4/9)A_2/T=2288/498741<2/9$. Every comparison uses the original areas and $\gamma_2/2=2/9$.
