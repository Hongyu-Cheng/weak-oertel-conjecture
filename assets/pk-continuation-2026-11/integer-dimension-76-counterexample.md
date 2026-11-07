# Optional n=76 parameters with a smaller continuous dimension

Status: analytic parameter refinement with independent full mathematical
review and exact rational interval checks completed; not Lean-formalized. This concerns the exact
constant `1/e`, not every positive absolute constant.

The complete geometric construction and proof are in
[barycentric-box-source-counterexample.md](barycentric-box-source-counterexample.md).
Its four-source construction also gives a full-dimensional rational polytope
in

    R^76 x R^(1372131+2^93)

whose mixed-integer set S satisfies

    sup_(y in S) depth_S(y) < 1/(e 2^76).

All nonempty fibers have the displayed full continuous dimension. Depth
uses the sum of their Lebesgue volumes, equivalently their Euclidean
Hausdorff measure. The only changes from the main note are the following
exact parameters:

    N=19, n=76, h=1372128,
    epsilon=1/10000000000,
    s=5000001/10000000,       t=9999997/10000000,
    eta=3999999/4000000,      q=500001/1000000,
    u=2(1-q),               ell=2^93.

Retain the notation of the main proof:

    theta=3/32,       v=27/64,
    kappa=(1/4+3epsilon)/(1/4-epsilon),
    m=(2s)^3 theta (2q)^h,
    alpha=t^3 theta u^h.

All its geometric conditions hold. In particular

    eta-t=2(1-s)-eta=1/20000000,
    3-2s-2 kappa t=70857143/178571428500000 >0.

Put U=27182819/10000000. The power series of e through 1/10! has sum S10.
Its remaining tail starts at 1/11! and has successive ratios at most 1/12.
Consequently

    e <= S10+12/(11*11!) < U,
    U-[S10+12/(11*11!)]=98141/1372140000000 >0.

Exact rational enclosures for the two volume ratios are

    1458094201550/10^12 < m < 1458094201551/10^12,
    6027739233/10^12 < alpha < 6027739234/10^12.

Writing these four endpoints as mlo,mhi,alo,ahi, direct rational calculation
proves

    mlo/U-27/64-19 ahi
      =11151455803863/13591409500000000000 >0,
    1+76 alo-mhi-mhi/2^17
      =374312936753/131072000000000000 >0.

Thus the two scalar hypotheses for the main construction and padding are

    27/64+19 alpha < m/e,
    Delta/M=(1+76 alpha-m)/m > 2^(-17).

The first gives a containing ambient cut of mass less than M/e for every
point of the origin fiber. The second gives

    W/(2^76 M)>1+1/(2^76 2^17)=1+1/ell>e Gamma_ell.

As proved in the main note, every other integer base is exposed, and a
containing cap in the common ell-simplex factor can be isolated by an
ambient halfspace. Its mass is at most M Gamma_ell times the factor volume.
Both bounds are uniform and strictly below 1/(e 2^76) after normalization.
This proves the displayed strict supremum inequality.

The executable [check_integer_dimension_76.py](check_integer_dimension_76.py)
and its [certificate](integer-dimension-76-certificate.json) verify all
parameter and scalar comparisons above. Positive rational powers are
bounded using outward-rounded intervals with denominator 10^40: initialize
by floor and ceiling; multiply lower endpoints and round down, multiply
upper endpoints and round up. Each operation preserves enclosure because
all factors are nonnegative. Binary exponentiation therefore preserves
exact enclosure by induction on its multiplication and squaring steps.
The exact rational prefactors are then applied and the resulting endpoints
are compared to the short intervals displayed above. No floating-point
calculation or transcendental numerical evaluation is used.

Review provenance: independent mathematical review checked the common
source geometry and halfspace construction; a separate review executed this
checker and verified its interval invariant, exponential-series bound, and
strict scalar margins. This parameter refinement has not been added to the
Lean theorem.
