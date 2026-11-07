# An exact empty-core slab obstruction and a higher-arity cap repair

Research draft, 6 November 2026. All claims in this note are proved below. This is not a counterexample to OC. It disproves a proposed geometric counting shortcut and exhibits a different cap-payment mechanism on the same family.

## 1. Complete empty lattice cores with one low target and many slab partners

Let n>=2, r=n-1, Q_r={0,1}^r, and use base coordinates (s,b) in R x R^r. Define

    A={1} x Q_r,
    D={2} x (Q_r minus {0}),
    P={0} union A union D,
    G=A union D.                                          (1)

Then |P|=2^n. The bases 0 and D represent all even-first-coordinate parity classes, and A represents all odd-first-coordinate classes, so P is a complete parity transversal. Moreover every point of P is a vertex of conv(P), and

    conv(P) intersect Z^n=P.                              (2)

To prove the vertex assertion, project onto the last r coordinates. Each b in Q_r is a vertex of the cube. Over b=0 the convex hull has segment 0<=s<=1, with endpoints 0 and (1,0). Over b!=0 it has segment 1<=s<=2, with endpoints (1,b),(2,b). A convex representation of either endpoint must use only generators with exactly the same cube coordinate b, and then must use that endpoint itself. Hence every listed point is extreme. For (2), the last r integer coordinates must be in Q_r; the segments just identified have no other integer points.

For the target w=0, the high-core set G has only one missing core vertex, while its partner set A has |A|=2^{n-1}. The functional u(s,b)=s has

    min_G u=max_A u=1.

Consequently the radial coefficient from the companion note is exactly lambda_*(0;G,A)=1/2: a feasible relation lambda g=(1-lambda)a forces lambda<=1/2 by u, and lambda=1/2 is realized by g=a. Thus no bound |A|<=C times |P minus G| with a dimension-independent C can follow solely from the empty-polytope, complete-parity and bounded-slab-ratio assumptions, even with G in convex position and G lattice convex.

## 2. Actual convex bodies realize the complete obstruction

Let K be a d-dimensional convex body containing zero, V=|K|>0, and 0<t<1. Put

    C=conv((G x K) union ((-A) x tK)).                    (3)

The notation means the convex hull of all the indicated fiber copies. The projection is conv(G union -A); the body is compact, convex and full-dimensional since its projected bases span R^n and each source fiber is full-dimensional. Its integer bases are exactly

    P union (-A).                                        (4)

Here is a complete verification of all projection slices. Write a convex combination of the generating base sets with total weights alpha on A, gamma on D, and beta on -A; these are nonnegative and sum to one. Its first coordinate is s=alpha+2gamma-beta, and every remaining coordinate lies between -beta and alpha+gamma.

- At s=-1, extremality forces beta=1, so the integer points are exactly -A.
- At s=2, extremality forces gamma=1. The convex hull of Q_r minus {0} is [0,1]^r intersect {sum b_i>=1}, whose integer points are Q_r minus {0}; these are exactly D.
- At s=1, the equations give gamma=2beta and beta<=1/3. Every remaining coordinate lies in [-1/3,1], so every integer slice point lies in Q_r; all of these occur already in A.
- At s=0, the equations give 2alpha+3gamma=1 and beta=(1+gamma)/2 in [1/2,2/3]. Every remaining coordinate lies in [-2/3,1/2], so the only possible integer point is 0; it occurs as the midpoint of (1,0) and (-1,0).

There are no other possible integer values of s. This proves (4).

All fibers at G equal K: all generating continuous coordinates lie in K, while each such base already carries K. Every fiber at -A equals tK because s=-1 forces only negative generators. Finally

    K_0=((1+t)/2)K.                                      (5)

Indeed a representation at s=0 has total high-core coefficient alpha+gamma=(1-gamma)/2<=1/2, hence its continuous coordinate lies in [alpha+gamma+beta t]K subset ((1+t)/2)K. Conversely the midpoint of the generators at (1,0) and (-1,0) gives the whole latter body. Homothetic copies are nested because 0 is in K.

Writing delta=t^d and sigma=((1+t)/2)^d, the original volume data are therefore

    V_v=V (v in G), V_0=sigma V,
    a_p=delta V (p in -A),
    E=2^{n-1}delta V,
    W=(2^n-1+sigma+2^{n-1}delta)V.                        (6)

Every outer fiber p=-v has partner v in A and reflected midpoint 0. There is exactly one outer fiber in each odd-first-coordinate parity class, and none in the others. Thus the maximum outer mass per parity class is delta V, but all outside mass arrives at the same low core target. If delta<2^{-d}sigma, the pointwise smallness condition in the clipping note holds as well. This can hold for arbitrarily small delta, with fixed d and arbitrary n.

For fixed theta>0 sufficiently small and t sufficiently small that sigma<1/(1+theta) and delta/2<theta, take n large enough that 2^n delta/2>1-sigma. Then B=W/2^n satisfies 1<B/V<1+theta, every core v in G lies in the good set {V_v>=B/(1+theta)}, and 0 does not. All outer mass therefore touches the unique bad core, even though good cores occupy the fraction 1-2^{-n}. The summed bad-target incoming mass has no small upper bound from these geometric and volume hypotheses alone.

The family does not establish failure of OC. In fact the next section proves a strictly stronger than target bound for a natural choice of K.

## 3. A general identical-simplex circuit payment

Let K be a d-simplex with centroid 0 and V=|K|. Suppose an actual mixed convex source contains a middle fiber K at an integer base w, k distinct other fibers K at bases z_1,...,z_k, and one fiber tK at a different integer base p. All these bases are distinct, and

    p+z_1+...+z_k=(k+1)w,
    0<t<=k/[k+(k+1)d].                                  (7)

Then the fixed actual point (w,0) has raw ambient halfspace depth at least

    (Gamma_d+t^d)V.                                      (8)

Proof. Let a containing closed halfspace be reduced to a parallel through-(w,0) halfspace. Suppose first its continuous normal f is nonzero and linear. Its cuts at the k large endpoints and one tiny endpoint have thresholds tau_1,...,tau_k,tau_p satisfying

    tau_p+sum_i tau_i=0                                  (9)

by (7). Put h=max_K f and ell=min_K f. Because K is full-dimensional with centroid zero, h>0. Its d+1 vertices sum to zero, so the least vertex value is at least minus d times the greatest vertex value. Therefore ell>=-dh and h-ell<= (d+1)h.

At a support point attaining h, the homothetic copy of K with ratio t has volume t^d V and lies in the cap {f>=h-t(h-ell)}. Hence any endpoint cut with tau_i<=h-t(h-ell) contributes at least t^d V, which already pays the desired bonus. Otherwise all tau_i>h-t(h-ell), and (9) gives

    tau_p < -kh+kt(h-ell)
          <=[-k+kt(d+1)]h
          <=-dt h
          <=t ell.

The penultimate inequality is precisely (7). Thus the entire tiny fiber tK lies in the cap and pays the same bonus. This counts each endpoint fiber once. The middle centroid cap contributes at least Gamma_d V by ordinary Grünbaum. If the continuous normal is zero, the entire middle fiber contributes V; this is at least (Gamma_d+t^d)V since t<=k/[k+(k+1)d]<1/(d+1), so t^d<=(d+1)^{-d}<=1/2<=1-Gamma_d. This proves (8) for every closed ambient halfspace, including pure integer halfspaces. No transformed or averaged point is used.

For the exact family (3) and n>=3, take w=(1,0), z_1=(2,e_1), z_2=(2,e_2), and p=(-1,-e_1-e_2), with standard basis vectors in R^{n-1}. These are all actual bases from (4), they are distinct, and their sum is 3w. Thus for t<=2/(3d+2),

    h_S(w,0)>=(Gamma_d+delta)V
       > Gamma_d [1-(1-sigma)/2^n+delta/2]V
        =Gamma_d W/2^n.                                 (10)

This bypasses the congested low reflected target by using a genuine three-endpoint circuit at a high core fiber. It shows exactly why the extra hypothesis 'OC fails' cannot be discarded from any proposed structural incidence argument.

## 4. Consequence for the research routes

The pure bounded-slab counting route is blocked by the exact family (1)-(6). To reopen it one needs cap geometry or another consequence of failed OC, not merely emptiness, almost complete parity, low individual outside masses, or affine rank. The circuit payment (7)-(8) supplies one such mechanism, but its identical centered-simplex hypotheses cannot be silently imposed on general fibers. The companion shared-endpoint credit lemma gives a genuine support-function formulation for general convex fibers without assuming aligned centroids.
