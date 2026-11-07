# An earlier three-source refinement with n=666

Status: analytic parameter refinement with independent mathematical review
and exact rational checks completed; not Lean-formalized. The later
[four-source construction](barycentric-box-source-counterexample.md) gives
n=76 and supersedes this integer-dimension bound. This note retains the
intermediate parameter certificate rather than repeating the common proof.

Use the general near-uniform-center and free-box construction in Sections
1–4 of [small-integer-dimension-exploration.md](small-integer-dimension-exploration.md),
with the following exact parameters:

    N=222, n=666, h=33666,
    epsilon=1/100000000,
    s=500001/1000000,       t=999997/1000000,
    eta=399999/400000,      q=10001/20000.

Let kappa=(1/3+epsilon)/(1/3-epsilon), u=2(1-q), and let the normalized
core and total outer volumes be

    m=((2s)^2/6)(2q)^h,
    E=666(t^2/6)u^h.

All geometric hypotheses in that proof hold; specifically

    eta-t=2(1-s)-eta=1/2000000,
    3-2s-2 kappa t=48500003/12499999625000 >0.

The exact rational powers satisfy

    4829177735/10^9 < m < 4829177736/10^9,
    3829582770/10^9 < E < 3829582771/10^9.

Write these endpoints as mlo,mhi,Elo,Ehi. Then

    (71/193)mlo-1/2-Ehi/3=168211/18093750000 >0,
    1+Elo-mhi-mhi/2^14=45172483/409600000000 >0.

Also e<193/71: the terms through 1/6! sum to 1957/720, and the remaining
tail is at most (1/7!)sum_(j>=0)(1/8)^j=1/4410. The difference between
193/71 and this rational upper bound is 23/834960>0. Thus

    1/2+E/3 < m/e,
    (1+E-m)/m > 2^(-14).

The common simplex-padding argument in Section 6 of the referenced proof,
with ell=2^(666+14)=2^680, gives a full-dimensional rational polytope in

    R^666 x R^(33668+2^680)

all of whose nonempty integer fibers have full continuous dimension and
whose induced mixed-integer set S satisfies

    sup_(y in S) depth_S(y) < 1/(e 2^666).

The [checker](check_integer_dimension_666.py) verifies the large-power
enclosures directly by integer cross-multiplication and prints the compact
[certificate](integer-dimension-666-certificate.json). The argument concerns
the exact constant 1/e; it does not refute every positive absolute constant.
