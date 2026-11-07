# A counterexample with 675 integer coordinates

Status: complete analytic construction and exact rational scalar checks;
independent source-level review passed. This result is not yet Lean-formalized.
It refutes the exact `1/(e 2^n)` bound, and therefore the larger sharp
`Gamma_d/2^n` bound. It does not refute every positive absolute constant.

## Theorem and mechanism

There is a full-dimensional rational polytope in

    R^675 x R^(1686+2^689)

whose nonempty integer fibers are all full-dimensional and whose induced
mixed-integer set S satisfies

    sup_(y in S) depth_S(y) < 1/(e 2^675).

Here depth uses the sum of the continuous Lebesgue volumes of the integer
fibers, equivalently normalized Euclidean Hausdorff measure in their common
dimension. Every point has a containing proper closed ambient halfspace of
insufficient mass.

Three changes make the small integer dimension possible. First, the ordered
sources live in a triangle; their chosen interior centers are almost the
triangle's center, rather than the source centroids. Second, free box
coordinates increase the source-to-middle volume ratio without imposing any
additional cut directions. Third, a common finite simplex factor supplies
caps near the constant 1/e on all exposed fibers, even though those fibers
are products rather than simplices.

The following proof includes the exact fiber census and the origin-fiber
containment; it does not assume that prescribed fibers survive convex hull.

## 1. General geometric parameters

Let B0 be the centered standard triangle, with affine barycentric coordinates
lambda_0,lambda_1,lambda_2, summing to 1 and each equal to 1/3 at the origin.
Put f_j=lambda_j-lambda_(j+1), with indices modulo 3. Each f_j is a nonzero
linear functional, their sum is zero, and each cuts exactly half the area
of B0 on its nonnegative side. The latter assertion follows by swapping
the two indicated barycentric coordinates; the separating line has zero area.

For a in {0,1,2}, put

    T_a={x in B0: lambda_(a+1)<=lambda_(a+2)<=lambda_a}.

This is the triangle with barycentric vertices

    e_a, (e_(a+2)+e_a)/2, (e_(a+1)+e_(a+2)+e_a)/3.

Its area is |B0|/6, by the determinant of these three columns. For j!=a,
max_(T_a) f_j=0; all f_j values on B0 lie in [-1,1].

Choose rational parameters satisfying

    0<epsilon<1/3,       1/2<s<1,
    0<t<eta<2(1-s),
    kappa=(1/3+epsilon)/(1/3-epsilon),
    2 kappa t <= 3-2s.                                  (1)

Choose c_a by its barycentric coordinates

    lambda_(a+1)(c_a)=1/3-epsilon,
    lambda_(a+2)(c_a)=1/3,
    lambda_a(c_a)=1/3+epsilon.

It is strictly inside T_a. On the two missed rows j!=a, f_j(c_a)=-epsilon;
on its root row, f_a(c_a)=2epsilon. Thus the missed-row center values are
the same for every source type. Define

    P_a^0=c_a+s(T_a-c_a),       A_a^0=t(T_a-c_a).

Let h be a positive integer, let F=[-1,1]^h, and choose rational 1/2<q<1.
Put u=2(1-q) and, in R^(2+h), define

    B=B0 x F,
    P_a=P_a^0 x qF,
    cbar_a=(c_a,0),
    A_a=A_a^0 x uF.

All these sets are full-dimensional rational polytopes. Both cbar_a in P_a
and 0 in A_a are interior points. Write b=|B|>0.

For any integer k>=1, the set

    K(a,k)=2P_a+(k-1)cbar_a

has the same volume M, independent of a and k. The common outer volume is
a0=|A_a|. Product measure and ordinary scaling give the exact ratios

    m=M/b=((2s)^2/6)(2q)^h,
    alpha=a0/b=(t^2/6)u^h.                              (2)

## 2. The containment for arbitrary mixtures of types

Let I be any nonempty finite set of indices assigned types tau(i), let k=|I|,
and select one index i(I) in I. Write a=tau(i(I)). We claim

    K(a,k)+sum_(i in I) A_(tau(i)) subset (k+1)B.         (3)

For the triangle coordinates, when k=1 the selected type is the only type,
and

    2P_a^0+A_a^0=(2s+t)T_a+(2-2s-t)c_a subset 2B0.

Both coefficients are nonnegative by (1), and sum to 2.

For k>=2, take p in P_a^0 and v_i in A_(tau(i))^0. For each barycentric
coordinate lambda_l, its linear part L_l satisfies

    lambda_l(p)>=(1-s)lambda_l(c_a),
    L_l(v_i)>=-t lambda_l(c_(tau(i))).

Set cmin=1/3-epsilon and cmax=1/3+epsilon. For

    y=[2p+(k-1)c_a+sum_i v_i]/(k+1),

the affine constant is correctly accounted for by 2+(k-1)=k+1, and

    (k+1)lambda_l(y)
      >=(k+1-2s)cmin-kt cmax
      >=cmin[(k+1-2s)-k(3-2s)/2]
      =cmin(k-2)(2s-1)/2 >=0.

Thus y belongs to B0. This bound allows every possible mixture of types;
the selected source need not have the same type as the other outer fibers.

For the free coordinates, the left side of (3) has factor

    2qF+kuF=(2q+ku)F subset (k+1)F,

because u=2(1-q) and

    k+1-(2q+ku)=(k-1)(2q-1)>=0.

Combining the two coordinate containments proves (3).

## 3. The actual convex body and exact integer fibers

Take a positive integer N and put n=3N. Assign N integer-coordinate indices
to each of the three types. For nonempty I subset {1,...,n}, set

    z_I=sum_(i in I)e_i,       K_I=K(tau(i(I)),|I|).

Define the base convex body C0 as the convex hull of

    {0} x B,
    {z_I} x K_I                  for every nonempty I,
    {-e_i} x A_(tau(i))          for i=1,...,n.           (4)

It is a compact rational polytope. Its affine span is the whole ambient
space: B supplies all 2+h vertical directions, and a point above each e_i
supplies the n independent projected directions. Hence it has nonempty
ambient interior.

The integer points in its projection are exactly {0,1}^n and the negative
unit vectors. Indeed, every projected coordinate lies in [-1,1]. An integer
point having coordinate -1 at i must be a convex combination entirely of
generators with that coordinate -1, and the unique such generator is -e_i.
Otherwise all its coordinates are 0 or 1.

Every nonzero cube vertex z_I is exposed among these generators by the
functional with coefficient 1 on I and -1/2 elsewhere. Its value |I| is
strictly greater than the value at any other generator. Each -e_i is exposed
by -z_i. Their fibers in C0 are therefore exactly the prescribed K_I and A_i.

To determine the fiber at 0, group any convex representation there by bases.
Let lambda_0, lambda_I, and mu_i be its respective weights on B, K_I, and A_i.
The integer-coordinate equations give

    mu_i=sum_(I containing i)lambda_I,
    lambda_0+sum_I(|I|+1)lambda_I=1.

Its continuous point can consequently be written

    lambda_0 x_0+sum_I lambda_I(x_I+sum_(i in I)v_i),

with x_0 in B, x_I in K_I, and v_i in A_(tau(i)). Repeated occurrences of
v_i use the same chosen point, which causes no problem in (3). Zero weights
may be assigned arbitrary points of the corresponding nonempty fibers.
By (3), each grouped term is (|I|+1)lambda_I times a point of B. Their weights
sum to 1, so the result lies in B. The reverse inclusion is a generator.
Thus the origin fiber is exactly B and there are no unlisted integer fibers.

Every nonempty integer fiber is full-dimensional. Its total mixed volume is

    W=(2^n-1)M+b+3N a0
      =2^n M+Delta,
    Delta=b(1+3N alpha-m).                              (5)

## 4. Three ambient cuts cover the origin fiber

Fix j in {0,1,2}. Call index i paid when tau(i)=j. Put R=3(n+1), and use
the following proper closed ambient halfspace, ignoring all free coordinates:

    H_j={(z,x,w): f_j(x)+sum_i beta_i z_i>=0},
    beta_i=-R           for paid i,
    beta_i=eta epsilon  for unpaid i.                    (6)

For an unpaid outer fiber, max f_j on A_i^0 is t epsilon; its largest
cut score is (t-eta)epsilon<0. For a paid outer fiber, its f_j values are
at least -2t because T_a and c_a lie in B0. Hence all its cut scores are
positive, since R>2t. Exactly N outer fibers are included completely.

If a nonempty cube set I contains a paid index, its continuous score is at
most k+1 and its integer score at most -R+(k-1)eta epsilon<=-R+k-1. Their
sum is negative because k<=n and R=3(n+1).

If every index in I is unpaid, its selected type is unpaid. Its largest
continuous score is exactly -(k+1-2s)epsilon. The total score is therefore

    [k eta-(k+1-2s)]epsilon
      <-(k-1)(2s-1)epsilon <=0,                         (7)

using eta<2(1-s). This is strict also for k=1. Every nonzero cube fiber is
excluded, for every type mixture.

On the origin fiber (6) cuts half of B0 and all of F. Thus its total mass is

    b/2+N a0 = b(1/2+N alpha).                          (8)

The three cuts cover the entire origin fiber since sum_j f_j=0. All omitted
fibers were strictly excluded; no boundary mass has been discarded.

## 5. Exact parameters with n=675

Choose

    epsilon=1/10000,    s=q=501/1000,
    t=997/1000,         eta=399/400,
    h=1684,            N=225,            n=675.

Then kappa=10003/9997. The conditions (1) hold by exact rational arithmetic;
in particular eta-t=2(1-s)-eta=1/2000 and
3-2s-2 kappa t>0. Formula (2) becomes

    m=(501/500)^1686/6,
    alpha=(997/1000)^2(499/500)^1684/6.

The companion checker verifies the following rational bounds by exact
integer arithmetic:

    483979/100000 < m < 24199/5000,
    113789/20000000 < alpha < 284473/50000000.            (9)

Write these four bounds as mlo,mhi,alo,ahi respectively. Direct rational
calculation gives

    1+675 alo-mhi-mhi/16384 >0,
    (32/87)mlo-1/2-225 ahi >0.                          (10)

Consequently the actual quantities satisfy

    Delta/M=(1+675 alpha-m)/m >1/16384,
    1/2+225 alpha <(32/87)m <m/e.                       (11)

For the last comparison, e<87/32 follows from its power series: the terms
through 1/4! sum to 65/24 and the remaining tail is at most
(1/120)sum_(j>=0)(1/6)^j=1/100. Thus
e<=1631/600<87/32. No decimal approximation is used in (9)-(11).

Also a0<M: in (2), t<2s and u<2q, so alpha/m<1. The base continuous
dimension is 2+h=1686.

## 6. Finite simplex padding and every possible center

Set ell=2^(n+14)=2^689, and let J be the rational standard ell-simplex,
with volume j0>0. Define

    C=C0 x J in R^675 x R^(1686+ell).

Its exact integer fibers are the fibers of C0 times J; they remain full
dimensional. The total mixed volume is W j0 by product Lebesgue measure.

For every positive integer ell, write Gamma_ell=(ell/(ell+1))^ell. The
strict inequality log(1+x)>x/(1+x) for x>0 gives

    e Gamma_ell <1+1/ell.

Indeed, set x=1/ell, multiply by ell+1, and exponentiate. From (5) and (11),

    W/(2^n M)>1+1/(16384*2^n)=1+1/ell,

so

    Gamma_ell M/W <1/(e 2^n).                           (12)

Take any actual mixed-integer point (z,x,w,v) in C. If z=0, one of the three
cuts (6), extended with zero coefficient on J, contains the point. By (8)
and (11), its mass is less than (M/e)j0<W j0/(e2^n).

If z is any other integer base, its fiber has the form K x J with |K|<=M
and z is exposed. At v in J, some barycentric coordinate is at least
1/(ell+1). Its containing vertex cap has volume at most Gamma_ell j0,
by the homothety formula (1-a)^ell at barycentric level a. This includes
vertices, where the cap has zero volume. The cap functional is nonzero.

To isolate this actual product cap, let g be a linear functional on the
integer coordinates uniquely maximized at z among the finite base set.
Write the chosen J cap as L(v')>=t, where L is nonzero and t<=L(v). Choose
a sufficiently large finite Q>0 and use

    L(v')-t+Q[g(z')-g(z)]>=0.

At z this is exactly K times the selected J cap. At every other base the
exposure gap is strictly negative. Compactness of the finitely many fibers
and J bounds L(v')-t, so one finite Q strictly excludes them all. The ambient
functional is nonzero because its J component is L. This is a containing
proper closed halfspace of mass at most M Gamma_ell j0, below the target
by (12).

Both classes of points have uniform upper bounds strictly below
1/(e2^n): respectively b(1/2+N alpha)/W and Gamma_ell M/W. Taking their
maximum proves the stated strict supremum bound. The proof uses no limiting
body, no unproved closure principle, and no restriction on legal ambient
halfspace directions.

## 7. Why the previous simplex-middle route could not do this

There is an exact geometric barrier in the earlier equal-length-three-chain
construction, with r>=2, d=3r-1, middle simplex B, source
T_a=B intersect {f_j<=0: j not in R_a}, source center c_a, and
P_a=c_a+s(T_a-c_a). Suppose an outer set A at -e_i is paired with 2P_a at
e_i, the origin fiber remains B, and each missed row has a through-origin
ambient cut strictly excluding both these fibers. Then necessarily

    A subset 2(1-s)(T_a-c_a).                            (13)

To prove this, exact origin containment forces 2P_a+A subset 2B. Every
barycentric coordinate has minimum zero on T_a (choose a vertex in another
chain, using r>=2), so for u in A its linear
part satisfies L_l(u)>=-2(1-s)lambda_l(c_a). On a missed row, existence of
an integer tilt beta excluding both fibers forces

    f_j(u)<beta<-2 max_(P_a)f_j=-2(1-s)f_j(c_a).

Thus c_a+u/[2(1-s)] belongs to B and satisfies every missed inequality;
it belongs to T_a. This proves (13), even when A is not a simplex.
Consequently source-shaped outers approaching the scale 2(1-s) are already
volume-optimal for this fixed source and cut mechanism.

If the original scheme includes every paid outer completely and uses all
cyclic rows, averaging its cut masses gives b/2+E/3, regardless of unequal
outer volumes or unequal clone counts. Let m=M/b. Necessary inequalities
E>(m-1)b and b/2+E/3<Gamma_d M yield

    m>1/[2(3 Gamma_d-1)].

For d>=2, the first three binomial terms give
(1+1/d)^d>=2+(d-1)/(2d)>=9/4, so Gamma_d<=4/9 and m>3/2.
The source formula m=(2s)^d/6^r then forces s>9/10: otherwise
m<=(1.8)^(3r-1)/6^r=(0.972)^r/1.8<1. By (13), the total outer volume
is at most n[2(1-s)]^d6^(-r)b. Hence necessarily

    n>(1-1/m)[s/(1-s)]^d >9^d/3.                       (14)

The free-box construction avoids this precise barrier by changing the middle
body and separating the directions controlling cuts from those controlling
volume. Formula (14) is not claimed for arbitrary convex bodies or for the
new product construction.

## 8. A rigorous projection fact for future code compression

One potential further route is to place many outer fibers at negative binary
vectors rather than allocating a separate integer coordinate to each outer.
The projection census itself can be controlled exactly. Let F be any family
of nonempty subsets of {1,...,n}, and put

    Q=conv({0,1}^n union {-1_J:J in F}).

Then

    Q intersect Z^n={0,1}^n union {-1_J:J in F},          (15)

and every listed nonzero point is exposed. To prove (15), note that Q lies
in [-1,1]^n and satisfies z_i-z_j<=1 for every i,j: these linear inequalities
hold on both positive and negative cubes. Thus an integer point cannot have
both a positive and a negative coordinate. A nonzero negative integer point
is -1_J for some nonempty J. In a convex representation, its coordinate -1
on each j in J forces every positive-weight generator to be a negative cube
vertex containing J. Its zero coordinates outside J then force each such
vertex to have no further entries. The sole possible generator is -1_J
itself, so it must be listed.

For exposure of 1_I, use coefficients 1 on I and -1/(n+1) outside I. Its
value |I| is uniquely maximal among positive cube vertices, while every
negative cube vertex has value at most (n-|I|)/(n+1)<1<=|I|. Negating the
same construction exposes -1_J. Consequently nonzero prescribed fibers at
these bases survive their convex hull exactly.

There is also a necessary volume constraint that any such construction must
respect. Suppose an actual convex body has origin fiber B of volume b,
fibers of volume M at every positive unit vector, and an outer fiber A_J
of volume a_J at -1_J, where h=|J|. Convexity at the cancelling bases gives

    A_J+sum_(i in J)C_(e_i) subset (h+1)B.

Brunn--Minkowski and then arithmetic--geometric mean imply

    a_J^(1/d)+h M^(1/d)<=(h+1)b^(1/d),
    a_J M^h<=b^(h+1),
    a_J<=b/m^h,               m=M/b.                   (16)

The zero-volume case is immediate; otherwise apply AM--GM to the h+1
positive terms in the first line. In particular positive outer volume
requires m<(1+1/h)^d. Summing (16) over every possible negative codeword
gives the universal necessary estimate

    E<=b[(1+1/m)^n-1].

These facts do not yet give a new counterexample. The origin must still be
controlled for all balanced combinations, and the middle cuts must exclude
every positive cube fiber while charging sufficiently little outer mass.
In the present paid/unpaid construction, a codeword containing coordinates
of different types is paid in multiple cuts. That increased cut cost is an
actual remaining obstruction; the exact projection census does not remove it.
