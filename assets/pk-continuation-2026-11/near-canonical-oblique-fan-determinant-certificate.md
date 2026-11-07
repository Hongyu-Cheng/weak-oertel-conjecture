# A quantitative determinant certificate for nearby oblique simplex cap fans

This is a finite-direction auxiliary theorem for the strict-hitting model. It does not select a point deep for every halfspace and does not assert a global reduction of Oertel's conjecture to nearby canonical normals. The proof is self-contained apart from elementary Hadamard, Jensen, and the exact simplex cap-volume formula.

## 1. Data and statement

Fix d>=2, put N=d+1 and Gamma=(d/(d+1))^d, and define

    kappa=1/2-Gamma>0,
    rho=4^(-(d+1)),
    C_d=d+N/log N.

Let V>0. Let B be a d-simplex of volume vV with 0<v<1, and let P_i be finitely many inscribed d-simplices of volumes at least 2^(-d)V. Let e_i>=0 have sum E=1-v>0. Discard zero-weight sources. Write lambda_1,...,lambda_N for the barycentric affine functions of B. For an affine function f put

    osc_B(f)=max_B f-min_B f.

Choose affine functions f_1,...,f_N such that

    osc_B(f_j-lambda_j)<=eta,
    0<=eta<=min{rho, E*kappa/(2C_d)}.                 (1)

All f_j are nonconstant, since osc_B(lambda_j)=1 and eta<1. For y in B define their normalized closed-cap/strict-source scores

    Q_j(y)=|B intersect {f_j>=f_j(y)}|/V
       +sum_i e_i 1{max_(x in P_i) f_j(x)>f_j(y)}.

Then for EVERY y in B,

    max_j Q_j(y)>=Gamma+(E*kappa)/2>Gamma.           (2)

The cap can have any of the nearby oblique orientations in (1). Equality at a source support threshold is counted as a miss throughout.

There is also a positive-fan version. Let a finite collection of affine functions f_l have positive coefficients theta_l with sum_l theta_l grad(f_l)=0. Suppose each f_l satisfies (1) relative to at least one lambda_{j(l)}, with the same eta. Then some member of this collection has score at least the right side of (2), at every y in B. No restriction is imposed on the number of members or their repeated facet labels.

## 2. Elementary determinant estimates

For an inscribed source P let M be its N by N barycentric vertex matrix. It is nonnegative and column stochastic, and

    |det M|=|P|/|B|>=2^(-d)/v.                      (3)

Write r_j=max_l M_jl and s_j=sum_l M_jl. Hadamard and AM-GM give

    |det M|^2<=product_j sum_l M_jl^2
       <=product_j r_j s_j<=product_j r_j.

Every r_j<=1, so in particular

    r_j>=|det M|^2>=4^(-d)/v^2>=4^(-d).            (4)

A second bound can omit any designated row r. Replace that row by the sum of all rows, namely the all-ones row. Multilinearity shows that the determinant is unchanged. From every other row j subtract r_j/2 times the new row. Each such row has Euclidean norm at most sqrt(N) r_j/2, whereas the replaced row has norm sqrt(N). Thus

    |det M|<=N^(N/2) 2^(-d) product_(j!=r) r_j.      (5)

## 3. A source cannot miss all perturbed caps

Fix y and put u_j=lambda_j(y) and t_j=u_j+eta. If source P misses the strict cap associated to f_j, then for every x in P,

    lambda_j(x)-lambda_j(y)
      =f_j(x)-f_j(y)-[(f_j-lambda_j)(x)-(f_j-lambda_j)(y)]
      <=eta,

so r_j<=t_j.

If P missed all N perturbed caps, it would be contained in the affine simplex

    R={x in aff(B):lambda_j(x)<=t_j for every j}.

Indeed the nonnegative deficiencies t_j-lambda_j(x) sum to N eta. When eta>0 this is an inverted homothetic simplex of volume (N eta)^d |B|; when eta=0 it is a single point. Since N<=4^d, condition eta<=rho implies N eta<=1/4. Consequently

    |R|<=4^(-d)vV<2^(-d)V<=|P|,

a contradiction. Thus there is at least one HIT row r for every individual source.

Suppose now all 0<t_j<1, and put L_j=log(1/t_j). Let I be this source's missed indices, and choose a hit row r. Combining (3) and (5), and dropping factors at most one from hit rows other than r, gives

    1/(v N^(N/2))<=product_(j!=r) r_j
       <=product_(j in I) r_j<=product_(j in I) t_j.

Hence the full missed logarithmic weight obeys

    sum_(j in I) L_j <= (N/2)log N+log v
                      <= (N/2)log N.              (6)

The omitted row is hit, so no missed logarithm is lost. This is the part of the determinant estimate that preserves the factor 1/2 independently of d.

## 4. Points close to a simplex face

If u_j<=rho for some j, then t_j<=2rho=4^(-d)/2. By (4), every source has r_j>t_j and therefore strictly hits the perturbed f_j cap. Also

    {lambda_j>=u_j+eta} intersect B
       subset {f_j>=f_j(y)} intersect B.

The exact canonical cap formula and Bernoulli's inequality give

    Q_j(y)>=v(1-t_j)^d+E
       >=1-vd t_j>=1-2d rho.

For d>=1, d/4^d<=1/4, so 1-2d rho>=7/8. On the other hand Gamma<=1/2, E<=1, and kappa=1/2-Gamma imply Gamma+E kappa/2<=1/2. Thus (2) holds, with room to spare. This includes boundary points.

## 5. The interior logarithmic estimate

It remains to consider u_j>rho for every j. Since sum_j u_j=1, each u_j<1-d rho. Thus eta<=rho implies 0<t_j<1. Put S=sum_j L_j>0.

The own-cap inclusion used above and the d-Lipschitz property of s -> (1-s)_+^d give

    |B intersect {f_j>=f_j(y)}|/V
       >=v(1-u_j)^d-vd eta.                        (7)

The sequences L_j=log(1/(u_j+eta)) and (1-u_j)^d have the same ordering. Chebyshev's inequality, followed by Jensen, yields

    sum_j L_j(1-u_j)^d
       >=(S/N)sum_j(1-u_j)^d>=Gamma S.              (8)

For each source, (6) bounds its missed weight, hence its hit weight is at least S-(N/2)log N. Sum with weights e_i and combine with (7)-(8):

    sum_j L_j Q_j(y)
       >=v Gamma S-vd eta S+E[S-(N/2)log N].        (9)

Because sum_j t_j=1+N eta, Jensen gives

    S>=N log(N/(1+N eta))
      >=N log N-N^2 eta.

Set x=N eta/log N. We have eta<=rho<=1/(4N) and log N>1/2, so 0<=x<1/2. Therefore

    ((N/2)log N)/S <= 1/[2(1-x)] <= 1/2+x.

Divide (9) by S, use v=1-E, and bound the weighted mean by the maximum. This gives

    max_j Q_j(y)
       >=Gamma+E(1/2-Gamma)-eta[vd+E N/log N]
       >=Gamma+E kappa-C_d eta
       >=Gamma+E kappa/2,

which proves (2). The positivity kappa>0 for d>=2 follows, for example, because (d/(d+1))^d strictly decreases with d and Gamma_1=1/2.

## 6. Positive fan consequence and remaining cases

For the positive-fan statement, assign one allowed label j(l) to each f_l. Every label must occur among the positively weighted members. Indeed, if label m were absent, evaluate the balanced gradient relation on the vector from the centroid g_B to vertex v_m. For every j(l)!=m,

    f_l(v_m)-f_l(g_B)
       <=lambda_{j(l)}(v_m)-lambda_{j(l)}(g_B)+eta
       =-1/N+eta<0.

The weighted sum would be strictly negative, contradicting sum theta_l grad(f_l)=0. Select one member of each label and apply (2). This proves that a positively balanced fan consisting entirely of these neighborhoods cannot have all its cap scores below Gamma.

For E=0, v=1, the above tolerance formula requires eta=0 and the canonical cap argument gives max score>=Gamma. More generally any positively balanced cap fan through y has a cap containing the ordinary centroid of B; ordinary Grunbaum gives that cap at least Gamma |B|, so the positive-fan conclusion with no surplus holds without any closeness condition.

For d=1 and eta<1, the two affine forms close to the two barycentric coordinates have opposite orientations. Their own interval cap lengths sum to |B|, and every nondegenerate source interval strictly hits at least one. The two scores sum to at least v+E=1, proving max score>=Gamma_1=1/2. No positive kappa or uniform positive surplus is claimed from this elementary argument.

## 7. Scope

The proof quantifies a finite-fan stability statement in the true simplex-source model. Its tolerance is proportional to the available deficit E and its constants are explicit. It allows oblique normals, arbitrary source positions, arbitrary nonnegative source weights, all points y including boundary points, and exact strict-support boundary handling.

It does not prove that an arbitrary obstructing cap fan must be close to canonical normals. It does not replace nonsimplex partners by simplices, discard source volume, provide an actual mixed-integer center, or turn a maximum over a finite fan into an infimum over all halfspaces. Such a global geometric reduction remains a separate unproved assertion.

## 8. One deterministic center for the entire neighborhood

The positive-fan exclusion also supplies a single center for all the nearby orientations simultaneously. This consequence uses an attained continuous minimax problem, not attainment of the discontinuous full strict-hitting depth.

Keep d>=2, 0<v<1 and (1), and set

    T=Gamma+E*kappa/4.

Let F be the compact family of all affine functions f satisfying f(g_B)=1/N and osc_B(f-lambda_j)<=eta for at least one j. This family is compact because its values at the N vertices are uniformly bounded, and it contains no constant function because eta<1. Adding an affine constant does not affect a cap through a point, so this normalization loses no allowed orientation. Define

    Q_f(y)=|B intersect {f>=f(y)}|/V
       +sum_i e_i 1{max_(x in P_i)f(x)>f(y)}.

Then there is one deterministic y_* in B such that

    Q_f(y_*)>=T>Gamma     for every f in F.           (10)

The same holds for containing halfspaces with the same positive orientation, by monotonicity in the threshold. The conclusion concerns this entire neighborhood only.

### 8.1 Continuous good-threshold function

For a fixed f define the scalar score

    G_f(t)=|B intersect {f>=t}|/V
       +sum_i e_i 1{h_i(f)>t},
    h_i(f)=max_(x in P_i)f(x),
    r_T(f)=sup{t in R:G_f(t)>=T}.

Here 0<T<1. Since G_f(t)=1 below min_B f and is zero at max_B f, the threshold r_T is finite and lies in [min_B f,max_B f]; equality at the upper endpoint is possible because of a support jump. The function G_f is nonincreasing and right-continuous. Thus

    t<r_T(f) implies G_f(t)>=T,
    t>=r_T(f) implies G_f(t)<=T.                     (11)

For the second assertion at equality, if G_f(r_T)>T then right continuity gives a larger t with G_f(t)>=T, contradicting the supremum. A value below T at the threshold is possible and is not excluded.

The map f -> r_T(f) is continuous on F. Here is a direct finite formula proving this. For each subset J of the source indices put e_J=sum_(i in J)e_i and q_J=T-e_J. Omit J if q_J>v. For 0<q<=v let b_q(f) be the unique cap quantile with

    |B intersect {f>=b_q(f)}|/V=q;

at q=v take b_v(f)=min_B f. For q<=0 put b_q(f)=+infinity. Let h_J(f)=min_(i in J)h_i(f), with h_empty=+infinity. Then

    r_T(f)=max_(J:q_J<=v) min{h_J(f), b_(q_J)(f)}.   (12)

Every included term is finite: if J is empty then q_J=T>0; if q_J<=0 then J is nonempty. There is at least one included J because T<1=v+E.

To prove (12), every t strictly below a displayed minimum is strictly below all supports in J and has own cap at least q_J when q_J>0; hence G_f(t)>=T. Conversely, if G_f(t)>=T, take J to be its actual strict-hit set. Then t<h_J(f), and when q_J>0 the own-cap inequality implies t<=b_(q_J)(f). This proves equality of the suprema.

Support functions h_i are continuous in the affine coefficients. For every fixed 0<q<v, b_q(f) is continuous: cap volumes are jointly continuous in nonconstant f and t by dominated convergence, and are strictly decreasing between min_B f and max_B f because B is full dimensional. A convergent subsequence of bounded quantiles must therefore converge to the unique correct quantile. The endpoint q=v uses the continuous minimum support. The finite max/min formula now proves continuity of r_T, including all source-support jumps.

### 8.2 Attained minimax and its active normals

Consider the continuous convex function on compact B

    Phi(y)=max_(f in F)[f(y)-r_T(f)].

Let y_0 minimize Phi, and write alpha=Phi(y_0). Suppose alpha>=0. Every active f, meaning f(y_0)-r_T(f)=alpha, has by (11)

    Q_f(y_0)<=T.                                   (13)

The active set is compact and nonempty. At a minimum over B, zero lies in the sum of the convex hull of active gradients and the outward normal cone of B at y_0. Explicitly, there are finitely many active f_l, nonnegative weights theta_l summing to one, and nonnegative weights sigma_j for the zero-coordinate indices J={j:lambda_j(y_0)=0}, such that

    sum_l theta_l grad(f_l)
       +sum_(j in J) sigma_j[-grad(lambda_j)]=0.     (14)

For completeness, this first-order certificate follows by separation. The sum of the compact convex hull of active gradients and the finitely generated normal cone is closed. If it did not contain zero, separation would give a vector h with every active gradient having strictly negative scalar product with h and every outward normal having nonpositive scalar product with h. Adding a sufficiently small positive multiple of g_B-y_0 preserves strict negativity on the active gradients and makes all boundary inequalities point inward. For a sufficiently small step in this direction the point remains in B. Compactness of F and continuity of the affine slopes show that near-active constraints still strictly decrease, while constraints with a fixed inactive gap remain below the previous maximum. This would decrease Phi, a contradiction. A finite convex combination in (14) exists by Caratheodory's theorem.

### 8.3 Boundary and interior contradictions

First suppose J is nonempty. It is a proper subset of {1,...,N}. If an active f had an admissible facet label j in J, Section 4 (using lambda_j(y_0)=0) would give Q_f(y_0)>=7/8>T, contradicting (13). Thus no active f admits a label in J. Assign every active f_l an allowed label outside J.

Let v_J be the barycenter of the vertices whose indices lie in J, and test (14) on h=v_J-g_B. For each active f_l labeled outside J,

    grad(f_l).h=f_l(v_J)-f_l(g_B)<=-1/N+eta<0.

For every boundary normal with j in J,

    -grad(lambda_j).h=-(1/|J|-1/N)<0.

All terms of (14) are nonpositive and at least the active convex-combination terms are strictly negative, a contradiction. Hence y_0 is interior.

Now (14) has no boundary normals. Remove its zero theta coefficients. The remaining active gradients form a positive fan, all in the prescribed neighborhoods. Section 6 gives an active cap score at least Gamma+E*kappa/2>T, again contradicting (13).

Therefore alpha<0. In particular f(y_0)<r_T(f) for every f in F, and (11) proves (10). To make the choice deterministic, minimize the first coordinate over the compact minimizer set of Phi, then the second, and so on. This selects one actual point of B. No maximum of the full strict-hitting depth was assumed to exist.

The construction does not make the neighborhood size independent of E. It also does not show that arbitrary oblique bad normals enter this neighborhood. Those remain genuinely additional geometric questions.
