# A strict half-mass score certificate for planar two-vertex-cap fans

Research theorem, 6 November 2026. This proves a direct two-cap certificate for every full positive three-fan at an arbitrary interior point of a triangle, when every row has exactly two strictly positive original vertex values. No center or source deformation is used.

## 1. Statement

Let B be a triangle of area vV with V>0 and 0<v<=1. Let y be an interior point with barycentric coordinates h_1,h_2,h_3>0 and sum h_i=1. Let f_1,f_2,f_3 vanish at y, have gradients spanning the plane, and satisfy a strictly positive linear dependence. Assume every row has two strictly positive original vertex values and one strictly negative value. Each original vertex must have a negative row entry by positive dependence. Thus the three negative entries occupy different vertices; relabel so f_i is negative at vertex v_i and positive at both other vertices.

Let triangle sources P_m subset B have areas at least V/4 and nonnegative weights e_m summing to E=1-v. A row is hit when its support maximum on P_m is strictly positive; a maximum of zero is a miss. Put

    c_i=|B intersect {f_i>=0}|/|B|,
    S_i=v c_i+sum_m e_m 1{max_(P_m)f_i>0}.

Then

    max_i S_i>1/2.                                           (1)

More precisely, there are two distinct rows whose own-cap fractions sum to more than1 and which jointly hit every qualifying source. Boundary contacts of sources are included in the strict-support convention. The strict sign and interior-center hypotheses remain explicit.

## 2. Complementary vertex caps and a universal upper bound

Define g_i=-f_i, scaled by a positive constant so that g_i(v_i)=1. Its two other vertex values are -a,-b, with a,b>0. Let p_i be its positive vertex-cap area fraction. Since a proper line has zero area,

    c_i=1-p_i,
    p_i=1/[(1+a)(1+b)].                                    (2)

The zero-at-y condition is h_i=a h_j+b h_k. If M=max(h_j,h_k), then a+b>=h_i/M, and ab>0. Consequently

    (1+a)(1+b)>1+h_i/M,
    p_i<M/(h_i+M).                                        (3)

In particular, for any two indices j,k whose coordinates are the largest two, with remaining coordinate h_i<=h_j<=h_k,

    p_j<h_k/(h_j+h_k),
    p_k<h_j/(h_j+h_k),
    c_j+c_k>1.                                           (4)

All inequalities are strict because every off-diagonal vertex value is strictly negative in the complementary vertex-cap fan.

## 3. Exact singleton geometry

A source that hits only row i is contained in

    R_i=B intersect {f_j<=0,f_k<=0}
       =B intersect {g_j>=0,g_k>=0}.

The region R_i is a triangle with apex y and its base on the original edge v_j v_k. Indeed g_k is strictly negative on edge v_i v_j and g_j is strictly negative on edge v_i v_k. Their two lines meet at y, and their positive sides overlap on edge v_j v_k. The latter overlap is nonempty because g_j(v_j)>0,g_k(v_k)>0 and the positive dependence of the three g rows makes their closed negative intersection only y. Equivalently, the edge ratios computed below have sum greater than1, by their center equations. Thus these two edge crossings and y exhaust the intersection vertices.

Let u_jk be the edge ratio of the vertex-j cap along the edge from v_j toward v_k, and let u_kj be the corresponding ratio from v_k toward v_j. Both lie strictly between0 and1. The base overlap has fraction u_jk+u_kj-1 of the original edge, so the exact area ratio is

    r_i=|R_i|/|B|=h_i(u_jk+u_kj-1).                         (5)

For a direct check of positivity, if g_j(v_k)=-a and g_k(v_j)=-b after normalizing their positive heights to1, the center equations imply a<h_j/h_k and b<h_k/h_j. Thus ab<1 and

    u_jk+u_kj-1=1/(1+a)+1/(1+b)-1
                    =(1-ab)/[(1+a)(1+b)]>0.

Since R_i is itself a triangle, a qualifying singleton-i source exists if and only if r_i>=1/(4v). Every full-area triangle in R_i strictly hits row i: positive dependence makes g_i<0 away from the common center whenever g_j,g_k>=0. Thus this condition realizes the entire strict hit pattern, including support-boundary equality.

For the argument below it is enough to call i potentially qualifying when

    r_i>=1/4.                                             (6)

Every actual qualifying singleton satisfies(6), since v<=1.

## 4. Two potentially qualifying singleton indices leave the smallest coordinate out

Suppose r_i>=1/4 and r_j>=1/4, and let k be the third index. Normalize g_k to have value1 at v_k and values -a,-b at v_i,v_j. Then

    h_k=a h_i+b h_j.

In(5), the edge-overlap fraction for R_i is strictly smaller than the full g_k cap edge ratio1/(1+b), because the other ratio u_jk is strictly below1. Similarly the R_j overlap is strictly smaller than1/(1+a). Therefore

    1/4<=r_i<h_i/(1+b),
    1/4<=r_j<h_j/(1+a),

which implies b<4h_i-1 and a<4h_j-1. Substitution gives

    h_k< h_i(4h_j-1)+h_j(4h_i-1),
    1<8h_i h_j.                                          (7)

This forces h_k<min(h_i,h_j). For example, if h_k>=h_i, then h_j<=1-2h_i and

    h_i h_j<=h_i(1-2h_i)<=1/8,

where the last bound follows from h(1-2h)=1/8-2(h-1/4)^2. This contradicts(7). Interchanging i,j proves the other strict comparison.

In particular, an index of smallest barycentric coordinate cannot be potentially qualifying together with any other index. If it is potentially qualifying, it is the unique such index.

## 5. A pair of large own caps covering every qualifying source

Choose i with smallest barycentric coordinate, and choose k with largest coordinate; let j be the remaining index. Ties may be resolved arbitrarily.

If r_i<1/4, then no qualifying source can hit only row i. No positive-area source misses all three rows, since the common closed negative region of a full positive fan is only y. Hence every qualifying source hits at least one of rows j,k. These are the largest two barycentric coordinates, so their own-cap fractions satisfy c_j+c_k>1 by(4).

It remains to treat r_i>=1/4. By Section4 this is the unique potentially qualifying singleton index. Every qualifying source therefore hits at least one of any pair containing i. We show that rows i,k have own-cap sum greater than1.

Set h=h_i, L=h_j, M=h_k, so h<=L<=M and h+L+M=1. Equation(5) and both edge ratios being less than1 give

    h>1/4,
    t:=u_kj>1/(4h).                                      (8)

The first inequality follows from r_i<h; the second follows from h(u_jk+t-1)>=1/4 and u_jk<1. Since L<=(1-h)/2 and 4h(1-h)<=1,

    t>1/(4h)>=1-h>=2L.                                  (9)

Write the vertex values of g_k as1 at v_k, -a at v_i, and -b at v_j. Thus M=a h+b L and t=1/(1+b). Solving for its other edge ratio gives

    1+a=(t-L)/(h t),
    p_k=1/[(1+a)(1+b)]=h t^2/(t-L).                       (10)

The function phi(t)=h t^2/(t-L) has derivative

    phi'(t)=h t(t-2L)/(t-L)^2.

It is strictly increasing for t>2L. By(9), t<1, and positivity of all denominators,

    p_k<phi(1)=h/(1-L)=h/(h+M).                           (11)

By(3), p_i<M/(h+M). Adding this to(11) gives p_i+p_k<1, or equivalently

    c_i+c_k>1.                                           (12)

This pair contains the unique potentially qualifying singleton index, so it jointly hits every qualifying source. The two cases prove the precise pair assertion following(1).

## 6. Weighted score and scope

For the pair a,b obtained above, each qualifying source contributes at least1 to its two hit indicators. Thus

    S_a+S_b>=v(c_a+c_b)+E>v+E=1,

because v>0. At least one score is strictly greater than1/2, proving(1). This also includes E=0 and v=1; no source weights need be positive for the argument.

The proof uses actual simultaneous source geometry and the exact area threshold. It does not assign compatible patterns from unrelated one-cut optima. It handles arbitrary interior centers, arbitrary positive balancing coefficients, and arbitrary qualifying source weights within the all-two-positive-vertex sign pattern. Mixed one-/two-positive row patterns, zero original vertex heights, boundary centers and higher dimensions are outside the present statement. No global OC conclusion is asserted.
