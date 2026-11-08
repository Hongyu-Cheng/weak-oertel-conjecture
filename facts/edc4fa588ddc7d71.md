---
fact_id: edc4fa588ddc7d71
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-double-core-support-triangle
depends_on: []
verifier_run: ef3deaa76dca3245
target_match: null
---

## Source

- [fd39a28eeb41e9c4](../candidates/fd39a28eeb41e9c4.json), fd39a28eeb41e9c4:01 §§1–4, (1)–(7), support-triangle theorem.

## Statement

Let $K\subset\mathbb R^2$ be a compact convex body with $0$ interior. Use the three caps $x\ge0$, $y\ge0$, and $x+y\le0$. Suppose every cap has area strictly below $|K|/2$ and that each sector captured by two caps is its core triangle, the hull of $0$ and the two actual ray endpoints. Then the three bridge halfplanes through the outer sides of these cores, on the sides containing $0$, intersect in a bounded triangle containing $K$ with exactly the same six ray endpoints.

## Proof

Write the counterclockwise endpoints as $(A,0),(0,B),(-t,t),(-a,0),(0,-b),(r,-r)$, all radii positive. Write $X_i$ for the unique area captured only by cap $i$ and $Y_i$ for the double area missed by cap $i$. Then $(Y_1,Y_2,Y_3)=(at,br,AB)/2$. The two caps other than $i$ have total area $|K|-X_i+Y_i$ by counting sector memberships, so $X_i>Y_i$ for all $i$.

Each core bridge supports $K$. Otherwise a segment from a point of $K$ beyond the bridge to a relative-interior point of the bridge enters its open sector on the wrong side arbitrarily close to that bridge point, contrary to the exact core assumption. The resulting three constraints are $x/A+y/B\le1$, $x+(1-a/t)y\ge-a$, and $y+(1-b/r)x\ge-b$. Their intersection $D$ contains $K$. An unbounded sequence in $D$ would give a nonzero common recession vector by normalizing its points and taking a convergent subsequence. The outward linear form of each bridge, normalized to equal one at its endpoints, is strictly positive on every nonzero vector of its closed double cone. Hence the recession vector lies in an open unique cone. Cyclically permute the normals by the invertible map $(x,y)\mapsto(y,-x-y)$ as necessary, so that it is $(s,-u)$ with $0<u<s$. The first and third constraints then give $\alpha=B/A\le u/s\le1-\beta$ for $\beta=b/r$, so $\alpha+\beta\le1$.

Set $\ell=a/t$, $D_2=1-\alpha+\alpha\ell$, $D_3=\beta+(1-\beta)\ell$, both positive. In unique sector 2 use coordinates $(x,y)=\xi(0,B)+\eta(-t,t)$ with $\xi,\eta\ge0$. The first two constraints give $\xi+m\eta\le1$ and $\eta-n\xi\le1$, with $m=t(1-\alpha)/B>0$ and $n=B(1-\ell)/a$. They contain both coordinate unit points, so $m\le1$ and $n\ge-1$. The two lines meet at $((1-m)/(1+mn),(1+n)/(1+mn))$ with $1+mn=D_2/\ell>0$. The quadrant polygon consists of the origin, the two unit points and that intersection, allowing a repeated vertex. Its area in $(x,y)$ is $Bt(2+n-m)/(2(1+mn))$. In unique sector 3 take $(x,y)=(-a\xi,-b\eta)$. The last two constraints are $\xi+v\eta\le1$ and $\eta+w\xi\le1$, with $v=(1-\ell)b/a\le1$, $0<w=(1-\beta)a/b\le1$, and $1-vw=D_3>0$. The same vertex calculation with $m=v,n=-w$ works also when $v\le0$, since $w>0$ bounds $\xi$ and the two intersection coordinates are nonnegative. Its area is $ab(2-v-w)/(2D_3)$. Discarding the unused third constraint in each sector thus gives
$$
X_2\le E_2=\frac{2Ba+B^2(1-\ell)-at(1-\alpha)}{2D_2},\qquad
X_3\le E_3=\frac{2ab-b^2(1-\ell)-a^2(1-\beta)}{2D_3}.
$$
But $E_2>b^2/(2\beta)$ and $E_3>B^2/(2\alpha)$. Multiply by $2\beta D_2,2\alpha D_3$ respectively and add to get
$$
2a(\beta B+\alpha b)>\ell B^2+b^2+\beta at(1-\alpha)+\alpha a^2(1-\beta).
$$
Dividing by $a$ and completing squares gives $0>(B-\beta t)^2/t+(b-\alpha a)^2/a+(1-\alpha-\beta)(\beta t+\alpha a)$, impossible. Thus $D$ is bounded. It is full-dimensional and has three defining halfplanes, hence is a triangle. Each ray is already stopped by a bridge at its endpoint, which belongs to $K\subseteq D$.
