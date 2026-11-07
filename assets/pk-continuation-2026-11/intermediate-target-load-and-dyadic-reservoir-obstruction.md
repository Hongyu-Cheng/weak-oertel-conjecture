# Intermediate-target load and the late dyadic-reservoir mismatch

This note extracts the applicable elementary identity from accepted
`e84695845cd7c824` and proves an actual-body obstruction to bounding the
intermediate-target incoming load from parity concentration and source
volumes alone. It does not refute sharp OC; every body constructed below
has an explicit sharp OC center.

## 1. The unconditional residue identity

Let a_z>=0 be finitely supported masses on Z^n. For each parity class xi
of positive mass A_xi=sum_(z equivalent xi) a_z, put

    r_{uv}=a_u a_v/(4 A_xi)

on distinct same-parity unordered pairs. For k>=1 define P_k by summing
r over pairs whose difference is divisible coordinatewise by 2^k. If
A_[k],eta is the mass in a residue class eta modulo 2^k, then

    P_k=sum_xi (1/(8 A_xi))
            [sum_(eta mod 2^k reducing to xi) A_[k],eta^2
                         -sum_(z equivalent xi) a_z^2].          (1)

This follows by expanding each residue-class square and counting every
unordered pair twice. Consequently

    P_k-P_(k+1)=sum_xi (1/(8 A_xi))
          [sum_eta A_[k],eta^2-sum_zeta A_[k+1],zeta^2]>=0.       (2)

No diffuseness or 'good parity' hypothesis is needed for (1)-(2).
For actual convex-body fiber volumes, the quarter-child comparison also
extends whenever all required points remain integral and in the same
parity class: a pair with difference in 2^(k+1)Z^n, k>=2, maps injectively
to {(3u+v)/4,(u+3v)/4}, of difference in 2^k Z^n and the same parity.
Brunn-Minkowski gives child endpoint product at least the parent product,
so the sum of these nonnegative product increments is at most
P_k-P_(k+1), as in the proof of accepted e846. The restriction k>=2 is
substantive: for an edge of exact dyadic valuation one, the quarter
points need not be integer.

## 2. Why the late hard ledger does not apply to a nearly complete core

Accepted `320dcb7d85f22889` defines its reservoir only on 'good' parity
classes satisfying

    max_(z equivalent xi) a_z <= A_xi/4.                          (3)

Accepted `ca061f9c44376a53` and `02a75ec03a8733a8` retain that same
canonical system, its optimized subcapacity, and its strict hard ledger.
The ordinary core/outside pairs in the small-outside regime instead have
one near-maximal core fiber and outside parity mass at most epsilon V.
Whenever that core exceeds epsilon V/3, condition (3) fails. In particular
all high-partner pairs used in the three-tier theorem are absent from
that good-class reservoir.

There is a separate quantitative mismatch. In any complete product
reservoir, or any subset of its parity classes, (1) at k=1 gives

    Q<=W/8.                                                       (4)

For a complete parity core P of size L=2^n, largest core volume V, and
outside parity masses at most epsilon V, one has W<=L(1+epsilon)V.
Ordinary Gruenbaum at the largest core gives h_max>=Gamma_d V. In the
late hard ledger's notation D=L h_max, so when Q>0,

    D/Q >=8 Gamma_d/(1+epsilon).                                 (5)

For example, epsilon<=1 makes this larger than 4/e>1. The hard ledger
requires D<Q/100. Thus that hard system cannot occur in this near-core
regime, even if its other objects were defined. Failure of sharp OC,
which only asserts D<Gamma_d W, does not imply the far stronger hard
ledger. Its terminal/KKT absorption conclusions cannot be used as a
sharp-target Mid-load bound without an additional new theorem.

## 3. Exact arbitrary concentration at an intermediate target

Fix d>=1, a d-dimensional simplex K with centroid zero and volume V.
Choose numbers 0<t<1 and s with

    (1+t)/2<=s<1.

Put delta=t^d and b=s^d. For any n>=1 define

    P={0,1}^n,
    G=P minus {0},
    O={-e_1,...,-e_n},
    C=conv[(G x K) union ({0} x sK) union (O x tK)].               (6)

This is a compact full-dimensional convex body. Its integer base census
is exactly P union O. Indeed every projected coordinate is in [-1,1].
A negative integer coordinate must equal -1 and forces its uniquely
minimizing negative generator -e_i. All remaining integer coordinates
are in {0,1}. Every point of P occurs, and the O points are generators.

The exact fibers are

    C_z=K       for z in G,
    C_0=sK,
    C_(-e_i)=tK for 1<=i<=n.                                    (7)

For z in G, the fiber contains K by construction and is contained in K
because all continuous generator coordinates lie in K. At -e_i, the
exposed integer base forces its whole fiber to be exactly tK.
At zero, let lambda_+,lambda_-,lambda_0 be the total coefficients on
G,O,{0} in a generator convex combination. Applying the coordinate-sum
functional gives lambda_+<=lambda_-, since each point of G has coordinate
sum at least one and each outer point has sum -1. Hence

    lambda_+ +t lambda_- +s lambda_0
       <=(1-lambda_0)(1+t)/2+s lambda_0<=s.

The continuous component therefore lies in sK, using convexity and
0 in K. The reverse inclusion is a generator fiber. This proves (7).
Every generator fiber contains tK, so C contains
conv(P union O) times tK. The first factor contains the full-dimensional
cube [0,1]^n and the second has positive d-dimensional interior. This
proves nonempty full ambient interior directly.

Thus the complete parity core has volumes V except for its zero core,
of volume bV. Its deficit and outside mass are

    Delta=(1-b)V,       E=n delta V,
    W=(L-1+b+n delta)V.                                          (8)

Each outside base -e_i has unique same-parity core partner e_i, and all
reflected targets are zero. Thus

    R_0=n delta V,       R_w=0 for w in P minus {0}.               (9)

Every outside parity mass is either delta V or zero. Every high core is
an exact simplex and has ordinary normalized maximal halfspace depth
Gamma_d. The same is true of the middle and all outer fibers.

For any fixed intermediate band (ell,u) with

    max(ell,2^(-d))<u<1,

choose b in that interval, set s=b^(1/d), and then choose t>0 so small
that t<2s-1 and delta is below any prescribed outside-parity bound.
The zero core is then in that band. Finally choose n so large that

    n delta >K(1-b)

for any prescribed finite K. Equations (8)-(9) show

    sum_(intermediate w) R_w >K Delta.                            (10)

In particular, the intermediate-band incoming-load budget of the
three-tier theorem is not implied by its per-parity smallness, exact
simplex high partners, all ordinary fiber depths equal to Gamma_d, or
failure of the largest-fiber certificate (take K>=1). This conclusion
is about those explicit hypotheses only, not the stronger assumption
that every actual mixed-integer point fails sharp OC.

## 4. All incoming pairs are at the first dyadic level

For the masses (7), the only parity classes with multiple positive
fibers are those of e_i. Each contains exactly e_i and -e_i, of masses
V and delta V. Their difference is 2e_i, of exact dyadic valuation one.
Thus the unrestricted product ledger of Section 1 has

    P_1=E/[4(1+delta)],       P_k=0 for every k>=2.                (11)

There is no quarter-child descent in the original integer lattice on
any of these incoming pairs. All late good-class reservoirs are empty,
since each two-atom class has largest mass greater than half its total,
and each other class is a single atom. The unweighted incoming load may
be arbitrarily large compared with Delta while every higher dyadic drop
vanishes. Therefore a direct bound of Mid load by higher-level product
curvature is false on actual bodies.

## 5. The missing information is geometrical, not a failure of OC

The actual middle centroid (0,0) has halfspace depth at least

    Gamma_d(b+n delta)V.                                         (12)

Every endpoint pair has centroids (e_i,0),(-e_i,0), whose midpoint is
(0,0), so a containing closed ambient halfspace captures at least one
endpoint centroid and hence at least Gamma_d delta V from that pair.
The middle contributes Gamma_d bV. Distinct pairs have distinct physical
fibers, so these contributions add. Pure integer halfspaces satisfy the
same estimate with full endpoint fibers.

If n delta<=1-b, a largest-core centroid has depth at least Gamma_d V, which is at least
Gamma_d W/L. If n delta>=1-b, put Q=b+n delta>=1; then
W/V=(L-1)+Q<=LQ, and (12) supplies the sharp target. Thus every member of
(6) satisfies OC by a concrete deterministic point. The obstruction says
that a useful compatibility invariant must charge geometrical failure
of an intermediate-target repair (for example centroid mismatch or cap
loss), not incoming mass alone or higher dyadic product increments.
