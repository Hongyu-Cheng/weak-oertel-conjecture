# A uniform capacity-deficit extension of the one-cap descendant range

Scoped theorem, 6 November 2026. This note gives a strictly larger sufficient
range for the source-simplex hitting model. Its positive parameter is defined
by an attained ordinary compact minimization; no explicit numerical value,
global range v<=1, or mixed-integer theorem is claimed.

Fix d>=3 and put

    Gamma=(d/(d+1))^d, q=1-Gamma, beta=2^(1-d),
    rho=(q/2-1/(d+1))/2,
    c=1/(d+1)+rho=(q/2+1/(d+1))/2,
    v_cap=2^(-d)/c.                                    (1)

Here rho>0: q>=37/64>1/2>=2/(d+1). We define a number delta_d in
(0,q/2] below and prove that the source-simplex hitting conclusion holds for

    0<v<alpha'_d:=min{v_cap,beta/(q-delta_d)},            (2)

where

    alpha'_d>beta/q.                                   (3)

The score guarantee is the explicit expression in this defined parameter

    T_d(v)=[1-q(q-delta_d)v]/2>Gamma.                   (4)

The volume v is relative to V, as in the source model: B is a convex d-body
with |B|=vV; each P_i subset B is a d-simplex of volume at least 2^(-d)V;
e_i>=0 and sum e_i=1-v. The score is

    F(H)=|B intersect H|/V
          +sum_i e_i 1{P_i intersect int(H) is nonempty}.

The family is finite, and the conclusion supplies one deterministic y in B
whose score satisfies (4) for every closed halfspace containing y.

## 1. A compact ordinary capacity-deficit parameter

Let J_d be the family of convex bodies K with

    B_2^d subset K subset d B_2^d.

By the Blaschke selection theorem this is a compact family in the Hausdorff
metric; it is closed and all its members contain the unit ball. For K in
J_d and u on the unit sphere define

    H_+(K,u)={x:u dot (x-g_K)>=0},
    H_-(K,u)={x:u dot (x-g_K)<=0},
    D(K,u)=|K intersect H_+(K,u)|/|K|-Gamma,
    A(K,u)=s(K intersect H_-(K,u))/|K|,

where s(Q) is the maximum volume of a d-simplex in Q. The maximum exists
because volume is continuous on the compact space of (d+1)-tuples of
vertices in Q. The retained body has nonempty interior since the centroid
of a full-dimensional body is interior.

D is continuous on J_d times the sphere. Indeed, Hausdorff convergence of
convex bodies containing the unit ball gives almost-everywhere convergence
of indicators away from the boundary of the limiting body, hence volume
and first-moment convergence by bounded convergence. Consequently the
centroids converge. A varying centroid halfspace has indicator convergence
off its limiting hyperplane, which has d-dimensional volume zero, proving
cap-volume convergence as well.

A is upper semicontinuous. For any convergent sequence (K_j,u_j), choose
maximizing simplex vertices in the retained bodies and pass to a convergent
subsequence of their tuples in the common compact ball. The limiting
vertices lie in the limiting body and satisfy its retained halfspace
inequality. Continuity of the determinant shows that the limiting simplex
volume is at most that retained body's maximum. Dividing by the converging
positive body volumes proves the assertion. Upper semicontinuity, rather
than an unproved continuity of moving cap bodies, is sufficient here.

Thus the set

    X_d={(K,u) in J_d times S^(d-1): A(K,u)>=c}

is compact. The ordinary centroid theorem gives D>=0 everywhere. Moreover,
D=0 implies that K is a pyramid with H_+ its apex-side centroid cap. By the
proved pyramid-frustum simplex-capacity lemma,

    A(K,u)<=1/(d+1)<c.

Therefore D is strictly positive on X_d. Define

    delta_d=min{q/2, min_(X_d) D} if X_d is nonempty,
    delta_d=q/2                         if X_d is empty. (5)

The minimum in the first line is attained and strictly positive by
compactness and continuity. This proves 0<delta_d<=q/2. The definition
involves only ordinary convex bodies, their centroids, and their largest
retained simplices; no source weights or desired hitting conclusion enter
it. Positivity has been proved by the explicit equality-cap capacity
obstruction.

The two standard compact-normalization inputs are John's theorem in its
nonsymmetric form (an affine image of any d-body lies between the unit ball
and its d-fold dilation) and Blaschke selection. The single-cap equality
input is the classical ordinary pyramid equality case. The nonstandard
capacity lemma is proved in simplex-volume-in-pyramid-centroid-frustum.md.

## 2. Transfer the cap deficit to every missing-source direction

Apply John's affine normalization to an arbitrary B. Centroids, simplices,
and halfspaces transform affinely; volume ratios and the properties of
source containment and strict halfspace intersection are preserved. The
normalized cap normal is then rescaled to unit length. This is an ordinary
continuous-space normalization, not a change of integer coordinates.

If a through-g_B halfspace H misses the interior of a source P_i, then P_i
lies in its opposite retained halfspace. For v<=v_cap,

    s(B intersect H^-)/|B|>=|P_i|/|B|
        >=2^(-d)/v>=c.

The normalized pair lies in X_d. Therefore (5) yields the uniform own-cap
bound

    |B intersect H|/V >=(Gamma+delta_d)v.              (6)

If X_d is empty, no such cap and source can occur, so this implication
remains valid. Only missing-source directions use (6); no improvement over
ordinary Gamma is asserted in directions that hit every source.

## 3. Deterministic one-cap construction

Fix v satisfying (2) and T=T_d(v). The source-simplex one-cap construction
minimizes the score over unit-normal halfspaces through g_B. This minimum
exists: the own-cap term is continuous, and each strict-source indicator
is lower semicontinuous because it is the indicator of an open positive
support-function difference. If the minimum is at least T, choose y=g_B.
Otherwise choose its lexicographically least minimizing normal.

Let h be the own normalized cap volume, let I index the sources it misses,
and let m=sum_(i in I)e_i. The bad score says

    h+E-m<T,   so m>E+h-T.                            (7)

In this branch m>0. To check this without implicitly using (6), note first
that v_cap<1/2. In d=3, c=69/256 and v_cap=32/69<1/2. For d>=4,
c>q/4>=37/256 and 2^(-d)<=1/16, so v_cap<16/37<1/2.
Thus E=1-v>1/2, whereas T<1/2 because q-delta_d>0 and v>0. A cap that
misses zero total source weight has score at least E>T, a contradiction.
There is consequently a missed positive-weight source, so (6) applies.

Let Q be the opposite retained part of B. It contains every P_i indexed
by I and has normalized volume

    |Q|/V=v-h<=(q-delta_d)v<beta.

Every such P_i occupies strictly more than half the volume of Q. The
proved inscribed-simplex moment inequality puts y=g_Q in the interior of
every missed source. The body Q is full-dimensional since it contains one
such source. In every through-y halfspace J, ordinary centroid depth of Q
and all of the missed weights therefore give

    F(J)>=Gamma(v-h)+m
         >Gamma(v-h)+E+h-T
          =Gamma v+E+q h-T
         >=Gamma v+E+q(Gamma+delta_d)v-T
          =1-q(q-delta_d)v-T=T.                       (8)

This is the same deterministic construction as before, with the cap deficit
proved only where needed. Containing halfspaces reduce monotonically to
through-point halfspaces. The strict hitting definition is preserved
throughout; no boundary contact is counted as a hit.

## 4. Strict range gain and exact comparison

Since c<q/2, v_cap=2^(-d)/c>2^(1-d)/q=beta/q. Also delta_d>0 implies
beta/(q-delta_d)>beta/q. Their minimum is strictly larger, proving (3).
The difference is a definite number depending only on d, not on B, the
source shapes, their number, or their weights.

From (2), (q-delta_d)v<beta. Consequently

    T_d(v)>(1-q beta)/2>Gamma.                        (9)

For completeness the last gap is 3/512 when d=3. For d>=4,
Gamma<=27/64 and q beta<beta<=1/8, so

    (1-q beta)/2-Gamma
        >7/16-27/64=1/64>0.

Thus the gain has no hidden deterioration in its target comparison. The
nonexplicit quantity is solely the positive extension of the admissible
volume interval, whose definition and attained positivity are fully proved.

Nothing here proves that alpha'_d reaches 1; in fact alpha'_d<=v_cap<1/2.
Multiple retained cuts with only scalar weights lead back to the previously
blocked averaging loss. Any further global extension needs additional
compatibility information or a different mechanism.

# Appendix: full proof of the pyramid-frustum capacity input

# Exact simplex capacity of a pyramid centroid frustum

Scoped ordinary geometric lemma, 6 November 2026. This supports the endpoint
of the one-cap source-simplex descendant theorem and does not close its
global volume range.

Let B=conv(F union {z}) be a d-dimensional pyramid, d>=2, with a
(d-1)-dimensional convex base F and apex z outside its affine hull. Let Q
be the base-side part cut off by the hyperplane through g_B parallel to F.
Then every d-simplex P contained in Q satisfies

    |P|<=|B|/(d+1).                                    (1)

This bound is attained when F is a simplex: take P with base F and apex
any point of the top face of Q.

## 1. Simplex chord-projection identity

Let P be a d-simplex, u a unit vector, pi its orthogonal projection onto
u-perp, and L its maximum chord length parallel to u. Then

    |P|=(L/d)|pi(P)|_(d-1).                            (2)

Here is a proof including nongeneric directions. Write lambda_0,...,lambda_d
for the barycentric functions and c_i=u dot grad(lambda_i). Their sum is
zero, and they are not all zero because the barycentric gradients span
R^d. Put s=sum_(c_i>0)c_i>0.

For any segment [x,x+ell u] in P, barycentric nonnegativity at its endpoints
gives lambda_i(x)>=-ell c_i for all c_i<0. Summing gives 1>=ell s, so
ell<=1/s. Conversely choose x with barycentric coordinates
lambda_i(x)=(-c_i)_+/s. At x+u/s the barycentric coordinates are
(c_i)_+/s. Both endpoints belong to P, proving L=1/s, including when
some c_i are zero.

Let F_i be the facet opposite vertex i. Its (d-1)-area equals

    |F_i|_(d-1)=d|P||grad(lambda_i)|.

Apart from a measure-zero set of projection points, the line parallel to u
through a point of pi(P) enters P through exactly one facet on which c_i>0.
The projections of these entering facets cover pi(P) with disjoint
interiors. Each such projection has (d-1)-area

    |F_i|_(d-1) c_i/|grad(lambda_i)|=d|P|c_i.

Facets with c_i=0 have zero projected area and do not affect the identity.
Therefore |pi(P)|_(d-1)=d|P|s=d|P|/L, proving (2).

## 2. Fit the frustum in a cylinder

Apply a volume-preserving affine shear which fixes the base hyperplane and
moves the orthogonal projection of z to a point of F. Choose coordinates
with F in height 0 and z at height H>0. Pyramid sections at height t are
homothetic to F with factor 1-t/H, so integrating shows that g_B has height
H/(d+1). The base-side body Q therefore has height at most H/(d+1), and
its orthogonal projection is contained in F.

For any P subset Q, its vertical chord length is at most H/(d+1), and its
projection area is at most |F|_(d-1). Equation (2) gives

    |P|<=H|F|_(d-1)/[d(d+1)]=|B|/(d+1).

All transformations preserve the volumes in the conclusion. The argument
concerns ordinary bodies only and makes no lattice change.

## 3. Consequence for a centroid cap missing a large simplex

Suppose a centroid cap H of a convex body B has the sharp ordinary fraction
Gamma_d and misses the interior of a contained simplex P. The classical
single-cap equality case makes B a pyramid and H its apex-side cap. Thus
P lies in the base-side centroid frustum and (1) gives

    |P|<=|B|/(d+1).                                    (3)

In the source model |B|=vV and |P|>=2^(-d)V, this equality-cap obstruction
is impossible whenever v<(d+1)2^(-d). This observation alone is not a
uniform lower bound for cap fractions above Gamma_d, nor does it prove
the global source-hitting theorem in that larger range.

At the particular descendant endpoint v=beta/q, with beta=2^(1-d) and
q=1-Gamma_d, one has |P|>=q|B|/2. For d>=3,

    q>=37/64>1/2>=2/(d+1),

so q|B|/2>|B|/(d+1). Consequently a selected sharp ordinary centroid cap
cannot miss any positive-weight source. This gives a second proof that the
one-cap descendant construction is valid at that endpoint: if the original
centroid fails its target score, its selected cap must have h>Gamma_d v,
and the retained body then has volume strictly less than beta V.

The equality input used here is the ordinary pyramid characterization,
recorded on page 1 of [Marin Sola and Yepes Nicolas, On Grunbaum type inequalities](https://webs.um.es/jesus.yepes/publicaciones_files/paper_grunbaum.pdf).
