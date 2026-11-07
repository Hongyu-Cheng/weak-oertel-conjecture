# Oblique simplex fans priced by circumscribed volume excess

Research support draft, 6 November 2026. This is an all-point finite-fan certificate. It does not assert that an arbitrary bad fan has small circumscribed volume, and does not prove a center for all ambient halfspaces or OC.

## 1. Statement

Fix d>=1, N=d+1, Gamma=(d/(d+1))^d, and kappa=1/2-Gamma>=0. Let V>0. Let B be any d-dimensional convex body of volume vV with 0<v<=1. Let Q be a d-simplex containing B, of volume qV, so q>=v. Let lambda_1,...,lambda_N be the barycentric affine functions of Q. Let P_i be finitely many d-simplices contained in B, each with volume at least 2^(-d)V, and let their nonnegative weights e_i sum to E=1-v. Zero-weight simplices may be omitted; an empty family is allowed when E=0.

At y in B define

    S_j(y)=|B intersect {lambda_j>=lambda_j(y)}|/V
          +sum_i e_i 1{max_(x in P_i)lambda_j(x)>lambda_j(y)}.

Then for EVERY y in B,

    max_j S_j(y)
      >=R_d(v,q)
       :=v-(1-Gamma)q+E/2-E log q/(N log N).         (1)

In particular, if v<1 and

    q-v<= [kappa/(1-Gamma)](1-v),                   (2)

then

    max_j S_j(y)>Gamma                              (3)

for every y in B. This condition includes d=1, where kappa=0 and it requires q=v. For d>=2 the allowed volume excess is a strictly positive multiple of E.

The middle body B need not be a simplex. The source bodies P_i are simplices, and their lower volume bound is essential to the proof.

## 2. Logarithmic source budget in Q

First suppose y is interior to Q. Put u_j=lambda_j(y), L_j=log(1/u_j), and S=sum_j L_j. Thus every L_j>0 and S>=N log N by Jensen.

For a source P let M be its N by N barycentric vertex matrix relative to Q. It is nonnegative and column-stochastic, and

    |det M|=|P|/|Q|>=2^(-d)/q.

Write r_j=max_l M_jl. At least one row h is hit, meaning r_h>u_h: if all r_j<=u_j, every column equals u because both have sum 1, contradicting the nonzero determinant.

Replace row h by the sum of all rows, the all-ones row, without changing the determinant. Subtract r_j/2 times this row from every other row j. Hadamard's inequality gives

    |det M|<=N^(N/2)2^(-d) product_(j!=h)r_j.

If I is the set of missed rows, every r_j<=u_j for j in I. Because the omitted row is hit and all remaining hit-row maxima are at most 1,

    product_(j in I)u_j>=product_(j!=h)r_j
       >=1/(q N^(N/2)).

Taking logarithms proves

    sum_(j in I)L_j<=(N/2)log N+log q=:A(q).         (4)

In every case with E>0, at least one source exists, and its nonnegative left side shows A(q)>=0. Its hit log-weight is at least S-A(q).

## 3. Subtracting the excess middle volume

The exact Q-cap formula is

    |Q intersect {lambda_j>=u_j}|/V=q(1-u_j)^d.

As B is contained in Q, deleting Q\B removes at most (q-v)V from any cap, so

    |B intersect {lambda_j>=u_j}|/V
       >=q(1-u_j)^d-(q-v).                         (5)

The two sequences L_j and (1-u_j)^d have the same ordering. Chebyshev followed by Jensen gives

    sum_j L_j(1-u_j)^d>=Gamma S.

Use this in (5), and sum the source hit budgets (4) with weights e_i:

    sum_j L_j S_j(y)
       >=[Gamma q-(q-v)]S+E[S-A(q)].                (6)

When E>0, A(q)>=0 and S>=N log N. Thus the weighted mean on the left of (6), divided by S, is at least

    Gamma q-(q-v)+E[1-A(q)/(N log N)]
       =v-(1-Gamma)q+E/2-E log q/(N log N),

which proves (1). If E=0, (6) without source terms proves the same formula directly.

If y lies on a facet of Q, some u_j=0. Its B-cap contains all of B; every full-dimensional P_i has positive support in lambda_j and strictly hits it. Hence that score is v+E=1. This also implies (1): for E>0 the right side can be written

    v-(1-Gamma)q+E[1-A(q)/(N log N)]<=v+E=1,

using A(q)>=0. If E=0, it is at most v=1. Source support equality at a positive threshold has always been counted as a miss.

## 4. Exact surplus under the volume-excess condition

Assume v<1, so E>0. Since Gamma<=1/2<1,

    0<=kappa/(1-Gamma)<1.

Condition (2) therefore gives q< v+E=1. Rewrite (1) as

    R_d(v,q)
      =Gamma+E kappa-(1-Gamma)(q-v)
             -E log q/(N log N).

The first two correction terms together are nonnegative by (2). The last term is strictly positive because q<1. This proves (3), with no asymptotic loss and in every dimension d>=1.

If v=1 and Q=B, the condition forces B to be the same simplex Q, and the usual canonical-fan bound is Gamma. No positive surplus is asserted in that case.

## 5. How a full-rank positive fan defines Q

Let f_1,...,f_N be affine functions whose gradients span the dual d-dimensional space, and suppose there are coefficients theta_j>0 such that

    sum_j theta_j grad(f_j)=0.

Put m_j=min_B f_j, which exists by compactness. The affine function

    D=sum_j theta_j(f_j-m_j)

has zero gradient and hence is constant. It is positive: at any interior point of B, every nonconstant f_j exceeds its minimum. Full rank together with a positive relation among N=d+1 gradients implies that none is zero and that their only linear relation is a scalar multiple of this positive relation.

Define

    lambda_j=theta_j(f_j-m_j)/D.

They sum to 1, their gradient map has rank d, and they are nonnegative on B. Thus

    Q={x:lambda_j(x)>=0 for every j}

is a bounded d-simplex containing B; the affine map x->(lambda_1(x),...,lambda_N(x)) identifies its affine hull with the hyperplane sum_j lambda_j=1. Each facet touches B by the definition of m_j. The cap {f_j>=f_j(y)} is exactly {lambda_j>=lambda_j(y)}.

Consequently the theorem applies to any such positively balanced full-rank d+1 fan whose associated circumscribed simplex has the required volume bound. If every fan score is at most Gamma, it necessarily has

    |Q\B|/V > [kappa/(1-Gamma)](1-v)                (7)

when v<1. This is a necessary geometric condition for a bad fan, not a proof that such a fan is impossible.

Fans of lower rank or with more members require a separate reduction; none is silently assumed here. The theorem does not convert simplex capacity into ordinary retained volume or remove the source-simplex assumption.
