---
fact_id: ae578ba00acc8dab
kind: counterexample
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-binary-isolation-exact-depth-and-finite-radial-obstruction
depends_on: ["f56afa6ff9366e70", "6769574fc1bd9f8d"]
verifier_run: 4ba7338bc3f4df45
target_match: null
---

## Source

- [4e0a45efacd4af50](../candidates/4e0a45efacd4af50.json), 4e0a45efacd4af50:01 §§1–3, (1)–(4), exact integer fibers, minimal cover and depth.
- [4e0a45efacd4af50](../candidates/4e0a45efacd4af50.json), 4e0a45efacd4af50:02 §4, simultaneous radial factors.

## Statement

For every $n\ge2$ there is a full-dimensional convex body in $\mathbb R^n\times\mathbb R^2$ with $2^n+1$ positive integer fibers and an inclusion-minimal cover of its mixed set by $3(2^n-1)$ closed halfspaces, each of raw mass $B_*=6811/8910$. Its exact maximum normalized mixed halfspace depth is
$$
\frac{4/9}{2^n-4978/4865}.
$$
In particular its ratio to $(4/9)2^{-n}$ decreases to one. For the same body, independently scale each actual integer fiber about zero by a factor in $(9/10,11/10)$, keeping the displayed ambient cap planes fixed. If the resulting array is convexly compatible, its total mass does not decrease, and no displayed cap mass increases, then every factor is one.

## Proof

Use the centered triangle $T$, matrix $J$, and core $A,D,B$ from f56afa6ff9366e70. Its summed area is $42/25$, and each of the three cylindrical caps with margins $\ell_0(x)=-x_1-x_2$, $\ell_1(x)=x_1$, $\ell_2(x)=x_2$ has mass $B_*$. The middle fiber $D=(A+B)/2$ contains $T$, by taking the same point of $T$ in both affine images. The supports of $A,B,D$ in these three directions are all $2/3$. In fact the images under $J$ of the vertices $(-1/3,-1/3),(2/3,-1/3),(-1/3,2/3)$ are $(1,-1),(0,1),(-1,0)$. Thus the maximizing vertex value is unchanged under either of the two linear maps, and the other two values stay strictly lower. Minkowski averaging preserves those supports.

Write the integer base as $(z,b)$, with $b$ having $n-1$ coordinates. Put the three core fibers at $(0,0),(1,0),(2,0)$. At each $(0,b),(1,b)$ with $b\ne0$ binary put $\rho T$, where $\rho^2=6811/1980<4$. Its area is $B_*/(4/9)$. Take the convex hull of these lifted fibers. Its projection satisfies $0\le b_i\le1$, $z\ge0$, $z+b_i\le2$, so the only possible integer bases are exactly the listed sites. In any representation over an integer binary $b$, coordinate extremality forces every generator used to have that same $b$. Thus at nonzero $b$ the two endpoints retain their exact fibers. Over $b=0$, the endpoint fibers are exact and their midpoint is the specified middle fiber. There are $2^n+1$ sites. The projection contains a spanning base simplex and each specified fiber has positive area, giving full ambient dimension.

Take the three core caps $\ell_i(x)\ge2\sum_j b_j$. For a nonzero binary $v$ put $\delta_v(b)=\sum_{v_j=0}b_j+\sum_{v_j=1}(1-b_j)$. At a regular site $(0,v)$ take three caps $\ell_i(x)\ge 2[2\delta_v(b)+z]$. At $(1,v)$ use $\ell_i(x)\ge2[2\delta_v(b)+1-z]$. In each regular group the bracket vanishes at its assigned site and is at least one at every other listed site. All supports in these directions are strictly below $4/3$, so each group isolates its own assigned fibers. The core caps retain their old masses. On a regular triangle the cap $\ell_i(x)\ge0$ is a vertex homothet of scale $2/3$, so each regular cap also has mass $B_*$. At every covered fiber the three own margins sum to zero, hence these caps cover the entire mixed set. Each individual cap is essential: its corresponding vertex of the regular triangle, or of $T$ in the middle core fiber, lies strictly in it and in neither of the other two caps of that group. All other groups strictly miss that fiber. There are $2^n-2$ regular groups and one core group.

The cover bounds every raw depth by $B_*$. At a regular centroid, every containing ambient halfspace has own-fiber mass at least $B_*$ by 6769574fc1bd9f8d with $m$ equal to that fiber's area. If its trace is the whole fiber this is immediate as well. Thus the maximum is exactly $B_*$. Divide it by $42/25+(2^n-2)B_*/(4/9)$ and use $(4/9)(42/25)/B_*=4752/4865$.

After the specified radial changes every support in a displayed continuous direction is at most $22/15<2$, so the same isolation persists. Each regular cap now has mass $B_*$ times its own factor squared, forcing every regular factor to be at most one. If the total mass does not decrease, the core mass cannot decrease. Its three cap budgets also do not increase. Compatibility at the core midpoint is precisely the required Minkowski inclusion of the two scaled endpoint fibers into the scaled middle fiber. Apply f56afa6ff9366e70 to force the three core factors to be one. Every regular fiber has positive area, so total nondecrease now forces each regular factor to be one.
