---
fact_id: a39d93bee9bf2fe9
kind: counterexample
author: "research-agent"
assurance: LLM-verified
subgoal_id: nov7-sharp-total-dimension-19
depends_on: []
verifier_run: c4ff05a3f641e4ad
target_match: null
---

## Statement

There is a full-dimensional rational polytope $C\subset\mathbb R^{14}\times\mathbb R^5$ with 17,770 nonempty integer fibers of positive volume. For one $0<r<(5/6)^5/2^{14}$, every point of $\mathbb Z^{14}\times\mathbb R^5$ belongs to a proper closed ambient halfspace whose intersection with $C$ has mixed-integer volume at most $r$ times that of $C$.

## Proof

# A counterexample to the strengthened depth bound in dimension 19

There is a full-dimensional rational polytope in $\mathbb R^{14}\times\mathbb R^5$
whose mixed-integer halfspace depth is uniformly less than $(5/6)^5/2^{14}$
after normalization by its total mixed-integer volume. At each point of
$\mathbb Z^{14}\times\mathbb R^5$, we give a proper closed halfspace that
contains the point and has mass below this bound. Mass is the sum of
five-dimensional volumes over the integer fibers.

## The simplex and its three sources

Work in the affine hyperplane $\sum_{\ell=0}^5 x_\ell=1$. Let $B$ be its
standard simplex with vertices $e_0,\ldots,e_5$ and centroid $q$.
Write $\rho S$ for the dilation $q+\rho(S-q)$. Use $|B|$ as the unit
of five-dimensional volume. Dropping the last coordinate identifies this
hyperplane with $\mathbb R^5$ by a rational affine isomorphism and multiplies
all volumes by the same constant.

For $j=0,1,2$, with subscripts on the first three coordinates read modulo
three, set $f_j(x)=x_j-\tfrac23 x_{j+1}-\tfrac13 x_{j+2}$. The scores sum
to zero, vanish at $q$, and lie in $[-1,1]$ on $B$. Define
$T_j=B\cap\{f_i\le0\text{ for }i\ne j\}$. Let $U_0$ be the simplex with vertices

$$
e_0,\quad (e_0+e_1+e_2)/3,\quad (3e_0+2e_2)/5,\quad e_3,\quad e_4,\quad e_5,
$$

and define $U_1,U_2$ by cyclic permutation. At the first three vertices of
$U_0$, the pairs of scores $(f_1,f_2)$ are
$(-1/3,-2/3)$, $(0,0)$, and $(-7/15,0)$. The last three vertices have
both scores zero. Thus $U_j\subseteq T_j$.

The determinant of the three active vertex columns gives $|U_j|=2/15$,
as the last three columns are coordinate vectors. In the active triangle
$\operatorname{conv}(e_0,e_1,e_2)$, the cap $f_j\ge0$ cuts the two edges
from $e_j$ at fractions $3/5$ and $3/4$ of their lengths. The cap in $B$
is the join of this triangle cap with $\operatorname{conv}(e_3,e_4,e_5)$,
so the same determinant argument gives its volume $\beta=9/20$.
Off the three score hyperplanes, a point has one or two positive scores.
The fraction with exactly one positive score is $2-3\beta$, since the
mean number of positive scores is $3\beta$. Cyclic symmetry then gives
$|T_j|=2/3-\beta=13/60$.

## The polytope and all its integer fibers

Use eleven ordinary integer coordinates and three selector coordinates
$s_0,s_1,s_2$. For a coordinate subset $I$, let $\mathbf1_I$ be its
indicator vector. Put
$r(z)=\sum_{\text{ordinary }i}z_i-5\sum_{j=0}^2z_{s_j}$ and
$\delta=69/100$. Take the convex hull $C$ of these generators:

| Base | Continuous generator | Number |
| --- | --- | ---: |
| $0$ | $B$ | 1 |
| One of $\pm\mathbf1_I$ for each $I\ne\varnothing$, choosing the sign with $r\ge0$ and the positive sign at a tie | $(1+\delta)U_j$, choosing any selector $s_j\in I$ or using $j=0$ if none is present | $2^{14}-1=16{,}383$ |
| $-\mathbf1_{J\cup\{s_j\}}$, for each selector $s_j$ and each five-element ordinary subset $J$ | $(1-\delta)T_j$ | $3\binom{11}{5}=1{,}386$ |

Call the generators in the second and third rows large and small, respectively.
Each small base has $r=0$, so the large generator with the same mask
has the opposite sign. All listed bases are distinct. The generators
are rational, and $C$ is full dimensional because the origin fiber
spans the continuous directions and the signed singleton bases span the
integer directions.

The projection lies in $[-1,1]^{14}$. At a nonzero integer base in the
projection, choose a coordinate equal to $\sigma\in\{-1,1\}$. Every
generator in a convex representation of that base must share this entry.
All those bases therefore belong to the same signed Boolean cube.
At every other coordinate an integer average of entries in $\{0,\sigma\}$
forces agreement. Hence the representation uses only the listed base itself,
and its actual fiber is exactly its generator.

At zero, only generators with $r=0$ can contribute, since $r$ is
nonnegative at every base. Each of these generators satisfies

$$
x_\ell\ \ge\ -\frac{\delta}{6}\sum_{j=0}^2z_{s_j}\qquad(0\le\ell\le5).
$$

A nonzero balanced large base is positive and has at least one selector,
so the dilation $(1+\delta)B$ satisfies these inequalities there. A small
base has exactly one negative selector, and its generator lies in
$(1-\delta)B$, whose lower coordinate bounds are $\delta/6$. The origin
generator also satisfies the inequalities. They are affine in $(z,x)$
and reduce to $x_\ell\ge0$ at zero. This proves that the origin fiber is
exactly $B$. In total there are $17{,}770$ nonempty integer fibers, all
of positive volume because $U_j\subseteq T_j$ are full dimensional and
both dilation factors are positive.

## A containing halfspace at every point

For the origin and small fibers use the three halfspaces
$H_j=\{(z,x):f_j(x)\ge5r(z)+3z_{s_j}\}$. They cover the origin fiber
because the scores sum to zero. At a small base of type $j$, its own
threshold is $-3$ and $f_j\ge0$ on its generator. The other thresholds
are zero, and the other cuts meet it only on their score hyperplanes,
which have zero fiber volume.

At an unbalanced large base every threshold is at least $5-3=2$,
whereas every score is at most $1+\delta<2$. At a balanced large base
the threshold is $3$ for a present selector, so those cuts also miss.
An absent selector gives a zero threshold, and its score is nonpositive
on the generator because the large source type is a present selector.
These last intersections have zero fiber volume. Thus each $H_j$
charges the origin cap and all small fibers of type $j$.

At a point in a large simplex, at least one of its six barycentric
coordinates, say $\lambda(x)$, is at least $1/6$. The affine score
$\lambda(x)-1/6$ defines a containing cap of volume fraction $(5/6)^5$
in that fiber by homothety. To isolate the
cap, expose its base $\sigma\mathbf1_I$ by a linear functional with
coefficients $\sigma$ on $I$ and $-\sigma/15$ off $I$. Its value there
is $|I|$. A distinct same-sign base either omits an element of $I$ or
adds an element outside $I$, so has smaller value. An opposite-sign
base has value at most $14/15$, and the origin has value zero.
Add a sufficiently large positive multiple of the exposing functional
minus $|I|$ to the affine cap score. The trace on this fiber stays the
same. All other fibers are excluded because they are compact, there
are finitely many, and the exposure gap is positive.

For a point outside $C$, strict separation from the compact convex
polytope gives a containing halfspace of zero mass.

## Exact mass comparison

Let $\Gamma=(5/6)^5$, $m=\tfrac2{15}(1+\delta)^5$ be the volume of
each large fiber, and $L=\binom{11}{5}\tfrac{13}{60}(1-\delta)^5$
be the total small-fiber volume of one type. The total volume is
$W=(2^{14}-1)m+1+3L$. The three $H_j$ have mass $\beta+L$ each, and
each isolated large-fiber cap has mass $\Gamma m$. Substitution gives

$$
W-2^{14}m=1+3L-m=\frac{6486053963}{300000000000}>0,\qquad
\Gamma m-\beta-L=\frac{1235613187493}{583200000000000}>0.
$$

Every mixed-integer point therefore has a containing halfspace of
normalized mass at most $\Gamma m/W<\Gamma/2^{14}$.
The [exact replay](../research/sharp-dimension-19/check.py) checks the signed support and the rational
comparisons. The [Lean theorem](../lean/SharpOC/SelectorCounterexample.lean)
checks the convex body, its actual integer fibers and mixed-integer
mass, and a uniform strict halfspace bound.
