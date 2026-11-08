---
fact_id: da544e8fcada039b
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-equal-endpoint-actual-mixed-centroid
depends_on: ["486fe778f838d99d", "607dca34de472b94"]
verifier_run: 00998539d8f1663f
target_match: null
---

## Source

- [660db01ed45063dd](../candidates/660db01ed45063dd.json), §5, (9)–(10), with the uniform surplus (8a).

## Statement

Let $d\ge1$ be an integer, and let $A,K,B\subset\mathbb R^d$ be convex bodies of volumes $v,k,v>0$ with $(A+B)/2\subseteq K$. Let $\mu$ be the sum of the $d$-volumes on the integer fibers $A,K,B$ at bases $-1,0,1$ of their lifted convex hull. The actual mixed centroid is

$$
Y=\left(0,\frac{v g_A+k g_K+v g_B}{k+2v}\right),
$$

where $g_A,g_K,g_B$ are the uniform-volume centroids. It lies in $\lbrace 0\rbrace\times\operatorname{int}K$. Write $\Gamma_d=(d/(d+1))^d$, $A_d=1/\Gamma_d$, and let the positive constant $\varepsilon_d$ be

$$
\varepsilon_d=\frac{d}{d+1}\left[2+(1+1/d)(1+A_d/3)
-2(1+1/(2d))^{d+1}-2(1-(4A_d/3-1)/(2d))_+^{d+1}\right],
$$

with $t_+=\max(t,0)$. The raw depth at $Y$, the infimum of $\mu(H)$ over closed ambient halfspaces containing $Y$, is at least

$$
\frac{3\Gamma_d}{4}(k+v)+
\min\left(\frac{3\Gamma_d^2\varepsilon_d k}{4\cdot3^d},
               (1-3\Gamma_d/4)(k+v)\right).
$$

In particular it is strictly greater than $(3\Gamma_d/4)(k+v)\ge(\Gamma_d/2)(k+2v)$. The same conclusion holds in any convex body whose only positive $d$-volume integer fibers are those three fibers; any other integer fibers of zero $d$-volume do not affect $\mu$.

## Proof

At levels $-1$ and $1$, the lifted convex hull has exactly the corresponding endpoint bodies, since those levels are extreme. At level $0$, a convex combination has equal total weights on the two endpoints. By convexity of the individual fibers, if their total weight is positive the endpoint part of the combination contributes a point of $(A+B)/2\subseteq K$. Hence the middle fiber is exactly $K$ and no other integer levels occur. The first moment of $\mu$ gives the displayed centroid formula. For an arbitrary convex body with the stated positive fibers, convexity also supplies the required midpoint containment, and the same sum of measures and first moment apply.

Use the coupling constructed in the proof of accepted fact 486fe778f838d99d, with the two full-dimensional convex bodies $A,B$, interpolation parameter $1/2$, and containing convex body $K$. Specifically its conditional-quantile map $T$ sends $U_A$ to $U_B$ and its midpoint map $G_{1/2}(x)=(x+T(x))/2$ sends $U_A$ to a law with Lebesgue density at most $1/v$, since the interpolation volume there is $((v^{1/d}+v^{1/d})/2)^d=v$. Let $\pi=v(\operatorname{Id},T)_\#U_A$. Its marginals are exactly $\mathbf 1_A\,dx$ and $\mathbf 1_B\,dx$. The midpoint pushforward $\eta=v(G_{1/2})_\#U_A$ is supported in $(A+B)/2$, satisfies $\eta\le\mathbf 1_K\,dx$, and has mass $v$. In particular $k\ge v$. Its first moment, by the marginals, is $v(g_A+g_B)/2$. Thus the continuous coordinate $g$ of $Y$ is exactly the centroid of $\mathbf 1_K\,dx+2\eta$, and the weight-two theorem puts $g$ in $\operatorname{int}K$.

For an ambient closed halfspace $H=\lbrace(z,x):L(z,x)\ge0\rbrace$ with affine margin $L$, put $H_i=\lbrace x:(i,x)\in H\rbrace$. For every pair $(x,y)$ in the coupling,

$$
L(0,(x+y)/2)=\tfrac12[L(-1,x)+L(1,y)].
$$

A nonnegative left side requires at least one nonnegative endpoint margin. Integrating the corresponding indicator inequality, with the exact marginals of $\pi$, gives $\eta(H_0)\le|A\cap H_{-1}|+|B\cap H_1|$. The same fixed coupling works for every affine margin and the inequality includes equality on closed boundaries.

Translate any containing halfspace inward until its boundary passes through $Y$. For a through-$Y$ halfspace with nonzero continuous normal, $H_0$ is a closed halfspace containing $g$. Its ordinary volume plus $\eta(H_0)$ is at most $\mu(H)$ by the preceding inequality and is at least $(3\Gamma_d/4)(k+v)+3\Gamma_d^2\varepsilon_d k/(4\cdot3^d)$ by the weight-two theorem. For a through-$Y$ halfspace with purely integer normal, the cap contains the entire middle fiber and exactly one endpoint, so its mass is $k+v$. The stated minimum of the two positive surpluses works for every halfspace, and hence for the infimum. Finally $(3\Gamma_d/4)(k+v)-(\Gamma_d/2)(k+2v)=(\Gamma_d/4)(k-v)\ge0$.
