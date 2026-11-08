---
fact_id: dfffa3e70be598b6
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-three-fiber-critical-middle-cover-deficit-margin
depends_on: ["6769574fc1bd9f8d", "3feef7505711fd58"]
verifier_run: e957ef6501d79103
target_match: null
---

## Source

- [fee4b98d94ecbcf2](../candidates/fee4b98d94ecbcf2.json), §5, (12), middle cover and exact-deficit specialization.
- [9f6a0ee7f33d8c84](../candidates/9f6a0ee7f33d8c84.json), Statement (1) and §§2–4, weaker proper critical equality-cover bound.

## Statement

Let $d\ge1$ be an integer and let $A,K,B\subset\mathbb R^d$ be compact convex bodies with nonempty interiors and $(A+B)/2\subseteq K$. Put $S=(\lbrace-1\rbrace\times A)\cup(\lbrace0\rbrace\times K)\cup(\lbrace1\rbrace\times B)$, measured by $d$-dimensional Hausdorff measure $\mu$ on $S$. Fix $y\in K$ and let $Q$ be the infimum of $\mu(S\cap H)$ over all closed ambient halfspaces $H$ containing $(0,y)$. Write $M=|A|+|K|+|B|$ and $\Gamma=(d/(d+1))^d$. Suppose finitely many closed ambient halfspaces $H_i=\lbrace(z,x):u_i\cdot(x-y)+\alpha_i z\ge0\rbrace$, with $u_i\ne0$, attain $Q$ and their middle traces cover $K$. For each $i$ let $U_i,q_i,V_i$ be the respective captured volumes in $A,K,B$. Suppose that for the same $\eta\in[0,1]$, every $i$ satisfies $U_i^{1/d}+V_i^{1/d}\ge2(1-\eta)q_i^{1/d}$. Set $D=2(1-\eta)^d$ and $\rho=(D\Gamma)^{1/d}$. Then

$$
\frac{Q}{M}\ge\frac{(1+D)\Gamma}{1+\rho^d+(2-\rho)^d},
\qquad
\frac{Q}{M}>\frac{8}{15}\Gamma>\frac{\Gamma}{2}
\quad\text{if }\eta\le\frac1{2(d+1)}.
$$

At $\eta=0$ the first lower bound is

$$
\frac{3\Gamma}{1+2\Gamma+(2-(2\Gamma)^{1/d})^d}.
$$

This is $1/2$ for $d=1$ and $12/(61-24\sqrt2)$ for $d=2$. For $d\ge2$ it strictly exceeds $3\Gamma/[1+\Gamma+((d+2)/(d+1))^d]$, which in turn is strictly greater than $3\Gamma/5>\Gamma/2$.

## Proof

The middle traces are actual closed halfspaces restricted to $K$ and cover $K$ as a set. At least one trace therefore contains the ordinary volume centroid of $K$. Apply the full-mass case of accepted fact 6769574fc1bd9f8d with body $K$, mass $m=|K|>0$, and admissible density identically one. The selected trace has volume $q_i\ge\Gamma|K|$, including when its bounding plane contains that centroid. It is a trace of a cap attaining the actual depth at the given $(0,y)$, with nonzero continuous normal and the common prescribed root deficit bound. Hence the one-cap quantitative theorem applies at this same point and gives both claims. When $\eta=0$, its hypothesis is the non-strict root inequality, so it includes every cover satisfying exact root equality.

For $d\ge2$, $(2\Gamma)^{1/d}>\Gamma^{1/d}=d/(d+1)$ and $(2\Gamma)^{1/d}\le1$. The function $1+t^d+(2-t)^d$ is strictly decreasing on $[0,1]$ because its derivative is strictly negative for $0<t<1$. Thus the denominator at $\eta=0$ is strictly smaller than its value at $t=d/(d+1)$, which is $1+\Gamma+((d+2)/(d+1))^d$. The latter is less than $5$, since $\Gamma<1$ and $(1+1/(d+1))^d<e<3$. This also verifies the older strict margin, whose weaker explicit bound is $12/29$ at $d=2$. In the new formula, direct substitution of $\Gamma=4/9$ and $(2\Gamma)^{1/2}=2\sqrt2/3$ gives $12/(61-24\sqrt2)$. When $d=1$, $\Gamma=1/2$ and $(2\Gamma)^{1/d}=1$, giving $1/2$. Three identical intervals centered at $y$ attain this one-dimensional value. Central symmetry gives half the total mass in every halfspace through $(0,y)$ or more, and a through-center cut with nonzero continuous normal gives exactly half. The two opposite continuous traces through that point cover the middle interval and both have exact root equality.
