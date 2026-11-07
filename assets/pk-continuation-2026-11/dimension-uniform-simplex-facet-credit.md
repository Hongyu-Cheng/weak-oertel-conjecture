# Dimension-uniform small-endpoint credit in simplex facet directions

Status: new draft lemma, requiring independent proof review. This is an exact geometric cap-credit statement, not an all-direction center theorem. It improves the smallness condition in pending candidate `986ab1688d049a3b`, Sections 2-4, and permits a larger simplex partner. Its proof is supplied in full below. No mixed-integer conjecture or pending local-star lemma is used.

## Statement

Let d>=2, N=d+1, J=ceil(N/2), q=N-J+1=floor(N/2)+1, and b=1/N. Put

    m_N=max{N^(-N/(2q)), 4^(-(N-1)/q)},
    tau_d=(1-1/(N m_N))^d.                        (1)

Then m_N>b and

    tau_d>2^(-64).                                (2)

Let B,C be d-dimensional simplices, let A be a convex d-body, and assume

    (A+C)/2 subset B,          |C|>=|B|.

Let lambda_1,...,lambda_N be the barycentric functions of B. For each i define the actual two-endpoint cap cost at the B-centroid threshold by

    e_i=inf_(beta in R) [|A intersect {lambda_i>=b+beta}|
                        +|C intersect {lambda_i>=b-beta}|].

If

    |A|/|C| <= tau_d,                              (3)

then

    sum_(i=1)^N e_i >= J |A|.                      (4)

In particular the dimension-independent sufficient condition |A|/|C|<=2^(-64) works for every d>=2. No diameter or shape condition on A is imposed, and |C| need not equal |B|.

The d+1 directional costs e_i have separately optimized integer tilts. Statement (4) does NOT assert that one point works for all continuous directions, does not establish a dimension-independent local-star repair, and does not imply OC on its own.

## 1. A stochastic-matrix row estimate

Let P be an N by N nonnegative column-stochastic matrix with |det P|>=2^(-(N-1)). Sort its row maxima r_1>=...>=r_N. Then r_J>=m_N.

For the first bound, replace the first row by the sum of all rows, which is the all-ones row. This leaves the determinant unchanged: the extra terms obtained by multilinearity have repeated rows and vanish. For every remaining row i subtract r_i/2 times that ones row. Its entries lie in [-r_i/2,r_i/2], so its Euclidean norm is at most sqrt(N)r_i/2. Hadamard's inequality gives

    |det P|<=N^(N/2) 2^(-(N-1)) product_(i=2)^N r_i.

Since J>=2, the factors with 2<=i<J are at most one, and the q=N-J+1 remaining factors are at most r_J. Thus

    r_J>=N^(-N/(2q)).                              (5)

For the second bound, let s_i be the row sums. Hadamard and entrywise nonnegativity give

    |det P|^2 <= product_i sum_j P_ij^2
                 <=product_i(r_i s_i)
                 <=product_i r_i,

because sum_i s_i=N and arithmetic-geometric mean gives product_i s_i<=1. Now product_i r_i<=r_J^q: discard the first J-1 factors, which are at most one. Therefore

    r_J>=4^(-(N-1)/q).                             (6)

Equations (5)-(6) prove the claim. Since q>N/2, the first term of m_N is strictly larger than 1/N.

## 2. The minimum row, not only the width, controls the cap scale

Fix p in A. The simplex (p+C)/2 is contained in B. Its barycentric vertex matrix P is nonnegative and column stochastic, and

    |det P|=2^(-d)|C|/|B|>=2^(-d).

For the i-th barycentric coordinate write

    h_i=max_C lambda_i, l_i=min_C lambda_i, W_i=h_i-l_i>0,
    r_i(p)=(lambda_i(p)+h_i)/2,
    a_i(p)=(lambda_i(p)+l_i)/2.

These are respectively the maximum and minimum of the i-th row of P. In particular

    a_i(p)>=0,
    W_i=2(r_i(p)-a_i(p)).                          (7)

At every p, at least J indices have r_i(p)>=m_N. For each such index,

    [r_i(p)-b]/[r_i(p)-a_i(p)]
       >=[r_i(p)-b]/r_i(p)
       >=1-1/(N m_N).                             (8)

The first inequality uses the NONNEGATIVE MINIMUM ROW VALUE in (7). This is the gain over the coarser width bound W_i<=2.

## 3. Exact cap accounting

Put a=|A|, W=|C| and r=(a/W)^(1/d). Brunn-Minkowski and |C|>=|B| imply a<=|B|<=W, so r<=1. For each i set

    T_i=2b-h_i+W_i r.

A homothetic copy of C toward an h_i-maximizer, of ratio r, has volume a and lies in the C-cap lambda_i>=h_i-W_i r. For any beta, either the actual C-cap lambda_i>=b-beta already has mass at least a, or its threshold is strictly greater than h_i-W_i r. In the latter case b+beta<T_i, so the A-cap contains A intersect {lambda_i>=T_i}. In either case,

    e_i>=|A intersect {lambda_i>=T_i}|.             (9)

For each p and every one of its J high rows, (3) and (8) give

    r<=[r_i(p)-b]/[r_i(p)-a_i(p)],

which is exactly lambda_i(p)>=T_i after substituting (7). Thus the N measurable sets on the right of (9) cover every p in A with multiplicity at least J. Integrating their indicators proves (4).

Every cap is closed. The only strict threshold comparison arose when the C-cap had STRICTLY less than a; it loses no boundary mass. A and C are full-dimensional, so these nonconstant-coordinate boundaries also have zero d-volume. No minimizing tilt or simultaneous choice of the directionwise minimizers is used.

## 4. An explicit dimension-independent constant

We prove tau_d>2^(-64) by three elementary ranges. The constants are deliberately conservative.

First, for every N>=3,

    N m_N >= N^(1/(N+1)).                          (10)

Indeed the exponent 1-N/(2q) is 1/(N+1) for odd N and 2/(N+2)>=1/(N+1) for even N.

For 3<=N<=15, the function log x/(x+1) has at most one interior critical point, a maximum: its derivative has the sign of 1+1/x-log x, which is strictly decreasing. Its minimum on [3,15] is therefore at an endpoint, and log3/4>log15/16 because 3^4>15. Also log15/16>log(7/6), since 15*6^16>7^16. Hence (10) gives

    1-1/(N m_N)>1/7.

As d=N-1<=14,

    tau_d>7^(-14)>2^(-40)>2^(-64),

where 7^14=678223072849<1099511627776=2^40.

For 16<=N<=31, (6) implies

    N m_N >= (N/16) 4^(4/(N+1)).                  (11)

For odd N this is equality for the expression from (6); for even N the exponent correction is 6/(N+2)>=4/(N+1), so it remains a lower bound. The right side of (11) is increasing for N>=16: its logarithmic derivative is 1/N-4log4/(N+1)^2>0 (use log4<3/2). At N=16 it equals 4^(4/17)>4/3, since 3^17=129140163>67108864=4^13. Consequently

    1-1/(N m_N)>1/4,
    tau_d>4^(-30)=2^(-60)>2^(-64).

For N>=32, (6) gives m_N>1/16, hence

    tau_d>=(1-16/N)^(N-1).

For 0<=x<=1/2, log(1-x)>=-2x; this follows by differentiating log(1-x)+2x, whose derivative is nonnegative on that interval. Therefore

    (1-16/N)^(N-1)>=exp(-32(N-1)/N)>e^(-32)>2^(-64),

using e<4. This proves (2) in all dimensions.

## 5. Limits of the conclusion

The exact scale tau_d is considerably better than the coarse displayed universal constant; no optimization of 2^(-64) is claimed. The same proof applies to any simplex partner C with volume at least that of B, because its midpoint determinant is only larger.

The result is nevertheless confined to the fixed B-centroid thresholds in its facet directions. The center-balancing and all-other-direction arguments from the local-star proof are separate obligations. No dimension-independent constant in that complete local repair is inferred here. In particular, a larger partner does not make an arbitrary nonsimplex low-volume target close to a simplex.
