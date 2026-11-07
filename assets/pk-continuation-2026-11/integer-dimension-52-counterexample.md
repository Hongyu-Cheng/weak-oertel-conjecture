# An intermediate 52-integer-variable counterexample to the 1/e bound

Status: complete geometric deduction and exact rational scalar certificate;
two independent full mathematical and exact-certificate reviews passed. This
is not Lean-formalized. Its continuous dimension is about `2.31*10^18`, so
it does **not** meet the current billion-scale dimension target.

## Statement and dimensions

There is a rational convex polytope with nonempty ambient interior in

    R^52 x R^(274784+2^61)

such that, for its induced mixed-integer set, every point belongs to a
proper closed ambient halfspace containing strictly less than
`1/(e*2^52)` of the mixed-integer volume. All its nonempty integer
fibers have full continuous dimension. In particular, the same statement
holds for the intrinsic Hausdorff measure specified in the task.

The continuous dimension is exactly

    d=2305843009213968736.

This reduces the common-simplex dimension from `2^93` in the formally
verified 76-variable example to `2^61`. It is an intermediate improvement,
not completion of the requested dimension reduction.

## Exact parameters and unpadded body

Use the complete geometric lemma in
[the accepted proof](../../facts/df488edae05a1702.md), with

    N=13,                  n=4N=52,
    h=274781,              ell=2^61,
    s=500000001/10^9,       t=999999997/10^9,
    eta=399999999/400000000,
    epsilon=1/10^12,        q=100001/200000,
    theta=3/32,             beta=27/64.

For clarity, the integer support consists of all Boolean bases together
with all nonempty negative Boolean subsets contained in any one of four
blocks of size 13:

    Z={0,1}^52 union { -1_J : empty!=J subset I_a, a=0,1,2,3 }.

Let `B0` be the centered standard tetrahedron, with barycentric
coordinates `lambda_j`, and let

    T_a={x in B0: lambda_j(x)<=1/4 for j!=a},
    lambda_a(c_a)=1/4+3 epsilon,
    lambda_j(c_a)=1/4-epsilon       (j!=a),
    F=[-1,1]^h,                    B=B0 x F.

At a positive Boolean base `1_I`, put

    K_I=[2(c_a+s(T_a-c_a))+(|I|-1)c_a] x (2q F),

where `a` is the block of any fixed selected member of `I`. At a
negative base `-1_J`, where `J subset I_a` and `r=|J|`, put

    G_(a,r)=[t_r(T_a-c_a)-(r-1)c_a] x (u_r F),
    t_r=1-r(1-t),                  u_r=1-r(2q-1).

Include `B` at zero and take the convex hull of these finitely many
fibers; call it `C0`. The linked geometric proof establishes:

1. Its integer projection points are exactly `Z`.
2. Every nonzero integer base is exposed, so its actual fiber is exactly
   the assigned `K_I` or `G_(a,r)`.
3. The origin fiber is exactly `B`. Specifically every generator obeys
   `lambda_j(x)+v sum_i z_i>=0` and
   `+/-w_l<=1+(2q-1)sum_i z_i`, where
   `v=(2s-1)/4+(2-2s)epsilon`. At `z=0` these inequalities define `B`.
4. `C0` is a full-dimensional rational convex polytope, and every actual
   nonempty integer fiber is a convex body in `R^(3+h)`.
5. Four proper closed halfspaces cover the origin fiber, strictly avoid
   every positive Boolean fiber, and each capture precisely one negative
   block and a tetrahedral `beta`-fraction of `B`.

All the hypotheses used for these conclusions are certified below.
In particular the argument controls convex combinations involving
overlapping negative subsets; no unproved independence of those subsets
is assumed.

## Exact scalar certificate

Write `b=vol(B)` and define the exact real numbers

    m=theta*(2s)^3*(2q)^h,
    alpha_r=theta*t_r^3*u_r^h,
    E=4 sum_(r=1)^13 binom(13,r)*alpha_r.

Then each positive fiber has volume `mb`, all negative fibers have
volume at most `theta b<mb`, and the unpadded total volume is

    W=b[(2^52-1)m+1+E].

Each of the four origin cuts has exact mass `b(beta+E/4)`.

The companion program
[check_integer_dimension_52.py](check_integer_dimension_52.py) uses
only integer arithmetic and `fractions.Fraction`. Its saved output is
[integer-dimension-52-certificate.json](integer-dimension-52-certificate.json).
It proves the strict enclosures

    1463268/10^6 < m < 1463269/10^6,
     465669/10^6 < E < 465670/10^6.                    (1)

Here are explicit margins for the geometric parameter conditions:

    eta-t = 2(1-s)-eta = 1/(2*10^9)>0,
    1-13(1-t)=999999961/10^9>0,
    1-13(2q-1)=99987/100000>0,

    1-13[(2s-1)+4 epsilon(3t+1-(2s-1))]
      =249999993448000000143/250000000000000000000>0.

All remaining conditions `0<epsilon<1/4`, `1/2<s,q<1`, and `0<t`
follow directly from the displayed rational parameters and are checked
in the same program.

For the transcendental comparison, set `e_+=1359141/500000`.
The exponential series and its geometric tail give

    e < sum_(j=0)^8 1/j! + 10/(9*9!) < e_+,

because the ratio of consecutive tail terms, beginning after `1/9!`,
is at most `1/10`, and subsequent ratios are strictly smaller.
The exact margin in the second inequality is `1717/10206000000`.
Using only the short enclosures (1), the origin-cut margin is

    (1463268/10^6)/e_+ - 27/64 - (465670/10^6)/4
      =40641/2970800000>0.                            (2)

The relative surplus over `2^52` maximal fibers satisfies

    Delta:=1+E-m > 1+465669/10^6-1463269/10^6
                 =3/1250.                            (3)

Finally, with `ell=2^61`, the exact padding margin is

    3/1250 - 2^52*(1463269/10^6)/(2ell-1)
      =139939647533841645493/144115188075855871968750
      >0.                                             (4)

### Why the power certificate is rigorous

The fourteen powers requiring enclosure are `(2q)^h` and
`(1-r(2q-1))^h` for `1<=r<=13`. All bases are positive rational
numbers. Put `D=10^40`. The initial integer bounds on a base `a/b`
are `floor(Da/b)` and `ceil(Da/b)`, interpreted after division by
`D`. For two nonnegative enclosed quantities, their product is
enclosed by flooring the product of the lower integer bounds divided
by `D`, and ceiling the product of the upper bounds divided by `D`.
This follows from monotonicity of multiplication on nonnegative reals.

Apply this rule at each multiplication and squaring in binary
exponentiation. Induction over the binary digits of `h` proves that
the accumulator intervals enclose the required exact power. Every
pre-update exponent, power interval, and accumulator interval is
recorded in the JSON certificate; all rounded operations are ordinary
integer floor or ceiling divisions. Multiplying by the exact positive
rational factors `theta(2s)^3` and `theta t_r^3`, and summing with
the exact nonnegative binomial coefficients, preserves enclosure.
The program then compares the resulting rational endpoints with (1).
Thus (1) is an exact interval certificate, not floating-point evidence.

## Padding with the sharper finite-dimensional estimate

For every positive integer `ell`, write

    Gamma_ell=(ell/(ell+1))^ell.

Then

    log(e Gamma_ell)
      = integral_0^1 t/(ell+t) dt < 1/(2ell).

Since `exp(x)<1/(1-x)` for `0<x<1`—equivalently
`-log(1-x)>x`, by integrating `1/(1-t)>1`—we obtain

    e Gamma_ell < 1+1/(2ell-1).                       (5)

This improves the earlier convenient estimate `1+1/ell` by enough
to use `ell=2^61` here. From (3)--(4),

    (2ell-1) Delta > 2^52 m.

Consequently

    e Gamma_ell * 2^52 m
      < 2^52 m + Delta = W/b.                        (6)

## Every point has a strictly small proper closed halfspace

Let `J` be any full-dimensional rational `ell`-simplex, and set
`C=C0 x J`. This is a rational convex body with the integer and
continuous dimensions stated above. Its total mixed-integer volume
is `W vol(J)`. All its nonempty integer fibers are full dimensional,
so its intrinsic dimension is `d=3+h+ell`.

For a point in the origin fiber, choose one of the four origin cuts
containing its `B0` coordinate; these cuts cover because the four
linear functions `lambda_j-1/4` sum to zero. Extend the chosen cut
to ignore the simplex coordinates. Its volume is exactly
`b(beta+E/4)vol(J)`, which is less than `mb vol(J)/e` by (2).
Since `W>2^52 mb` by (3), its normalized mass is strictly less than
`1/(e*2^52)`.

For a point above a nonzero integer base, take a simplex cap through
its `J` coordinate of relative volume at most `Gamma_ell`. Such a
cap exists at every point: choose a largest barycentric coordinate
`lambda`, which is at least `1/(ell+1)`, and use the cap where that
coordinate is at least `lambda`. Its relative volume is
`(1-lambda)^ell<=Gamma_ell`. Since the chosen integer base is
exposed and there are only finitely many other fibers, adding a
sufficiently large positive multiple of its integer exposing
functional to the simplex cap's functional produces a proper closed
ambient halfspace that agrees with the cap on this fiber and misses
every other fiber. Compactness bounds the cap functional uniformly,
and the exposing gaps are strictly positive, so a finite multiplier
suffices. The halfspace's mass is at most
`Gamma_ell mb vol(J)`, strictly below the target by (6).

All cuts are ambient halfspaces with nonzero normals. The integer
exclusion gaps are strict; the continuous cap boundaries have zero
volume. Thus their stated masses are valid for closed halfspaces,
including points on the boundary of a fiber. The uniform bound

    max{ b(beta+E/4), Gamma_ell mb } / W < 1/(e*2^52)

applies to every point of the actual mixed-integer set. This proves
the claimed intermediate counterexample.
