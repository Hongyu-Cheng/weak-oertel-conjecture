---
fact_id: 20a50fadbdf54b5a
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-nov6-actual-triangle-all-ratio-repair
depends_on: ["cba04fbe065c480a", "6769574fc1bd9f8d"]
verifier_run: b04335b83382453f
target_match: null
---

## Statement

Let pairwise distinct integer bases w,u_i,v_i satisfy u_i+v_i=2w. At these bases let B be a full planar triangle and A_i,C_i full planar compact convex bodies with (A_i+C_i)/2 contained in B. Suppose every C_i contains a triangle of area at least M, b=|B|<M, D=M-b, and 0<xi<=1/9. If |A_i|<=xi^2 D^2/(36M) individually and sum_i |A_i|>=(1-xi)D, then one deterministic point (w,y) with y in int B has raw star halfspace depth at least (4/9)M+(1-9xi)D/18 for all closed ambient halfspaces. The result has no incoming diameter restriction and proves uniform quadrature, attainment, actual oblique pair payments, and pure integer directions. At xi=1/18 the incoming threshold is17D/18 and the surplus isD/36.

## Proof

# Actual triangle-middle repair at every volume ratio by small reflected pairs

Research theorem, 6 November 2026. This is an actual mixed-integer reflected-star consequence of the all-direction planar triangle source-hitting theorem. It permits arbitrary ambient halfspace orientations and imposes no diameter or aspect-ratio condition on the incoming convex fibers. The middle fiber is required to be a triangle. It is not a theorem for arbitrary middle bodies or a complete proof of OC.

## 1. Statement and constants

Let n>=1. Let w,u_i,v_i in Z^n,1<=i<=k, be pairwise distinct, with

    u_i+v_i=2w.

At these bases place, respectively, a triangle B and full-dimensional compact convex bodies A_i,C_i in R^2, satisfying

    (A_i+C_i)/2 subset B.

Let b=|B|, a_i=|A_i|. Suppose each C_i contains a triangle Q_i with area c_i>=M>0. Assume b<M and put D=M-b>0. Fix

    0<xi<=1/9.

Suppose

    a_i <= xi^2 D^2/(36M) for every i,
    sum_i a_i >= (1-xi)D.                                  (1)

Then there is one deterministic y in int B such that every closed ambient halfspace containing(w,y) has, on this star alone, two-dimensional fiber-sum mass at least

    (4/9)M + (1-9xi)D/18.                                 (2)

Other fibers, if present, only increase this mass. For example xi=1/18 gives the explicit conditions and conclusion

    a_i<=D^2/(11664M),       sum_i a_i>=17D/18,
    mass >=(4/9)M+D/36.                                    (3)

If b>=M, the ordinary centroid of B already has through-halfspace mass at least(4/9)b>=(4/9)M on B alone; no incoming conditions are needed for that weaker target. The surplus in(2) is positive when b<M and xi<1/9. At xi=1/9 the exact conclusion is mass>=(4/9)M, requiring only sum_i a_i>=8D/9 and a_i<=D^2/(2916M).

## 2. Precise planar hitting input

We use the proved planar triangle source-hitting theorem in the following exact form. If B has area vV,0<v<1, and finitely many triangles P_j subset B have area at least V/4 and nonnegative weights e_j totaling1-v, then for every fixed0<eta<1/18 a point y in int B satisfies for every unit vector u

    |B intersect {x:u.x>=u.y}|/V
      +sum_j e_j 1{h_(P_j)(u)>u.y}
        >=4/9+eta(1-v).                                  (4)

The support comparison is strict. The theorem is obtained from the audited covering-pair certificates for all strict positive planar three-fan sign patterns and the audited continuous-threshold minimax interface, including zero vertex heights and boundary-center treatment. This note uses precisely(4), not a mixed-integer center statement. The threshold parameter is legitimate: in the minimax interface, active rows have scores at most4/9+eta(1-v), strictly below the universal fan bound4/9+(1-v)/18. Every other step of that proof is unchanged. Repository registration should cite that assembled theorem as its mathematical predecessor.

We next prove the continuum extension needed for actual incoming bodies, rather than replacing their mass by an unproved centroid surrogate.

## 3. Uniform halfspace quadrature and the continuum extension

For a compact convex set A with positive planar area, define

    omega_A(delta)=sup_(||u||=1,t real)
       |A intersect {p:|u.p-t|<=delta}|.

Then omega_A(delta) tends to0 as delta decreases to0. To prove this, contain A in a ball of radius R. A nonempty strip intersection with delta<=1 has |t|<=R+1. If the assertion failed, compactness would give a sequence of unit normals u_m converging to u, thresholds t_m converging to t, and widths delta_m tending to0, whose strip areas stay bounded below. At every p outside the line u.p=t, the strip indicators eventually vanish. That line has planar measure zero. Dominated convergence on the finite-area set A gives a contradiction.

Partition the plane into half-open squares of side epsilon. Only finitely many meet a fixed compact A. For every cell whose intersection with A has positive area, choose a point p_l in its closed intersection with A and assign weight w_l equal to its intersection area. Such a point exists; it may be selected lexicographically in the compact closed intersection. The closed and half-open intersections have the same area because grid lines have zero planar measure. All weights sum to|A|. For every unit u and real t,

    |sum_l w_l 1{u.p_l>t} - |A intersect {p:u.p>t}||
          <=omega_A(sqrt(2)epsilon).                           (5)

Indeed a disagreement between a representative and any point in its cell implies distance in the u-coordinate from t at most the cell diameter sqrt(2)epsilon. Integrating this elementary pointwise bound proves(5). No probabilistic sampling or bounded aspect ratio is involved.

Now let B be a triangle of area b<V. Let A_i be finitely many positive-area compact convex sets with sum_i|A_i|=V-b. Let T_i be fixed triangles such that, for every p in A_i,

    P_i(p)=(p+T_i)/2 subset B,
    |P_i(p)|>=V/4.

Define

    F(y,u)=|B intersect {x:u.x>=u.y}|
       +sum_i |{p in A_i:u.p+h_(T_i)(u)>2u.y}|.             (6)

This function is jointly continuous on B times the unit circle. For each incoming term, the threshold2u.y-h_(T_i)(u) is continuous; along any convergent sequence(y_m,u_m), its indicators converge at every p outside the limiting line. Dominated convergence applies because A_i has finite area. The own-cap term has the same argument. All normals in this parameter space are nonzero.

Apply the square quadrature to every A_i. Use the finite triangles P_i(p_l) with normalized weights w_l/V in(4). Their qualification and containment follow from the hypotheses, and their weights sum to(V-b)/V. Fix any0<eta<1/18. Thus for every mesh size epsilon there exists y_epsilon in B with the finite version of(6) at least

    T_eta=(4/9)V+eta(V-b)

for every unit direction. Equation(5), summed over the finitely many A_i, shows that the finite score differs from F uniformly in both y and u by a quantity tending to0.

For complete attainment details, joint continuity on compact B times the unit circle implies uniform continuity. Therefore the function

    d_F(y)=min_(||u||=1)F(y,u)

is continuous on B: the difference of two minima is at most sup_u|F(y,u)-F(y',u)|. The directional minimum is attained by compactness, and d_F has an attained maximum on B. The finite approximations imply max_B d_F>=T_eta by letting epsilon decrease to0. Since this holds for every eta<1/18, the same attained maximum satisfies

    max_B d_F >=T:=(4/9)V+(V-b)/18.                         (7)

This last limit is valid for the continuous integrated score; it is not an assumption that the discontinuous finite strict-hit score attains its limiting target. The set of maximizers is nonempty and compact. Successive minimization of its first and second Euclidean coordinates selects one deterministic y_*. No convexity of that maximizing set is needed for this selection.

Thus F(y_*,u)>=T for all unit u. This point is interior: at a boundary point an outward supporting direction gives zero own-cap area and no strict source hit, because every full-dimensional P_i(p) is contained in B. Hence F=0 in that direction, while T>0. This proves the required continuum form of(4), with exact constants and all support contacts included.

## 4. Clipping, shrinking, and source qualification

Put

    V=M-xiD,       theta=1-sqrt(V/M).

Then b<V<M, V-b=(1-xi)D, and

    theta>=xiD/(2M).                                      (8)

The last inequality is1-sqrt(1-t)>=t/2 for0<t<1. If the incoming total exceeds V-b, replace each A_i by its homothetic copy about its centroid with common linear ratio sqrt((V-b)/sum_i a_i). These are convex subsets of the actual incoming fibers, their midpoint inclusions persist, and their areas now sum to V-b. The per-pair bounds in(1) persist. A mass lower bound for these subsets implies the same bound for the original star. Denote the clipped bodies again by A_i and their areas by a_i.

Let g_i be the centroid of the inscribed partner triangle Q_i, and define

    T_i=g_i+(1-theta)(Q_i-g_i).

For every p in A_i, the triangle P_i(p)=(p+T_i)/2 lies in B, and

    |P_i(p)|=(1-theta)^2 c_i/4
             =(V/M)c_i/4>=V/4.                            (9)

All hypotheses of the continuum theorem in Section3 therefore hold. It produces y_* in int B for which(6) is at least T from(7), simultaneously in all directions.

## 5. Actual pair payment for every oblique ambient halfspace

Consider an ambient halfspace through(w,y_*) with nonzero continuous normal u; rescale positively so||u||=1. Let t_A,t_C be its thresholds in the fibers at u_i,v_i. The reflected integer relation gives exactly

    t_A+t_C=2u.y_*.

Write

    G_i={p in A_i:u.p+h_(T_i)(u)>2u.y_*}.

If every point of G_i belongs to the actual closed A_i cap, that cap has area at least|G_i|. Otherwise choose p in G_i with u.p<t_A. Then

    t_C<2u.y_*-u.p<h_(T_i)(u).                             (10)

Let h=max_(Q_i)u.x, m=min_(Q_i)u.x, and W=h-m>0. Since the triangle centroid is the mean of its three vertices,

    h-u.g_i>=W/3,
    h_(T_i)(u)<=h-theta W/3.

Choose a vertex z of Q_i attaining h. The triangle

    z+(theta/3)(Q_i-z)

lies in Q_i and in the actual C_i cap by(10); all its u-values are at least h-theta W/3>t_C. Its area is at least

    (theta/3)^2 c_i >=xi^2 D^2/(36M)>=a_i>=|G_i|,           (11)

using(8), c_i>=M, and(1). Thus in every case the actual pair contributes at least|G_i|. There is no assumption on the diameter, width, or shape of A_i. Pairwise distinct integer bases allow these lower bounds to be added without counting any fiber twice.

Adding the middle cap and all pair payments proves actual star mass at least T for every through-(w,y_*) ambient halfspace with nonzero continuous normal. Substituting V=M-xiD into(7) gives exactly

    T=(4/9)M+(1-9xi)D/18,

which is(2).

## 6. Pure integer directions and containing halfspaces

If the continuous normal is zero, the through-(w,y_*) halfspace contains the entire middle fiber. In each reflected pair at least one endpoint fiber is entirely included, because its two integer offsets are opposite. Each possible endpoint has area at least a_i: this is immediate for A_i and follows from|C_i|>=M>a_i for the partner, using(1). The total actual mass is therefore at least b+sum_i a_i=V. Since T=(4/9)V+(V-b)/18<V/2<V, it exceeds the claimed lower bound.

Finally every closed ambient halfspace containing(w,y_*) contains its parallel closed halfspace whose boundary passes through(w,y_*). Monotonicity transfers the bound to the original halfspace. This includes arbitrary integer-continuous coupling and all boundary masses.

The argument constructs one deterministic actual point(w,y_*) in the middle fiber. The only limiting step is the proved uniform quadrature argument inside compact fixed actual fibers; no lattice bases move and no fiber-sum is replaced by an integral over the integer projection. The conclusion remains a sufficient reflected-star theorem with a triangular middle fiber and the explicit per-pair smallness condition.
