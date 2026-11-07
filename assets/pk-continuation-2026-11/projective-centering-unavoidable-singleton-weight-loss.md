# Projective centering must lose source qualification on an all-bad planar fan

Research draft, 6 November 2026. This is a conditional obstruction to one proposed proof transformation, not a construction of an all-bad fan. It shows that if an all-bad fan existed in the stated vertex-cap sign class, a projective map to the centroid preserving every hit pattern would necessarily destroy source qualification on more than one ninth of the total source weight. Increasing the middle volume to any allowed ratio at most1 cannot repair that loss.

## 1. Model and precise conclusion

Let B be a triangle of area vV, 0<v<=1. Fix an interior point y with positive barycentric coordinates s=(s_1,s_2,s_3). Let F be a rank2 matrix whose rows are the vertex values of three affine functions vanishing at y, so F s=0. Suppose F has a strictly positive left kernel and every row has exactly one strictly positive entry and two strictly negative entries. These rows define a full positive fan through y, each positive cap containing exactly one original vertex.

Let P_m subset B be finitely many source triangles of areas at least V/4, with weights e_m>=0 summing to E=1-v. A source hits row i when it contains a point of strictly positive row value; a zero support value is a miss. Put

    p_i=|B intersect {F_i lambda>=0}|/|B|,
    S_i=v p_i+sum_m e_m 1{P_m strictly hits row i}.

Assume, solely for the following obstruction,

    S_i<4/9,       i=1,2,3.                          (1)

Then E>0. Under the projective map taking y to the uniform centroid while fixing the three original vertices, sources of total weight greater than E/9 become triangles of ratio strictly less than1/4 to B. Their exact original hit patterns are preserved. Consequently no subsequent global scaling that makes the middle area v'V with v'<=1 can make those image sources qualify for area at least V/4.

Thus a proof using this map in the all-bad branch must change source hit patterns, delete or replace a definite amount of source weight, or supply another compensating construction. Pattern preservation together with middle-volume compensation alone cannot be the required invariant.

## 2. Two largest caps and the forced singleton weight

We use the accepted planar positive-fan sector inequality in fact2a8c2bc6d7992c5e. For any planar convex body of area A and a positive3-fan through an interior point, write s_i for its singleton sector areas and D_i for their opposite double-covered sectors. Then

    A=sum_i(s_i+D_i),
    c_j+c_k=A+D_i-s_i,
    sum_i D_i/s_i>=3/2,                             (2)

where c_i are cap areas, all six sector areas are positive, and boundary lines have area zero. Only this accepted ordinary auxiliary inequality is used.

For completeness, (2) implies that the two largest cap areas sum to at least8A/9. Otherwise every pair sum is below8A/9, so x_i=s_i-D_i>A/9. Write D=sum_i D_i. The area identity gives D<A/3. Since t/(t+A/9) is increasing and concave for t>=0,

    sum_i D_i/s_i
      <sum_i D_i/(D_i+A/9)
      <=3D/(D+A/3)<3/2,

contradicting(2). Therefore there is a pair i,j such that

    p_i+p_j>=8/9.                                  (3)

Let k be the remaining row, and let m_k be the total source weight whose sources hit ONLY row k. No positive-area source can miss all three rows: positive dependence and rank2 make their three closed negative halfplanes intersect only at y. Every source except those counted by m_k therefore hits at least one of i,j. Hence

    S_i+S_j>=v(p_i+p_j)+E-m_k.

Combining(1) and(3) yields

    m_k>v(p_i+p_j)+E-8/9>=E/9.                      (4)

In particular E cannot be zero, because m_k<=E. This is a positive-weight obstruction forced by the hypothetical bad inequalities, not merely the possible existence of an unused singleton pattern.

## 3. Exact projective map, source determinant, and preserved signs

Let D=diag(1/s_1,1/s_2,1/s_3), and for barycentric columns lambda define

    Phi(lambda)=D lambda/(1^T D lambda).

All denominators are positive on B. The map fixes each original vertex, maps B bijectively onto itself, and sends s to g=(1/3,1/3,1/3). Its inverse uses D^(-1) in the same formula.

It maps every source triangle exactly to the convex hull of its three image vertices. Indeed, for a convex combination lambda=sum_l alpha_l a_l,

    Phi(lambda)=sum_l [alpha_l(1^T D a_l)/(1^T D lambda)] Phi(a_l),

with nonnegative coefficients summing to1; the inverse gives the reverse convex-hull inclusion. Let A_m be the3 by3 barycentric vertex matrix of P_m and let d=(1/s_1,1/s_2,1/s_3). Its image matrix and area ratio are exactly

    A'_m=D A_m diag((d^T A_(m,1))^(-1),
                    (d^T A_(m,2))^(-1),
                    (d^T A_(m,3))^(-1)),

    |Phi(P_m)|/|B|
       =det(D)|det(A_m)|/product_l(d^T A_(m,l)).       (5)

The transformed fan matrix is F'=F D^(-1). Its rows vanish at g, retain the same strictly positive left kernel and rank2, and keep the same vertex sign patterns. Moreover

    F lambda=[1^T D lambda] F' Phi(lambda),

so every strict hit and every support-boundary miss is preserved exactly. Multiplying by the positive scalar denominator does not convert equality into a hit.

## 4. The centroid vertex-cap sign cone has no qualifying singleton source

Here is the exact geometric capacity argument, included to avoid assuming a global fan theorem. After permuting rows, the unique positive entries of F' lie on the diagonal: every column must contain a positive entry under a positive left dependence, and there are exactly three such entries.

For any two rows, their common closed negative region in barycentric coordinates(X,Y,1-X-Y) is a quadrilateral

    (0,0), (alpha,0), (1/3,1/3), (0,beta),

where0<alpha,beta<1/2. Each row is negative on the edge joining its two negative vertices, its zero edge intercept from the surviving third vertex is below1/2 because its positive height is the sum of its two negative magnitudes, and the two lines meet at g. Positive dependence excludes points on the opposite original edge, proving the exhaustive vertex list.

The four vertex-triangle ratios to B are

    alpha/3, beta/3, alpha beta,
    (alpha+beta)/3-alpha beta.

The first two are less than1/6, the third is less than1/4, and the last is at most1/6 by maximizing that bilinear function on[0,1/2]^2. The largest inscribed triangle can be chosen at polygon vertices by successive maximization of the absolute affine determinant. Thus every triangle missing those two rows has ratio strictly less than1/4.

Every source counted in m_k still misses rows i,j after Phi. Its image therefore has ratio below1/4. Combining this with(4) proves that more than E/9 of source weight is attached to such image triangles. If a later global scaling gives B area v'V with v'<=1, each such image triangle still has area

    less than (1/4)v'V<=V/4,

so qualification cannot be restored. This remains true at v'=1 even though a separately chosen reweighting might choose to delete all source weight; deletion is a change to the weighted source data, not preservation of the source triangles' qualification.

The argument makes no assertion that data satisfying(1) exist. It establishes the precise incompatibility of the proposed pattern-preserving projective-center step with any such data in this sign class, and supplies the explicit lost-weight lower boundE/9.
