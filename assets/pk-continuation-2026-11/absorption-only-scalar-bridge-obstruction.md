# Exact obstruction to an absorption-only scalar bridge

This note concerns a relaxation of the simplex-source hitting problem. It
is not a counterexample to that geometric problem or to Oertel's conjecture.
No actual source simplex is asserted to realize any pattern below.

## 1. The proposed implication and its failure

Let d=5, N=6, v=9/10 and Gamma=(5/6)^5=3125/7776. Work in barycentric
coordinates of a 5-simplex B of volume vV. For one common irreducible
row-stochastic matrix P with zero diagonal, the cuts

    lambda_j-(P lambda)_j>=0                                 (1)

pass through the centroid and have a positive linear dependence. Their
own-cap fractions are exactly

    p_j=product_l (1+P_jl)^(-1).                              (2)

For a nonempty hit pattern R with missed rows J, set

    H_J=(I-P_JJ)^(-1)P_JR,
    m_j=max_(r in R)(H_J)_jr,
    U_J=product_(j in J) sqrt(m_j)/(1+sqrt(m_j)).              (3)

The stochastic sign-cone capacity theorem says that the relative volume
of a simplex missing J is at most U_J. A source with absolute volume
at least V/32 must therefore satisfy the NECESSARY condition

    U_J>=1/(32v)=5/144.                                      (4)

The following explicit data satisfy (4) for every positive-weight
pattern, yet the six relaxed scores

    v p_j+sum_(R containing j)e_R                            (5)

are all strictly less than Gamma, although sum_R e_R=1-v.
Consequently, (4), the common stochastic matrix, the exact own-cap
fractions, and the total-weight constraint do not imply the sharp fan
score. Keeping the true source vertices or stronger geometric capacity
information is essential for this route.

## 2. Exact rational data

Take P to be 1/1000 times

    [  0 179  90 268 157 306 ]
    [109   0 219 385 130 157 ]
    [250 202   0 319  68 161 ]
    [218 166 257   0 195 164 ]
    [ 90 514 218  56   0 122 ]
    [241 155 217 113 274   0 ].                              (6)

Every row sums to 1000 and every off-diagonal entry is positive. In
particular P is irreducible. An explicit positive stationary vector is

    (390041764289056, 478505121826412, 426233422063798,
     488167936538412, 353460491043747, 386283386451106)
       /2522692122212531.                                    (7)

Thus (1) really has a strictly positive dependence; the obstruction does
not come from treating six unrelated cuts as a positive fan.

All indices in the following table are one-based. Weight numerators
have the common denominator 10^8. In the final column, list the missed
rows in increasing order; the displayed integers r_j satisfy

    (r_j/10^8)^2<=m_j<((r_j+1)/10^8)^2.                       (8)

| Hit pattern R | 10^8 e_R | Lower-root numerators r_j |
|---|---:|---|
| {1,3} | 3325032 | 77847299, 75490433, 79258898, 73990248 |
| {2,4} | 2926661 | 71820346, 72460962, 85742987, 76407777 |
| {1,2,6} | 257610 | 61256819, 61617715, 78410145 |
| {2,3,6} | 184033 | 64075908, 59722150, 75273750 |
| {4,6} | 963218 | 72914871, 80890710, 78946842, 75897691 |
| {5,6} | 2343446 | 77900568, 75108245, 77476941, 73770372 |

The weight numerators sum to 10^7. For each row, rational arithmetic gives

    product_j r_j/(10^8+r_j)>87/2500>5/144.                   (9)

Since t/(1+t) is increasing for t>=0, (8)-(9) prove (4) without numerical
square-root evaluation. Note that (9) is a lower bound on the *upper
bound* U_J on true simplex capacity, not a lower bound on true capacity.

Using (2), all six scores (5) obey the rational certificate

    v p_j+sum_(R containing j)e_R<2007/5000<3125/7776.        (10)

The second gap in (10) is 2321/4860000. The exact smallest gap between
Gamma and the six scores is the stronger positive number

    14948831998616419019/27935376210333900000000.              (11)

All claims in (7)-(11) follow by exact rational elimination, multiplication,
and comparison from (6) and the table. The complete individual absorption
maxima and individual score fractions are retained in the certificate
`absorption-relaxation-rational-certificate.json`.

## 3. Independent verification and scope

`check_absorption_relaxation_certificate.py` is an independent standard-
library checker. It reconstructs each absorption matrix by Fraction
Gaussian elimination, verifies its defining matrix equation, positivity,
and row sums, recomputes every absorption maximum, proves (8) using integer
square roots, and checks (7), (9)-(11) and the exact total weight. It uses
neither the numerical search, its saved array, nor an optimization solver.

Run:

    python3 -B check_absorption_relaxation_certificate.py

The report is `audit-absorption-relaxation-rational-certificate.json`.
The checked original certificate SHA-256 is
`99bb5c36c4b5e1ae2eda699ce0045cb753b968e18f77f98e7d71edab974b66dd`.

The exact source-vertex defect inequality in the stochastic capacity note
remains available. This certificate omits those nonnegative defect terms,
and cannot determine whether even one of its six patterns admits an
actual simplex of the required volume. It therefore blocks the
absorption-only scalar implication, not the stronger geometric route.
