---
fact_id: b2ded0fb7bce1188
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-tetrahedral-three-root-reciprocal-stiffness
depends_on: ["1462fa9ce6ced54e"]
verifier_run: 55f5458c28c166ca
target_match: null
---

## Source

- [03420419c4771251](../candidates/03420419c4771251.json), 03420419c4771251:01 §§1–2, (1)–(7).

## Statement

Let a strict quadrilateral tetrahedral section with margins $C(p)=(p,q,-1,-1)$, $p,q>0$, have actual area centroid $(a,c,B,B)$, with $a,c>1/3$ and $a+c+2B=1$. Let $P(C)=\Pr(C\cdot\Xi\ge0)$ for uniform barycentric $\Xi$, let $f$ be the density at zero of the signed exponential sum with coefficients $C$, and put $J(p)=\nabla^2P(C)[(0,0,1,-1),(0,0,1,-1)]/(3f)$. Write $t=2-(1+p)^{-1}-(1+q)^{-1}$. Then $ap+cq=2B$ and $J(p)=2B-4Bt+2t^2/3>0$. For fixed centroid the actual $p$ values are roots of the cubic $F$ below, and their reciprocal stiffness agrees with the explicit quadratic $(N_2p^2+N_1p+N_0)/(2BE)$ below. In particular, if three distinct actual roots $p_1<p_2<p_3$ occur and $\theta=(p_3-p_2)/(p_3-p_1)$, then $\theta/J(p_1)+(1-\theta)/J(p_3)-1/J(p_2)=(N_2/(2BE))(p_2-p_1)(p_3-p_2)>0$.

## Proof

By 1462fa9ce6ced54e, writing $u=(1+p)^{-1}$, $v=(1+q)^{-1}$ and $t=2-u-v$, the first two centroid coordinates satisfy
$$
3a=u(1+t-u)/t,\qquad 3c=v(1+t-v)/t.
$$
Indeed, the two raw negative heights are equal, and substituting the four reciprocal heights in the centroid formula gives these expressions. The density of $pE_1+qE_2-E_3-E_4$ at zero is $f=uvt$, by evaluating $\mathbb E[(pE_1+qE_2)e^{-(pE_1+qE_2)}]$. Incidence gives $q=(2B-ap)/c$. Write $D=a-c$ and substitute $a=(1-2B+D)/2$, $c=(1-2B-D)/2$ into the first centroid equation. Clearing its denominators gives $F(p)=0$ with
$$
\begin{aligned}
F(p)={}&3(2B-D-1)^2p^3+6(6B^2-5BD-3B+D^2+D)p^2\\
&+(36B^2-24BD-8B+3D^2+1)p+2B(6B-3D-1).
\end{aligned}
$$
The denominator clearing can be checked by taking the numerator of $u(1+t-u)/(3t)-a$ after the stated substitutions, which yields $2F$ with a common polynomial denominator.

Let $J=\nabla^2P[(0,0,1,-1),(0,0,1,-1)]/(3f)$ at $C(p)$. To calculate $J$, write $P(p,q,-r,-w)$ as
$$
\frac{p^2q^2+pq(p+q)(r+w)+(p^2+pq+q^2)rw}{(p+r)(p+w)(q+r)(q+w)}.
$$
Set $r=1-\varepsilon$, $w=1+\varepsilon$ and extract twice the coefficient of $\varepsilon^2$. Dividing by $3f$ gives
$$
J=\frac{2[(u+v-1)^3+uv(3-2u-2v)]}{3t}.
$$
The sum of the two centroid equations and $a+c=1-2B$ give $uv=t^2-(1+3B)t+1$. Substituting this into the expression for $J$ gives $J=2B-4Bt+2t^2/3$. It is positive since $0<B<1/6$ and its discriminant in $t$ is $16B(B-1/3)<0$.

Define
$$
\begin{aligned}
L&=2B-D-1,\\
E&=432B^2D^2-216BD^2-8B+27D^4+18D^2+3,\\
N_2&=-9L^2(4B-3D^2-1),\\
N_1&=-18L(24B^2D+8B^2-6BD^2-12BD-2B+3D^3+D),\\
N_0&=-3(288B^3D+48B^3-180B^2D^2-144B^2D-12B^2
          +36BD^3+96BD^2+12BD-9D^4-6D^2-1).
\end{aligned}
$$
For explicit denominator clearing let $M=(1+p)(1+q)$ and $S=2M-2-p-q$, so $t=S/M$. Polynomial division in $p$ gives
$$
\left[(6BM^2-12BSM+2S^2)(N_2p^2+N_1p+N_0)-6BE M^2\right]\bmod F=0.
$$
This identity is over the rational functions of $B,D$ after the displayed affine substitution for $q$. To reproduce the division, put $F=f_3p^3+f_2p^2+f_1p+f_0$, start with the coefficients of the displayed dividend and for $k=6,5,4,3$ replace its term $h_kp^k$ by $-(h_k/f_3)(f_2p^{k-1}+f_1p^{k-2}+f_0p^{k-3})$. The three remaining coefficients are $(0,0,0)$. Here $f_3=12a^2>0$ and $c>0$, so the division is valid also at $D=0$. At every actual root, $M>0$, and the identity proves $1/J=(N_2p^2+N_1p+N_0)/(2BE)$.

Since $0<B<1/6$ and $|D|<1/3$, the bound $24B^2-12B+1\ge-1/3$ gives $E=27D^4+18(24B^2-12B+1)D^2+3-8B\ge3-8B-6D^2>1$. Also $N_2>0$ since $L=-2a\ne0$ and $4B-3D^2-1<0$. The leading coefficient of the reciprocal-stiffness quadratic is thus positive. At three ordered actual roots $p_1<p_2<p_3$, affine terms cancel in the secant difference at $p_2$. The quadratic term gives $(N_2/(2BE))(p_2-p_1)(p_3-p_2)$ as claimed.
