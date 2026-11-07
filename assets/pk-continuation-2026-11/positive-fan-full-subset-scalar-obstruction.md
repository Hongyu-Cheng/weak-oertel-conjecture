# Exact positive-fan obstruction to all-subset scalar endpoint credits

Research draft, 6 November 2026. This refutes a specific scalar/atom relaxation of a three-fiber positive-cap fan. It is not an actual mixed-integer depth counterexample. The continuous middle fan and the fiber volume table are actual; the proposed outside atoms deliberately fail an additional geometric endpoint constraint proved in Section 4.

## 1. The precise relaxation

Let A,B,C be d-dimensional convex bodies at integer bases -1,0,1, with (A+C)/2 subset B. Normalize |B|=1 and write a=|A|<=c=|C|. Define

    F_(a,c)(s)=[a-(2s^(1/d)-c^(1/d))_+^d]_+.

For a finite positive circuit of through-y middle cap traces H_i, let c_i=|B intersect H_i| and, for nonempty J, let

    s_J=|B intersect intersection_(i in J) H_i^opp|.

Here H_i^opp is the opposite closed halfspace. Proper boundary planes have zero ordinary volume. Compatible convex remainders force at least F_(a,c)(s_J) endpoint mass to lie in the union of the original ambient caps indexed by J.

The strongest outside-atom relaxation using only these particular union constraints introduces nonnegative masses x_L indexed by nonempty cap subsets L and requires

    sum_(L intersects J) x_L >= F_(a,c)(s_J)
                          for every nonempty J.

The individual cap budgets are c_i+sum_(L contains i)x_L. One may also impose the physical total outside-mass constraint sum_L x_L<=a+c; the example below satisfies it. Original middle cap overlaps are retained exactly in the s_J, rather than discarded.

## 2. An exact five-dimensional middle fan

Take d=5 and a unit-volume 5-simplex B, with barycentric coordinates lambda_0,...,lambda_5. At its centroid use all six vertex caps

    H_i={lambda_i>=1/6},       i=0,...,5.

Their gradients sum to zero and span dimension five, so this is a minimal strictly positive circuit. Every own cap has volume

    c_i=Gamma=(5/6)^5=3125/7776.

For a subset J of size k, inclusion-exclusion gives the exact retained volume

    s_k=sum_(r=0)^k (-1)^r binom(k,r)(1-r/6)^5.

These numbers depend only on k. They decrease as k increases, and in particular

    s_4=5/81,       s_5=5/324,       s_6=0.

The last equality also follows because the six caps cover all continuous space. This is an actual common-contact full-rank fan; there is no arbitrary choice of inconsistent middle cap volumes.

Set

    a=7^(-5)=1/16807,       c=1,       W=2+a.

All three volumes a,1,1 are strictly less than W/2. They have an actual compatible realization: choose a simplex T containing the origin, with |T|=1, and take A=(1/7)T, B=C=T. Their lifted convex hull has precisely these three integer fibers.

The zero-credit threshold is

    M=((a^(1/5)+c^(1/5))/2)^5=(4/7)^5=1024/16807.

Exact arithmetic gives

    5/81-M=1091/1361367>0,
    1/32-5/324=41/2592>0.

Consequently

    F_(a,1)(s_J)=0  for |J|<=4,
    F_(a,1)(s_J)=a  for |J|=5 or 6.                  (1)

Indeed the first case has s_J>=s_4>M. In the second, s_J<=s_5<2^-5, so 2s_J^(1/5)<1 and the positive part inside the fifth power vanishes.

## 3. Exact optimum of the all-subset atom relaxation

Assign only singleton outside atoms:

    x_{ {i} }=a/5 for each i=0,...,5,
    x_L=0 for |L|>=2.

For every five-index set, its union mass is a, as required by (1). The six-index set has union mass 6a/5>=a; all smaller constraints have zero right-hand side. The total assigned outside mass is 6a/5<=1+a. The remaining outside mass 1-a/5 can be placed in the empty cap atom, if a full outside partition is recorded.

Every individual budget is exactly

    delta_relax=Gamma+a/5.                            (2)

This is the exact optimum, not just a feasible upper bound. For any feasible outside atoms let q_i=sum_(L contains i)x_L. For a five-index set J,

    sum_(i in J)q_i >=sum_(L intersects J)x_L>=a.

Thus max_i q_i>=a/5, and all c_i=Gamma. The singleton assignment attains that lower bound.

The desired sharp raw three-fiber target is

    T_OC=Gamma W/2=Gamma(1+a/2).

But

    T_OC-delta_relax
       =a(Gamma/2-1/5)=73a/77760
       =73/1306912320>0.                             (3)

Hence even a minimal full-rank positive fan with one common middle contact, exact original middle intersections, every subset endpoint credit, equal active scalar budgets, no heavy fiber, and the correct outside mass bound does not make this relaxation prove sharp OC. The additional scalar requirements sum_(i in J)c_i+F(s_J)<=|J|delta are also all satisfied, as consequences of the explicit atom construction.

## 4. The missing endpoint geometry gives an additional exact inequality

The outside atom assignment above CANNOT arise from actual ambient lifts of this fan. The reason is an elementary constraint that is absent from the scalar endpoint-union prices.

More generally, let finitely many actual ambient caps pass through (0,y), and write their margins as

    u_i.(x-y)+b_i z,

with positive weights theta_i satisfying sum_i theta_i u_i=0. Put B_0=sum_i theta_i b_i. On the endpoint z=1 the weighted sum of margins is B_0, while on z=-1 it is -B_0. At at least one endpoint this sum is nonnegative. The cap traces at that endpoint therefore cover ALL of R^d: it is impossible that every individual margin is strictly negative. This remains true when B_0=0, in which case both endpoints have full-space covers.

The ordinary centroid of that endpoint body belongs to at least one of those closed traces. Ordinary Gruenbaum gives at least Gamma_d times that entire endpoint's volume in one such cap. Consequently, for arbitrary own middle cap volumes c_i, the actual maximum cap budget satisfies

    max_i mu(H_i) >= min_i c_i + Gamma_d min(a,c).       (4)

This is an all-y positive-fan statement. It uses neither centroid alignment nor a common shape of the endpoint fibers. Closed boundary membership is harmless: Gruenbaum applies directly to a cap containing the actual centroid.

In the canonical middle-centroid fan of Section 2, all c_i=Gamma. Therefore every actual ambient lift has

    max_i mu(H_i)>=Gamma(1+a)>T_OC,

whereas the scalar atom relaxation gives the smaller value (2). Thus this example certifies the need for labeled endpoint fan geometry, and does not claim an actual below-target family.

For an equal-budget active fan at a deepest middle point y, (4) yields the useful necessary condition

    delta>=depth_B(y)+Gamma_d min(a,c).

The own point depth here is unnormalized. It cannot automatically be replaced by Gamma_d |B|, since y need not be the centroid or any ordinary deepest point of B.

## 5. Why the elementary new fan inequality is not yet a sharp repair

Even for a simplex, a positive fan with bounded largest own cap need not have its smallest own cap within the same error below Gamma_d. For example, for a triangle take barycentric contact (1/2,1/4,1/4) and its three canonical vertex caps. Their fractions are

    1/4, 9/16, 9/16.

They form a positive circuit through one actual point, yet

    min_i c_i+max_i c_i=13/16<8/9=2Gamma_2.

Thus the tempting estimate min_i c_i>=2Gamma_d-max_i c_i is false. Combining (4) with that estimate would silently insert an invalid ordinary-geometric lemma. A successful all-dimensional argument needs additional endpoint shape/threshold information or a proved way to control the source contact, not merely the full-subset scalar loss constraints plus the own-cap range.
