---
fact_id: e12e78bf7fbb5e3f
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-pk-w34-envelopes-all-point-envelope-layer-cake
depends_on: ["eba0d0c59b328385", "078744022bac23b7", "6769574fc1bd9f8d"]
verifier_run: 8b50a4565fe05c9a
target_match: null
---

## Source

- [de93d15065ebea14](../candidates/de93d15065ebea14.json), de93d15065ebea14:01 §§1–2, (1)–(5), deficit conjugate and inverse-slope forms.
- [de93d15065ebea14](../candidates/de93d15065ebea14.json), de93d15065ebea14:02 §3, (6)–(8), all-point identity and remainder.
- [de93d15065ebea14](../candidates/de93d15065ebea14.json), de93d15065ebea14:03 §4, (9)–(11), geometric level and first-moment budget.
- [de93d15065ebea14](../candidates/de93d15065ebea14.json), de93d15065ebea14:04 §5, product with identically zero envelope charge.

## Statement

Let $C\subset\mathbb R^n\times\mathbb R^d$ be a compact convex body, $d\ge1$, with summed mixed $d$-volume measure $\mu$ on $S=C\cap(\mathbb Z^n\times\mathbb R^d)$ of total mass $M>0$. For $Y\in S$ let $D(Y)$ be its raw ambient closed-halfspace depth and let $F(Y)$ be the $d$th root of its raw ordinary depth in its own fiber, zero on null fibers. Define
$$
E(\lambda)=\max_{Y\in S}(D(Y)+\lambda F(Y)),\quad Q=E(0),\quad g=E'_+,\quad
a=g(0),\quad b=\max_S F,\quad D_{\rm top}=\max_{\{F=b\}}D.
$$
For $a<s<b$ set $\Lambda(s)=\inf\{\lambda\ge0:g(\lambda)\ge s\}$. For $0\le t\le b$, let $L(t)=0$ when $t\le a$ and $L(t)=\int_a^t\Lambda(s)\,ds$ otherwise. Then
$$
L(t)=\sup_{\lambda\ge0}(Q+\lambda t-E(\lambda))
    =\int_0^\infty(t-g(\lambda))_+\,d\lambda,\qquad
L(b)=Q-D_{\rm top}.
$$
The nonnegative function $J(Y)=Q-D(Y)-L(F(Y))$ vanishes at every finite-parameter maximizer and at every $Y$ with $F(Y)=b$ and $D(Y)=D_{\rm top}$. The exact integrated identity is
$$
MQ-\int_S D\,d\mu
=\int_a^b\Lambda(s)\mu\{Y\in S:F(Y)>s\}\,ds+\int_S J\,d\mu.
$$
The first term also equals $\int_0^\infty\int_S(F(Y)-g(\lambda))_+\,d\mu\,d\lambda$. With $V_z$ denoting the positive fiber volumes and $\Gamma_d=(d/(d+1))^d$, one has for all $s\ge0$
$$
\mu\{F>s\}\ge\sum_z V_z\left(1-\frac{s}{(\Gamma_d V_z)^{1/d}}\right)_+^d .
$$
Consequently
$$
MQ\ge\int_S D\,d\mu
+\int_a^b \Lambda(s)\sum_z V_z\left(1-\frac{s}{(\Gamma_d V_z)^{1/d}}\right)_+^d\,ds,\qquad
\int_S D\,d\mu\ge\frac{\Gamma_d}{\binom{2d}{d}}\sum_z V_z^2.
$$
When $a=b$ the integrals over $(a,b)$ are zero. For $C=[0,N-1]\times B$ with $N\ge3$ odd and $B$ a centrally symmetric $d$-body, the charge $L$ vanishes identically and each fiber has volume strictly less than $M/2$.

## Proof

Apply eba0d0c59b328385 to the same original summed mixed measure and own-fiber root. It gives the required maxima, fiberwise continuity of $D,F$, and the nondecreasing right-continuous largest active slope $g$, which tends to $b$ at infinity. By local absolute continuity of the convex Lipschitz envelope, $E(\lambda)-Q=\int_0^\lambda g(r)\,dr$. For fixed $t$, the integrand $t-g(r)$ is nonincreasing, so the supremum of its initial integrals is the integral of its positive part, including a possible infinite initial interval. Tonelli expresses this positive-part integral as $\int_a^t |\{r\ge0:g(r)<s\}|\,ds$ for $t>a$, and as zero for $t\le a$. The inner set has length $\Lambda(s)$ for $a<s<b$. Jumps of $g$ merely make the inverse constant on an interval of levels. At $t=b$, the same Tonelli argument for the right-continuous Lebesgue–Stieltjes measure gives
$$
\int_0^\infty(b-g(r))\,dr=\int_0^\infty\int_{(r,\infty)}dg(\lambda)\,dr=\int_{(0,\infty)}\lambda\,dg(\lambda)=Q-D_{\rm top}
$$
by the accepted work identity. Thus all conjugate values are finite.

For every original point $Y$, the bound $D(Y)+\lambda F(Y)\le E(\lambda)$ gives $L(F(Y))\le Q-D(Y)$ by taking the supremum. Equality follows at finite-parameter optimizers by evaluating at that parameter, and at the stated top points by the endpoint formula. Since $D,F$ are fiberwise continuous on finitely many compact fibers and $L$ is measurable, $J$ is measurable. Also $0\le L(F(Y)),J(Y)\le Q$. Integrate the defining equality for $J$ and use Tonelli on the two expressions for $L$. A singleton level endpoint at $s=F(Y)$ does not change its integral in $s$; no assertion about the mass of individual level boundaries is needed.

For a positive fiber let $A_z$ be its peak ordinary raw depth. Fact 078744022bac23b7 applies to this compact $d$-body and gives the homothetic lower bound of volume $V_z(1-(r/A_z)^{1/d})^d$ for each weak raw level $0\le r\le A_z$. Its centroid satisfies $A_z\ge\Gamma_d V_z$ by the full-mass case of 6769574fc1bd9f8d. Use the lower bound at raw level $(s+\eta)^d$ if $s+\eta<(\Gamma_d V_z)^{1/d}$ and let $\eta\downarrow0$ to obtain the stated strict level estimate. When $s\ge(\Gamma_d V_z)^{1/d}$ the right side for that fiber is zero. Null fibers contribute zero. Insert the estimate into the all-point identity and drop the nonnegative remainder. Finally $D(Y)\ge F(Y)^d$, since every ambient cap contains a qualifying own-fiber cap or the whole fiber. Fact 078744022bac23b7 gives $\int F^d\,d\mu$ on each positive fiber at least $V_z A_z/\binom{2d}{d}$, which proves the displayed moment bound.

For the zero-charge calibration take $C=[0,N-1]\times B$ with $N\ge3$ odd and $B$ centrally symmetric of volume $V$ about zero. The mark $((N-1)/2,0)$ bisects the entire summed measure for every nonvertical through-mark cut by symmetry and null boundary mass. Pure-base through-mark cuts include at least $(N+1)/2$ whole fibers. The opposite through-point nonvertical cuts at any mark have total mass $M$ and bound its depth by $M/2$. Thus $Q=M/2$. The central mark also has $F=(V/2)^{1/d}=b$ by symmetry and the opposite-cut upper bound in $B$. It follows that $a=b$, $E(\lambda)=Q+\lambda b$ and $L\equiv0$, although there are arbitrarily many positive fibers, each with $V<M/2$. In this family the deficit is entirely the remainder term.
