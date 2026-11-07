# Exact inscribed-triangle capacity core

This is an ordinary planar geometric support lemma. It asserts no unrestricted
mixed-integer or all-direction hitting theorem.

## 1. Statement

Let T be a nondegenerate triangle, of area A>0, and let x be an interior point
with barycentric coordinates lambda_0,lambda_1,lambda_2>0. Write

    m=min_i lambda_i,  M=max_i lambda_i,
    r(x)=M/(M+m).

Then the maximum area of a triangle P contained in T and with x NOT in the
interior of P is exactly r(x)A. The maximum exists and can be realized by a
triangle P having x on one of its edges and two vertices among the vertices
of T. Consequently, for q in (1/2,1], the intersection of all triangles P contained in T with
|P|>=qA is exactly the closed set

    K_q(T)={x in T: max_i lambda_i(x) / min_i lambda_i(x)
                         <=q/(1-q)}                     (1)

when q<1; for q=1 put K_1(T)=T. For q in (1/2,1), the ratio in (1) is defined
only at interior points, and (1) is a compact convex hexagon. Every point
satisfying the strict inequality belongs to int(P). The assertion for the
closed boundary of K_q is containment, not necessarily interior containment.

Equivalently, K_q is cut out by all six linear inequalities

    (1-q) lambda_i <=q lambda_j,   i!=j.

It has vertices, in barycentric notation, obtained by permuting the two
vectors

    (q,q,1-q)/(1+q),
    (q,1-q,1-q)/(2-q).                              (2)

At q=1/2 the limiting set is the centroid. Every inscribed triangle of area
at least A/2 contains that centroid, and area strictly greater than A/2 puts
it in the interior.

## 2. Reduction to a cap and vertices

Affine changes of coordinates preserve all relative areas and barycentric
coordinates, so work in the standard triangle with vertices v_0,v_1,v_2.
If x is not in the interior of P, a separating/supporting line through x
puts P into a closed halfplane H. To see this also when x lies outside P,
first strictly separate x from compact convex P; move that line parallel
toward x until it passes through x, retaining P on the same closed side.
If x is on the boundary of P, use a supporting line there. Degenerate P
has area zero and needs no separate separation argument for the area bound.

The cap Q=T intersect H is a compact polygon with at most four vertices.
Its maximum-area inscribed triangle has vertices among those of Q. Indeed,
for fixed two of a triangle's vertices, its unsigned doubled area is the
absolute value of an affine function of the third vertex. Such a convex
function has a maximizing polygon vertex: write any point as a convex
combination of polygon vertices and use the triangle inequality. Replace
successively all three vertices, never decreasing area. A finite maximum
exists among these triples, so this procedure proves the assertion without
an assumption that the original triangle is extremal.

Write H={f<=0}, where f is affine and f(x)=0. Since x is interior and f is
nonconstant, there are both positive and negative values among f(v_i).
A zero vertex value can be included in either of the following weak cases;
all the formulas persist by continuity. We give the nonzero cases first.

## 3. A cap retaining one original vertex

Relabel so f(v_0)<0<f(v_1),f(v_2), and divide f by -f(v_0). Write its vertex
values as (-1,b,c), b,c>0. The condition f(x)=0 says

    b lambda_1+c lambda_2=lambda_0.                 (3)

The cap is the triangle with vertex v_0 and the intersections of f=0
with the two adjacent edges. Their edge fractions from v_0 are
1/(1+b) and 1/(1+c), so its relative area is

    1/[(1+b)(1+c)].                                 (4)

On the closed interval b in [0,lambda_0/lambda_1], put
c=(lambda_0-b lambda_1)/lambda_2. The product (1+b)(1+c) is concave
in b: its quadratic coefficient is -lambda_1/lambda_2<0. A concave
function on an interval attains its minimum at an endpoint. Thus (4)
is no greater than

    max{lambda_1/(lambda_0+lambda_1),
        lambda_2/(lambda_0+lambda_2)} <= r(x).       (5)

## 4. A cap retaining two original vertices

Relabel so f(v_0)=-b, f(v_1)=-c, f(v_2)=a, with a,b,c>0. Then

    a lambda_2=b lambda_0+c lambda_1.               (6)

The cap quadrilateral has vertices v_0,v_1,p,q, where p lies on v_0v_2
at height t=b/(a+b) from v_0, and q lies on v_1v_2 at height
u=c/(a+c) from v_1. Its four candidate triangle areas, in units A, are

    t, u, t(1-u), u(1-t).

This follows either by direct determinants in the standard triangle or by
using the v_0v_1 base and multiplying the two relevant edge fractions.
Since 0<t,u<1, their maximum is max(t,u). Equation (6) gives

    a>=b lambda_0/lambda_2,
    a>=c lambda_1/lambda_2,

hence

    t<=lambda_2/(lambda_0+lambda_2)<=r(x),
    u<=lambda_2/(lambda_1+lambda_2)<=r(x).           (7)

Equations (5) and (7) prove the upper bound. If a vertex value is zero,
approximate f among affine functions vanishing at x by nondegenerate such
functions, or read (3)-(7) with a zero parameter. The polygon areas are
continuous in the line and the same weak inequalities hold.

## 5. Equality and the core

Choose indices i,j with lambda_i=M and lambda_j=m, and let k be the third
index. Choose affine f with vertex values

    f(v_i)=1, f(v_j)=-M/m, f(v_k)=0.

Then f(x)=M-(M/m)m=0. The cap {f<=0} is a triangle with original vertices
v_j,v_k and a third vertex on v_iv_j. Its relative area is

    (M/m)/(1+M/m)=M/(M+m)=r(x).

The point x lies on the cut edge, proving attainment and sharpness.

If r(x)<q and |P|>=qA, the area bound proves x in int(P).
For q in (1/2,1), the set with r(x)<q is the relative interior of the
polygon in (1), because it is given by the six strict linear inequalities
and contains the centroid. Every point of K_q is a limit of such points:
move it along the segment toward the centroid. Since P is closed, the
whole K_q is contained in P. Formula (2) follows by making two independent
ratio inequalities equalities. To verify completeness, order the three
coordinates; the only possible nontrivial vertices have either both
largest coordinates equal or both smallest coordinates equal. Otherwise
only one of the six bounding inequalities is active, so the point is not
a vertex in the two-dimensional barycentric plane. The two displayed
families are exactly those two possibilities.

Conversely, for an interior x outside K_q one has r(x)>q. Take the
maximizing triangle P_0 from Section 5 and an interior point p of P_0.
For sufficiently small e>0, the homothetic triangle
P_e=(1-e)P_0+e{p} remains in T, has area (1-e)^2 r(x)A>qA,
and strictly excludes x because x lay on a supporting edge of P_0.
Thus x is absent from some member of the family. If x is on the boundary
of T, the triangles (1-e)T+e{g_T}, with e>0 small, have area >qA and
exclude x. This proves the asserted exact intersection description.

For q=1, an inscribed compact triangle of area A must equal T. Otherwise,
a point of T outside P has a neighborhood whose intersection with int(T)
has positive area outside P, contradicting equal areas. Thus K_1=T is
contained as stated.

At q=1/2, the upper bound at the centroid is r=1/2, so every inscribed
triangle of area >A/2 contains it in its interior. Suppose an inscribed
triangle of area A/2 strictly excluded the centroid. Strict separation
puts it in a cap {f<=t_0}, with f(g_T)=t_1>t_0. For t between t_0 and t_1,
the maximal inscribed triangle area in {f<=t} strictly increases whenever
it is positive. Indeed, before the second original vertex enters the cap,
formula (4) is the product of two strictly increasing positive edge
fractions. Afterwards Section 4 shows that the capacity is the maximum
of two strictly increasing retained edge fractions. These formulas agree
at the transition; the cap never becomes all of T because t<=f(g_T)
with g_T interior. Thus its capacity at t_0 is strictly below its capacity
at t_1, which is at most A/2 by the through-centroid bound. This contradicts
the triangle of area A/2 in the first cap. Hence closed containment also
holds at q=1/2.

## 6. Use and limitation for a strict-hitting fan

Suppose a fan's own cap B_j=B intersect H_j is itself a triangle and a
source triangle P is contained in the singleton region for label j.
If |B_j|=c_j V and |P|>=V/4, then P occupies at least q_j=1/(4c_j) of B_j.
When 1/4<=c_j<1/2, q_j>1/2, so every such source contains the same explicit
hexagon K_{q_j}(B_j), and that hexagon lies in the closed complements of
all other fan caps. If c_j=1/4, equal area forces P=B_j. If c_j<1/4, no
such source exists. This is a necessary geometric constraint and a common
source core. It does not alone establish the unresolved all-fan inequality.

## 7. Exact limitation of the common-core substitution

The common core is a necessary condition for a large source triangle in a
singleton region, but it cannot replace the source triangle's actual
capacity, even together with all own-cap budgets. Here is a certificate.

Let B be a triangle with area vV, v=19/20. Put t=sqrt(2/5), choose y with
B-barycentric coordinates

    (1-t,t/2,t/2),

and use the canonical positive fan H_j={lambda_j>=lambda_j(y)}. Write the
own cap masses in units V as c_j. Then

    c_1=(19/20)t^2=19/50,
    c_2=c_3=(19/20)(1-t/2)^2
             =209/200-(19/20)sqrt(2/5).             (8)

Both c_2 and c_3 are strictly less than 4/9. This is equivalent to
sqrt(2/5)>1081/1710; both sides are positive, and their squared difference
is exactly 1079/2924100>0. Also c_1<4/9.

The first own cap B_1=B intersect H_1 is a triangle. Relative to B_1, the
other two barycentric coordinates are lambda_2/t and lambda_3/t. A point
is outside the open second and third caps exactly when these coordinates
are each at most 1/2. A source of area V/4 would occupy fraction

    q=(1/4)/c_1=25/38

of B_1. The common core K_q(B_1) has every relative barycentric coordinate
at most q/(2-q)=25/51<1/2, by (2). Thus this ENTIRE exact common core lies
in the strict complements of both other caps, as required of a putative
singleton1 source.

Nevertheless the singleton region has maximum triangle area only

    (19/20)*(t/2)^2 V=19V/200<V/4.                  (9)

Indeed in the two coordinates lambda_2,lambda_3 it is the full rectangle
[0,t/2]^2; its upper corner has coordinate sum t<1, so the rectangle lies
inside the barycentric domain. Its area is twice (t/2)^2 times |B|, and
the maximum inscribed triangle has half its area, by the vertex argument
of Section 2. This proves (9).

If one nevertheless admitted a source of weight E=1-v=1/20 solely from
common-core containment and assigned it the singleton1 pattern, its three
scores would be

    c_1+E=43/100<4/9,    c_2<4/9,    c_3<4/9.

This is a rigorous obstruction to replacing triangle capacity by common
core containment in the finite fan LP. It is not a counterexample to that
LP with genuine source triangles, because (9) certifies that the proposed
source cannot exist.
