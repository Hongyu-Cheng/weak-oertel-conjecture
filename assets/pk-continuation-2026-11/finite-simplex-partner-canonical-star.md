# A finite reflected star with simplex partners: all canonical directions and arbitrary integer tilts

Research draft, 6 November 2026. This is an actual finite-fiber theorem, not an atomic endpoint limit. It constructs one deterministic point of the middle fiber and controls the specified continuous directions with arbitrary integer-coordinate components. For d>=2 it does not control all continuous normal directions and therefore does not resolve OC.

## 1. Precise data and conclusions

Fix integers n>=1 and d>=1. Let w in Z^n. Let u_i,v_i in Z^n be finitely many bases with

    u_i+v_i=2w.

Assume all bases in the list w,u_1,v_1,...,u_m,v_m are distinct. At these bases place d-dimensional convex bodies B,A_i,C_i respectively. Suppose B and every C_i are d-simplices, while A_i may be arbitrary d-dimensional convex bodies, and suppose

    (A_i+C_i)/2 subset B.                           (1)

Let |.| denote d-dimensional Lebesgue volume. Fix V>0 and write

    |B|=vV,     a_i=|A_i|,     c_i=|C_i|,
    0<v<=1,    c_i>=V,
    sum_i a_i=(1-v)V=:EV,
    a_i/c_i<=eta:=2^(-64).                          (2)

The empty family is allowed when v=1. Define the actual finite union

    S_* = ({w} x B) union union_i [({u_i} x A_i) union ({v_i} x C_i)].

Its measure is the sum of the d-volumes on these distinct integer fibers. Let lambda_1,...,lambda_N, N=d+1, be the barycentric affine functions of B, and set Gamma=(d/(d+1))^d.

For d>=2 there is one deterministic y_* in B such that every closed ambient halfspace containing (w,y_*) whose continuous normal is either zero or a positive multiple of one of grad(lambda_j) contains at least

    [Gamma+E/400]V                                  (3)

of S_* when E>0. When E=0 the guaranteed mass is Gamma V.

For d=1, there is one deterministic y_* in B such that EVERY closed ambient halfspace containing (w,y_*) contains at least V/2 of S_*.

A set induced by an actual convex body may have additional fibers. If it contains the displayed fibers with their stated volumes and compatibility, these lower bounds continue to hold for the indicated halfspaces. The statement does not compare V automatically with the total mixed-integer mass of that larger set.

## 2. An elementary cap homothety

Let K be any full-dimensional convex body, and let ell be a nonconstant affine function. Put m=min_K ell, r=max_K ell. For a threshold t with m<=t<=r, a maximum point z of ell exists by compactness. Convexity gives

    z+[(r-t)/(r-m)](K-z) subset K intersect {ell>=t}.

Consequently

    |K intersect {ell>=t}| >= |K|[(r-t)/(r-m)]^d.     (4)

For t<m the whole body is included; for t>r the cap is empty. No smoothness or exposed-point uniqueness is required.

## 3. Pair credit from good midpoint supports

Choose a parameter alpha with

    0<alpha<1,      alpha^d c_i>=a_i for every i.    (5)

For p in A_i put P_(i,p)=(p+C_i)/2. It is a d-simplex contained in B by (1), of volume c_i/2^d>=2^(-d)V. Define

    r_ij(p)=max_(x in P_(i,p))lambda_j(x),
    G_ij(t)={p in A_i:(1-alpha)r_ij(p)>t}.

Fix y in B and an ambient closed halfspace H through (w,y) whose continuous normal is grad(lambda_j). Its traces on the two endpoint fibers have thresholds t_A,t_C in the same affine function lambda_j, with

    (t_A+t_C)/2=lambda_j(y)=:t.                     (6)

This follows from u_i+v_i=2w, regardless of the integer-coordinate part of the ambient normal.

The actual mass of the two endpoint fibers in H is at least

    |G_ij(t)|.                                     (7)

Indeed, if all of G_ij(t) lies in the A_i trace, the A_i contribution alone proves (7). Otherwise choose p in G_ij(t) outside that closed trace, so lambda_j(p)<t_A. By (6),

    t_C<2t-lambda_j(p).

Under the affine map x -> (p+x)/2, the C_i trace therefore contains the inverse image of the P_(i,p) cap {lambda_j>=t}. Write r=r_ij(p) and m=min_(P_(i,p))lambda_j. Both are nonnegative because P_(i,p) subset B, and r>0 by full dimensionality. If t<m the full C_i is included. Otherwise (4) and m>=0 give

    |C_i intersect H_trace|
       >=c_i[(r-t)/(r-m)]^d
       >=c_i[(r-t)/r]^d
       >c_i alpha^d>=a_i>=|G_ij(t)|.

This proves (7) for every integer tilt. Source support equality is excluded by the strict definition of G_ij; the halfspaces themselves are closed. Any halfspace containing (w,y) may be shrunk by moving its boundary parallel to itself through that point, so the same lower estimate applies to containing halfspaces.

Distinct endpoint bases are essential here. They permit us to sum (7) without counting one physical fiber more than once.

## 4. Determinant budgets for each source point

Assume for now that y is interior to B, put u_j=lambda_j(y), and define

    L_j=log_+((1-alpha)/u_j),       S=sum_j L_j.

Here log_+(x)=max(0,log x). For any p in A_i, let M be the N by N barycentric vertex matrix of P_(i,p) in B. It is nonnegative and column-stochastic. Writing r_j for its row maxima,

    |det M|=c_i/(2^d vV)>=2^(-d)/v,
    0<r_j<=1.                                     (8)

Call row j good if r_j>u_j/(1-alpha), exactly the condition p in G_ij(u_j).

The first determinant budget is valid without assuming any good row exists. Let I be the bad rows with L_j>0. Hadamard, entrywise nonnegativity and AM-GM give

    |det M|^2<=product_j sum_l M_jl^2
       <=product_j r_j sum_l M_jl
       <=product_j r_j
       <=product_(j in I)r_j
       <=product_(j in I)[u_j/(1-alpha)].

Thus

    sum_(j bad)L_j<=A_1:=2d log2+2log v.             (9)

Rows with L_j=0 contribute nothing to the left. Every source exists with nonzero determinant, so the bound also shows A_1>=0 whenever E>0.

There is an improved second budget when alpha<1/3. If every row were bad, P_(i,p) would be contained in

    {x in aff(B):lambda_j(x)<=u_j/(1-alpha) for all j}.

This is an inverted simplex with homothety factor alpha/(1-alpha), since the nonnegative deficiencies sum to alpha/(1-alpha). Its volume is

    [alpha/(1-alpha)]^d vV<2^(-d)V,

contrary to the volume of P_(i,p). Therefore a good row h exists. It necessarily has L_h>0.

Replace row h of M by the all-ones row, the sum of the rows, without changing the determinant. Subtract r_j/2 times this row from the other rows. Hadamard yields

    |det M|<=N^(N/2)2^(-d) product_(j!=h)r_j.

Because every bad positive-weight row remains in the product, (8) implies

    sum_(j bad)L_j<=A_2:=(N/2)log N+log v.           (10)

In (10), one can discard every other factor at most 1, exactly as in (9). In every case where this budget applies, A_2>=0 follows from the nonnegative missed logarithmic sum.

For either applicable budget A, each source point therefore satisfies

    sum_(j good)L_j>=S-A.                           (11)

Integrating (11) over p in A_i is legitimate: r_ij(p) is affine in p, as follows directly from affine midpoint preservation and the fixed support of C_i. The good sets are measurable.

## 5. The all-point actual-fan estimate

Define the continuous scalar score functions on [0,1]

    F_j(t)=v(1-t)^d+(1/V)sum_i |G_ij(t)|.             (12)

For any y and any ambient halfspace in the positive continuous direction grad(lambda_j) through (w,y), (7) gives the actual lower bound V F_j(lambda_j(y)).

The sequences L_j and (1-u_j)^d are ordered in the same direction. Chebyshev and Jensen give

    sum_j L_j(1-u_j)^d>=Gamma S.

Integrate (11) over all A_i, divide by V, and use sum_i a_i/V=E. It follows that

    sum_j L_j F_j(u_j)>=v Gamma S+E(S-A).

Whenever S>0,

    max_j F_j(u_j)>=Gamma+E[(1-Gamma)-A/S].          (13)

A lower bound for S follows because log_+(x)>=log x:

    S>=N log[N(1-alpha)].                           (14)

If a barycentric coordinate is zero, its own cap contains all B, and every p has r_ij(p)>0. Hence F_j(0)=v+E=1. Boundary points therefore cause no missing case in the maximum estimates below.

## 6. One absolute per-fiber threshold works for every d>=2

Set alpha=eta^(1/d)=2^(-64/d). We prove

    max_j F_j(lambda_j(y))>=Gamma+E/200             (15)

for every y in B and every d>=2 when E>0.

First suppose 2<=d<=9. Then alpha<1/64<1/3, so the second budget applies. By log(1+t)<t for t>0 and log N>=log3>1,

    log[N(1-alpha)]
       >log N-1/63 >=(62/63)log N.

As v<=1, A_2<=(N/2)log N, hence (14) gives

    A_2/S<63/124.

Also Gamma<=Gamma_2=4/9. Thus the correction in (13) is strictly greater than

    5/9-63/124=53/1116>1/200.                       (16)

Now suppose d>=10, and use only the first budget. Write L=64log2>2 and

    g(x)=(x+1)(1-exp(-L/x)),       x>0.

With t=L/x, differentiation gives

    g'(x)=1-exp(-t)[1+t+t^2/L]>0,

because exp(t)>1+t+t^2/2 and L>2. Therefore

    N(1-alpha)=g(d)>=g(10)
       >11(1-1/64)=693/64>2^(10/3).

The last inequality is exact: 693^3=332812557>268435456=2^28. From (14) and A_1<=2dlog2,

    A_1/S < (2dlog2)/[N(10/3)log2] <3/5.

The sequence Gamma_d decreases, and

    Gamma_d<=Gamma_7=(7/8)^7<79/200,

as 200*823543=164708600<165675008=79*2097152. Consequently the correction in (13) is strictly greater than

    1-79/200-3/5=1/200.                             (17)

This proves (15) at interior points in every d>=2. At a boundary point a score is 1, and Gamma+E/200<=1/2+1/200<1, so it also holds there. The elementary monotonicity of Gamma_d follows by differentiating x log(x/(x+1)); its derivative is -log(1+1/x)+1/(x+1)<0.

## 7. One deterministic point for every canonical direction and integer tilt

For E>0 and d>=2 put T=Gamma+E/400. Each F_j in (12) is continuous and strictly decreasing on [0,1]. To see continuity of the good-set term, r_ij(p) is a nonconstant affine function of p, with gradient grad(lambda_j)/2. Its level hyperplanes have zero d-volume inside the full-dimensional A_i; dominated convergence therefore proves continuity of |G_ij(t)|. Strict decrease of the own term v(1-t)^d makes the total strictly decreasing. The endpoint values are F_j(0)=1 and F_j(1)=0.

There is therefore a unique a_j in (0,1) with F_j(a_j)=T. We claim A=sum_j a_j>1. If A<=1, choose barycentric coordinates u_j>=a_j summing to 1. They give F_j(u_j)<=T for all j, contradicting (15), whose right side exceeds T. Define

    lambda_j(y_*)=a_j/A.

These coordinates determine one point y_* in B, and each is strictly less than a_j. Thus F_j(lambda_j(y_*))>T for every j. Section 3 proves (3) for all the stated continuous orientations and every possible integer tilt, at this same deterministic point.

For a pure integer normal, a containing halfspace includes the whole middle fiber. For each reflected pair it also includes at least one whole endpoint fiber: their signed base values average to the middle value. Since c_i>=a_i, its total mass is at least

    |B|+sum_i min(a_i,c_i)=vV+EV=V,

which is stronger than (3).

If E=0, take the centroid of B. Its canonical own caps all have mass Gamma V. The pure-integer case has mass V. No endpoint determinant or parameter alpha is needed.

## 8. The one-dimensional case

Let d=1 and E>0. Here Gamma=1/2, each C_i is automatically an interval, and every nonzero continuous normal is a positive multiple of one of the two barycentric gradients. Set

    alpha=min(eta,E)>0.

For every i,

    a_i/c_i<=eta,
    a_i/c_i<=a_i/V<=E,

so (5) holds. Also alpha<1/3. Because P_(i,p) has length c_i/2>=V/2 and lies in B, we have v>=1/2, making A_2=log(2v)>=0. Equations (10), (13), and (14) apply, and

    S>=2log[2(1-alpha)]>=2log(2v)=2A_2,

since alpha<=E=1-v. Thus A_2/S<=1/2, and (13) gives max_j F_j(lambda_j(y))>=1/2 for every y. Here S>0 because alpha<=eta<1/2.

Use T=1/2 in the continuous threshold construction of Section 7. If the two threshold coordinates a_1+a_2 were less than 1, both could be increased to sum 1, producing both scores strictly below 1/2, a contradiction. Hence A=a_1+a_2>=1. The point with coordinates a_j/A has both scores at least 1/2. The pair-credit argument covers every nonzero continuous normal, with arbitrary integer tilt, and the pure-integer argument gives V. This proves the stated full ambient halfspace conclusion V/2 for this specific reflected-star configuration. If E=0, the midpoint of B gives it directly.

## 9. Exact scope

This theorem uses an actual single deterministic middle-fiber point, actual finite endpoint bodies, Lebesgue volume on each distinct fiber, closed ambient halfspaces, and arbitrary integer-coordinate components of the normal. No midpoint atom approximation, common centroid alignment, equal-volume partners, or smallness assumption on total E is used.

Its structural hypotheses remain strong: a simplex middle, simplex large partners, a reflected star with disjoint physical endpoints, and the exact mass normalization in (2). In d>=2 the allowed nonzero continuous normals comprise N positive orientations only. No assertion is made for their arbitrary oblique perturbations or for the missing continuous orientations, and no sharp OC total-mass comparison is implicit.
