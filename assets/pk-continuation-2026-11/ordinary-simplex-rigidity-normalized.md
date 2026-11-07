# Continuous minimal maximal depth forces a simplex

This is an ordinary continuous theorem and compact stability statement.
It does not resolve the mixed-integer problem. Its external geometric
input is precisely the CLASSICAL equality case in Grünbaum's theorem,
not any mixed-integer inequality or an assumed extremal classification.

For a full-dimensional compact convex K in R^d, d>=1, let mu_K be
normalized volume and define

    D(K)=max_y inf_(u in S^(d-1)) mu_K{X:u.(X-y)>=0}.

The maximum can equivalently be taken over y in K. Write
Gamma=(d/(d+1))^d. Then

    D(K)=Gamma  if and only if K is a simplex.                (1)

For fixed R>=1 and epsilon>0, among bodies B_2^d subset K subset R B_2^d
whose Hausdorff distance from EVERY simplex with vertices in R B_2^d is
at least epsilon, there is a uniform positive gap

    D(K)>=Gamma+eta(d,R,epsilon)>Gamma,                       (2)

provided this class is nonempty. The gap is attained by compactness;
no explicit rate or uniformity in d is claimed.

This atomic normalization preserves the mathematical content of pending intake `e2c55c91458e1e8c`; it is not a newly discovered theorem. The full proof is retained so it can serve as a reviewed ordinary dependency.

## 1. The standard equality input and its precise orientation

Classical Grünbaum states that every centroid cap has fraction >=Gamma.
For d>=2, equality means K is a pyramid conv(v,F), with F in a
hyperplane parallel to the cut and the equality cap on the apex side.
The affine height lambda, zero on F and one at v, has centroid value
1/(d+1). In dimension one K is already an interval, hence a simplex.

The ordinary equality statement is recorded, for example, in the
introduction of [Tanganelli Castrillón, An improved stability result for
Grünbaum's inequality](https://arxiv.org/html/2410.12072v2), equations
(1.1) and the paragraph immediately following. The proof below uses only
that classical equality characterization, not the paper's stability
theorem. Everything passing from single-cap equality to (1)--(2) is
proved here.

The height mean can also be checked directly: sections of a pyramid
at height t have volume proportional to (1-t)^(d-1), 0<=t<=1, whose
normalized mean is 1/(d+1).

## 2. Equality-cap normals balance at a minimal-depth body

Let g be the centroid, suppose D(K)=Gamma, and let

    U={u in S^(d-1):mu_K{u.(X-g)>=0}=Gamma}.

The cap-mass function is continuous in u by dominated convergence,
because a full-dimensional volume measure gives every hyperplane mass
zero. Thus U is compact. It is nonempty: the sphere is compact and
centroid depth is at least Gamma and at most D(K)=Gamma.

We claim 0 belongs to conv(U). Otherwise strict separation gives a vector
v and a constant a>0 with u.v>=a for all u in U. There is a neighborhood
N of U on the sphere where u.v>=a/2. Outside N, the centroid cap fractions
exceed Gamma by a uniform positive amount b, by compactness.

Choose r>0 with g+rB_2^d subset K and an outer ball containing K. Section
areas are uniformly bounded above by the outer ball's maximal section
area, so translating a cut by distance h changes its normalized mass
by at most L|h|, with a fixed finite L. They are uniformly bounded BELOW
by a positive c for cuts whose signed distance from g has magnitude at
most r/2, because such sections contain an appropriate section of the
inner ball. These elementary bounds follow by integrating section areas;
there is no boundary differentiability assumption.

Move the candidate point to g-tv. For t>0 sufficiently small, on N every
through-point cap gains at least c t a/2 over its centroid mass, while
outside N it loses at most Lt|v|<b/2. Also g-tv belongs to int(K).
Every through-point cap then has fraction strictly greater than Gamma,
contradicting D(K)=Gamma. This proves the claim.

Caratheodory now gives finitely many DISTINCT directions u_1,...,u_k in U,
positive weights theta_i, k<=d+1, with sum theta_i u_i=0. Zero weights
have been discarded.

## 3. Balanced pyramid heights force d+1 simplex vertices

By the standard equality case, each u_i gives a pyramid representation

    K=conv(v_i,F_i),

with affine height lambda_i zero on F_i, one at v_i, and nonnegative on K.
Its gradient is a positive multiple of u_i. Its mean is 1/(d+1).

The apex v_i is an extreme point of K. Every OTHER extreme point of K
lies in F_i: a point of a pyramid with height strictly between zero and
one lies on a nontrivial segment between its apex and its base. Distinct
u_i have distinct apex vertices. Indeed, for a fixed apex, all the other
extreme points span its full-dimensional base hyperplane, determining
that hyperplane and its oriented normal uniquely. Hence

    lambda_i(v_j)=1 if i=j, and 0 otherwise.                 (3)

Rescale the positive balancing weights to obtain positive beta_i with
sum beta_i grad(lambda_i)=0. Therefore sum beta_i lambda_i is a constant
h. Evaluating it at v_j using (3) shows beta_j=h for every j. In
particular h>0 and

    sum_(i=1)^k lambda_i=1 on all R^d.                       (4)

Integrate (4) over K. Each height has mean 1/(d+1), so

    k/(d+1)=1.

Thus k=d+1. The points v_i are affinely independent: applying the affine
functions lambda_i to any affine dependence isolates each coefficient
by (3). They form a full-dimensional simplex Q inside K. Conversely
lambda_i>=0 and (4) put K inside the simplex Q whose barycentric
coordinate functions are these lambda_i. Therefore K=Q.

For the converse, let K be a simplex with barycentric functions lambda_i.
At any y in K, some lambda_i(y)>=1/(d+1). The facet-parallel apex cap
lambda_i>=lambda_i(y) has volume fraction (1-lambda_i(y))^d<=Gamma.
Ordinary Grünbaum gives Gamma at the simplex centroid. Hence D(K)=Gamma.
This also proves the converse for d=1 and completes (1).

## 4. Existence and continuity of maximal depth

For fixed K, the cap function is jointly continuous in (u,y) on the
sphere times each compact set, again because all boundary hyperplanes
are volume-null. Taking its minimum over the compact sphere gives a
continuous depth function of y. Points outside K have depth zero by
strict separation, and points on its boundary have depth zero by a
supporting hyperplane with no volume beyond it. Thus the positive maximum
is attained inside compact K.

For any two normalized finite measures mu,nu, write
TV(mu,nu)=sup_A |mu(A)-nu(A)|. Their depth functions differ at EVERY
ambient point by at most TV, since each defining halfspace mass does.
Taking suprema over all ambient points gives

    |D(mu)-D(nu)|<=TV(mu,nu).                               (5)

If K_l converges to K in Hausdorff distance and all contain the unit
ball and lie in R B_2^d, their indicator functions converge almost
everywhere, except on the null boundary of K. Dominated convergence
gives L1 convergence of indicators and convergence of their positive
volumes. Their normalized uniform measures converge in TV. Equation
(5) therefore proves continuity of D(K) on this normalized body class.

## 5. An attained, strictly positive compact stability gap

The class of compact convex bodies between B_2^d and R B_2^d is compact
in the Hausdorff metric by Blaschke selection and preservation of the
two inclusions. Let Sigma_R consist of all convex hulls of d+1 points
in R B_2^d, allowing repeated points and lower-dimensional hulls. This
is compact, as the continuous image of (R B_2^d)^(d+1).

Distance to Sigma_R is continuous. Consequently the subclass of bodies
at Hausdorff distance at least epsilon from Sigma_R is compact. On a
nonempty such subclass the continuous function D(K)-Gamma attains its
minimum. It is strictly positive by (1), since a full-dimensional member
of Sigma_R is a simplex and no other body has D(K)=Gamma. This proves
(2). Allowing degenerate hulls in Sigma_R only strengthens the distance
condition and makes the compactness argument explicit.

All affine normalizations mentioned in this note concern ORDINARY
continuous bodies only. No unrestricted affine transformation of a
mixed-integer source is performed, and no assertion about the geometry
or depth of mixed extremizers follows from this continuous classification.
