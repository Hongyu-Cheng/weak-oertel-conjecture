# Continuous-simplex padding violates the exact 1/(e 2^n) bound

Status: analytic proof with independent mathematical review and exact
rational checks completed. This extension is not Lean-formalized. It concerns the
specific constant `1/e`, not the collaboration repository's weaker target
of some absolute positive constant below `1/e`.

## Theorem

Put

    n = 25 * 6^8 * 51^26,
    ell = 2^(n+8),
    d = 26+ell.

There is a full-dimensional rational polytope C in R^n x R^d, with nonempty
mixed-integer intersection S and full-dimensional nonempty integer fibers,
such that

    sup_(y in S) depth_S(y) < 1/(e 2^n).

Depth is the infimum of the normalized d-dimensional fiber-sum measure over
all containing closed ambient halfspaces. Equivalently it uses normalized
Hausdorff d-measure on these full Euclidean fibers. The result does not
require an approximation, an infinite-dimensional body, or an infinite
number of fibers. The displayed dimensions, while enormous, are finite.

The construction also violates the larger sharp constant Gamma_d/2^n.
It does not show that no positive universal constant c/2^n exists.

## 1. A base body with middle cuts below M/e

Use the generalized three-type construction proved in
[dimension-reduction-exploration.md](dimension-reduction-exploration.md),
with the following different exact parameters:

    r=9, d0=26,
    s=100/101,
    t=1/51,
    eta=203/10302,
    N=(25/18)*6^9*51^26,
    n=3N=25*6^8*51^26.

N is an integer because 18 divides 6^9. Keep the notation of that proof:
B is the centered 26-simplex, b=|B|, the three ordered sources T_a have
volume 6^(-9)b, their explicit centers are c_a, and

    P_a=c_a+s(T_a-c_a),
    A_a=t(T_a-c_a),
    K_I=2P_(a(I))+(|I|-1)c_(a(I)).

Let C0 be the finite convex hull (C) in that note. It is a full-dimensional
rational polytope with exactly the origin fiber B, the nonzero cube fibers
K_I, and the negative-unit fibers A_(tau(i)). All have dimension 26. Each
nonzero projection base is exposed. These conclusions use only the
geometric inequalities (A) of that note, which hold here:

    eta-t = 2(1-s)-eta = 1/10302 > 0,
    3-2s-11t = 4142/5151 > 0,
    3-2s-4eta = 4847/5151 > 0.

Write M=|K_I| and a0=|A_a|. The normalized quantities are

    m=M/b=(2^26/6^9)(100/101)^26,
    alpha=a0/b=(1/51)^26/6^9,
    E/b=3N alpha=25/6.

Exact rational arithmetic gives

    493/96 < m < 3968/771.                             (1)

The companion checker verifies both strict inequalities by positive
integer numerator certificates. Their roles are different and explicit.
The lower inequality implies

    17/9 < (32/87)m.                                  (2)

The upper inequality implies, with Delta=b+E-M,

    Delta/M = (31/6-m)/m > 1/256.                      (3)

The elementary bound e<87/32 shows from (2) that

    b/2+E/3 = 17b/9 < M/e.                            (4)

For completeness, this bound on e follows directly from its power series.
The terms through 1/4! sum to 65/24. For j>=0,

    1/(5+j)! <= (1/120)(1/6)^j.

Summing this geometric majorant bounds the remaining tail by 1/100. Thus

    e <= 65/24+1/100 = 1631/600 < 87/32.

No decimal estimate of e is used.

The explicit ambient cuts (F) of the generalized construction therefore
cover all points of the origin fiber and have mass exactly 17b/9<M/e.
The proof of those cuts is independent of the ordinary simplex cap
constant: it uses only the geometry conditions (A). In particular it is
valid with the parameters above even though the desired global target
will now be 1/e rather than Gamma_26.

The total mixed-integer volume of C0 is

    W=(2^n-1)M+b+E=2^n M+Delta,

and (3) gives

    W/(2^n M) > 1+1/(256*2^n) = 1+1/ell.              (5)

The outer fibers are smaller than the cube fibers, since

    a0/M=(t/(2s))^26<1.                               (6)

## 2. A finite simplex factor with depth close enough to 1/e

For every positive integer ell, put

    Gamma_ell=(ell/(ell+1))^ell.

One has the strict elementary inequality

    e Gamma_ell < 1+1/ell.                            (7)

Indeed, for x>0,

    log(1+x)=integral_0^x 1/(1+u) du > x/(1+x).

The strict inequality follows because the integrand is strictly greater
than 1/(1+x) on the interval [0,x). With x=1/ell, this says

    (ell+1)log(1+1/ell)>1.

Exponentiation gives e<(1+1/ell)^(ell+1), which rearranges to (7).
Combining (5) and (7),

    Gamma_ell M/W < 1/(e 2^n).                        (8)

Let J be any rational full ell-simplex, for example the convex hull of
0 and the ell standard unit vectors. Write j0=|J|>0.
At every point u of J, at least one of its ell+1 barycentric coordinates
is at least 1/(ell+1). The cap where that coordinate is at least its value
at u is a containing closed halfspace cap of volume at most

    Gamma_ell j0.                                     (9)

To verify (9), the cap at barycentric level a is a homothetic copy of J
with length ratio 1-a and therefore volume (1-a)^ell j0. If a=1 the cap
is a vertex, whose ell-volume is zero. This proves the assertion for all
u, including boundary points, without appealing to centroid existence.

## 3. The padded rational body and every mixed-integer point

Set

    C=C0 x J in R^n x (R^26 x R^ell).

A product of full-dimensional rational polytopes is again such a polytope.
Its integer projection and exact fiber census are those of C0. Each fiber
is the corresponding base fiber F times J. These fibers have full dimension
d=26+ell. Fubini's product-volume identity gives |F x J|=|F|j0, and the total
mixed-integer volume is Wj0.

Take any y=(z,x,u) in the induced mixed-integer set.

If z=0, choose the explicit base halfspace from (4) containing (0,x),
and give its normal zero coefficients on the new ell coordinates. This is
a proper closed ambient halfspace containing y. Its mixed-integer mass is

    (17b/9)j0 < (M/e)j0 < Wj0/(e 2^n),

where the last inequality follows from W>2^n M.

If z is a nonzero cube base or a negative unit base, it is exposed among
the finitely many integer bases. Select a cap (9) containing u in J.
Its product with the full F factor is a containing halfspace cap in F x J
of volume at most |F| Gamma_ell j0. This is at most M Gamma_ell j0 by (6).

Here is the exact ambient isolation argument. Write the selected factor
cap as {v:a dot v>=a dot u}, with a nonzero. Let g be an integer-coordinate
linear functional strictly maximizing at z among all the other bases.
For A>0 consider the ambient halfspace

    a dot(v-u)+A[g(w)-g(z)] >= 0.

At w=z this is exactly the selected factor cap and contains y. For every
other integer base w, the bracket is strictly negative. There are only
finitely many such bases, and the continuous fibers and J are compact,
so a dot(v-u) has a finite maximum over their union. Taking A larger than
that maximum divided by the smallest positive exposure gap excludes all
other fibers strictly. Thus the resulting actual closed ambient halfspace
has mass at most M Gamma_ell j0. By (8) this is strictly less than
Wj0/(e 2^n).

Every point has now been treated, and both classes use a uniform strict
upper bound below the desired threshold. Taking a supremum of their
normalized depths proves the theorem. No replacement by open halfspaces,
no loss of boundary mass, and no unspecified limiting passage occurs.

## Scope of this result

The factor dimension ell is specified as the finite integer 2^(n+8).
The convergence Gamma_ell->1/e is not used as an unquantified choice:
(7) and the explicit rational defect bound (3) establish the exact finite
value that suffices.

The new continuous factor is a product, which is allowed in a
counterexample. The original universal statement requires its lower bound
for every convex body, including products. Although the new fibers are
products rather than simplices, only an upper bound on their depth is
needed, and (9) supplies that bound in the simplex factor directly.

The final violation concerns the exact constant 1/e. Its size is very
small, and it does not by itself refute a bound with some unspecified
smaller positive absolute constant. No such implication is claimed.
