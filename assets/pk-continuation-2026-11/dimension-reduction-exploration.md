# Dimension reduction using source-shaped outer fibers

Status: analytic proof with independent model review and exact rational checks;
not Lean-formalized. One independent review checked the mixed-type origin
containment, the paid/unpaid cube cuts, and the scalar certificate. This note
is not part of the completed Lean source modules and makes no claim about the
weaker `1/(e 2^n)` bound.

## Concrete improvement

The same cube-completion mechanism admits a rational counterexample with

    d = 26,    n = 19227 * 10^40,

in place of `d=23, n=3*10^92`. The change is geometric: the outer fibers are
small copies of their own ordered-chain source simplices, rather than small
copies of the whole middle simplex. The key further change is to verify the
origin-fiber containment directly from barycentric coordinate inequalities.
The stronger intermediate condition `c_i+2A_j subset P_i` is unnecessary.

The decimal magnitude of n is approximately `1.923*10^44`. This is a reduction
of about 48 orders of magnitude, but is still an extremely large integer
dimension. It is not a low-dimensional counterexample.

## A generalized three-type construction

Fix an integer r>=1, put D=3r and d=D-1, and let B be a centered d-simplex
with D barycentric coordinates lambda_1,...,lambda_D. Write b=|B|. Indices
are cyclic, and f_j=lambda_j-lambda_(j+1). Thus each closed cut f_j>=0
has volume b/2, the f_j are nonzero linear forms, and their sum is zero.

For a=0,1,2 let R_a be one of the three residue classes modulo 3 and set

    T_a = B intersect {f_j<=0 : j not in R_a}.

As in the direct proof, the coordinates form r increasing chains of length
three. Each T_a is a full d-simplex of volume 6^(-r)b. Its vertex average
c_a has, on each increasing chain, barycentric coordinates

    (1/(3D), 5/(6D), 11/(6D)).

The two internal-edge values f_j(c_a) are -1/(2D) and -1/D. The value on
a root edge is 3/(2D). In particular,

    c_min=1/(3D),  c_max=11/(6D),  c_max/c_min=11/2.

On a missed edge j not in R_a, max_(T_a) f_j=0. All these statements follow
from the explicit three suffix vertices on each chain; there is no
assumption about centroid rounding.

Choose rational s,t,eta and a positive integer N such that

    1/2 < s < 1,
    0 < t < eta < 2(1-s),   eta < 1,
    11t <= 3-2s,
    4eta < 3-2s.                                      (A)

Define

    P_a = c_a+s(T_a-c_a),
    A_a = t(T_a-c_a),
    M = 2^d s^d 6^(-r)b,
    a0 = t^d 6^(-r)b,
    E = 3N a0,
    Gamma = (d/(d+1))^d.

Here every outer fiber A_a contains 0 in its interior. All A_a have the
same volume a0 although their shapes and orientations differ. Assume also

    b+E > M,
    b/2+E/3 < Gamma*M.                                (B)

There are n=3N integer coordinates, N of each type tau(i). For each nonempty
I subset {1,...,n}, let k=|I|, choose any i(I) in I, put a(I)=tau(i(I)), and
set

    z_I = sum_(i in I) e_i,
    K_I = 2P_(a(I))+(k-1)c_(a(I)).

Define the convex body C as the convex hull of

    {0} x B,
    {z_I} x K_I              (I nonempty),
    {-e_i} x A_(tau(i))      (1<=i<=n).                (C)

Every generating fiber is a full simplex, every coordinate is rational,
and C is a full-dimensional rational polytope. The positive cube fibers
have the common volume M, while the negative unit fibers have volume a0.

## Exact origin-fiber containment with different outer shapes

The projection and exposure arguments from the direct proof apply unchanged:
its integer points are the cube vertices and the negative unit vectors;
each nonzero cube vertex and each negative unit vector is exposed and has
exactly its prescribed fiber. To establish that the origin fiber is B, it
is enough to prove, for every nonempty I,

    K_I + sum_(i in I) A_(tau(i)) subset (k+1)B.        (D)

For k=1, the selected type is the only type in I. Directly,

    2P_a+A_a = (2s+t)T_a+(2-2s-t)c_a subset 2B,

because t<2(1-s), so both coefficients are nonnegative and sum to 2.

For k>=2, write a=a(I), take p in P_a and u_i in A_(tau(i)), and consider

    y = [2p+(k-1)c_a+sum_i u_i]/(k+1).

For every barycentric coordinate ell,

    lambda_ell(p) >= (1-s)lambda_ell(c_a),
    linear_part(lambda_ell)(u_i) >= -t lambda_ell(c_(tau(i))).

The affine constant is handled by the coefficients 2+(k-1)=k+1. Hence

    (k+1)lambda_ell(y)
       >= (k+1-2s)c_min - kt c_max
       = [2(k+1-2s)-11kt]/(6D).

This is nonnegative under (A):

    2(k+1-2s)-11kt
       >= 2(k+1-2s)-k(3-2s)
       = (k-2)(2s-1) >= 0.

Thus y belongs to B and (D) holds. In a convex representation at integer
base 0 the negative-unit weights satisfy

    mu_i = sum_(I containing i) lambda_I,
    lambda_0+sum_I (|I|+1)lambda_I = 1.

Applying (D) to each term proves that the entire origin fiber is contained
in B; the reverse inclusion is part of (C). This verifies the exact fiber
census, including potentially mixed types in every convex representation.

The total mixed-integer volume is consequently

    W = (2^n-1)M+b+E = 2^n M+(b+E-M) > 2^n M.         (E)

## Actual oblique cuts at every point of the origin fiber

Fix a row j. Call an integer coordinate paid when j is a root of its type;
there are exactly N paid coordinates. For every unpaid coordinate i put

    h_i = -f_j(c_(tau(i))) in {1/(2D),1/D}.

Choose R=3(n+1), and define the closed ambient halfspace

    H_j = {(z,x): f_j(x)+sum_i beta_i z_i >= 0},
    beta_i = -R         on paid coordinates,
    beta_i = eta*h_i    on unpaid coordinates.         (F)

For an unpaid outer fiber at -e_i, its largest cut score is

    t h_i-eta h_i < 0.

For a paid outer fiber, every score is strictly positive. Indeed T_a and
c_a lie in B, whose f_j values lie in [-1,1], so every point of A_a has
f_j value at least -2t; now R>2t follows from (A), n>=3, and t<1.
Thus H_j includes exactly the N paid outer fibers and excludes the others.

If a nonempty cube set I contains a paid coordinate, its continuous cut
score is at most k+1, since P_a,c_a subset B. Its integer contribution is
at most -R+(k-1)eta/D <= -R+k-1. Their sum is at most 2k-R<0.

Suppose instead all coordinates in I are unpaid. If k=1, the largest score
is

    [-2(1-s)+eta]h_(i(I)) < 0.

For k>=2 it is bounded above by

    -(k+1-2s)/(2D)+k eta/D.

This is strictly negative under (A), because

    k+1-2s-2k eta
       > k+1-2s-k(3-2s)/2
       = (k-2)(s-1/2) >= 0.

Therefore H_j excludes every nonzero cube fiber. All exclusions are strict;
no positive-dimensional boundary contribution has been discarded. On the
origin fiber its cut is the ordinary half-simplex f_j>=0, so

    vol_MI(S intersect H_j) = b/2+N a0 = b/2+E/3 < Gamma*M.

The cuts cover B because sum_j f_j=0. Thus every point of the origin fiber
admits an insufficient ambient closed halfspace.

At any other fiber, exposure of its integer base lets one isolate any
ordinary cap by a sufficiently large multiple of its exposing integer
functional. The ordinary simplex cap bound gives an insufficient containing
halfspace of mass at most Gamma*M on cube fibers, and at most Gamma*a0
on outer fibers. Since t<2(1-s)<2s, one has a0<M. The argument uses actual
containing closed halfspaces and finite strict exposure gaps.

Combining these bounds with (E) gives

    sup_(y in S) depth_S(y) <= Gamma*M/W < Gamma/2^n.

This completes the generalized construction under the explicit rational
conditions (A) and (B).

## An exact smaller integer dimension

Use

    r=9, d=26,
    s=51/52,
    t=999/26000,
    eta=1999/52000,
    N=6409*10^40,
    n=3N=19227*10^40.

The conditions in (A) are immediate rational comparisons; for example,

    eta-t = 2(1-s)-eta = 1/52000,
    3-2s-11t = 16011/26000 > 0,
    3-2s-4eta = 11501/13000 > 0.

For (B), divide by b and use the exact rational quantities

    m = M/b = (2^26/6^9)(51/52)^26,
    alpha = a0/b = (999/26000)^26/6^9,
    Gamma = (26/27)^26.

The two required strict inequalities are

    1+3N alpha-m > 0,
    Gamma*m-1/2-N alpha > 0.

The companion standard-library Fraction checker verifies these inequalities
by exact integer arithmetic and emits their positive numerators and
denominators. For orientation only, the margins are approximately
0.00022149939 and 0.00010076887 respectively. The proof uses the exact
inequalities, not these decimal approximations.

## Further routes and their present obstacles

The generalized scalar feasibility condition, allowing the total outside
mass E to vary continuously, is

    M/b > (1/2)/(3 Gamma-1).

It follows by eliminating E from (B). A clone count is then chosen in the
strict interval

    (M/b-1)/(3 alpha) < N < (Gamma*M/b-1/2)/alpha.

The old choice E=3b is unnecessarily rigid: it fails already at d=26,
where Gamma<3/8. Letting E vary is essential to the displayed improvement.

Within the simple equal-length-three-chain family, increasing d eventually
hurts: each source volume is 6^(-r)b, and making the outer homothety t larger
does not compensate indefinitely for raising it to the power d=3r-1.
Exact tests of simple rational parameters favor r=9 over nearby r. This is
an observation about that parameter search, not a global optimality theorem.

A different potential route is to encode many outer fibers at distinct
negative 0/1 vectors using fewer integer coordinates, rather than allocating
one coordinate per copy. This is currently unproved. It introduces extra
integer fibers and additional origin representations. A concrete constraint
is already visible: if a negative outer vector has h ones, cancellation by
the h positive unit bases forces, by Brunn-Minkowski,

    M <= (1+1/h)^d b

when each of those unit fibers has volume M. Thus long binary codes cannot
simply be substituted into the present construction. Exact origin control,
all additional fibers, and simultaneous separating cuts would have to be
proved anew. No dimension bound is claimed for this route.
