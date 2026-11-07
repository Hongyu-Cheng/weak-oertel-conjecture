# A sharp-bound counterexample with 132 integer and 99 continuous dimensions

Analytic proof with exact rational scalar certificates and independent
mathematical reviews. This construction is not Lean-formalized.
It refutes the sharp bound `Gamma_d / 2^n`; it makes no claim against
`1 / (e 2^n)` or the repository's absolute-constant target. It reaches
`d < 100` but does not reach `n < 100`.

There is a full-dimensional rational polytope in `R^132 x R^99` whose
nonempty integer fibers all have dimension 99 and whose normalized
mixed-integer halfspace depth satisfies

    sup_y depth(y) < (99/100)^99 / 2^132.

The construction uses simplex joins, so its large positive fibers are
99-simplices. No common simplex padding is needed. Its negative fibers
are larger nonsimplicial sources, but their entire volumes are small
enough to isolate them without a continuous cap.

## 1. A simplex and three source types

Set `d=99`, `D=d+1=100`, `N=44`, `n=3N=132`, and

    a=63/100,    delta=329/10000,    epsilon=1/10^13,
    Q=1-a+a^2,   eta=(1-delta)/2,
    v=delta/D+(1-delta)a epsilon/Q.

Work in the `d`-dimensional linear space of vectors whose `D` coordinates
sum to zero. Let `B` be the standard simplex translated by
`p=(1/D,...,1/D)` so that its centroid is the origin. Write `lambda_i`
for its barycentric coordinates, and `b=vol_d(B)`. Barycentric vectors
such as `e_i` below specify points of this translated simplex. All scalar
multiplication and addition of points is performed in the centered linear
coordinates, not by multiplying affine barycentric vectors.

To obtain a rational polytope in `R^n x R^d` literally, identify this
zero-sum linear space with `R^d` by dropping its last coordinate. The
inverse appends the negative sum of the retained coordinates. This fixed
rational linear isomorphism preserves halfspaces and multiplies every
fiber volume by the same positive Jacobian, so all depth and volume-ratio
claims below are unchanged. An orthonormal rational basis is not needed.

On the first three barycentric coordinates, use cyclic indices and set

    f_j=lambda_j-a lambda_(j+1)-(1-a)lambda_(j+2),   j=0,1,2.

These are nonzero linear functionals, since their affine constants cancel.
They sum to zero and have values in `[-1,1]` on `B`.

Put `c=(1/3,1/3,1/3)` in the first-three-coordinate face. For type zero,
define the full `d`-simplex `U_0` by its barycentric vertices

    e_0, c, (1,0,a)/(1+a), e_3,...,e_(D-1).

Define `U_1,U_2` by cyclically permuting the first three coordinates. The
larger source is

    T_j=B intersect {f_l<=0 for l!=j}.

For type zero its first-three-coordinate polygon is the quadrilateral

    e_0, (1,1-a,0)/(2-a), c, (1,0,a)/(1+a).

It is joined with the face on `e_3,...,e_(D-1)`. Indeed, after dividing
the first three barycentric coordinates by their sum, the two homogeneous
missed-row inequalities give precisely this quadrilateral. A zero sum
gives the free face itself. In particular `U_j` is contained in `T_j`.

The three relevant volume ratios are

    theta_P=vol(U_j)/b = a/[3(1+a)],
    theta_A=vol(T_j)/b = [a/(1+a)+(1-a)/(2-a)]/3,
    beta=vol(B intersect {f_j>=0})/b = 1/[(1+a)(2-a)].     (1)

For the first ratio take the determinant of the displayed three vertices
in their three barycentric coordinates. The remaining vertex columns form
an identity block, so joining the free simplex preserves this ratio.
For the second, split the quadrilateral along `e_0 c`; the two triangle
ratios are `a/[3(1+a)]` and `(1-a)/[3(2-a)]`. For the third, the cap in
the first-three-coordinate face is the triangle with vertices
`e_0`, `(a,1,0)/(1+a)`, and `(1-a,0,1)/(2-a)`. Its determinant is the
displayed `beta`, and again the identity block preserves the ratio.

Let `c_j` have barycentric coordinates `p+epsilon w_j`, where

    w_0=(1,-a,-(1-a),0,...,0)/Q

and the other `w_j` are its cyclic permutations. Direct substitution gives
`f_j(c_j)=2 epsilon` and `f_l(c_j)=-epsilon` for `l!=j`.
Moreover `c_0` is strictly inside `U_0`: its weights on the displayed
vertices of `U_0`, in the same order, are

    epsilon/a,
    3/D-3a epsilon/Q,
    epsilon(2a-1)(1+a)/(a Q),
    1/D,...,1/D.                                           (2)

They sum to one and are strictly positive. The certificate checks these
inequalities exactly. Every coordinate of every `w_j` is at least `-a/Q`.

## 2. Generators and the complete integer-fiber census

Partition the `n` integer-coordinate indices into three blocks `I_0,I_1,I_2`
of size `N`. For each nonempty subset `I` of all indices, choose any member
and let `a(I)` denote its block. At the positive Boolean base `1_I` place

    K_I=(1+delta) U_(a(I))+(|I|-delta)c_(a(I)).              (3)

This is a translate of a full `d`-simplex, of common volume

    M=mb,    m=theta_P(1+delta)^d.                         (4)

For each block `I_j` and every nonempty `J subset I_j` of size `r<=30`,
place at the negative Boolean base `-1_J` the full-dimensional polytope

    G_(j,r)=(1-rDv)T_j.                                   (5)

Its scale is positive, including at `r=30`, as checked exactly below.
Finally place `B` at integer base zero and take the convex hull of all
these generating fibers; call the resulting rational polytope `C`.

The integer points of its projection are exactly the positive Boolean cube
and the listed negative subsets. Each coordinate lies in `[-1,1]`. If an
integer projection has a coordinate `-1`, every generator in a convex
representation has `-1` there, so all these generators are negative
Boolean vectors from that coordinate's block. At every remaining integer
coordinate their entries are zero or minus one. An average of such entries
can be zero or minus one only when all entries agree. Thus all generators
in the representation equal that integer projection, which is listed.
If no coordinate is negative, the projection is a positive Boolean vector.

Every listed nonzero base is uniquely exposed. Let `rho=1/(n+1)`. To expose
`1_I`, use coefficients `1` on `I` and `-rho` outside; its value `|I|`
strictly exceeds every other positive-cube value, and all negative values
are less than one. To expose `-1_J`, use coefficients `-1` on `J` and
`rho` outside. Its value `|J|` strictly exceeds every other negative value,
and all positive-cube values are less than one. Consequently all nonzero
actual fibers are exactly (3) and (5).

The origin fiber is exactly `B`. To prove this, every generating point
`(z,x)` satisfies the affine inequalities

    lambda_l(x)+v sum_i z_i >=0,    l=0,...,D-1.           (6)

For a positive base of size `k`, using `min_(U_j) lambda_l>=0` gives

    lambda_l(x)>=-delta/D+(k-delta)epsilon w_(j,l)
                 >=-delta/D-(k-delta)a epsilon/Q.

Adding `kv` leaves at least
`(k-1)delta(1/D-a epsilon/Q)>=0`. The final factor is positive by (2)
or the exact certificate. For a negative base of size `r`, the scaling
in (5) gives `lambda_l(x)>=rv`, which is exactly (6). The middle generators
also satisfy (6). At integer base zero, (6) is the defining system of `B`,
so the actual fiber is contained in `B`; the reverse inclusion was included
among the generators.

All actual fibers have dimension `d`. The middle fiber spans all continuous
directions, and points above the positive unit bases span the additional
`n` integer directions. Hence `C` is full dimensional and has nonempty
ambient interior.

## 3. Exact volumes and three cuts of the origin fiber

Define

    alpha_r=theta_A(1-rDv)^d,
    E=3 sum_(r=1)^30 binom(N,r) alpha_r.

The exact mixed-integer volume is

    W=b[(2^n-1)m+1+E].                                   (7)

Fix `j=0,1,2`, put `R=3(n+1)`, and consider the closed ambient halfspace

    H_j={ (z,x): f_j(x)+sum_i beta_i z_i>=0 },
    beta_i=-R for i in I_j, and beta_i=eta epsilon otherwise.  (8)

On a negative fiber of a different type, `f_j<=0` and the integer
contribution is `-r eta epsilon<0`, so it is strictly excluded. On a
negative fiber of type `j`, `f_j>=-1` and the integer contribution is
`rR`, so the entire fiber is included.

For a positive fiber indexed by `I`, put `k=|I|`. If `I` contains an index
from `I_j`, its continuous score is less than `k+1`, since
`f_j<=1` on `U_a`, `f_j(c_a)<=2 epsilon`, `delta<1`, and `2epsilon<1`.
Its integer score is at most `-R+(k-1)eta epsilon<-R+k-1`.
The total is therefore less than `2k-R<0`.

If `I` contains no index from `I_j`, its selected source has type different
from `j`, so its maximum continuous score is `-(k-delta)epsilon`.
The total score is at most `[k eta-k+delta]epsilon<0`, because
`eta<1-delta`. Thus every positive fiber is strictly excluded.

On `B`, the cap in (8) has volume `beta b`. The three cuts cover the middle
fiber because `f_0+f_1+f_2=0`. Each has exactly the mass

    vol_MI(C intersect H_j)=b(beta+E/3).                  (9)

Their continuous normals are nonzero; boundaries inside `B` have zero
`d`-volume, and every excluded fiber has a strict score gap.

## 4. Exact scalar certificate

Set `Gamma_d=(d/(d+1))^d`. The companion program
[sharp-triangle-join-check.py](sharp-triangle-join-check.py) uses only
integer arithmetic and `fractions.Fraction`. Its saved output is
[sharp-triangle-join-certificate.json](sharp-triangle-join-certificate.json).
It checks all parameter signs used above and the three strict inequalities

    1+E-m>0,
    Gamma_d m-beta-E/3>0,
    Gamma_d m-alpha_1>0.                                 (10)

These are direct rational comparisons, not interval approximations or
floating-point tests. The certificate records each positive numerator and
denominator. For orientation only, the principal quantities are

    m                         approximately 3.1754198503448268,
    E                         approximately 2.1763054457022837,
    1+E-m                     approximately 0.0008855953574570216,
    Gamma_d m-beta-E/3         approximately 0.000803702148111982,
    Gamma_d m-alpha_1          approximately 1.1660699933505152.

The largest negative-subset scale `1-30Dv` is approximately
`0.012999999761661364`, and is strictly positive exactly.

## 5. Every point has an insufficient proper closed halfspace

At an origin-fiber point, select a containing cut (8). Its mass is less
than `Gamma_d M` by (9)-(10).

At a positive fiber, which is a `d`-simplex, choose a largest barycentric
coordinate of the point. It is at least `1/(d+1)`, so the vertex cap through
that point has relative volume at most `Gamma_d`, by homothety. Since the
integer base is exposed, this continuous cap can be isolated from all
other integer fibers by adding a sufficiently large finite multiple of
an integer exposing functional to its inequality. The finitely many
exposure gaps are positive and the fibers are compact, so a finite
multiplier strictly excludes all the other fibers. The resulting proper
closed ambient halfspace has mass at most `Gamma_d M`.

At a negative fiber, isolate its entire exposed fiber using an integer
halfspace. Its mass is `alpha_r b<=alpha_1 b<Gamma_d M`, by (10).
It is irrelevant that these negative fibers are not simplices.

Thus all points admit a proper closed containing halfspace of mass at most
`Gamma_d M`, uniformly. Equations (7) and (10) give `W>2^n M`, whence

    sup_y depth(y) <= Gamma_d M/W < Gamma_d/2^n.

In fact the first inequality is an equality. The centroid of any positive
simplex fiber has depth at least `Gamma_d M/W`: every ambient halfspace
containing that point retains at least a `Gamma_d` fraction of that fiber,
by the ordinary centroid Grunbaum inequality. Combined with the uniform
upper bound just proved, this gives the exact value

    sup_y depth(y) = Gamma_d m / [(2^n-1)m+1+E].

All fibers have the common dimension `d`, so their volume sum agrees with
the normalized `d`-dimensional Euclidean Hausdorff measure of the finite
disjoint mixed-integer union. This proves the stated sharp-bound
counterexample without a limiting body or a padding dimension.

## 6. Further exact dimension tradeoffs

The same proof works for the following parameter sets. In each row put
`D=d+1`, `N=n/3`, `a=159/250`, `epsilon=1/10^13`, and retain the formulas
for `Q`, `eta`, and `v` above. Replace the negative-subset cutoff 30 by
the listed cutoff.

| Integer dimension n | Continuous dimension d | delta | Negative-subset cutoff |
| --- | --- | --- | --- |
| 153 | 34 | 95483588829/10^12 | 10 |
| 132 | 82 | 791357067/20000000000 | 25 |
| 129 | 104 | 31193387251/10^12 | 32 |

The independent exact calculations for these parameter sets are in
[sharp-triangle-join-pareto-check.py](sharp-triangle-join-pareto-check.py)
and [its certificate](sharp-triangle-join-pareto-certificate.json).
They verify every parameter inequality and all three margins in (10).
The proof therefore also gives a sharp-bound counterexample in each of
these dimensions. The pair `(132,82)` improves both coordinates of the
main worked example weakly, and `(153,34)` has total dimension 187.
The pair `(129,104)` has both dimensions at most 129.

These are witnessed tradeoffs, not global minimality claims. A numerical
parameter scan located them; only their subsequent rational certificates
are used to assert their existence. None has both dimensions below 100.

All four examples satisfy the weaker `1/(e 2^n)` bound. Indeed, their
number `L` of nonempty fibers is less than
`2^(3N)[1+3/2^(2N)]`, with `N>=43` and `d<=104`. The centroid of a
largest fiber has normalized depth at least `Gamma_d/L`. The identity
`log(e Gamma_d)=integral_0^1 t/(d+t) dt` implies
`e Gamma_d>1+1/[2(d+1)]>=1+1/210`, whereas `3/2^86<1/210`.
Therefore `Gamma_d/L>1/(e 2^n)`. This proves the distinction from the
specific `1/e` counterexample, rather than only recording a limitation
of the cuts used above.
