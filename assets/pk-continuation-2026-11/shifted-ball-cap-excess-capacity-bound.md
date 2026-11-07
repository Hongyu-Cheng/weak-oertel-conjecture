# An overlap-free cap-excess bound for stochastic sign-cone capacity

This is a geometric capacity theorem for a fixed stochastic sign cone.
It connects ordinary vertex-cap fractions to the largest possible
retained simplex. It does not assert an all-fan score bound or resolve
Oertel's conjecture.

## 1. Statement

Let d>=2, N=d+1, and let P be an N-by-N row-stochastic matrix with
P_jj=0 and P_jr>0 for all j!=r. Let J be a nonempty proper subset of
{1,...,N}, put k=|J| and R=J^c, and define

    Delta={lambda>=0:sum lambda_j=1},
    K_J={lambda in Delta:lambda_j<=(P lambda)_j, j in J},
    p_j=product_(l!=j)(1+P_jl)^(-1),
    Gamma_k=(k/(k+1))^k,
    c_j=max(0,log(Gamma_k/p_j)), j in J.                     (1)

For arbitrary offsets 0<=b_j<=c_j/2 put B_*=sum_(j in J)b_j and

    Phi(b)=1-[2B_*+B_*^2-N sum_j b_j^2]/d.                  (2)

Then Phi(b)>0, and every d-simplex Q contained in K_J satisfies

    |Q|/|Delta| <=2^(-k) Phi(b)^(d/2).                       (3)

The volume ratio uses the d-dimensional Euclidean measure on the
barycentric hyperplane; it is unchanged under an affine identification
with any ordinary d-simplex. If at least one c_j is positive, an allowed
choice of b gives Phi(b)<1, hence a strict improvement on2^(-k).

There is no sum over sources or repeated support incidences in (3).
All row quantities p_j in (1) refer to the same original stochastic fan.

## 2. The vertex inequality extends to the whole cone

Let H=(I-P_JJ)^(-1)P_JR and use the unweighted map

    T_0(y_J,x_R)=(2y,x-H^T y),  det T_0=2^k.                 (4)

This map preserves the coordinate sum. The stochastic capacity norm
lemma gives ||T_0 lambda||_2<=1 on K_J.

We claim the stronger convex inequality

    ||T_0 lambda||_2^2+2sum_(j in J)c_j lambda_j<=1
       for EVERY lambda in K_J.                            (5)

To prove it, first consider a vertex of K_J. The finite-vertex lemma
shows that it has one surviving root r in R and a support A subset J.
Write a=|A|. Pure root vertices have T_0 e_r=e_r and zero additional
term, so (5) is equality there. Otherwise let X=lambda_r and
u_j=lambda_j/X for j in A. Absorption implies 0<u_j<=1 and
X=1/(1+sum_A u_j)>=1/(a+1). Define the original row escape masses

    e_j=sum_(l outside A union {r})P_jl.

The original sign constraints imply u_j<=1-e_j. To see the needed norm
defect directly, put x=Xe_r, z=H^T y, and Y=sum y. Then

    1-||T_0 lambda||_2^2
      =2XY-4||y||_2^2+2x dot z+Y^2-||z||_2^2
      >=2XY-2||y||_2^2
      =2X^2 sum_A u_j(1-u_j),

because x dot z=y dot Hx>=||y||_2^2 and ||z||_2<=Y. Therefore

    1-||T_0 lambda||_2^2
       >=2X^2 sum_A u_j e_j.                                (6)

The grouped ordinary-cap inequality proved in the escape/cap note is

    e_j>=(a+1)max(0,log(Gamma_a/p_j)).                       (7)

For completeness, if a<d, grouping the a within-support and d-a outside
entries in row j by arithmetic-geometric mean gives

    log(p_j/Gamma_a)
      >=-a log(1-e_j/(a+1))
          -(d-a)log(1+e_j/(d-a))
      >=-e_j/(a+1).

Combining this with e_j>=0 proves (7). If a=d, e_j=0 and p_j>=Gamma_d
by ordinary arithmetic-geometric mean, so (7) still holds.
The sequence Gamma_a decreases with a>=1: differentiating the continuous
extension a log(a/(a+1)) gives
-log(1+1/a)+1/(a+1)<0. Consequently a<=k implies
max(0,log(Gamma_a/p_j))>=c_j. Equations(6)-(7) yield

    1-||T_0 lambda||_2^2
       >=2X^2(a+1)sum_A u_j c_j
       =2X(a+1)sum_A lambda_j c_j
       >=2sum_A lambda_j c_j.

This proves (5) on all vertices. Its left side is a convex quadratic
function of lambda. Every point of the polytope is a convex combination
of its vertices, so (5) holds throughout K_J. This is the step that
removes any need to sum overlapping source-vertex charges.

## 3. A determinant bound in a hyperplane section of a ball

Let q_1,...,q_N be vectors in R^N with

    sum_j(q_l)_j=s>0,  ||q_l||_2^2<=R_0^2 for every l.

Then, with d=N-1,

    |det[q_1 ... q_N]|
       <=s [(N R_0^2-s^2)/d]^(d/2).                         (8)

The quantity in brackets is nonnegative by Cauchy-Schwarz.
To prove (8), make an orthogonal row change whose first row is
N^(-1/2)(1,...,1). The first row of the resulting matrix is
(s/sqrt(N),...,s/sqrt(N)). Next make an orthogonal column change whose
first column is N^(-1/2)(1,...,1). The result has block form

    [ s  0 ]
    [ z  Z ],

where Z is d-by-d. Orthogonal changes preserve determinant magnitude
and the sum of squared entries. Hence

    ||Z||_F^2<=sum_l||q_l||_2^2-s^2<=N R_0^2-s^2.

The arithmetic-geometric mean inequality applied to the nonnegative
eigenvalues of Z Z^T gives

    |det Z|<= (||Z||_F^2/d)^(d/2).

Multiplying by s proves (8), including singular Z by continuity or the
same eigenvalue inequality. This is a proof of the needed determinant
bound, rather than an appeal to an unspecified optimal simplex theorem.

## 4. Shift, apply the determinant bound, and cancel the column sum

Extend b by zero in the R coordinates, writing this vector as b_tilde.
Since the J coordinates of T_0 lambda are 2lambda_j, (5) and
0<=b_j<=c_j/2 give

    ||T_0 lambda+b_tilde||_2^2
      =||T_0 lambda||_2^2+4sum_j b_j lambda_j+||b||_2^2
      <=1+||b||_2^2.                                       (9)

The shifted vector has coordinate sum s=1+B_*. On the hyperplane
sum lambda=1, this affine map is the restriction of the linear map

    S=T_0+b_tilde 1^T.

The determinant identity for a rank-one update gives

    det S=det T_0 [1+1^T T_0^(-1)b_tilde]
         =2^k(1+B_*),                                      (10)

because T_0 preserves coordinate sum. In particular S is invertible.
Apply (8) to the image columns of a simplex vertex matrix Lambda. With
R_0^2=1+||b||_2^2 and s=1+B_*, (9)-(10) give

    2^k(1+B_*)|det Lambda|
       <=(1+B_*)
          [(N(1+||b||_2^2)-(1+B_*)^2)/d]^(d/2).

The bracket equals Phi(b). Cancelling the positive factor1+B_* proves
(3). Moreover K_J has nonempty relative interior: for any r in R, a
small mixture of the uniform vector with e_r has positive coordinates
and all J inequalities strict. Its invertible image under S has positive
d-dimensional volume, so the enclosing hyperplane ball in (9) has
positive radius. Therefore Phi(b)>0, as claimed.

Finally, if c_j>0 for some j, choose only b_j=t>0 and take t small enough
that t<=c_j/2 and dt<2. Then

    2B_*+B_*^2-N||b||_2^2=2t-dt^2>0,

so Phi(b)<1. This improvement is exact, but no universal quantitative
surplus is claimed when the cap excess information vanishes.

## 5. The best offset is a one-variable threshold

The smallest right side obtainable from (3) is determined without an
optimization oracle. Let a_j=c_j/2. There is a unique t>0 satisfying

    N t=1+sum_(j in J)min(a_j,t).                            (11)

Indeed the difference between the left and right sides is continuous,
strictly increasing with slope at least N-k>0, negative at0, and tends
to infinity. The unique minimizing offset is

    b_j=min(a_j,t).                                         (12)

To check this, minimizing Phi is equivalent to minimizing the strictly
convex quadratic

    N sum b_j^2-(sum b_j)^2-2sum b_j

on 0<=b_j<=a_j. Its Hessian is positive definite because k<N.
At any unconstrained coordinate the derivative vanishes precisely when
N b_j=1+B_*; at an upper-bound coordinate the derivative is nonpositive
precisely when a_j<=t. These are exactly (11)-(12), including a_j=0.
Thus the elementary first-order conditions prove the global minimum.

Equations(3), (11), and(12) constitute a row-cap-dependent geometric
capacity bound. They do not establish that the resulting finite pattern
constraints force a sharp score for every fan.
