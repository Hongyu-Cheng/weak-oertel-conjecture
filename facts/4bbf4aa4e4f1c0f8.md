---
fact_id: 4bbf4aa4e4f1c0f8
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-w33-independent-endpoint-capped-plateau
depends_on: []
verifier_run: 9edc11add679d454
target_match: null
---

## Source

- [5afcd34e3cea10b1](../candidates/5afcd34e3cea10b1.json), 5afcd34e3cea10b1:01 Construction and proof, midpoint density and capped acceptance.
- [5afcd34e3cea10b1](../candidates/5afcd34e3cea10b1.json), 5afcd34e3cea10b1:02 Last paragraph, exact equal-interval obstruction to independent construction.

## Statement

Let $A,B,D$ be compact convex $d$-fibers at three consecutive integer bases, $d\ge1$, with positive volumes and $(A+D)/2\subset B$. Put $a=|A|$ and $c=|D|$, and let $f$ be the midpoint density of independent uniform $X\in A$ and $Y\in D$. Then
$$
f(x)=\frac{2^d}{ac}|A\cap(2x-D)|,\qquad f^{1/d}\ \text{is concave on }(A+D)/2.
$$
For $0<r\le\min(a,c)$ and $h>1$, set $g=rf$ and $J_h=\{g\ge h-1\}$. If $J_h$ has positive volume, it is compact and convex, and the middle-layer measure $h\mathbf1_{J_h}\,dx$ assigns to every closed ambient halfspace at most the original summed volume of its three traces. If $h|J_h|\ge M/2$ for total mixed volume $M$, the uniform probability on $J_h$ assigns at most twice the original normalized mass to every such halfspace.

For three identical intervals of length $a$, the largest plateau mass obtainable by this construction is $9a/8$, attained at $r=a$ and $h=3/2$, strictly below $M/2=3a/2$.

## Proof

The lifted convex hull of the three layers has exactly the stated fibers. Its endpoints are exposed, and any mixture at the middle layer is a mixture of a point in $B$ and an endpoint midpoint in $(A+D)/2\subset B$. Thus the summed measure is the actual one.

The change of variables $y=2x-p$ in the joint density of $(p,Y)$ gives the stated $f$. For $x,y\in(A+D)/2$, the Minkowski interpolant of $A\cap(2x-D)$ and $A\cap(2y-D)$ lies in $A\cap(2((1-t)x+ty)-D)$ at weight $t\in[0,1]$. The two compact convex sets are nonempty, allowing zero volume. Brunn–Minkowski yields concavity of the indicated root. The convolution is continuous by continuity of translations of the integrable indicator of $D$ in $L^1$, bounding the other indicator by one. The positive superlevel is therefore a compact convex subset of $(A+D)/2$.

Give the independent endpoint pair law mass $r$. Its source marginals are bounded by the two fiber volume measures because their densities are $r/a,r/c\le1$. Keep a pair with output $x\in J_h$ with probability $\min(1,h/g(x))$, and reject all other pairs. The retained pair measure has output density $\min(g,h)\mathbf1_{J_h}$ and still obeys both endpoint capacities. Add singleton output mass at the middle with density $(h-g)_+\mathbf1_{J_h}$, bounded by one because $g\ge h-1$ there. Their sum is exactly the stated target. Whenever a midpoint lies in a closed halfspace, at least one of its source points is in that same halfspace, since the complement is convex. Integrating that indicator inequality against the retained pair measure and adding the middle singleton mass gives domination by the three original traces. Dividing by $h|J_h|\ge M/2$ proves the probability assertion.

For identical centered intervals the maximal allowed $r=a$ gives $g(x)=2(1-2|x|/a)$ on $[-a/2,a/2]$ and zero outside. For $1<h\le3$, its plateau mass is $(a/2)h(3-h)$, whose maximum is $9a/8$ at $h=3/2$. At larger $h$ the plateau is empty. For each $h$ decreasing $r$ only shrinks the superlevel. This proves the exact independent-construction obstruction. In contrast, the same-coordinate endpoint pairing of mass $a$, plus all middle singletons, has uniform target density two on the common interval and obeys the same halfspace indicator bound.
