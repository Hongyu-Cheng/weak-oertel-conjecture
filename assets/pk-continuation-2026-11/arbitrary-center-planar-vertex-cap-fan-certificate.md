# A source-score certificate for every planar vertex-cap positive fan

Research theorem, 6 November 2026. This proves a direct two-cap certificate at every interior center of a triangle, for every full positive three-fan whose rows each contain precisely one original vertex on their strict positive side. No deformation of the center, fan, or source triangles is used.

## 1. Statement and conventions

Let B=conv(v_1,v_2,v_3) be a triangle of area vV, where V>0 and 0<v<=1. Let y be an interior point of B, with barycentric coordinates s_1,s_2,s_3>0 and sum s_i=1. Let f_1,f_2,f_3 be affine functions vanishing at y whose gradients span the plane and admit a dependence

    theta_1 f_1+theta_2 f_2+theta_3 f_3=0,
    theta_i>0.

Assume every row has exactly one strictly positive original vertex value and two strictly negative vertex values. Every original vertex must have some positive row value, because a positive weighted sum of three strictly negative values cannot be zero. There are exactly three positive entries overall. Relabeling the rows therefore makes

    f_i(v_i)>0,       f_i(v_j)<0 for j different from i.

Let P_m subset B be finitely many triangle sources with area at least V/4, carrying nonnegative weights e_m with sum E=1-v. A source hits row i if max_{x in P_m}f_i(x)>0. A source with maximum0 misses that row. Define normalized scores

    p_i=|B intersect {f_i>=0}|/|B|,
    S_i=v p_i+sum_m e_m 1{max_(P_m)f_i>0}.

Then

    max_i S_i >=4/9+E/18.                              (1)

In fact, choose i with maximal barycentric coordinate s_i and let j,k be the other two indices. Every qualifying source hits at least one of j,k, and

    p_j+p_k>=8/9,
    S_j+S_k>=(8/9)v+E.                                (2)

These statements include zero source weights, E=0, equal maximal coordinates, and sources touching fan boundaries. The inequalities on the original vertex signs and the interiority of y are explicit hypotheses.

## 2. The maximal-coordinate row cannot be a sole hit

Fix i with s_i>=s_j,s_k. Consider the closed region

    R_i=B intersect {f_j<=0,f_k<=0}.

In coordinates X=lambda_j,Y=lambda_k, its vertices are exactly

    O=(0,0), U=(A,0), y=(s_j,s_k), W=(0,B_0).           (3)

Here U is the zero of f_j on edge v_i v_j, and W is the zero of f_k on edge v_i v_k. To justify the list, f_j is negative on the edge v_i v_k and f_k is negative on the edge v_i v_j. Their boundary lines meet uniquely at y: two proportional rows with distinct positive original vertices could only be negatives of one another, which is impossible since both are strictly negative at the remaining original vertex. The opposite edge v_j v_k contains no common nonpositive point of f_j,f_k, because f_i is strictly negative there and positive dependence would then fail. The four listed points are therefore the complete intersection polygon.

Normalize row j to have heights a>0 at v_j, -b<0 at v_i, and -c<0 at v_k. Since it vanishes at y,

    a s_j=b s_i+c s_k>b s_i.

Consequently

    A=b/(a+b)<s_j/(s_i+s_j)<=1/2.                     (4)

The identical argument for row k gives

    0<B_0<s_k/(s_i+s_k)<=1/2.                         (5)

Also s_j,s_k<1/2, since neither exceeds s_i and all three coordinates are positive.

Every largest triangle contained in R_i may be chosen at its polygon vertices. Indeed, a maximum exists by compactness; fixing two vertices makes its absolute affine determinant convex in the third, so it has a maximizing polygon vertex. Replacing vertices successively preserves the global maximum. The four vertex-triangle area ratios to B are

    A B_0,       A s_k,       B_0 s_j,
    A s_k+B_0 s_j-A B_0.                              (6)

The first three are strictly less than1/4 by(4)-(5) and s_j,s_k<1/2. The fourth is also strictly less than1/4. For a direct bound, the bilinear function

    F(A,B_0)=A s_k+B_0 s_j-A B_0

has its maximum on the square[0,1/2]^2 at a corner, whose four values are

    0,       s_k/2,       s_j/2,
    (s_j+s_k)/2-1/4=1/4-s_i/2.

All are strictly less than1/4. Thus the exact maximal inscribed-triangle ratio of R_i is strictly less than1/4.

Every qualifying source has ratio at least V/(4|B|)=1/(4v)>=1/4. Therefore no qualifying source can be contained in R_i. In other words every source hits at least one of rows j,k, in the exact strict-support convention. This proves the source part of(2).

## 3. The two complementary own caps have total fraction at least eight ninths

Write a=s_i=max(s_1,s_2,s_3), so1/3<=a<1. For row j, normalize its positive vertex value to1 and its negative values at i,k to-b,-c, with b,c>0. The zero-at-y condition is

    b a+c s_k=s_j,
    (1+b)a+(1+c)s_k=1.                               (7)

The positive cap is a vertex triangle whose two edge ratios are1/(1+b) and1/(1+c), so

    p_j=1/[(1+b)(1+c)].                              (8)

First suppose a<=1/2. Arithmetic-geometric mean in(7) gives

    [(1+b)a][(1+c)s_k]<=1/4,
    p_j>=4a s_k.

Similarly p_k>=4a s_j. Hence

    p_j+p_k>=4a(1-a)>=8/9,                           (9)

because a lies in[1/3,1/2] and a(1-a) is increasing there.

Now suppose a>=1/2. Put X=1+b>1 and Y=1+c>1. Equation(7) gives aX+s_kY=1 and

    XY=X(1-aX)/s_k.

For X>=1, this last function has derivative(1-2aX)/s_k<=0. Thus

    XY<=(1-a)/s_k,
    p_j>=s_k/(1-a).

Similarly p_k>=s_j/(1-a), and consequently

    p_j+p_k>=1.                                     (10)

The case a=1/2 is covered consistently by both calculations. Equations(9)-(10) prove the own-cap part of(2) for every interior center; no silent assumption that all barycentric coordinates are below one half enters the argument.

## 4. Score conclusion and scope

By Section2 each source indicator contributes at least1 to the pair of rows j,k. Nonnegative weights therefore give

    S_j+S_k>=v(p_j+p_k)+E>=(8/9)v+E.

At least one of these two deterministic rows has score at least

    (4/9)v+E/2=4/9+E/18,

since E=1-v. This proves(1), including E=0.

The proof uses exact inscribed-simplex capacity at the source threshold and elementary vertex-cap optimization. It applies to unequal fan balancing coefficients, arbitrary nonuniform interior centers, unequal source volumes above the threshold, and arbitrary nonnegative source weights. It does not assume that individual source triangles can be held fixed under a fan deformation; the fan and sources never move.

This establishes a direct certificate for the entire stated vertex-cap sign cone. It does not cover rows with two positive original vertex values, zero original vertex values, boundary centers, higher-dimensional fans, or every halfspace through a single selected point. In particular it is not a proof of the full source-simplex hitting theorem or OC.
