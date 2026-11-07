# A nested root-retention functional for actual halfspace depth

Status: proposed new lemma and finite functional, not an accepted result. This gives a proved all-dimensional consumer and a strict improvement on the cutoff-by-cutoff hitting consumer. It does not assert the missing global dyadic lower bound for the new functional, and does not resolve OC. The ordinary centroid form cannot by itself prove unrestricted sharp OC, because restriction to original fiber centroids is already obstructed elsewhere.

## 1. Setup

Let n>=0 and d>=1, let C be a convex body in R^n x R^d, and assume W=sum_{i in Z^n}|C_i|>0. Let D={i: w_i=|C_i|>0}; this is finite and nonempty. Use the original mixed measure mu_C, supported on S=C intersect (Z^n x R^d). Let h_S(y) be its raw depth against every containing closed ambient halfspace. Write

    gamma=(d/(d+1))^d, q=1-gamma, ell=-log q.

Fix j in D. Let E_j be the finite family of nonempty affinely independent subsets E of D such that j lies in the relative interior of conv(E). For E in E_j, let lambda_{E,i}>0 be the unique barycentric coefficients of j and define

    L_E=log[w_j/(sum_{i in E}lambda_{E,i} w_i^(1/d))^d].   (1)

Convexity and Brunn--Minkowski give L_E>=0. The singleton {j} belongs to E_j and has cost zero. This is the same support/cost family as accepted fact 7fa5a28fe1ac6893; no fractional source capacities are introduced.

For 0<=t<=1 define the finite *nested retention loss*

    Phi_j(t)=min sum_{i in D} w_i(1-rho_i),                (2)

where the minimum is over rho in [0,1]^D satisfying

    min_{i in E} rho_i <= min(1,t exp(L_E))
                          for every E in E_j.            (3)

The min in (3) is a minimum of scalar coordinates, not a barycentric mean. This is a finite, generally nonconvex optimization problem. It is defined from the original actual weight table.

Also retain the integral hitting profile

    m_j(L)=min{sum_{i in F}w_i : F subset D,
          F meets every E in E_j with L_E<=L}, L>=0.       (4)

## 2. Finite attainment and an exact combinatorial formula

Every Phi_j(t) is attained: (3) gives a closed subset of the compact cube, and rho=0 is feasible. Equivalently, assign to every E in E_j one witness sigma(E) in E, and put

    a_i(sigma)=min{L_E:sigma(E)=i},

with a_i=+infinity if no support is assigned to i. Then

    Phi_j(t)=min_sigma sum_i w_i (1-t exp(a_i(sigma)))_+,  (5)

where an unassigned index contributes zero (including t=0, for which its contribution is defined to be zero). For every assigned index the exponential is finite. Indeed, (3) is the union over the finitely many assignments of the boxes rho_i<=min(1,t exp(a_i)). In each box the minimum loss sets every rho_i to its largest allowed value. This proves (5).

In particular Phi_j is continuous, nonincreasing, and piecewise affine on [0,1]. Its possible breakpoints come from the finite lower envelope in (5), including intersections of affine pieces. Since the singleton forces a_j=0, the target's contribution is exactly (1-t)w_j in every box. We have

    (1-t)w_j <= Phi_j(t) <= (1-t)m_j(infinity),
    Phi_j(1)=0, Phi_j(0)=m_j(infinity).                   (6)

Here m_j(infinity) is the minimum hitting mass of the full finite family. For the upper bound choose a minimum full hitting set F, put rho_i=t on F and rho_i=1 elsewhere. Then each support contains an i with rho_i=t<=t exp(L_E). The endpoint t=0 is exactly the full hitting-set problem: a feasible vector has at least one zero coordinate in each support, and all positive coordinates may be raised to one without increasing loss or losing feasibility.

## 3. Exact loss inequality for every actual convex remainder

Let K subset C be compact and convex, with |K_j|<=t w_j, where 0<t<=1. Then

    mu_C(C\K)=sum_i(w_i-|K_i|) >= Phi_j(t).               (7)

Only the fiber-volume sum is meant on the left; lower-dimensional fibers have zero d-volume. Put rho_i=|K_i|/w_i. If (3) failed for one E, then t exp(L_E)<1 and every rho_i on E would be strictly larger than t exp(L_E), hence positive. Thus all K_i for i in E are nonempty full-dimensional d-bodies. Convexity gives sum_i lambda_i K_i subset K_j, and Brunn--Minkowski yields

    |K_j|^(1/d)
      >=sum_i lambda_i |K_i|^(1/d)
      >(t exp(L_E))^(1/d) sum_i lambda_i w_i^(1/d)
       =t^(1/d) w_j^(1/d),

contrary to the target-volume bound. Therefore rho is feasible in (2), proving (7).

This argument does NOT silently use Brunn--Minkowski on empty fibers. The contradiction explicitly gives positive volume to every source on the chosen support. No source outside E is needed.

## 4. A deterministic centroid bound and a cut-search bound

Let c_j be the ordinary centroid of C_j. Then

    h_S((j,c_j)) >= Phi_j(q).                             (8)

More generally,

    max_{x in C_j} h_S((j,x))
           >= sup_{k>=1} Phi_j(q^k)/k.                   (9)

The maximizing point in the left side exists and belongs to the original target fiber. Equation (9) asserts existence of one point for each resulting numerical guarantee, not a distribution or an adaptive choice after seeing the final halfspace.

### Vertical halfspaces

A closed base halfspace through j meets every E in E_j: a positively weighted average of strictly negative base scores cannot equal zero. Its source weight is therefore at least m_j(infinity). This lower bound applies to every vertical ambient halfspace containing any point over j. By (6), this mass is at least Phi_j(t), for every t.

### Proof of (8)

Move any containing halfspace parallel until its boundary contains (j,c_j). If its continuous normal is zero, use the vertical observation. Otherwise its boundary has zero d-volume in every fiber, hence zero mixed volume. Intersect C with its opposite closed halfspace to form K. Ordinary centroid Grünbaum gives |K_j|<=(1-gamma)w_j=q w_j. Equation (7) shows that the removed mass, which equals the original cap mass because the boundary is null, is at least Phi_j(q). This proves (8) for every orientation.

### Attainment of the fiberwise maximum

For a fixed unit ambient normal u, the closed cap mass at a point y is upper semicontinuous: for y_l->y the pointwise upper limit of the cap indicators is at most the indicator of the closed cap through y, and reverse Fatou applies to the finite measure. The depth is the infimum over normals of these upper semicontinuous functions, hence is upper semicontinuous. Its restriction to compact C_j attains a maximum. This proof retains vertical boundary mass.

### Proof of (9)

Fix k>=1 and suppose the attained fiberwise maximum is smaller than Phi_j(q^k)/k. Choose delta strictly between them. Since Phi_j(q^k)<=m_j(infinity), delta<m_j(infinity). Start with C^0=C. At stage s, select the true centroid c_s of the current positive target fiber C^s_j. This is still a point of the original C_j, so there exists a closed ambient cap of original measure less than delta containing (j,c_s). Shift it to pass through that point. The vertical observation forces its continuous normal to be nonzero. Keep the opposite closed halfspace to form C^{s+1}.

Ordinary Grünbaum on the current target fiber gives

    gamma |C^s_j| <= |C^{s+1}_j| <= q |C^s_j|.

Thus every target fiber remains positive, and |C^k_j|<=q^k w_j. Every remainder is compact and convex. In fact it is full-dimensional: the retained strict side contains a target-fiber point; a convex combination with an interior point of the preceding body, sufficiently close to that retained point, is an ambient interior point on the retained strict side. At most delta original mixed mass is removed at each stage, so

    mu_C(C\C^k)<k delta<Phi_j(q^k).

This contradicts (7). Equation (9) follows for each k and then for the supremum. The left-side maximum is one fixed attained number, so no exchange of selected points and infinitely many k is required.

## 5. The whole hitting profile contributes simultaneously

For 0<t<=1,

    Phi_j(t) >= t integral_0^log(1/t) exp(L) m_j(L) dL.    (10)

Proof. Take any feasible rho. The elementary layer-cake identity gives

    sum_i w_i(1-rho_i)
       =integral_0^1 sum_{i:rho_i<theta}w_i dtheta.

For theta>t, the set {i:rho_i<theta} meets every E with L_E<log(theta/t), by (3). Its weight is at least the left limit m_j(log(theta/t)-). The profile has only finitely many jumps, so the left limit and the function itself have the same integral. Discard theta in [0,t], integrate, and substitute theta=t exp(L). This proves (10), including exact boundary-cost ties.

Consequently

    h_S((j,c_j))
      >= q integral_0^ell exp(L)m_j(L)dL,                (11)

    max_{x in C_j}h_S((j,x))
      >=sup_{k>=1} [q^k/k]
               integral_0^{k ell} exp(L)m_j(L)dL.       (12)

For any fixed L>=0, monotonicity of m_j and the target's unavoidable contribution yield the more explicit bound

    Phi_j(t) >= (1-t)w_j
         +(1-t exp(L))_+ [m_j(L)-w_j].                  (13)

Indeed, apply (10) to m_j-w_j, which is nonnegative and nondecreasing, and integrate over [L,log(1/t)] when that interval is nonempty. This can be strictly stronger than the predecessor's single-cutoff expression (1-t exp(L))_+ m_j(L). The baseline own-fiber loss is paid separately rather than weakened to the cutoff's coefficient.

Equations (10)--(13) concern the ORIGINAL hitting profile. No minimum is interchanged with an integral. The potentially stronger Phi in (2) also retains compatibility of the hitting choices across all levels.

## 6. An actual exact example where the new consumer crosses the OC target

Take n=d=1 and

    C={(z,x):-1<=z<=1, 0<=x<=3/2-|z|/2}.

This is a convex body with exactly three positive integer fibers, of lengths 1,3/2,1 at -1,0,1. Its total mass is W=7/2, and the sharp OC target is W/4=7/8.

At target j=0 there are precisely two supports: {0} with cost zero and {-1,1} with cost log(3/2). Thus

    m_0(L)=3/2 if 0<=L<log(3/2),
           5/2 if L>=log(3/2),

and the exact finite program (2) gives

    Phi_0(t)=(3/2)(1-t)+(1-(3/2)t)_+.

For t=q=1/2, Phi_0(q)=1. The new bound proves raw depth at least 1 at the actual middle centroid (0,3/4), strictly above 7/8.

In contrast, optimize the old 7fa5a28fe1ac6893 first bound over every target, cutoff L, and integer k. At the exposed targets it is at most 1/2. At j=0 the only relevant cutoffs are 0 and log(3/2), giving

    max{(3/2)(1-2^{-k})/k,
        (5/2)(1-(3/2)2^{-k})_+/k}.

For k=1 the value is 3/4; for k=2 it is 25/32; for k=3 it is 65/96; for k>=4 it is at most (5/2)/4=5/8. Therefore the optimized old bound is exactly 25/32<7/8. This is a strict improvement of a certificate on a rigorously realized table, not numerical evidence or a new claim about the general n=d=1 theorem.

## 7. Sharp product calibration and scope

For C=[0,1]^n x K, every positive base is a vertex of the cube, so each E_j contains only the singleton {j}. Then Phi_j(t)=(1-t)|K|. Since (1-q^k)/k<=1-q=gamma, (9) gives exactly gamma|K|, or normalized gamma/2^n. If K is a simplex, this agrees with the exact sharp depth. Thus no factor loss is built into this consumer at the required extremal product example.

The new finite invariant is

    R_nested(C)=max_{j in D} sup_{k>=1} Phi_j(q^k)/k,

and the proved conclusion is h_max(C)>=R_nested(C). Its definition uses the entire original volume table and the dimension d. It is neither the fractional packing score nor exponential capacity nor the cutoff hitting score. No global lower bound R_nested(C)>=gamma 2^{-n}W (or a universal weak counterpart) is asserted. Establishing such a bound, or proving an exact obstruction to it, is a separate research problem. Zero mixed d-volume and intrinsic q<d are outside this note's positive-volume hypothesis; ordinary n=0 is included and reduces to classical Grünbaum.

## 8. Novelty check

A local lexical and statement search of the shared candidate graph found the cutoff consumer in accepted 7fa5a28fe1ac6893 and related root-cost/log-cost scores, but no nested-retention program or integrated hitting-profile consumer. This is a mathematical novelty check within the available records, not a claim of literature priority. The proof of (9) deliberately uses the predecessor's sound centroid-cut mechanism; the new ingredient is the simultaneous remainder-loss inequality (7), with the full finite program and layer-cake consequence.

## 9. Exact limitations and the new two-step mechanism

For d=2 and the three-site table (s,1,s), the central program is Phi_0(t)=1-t+(s-t)_+, and both outer programs are Phi_{+-1}(t)=s(1-t). These are actual tables: take a triangle T of area one containing the origin and form the convex hull of (-1,sqrt(s)T),(0,T),(1,sqrt(s)T). The midpoint endpoint section sqrt(s)T is contained in T, so these are exactly its integer fibers.

At s=5/9=q, the original two-cut term gives

    Phi_0(q^2)/2=38/81=gamma_2(1+2s)/2.

This is the exact table of the archived original-fiber-centroid obstruction8dd62757ee4f1859. The new finite-cut consumer therefore certifies its target although the ordinary original fiber-centroid restriction fails.

However the global sharp inequality for the ORIGINAL q^k-based R_nested is false. Choose s=19/36. Then

    W=37/18, sharp target=37/81=296/648,
    Phi_0(q)/1=4/9=288/648,
    Phi_0(q^2)/2=295/648.

For k=3, q^3=125/729>1/6, so Phi_0(q^3)/3<43/108=258/648. For k>=4 it is at most (1+s)/k<=55/144<295/648. The exposed target programs optimize at gamma_2 s=19/81<295/648. Thus R_nested is exactly295/648, strictly below the sharp target296/648. This is a certified counterexample to that stronger scalar bridge, not to OC and not to the remainder-loss or consumer lemmas.

The separate note `uniform-two-centroid-cut-gap.md` proves a new mechanism: for each fixed d>=2, two consecutive centroid cuts contract by c_d<(1-gamma_d)^2 uniformly over all bodies and cut directions. It replaces q^k in the consumer by c_d^floor(k/2) q^(k mod2), while leaving Phi unchanged. The proof uses compactness and classical single-cap equality: a first equality remainder is a proper pyramid frustum, which cannot itself be any equality pyramid. This strictly improves the old consumer and reopens the route; it does not yet prove the global scalar bridge, nor establish enough quantitative gap to decide the displayed s=19/36 example by that new bound alone.
