---
fact_id: 6fbefd0eb6914aa9
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-nov6-arbitrary-cut-simplex-capacity
depends_on: []
verifier_run: b2e72bcc17554c26
target_match: null
---

## Statement

For a d-simplex T and an affine height h with a=max h(v_i)>0 and negative heights -b_j, the largest d-volume simplex in T intersect {h>=0} has volume |T| product_j a/(a+b_j), with an explicit attaining simplex. All constant, zero-height, and zero-volume cases are specified. At a centroid cut with l negative heights the sharp capacity lower bound is (l/(d+1))^l. The proof also gives exact counterexamples to a proposed volume-only capacity inequality and to iterating the surviving-original-vertex rule through multiple cuts. These are ordinary geometric statements, not an all-fan or OC conclusion.

## Proof

# Exact maximal-simplex capacity of an arbitrary halfspace cut

Research draft, 6 November 2026. This extends the grouped-height incidence determinant calculation to an arbitrary oblique halfspace cut of a simplex. It supplies an exact one-cap capacity test for the finite source-simplex hitting model. It does not assert that the resulting tests imply an all-fan inequality.

## 1. Statement and boundary conventions

Let T=conv(v_1,...,v_N) be a d-dimensional simplex, N=d+1, d>=1. Let h be an affine function, and write h_i=h(v_i). Put K=T intersect {h>=0}. For a compact convex set Q, let s(Q) be the maximal d-volume of a simplex contained in Q, with s(Q)=0 if Q has empty d-dimensional interior. All volumes in this note are ordinary d-dimensional volumes.

If max_i h_i<=0, then K either has zero d-volume or equals T: the latter case occurs precisely when all h_i=0. Thus s(K)/|T| is respectively0 or1. If every h_i>=0, then K=T and the ratio is1.

In the remaining case define

    a=max_i h_i>0,       J={j:h_j<0},       b_j=-h_j>0.

Then the exact formula is

    s(K)/|T| = product_(j in J) a/(a+b_j).                 (1)

In fact an attaining simplex has a particularly simple form: retain every original vertex with h_i>=0, choose one index i_* with h_(i_*)=a, and for each negative index j replace v_j by the intersection of [v_(i_*),v_j] with {h=0}. These are exactly N vertices counting all retained ones, and their simplex has ratio (1).

## 2. Exhaustive vertex reduction

First suppose no h_i equals zero. Let I={i:h_i>0}, k=|I|, and l=|J|, so k+l=N. Write a_i=h_i>0 for i in I. The vertices of K in barycentric coordinates are

    e_i, i in I,
    q_ij=[b_j e_i+a_i e_j]/(a_i+b_j), i in I,j in J.      (2)

Indeed, a new vertex must lie on the cutting plane. On a simplex face supported by r positive barycentric coordinates, that plane has intersection dimension r-2 when it crosses the face. A new vertex therefore has r=2, with opposite-sign endpoint heights, giving (2). Original surviving vertices are precisely the e_i listed.

A largest inscribed simplex exists by compactness of K^N and continuity of the determinant. It may be chosen with its N vertices among (2): with all but one vertex fixed, the absolute determinant is a convex function of the remaining vertex, so its maximum over K is attained at a vertex of K. Replacing vertices successively preserves the global maximum. The ratio of a candidate simplex to T is the absolute determinant of its N barycentric columns.

## 3. Weighted spanning-tree formula

Consider any N chosen columns from (2), allowing repeated columns only to observe that their determinant is zero. Multiply every row i in I by a_i and every row j in J by b_j. A pure column e_i becomes a_i e_i. A cut column becomes

    w_ij(e_i+e_j),       w_ij=a_i b_j/(a_i+b_j).

Multiply all J rows by -1. After extracting each column's positive weight, the remaining matrix is the reduced incidence matrix of a graph with vertex set {0,1,...,N}: a pure column is the root edge {0,i}, and a cut column is the edge {i,j}. The root row has been deleted. Consequently

    |det(original)|
      = product_(edges e chosen) weight(e)
          / [ product_(i in I) a_i product_(j in J) b_j ]          (3)

when the chosen N edges form a spanning tree, and it is zero otherwise. Here the root edge {0,i} has weight a_i and the edge {i,j} has weight w_ij.

For completeness, a cycle yields a signed dependence among incidence columns. An acyclic graph on N+1 vertices with N edges is connected, hence a tree. A nonroot leaf row has exactly one entry equal to1 or-1; expansion removes that leaf and edge, and induction proves absolute determinant1. This proves (3) without an unproved matrix-integrality input.

All graph weights are strictly positive. A maximum-product spanning tree exists because the graph is finite and connected. Every such maximizing tree contains every root edge {0,i}, i in I. If the root edge at i is absent, its addition creates a unique cycle consisting of that edge and the former tree path from i to0. The first edge on that path is some {i,j}, whose weight

    w_ij=a_i b_j/(a_i+b_j)<a_i

is strictly less than the added root-edge weight. Removing that first edge leaves a spanning tree with strictly greater product, a contradiction.

Once all k root edges are present, exactly l other edges remain. Every negative vertex j needs an incident edge. Thus each such vertex has exactly one, and it is attached to a positive vertex. The product is maximized independently for each j. Since a_i b_j/(a_i+b_j) increases strictly with a_i, every j can be attached to any i_* maximizing a_i. Substitution into (3) cancels all a_i and b_j factors except

    product_(j in J) a/(a+b_j).

This proves (1) and the stated attaining simplex when all heights are nonzero.

## 4. Zero-height vertices

If a>0 but some h_i=0, define h^epsilon=h+epsilon for epsilon>0. For all sufficiently small epsilon its positive vertices are the original positive and zero-height vertices, and its negative vertices are the original negative ones. Set K_epsilon=T intersect {h^epsilon>=0}. These compact sets decrease to K as epsilon decreases to0. Moreover s(K_epsilon) decreases to s(K): the lower bound follows from K subset K_epsilon, while maximizing N-tuples along any epsilon_m down to0 have a convergent subsequence whose limiting vertices lie in every K_epsilon and hence in K. Their determinant limits give the reverse bound. Formula(1) for K_epsilon therefore passes exactly to the limit:

    product_(j in J) (a+epsilon)/[(a+epsilon)+(b_j-epsilon)]
       ->product_(j in J) a/(a+b_j).

The explicit attaining simplex stated in Section1 has this determinant as well: use all nonnegative original vertices and the cut-edge intersections from a maximum-height vertex to each negative vertex. Those N columns form a block-triangular barycentric matrix whose negative-coordinate diagonal entries are a/(a+b_j). Thus the attainment description needs no limiting selected vertices.

## 5. Sharp uniform capacity among cuts through the simplex centroid

Suppose h is nonconstant and h(g_T)=0, where g_T is the centroid of T. Then sum_i h_i=0, so at least one height is positive and at least one is negative. Let l be the number of negative heights, 1<=l<=d, and let k=N-l count all nonnegative heights, including zeros. Normalize a=max h_i=1. Then

    sum_(j in J) b_j =sum_(h_i>0) h_i <=k.

Arithmetic-geometric mean and (1) give

    s(K)/|T|=1/product_(j in J)(1+b_j)
       >=[l/(l+sum_j b_j)]^l >=(l/N)^l.                 (4)

For each l this lower bound is attained: take every one of the k positive heights equal to1 and every one of the l negative heights equal to-k/l. Their sum is0 and formula(1) gives exactly(l/N)^l. Hence the sharp uniform lower bound over all centroid cuts is

    min_(1<=l<=d) (l/(d+1))^l.                          (5)

This is an exact finite minimum, not an asymptotic claim. It is often much smaller than the ordinary centroid cap-volume constant Gamma_d. In particular it recovers every grouped centroid-cut capacity, including the d5 half-volume cut with capacity1/8, but also identifies the sharp capacity across all oblique centroid cuts.

## 6. Exact one-cap test in the simplex-source hitting model

Let B be a d-simplex with |B|=vV, where v,V>0. A source simplex must be contained in B and have volume at least2^-d V. For a nonconstant affine f and a chosen point y, put

    h_i=f(y)-f(v_i),
    a=max_i h_i,
    J={j:f(v_j)>f(y)},       b_j=f(v_j)-f(y).

The source fails to strictly hit the oriented halfspace {f>=f(y)} exactly when its maximum f-value is at most f(y), that is, when it lies in the closed opposite part K=B intersect {f<=f(y)}. There EXISTS a qualifying source simplex with this failure pattern if and only if

    v product_(j in J) a/(a+b_j) >=2^-d,               (6)

when a>0, with the degenerate whole/zero cases treated in Section1. Necessity follows from(1); sufficiency follows from its explicit attaining simplex. At equality, its vertices on the cutting plane have no strict hit, so the weak inequality in(6) is exact and boundary-sensitive.

This test treats one oriented cut. It does not assert that choices attaining the separate tests for several cuts can be realized by one common source simplex, and it does not assert a global center or arbitrary-positive-fan depth bound. The exact maximizer and the tree-exchange proof provide a possible deformation mechanism without assuming those unresolved compatibility conclusions.

## 7. A smaller-dimensional centroid-cut counterexample to the proposed volume-only inequality

The proposed bound s(K)/|T|>=1-(1-|K|/|T|)^(1/d) already fails in d=4. Take three vertex heights equal to1 and two equal to-3/2. Their sum is0, so the cut passes through the true centroid. Equivalently, the sum of the first three barycentric coordinates is at least3/5. The exact capacity is(2/5)^2=4/25. The grouped beta-tail integral, or direct polynomial integration, gives

    |K|/|T|=(2/5)^4+4(3/5)(2/5)^3+6(3/5)^2(2/5)^2
             =328/625.

The claimed inequality is equivalent to(1-4/25)^4<=1-328/625, whereas

    (21/25)^4-297/625=8856/390625>0.

This is a strict rational certificate at a true centroid cut. The general capacity formula in Sections1–4 proves extremality of4/25.

## 8. Exact obstruction to iterating the surviving-vertex deformation over two cuts

The one-cut proof retains every surviving original simplex vertex. That property fails for two cuts, even when the joint intersection can contain a qualifying source in dimension4.

In the plane let

    x=(11/20,11/20),
    u=(119/20,-121/20),
    v=(-121/20,119/20),
    T_2=conv{x,u,v}.

The line segment from x to u crosses the horizontal axis at(1,0); the segment from x to v crosses the vertical axis at(0,1). The remaining edge lies on X+Y=-1/10. Consequently

    K_2=T_2 intersect {X>=0,Y>=0}
       =conv{(0,0),(1,0),x,(0,1)}.

The point(0,0) lies in the interior of T_2. In particular the two cuts pass through a common interior point of the original simplex, while x is its sole surviving original vertex.

The four possible vertex triangles in K_2 have areas

    1/2, 11/40, 11/40, 1/20.

The same vertexwise determinant maximization as above proves that its maximal inscribed triangle is conv{(0,0),(1,0),(0,1)}, uniquely among vertex triangles, and has area1/2. Every triangle using x and two other polytope vertices has strictly smaller area. In fact no maximum triangle can contain x as one of its vertices: fix that vertex and maximize the other two successively over K_2; their attained maximum is only11/40. Thus the original surviving vertex is excluded from every maximizing triangle.

The vectors u-x and v-x are12 times the corresponding vectors from x to(1,0) and(0,1). Since the latter triangle has area1/20, |T_2|=144/20=36/5. Therefore

    s(K_2)/|T_2|=5/72.                                (7)

Now form a d-simplex B as the join of T_2 with d-2 additional affinely independent vertices in complementary affine directions, for any d>=3. Extend X,Y affinely by assigning value0 to every added vertex. Then

    K=B intersect {X>=0,Y>=0}

is the join of K_2 with the same added vertices. To see this, decompose a point of B into its total weight theta on T_2 and the remaining added-vertex weights. When theta>0 its X,Y signs are exactly those of its normalized T_2 component; theta=0 gives the added face, already in the join.

Every full-dimensional vertex simplex in K must contain every added vertex: each added barycentric coordinate is zero at all other vertices, so omitting that vertex would force the determinant to vanish. The remaining three vertices come from K_2. Thus vertexwise determinant maximization and the common join-volume factor give

    s(K)/|B|=5/72,

and no maximizing simplex contains the original vertex x. The two cutting planes still pass through a common point in int(B): take a strictly positive convex combination of(0,0) in int(T_2) with all added vertices.

In d=4, 5/72>1/16. Thus if |B|=V, this joint opposite region does contain a source simplex of volume at least2^-4 V. However NO qualifying source can retain x: because x is an extreme point of K, any contained simplex that contains x must have x as a vertex. With x fixed, maximize the other vertices over K; every added join vertex must again be present for a nonzero determinant, and the planar bound is only11/40. Its ratio is therefore at most(11/40)/(36/5)=11/288<1/16. Thus retaining the surviving original vertex can destroy even the source-volume qualification, not merely optimality. This is not a bad-fan or OC counterexample. It rules out the specific deformation rule that would apply the one-cut surviving-vertex conclusion successively to several missing-source constraints; the exact one-cut formula does not carry that conclusion over to their intersection.
