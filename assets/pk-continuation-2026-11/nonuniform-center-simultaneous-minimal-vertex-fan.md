# Simultaneously minimizing vertex caps at nonuniform triangle centers

Research draft, 6 November 2026. This identifies an explicit noncanonical positive fan at every interior barycentric center with all coordinates below one half. It proves an exact source-capacity and score certificate for that fan, allowing arbitrary source weights. It does not assert that an arbitrary fan can be deformed to this one while preserving bad scores.

## 1. A simultaneous minimum-cap positive fan

Let B be a triangle and let y have barycentric coordinates s=(s_1,s_2,s_3), with

    0<s_i<1/2,       sum_i s_i=1.

For i=1,2,3 define an affine function by its vertex values

    F_ii=1,
    F_ij=1-1/(2s_j),       j!=i.                     (1)

Every off-diagonal entry is strictly negative. Direct substitution gives F s=0. The vector theta with coordinates theta_i=1-2s_i is strictly positive, sums to1, and satisfies theta^T F=0: in column j the weighted sum is

    theta_j+(1-theta_j)[1-1/(2s_j)]=0.

The rank is2. Indeed F=diag(1/(2s_i))+1 r^T, where r_j=1-1/(2s_j). An invertible diagonal matrix plus a rank-one matrix has rank at least2, and F s=0 gives rank at most2. Thus the three positive halfplanes form a full positive fan through y.

Each row independently minimizes the area of a vertex-side cap through y which contains only its own original vertex strictly. To prove this, normalize any competing row i to have positive height1 and negative heights-b,-c at j,k. Passing through y gives

    b s_j+c s_k=s_i,
    (1+b)s_j+(1+c)s_k=1.

Its cap fraction is1/[(1+b)(1+c)]. Arithmetic-geometric mean gives

    [(1+b)s_j][(1+c)s_k]<=1/4,

so that fraction is at least4s_j s_k. Equality occurs precisely at

    1+b=1/(2s_j),       1+c=1/(2s_k),

which are positive admissible negative magnitudes because s_j,s_k<1/2, and give exactly(1). Hence the fan's cap fractions are

    p_i=4s_j s_k.                                    (2)

No assertion that these are minima among cuts containing two original vertices is used.

## 2. Exact singleton source capacities

Fix i and let{j,k} be the other indices. Put alpha_i=1-2s_i>0. The region R_i which misses rows j,k is a quadrilateral. In coordinates(lambda_j,lambda_k), its four vertices are

    (0,0), (alpha_i,0), (s_j,s_k), (0,alpha_i).        (3)

The origin is the original vertex i. On edge ij, the zero of row j has lambda_j=alpha_i, and on edge ik the zero of row k has lambda_k=alpha_i. The two lines intersect at y. There is no feasible point on the opposite edge jk because row i is strictly negative there and the three rows have a positive dependence. This proves the exhaustive vertex description.

The four vertex-triangle ratios to B are respectively

    alpha_i s_j, alpha_i s_k, alpha_i^2,
    alpha_i(s_j+s_k)-alpha_i^2=alpha_i s_i.

A maximum inscribed triangle can be chosen at polygon vertices by maximizing its absolute affine determinant successively in the vertices. Therefore the exact singleton capacity is

    b_i=s(R_i)/|B|
       =alpha_i max{alpha_i,s_1,s_2,s_3}.             (4)

In particular, if s_i>1/4, then alpha_i<1/2 and every s_j<1/2, so b_i<1/4. If s_i=1/4, then b_i=1/4, attained by the corner triangle with vertices(0,0),(1/2,0),(0,1/2). If s_i<1/4, alpha_i>1/2 exceeds every s_j, and

    b_i=(1-2s_i)^2.                                 (5)

In this last case the maximum is attained by the corner triangle consisting of the surviving original vertex i and the two edge-zero points in(3). Thus any feasible singleton pattern at the source threshold below has an explicit attaining source that retains that original vertex.

At most one index can have s_i<=1/4, since otherwise the remaining coordinate would be at least1/2. Hence at most one singleton-hit pattern can be feasible for a source of ratio at least1/4. When it is feasible, its index has the smallest barycentric coordinate, and therefore the largest own-cap fraction in(2).

## 3. Source qualification and arbitrary-weight score certificate

Normalize |B|=vV with0<v<=1. Let finitely many source triangles P_m subset B have areas at least V/4, and nonnegative weights summing to E=1-v. A strict hit means a strictly positive support value; a source supported on a cutting line and its opposite side misses that row.

For E>0 such data automatically require v>=1/4. Every source has ratio at least1/(4v)>=1/4. By(4), a singleton-hit-i source is feasible exactly when

    (1-2s_i)^2>=1/(4v),       s_i<=1/4.              (6)

The necessity uses(4) and the preceding classification. For sufficiency use the explicit corner triangle in(5), including its equality cases. A positive-area source cannot miss all three rows because their closed opposite halfplanes intersect only at y. The corner triangle therefore hits row i strictly and misses the other two exactly as required.

Let s_1=max_i s_i after relabeling, so s_1>=1/3 and s_1<1/2. A source cannot hit only row1 because s_1>1/4. Hence every source hits at least one of rows2,3. The own-cap fractions in(2) satisfy

    p_2+p_3=4s_1(s_2+s_3)=4s_1(1-s_1)>=8/9,         (7)

because x(1-x) is increasing on[1/3,1/2]. Consequently their normalized scores satisfy

    S_2+S_3
      >=v(p_2+p_3)+E
      >=(8/9)v+1-v.

At least one row has score at least

    (4/9)v+(1-v)/2 =4/9+E/18.                       (8)

This includes v=1, when all source weight is zero, as well as source-volume equality and source support on a fan boundary. No equal source weights, cyclic symmetry, uniform barycentric center, or probabilistic source selection is assumed.

## 4. Exact remaining mechanism

For this family, all three own caps are simultaneously optimal within their vertex-side classes, the fan remains positively balanced, and every potentially feasible singleton credit lies on the row of largest own cap and has an explicit corner-simplex representative. These properties establish(8) for this particular oblique fan.

A possible deformation argument would have to show that arbitrary vertex-cap fan data can be replaced by this fan without increasing the maximum score or losing the necessary source-volume conditions. Neither independent row optimization nor centroid projection proves that compatibility. In particular, source triangles need not remain inside their original missed-row intersections during independent row changes. This note does not assume that missing step, does not infer a center whose every halfspace has the target score, and does not assert the full source-simplex hitting statement or OC.
