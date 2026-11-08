---
fact_id: bdba0add78e31c89
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-simplex-fixed-normal-uniform-tilt-gap
depends_on: ["1ec728c26c11b368"]
verifier_run: a2c6259943284c47
target_match: null
---

## Source

- [714bee9248df3ce6](../candidates/714bee9248df3ce6.json), 714bee9248df3ce6:08 §6, (12), fixed-normal stability margin.

## Statement

For an integer $d\ge2$, let $T_d=\{x:x_i\ge-1,\ \sum_i x_i\le1\}$, $V_d=(d+1)^d/d!$, and $\Gamma_d=(d/(d+1))^d$. Put the same fiber $T_d$ at each of the three bases $-1,0,1$, and let $F(a)$ be the closed cap mass at normal $(a,e_1)$ through $(0,0)$. For $0<\eta\le1$ and every $|a|\ge\eta$,
$$
F(a)-F(0)\ge g_\eta
=\min\left\{\frac{d^{d-2}}{(d-2)!}\eta^2,\ (1-2\Gamma_d)V_d\right\}>0.
$$
Replace these fibers by positive convex bodies $L_z$ on the same bases and keep the same anchor and continuous normal. If $\Delta=\sum_z|L_z\mathbin{\triangle}T_d|$ and $2\Delta<g_\eta$, all global minimizing tilts for the new fixed-normal objective belong to $(-\eta,\eta)$. When $\eta<1$, the corresponding three sections are proper whenever the $L_z$ are sufficiently close to $T_d$ in Hausdorff distance.

## Proof

In coordinates $s_i=x_i+1$, $T_d$ is the nonnegative simplex $\sum_i s_i\le d+1$. For $-1\le c\le d$, its upper $e_1$ cap is a translate of the nonnegative simplex of side parameter $d-c$, hence has volume $(d-c)^d/d!$. The cap has full mass $V_d$ below that interval and zero volume above it. For $|a|\le1$ the three thresholds are $a,0,-a$, giving
$$
F(a)-F(0)=\frac{(d+a)^d+(d-a)^d-2d^d}{d!}
\ge \frac{d^{d-2}}{(d-2)!}a^2
$$
by the even binomial terms. For $|a|\ge1$, one endpoint fiber is full and the middle takes $\Gamma_d V_d$, so $F(a)-F(0)\ge(1-2\Gamma_d)V_d$. Positivity follows from $(1+1/d)^d>2$ by the binomial expansion for $d\ge2$.

For every $a$, the same halfspace on old and new fibers gives $|F_L(a)-F(a)|\le\Delta$. For $|a|\ge\eta$ this yields $F_L(a)-F_L(0)\ge g_\eta-2\Delta>0$. The new objective attains its minimum by 1ec728c26c11b368 at fixed $(u,t)=(e_1,0)$. For $\eta<1$ each threshold in $[-\eta,\eta]$ stays at positive distance from both support endpoints $-1,d$ of the old simplex. A Hausdorff displacement less than $1-\eta$ changes either support endpoint by at most that displacement, since the normal is a unit vector. All such cuts in the new fibers are therefore proper.
