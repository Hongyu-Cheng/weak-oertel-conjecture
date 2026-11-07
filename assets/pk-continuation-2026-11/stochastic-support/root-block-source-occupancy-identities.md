# Root-block covariance and source occupancy

This supporting note concerns simplices formed from the one-root vertices
of a stochastic retained cone. It supplies exact overlap-safe identities
and upper bounds. It does not assert the proposed mean-cap bridge or any
sharp all-fan score theorem.

Let N=k+r, with k>=1 and r>=1. Let Lambda be an invertible N-by-N
barycentric vertex matrix whose columns have the form

    lambda^l=X_l(h_l,e_(r_l)),
    X_l=1/(1+sum_j(h_l)_j)>0,
    h_l in R_+^k,  r_l in {1,...,r}.                         (1)

This includes every maximum-volume simplex whose vertices come from a
strictly positive stochastic cone with k missed rows and r surviving
roots. Write rho=|det Lambda|. Every root occurs, since otherwise its
row in Lambda would be zero. Let C_s={l:r_l=s}, n_s=|C_s|>=1.

## 1. Exact unweighted root covariance

Define hbar_s=n_s^(-1)sum_(l in C_s)h_l and

    V=sum_s sum_(l in C_s)(h_l-hbar_s)(h_l-hbar_s)^T.

Then

    rho^2=(product_l X_l^2)(product_s n_s) det V.             (2)

To prove this, divide each column by X_l and write the resulting matrix
as [H;C], where C is the root-incidence matrix. Then CC^T=diag(n_s).
The Schur complement of this positive definite block in
[H;C][H;C]^T is exactly V. Taking determinants gives(2).

In particular V must have rank k. Support occurrence alone is
insufficient: the h-vectors must vary in k independent directions WITHIN
their root groups. The trace bound gives

    rho^2<=(product_l X_l^2)(product_s n_s)
                  [sum_s sum_(l in C_s)||h_l-hbar_s||_2^2/k]^k. (3)

If a root occurs only once, changing that column's h_l to zero leaves V
and all n_s unchanged and raises X_l to1. Thus whenever the pure root is
an allowed vertex, a maximum-volume simplex must use the pure root for
each singleton root group. This is strict if its old h_l was nonzero.

## 2. Exact covariance with the normalization retained

The factors X_l can instead remain in the covariance. Put

    s_a=sum_(l in C_a)X_l^2,
    htilde_a=s_a^(-1)sum_(l in C_a)X_l^2 h_l,
    W_*=sum_a sum_(l in C_a)
                 X_l^2(h_l-htilde_a)(h_l-htilde_a)^T.

Then the alternative exact identity is

    rho^2=(product_a s_a) det W_*.                           (4)

This is the Schur complement of the root block of Lambda Lambda^T,
whose root Gram matrix is diag(s_a). It does not discard normalization
loss from large supports.

Let G be any positive definite k-by-k matrix, and choose arbitrary
centers a_s in R^k for each root. Centering at the weighted mean minimizes
the sum of quadratic deviations, so

    tr(G W_*)
       <=sum_l X_l^2(h_l-a_(r_l))^T G(h_l-a_(r_l))=:Q_G.

The eigenvalue arithmetic-geometric mean inequality applied to
G^(1/2)W_*G^(1/2) proves

    rho^2 <= (product_s s_s)/det G * (Q_G/k)^k.               (5)

All group sizes, weights, centers, and repeated support incidences remain
explicit in(4)-(5).

A convenient finite ellipsoid certificate follows. Suppose positive
numbers alpha_s and centers a_s satisfy, for every AVAILABLE retained-
cone vertex X(h,e_s),

    X^2[alpha_s+(h-a_s)^T G(h-a_s)]<=1.                      (6)

Then every source simplex in the cone has capacity at most

    (det G product_s alpha_s)^(-1/2).                        (7)

Indeed the block triangular linear map

    (y,x) -> (G^(1/2)(y-Ax), diag(sqrt(alpha_s))x)

has determinant magnitude sqrt(det G product alpha_s), and(6) bounds
the norm of every transformed vertex by1. The squared norm is convex,
so the bound extends to the polytope. Hadamard proves(7).
This is a valid route for exact rational quadratic certificates; it is
not asserted that a useful certificate always exists for the mean-cap
threshold. Formula(5) can also be used without the uniform bound(6).

## 3. Quantitative nonroot coordinate occupancy

Let mu_j=sum_l Lambda_jl, and let M=sum_(j in missed rows)mu_j.
Every mu_j is positive. Row normalization gives a nonnegative matrix
with row sums1, hence row Euclidean norms at most1. Hadamard yields

    rho<=product_(j=1)^N mu_j
       <=(M/k)^k[(N-M)/r]^r.                                (8)

The second inequality is arithmetic-geometric mean within the two row
blocks. In particular,

    M>=k rho^(1/k)(r/N)^(r/k)>0.                            (9)

The sharper implicit bound in(8) may be used when M<k, because its right
side is strictly increasing on0<M<k. Thus a positive-volume source
cannot put all its coordinate mass in root directions. This occupancy
constraint alone does not control how different sources reuse rows.

Equations(2), (4), and(8) are exact geometric constraints absent from a
relaxation that retains only the largest individual vertex norms. A
proof that they force the desired general mean-cap or sharp fan bound
has not been obtained here.

## 4. Exact ellipsoid certificates for five stress configurations

The file `stress-cone-rational-ellipsoids.json` gives five explicit rational
stochastic matrices of sizes N=6,7,8,9,10 and one indicated surviving-root
set R for each. These are rationalized versions of numerical stress
examples; the assertions here concern the rational matrices in that JSON,
not unspecified numerical approximations. All matrix entries and all
ellipsoid coefficients have denominator10^6.

For each matrix, the JSON also gives a symmetric rational N-by-N matrix Q
such that

    Q is positive definite,
    v(r,A)^T Q v(r,A)<=1 for EVERY retained-cone vertex,
    det Q>4^(N-1).                                         (10)

The exact counts are:

| N | Surviving roots R, one-based | All cone vertices checked |
|---:|---|---:|
| 6 | {5,1} | 32 |
| 7 | {1,5} | 64 |
| 8 | {4,5} | 128 |
| 9 | {2,7} | 256 |
| 10 | {1,5,3} | 384 |

These are general enclosing ellipsoids; they need not have the restricted
block form of(6). Positive definiteness makes the quadratic function
convex, so its bound extends from the listed vertices to their entire
retained polytope. Applying Hadamard to Q^(1/2) times a simplex vertex
matrix gives

    capacity(K_J)<=1/sqrt(det Q)<2^(-(N-1)).                 (11)

Thus each indicated source pattern is impossible for a simplex source
of absolute volume at least2^(-(N-1))V inside an ambient simplex of
volume at most V.

`check_stress_cone_ellipsoids.py` verifies(10) using only exact Fraction
arithmetic: positive pivots of rational symmetric elimination establish
positive definiteness and its exact determinant; the complete vertex
formula checks all864 vertices and their quadratic forms. No numerical
square root, eigensolver, optimizer, or tolerance enters verification.
The report is `audit-stress-cone-rational-ellipsoids.json`.

The proposed mean-cap threshold referred to here is

    [mean_j p_j-|R|/N]/[2^d(Gamma_d-|R|/N)],

under the condition |R|/N<Gamma_d, with d=N-1 and
p_j=product_(l!=j)(1+P_jl)^(-1). For these five matrices it is at least
2^(-d), because mean_j p_j>=Gamma_d. The certified bound(11) therefore
falls below it in these examples. The general proposed bridge is FALSE:
`actual-mean-cap-capacity-bridge-obstruction.md` supplies a different
strictly positive rational matrix and an actual retained simplex above
that threshold. The exact covariance identities and these five finite
certificates do not rely on the false general bridge.
