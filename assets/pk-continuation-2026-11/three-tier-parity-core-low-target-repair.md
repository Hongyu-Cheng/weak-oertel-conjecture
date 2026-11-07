# Three-tier parity-core repair with no load restriction at low targets

Scoped sufficient theorem, 6 November 2026. Accepted ordinary rigidity and
accepted high- and low-target repair theorems give the result below. The
inscribed-simplex accuracy of high partners is derived automatically under
a failed-target assumption, with its full compactness proof supplied here.
The incoming-load restriction remains only on the intermediate volume tier;
it is not proved automatic. No unrestricted OC conclusion is asserted.

## 1. Accepted inputs and notation

Fix n>=1 and d>=3. Put Gamma=(d/(d+1))^d and q=1-Gamma. Accepted fact
c77c6c94c4f34008 supplies

    A=(Gamma+ceil((d+1)/2)/(d+1))/2>Gamma

and rho_LS>0 with Gamma+A rho_LS<1, satisfying this precise one-sided
local-star statement: if finitely many convex d-bodies A_j,B,C_j satisfy

    (A_j+C_j)/2 subset B,
    D(C_j)<=Gamma(1+rho_LS),
    |C_j|>=|B|/(1+rho_LS),
    0<e=sum_j |A_j|<=rho_LS|B|,

then one y in int(B) simultaneously satisfies, for every nonconstant affine
f and every list of real thresholds t_j,

    |B cap {f>=f(y)}|
      +sum_j (|A_j cap {f>=f(y)+t_j}|
               +|C_j cap {f>=f(y)-t_j}|)
      >=Gamma|B|+A e.                                  (LS)

Here D is ordinary normalized maximum halfspace depth. No upper bound on
partner-to-middle volume or on D(B) is required. The ordinary input below
is accepted ea91e021ff1f4416: D(K)=Gamma exactly for simplices, and D is
continuous on normalized compact families of ordinary convex bodies.

Use the explicit constants a,delta,sigma,lambda of accepted actual
low-middle simplex-partner descent theorem 583b3086fe614511:

    beta=2^(1-d),
    a_star=2 Gamma beta/[q(1-beta q)],
    a=(beta+a_star)/2,
    delta=(1-2 Gamma-q^2 a)/4,
    sigma=[delta/(d(d+1))]^d,
    lambda=2 Gamma+(Gamma^2 a+delta)/(1-a).

That theorem proves beta<a<beta/q<1, delta>0, sigma<1, and lambda<1.
Its exact input/output used here is: if a target B of volume b<=a M_0
has distinct reflected outer partners A_i and core partners C_i, each C_i
contains a simplex of volume >=M_0, each |A_i|<=sigma M_0, and

    sum_i |A_i|>=r(b):=(2 Gamma+delta)M_0-(1-q^2)b,

then an actual point in B has raw mixed depth at least
(Gamma+delta/2)M_0 on that star alone. Also

    0<r(b)<=lambda(M_0-b).                            (1)

This is an all-oblique-halfspace statement, including pure integer normals.
The complete actual-body proof is accepted fact 583b3086fe614511.

Let C be a convex body in R^n times R^d and K_z its fibers. Write V_z=|K_z|.
Let P contain exactly one integer representative from each parity class,
all with positive volume. Put

    L=2^n, V=max_(w in P)V_w,
    E=sum_(p notin P)V_p,
    W=sum_(w in P)V_w+E,
    Delta=sum_(w in P)(V-V_w),
    b_avg=W/L, T=Gamma b_avg.

All sums are finite. Zero-volume fibers do not contribute. This statement
uses d-dimensional fiber volume and does not assert an intrinsic q<d
extension. Define the outside parity loads and incoming core loads by

    F_r=sum_(p notin P, p equivalent r mod2)V_p,
    R_w=sum_(v in P, 2w-v notin P)V_(2w-v).

## 2. Inscription accuracy from ordinary near-minimal depth

For zeta in (0,1), there is a positive tau_ins(zeta), depending only on d
and zeta, such that

    D(K)<=Gamma(1+tau_ins(zeta))
        implies s(K)>(1-zeta)|K|,                     (I)

where s(K) is the maximum volume of an inscribed d-simplex. We prove the
compactness parameter and every continuity needed for this assertion.

Let J consist of bodies B_2^d subset K subset d B_2^d. This is Hausdorff
compact by Blaschke selection and closedness of its defining inclusions.
The maximum s(K) is attained on the compact space of vertex tuples K^(d+1).
If K_j tends to K, maximizing tuples have convergent subsequences whose
limits lie in K, giving limsup s(K_j)<=s(K). For the reverse bound, let
h_K denote the support function. Uniform Hausdorff convergence gives
sup|h_(K_j)-h_K|->0. Since h_K>=1, for every epsilon in (0,1) and all
sufficiently large j,

    h_((1-epsilon)K)=(1-epsilon)h_K
        <=h_K-epsilon<=h_(K_j).

Thus (1-epsilon)K subset K_j and
s(K_j)>=(1-epsilon)^d s(K). Taking liminf and then epsilon down to zero
proves continuity of s. Volume is continuous on J by almost-everywhere
indicator convergence and bounded convergence, so s(K)/|K| is continuous.

For completeness D is continuous here as well: the normalized uniform
measures of K_j converge in total variation to that of K. Halfspace masses,
their infima at every candidate point, and then their suprema differ by at
most this total variation distance. This is the continuity argument in
accepted ordinary rigidity ea91e021ff1f4416.

The class J_zeta={K in J:s(K)/|K|<=1-zeta} is compact and contains no
simplex. If nonempty, the continuous D(K)-Gamma has a strictly positive
attained minimum g_zeta on it, by the accepted equality classification.
Set tau_ins(zeta)=g_zeta/(2 Gamma). If it is empty, set tau_ins(zeta)=1.
In both cases a body of J with D<=Gamma(1+tau_ins(zeta)) cannot belong to
J_zeta. John's ordinary affine normalization sends any convex d-body to J;
D and s(K)/|K| are affine invariant. This proves (I) for every K. All these
normalizations are confined to ordinary continuous bodies, with no change
to a mixed-integer source or its lattice.

## 3. Exact error and load parameters

Define

    kappa_H=Gamma/A,
    kappa=max{kappa_H,lambda}<1,
    k=(1-kappa)/4,
    zeta=delta/[16(Gamma+delta/2)],
    tau=min{rho_LS,tau_ins(zeta),1/4},
    eta=min{tau/4,zeta},
    mu=(1-eta)(1-zeta), M_0=mu V,
    epsilon=min{tau/4, 2^(-d-1)(1-eta), eta k,
                 sigma mu, delta/(8 Gamma)}.

These constants are strictly positive. The parameter zeta measures an
ordinary inscribed-simplex volume error; it is not set to zero.
Let

    G={w in P:V_w>=(1-eta)V},
    Low={w in P:V_w<=a M_0},
    Mid=P minus (G union Low).

The sets G and Low are disjoint because a mu<1-eta.
Assume:

(a) F_r<=epsilon V for every parity r.

(b) Only intermediate targets have an incoming-load restriction:

    sum_(w in Mid) R_w<=k Delta.                       (2)

There is NO incoming-load condition at high targets or at low targets.
Then an actual mixed-integer point has raw depth at least T.

There is no simplex shape or inscription assumption in the theorem. The
following proof derives the required accuracy from (I) only after assuming
that the target fails.

## 4. Route every high-partner edge to a core

For each positive-volume outside fiber p, let v(p) in P be its unique
parity representative and w(p)=(p+v(p))/2. Convexity gives

    (K_p+K_(v(p)))/2 subset K_(w(p)),
    V_(w(p))>=2^(-d)V_(v(p)).                          (3)

The second inequality follows already by fixing any point of K_p and
including its translate of half K_(v(p)). If v(p) in G and w(p) were
outside P, (3) would contradict

    V_(w(p))<=epsilon V
       <=2^(-d-1)(1-eta)V<2^(-d)V_(v(p)).

Thus all outside edges with high partner have core targets. For a fixed
target w, different outside p give different partners v=2w-p; the target
is distinct from every partner, and every outer fiber is outside the core.
Each local star therefore counts every physical fiber at most once.

## 5. Discarded mass is controlled only at bad partners and mid-band targets

Suppose for contradiction that no actual point attains T. The largest-core
centroid gives Gamma V<T, hence

    Delta<E, b_avg>V.                                 (4)

Every core outside G contributes more than eta V to Delta. Its outside
parity load is at most epsilon V. Therefore the total mass D_partner of
outside edges with partner outside G satisfies

    D_partner<=k Delta.

For an empty bad-partner set this is immediate; otherwise it follows from
|P minus G| eta V<Delta and epsilon<=eta k.

After removing these edges, every remaining edge targets a core. Remove
those targeting Mid. Their total mass D_mid is at most sum_(Mid) R_w,
so (2) gives D_mid<=k Delta. If e_w denotes all retained incoming mass at
a target in G union Low, then

    sum_(G union Low)e_w
      =E-D_partner-D_mid
      >=E-2k Delta>(1-2k)E.                           (5)

No high-partner load into a low target has been discarded. The sets of edges removed
in the two stages are disjoint, irrespective of the upper bounds used.

## 6. Failure gives a strict deficit contraction at every retained target

Put d_w=b_avg-V_w>0. By (4),

    sum_(w in P)d_w=E.                                (6)

For a high target w, every partner of its retained star is also high.
Since (a) gives E<=L epsilon V, failure of the target and existence of
ordinary deepest points imply

    D(K_v)<Gamma b_avg/V_v
       <=Gamma(1+epsilon)/(1-eta)<=Gamma(1+tau).

The last inequality follows from epsilon,eta<=tau/4 and tau<=1/4:
epsilon+(1+tau)eta<=9tau/16<tau. In particular the partner depth
hypothesis of (LS) holds. Also (I) yields, for every high core v,

    s(K_v)>(1-zeta)V_v>=(1-zeta)(1-eta)V=M_0.           (I2)

These maximum inscribed simplices are attained. They may be chosen by
lexicographically minimizing their maximizing vertex tuples in fixed
coordinates if a deterministic tie-break is desired. This proves exactly
the partner accuracy needed by the low theorem, with its error retained.
For high-to-high stars, the volume ratios lie between 1-eta and
(1-eta)^(-1)<=1+tau, so their lower ratio is sufficient for (LS).
The amount required by LS is

    r_H(w)=kappa_H d_w.

It satisfies

    r_H(w)<=kappa_H(eta+epsilon)V
       <=(tau/2)V<tau V_w<=rho_LS V_w.

If e_w>=r_H(w), shrink all the outer witnesses about their centroids by a
common ratio so their total becomes exactly r_H(w). They remain convex
subbodies of the actual fibers, preserve all midpoint inclusions, and the
LS guarantee becomes Gamma V_w+A r_H(w)=T. Integer tilts are the
simultaneous thresholds in LS. Pure integer directions include the whole
middle, whose volume exceeds Gamma V_w+A rho_LS V_w by the chosen bound
Gamma+A rho_LS<1. This contradicts failure. Thus

    e_w<kappa_H d_w                 for w in G.        (7)

For a low target w, its retained partners all lie in G, so (I2) supplies
inscribed simplices of volume at least M_0. Each outer volume is at most
epsilon V<=sigma M_0. Hence the actual low-middle theorem applies whenever
e_w>=r(V_w). Its depth would exceed the desired target, since

    (Gamma+delta/2)mu
      >=Gamma+delta/2-(Gamma+delta/2)(eta+zeta)
      >=Gamma+3delta/8,
    Gamma b_avg/V<=Gamma(1+epsilon)<=Gamma+delta/8.

Failure therefore forces

    e_w<r(V_w)<=lambda(M_0-V_w)<lambda d_w
                                         for w in Low, (8)

where M_0<=V<b_avg. The hypothesis e_w>=r(V_w)>0 guarantees a nonempty
star whenever the low theorem is invoked; rows of zero load automatically
satisfy (8).

Summing (7)--(8) and using (6) yields

    sum_(G union Low)e_w
      <kappa_H sum_G d_w+lambda sum_Low d_w
      <=kappa E.                                     (9)

The strict sum is legitimate even if Low is empty because G is nonempty
(it contains a largest core), all d_w>0, and kappa_H>0. But (5) contradicts
(9), since

    1-2k=(1+kappa)/2>kappa.

This proves the sufficient theorem.

## 7. Exact unresolved coverage

The incoming-load hypothesis is now imposed on Mid alone. Low targets may
receive arbitrarily large total incoming mass; excess mass triggers an
actual target point rather than being counted as lost. Errors in high
partner simplex volumes are retained through M_0=(1-eta)(1-zeta)V and
are paid explicitly by the low theorem's strict surplus.

The proof uses only the three accepted dependencies ea91e021ff1f4416,
c77c6c94c4f34008, and 583b3086fe614511, together with ordinary standard
compactness and normalization. The theorem's remaining geometric
hypotheses are the complete positive parity core, small outside parity
loads, and (2) on the intermediate band. It does not prove that those
hypotheses hold for every convex body or that every parity class occurs.
Its scope is a precise replacement of part of the earlier bad-target
budget by an actual all-direction geometric repair.
