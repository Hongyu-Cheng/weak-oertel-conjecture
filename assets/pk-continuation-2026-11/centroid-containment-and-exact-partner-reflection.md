# Centroid containment by facet moments and exact partner reflection

The ordinary containment inequalities below have complete proofs. Their mixed
applications use the stated simplex-volume or polytope facet-moment conditions;
these conditions are not asserted for arbitrary partners.

The cone comparison underlying (1) is classical: see B. Grunbaum,
[*Partitions of mass-distributions and of convex bodies by hyperplanes*](https://msp.org/pjm/1960/10-4/pjm-v10-n4-p18-p.pdf),
Section 3, printed p.1259. The complete elementary comparison is retained
below; the mixed reflection and core consequences are derived explicitly.

## A one-sided first-moment comparison

Let d>=2. Let f:[0,L] -> [0,infinity) be the section-volume density of a
full-dimensional compact convex body cut off by the hyperplane t=0. Assume
f(0)=S>0, and write V=integral f(t)dt. Thus f^(1/(d-1)) is concave on its
support by ordinary Brunn--Minkowski. Then

    integral t f(t)dt <= d V^2/((d+1)S).                 (1)

Here the slicing parameter may be an affine functional: the fixed coarea
factor is included in f and does not change its root concavity.

Put T=dV/S and k(t)=S(1-t/T)_+^(d-1). Its volume is V and its first moment
is S T^2/[d(d+1)]=dV^2/[(d+1)S]. We justify that f has no larger first
moment. If L>T and f(T)>0, concavity between 0 and T makes f^(1/(d-1))
at least the cone's affine root on [0,T], strictly on a nonempty interval;
the additional positive mass after T contradicts equal volume. For a convex
body, every interior section of its projection has positive volume, so L>T
would indeed imply f(T)>0. Hence L<=T.

On [0,L], subtract the cone's affine root from f^(1/(d-1)). The difference
is concave and zero at 0. Its quotient by t is nonincreasing for t>0.
Consequently its sign, and the sign of f-k, can change only from positive
to negative. Extend f by zero on (L,T]; the same sign order persists there.
Equal integrals then imply that for a crossing parameter c,

    integral t(f-k)dt = integral (t-c)(f-k)dt <=0.

If there is no genuine crossing, equal volume implies equality almost
everywhere and the conclusion is the same. This proves (1). In dimension
one the density on a nondegenerate interval is constant; (1) reads
V^2/(2S) and holds with equality.

## Quantitative simplex containment of the centroid

Let B be a convex d-body, d>=1, and let Delta subset B be a nondegenerate
d-simplex. Write a=|Delta|, V=|B|, R=V/a, and let lambda_0,...,lambda_d be
the affine barycentric functions of Delta. Then, for every i,

    lambda_i(g_B) >= (2-R)/(d+1).                      (2)

Equivalently,

    g_B belongs to g_Delta+(R-1)(Delta-g_Delta).        (3)

In particular, if a>=V/2, then g_B belongs to Delta. At a>V/2 it belongs
to its interior, with the quantitative barycentric margin in (2).

To prove (2), put lambda=lambda_i and split B into its nonnegative and
negative lambda parts. The positive first moment is at least its value
on Delta, namely a/(d+1). Let m be the negative part's volume. Then
m<=V-a. If m>0, the plane lambda=0 is a proper section of B and contains
the opposite facet of Delta. Its coarea section density S is at least
d a, since Delta has lambda-height one and volume equal to its base
density divided by d. Applying (1) to t=-lambda on the negative part gives

    -integral_(B intersect {lambda<0}) lambda dx
       <=d m^2/[(d+1)S] <=m^2/[(d+1)a].

If m=0, the same upper bound is zero directly. Therefore

    V lambda(g_B)
       >= a/(d+1) -(V-a)^2/[(d+1)a]
        = V(2-V/a)/(d+1),

which proves (2). Formula (3) is precisely the barycentric description of
that nonnegative homothety, including R=1, when equality of contained
full-dimensional convex bodies makes B=Delta.

The coordinate bound and the half-volume threshold are sharp. For the
standard Delta=conv(0,e_1,...,e_d), take B_R=conv(0,R e_1,e_2,...,e_d),
R>=1. Then |B_R|/|Delta|=R and the coordinate opposite 0 satisfies
lambda_0(g_BR)=(2-R)/(d+1). If R>2 the centroid is outside Delta.

## Actual reflection from a large inscribed partner simplex

For a convex d-body C, define s(C) as the maximum volume of a d-simplex
contained in C. This maximum is positive and attained: simplex volume is a
continuous function on the compact space of d+1 vertex tuples in C, and C
contains at least one nondegenerate simplex.

Let A,B,C be full-dimensional convex bodies in R^d with

    (A+C)/2 subset B,
    s(C)>=2^(d-1)|B|.                                 (4)

Fix an attaining simplex Q subset C. For every p in A, the simplex
Delta_p=(p+Q)/2 lies in B and has volume s(C)/2^d>=|B|/2.
The preceding theorem puts g_B in every Delta_p. Thus

    2g_B-A subset Q subset C.                         (5)

This is an exact set inclusion, with no smallness assumption on A, no
centroid alignment assumption, and no restriction to facet directions.

Put the three bodies in actual fibers at bases p,w,z with p+z=2w. A closed
ambient halfspace through (w,g_B) has paired thresholds whose sum is twice
the middle threshold. Reflection (5), which preserves d-volume, implies
that the union of its A cap and its reflected C cap covers A. Its actual
endpoint contribution is therefore at least |A|. The own middle cap has
volume at least gamma_d |B| by ordinary Grunbaum. Pure integer normals
include the whole middle and at least one whole endpoint, so the same
bound holds. Containing halfspaces reduce to through-point halfspaces.

More generally, for disjoint actual reflected pairs A_i,C_i about one
middle B, if every C_i satisfies (4), then the single actual
point (w,g_B) has raw mixed depth at least

    gamma_d |B| + sum_i |A_i|.                        (6)

Every fiber is counted once. This improves the sufficient partner-volume
threshold 2^d(1-gamma_d)|B| of the shape-free complementary-cap theorem
when simplex partners are available; in d=1 the two thresholds coincide.
For nonsimplex partners, (4) concerns their maximum inscribed simplex
volumes, not their full volumes. These quantities must not be identified.

If B belongs to a core of L positive fibers, all positive outside fibers
are exactly the A_i, and all their distinct partners C_i belong to that
core, let M be the largest core volume and E=sum_i |A_i|. The two actual
points supplied by the largest-core centroid and (6) have respective
guarantees gamma_d M and at least gamma_d(|B|+E). Since

    W <= (L-1)M+|B|+E <=L max(M,|B|+E),

one of them has depth at least gamma_d W/L. For a complete parity core
L=2^n, this is the sharp OC fraction on the stated simplex-partner class.

The ordinary lemma uses no mixed-dimensional approximation. The mixed
conclusions here use full d-dimensional fibers; intrinsic degeneracy is
not silently included. For d=0 the ordinary simplex-section argument is
not used.

## Extension to polytope facet moments

The one-sided moment comparison proved above also gives the following extension.

Let P be a full-dimensional compact convex polytope in R^d, d>=1. Choose
one affine defining function lambda_i for each facet, so that

    P = intersection_i {x : lambda_i(x)>=0},
    F_i = P intersect {lambda_i=0},
    grad lambda_i !=0.

Write a=|P|, and define the coarea facet density and inward first moment by

    S_i = H_(d-1)(F_i)/|grad lambda_i|,
    M_i = integral_P lambda_i(x) dx.

For d=1 use H_0({point})=1. All S_i and M_i are strictly positive. Set

    eta(P) = min_i sqrt((d+1) S_i M_i/d)/a.             (P1)

Multiplying an individual lambda_i by any positive scalar c multiplies
S_i by 1/c and M_i by c, so (P1) is independent of these choices.
It is invariant under invertible affine maps of the continuous space:
if P'=L P+v, J=|det L|, and lambda'_i(Lx+v)=lambda_i(x), then the coarea
identity gives S'_i=J S_i, while M'_i=J M_i and |P'|=J a. In particular,
eta((p+P)/2)=eta(P). No mixed-integer lattice transformation is used here.

## Containment criterion

If B is a convex d-body containing P and

    |B| <= |P| [1+eta(P)],                             (P2)

then its ordinary centroid g_B belongs to P. If the inequality is strict,
then g_B is in the interior of P.

Indeed, fix a facet function lambda_i. The nonnegative-lambda portion of
B has first moment at least M_i. The negative portion has volume m_i at
most |B|-a. If m_i>0, its section at lambda_i=0 has coarea density at least
S_i, because it contains F_i. The proved one-sided moment comparison,
applied to t=-lambda_i, therefore gives

    |B| lambda_i(g_B)
       >= M_i - d m_i^2/[(d+1) S_i]
       >= M_i - d (|B|-a)^2/[(d+1) S_i].               (P3)

If m_i=0, the negative moment is zero and the same inequality follows
directly. By (P1)-(P2), the final expression in (P3) is nonnegative for
every i, proving g_B in P. Under strict (P2) every expression is positive.

Applying the same one-sided moment lemma directly to P and its coordinate
lambda_i gives

    M_i <= d a^2/[(d+1) S_i].

Consequently

    0 < eta(P) <=1.                                   (P4)

For a simplex, take barycentric facet functions. Then S_i=d a and
M_i=a/(d+1), so eta(P)=1 and (P2) is the half-volume simplex criterion.

## Parallelotopes and sharpness of their ordinary threshold

For P=[0,1]^d, every coordinate facet has S_i=1 and M_i=1/2. Therefore,
by affine invariance, every full-dimensional parallelotope satisfies

    eta(P)=sqrt((d+1)/(2d)).                            (P5)

The corresponding ordinary containment threshold

    |B|/|P| <= 1+sqrt((d+1)/(2d))                      (P6)

is sharp for parallelotopes. To check this explicitly for the unit cube,
let L>0, put

    v_L=(-L,1/2,...,1/2),
    B_L=conv([0,1]^d union {v_L}).

For d=1 interpret v_L=-L. The part with x_1>=0 is exactly the cube, and
the part with x_1<=0 is the pyramid with apex v_L and base
{0} times [0,1]^(d-1). To verify the union description, the intersection
with x_1=0 of a segment from v_L to a cube point has each other coordinate
between 0 and 1; all its nonnegative-x_1 points are then in the cube.
The converse inclusion follows by convexity. The two pieces overlap only
on a zero-volume common facet. The pyramid has volume L/d and mean
x_1=-L/(d+1). Thus

    |B_L|=1+L/d,
    integral_(B_L) x_1 dx = 1/2-L^2/[d(d+1)].          (P7)

For L=sqrt(d(d+1)/2), the centroid is on x_1=0 and the volume ratio is
exactly (P6). For every larger L its first coordinate is negative, so the
centroid is outside the cube. Reflection symmetry in the other coordinate
midplanes also gives (g_(B_L))_j=1/2 for j>=2. This proves sharpness of
(P6). It does not assert sharpness of any mixed-integer depth threshold.

## Actual polytope-partner reflection

Let A,B,C be full-dimensional convex d-bodies with C a polytope and
(A+C)/2 subset B. If

    |C| >= 2^d |B|/[1+eta(C)],                        (P8)

then

    2 g_B-A subset C.                                (P9)

For every p in A, the polytope P_p=(p+C)/2 is contained in B, has volume
2^(-d)|C|, and has eta(P_p)=eta(C). Condition (P8) is exactly (P2) for
P_p subset B, so g_B in P_p. This is equivalent to 2g_B-p in C, proving
(P9) for every p.

In actual fibers at bases z_-,w,z_+ with z_-+z_+=2w, (P9) pays at least
|A| from the endpoint pair in every closed ambient halfspace through
(w,g_B), by the reflection (z_-,p) -> (z_+,2g_B-p). At least one point of
each such reflected pair lies in the halfspace. The map is injective and
volume preserving, so this is a genuine volume lower bound. The own
middle fiber supplies gamma_d |B|. The argument includes oblique and
pure integer normals. Distinct pairs can be summed with the same
no-double-counting requirement as in the simplex-partner theorem.

For parallelotope partners, (P8) becomes the explicit condition

    |C| >= 2^d |B|/[1+sqrt((d+1)/(2d))].               (P10)

Its coefficient is strictly below 2^d(1-gamma_d) for d>=2, and equal to
it for d=1. Here is an exact comparison. Put r_d=sqrt((d+1)/(2d)); the
strict inequality is equivalent to

    r_d > gamma_d/(1-gamma_d).

The function x -> (x/(x+1))^x decreases for positive real x, since the
derivative of its logarithm is log(1-1/(x+1))+1/(x+1)<0. For d=2 the
comparison reduces, after squaring positive quantities, to 3/4>16/25.
For d=3 it reduces to 2/3>729/1369. For d>=4,

    gamma_d/(1-gamma_d) <=256/369 <1/sqrt(2) <r_d,

where the strict rational comparison is 2*256^2=131072<136161=369^2.
For d=1 both original coefficients are one. Thus (P10) is a strictly
stronger sufficient partner-volume criterion than the shape-free
complementary-cap threshold on this particular shape class.

There is no claim that eta is bounded away from zero for arbitrary
polytopes, or that an arbitrary convex partner satisfies (P8). Smooth
partners are not assigned a fictitious positive facet density.
