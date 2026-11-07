# An actual simplex obstruction to a mean-cap capacity bridge

The following suggested bridge is false, even for a strictly positive
stochastic centroid fan in dimension5:

    capacity(K_J)
      <=[mean_j p_j-r/N]/[2^d(Gamma_d-r/N)],                 (1)

where N=d+1, r=|J^c|, r/N<Gamma_d, and
p_j=product_(l!=j)(1+P_jl)^(-1) are the own vertex-cap fractions.
The example below supplies an actual retained simplex above the proposed
bound. It is not a counterexample to the sharp hitting theorem or
Oertel's conjecture.

Take N=6, d=5, J={1,2,3,4}, R={5,6}, and epsilon=1/10000. Let P have
zero diagonal. In each row j in J, set

    P_j5=1-4epsilon,
    P_jl=epsilon for l not in {j,5}.

In rows5 and6, set every off-diagonal entry equal to1/5. All off-diagonal
entries are strictly positive and every row sums to1. Thus the cuts
lambda_j-(P lambda)_j>=0 form a full positive fan through the uniform
centroid, with the usual strictly positive stationary dependence.

Put

    t=(1-4epsilon)/(2-4epsilon)=2499/4999.

The simplex Q with vertices

    e_5, e_6,
    t e_j+(1-t)e_5, j=1,2,3,4                               (2)

lies in K_J. At the j-th edge vertex its j-th retained constraint is an
equality, because t=P_j5(1-t). Every other retained constraint has left
side zero and nonnegative right side; at the two root vertices those
constraints are strict. The source strictly hits both rows5 and6 at
its corresponding root vertex, so R is its exact hit pattern.
Expansion in the four constrained rows gives

    |Q|/|Delta|=t^4
      =39000037490001/624500149980001.                        (3)

The own-cap fractions are

    p_1=...=p_4
      =1/[(2-4epsilon)(1+epsilon)^4]
      =25000000000000000000/50009998999599964999,
    p_5=p_6=Gamma_5=3125/7776.

Substituting their mean and r/N=1/3 into the right side of(1) gives

    T=156203494652860562789651/2558911628811531009068832.

Direct rational subtraction yields

    |Q|/|Delta|-T
      =449798683564218185227421478115819
         /319672073610396031852077442623411168>0.             (4)

This is an exact geometric contradiction to(1), not a failure of a
particular capacity upper-bound method. It is robust to strict contact
conventions: contract Q by999/1000 about its centroid. All J constraints
then become strict, and its ratio(999/1000)^5 t^4 remains strictly
larger than T. Both claims are exact rational comparisons.

The mechanism is already visible at epsilon=0. The J rows then point
entirely to root5, giving the retained simplex ratio1/16, while those
rows' cap fractions are1/2 and the two root rows' fractions are Gamma_5.
The mean-cap bound becomes Gamma_5/[96(Gamma_5-1/3)], which is less than
1/16 precisely when Gamma_5>2/5; indeed15625>15552 verifies that inequality.
The positive epsilon above removes all zero off-diagonal transitions
while retaining a strict violation.

`check_mean_cap_bridge_obstruction.py` reconstructs the matrix, source
vertices, all retained inequalities and strict hits, the exact volume,
cap fractions, and positive gap using only Fraction arithmetic. It also
verifies the strict-miss contraction. The complete output is
`audit-mean-cap-bridge-obstruction.json`.

The obstruction shows that a uniform average of the row cap fractions
cannot by itself provide the proposed capacity bound. A direction-dependent
weight or another compatibility condition would be necessary for that
approach. No such replacement is asserted here.
