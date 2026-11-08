---
fact_id: c00fa968aedd9c1a
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-distinct-positive-tetrahedral-row-capacity
depends_on: ["1462fa9ce6ced54e"]
verifier_run: d61b39c8a3fc0eec
target_match: null
---

## Source

- [f5d111431879f6ef](../candidates/f5d111431879f6ef.json), §1, (1)–(2), four distinct positive entries.

## Statement

Let $\Xi$ be uniform on the probability tetrahedron, let $F(t)=\Pr((x,y,w,z)\cdot\Xi\le t)$ for $0<x<y<w<z$, and set $\phi_3=\inf_{t>0,F(t)>0}t/F(t)^{1/3}$. Put $D=(z-x)(z-y)(z-w)$ and $h=z-\sqrt{D/z}$. If $h\ge w$ then $\phi_3^3=zh^2$, attained only at $t=h$. If $h<w$ then
$$
\phi_3^3=
\frac{\left[y^{3/2}\sqrt{(y-x)(w-x)(z-x)}-x^{3/2}\sqrt{(y-x)(w-y)(z-y)}\right]^2}{(y-x)^3}.
$$
In the latter case the minimizing threshold lies strictly between $y$ and $w$.

## Proof

Put $A=(y-x)(w-x)(z-x)$ and $B=(y-x)(w-y)(z-y)$. On $(x,y]$ the lower cap is a vertex tetrahedron with $F(t)=(t-x)^3/A$, so the ratio is strictly decreasing. On $[w,z]$ its complement is a vertex tetrahedron, giving $F(t)=1-(z-t)^3/D$. On $(y,w)$ the signed heights $t-(x,y,w,z)$ have two positive and two negative, all distinct. The distinct-height formula of 1462fa9ce6ced54e gives $F(t)=(t-x)^3/A-(t-y)^3/B$, also at the endpoints by continuity. The pieces have matching first derivatives at the knots: the proper-cut projection density is its area coarea and the sections vary continuously there. This also follows by evaluating the polynomial derivatives at the two knots.

On $[w,z]$ the sign of the ratio derivative is the sign of $F-tF'/3=1-z(z-t)^2/D$, strictly increasing on $[w,z)$ and positive above $h$. On $[y,w]$ the sign is that of $V(t-y)-U(t-x)$ with $U=\sqrt{x/A}$ and $V=\sqrt{y/B}$, since $F-tF'/3=V^2(t-y)^2-U^2(t-x)^2$. This affine expression is strictly negative at $y$. If $h\ge w$ it is nonpositive at $w$ and has no interior zero, so the unique minimum is $h$, where $F(h)=h/z$. If $h<w$, it is positive at $w$, so its unique zero is $t_*=(Vy-Ux)/(V-U)\in(y,w)$. At that threshold $U(t_*-x)=V(t_*-y)=UV(y-x)/(V-U)$ and $F(t_*)=t_*F'(t_*)/3$. Thus $t_*^3/F(t_*)=AB(Vy-Ux)^2/(y-x)^3$, which is the second formula. For $t\ge z$ the ratio equals $t$ and is increasing, and below or at $x$ the cap has zero probability.
