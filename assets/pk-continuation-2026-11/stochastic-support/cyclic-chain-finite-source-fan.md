# An exact cyclic-chain finite simplex-source fan

This note constructs a finite simplex-source hitting fan whose24 scores
are all below Gamma_23. It does not, by itself, construct a mixed-integer
body. Any implication through a separate completion theorem must be
independently verified; no such implication is assumed in this proof.

## 1. Ambient simplex and positive fan

Let B be a23-dimensional simplex of volume V/4, with barycentric
coordinates lambda_0,...,lambda_23. Indices are taken modulo24. Put

    f_j=lambda_j-lambda_(j+1),
    H_j={x:f_j(x)>=0}, j=0,...,23.                           (1)

All cuts pass through the centroid g_B. Their affine functions sum to
zero, hence their normals have a positive dependence with all24
coefficients equal to1. Their rank is23: if all successive differences
vanish, every barycentric coordinate equals1/24. Thus this is a full
positive fan. Every own cap has exactly half the volume of B, since
exchanging vertices j and j+1 is a volume-preserving affine symmetry of
the simplex interchanging the two sides. Its boundary has23-dimensional
measure zero. Consequently

    |B intersect H_j|=V/8 for every j.                       (2)

## 2. Three actual simplex sources

For a=0,1,2 define the eight-element root set

    R_a={j:j is congruent to a modulo3},

and the retained region

    K_a={x in B:f_j(x)<=0 for every j outside R_a}.           (3)

The constraints split the24 coordinates into eight disjoint chains

    lambda_(r-2)<=lambda_(r-1)<=lambda_r, r in R_a.

For each root r form three barycentric points

    e_r,
    (e_(r-1)+e_r)/2,
    (e_(r-2)+e_(r-1)+e_r)/3.                                (4)

The region K_a is exactly the simplex with these24 vertices. Indeed, a
nonnegative ordered triple (u,v,w) with u<=v<=w decomposes as

    u(1,1,1)+(v-u)(0,1,1)+(w-v)(0,0,1).

Replacing the three unnormalized generators by(4) multiplies their
coefficients by3,2,1 respectively. Summing the resulting coefficients
over all chains gives the total coordinate sum1. This proves convex
containment in the vertices(4); the reverse containment is immediate.
After grouping each chain's rows and columns, the barycentric vertex
matrix has eight3-by-3 blocks of determinant magnitude1/6. Hence

    |K_a|/|B|=6^(-8),
    |K_a|=V/(4*6^8)=V/6718464>V/8388608=2^(-23)V.            (5)

Each source strictly hits every root cut, because f_r(e_r)=1. It misses
all other cuts by(3). Its exact strict hit set is therefore R_a.

## 3. Interior sources and strict missed inequalities

The source centroid g_a has coordinates, along every chain,

    (lambda_(r-2),lambda_(r-1),lambda_r)
       =(2,5,11)/144.                                      (6)

For example, the first coordinate receives1/3 from just one of the24
vertices; the middle receives1/2+1/3; and the root receives1+1/2+1/3.
Define actual smaller simplices

    P_a=(199/200)K_a+(1/200)g_a.                             (7)

All their barycentric coordinates are at least1/14400, so P_a lies in
the interior of B. Every missed f_j is at most-1/9600: its maximum on
K_a is zero, while its centroid value is either-1/48 or-1/24. Every root
support maximum is

    max_(x in P_a)f_r(x)=199/200+(1/200)(1/16)=637/640>0.

Thus strict contacts are not needed for the exact hit pattern R_a.
The sources still meet the required volume threshold. Bernoulli's
inequality gives

    (199/200)^23>=1-23/200=177/200>6561/8192=6^8/2^21.

Combining this with(5) proves

    |P_a|=(199/200)^23 V/(4*6^8)>2^(-23)V.                  (8)

## 4. Exact scores and constant comparison

Assign each of the three sources weight e_a=V/4. The total source weight
is3V/4=V-|B|. Each row belongs to exactly one root set R_a. By(2), its
strict-hitting score is therefore

    |B intersect H_j|+sum_a e_a 1{P_a hits int H_j}
      =V/8+V/4=3V/8.                                      (9)

On the other hand,

    Gamma_23=(23/24)^23>3/8,                               (10)

because

    8*23^23-3*24^23=326771892497780718705079179064>0.

Even the slightly smaller reference M=(999/1000)V satisfies

    Gamma_23 M>3V/8.                                      (11)

Indeed its cross-multiplied positive difference is

    8*999*23^23-3000*24^23
      =159728148498997422430238915779464>0.

Equation(11) is recorded only as an exact margin useful for
checking a separate construction; it is not a mixed-integer inference.

The standard-library checker `check_cyclic_chain_source_fan.py` uses
Fraction arithmetic to calculate all three24-by-24 determinants, all
vertex cuts, centroid coordinates, strict-miss and interior margins,
volumes, exact scores, and(10)-(11). Its full report is
`audit-cyclic-chain-source-fan.json`. No numerical approximation or
optimization is used in the certificate.
