---
fact_id: ef6cc6d9e2fd4c8e
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-nov6-high-arity-centroid-repair
depends_on: ["69e7900bfbf7454b", "6769574fc1bd9f8d"]
verifier_run: dff64eb2fa6a4892
target_match: null
---

## Statement

Write Gamma=(d/(d+1))^d for d>=1. All masses are d-dimensional Lebesgue volume in actual integer fibers of one convex body C subset R^n x R^d. For a point y at an integer base w, h_C(w,y) denotes the infimum of the mixed fiber-sum mass in closed ambient halfspaces containing that actual point.

## Theorem

Let w be an integer base with a full-dimensional fiber B=K_w of volume V>0 and true centroid g. Let A_j=K_{p_j}, j in J, be finitely many positive-volume actual fibers at distinct bases p_j. Let C_i=K_{z_i}, i in I, be finitely many full-dimensional actual fibers at distinct bases z_i. The groups {w}, {p_j}, {z_i} are pairwise disjoint. High endpoint fibers may be shared between different circuits.

Suppose parameters a>0, 0<b<1 and coefficients beta_j,lambda_ji satisfy

    |C_i|>=aV for every i,
    0<beta_j<=b, lambda_ji>=0,
    beta_j+sum_i lambda_ji=1,
    beta_j p_j+sum_i lambda_ji z_i=w.                     (1)

Let E=sum_j |A_j| and assume

    0<E<=min(a,1-Gamma)V,
    a(1-b)^d > 1-Gamma+d(E/(aV))^{1/d}.                  (2)

Then the single deterministic actual point (w,g) satisfies

    h_C(w,g)>=Gamma V+E.                                 (3)

The same conclusion holds if each A_j is a positive-volume homothetic subbody of an actual fiber K_{p_j}, with all the sums and hypotheses using its retained volume. In this version E is the retained total and the actual containing-halfspace mass is at least the retained-fiber mass used in the proof.



## Proof

## Lemma 1: an elementary uniform projection-density bound

Let B be any full-dimensional d-body, f a nonconstant affine functional, and W_f=max_B f-min_B f>0. Write S(t) for the (d-1)-dimensional measure of B intersect {f=t}, divided by the norm of the linear part of f. Then

    S(t)<=d|B|/W_f                                      (4)

for every t (with the usual H_0 measure when d=1). Consequently every slab of f-width s>=0 has volume at most ds|B|/W_f.

Proof. Fix a nonempty section, and choose support points of B where f attains its minimum and maximum. The two cones with common base equal to the section and apices those support points lie in B. Their interiors lie on opposite sides of the section and are disjoint. Their volumes add to the section's (d-1)-measure times the sum of their perpendicular heights divided by d, namely S(t)W_f/d. Hence this is at most |B|. At an endpoint section one cone has zero height and the other yields the same inequality. In d=1 the section is a point, H_0=1, and the assertion is the interval-length identity. Coarea integration gives the slab statement.

## Lemma 2: support margin from excess volume

Let g be the centroid of B, let Q subset B be a compact convex body, and let r>=0. If

    |Q|>(1-Gamma+dr)|B|,                                (5)

then for every nonconstant affine f,

    max_Q f>f(g)+r W_f.                                  (6)

Proof. Ordinary Grünbaum at g gives |B intersect {f>=f(g)}|>=Gamma|B|. A nonconstant affine hyperplane has zero d-volume, so |B intersect {f<=f(g)}|<=(1-Gamma)|B|. Lemma 1 bounds the added slab up to f(g)+r W_f by dr|B|. If (6) failed, Q would lie in that truncated portion of B and contradict (5).

## Proof of the theorem

Put r=(E/(aV))^{1/d} and fix any nonconstant affine f. For every j and every x in A_j, actual convexity and (1) imply

    Q_{j,x}=beta_j x+sum_i lambda_ji C_i subset B.        (7)

This is a compact full-dimensional convex body because at least one lambda_ji is positive. Indeed if all were zero then beta_j=1, contrary to beta_j<=b<1. Iterated Brunn-Minkowski and the volume lower bounds give

    |Q_{j,x}|^{1/d}
       >=sum_i lambda_ji |C_i|^{1/d}
       >=(1-beta_j)(aV)^{1/d}
       >=(1-b)(aV)^{1/d}.                                (8)

The strict inequality in (2) and Lemma 2 therefore yield

    beta_j f(x)+sum_i lambda_ji max_{C_i}f
       =max_{Q_{j,x}}f>f(g)+r W_f.                       (9)

The support identity uses the coefficient sum beta_j+sum lambda_ji=1, so it remains true for affine f with a constant term.

On the other hand, widths of Minkowski sums add, and (7) gives

    sum_i lambda_ji width_{C_i}(f)
        =width_{Q_{j,x}}(f)<=W_f.                        (10)

Set r_i=(E/|C_i|)^{1/d}<=r. The first condition in (2) ensures E<=|C_i| and hence r_i<=1. Combining (9)-(10) proves, for every x in A_j,

    beta_j f(x)+sum_i lambda_ji
        [max_{C_i}f-r_i width_{C_i}(f)]>f(g).             (11)

Thus every tiny fiber point belongs to its credit set from the shared-endpoint circuit-credit lemma. That lemma shows that every through-(w,g) ambient halfspace with nonzero continuous normal receives at least E from the distinct endpoint fibers, counted as actual sources. The middle fiber's centroid cap contributes at least Gamma V. This proves (3) for such halfspaces. The same conclusion can also be read directly from the lemma's dichotomy: either a single high cap pays all E, or all high cuts lie past their E-volume support-cap witnesses and (11) forces each tiny fiber into the halfspace.

If the continuous normal is zero, the through-point halfspace contains the entire middle fiber and contributes V>=Gamma V+E by (2). A general containing closed halfspace contains its parallel through-point halfspace, so all cases follow. Boundary mass has not been discarded from any ambient halfspace; only the ordinary zero-volume proper hyperplane fact was used inside the full-dimensional middle fiber in Lemma 2. The point is its actual centroid before any halfspace is chosen.

For retained subbodies, (7) still holds because each retained A_j is contained in the actual source fiber; the theorem's endpoint caps are then lower bounds on the actual caps. Exact retained volumes can be chosen by homothety as in the clipping note. This proves the final assertion.

## Explicit constants independent of n and of the number of circuits

Define

    a_d=1-Gamma/4,
    b_d=1-a_d^{1/d},
    epsilon_d=a_d (Gamma/(4d))^d.                        (12)

If |C_i|>=a_d V, all beta_j<=b_d, and 0<E<=epsilon_d V, then the theorem applies. Indeed

    a_d(1-b_d)^d=a_d^2
       =1-Gamma/2+Gamma^2/16
       >1-Gamma+Gamma/4,

while d(E/(a_dV))^{1/d}<=Gamma/4. Also Gamma<=1/2 and d>=1 imply epsilon_d<=1/8<=1-Gamma and epsilon_d<=a_d. This verifies every inequality in (2), with strict margin even at E=epsilon_d V. Thus the exact bonus coefficient one is uniform in the number of integer coordinates, the number of tiny fibers, and the number of shared high endpoints. The constants depend only on d.

For an equal-coefficient circuit p+z_1+...+z_k=(k+1)w, beta=1/(k+1). Consequently every k with 1/(k+1)<=b_d is legal; repeated high bases within one circuit can be merged by adding their lambda coefficients, and no source cap is counted twice. In an application it remains necessary to exhibit actual circuits and enough retained tiny mass. The theorem does not supply those circuits by assumption-free lattice geometry.

## Accepted mathematical inputs and relation to the graph

The ordinary centroid Grünbaum bound used above is available in accepted fact `6769574fc1bd9f8d` by taking the full-mass metronoid. Ordinary Brunn-Minkowski is used directly as a standard named theorem; its volume form is stated, for example, in equation (1.2) of [Tanganelli Castrillón, An improved stability result for Grünbaum’s inequality](https://arxiv.org/html/2410.12072v2). The shared-endpoint circuit-credit lemma has now been independently approved as fact `69e7900bfbf7454b`. Lemmas 1 and 2 and the source accounting also have complete proofs here or in the accepted shared-credit fact. No pending simplex-rigidity or local-star claim is invoked.

The mechanism differs from the pending pair-star repair in `ff31d56304dd901a`: it requires a small barycentric coefficient on the tiny endpoint, but in exchange makes every tiny fiber pay in every continuous direction at the unchanged actual middle centroid. It needs neither shape rigidity, equal volumes, affine centroids, nor independent high endpoints. This gives a concrete new way to route mass that was concentrated at a low reflected target, whenever suitable higher-arity circuits to high targets exist.

## Exact target-deficit corollary

Let T>0 be any desired raw ambient depth. Fix a middle base w of volume V and a finite set Z of high endpoint bases distinct from w, each having volume at least a_d V. Let R be the sum of the volumes of a finite collection of other distinct actual fibers, disjoint from {w} union Z, each of whose base p admits a circuit

    w=beta_p p+sum_{z in Z}lambda_pz z,
    0<beta_p<=b_d, lambda_pz>=0, beta_p+sum lambda_pz=1.

If T<=Gamma V, ordinary Grünbaum at the middle centroid already gives the target. If

    0<T-Gamma V<=epsilon_d V,
    R>=T-Gamma V,                                        (13)

then the same actual middle centroid has depth at least T. Indeed homothetically retain the total E=T-Gamma V from the selected tiny fibers, omitting any assigned zero masses; all circuit coefficients and high fibers are unchanged. The theorem gives Gamma V+E=T.

For the sharp OC target T=Gamma W/2^n, write B=W/2^n. Failure of that target therefore forces, at every w with

    B/(1+epsilon_d/Gamma)<=V_w<B,

the strict reservoir inequality

    R_w<Gamma(B-V_w),                                    (14)

for every legally chosen high endpoint set Z as above. This is unconditional: it uses no near-simplex or pending star lemma. It is an exact failure certificate once the relevant circuits are found. Large available reservoir mass requires no incoming-load bound, since only the target deficit is retained.

## A circuit reservoir on the exact slab-obstruction bases

Fix n>=2, put r=n-1, and define

    A={1} x {0,1}^r,
    D={2} x ({0,1}^r minus {0}),
    G=A union D, P={0} union G, w=(1,0).

Assume that the entire positive integer-fiber support is P union (-A), that every fiber at G has volume V, that the fiber at zero has volume sigma V with 0<sigma<1, and that every fiber at -A has volume delta V with delta>0. These are explicit hypotheses on an actual convex source; no common high-fiber shape or centroid relation is assumed. They give exactly

    W=(2^n-1+sigma+2^(n-1)delta)V.

The companion obstruction note supplies one homothetic realization, but that realization is not a premise of this corollary. Let p=(-1,-b) with b in {0,1}^r and k=|supp b|>=2. Enumerate its support i_1,...,i_k. Take high endpoints

    z_1=(2,e_{i_1}), z_2=(2,e_{i_2}),
    z_l=(1,e_{i_l}) for 3<=l<=k.

They all belong to G and are distinct from w. Their sum with p is (k+1)w. Therefore each such outer base has a legal equal-coefficient circuit whenever 1/(k+1)<=b_d. The same high endpoints may be reused for many different b, as permitted by the theorem.

Set k_d=max(2,ceil(1/b_d)-1). Every outer fiber indexed by a binary b of Hamming weight at least k_d belongs to this reservoir. Its total original mass is the sum over those actual fibers. If that sum pays the deficit in (13), the actual centroid at (1,0) gives sharp OC. Thus the geometric obstruction family is repaired, in sufficiently large base dimension and a suitable small-deficit regime, for completely unaligned convex high fibers of equal volume. The statement is conditional only on its displayed, directly checkable masses and actual base support; no equality-case Brunn-Minkowski argument is used.

In the uniform tiny-volume instance a_p=delta V, this reservoir has mass

    R=delta V sum_{j=k_d}^r binom(r,j).

When r>=k_d it contains at least delta V. For the displayed source mass, B=W/2^n and the deficit at w is Gamma(B-V)=Gamma[delta/2-(1-sigma)/2^n]V<Gamma delta V/2. Thus R covers that deficit whenever it is positive. If additionally Gamma delta/2<=epsilon_d, the theorem gives the sharp target with arbitrary high-fiber shapes whenever those exact masses and supports are realized. This is a certified use of higher arity to route mass away from a low reflected center.
