# Exact simplex capacities of grouped barycentric cuts

Scoped obstruction, 6 November 2026. The proposed inequality

    s(T intersect H)/|T|
      >=1-(1-|T intersect H|/|T|)^(1/d)                 (X)

for every simplex T and halfspace H is false. Here s denotes the maximum
volume of an inscribed d-simplex. We prove the exact capacity of a family
of cuts and give rational counterexamples, including a cut through the
true simplex centroid. This does not contradict OC or the separate exact
capacity calculation for facet-parallel pyramid frusta.

## 1. Exact capacity theorem

Let T be a d-simplex with N=d+1 barycentric coordinates lambda_1,...,lambda_N.
Choose a nonempty proper subset I of size k and put J=I^c, l=N-k.
For 0<t<1 define

    K={x in T:sum_(i in I)lambda_i(x)>=t}.

Then

    s(K)/|T|=(1-t)^l,                                 (1)
    |K|/|T|=sum_(r=0)^(k-1) binom(d,r)t^r(1-t)^(d-r).  (2)

### Proof of (1)

Work in barycentric coordinates. The vertices of K are the original
vertices e_i for i in I and the cut-edge vertices

    v_ij=t e_i+(1-t)e_j, i in I, j in J.

To justify this exhaustive list, an original simplex vertex survives
exactly when its index belongs to I. Any new vertex lies on the cutting
plane and has at most two positive barycentric coordinates, since the
intersection of that plane with the simplex face supporting a vertex must
be zero-dimensional. A two-coordinate support must have one index in
each group and then has the displayed coefficients.

A maximal-volume inscribed simplex can be chosen with all vertices among
these vertices of K. Indeed, its volume is the absolute value of a
determinant, affine in each vertex separately. Maximizing one vertex over
a polytope attains its maximum at an extreme point, and replacing its
vertices one at a time preserves a global maximum. The volume ratio of
such a simplex to T is the absolute determinant of the N by N matrix of
its barycentric vertex columns.

Choose N columns and let p be the number of pure columns e_i. If a column
is repeated the determinant is zero; otherwise p<=k. Factor t from each
I row and (1-t) from each J row, and then factor 1/t from each pure column.
The remaining columns are e_i for a pure column and e_i+e_j for a cut
column. Multiplying the J rows by -1 makes them e_i and e_i-e_j. Therefore

    |det(original)|=t^(k-p)(1-t)^l |det(M)|,             (3)

where M is a reduced oriented incidence matrix of a graph on N+1 vertices:
the N coordinate vertices plus an extra root 0. A pure column is an edge
from the root to i; a cut column is an edge from j to i. The root row has
been deleted.

For completeness, det(M) is 0 or plus or minus 1 by an elementary graph
argument. If the N edges contain a cycle, their signed cycle columns are
linearly dependent, so the determinant is zero. If there is no cycle,
the graph on N+1 vertices with N edges is a tree. Choose a leaf other
than the root; its row has exactly one nonzero entry, equal to 1 or -1.
Expanding the determinant along that row removes the leaf and its edge.
Induction ends with determinant 1 in dimension zero, proving absolute
value 1 for the original tree. This includes nongeneric or repeated-edge
choices by the cycle/dependence case, with no total-unimodularity theorem
left unproved.

Equation (3) and p<=k show that every candidate volume ratio is at most
(1-t)^l. Equality is attained by taking all k pure vertices and, for each
j in J, the cut vertex t e_(i0)+(1-t)e_j for one fixed i0 in I. The
resulting determinant is triangular after its pure columns are used,
with absolute value (1-t)^l. This proves (1).

### Proof of (2)

The sum S=sum_(i in I)lambda_i of a uniformly chosen simplex point has
density

    d!/[(k-1)!(l-1)!] s^(k-1)(1-s)^(l-1), 0<s<1.

This follows by grouping the two barycentric blocks: at a fixed sum s,
their simplex coordinates scale by s and 1-s in dimensions k-1 and l-1.
The resulting product section density has those powers; its normalizing
constant is the displayed factorial ratio, obtained by the elementary
beta integral (or by repeated integration of monomials). Thus the retained
fraction is the integral of this density from t to 1. Differentiating the
polynomial on the right of (2) telescopes to the negative of that density,
and its value at t=0 is 1. This verifies (2), including k=1 or l=1.

## 2. Five-dimensional counterexample through the true centroid

Set d=5, N=6, k=l=3 and t=1/2. Since the centroid has all barycentric
coordinates 1/6, the cutting hyperplane passes through it. Equations
(1)--(2) give

    |K|/|T|=1/2,       s(K)/|T|=1/8.

Inequality (X) would require 1/8>=1-2^(-1/5), or equivalently
(7/8)^5<=1/2. Instead the exact gap is

    (7/8)^5-1/2=423/32768>0.

Thus (X) fails even for a centroid cut of a simplex, with no degeneracy or
approximation.

More generally, let d=2m-1, k=l=m, t=1/2 and m>=3. The cut still passes
through the centroid, the retained fraction is 1/2, and the capacity is
2^(-m). The claimed bound fails for every such odd d>=5. For m=3 use the
calculation above. For m>=4, Bernoulli's inequality gives

    (1-2^(-m))^(2m-1)>=1-(2m-1)2^(-m)>=9/16>1/2,

because (2m-1)/2^m decreases for m>=4 and equals 7/16 at m=4.

## 3. A retained-volume example larger than the ordinary q_7 fraction

Set d=7, N=8, k=l=4, t=2/5. Equations (1)--(2) give

    |K|/|T|=11097/15625,
    s(K)/|T|=81/625.

With Gamma_7=(7/8)^7=823543/2097152 and q_7=1-Gamma_7,

    |K|/|T|-q_7=3371955119/32768000000>0.

Nevertheless the proposed capacity bound still fails, with exact equivalent
gap

    (1-81/625)^7-(1-11097/15625)
      =3303536184833555664/37252902984619140625>0.

This particular cut is not through the ordinary centroid: its grouped
coordinate has threshold 2/5 while the centroid value is 1/2. Its purpose
is to show that retaining more than the numerical fraction q_7 does not
by itself rescue (X). The five-dimensional counterexample already
addresses true centroid cuts.

The capacity in (1) may remain sufficient for other source-volume
thresholds; no broader impossibility follows without checking those
thresholds. What is excluded here is precisely (X) and any proof step
that invokes it unconditionally.
