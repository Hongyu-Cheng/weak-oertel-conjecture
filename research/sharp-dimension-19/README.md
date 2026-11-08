# A counterexample to the strengthened depth bound in dimension 19

There is a full-dimensional rational polytope $C\subseteq\mathbb R^{14}\times\mathbb R^5$
and a constant $r_*<(5/6)^5/2^{14}$ such that every point of
$\mathbb Z^{14}\times\mathbb R^5$ lies in a proper closed halfspace $H$ with
$\mu(C\cap H)/\mu(C)\le r_*$. Here $\mu$ sums five-dimensional volumes over
the integer fibers.

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
$T_j=B\cap\{f_i\le0\text{ for }i\ne j\}$, so $f_j\ge0$ on $T_j$.
Let $U_0$ be the simplex with vertices

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
Each $f_j$ is nonconstant on the continuous affine space, so its zero set
has five-dimensional volume zero. Away from those hyperplanes, a point
has one or two positive scores.
The fraction with exactly one positive score is $2-3\beta$, since the
mean number of positive scores is $3\beta$. Cyclic symmetry then gives
$|T_j|=2/3-\beta=13/60$.

## The polytope and all its integer fibers

Use eleven ordinary integer coordinates and three selector coordinates
$s_0,s_1,s_2$. For a coordinate subset $I$, let $\mathbf1_I$ be its
indicator vector. Put
$r(z)=\sum_{\text{ordinary }i}z_i-5\sum_{j=0}^2z_{s_j}$ and
$\delta=69/100$. The polytope $C$ is the convex hull of the following generators.

| Base | Continuous generator | Number |
| --- | --- | ---: |
| $0$ | $B$ | 1 |
| One of $\pm\mathbf1_I$ for each $I\ne\varnothing$, choosing the sign with $r\ge0$ and the positive sign at a tie | $(1+\delta)U_j$, choosing any selector $s_j\in I$ or using $j=0$ if none is present | $2^{14}-1=16{,}383$ |
| $-\mathbf1_{J\cup\{s_j\}}$, for each selector $s_j$ and each five-element ordinary subset $J$ | $(1-\delta)T_j$ | $3\binom{11}{5}=1{,}386$ |

Call the generators in the second and third rows large and small, respectively.
Each small base has $r=0$, so the large generator with the same mask
has the opposite sign. All listed bases are distinct. The generators
are rational. The copy of $B$ at base zero spans the continuous directions.
Differences from any point in that copy to points above the 14 signed
singleton bases project onto a basis of the integer coordinate space.
Thus $C$ is full dimensional.

The projection lies in $[-1,1]^{14}$. At a nonzero integer base in the
projection, choose a coordinate equal to $\sigma\in\{-1,1\}$. Every
generator in a convex representation of that base must share this entry.
All those bases therefore belong to the same signed Boolean cube.
At every other coordinate an integer average of entries in $\{0,\sigma\}$
forces agreement. Hence the representation uses only the listed base itself,
and its fiber is exactly its continuous generator.

At zero, only generators with $r=0$ can contribute, since $r$ is
nonnegative at every base. Each of these generators satisfies

$$
x_\ell\ \ge\ -\frac{\delta}{6}\sum_{j=0}^2z_{s_j}\qquad(0\le\ell\le5).
$$

At a nonzero large base with $r=0$, the tie rule gives positive sign and
$r=0$ forces at least one selector. The generator lies in $(1+\delta)B$,
where each coordinate is at least $-\delta/6$. At a small base the
selector sum is $-1$ and the generator lies in $(1-\delta)B$, where each
coordinate is at least $\delta/6$. The copy of $B$ at zero also satisfies
the inequalities. They are preserved under convex combinations and force
all coordinates to be nonnegative at base zero, so the origin fiber is
exactly $B$. In total there are $17{,}770$ nonempty integer fibers, all of
positive volume because $U_j\subseteq T_j$ are full dimensional and both
dilation factors are positive.

## A containing halfspace at every point

For the origin and small fibers use the three halfspaces
$H_j=\{(z,x):f_j(x)\ge5r(z)+3z_{s_j}\}$. They cover the origin fiber
because the scores sum to zero. At a small base of type $j$, its own
threshold is $-3$ and $f_j\ge0$ throughout the fiber. The other thresholds
are zero and the other scores are nonpositive, so those cuts can meet the
fiber only on their zero sets.

At an unbalanced large base every threshold is at least $5-3=2$,
whereas every score is at most $1+\delta<2$. At a balanced large base
the threshold is $3$ for a present selector, so those cuts also miss.
An absent selector gives a zero threshold, and its score is nonpositive
on the generator because the large source type is a present selector.
These last intersections have zero fiber volume. Thus each $H_j$
has positive-volume traces only on the origin cap and the small fibers
of type $j$, which it contains in full.

At a point in a large simplex, at least one of its six barycentric
coordinates, say $\lambda(x)$, is at least $1/6$. The affine score
$\lambda(x)-1/6$ defines a containing cap. This cap is the image of the
simplex under dilation about the vertex where $\lambda=1$ by a factor
$5/6$, so its volume is $(5/6)^5$ times the fiber volume. To isolate the
cap, expose its base $\sigma\mathbf1_I$ by a linear functional with
coefficients $\sigma$ on $I$ and $-\sigma/15$ off $I$. Its value there
is $|I|$. A distinct same-sign base either omits an element of $I$ or
adds an element outside $I$, so has smaller value. An opposite-sign
base has value at most $14/15$, and the origin has value zero.
Add a sufficiently large positive multiple of the exposing functional
minus $|I|$ to the affine cap score. The trace on this fiber stays the
same. All other fibers are excluded because they are compact, there
are finitely many, and the exposure gap is positive. The three $H_j$
and the isolated cap halfspaces are proper because their continuous
scores are nonconstant.

For a point outside $C$, strict separation from the compact convex
polytope gives a proper containing halfspace disjoint from $C$.

## Exact mass comparison

Let $\Gamma=(5/6)^5$, $m=\tfrac2{15}(1+\delta)^5$ be the volume of
each large fiber, and $L=\binom{11}{5}\tfrac{13}{60}(1-\delta)^5$
be the total small-fiber volume of one type. The total volume is
$W=\mu(C)=(2^{14}-1)m+1+3L$. The three $H_j$ have mass $\beta+L$ each, and
each isolated large-fiber cap has mass $\Gamma m$. The exact margins are

$$
W-2^{14}m=1+3L-m=\frac{6486053963}{300000000000}>0,\qquad
\Gamma m-\beta-L=\frac{1235613187493}{583200000000000}>0.
$$

The second margin bounds the mass of each $H_j$ by $\Gamma m$, and the
first gives $r_*=\Gamma m/W<\Gamma/2^{14}$. The same $r_*$ applies to all
mixed-integer points, including points outside $C$.

## Verification

Run `python3 -B research/sharp-dimension-19/check.py` from the repository
root to enumerate the signed support, check the affine guard and cut
thresholds on it, and reproduce the rational margins. The geometric
argument above identifies the fibers over that support and rules out
any others.

[`SharpOC.Selector.sharp_oc_counterexample`](../../lean/SharpOC/SelectorCounterexample.lean)
formalizes the convex body and uniform strict depth bound using its
actual mixed-integer measure. The [Lean replay instructions](../../lean/README.md#reproduce-the-verification)
include the axiom audit.
