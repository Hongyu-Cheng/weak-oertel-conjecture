# An actual three-fiber source whose entire middle fiber misses the sharp OC target

This is an obstruction to selecting the middle fiber, even after optimizing over every point in that fiber. It is not a counterexample to OC: the other large endpoint is a nonsimplex with a strict ordinary centroid-depth surplus. The construction has n=1,d=15, a simplex middle fiber, and volumes (a,1,1). All three fibers are below half the total mass.

## 1. Exact clipped simplex and its volume certificate

Let d=15, N=16 and Gamma=(15/16)^15. Let T be any d-dimensional simplex of volume one, with barycentric affine coordinates lambda_1,...,lambda_16. Put

    D={x in T:lambda_i(x)<=1/16 for i=1,...,13}.

Inclusion--exclusion gives

    p=|D|=sum_(l=0)^13 (-1)^l binom(13,l)(1-l/16)^15
      =59717129472000/16^15
      =29158754625/562949953421312.                    (1)

For each chosen l-coordinate intersection, subtracting 1/16 from those coordinates leaves a simplex of linear scale 1-l/16, which proves each term in (1). Thus this is an exact volume identity.

Define rho by

    rho^15=2^(-15)/p=17179869184/29158754625.

Then 0<rho<63/64<1. The nontrivial rational inequality is certified by

    59717129472000*63^15-2^135
      =14816205358430717469293609548549415237632>0.    (2)

Let g be the centroid of T, so lambda_i(g)=1/16. Let p_0 be the point whose first13 barycentric coordinates are 1/32 and whose last3 coordinates are 19/96. These coordinates are positive and sum to one; p_0 lies in the interior of D. Define

    D_0=p_0+rho(D-p_0),       C=2D_0-g.              (3)

Then |D_0|=2^(-15) and |C|=1. These are genuine compact full-dimensional convex polytopes.

## 2. The actual source and a uniform threshold gap

Choose any 0<epsilon<=2^(-12), set

    A=g+epsilon(T-g),        a=|A|=epsilon^15<=2^(-180),
    S=({-1} x A) union ({0} x T) union ({1} x C).

We prove that S is exactly the mixed-integer intersection of its lifted convex hull.

The midpoint body is

    M=(A+C)/2=D_0+(epsilon/2)(T-g).                   (4)

Every barycentric coordinate of D_0 is at least (1-rho)/32, because the minimum coordinate of p_0 is 1/32 and all coordinates of D are nonnegative. The corresponding minimum on the perturbation (epsilon/2)(T-g) is -epsilon/32. Since epsilon<=1/4096<1/64<1-rho, every coordinate of M is positive. In particular M subset T.

For i<=13, the maximum on D_0 is (1+rho)/32. Therefore

    max_M lambda_i <=(1+rho)/32+15epsilon/32
                    <=1/16-delta,
    delta=(1-rho)/64>1/4096.                          (5)

The second inequality uses epsilon<1/1920<(1-rho)/30, which follows from (2). Thus all13 specified coordinate gaps are uniform and strictly positive.

Midpoint inclusion proves that the only integer fibers of conv(S) are exactly A,T,C. Indeed its projection is [-1,1], its two extreme fibers are unchanged, and any endpoint contribution to its fiber at zero is a convex combination involving (A+C)/2 subset T. The lifted hull is a full-dimensional convex body. Its total mixed volume is W=2+a. Each fiber has volume strictly below W/2=1+a/2.

## 3. Actual oblique facet caps and simultaneous threshold compatibility

For y in T write s_i=lambda_i(y). The vertex-side cap in T given by lambda_i>=s_i has volume (1-s_i)^15. For every i and every y, there is an actual ambient halfspace through (0,y), with this exact middle trace, that misses C. Its mass is at most

    (1-s_i)^15+a.                                    (6)

To see this, write the ambient cap as

    H_i={ (z,x):lambda_i(x)+beta_i z>=s_i }.

Choose beta_i<s_i-max_C lambda_i. Then its C trace is empty; its A trace has mass at most a. Its continuous normal is nonzero.

If s_i>max_M lambda_i, then beta_i can be chosen to miss BOTH endpoints, giving the sharper exact cap mass

    mu(H_i)=(1-s_i)^15.                              (7)

Indeed the two endpoint thresholds are s_i+beta_i on A and s_i-beta_i on C. Both can exceed their endpoint maxima exactly when

    max_A lambda_i+max_C lambda_i<2s_i.

The left side equals 2max_M lambda_i by the actual Minkowski sum in (4). Thus (7) follows. These are actual shared-threshold ambient halfspaces, rather than separate hypothetical fiber caps.

## 4. Every middle point lies below the sharp target

The raw sharp OC target is

    T_a=Gamma(1+a/2).

We prove the stronger bound h_S((0,y))<U_a for EVERY y in T, where

    U_a=Gamma+(189/1000)a<T_a.

The exact comparison Gamma>379/1000 below gives T_a-U_a>a/2000.

Suppose instead that some y satisfies h_S((0,y))>=U_a. Formula (6) implies, for every i,

    s_i<=1-(U_a-a)^(1/15).                           (8)

Put q=Gamma^(1/15)=15/16. Since a<=2^(-180)<Gamma/2, one has U_a-a>=Gamma/2. The derivative of x^(1/15) on [Gamma/2,Gamma] is at most 2/(15Gamma). Hence

    q-(U_a-a)^(1/15)<=2a/(15Gamma).

Using sum_i s_i=1 and (8) on the other15 coordinates gives

    s_i>=15(U_a-a)^(1/15)-14
        >=1/16-2a/Gamma
        >1/16-1/4096.                               (9)

The last strict inequality follows from Gamma>3/8 and a<=2^(-180). In view of (5), all first13 coordinates satisfy s_i>max_M lambda_i, so their endpoint traces can both be missed. Formula (7), together with h_S((0,y))>=U_a, then gives

    s_i<=1-U_a^(1/15)              for i<=13,
    s_i<=1-(U_a-a)^(1/15)         for i=14,15,16.

Summing these16 inequalities forces

    13 U_a^(1/15)+3(U_a-a)^(1/15)<=15.               (10)

The following exact scalar estimate contradicts (10). Define

    f(v)=13[Gamma+(189/1000)v]^(1/15)
          +3[Gamma-(811/1000)v]^(1/15).

Then f(0)=15 and

    f'(0)=[16(189/1000)-3]/(16Gamma)>3/1000.                 (11)

Here the exact integer comparisons 1000*15^15>379*16^15 and 2*15^15<16^15 show 379/1000<Gamma<1/2. The numerator in (11) is 3/125 and 16Gamma<8, proving (11).

For 0<=v<=Gamma/2, both arguments of the roots are at least Gamma/2>3/16. With r=1/15, X=Gamma+(189/1000)v and Y=Gamma-(811/1000)v,

    |f''(v)|
      =r(1-r)[13(189/1000)^2 X^(r-2)
                  +3(811/1000)^2 Y^(r-2)]<8.       (12)

For a direct bound, the squared-coefficient sum is less than 13/16+3<4, and each power is at most (3/16)^(-2)=256/9<29; multiplying by r(1-r)<1/15 gives less than 116/15<8. (If X>=1 its power is smaller still.) Taylor's formula with its integral remainder therefore gives

    f(a)>15+(3/1000)a-4a^2>15,                           (13)

because 0<a<=2^(-180)<3/4000. Equations (10) and (13) contradict one another.

This proves that every point in the actual middle fiber has depth strictly below the sharp raw target. The middle depth maximum is attained: for finite Borel measures the closed-halfspace depth is upper semicontinuous, by slight cap enlargement and continuity from above, and T is compact. Consequently the strict pointwise result gives the strict maximum statement

    max_(y in T) h_S((0,y)) < Gamma+(189/1000)a
                              < Gamma(1+a/2)-a/2000.            (14)

All cap boundaries used here are nonvertical and have zero d-volume. No boundary-only mixed mass is discarded, and the conclusion includes every middle point, not only a centroid or a restricted candidate family.

## 5. Endpoint depths and why this is not an OC counterexample

At an extreme integer fiber, mixed depth equals ordinary fiber depth. One inequality follows because every ambient cap restricts to a containing cap on that fiber. Conversely, any desired containing continuous cap can be extended with a sufficiently large integer tilt to exclude both other bounded fibers.

Thus the small simplex endpoint has maximum raw depth exactly Gamma*a. The other endpoint C has maximum raw depth beta(C) satisfying

    Gamma<beta(C)<=1/2.                               (15)

Here is a justification of the strict lower inequality using the classical equality statement in the ordinary centroid Grünbaum theorem: a centroid halfspace can have volume fraction exactly Gamma only if the body is a pyramid (in dimension15, a cone over a14-dimensional base). This ordinary equality characterization is stated in Marín Sola--Yepes Nicolás, *On Grünbaum type inequalities*, p.1, https://webs.um.es/jesus.yepes/publicaciones_files/paper_grunbaum.pdf, and is the same classical input used in the audited two-centroid-cut note.

The polytope D has precisely29 facets: its16 simplex-coordinate facets and its13 upper-coordinate facets. Each is nonredundant, as one can vary the unconstrained positive coordinates while putting only the designated inequality at equality. Every vertex has all13 constrained coordinates at endpoints0 or1/16 and exactly one of the3 unconstrained coordinates positive; otherwise a nontrivial feasible coordinate exchange prevents extremality. Conversely all such choices are vertices. Each vertex therefore lies on exactly15 facets and misses14. A polytope pyramid has an apex lying on every facet except its base, so D is not a pyramid. Neither are its homothets D_0,C.

The ordinary centroid of C is interior. Its proper cap-volume function is continuous on the unit sphere, so its minimum is attained. Ordinary Grünbaum and the equality characterization show that every such cap has fraction strictly greater than Gamma; compactness makes the minimum strictly greater than Gamma. This proves the first inequality in (15). The upper bound1/2 follows by taking the two opposite proper halfspaces through any point.

For a certified subfamily where an explicit admissible kind of point DOES meet OC, let delta_C>0 be the ordinary centroid's attained depth surplus above Gamma. The body C and delta_C do not depend on epsilon. Choose, in addition,

    epsilon^15<=2delta_C/Gamma.

Then the ordinary centroid of the large endpoint C has raw depth at least Gamma+delta_C>=Gamma(1+a/2), while (14) still rules out every middle point. This produces an actual family for which selection of that endpoint is necessary. The construction with the explicit choice epsilon=2^(-12) has the exact middle-fiber obstruction and the endpoint bounds (15); no unsupported numerical lower bound for delta_C is asserted.

## 6. Scope and relation to earlier notes

The obstruction is to the full middle-fiber selection claim at the sharp OC threshold, even for a middle simplex of maximum fiber volume and one equal-volume endpoint. It does not restrict the possible choice of the large nonsimplex endpoint and does not refute OC.

The previously recorded midpoint-of-endpoint-centroids failure `64c5bdbc0c6d6575` excludes one candidate point only. The own-depth-capacity obstruction `325d279c18e3a49e` excludes a different capacity, not actual mixed depth. The balanced sharp-heavy-endpoint transfer criterion `10419d22ef690267` assumes a=k+b and beta(A)=Gamma*a; neither condition holds for our nonsimplex large endpoint of volume1 and total mass2+a. Thus there is no contradiction with that perturbation implication. The all-ratios homothetic theorem `aae24573a37976a6` is also inapplicable: C is not homothetic to the simplex middle T.

The accepted equal-large-partner obstruction `5e8a8af95fa24a1d` uses the same broad idea of a clipped simplex partner and exact endpoint-excluding facet caps, but it disproves the stronger proposed middle-star budget Gamma(1+a). Its text explicitly leaves the smaller OC budget Gamma(1+a/2) intact. The present d=15 construction certifies failure at that smaller sharp budget. It should therefore be recorded as a strengthening of that existing mechanism, not an unrelated new mechanism.

Pending `1350a6f7ed8eb7d0` asserts a small-endpoint theorem selecting among all fibers. Its proof assumes a failing sequence, which forces BOTH large fibers' ordinary maximal depths toward Gamma and hence simplex limits. Our fixed nonsimplex large endpoint has a strictly positive depth surplus, so this construction is excluded by that failure-sequence reduction. In the small subfamily explicitly treated in Section5 the large endpoint supplies OC, in agreement with that result.
