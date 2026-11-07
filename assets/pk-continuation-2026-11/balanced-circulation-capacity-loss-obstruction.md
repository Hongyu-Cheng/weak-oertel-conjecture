# A balanced circulation cannot be removed while retaining source feasibility

Research draft, 6 November 2026. This gives an exact test of a proposed matrix-normal deformation in the finite source-simplex hitting model. Removing a skew circulation decreases every affected own-cap volume, but can destroy the existence of any qualifying source with a specified missed-row pattern. It also produces a linear change in missed-source capacity for only a quadratic change in own-cap volume. No bad positive fan or counterexample to OC is asserted.

## 1. A full positive fan with both balanced kernels fixed

Fix d>=2, N=d+1, a d-simplex B, and its barycentric centroid s=(1/N,...,1/N). In barycentric vertex coordinates put

    F(t)=N I_N - 1 1^T + t C,       0<=t<1,

where C is zero outside its first three rows and columns and its first block is

       [ 0  1 -1 ]
       [-1  0  1 ]
       [ 1 -1  0 ].

Both row and column sums of C are zero. Hence

    F(t)s=0,       1^T F(t)=0.

The rows define oriented cuts through the same centroid. Their continuous gradients have rank d and positive dependence with every coefficient1. Indeed, on the subspace1^perp, for every nonzero real x,

    x^T F(t)x=N|x|^2>0,

because C is skew-symmetric. Thus the restriction is invertible and the only linear dependence among the N rows is their sum. This is an actual full positive fan, not merely a collection of scalar rows. Multiplying by diag(s) produces a matrix with both row and column sums zero, as in the balanced-matrix formulation.

At t=0 the rows are the canonical positive facet orientations. Deleting the circulation is the path t down to0, preserving the point, both kernels, full rank, and canonical one-positive-entry sign pattern.

## 2. Exact own-cap costs

For each of the first three rows, the vertex heights consist of one positive height d, two negative heights -(1-t),-(1+t), and d-2 other negative heights -1. Its positive cap is a vertex simplex. Its normalized volume is therefore

    p(t)=d^d / [(N-t)(N+t)N^(d-2)]
        =Gamma_d/[1-t^2/N^2].                         (1)

Here the elementary vertex-cap formula follows directly by intersecting each edge from the positive vertex with the cutting plane and multiplying its d edge ratios. The remaining N-3 rows are unmodified and their own-cap fractions are Gamma_d. Thus deleting the circulation decreases every affected own-cap fraction, with exact increase over the canonical value

    p(t)-Gamma_d=Gamma_d t^2/(N^2-t^2).                (2)

## 3. Exact source-capacity loss

A simplex source misses an oriented row strictly in the support sense when all its points have row value at most0; it is a robust miss if their values are all strictly negative. In the closed negative part of any affected row, the signed heights have one negative value-d and positive values1-t,1+t,1,...,1. The arbitrary-cut capacity formula gives

    kappa(t)=max{|P|/|B|:P a d-simplex, P subset B,
                            F_j(t)P<=0}
            =(1+t)/(N+t).                            (3)

This also has a direct attaining construction. Retain every original vertex except the positive vertex of F_j(t). Let v_* be the original vertex where that row is -(1+t). Replace the omitted positive vertex v_j by

    q_c=c v_j+(1-c)v_*,       0<c<=kappa(t).

The resulting simplex P_c has ratio c, and its only potentially limiting row value is

    F_j(t)(q_c)=(N+t)c-(1+t).

Consequently it is contained in the negative part at equality and robustly contained when c<kappa(t). Formula(3)'s upper bound is the arbitrary-cut tree theorem; it is not inferred merely from this construction.

At t=0 the maximum capacity is1/N. For every t>0, choose

    2^-d/kappa(t)<v<N 2^-d,

which is a nonempty interval contained in(0,1), since N 2^-d<=3/4 for d>=2. Scale B to volume vV. Then the required source ratio for volume at least2^-d V is

    c_req=2^-d/v,

and it satisfies

    1/N<c_req<kappa(t).

Choose c strictly between c_req and kappa(t). The source P_c has more than the required volume and robustly misses the affected row at parameter t. After deleting the circulation, no qualifying source anywhere in B can miss the corresponding canonical row, because its maximum possible ratio1/N is smaller than c_req. Thus allowing the source to change freely cannot repair this missed-row feasibility loss.

This rules out the proposed unconditional invariant that circulation deletion should preserve source determinant feasibility whenever it decreases all own-cap volumes. It does not rule out deformations that change the center, alter which rows a source misses, or track a compensating geometric quantity.

## 4. A fully rational planar instance

Take d=2,N=3,t=1/2,v=2/3. Then

    F(1/2)=[ 2   -1/2 -3/2 ]
           [-3/2  2   -1/2 ]
           [-1/2 -3/2  2   ],
    p(1/2)=16/35,       kappa(1/2)=3/7,
    c_req=3/8.

For row1 let P have barycentric vertices

    e_2, e_3, (2/5,0,3/5).

Its ratio to B is2/5>3/8 and its three row1 values are-1/2,-3/2,-1/10, all strictly negative. Its absolute volume is4V/15>V/4. At t=0 every source missing row1 has volume at most|B|/3=2V/9<V/4. The own-cap fraction meanwhile decreases from16/35 to4/9. All inequalities are strict, rational, and use actual simplices and genuine positive fans.

## 5. No linear capacity-loss charge by the own-cap volume change

From(3),

    kappa(t)-kappa(0)=d t/[N(N+t)].                    (4)

Dividing by(2) gives the exact ratio

    [kappa(t)-kappa(0)]/[p(t)-Gamma_d]
        =d(N-t)/(N Gamma_d t),                        (5)

which is unbounded as t decreases to0. Thus there is no finite constant depending only on d which, for all these centroid cuts, bounds the increase in maximal missed-source simplex capacity by that constant times the increase in own-cap volume above Gamma_d.

The phenomenon is geometric: a split in the two equal negative vertex heights changes the maximizing positive height of the opposite cut at first order, whereas the vertex-cap volume has its stationary minimum at the canonical orientation. Any deformation or mass-accounting argument using this circulation must retain this capacity sensitivity or a nonlinear error term. This conclusion is a scoped obstruction to a specific quantitative charge, not an obstruction to the full source-simplex hitting theorem.

## 6. Exact planar pattern capacities and a valid joint rescaling flow

In the planar cyclic family, the preceding obstruction disappears if circulation deletion may increase the middle volume and rescale the total source weight. This section proves the exact monotonicity; it does not extend it to nonsymmetric fans.

Keep d=2 and 0<=t<1. Write

    alpha(t)=(1+t)/(3+t),
    beta(t)=(1-t)/(3-t),
    p(t)=4/(9-t^2).

The largest source ratio missing any specified single row is alpha(t). The largest source ratio missing any specified two rows is

    alpha(t)/3<1/6.                                  (6)

To prove the second claim, use lambda_1=X,lambda_2=Y,lambda_3=1-X-Y and the first two rows. Their closed negative region has exactly the four vertices

    (0,0), (alpha(t),0), (1/3,1/3), (0,beta(t)).

Indeed the two inequalities are

    (3+t)X+2tY<=1+t,
    -2tX+(3-t)Y<=1-t.

They meet at the centroid. Their intersections with the coordinate axes are as displayed, and there is no common feasible point on X+Y=1 because the third row is strictly negative there while the three rows sum to zero. The four possible vertex-triangle ratios to B are

    alpha/3, beta/3, alpha beta, (alpha+beta)/3-alpha beta.

Since alpha>=1/3>=beta>=0, the largest is alpha/3. Vertexwise determinant maximization proves that this is the exact inscribed-triangle capacity. Cyclic symmetry gives the same answer for any pair of rows. All three rows can be missed only at their common point, of zero area.

Now let |B|=vV, where1/4<=v<=1, and let sources have areas at least V/4 and normalized weights summing to E=1-v. Since their ratios to B are at least1/(4v)>=1/4, equation(6) shows that EVERY source hits at least two of the three rows. The single-miss patterns are feasible precisely when

    v>=v_c(t):=1/[4alpha(t)]=(3+t)/[4(1+t)].           (7)

Necessity follows from the exact one-cap formula; sufficiency follows from its attaining source. Such a source automatically hits the other two rows because(6) forbids missing another. A source hitting all three is always feasible, by taking B itself.

Let q_j be the fraction of total source weight hitting row j, when E>0. Thus q_j lies in[0,1], and sum_j q_j>=2. Every row's own cap fraction is the same p(t), so

    max_j S_j(t,v)=v p(t)+(1-v)max_j q_j.              (8)

The exact source-pattern LP optimum, minimizing this maximum over nonnegative pattern weights summing to E, is

    L(t,v)=1-v+v p(t),                  if v<v_c(t),
    L(t,v)=(2/3)(1-v)+v p(t),           if v>=v_c(t). (9)

In the first regime every source hits all rows. In the second, sum q_j>=2 gives the lower bound, and three cyclic single-miss sources with equal weights attain q_j=2/3. Equality at the capacity threshold is valid: touching a row on its boundary still counts as a strict-support miss. At v=1 there is no source mass, and both expressions reduce to p(t).

More strongly, a joint deformation works for EVERY fixed feasible pattern-weight distribution, not merely the optimal one. Let0<=s<=t. If the distribution uses any single-miss pattern, set

    v'=max{v,v_c(s)}.

If it uses only the all-hit pattern, set v'=v. Then v'<=1 and v'>=v. At parameter s and middle volume v'V, all the original hit patterns are feasible: equation(7) ensures this for a single miss, and the all-hit pattern is always feasible. Select any qualifying source of each original pattern, and rescale all its weights by(1-v')/(1-v) when v<1. The normalized pattern fractions q_j are unchanged. The boundary case v=1 has zero source mass and needs no rescaling.

Since p(s)<=p(t)<1/2 and max q_j>=2/3, equation(8) gives

    max_j S_j(s,v')
       =v'p(s)+(1-v')max q_j
       <=v'p(t)+(1-v')max q_j
       <=v p(t)+(1-v)max q_j
       =max_j S_j(t,v).                              (10)

Thus circulation deletion together with this explicit volume/weight change preserves feasibility and never increases the maximum fan score. Individual rows with smaller q_j need not be monotone; the actual maximum is, because the own-cap fractions coincide.

For the rational example t=1/2,v=2/3, complete deletion takes v'=3/4. The optimal maximum decreases exactly from

    L(1/2,2/3)=166/315

    to L(0,3/4)=1/2.

This is a genuine valid monotonicity region for the joint deformation suggested above. It relies on the cyclic equality of own-cap fractions and the exact exclusion of singleton-hit patterns. Those two properties are proved here and are not asserted for arbitrary positive fans. In particular, it does not establish an arbitrary-fan extremal reduction.
