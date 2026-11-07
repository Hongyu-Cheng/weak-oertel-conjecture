# An exact Brunn-Minkowski deficit price for a reflected star

Research draft, 6 November 2026. The theorem below is proved from a precise standard displacement-interpolation theorem and ordinary Grünbaum. It permits arbitrary endpoint shapes and locations in their actual fibers. It neither assumes centroid alignment nor solves the global problem of finding a useful star.

## Standard transport input

For bounded absolutely continuous probability densities rho_0,rho_1 on R^d, there is a transport coupling whose displacement interpolant rho_t satisfies

    ||rho_t||_infinity^(-1/d)
       >=(1-t)||rho_0||_infinity^(-1/d)
            +t||rho_1||_infinity^(-1/d).                 (T)

The interpolant is the law of (1-t)X+tY under that same coupling, whose marginals are rho_0 and rho_1. This is the q=infinity case of Theorem 2.3 in Robert J. McCann, *A Convexity Principle for Interacting Gases*, Advances in Mathematics 128 (1997), 153-179, printed page164. The author-hosted primary source is https://www.math.toronto.edu/~mccann/papers/advances.pdf . The theorem applies to the compactly supported uniform densities of convex bodies; no smooth boundary or positive curvature assumption is needed. The accepted proof of `dfd25e72c1f45a4e` uses this same standard input.

This note does not infer a multivariate change-of-variables formula from almost-everywhere differentiability alone. The existence and density estimate in (T) are the named standard theorem being used.

## Lemma 1: a midpoint source with the exact BM density ceiling

Let A,C be full-dimensional compact convex bodies in R^d, with volumes 0<a<=c. Put

    M=((a^{1/d}+c^{1/d})/2)^d.                           (1)

There is a finite measure nu of mass a, supported in (A+C)/2, with density bounded above by a/M, obtained as the midpoint pushforward of a coupling whose first marginal is Lebesgue measure restricted to A and whose second marginal is (a/c) times Lebesgue measure restricted to C.

Proof. Apply (T) to the uniform probability densities 1_A/a and 1_C/c at t=1/2. Their midpoint density is bounded by1/M. Multiply the entire coupling and its midpoint pushforward by a. Its marginals then have precisely the stated masses and densities; its midpoint density is bounded by a/M. Its support lies in (A+C)/2 because each coupled endpoint lies in its respective compact body almost surely.

## Lemma 2: exact domination for paired ambient cuts

Suppose A,C are actual fibers at integer bases p,z with p+z=2w. For the measure nu from Lemma1, any closed ambient halfspace H satisfies

    nu(H_w)<=|A intersect H_p|+|C intersect H_z|.         (2)

Proof. For every coupled pair (x,y), if its actual ambient midpoint (w,(x+y)/2) lies in a closed halfspace, at least one of (p,x),(z,y) lies in that same halfspace. Integrate the indicator inequality against the mass-a coupling. Its first marginal is1_A dx; its second is(a/c)1_C dx, which is dominated by1_C dx because a<=c. This proves (2) for all closed halfspaces, including pure integer cuts and boundaries carrying entire fibers. The coupling is fixed before H is chosen.

## Theorem: centroid depth with a linear BM-excess penalty

Let C_total subset R^n x R^d be a convex body, d>=1. Let its actual middle fiber B at integer base w have volume v>0 and true centroid g. Consider finitely many positive-volume actual endpoint pairs A_i,C_i at bases p_i,z_i such that

    p_i+z_i=2w,
    0<a_i:=|A_i|<=c_i:=|C_i|.

Assume that the middle base and all endpoint bases are pairwise distinct. Put Gamma=(d/(d+1))^d and

    M_i=((a_i^{1/d}+c_i^{1/d})/2)^d,
    Delta_i=v/M_i-1 >=0,
    theta_i=[Gamma-(1-Gamma)Delta_i]_+
           =[1-(1-Gamma)v/M_i]_+,                       (3)

where [s]_+=max(s,0). Then the single actual point (w,g) satisfies

    h_{C_total}(w,g)>=Gamma v+sum_i a_i theta_i.         (4)

In particular, the bound implies the untruncated linear estimate

    h_{C_total}(w,g)
       >=Gamma(v+sum_i a_i)
          -(1-Gamma)sum_i a_i(v-M_i)/M_i.                (5)

The exact coefficient multiplying the BM relative excess is 1-Gamma. No approximation or hidden dimension-dependent factor appears.

Proof. Actual convexity gives (A_i+C_i)/2 subset B. Brunn-Minkowski therefore gives M_i<=v, establishing Delta_i>=0. By Lemma1 choose fixed midpoint measures nu_i of mass a_i carried by B with density at most a_i/M_i. Define the nonnegative deficit measure

    eta_i=(a_i/M_i)1_B dx-nu_i.

Its total mass is exactly a_i(v/M_i-1). Thus for every Borel set F,

    nu_i(F)>=(a_i/M_i)|B intersect F|-a_i(v/M_i-1),      (6)

and nu_i(F)>=0.

Take a closed ambient halfspace containing (w,g), and first reduce it by inclusion to a parallel through-point halfspace H. If its continuous normal is nonzero, H_w is an ordinary proper closed halfspace through g, so ordinary Grünbaum gives |B intersect H_w|>=Gamma v. Substituting this into (6) and taking the maximum with zero yields

    nu_i(H_w)>=a_i[1-(1-Gamma)v/M_i]_+=a_i theta_i.

Lemma2 bounds each nu_i(H_w) by the two actual endpoint cap masses. Distinctness of all endpoint bases makes the sum of these bounds a legal source sum. Adding the middle cap's Gamma v proves (4).

If the continuous normal is zero, H_w is the whole R^d, so the middle fiber contributes v and nu_i(H_w)=a_i. Lemma2 again gives actual endpoint payments at least a_i. Since v>=Gamma v and 0<=theta_i<=Gamma<=1, this proves (4) directly, without a special upper bound on the requested depth and without dropping boundary fibers. Enlarging back to the original containing halfspace proves the universal claim. Dropping the positive-part operation gives (5).

Every constructed point and measure belongs to an actual fiber. Only the continuous midpoint measures are auxiliary, and they are used through a proved halfspace domination inequality; no claim that the original source is their sum is made.

## Exact saturation and a practical uniform-excess consequence

If M_i=v for all i, then theta_i=Gamma and (4) becomes

    h_{C_total}(w,g)>=Gamma(v+E),
    E=sum_i a_i.                                         (7)

This recovers the centroid-compatible star bound without separately invoking the equality characterization in Brunn-Minkowski. In particular, the transport proof avoids proving centroid compatibility as an intermediate step.

If Delta_i<=epsilon for all i, then

    h_{C_total}(w,g)
       >=Gamma v+[Gamma-(1-Gamma)epsilon]_+ E.           (8)

More precisely the weighted excess sum in (5), not the largest excess, is what controls the exact loss. This permits a small collection of poorly saturated pairs if their total weighted excess is small. A pair contributes positively exactly when M_i>(1-Gamma)v.

## Sharp target test for a one-low-core star

Suppose a core contains L positive-volume fibers including B, every A_i is an outside fiber and the A_i are precisely all positive-volume outside fibers, and every C_i is a core fiber. Let M be the largest core volume. Then W<= (L-1)M+v+E. The largest-core centroid supplies depth Gamma M. If W<=LM, it already gives Gamma W/L. In the complementary case define

    D=v+E-M>0,
    P_BM=(1-Gamma)sum_i a_i(v-M_i)/M_i.

The bound (5) reaches Gamma W/L whenever

    P_BM <= Gamma(1-1/L)D.                               (9)

Indeed W/L<=M+D/L=v+E-(1-1/L)D. Multiplying by Gamma and comparing with (5) proves the claim. Thus BM excess is an explicit price to be covered by the surplus over the maximum-core mass. At exact saturation P_BM=0, one of the two actual centroids always proves the sharp factor Gamma/L. This is a proved sufficient criterion; inequality (9) is not asserted for arbitrary convex bodies.

## Relation to existing midpoint facts

Accepted `280b299bc1e87c14` uses independent midpoint convolutions and relative-entropy comparison with the middle self-convolution, producing a different depth guarantee. The present argument uses an optimally coupled midpoint law with the exact BM density ceiling and compares it directly to uniform measure on B. Accepted `dfd25e72c1f45a4e` already uses the transport input (T) to establish metronoid convexity; the new conclusion here is the actual paired-halfspace domination together with the explicit linear excess-volume price at the unchanged middle centroid.

No same-fiber endpoint is reused in this theorem. The shared-endpoint all-or-nothing lemma from the higher-arity route is a different mechanism; its reuse permission must not be transferred to these summed midpoint measures without a separate marginal-capacity allocation.

## Stronger pointwise transfer and deepest-middle choice

For any point y in B, let t_B(y) be its ordinary absolute halfspace depth inside B. Define

    F(t)=t+sum_i a_i[1-(v-t)/M_i]_+ for 0<=t<=v.

The same measures and proof yield the stronger pointwise bound

    h_{C_total}(w,y)>=F(t_B(y)).                          (10)

Indeed every containing ambient halfspace with nonzero continuous normal has middle cap volume s>=t_B(y), and (6), Lemma2 and distinct source counting give mass at least F(s)>=F(t_B(y)). A pure integer containing halfspace has whole middle fiber and midpoint measures, hence total mass at least v+E=F(v)>=F(t_B(y)). Thus (10) holds before choosing a special middle point.

An ordinary deepest point y_* of B exists: cap volume through y is jointly continuous in y in compact B and in its unit normal, by dominated convergence and the fact that nonconstant affine hyperplanes have d-volume zero. Taking a minimum over the compact unit sphere preserves continuity in y. Thus the ordinary depth attains its maximum T=vD(B) on B. Formula (10) gives h_{C_total}(w,y_*)>=F(T). This requires no ordinary rigidity theorem.

In particular let delta_0=T-Gamma v>=0. Using the untruncated terms in F and expanding shows

    h_{C_total}(w,y_*)
      >= Gamma(v+E)
           -(1-Gamma)sum_i a_i(v/M_i-1)
           +delta_0(1+sum_i a_i/M_i).                   (11)

Thus a genuine ordinary depth surplus in the middle fiber pays the linear BM-excess price with the displayed exact multiplier. In the oriented one-low-core setting above, the sharp target is reached whenever

    P_BM <= Gamma(1-1/L)D
                +delta_0(1+sum_i a_i/M_i).              (12)

This is an additional sufficient criterion, not a claimed universal relation between ordinary depth and the BM deficits.
