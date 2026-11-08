---
fact_id: f5dea144eae3ba15
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-ordinary-centroid-cut-triangle-finite-ear-cubic
depends_on: []
verifier_run: 8a2cee5f1489f049
target_match: null
---

## Source

- [7ea1c8120620b951](../candidates/7ea1c8120620b951.json), §1 (1), §§2–4 (4)–(10), §§5–6 (11)–(17), strict-ear theorem and affine interpretation.

## Statement

Take $P_1=(2,-1)$, $P_2=(-1,2)$, $P_3=(-1,-1)$ and $Q=(X,Y)$ with $X,Y>-1$ and $X+Y>1$. For $K=\operatorname{conv}(P_3,P_1,Q,P_2)$, source $0$ and normals $(1,0),(0,1),(-1,-1)$, write $k$ for area, $Q_i$ for cap areas, $\sigma_i$ for coarea chord lengths, $M=\sum_iQ_i/\sigma_i$ and $f_i=2\sqrt{kQ_i}/(\sigma_iM)$. Then $\sum_i f_i^2+f_1f_2f_3<4$ and the symmetric zero-diagonal matrix with off-diagonal entries $f_i/2$ has top eigenvalue less than one. This applies to any actual ear on any triangle whose cuts through the original centroid are parallel to the opposite edges, provided the three old vertices remain strict vertices of the resulting quadrilateral. It includes both unique-tip branches, the double-tip branch, and the ray seams. If $Q$ is on the old edge the body is the original triangle and $f_i=1$. At the limiting parameters $X=-1,Y>2$ or $Y=-1,X>2$, the old quadrilateral degenerates to a nondegenerate triangle and the cubic is still strict.

## Proof

Let $r=X+Y-1$. The four consecutive turn determinants are $3(Y+1),3r,3(X+1),9$, and the four successive vertex-pair determinants are $3,X+2Y,2X+Y,3$. The turn determinants give strict convexity in the displayed order: the two vertices not on a directed edge are strictly to its left by the adjacent turns. The vertex-pair determinants are all positive since $X+2Y=(X+Y)+Y>1+Y>0$ and $2X+Y>1+X>0$. Thus $0$ is interior. The total area is $k=3(r+3)/2$.

Put $T=\sum_iQ_i/\sigma_i^2$, $U=\prod_i(Q_i/\sigma_i^2)$, $E=M^2-kT$ and $R=M^2E^2-4k^3U$. All cap areas and sections are positive. The cubic inequality is equivalent to $ME>2k^{3/2}\sqrt U$, or to $E>0$ and $R>0$. This tests the sign before squaring. If the cubic is strict, then each $f_i<2$ and the three $2\times2$ principal minors of $I-B$ are positive for the indicated matrix $B$. Its determinant is $(4-\sum_i f_i^2-f_1f_2f_3)/4>0$. Thus $I-B$ is positive definite.

First suppose $X,Y\ge0$, and put $p=XY$. Direct intersection with the three lines gives
$$
\sigma_1=2+\frac r{X+1},\qquad
\sigma_2=2+\frac r{Y+1},\qquad
\sigma_3=2,\qquad
Q_1=\frac{3r+6-\sigma_1}{2},\quad
Q_2=\frac{3r+6-\sigma_2}{2},\quad Q_3=2.
$$
The first chord runs from $(0,-1)$ to $(0,(2X+Y)/(X+1))$. The complement cap is the trapezoid with parallel vertical sides $3,\sigma_1$ at distance one, and subtracting its area from $k$ gives $Q_1$. Reflection gives cap 2. The third cap is the unchanged triangle on $P_3,(1,-1),(-1,1)$. The formulas include either tip lying on a cutting line.

Let
$$
c=\tfrac32(r+2),\quad D=4p+3r^2+10r+8,\quad
h=(4p+r^2+7r+8)/D,\quad q=(p+r+2)/D .
$$
Adding and multiplying the first two reciprocal chords gives their sum $h$ and product $q$. Hence
$$
M=ch,\qquad T=c(h^2-2q)-h/2+1/2,\qquad
U=q(c^2q-ch/2+1/4)/2.
$$
Clearing denominators in $E,R$ gives $E=3E_0/(4D^2)$ and $R=27rR_0/(64D^6)$, where
$$
\begin{aligned}
E_0={}&(r+2)(9r^4+73r^3+198r^2+228r+96)\\
&+2p(9r^4+71r^3+186r^2+210r+96)+24p^2(r+1)(r+2).
\end{aligned}
$$
Write $R_0=\sum_{j=0}^6 A_j(r)p^j$. Its coefficient polynomials are
$$
\begin{aligned}
A_0&=(r+2)^4P_0,& A_1&=12(r+2)^3P_1,& A_2&=12(r+2)^2P_2,\\
A_3&=32(r+2)^2P_3,& A_4&=192(r+2)^2P_4,& A_5&=1536(r+2)^2P_5,\\
A_6&=1024(3r^2+11r+9)(9r^3+54r^2+109r+72).
\end{aligned}
$$
The following arrays list the coefficients of $P_0,\ldots,P_5$ in ascending powers of $r$. Together with the preceding formulas they specify the identities by polynomial expansion.

```text
P0 = [663552, 3778560, 9625088, 14460848, 14226512, 9622452,
      4572636, 1532931, 358116, 56190, 5400, 243]
P1 = [497664, 2774016, 6909568, 10127784, 9680204, 6316694,
      2863620, 900238, 192369, 26711, 2187, 81]
P2 = [1658880, 8773632, 20708992, 28704164, 25850592, 15799832,
      6646108, 1910496, 364947, 43735, 2925, 81]
P3 = [518400, 2300544, 4474696, 4983734, 3481338, 1570257,
      453723, 80373, 7875, 324]
P4 = [38880, 138168, 208516, 171635, 82370, 22801, 3336, 198]
P5 = [1134, 3006, 3157, 1610, 393, 36]
```

Every listed coefficient is positive. Since $r>0$ and $p\ge0$, this proves $E,R>0$ on this branch.

If one tip coordinate is negative, by reflecting the two axes assume $X=-a$ and $Y=r+1+a$ with $0<a<1$. The two cases cannot both be negative since $X+Y>1$. Put $V=r+a+2$ and $W=3r+2a+4$. Now
$$
\sigma_1=2V/(a+2),\quad \sigma_2=W/V,\quad \sigma_3=2,\qquad
Q_1=\sigma_1,\quad Q_2=(3r+6-\sigma_2)/2,\quad Q_3=2.
$$
Cap 1 is the triangle with apex $P_1$ and base on $x=0$, whose top intersection is on $P_1Q$ and whose bottom intersection is $(0,-1)$. Its height is two. The previous trapezoid argument on the second cut and the unchanged third cap give the other areas. At $a=0$ these formulas agree with the first branch.

Substitution gives $E=3E_1/(4VW^2)$ and $R=27rR_1/(64V^2W^6)$, where
$$
E_1=12(a+2)^3+3(a+2)^2(a+19)r+3(a+2)(4a+33)r^2+(17a+73)r^3+9r^4.
$$
For $R_1=\sum_{j=0}^{11}B_j(a)r^j$, the complete coefficient list obtained by clearing the denominators is

```text
B0  = 5184(1-a)(a+2)^7
B1  = 288(a+2)^6(205-182a-17a^2)
B2  = 16(a+2)^5(18799-14241a-3057a^2-97a^3)
B3  = (a+2)^4(903803-546492a-211566a^2-14684a^3-165a^4)
B4  = 2(a+2)^3(889157-376278a-257322a^2-29756a^3-729a^4)
B5  = 3(a+2)^2(801871-164870a-253382a^2-44598a^3-1809a^4)
B6  = 6(a+2)(381053+21565a-112186a^2-29895a^3-1823a^4)
B7  = 3(510977+189486a-100415a^2-46894a^3-4217a^4)
B8  = 6(59686+14249a-6352a^2-1325a^3)
B9  = 6(9365+1403a-319a^2)
B10 = 216(2a+25)
B11 = 243
```

The final polynomial factors in $B_1$ through $B_9$ have lower bounds $(6,1404,130896,225072,337212,237149,359451,52009,9046)$ on $[0,1]$, by replacing each negative term's power of $a$ by one and dropping each positive term of positive degree. Thus $E_1,R_1>0$ for $r>0$ and $0\le a\le1$, even if $B_0=0$. At $a=1$ the point $P_2$ is on $P_3Q$ and the retained body is a triangle. The same clipping formulas hold by continuity of area and proper section length at those parameters, or by clipping the triangle directly. Reflection gives the other limiting branch.

When the tip is on the original edge the body is the original triangle. Its caps have $k=9/2$, $Q_i=\sigma_i=2$, so $f_i=1$. For an arbitrary triangle, relabel the vertices so the ear is on the edge $P_1P_2$, and transport the whole body and cuts by the affine map taking its triangle to the displayed one. Its centroid maps to $0$. Normals for the three cuts may be chosen to balance and then agree with the three displayed normals up to common scale. Under a linear part $L$, covectors transport by $L^{-\mathsf T}$ and both areas and coarea lengths multiply by $|\det L|$, the latter by differentiating cap area with respect to its level. Thus all $f_i$ are unchanged. The strict convexity condition in the displayed coordinates is exactly $X,Y>-1$ and $X+Y>1$, as the turn formulas show. In particular for a diagonal motion $Q=P_3+t(a,b)$ with $a,b>0$, it is exactly $t>3/(a+b)$.
