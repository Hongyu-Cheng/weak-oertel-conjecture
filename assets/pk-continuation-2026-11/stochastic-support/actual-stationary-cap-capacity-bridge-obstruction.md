# An actual obstruction to stationary-weighted cap averaging

Consider the proposed stationary-weighted bridge

    capacity(K_J)
      <=[sum_j pi_j p_j-pi(R)]/[2^d(Gamma_d-pi(R))],          (1)

under pi(R)<Gamma_d, where pi is the positive stationary distribution of
P and R=J^c. This implication is false for a strictly positive stochastic
centroid fan in dimension5. The counterexample below concerns exactly
that assumption; its uniform hit fraction |R|/N=2/3 exceeds Gamma_5,
so it does not refute a different assertion imposing both conditions.
No Oertel or sharp hitting-center counterexample is asserted.

Let N=6, d=5, J={1,2}, R={3,4,5,6}, epsilon=1/10000, and

    a=(1-3epsilon)/2.

Row1 of P has entries a at columns2 and3, epsilon at columns4,5,6, and
zero on its diagonal. Row2 has entries a at columns1 and3, epsilon at
columns4,5,6, and zero on its diagonal. Each row indexed by R has entries
a at columns1 and2, epsilon at the other three columns in R, and zero
on its diagonal. Thus every row has two entries a and three epsilon,
and all off-diagonal entries are positive.

Every own cap has the SAME fraction

    p=1/[(1+a)^2(1+epsilon)^3]
      =400000000000000000000/900089981998200090009.            (2)

In particular sum pi_j p_j=p. The exact positive stationary distribution
is

    pi=(9997/29997, 9997/29997, 99950012/299999997,
          1/10001, 1/10001, 1/10001).

It sums to1 and satisfies pi P=pi by direct rational multiplication.
Equivalently, the two-state flux between J and R gives

    pi(R)=(1+3epsilon)/(3-3epsilon)=10003/29997<Gamma_5.       (3)

Put t=a/(1+a)=9997/29997. The six vertices

    e_3,e_4,e_5,e_6,
    t e_1+(1-t)e_3,
    t e_2+(1-t)e_3                                           (4)

form a simplex Q in K_J. At its corresponding edge vertex, each retained
constraint is an equality because t=a(1-t). At the other vertices that
row's coordinate is zero and its right side is nonnegative. Each root
row is strictly hit at its own original vertex, so its exact hit set is R.
Expansion in rows1,2 gives

    |Q|/|Delta|=t^2=99940009/899820009.                        (5)

The proposed right side of(1), using(2)-(3), equals

    T=99849982000600210009/1970430673996059729663.

The actual retained simplex exceeds it by

    |Q|/|Delta|-T
      =32126566933877094620869342
         /531963080350738233396309099>0.                     (6)

The violation persists after contracting Q by999/1000 about its centroid,
which makes every missed inequality strict. Thus boundary contacts do
not account for the failure.

The issue is visible as epsilon tends to zero: the three active states
1,2,3 carry equal stationary masses, while the other three surviving
roots have vanishing stationary mass. The retained simplex still uses
all four root directions. Consequently stationary mass alone does not
record their geometric contribution. The example is not a proposal to
replace stationary weights by another fixed mixture.

`check_stationary_cap_bridge_obstruction.py` verifies the stochastic
matrix, stationary distribution, equal cap fractions, actual source
vertices, all cone inequalities, strict hits, exact volume and gap, and
the strict-miss contraction using only Fraction arithmetic. Its full
output is `audit-stationary-cap-bridge-obstruction.json`.
