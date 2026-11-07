# Regular projected contacts, section centroids, and the absence of regular facets

Research draft, 6 November 2026. These are exact contact-certificate results and a limitation of the facet mechanism. They give no lower bound for the global mixed-integer centerpoint constant.

Let n,d>=1. Let P be a finite subset of Z^n and let K_p be full-dimensional compact convex bodies in R^d. Define

    mu=sum_(p in P) delta_p x Lebesgue_d|K_p,
    W=mu(R^(n+d)),
    h(Y)=inf {mu(H): H is a closed ambient halfspace containing Y},
    D_T={Y:h(Y)>=T},       Q_T=projection_z D_T,

where 0<T<W. Assume D_T has nonempty ambient interior. Define the finite base skeleton

    Sigma(P)=union {conv(A): A subset P, affdim(A)<n}.

All measure is full d-dimensional fiber volume. No q<d extension is asserted. The bodies need not be realized by a common ambient convex body. The lattice bases stay fixed throughout.

## 1. Replace the facet assumption by a ray normal cone

Suppose z_0 is a boundary point of Q_T outside Sigma(P), and its ordinary convex normal cone is the ray

    N_(Q_T)(z_0)={t ell:t>=0},       ell !=0.

For any lift Y_0=(z_0,x_0) in D_T there are k<=d+1 actual nonvertical closed caps

    H_i={ (z,x): a_i.z+u_i.x>=b_i },      |u_i|=1,

and positive coefficients theta_i with

    mu(H_i)=T,       b_i=a_i.z_0+u_i.x_0,
    sum_i theta_i u_i=0,
    sum_i theta_i a_i=c ell,       c>0.

The continuous normals form a minimal positive dependence. Their complementary closed halfspaces contain D_T.

Proof. Appendix A below proves the local active-cap normal-cone representation at any lift whose base lies outside Sigma(P). This is the same mechanism as Sections 1--3 of pending intake `3e1d949289e94035`, whose earlier independent audit does not by itself make it an accepted repository premise. Apply the representation to (ell,0).

Decompose its positive continuous-normal dependence into minimal positive dependencies. Explicitly, within the current nonnegative kernel vector choose a nonzero nonnegative kernel vector of minimal support, subtract its largest permissible positive multiple, delete a zero coefficient, and repeat. A minimal support has at most d+1 members: its kernel is one-dimensional, since otherwise an independent kernel perturbation of its strictly positive vector could reach the boundary of the nonnegative orthant and reduce the support. Thus its support size is at most the rank of its continuous normals plus one.

For one such circuit put ell'=sum theta_i a_i. The sum of its valid inequalities is ell'.z<=ell'.z_0 on Q_T. It cannot have ell'=0: if G is an interior point of D_T, every active normal has strictly negative dot product with G-Y_0, and so does their positive sum. Hence ell' is a nonzero member of N_(Q_T)(z_0), and therefore equals a positive multiple of ell. The selected circuit proves the assertion. No flat piece of the projected boundary was needed.

This allows a supporting hyperplane of a containing polyhedron to be used at its touching point only when that point is outside Sigma(P) and Q_T has the stated ray normal cone there. It does not identify the containing facet with a facet of Q_T, guarantee that a maximal lattice-free container touches Q_T on every facet, or prove the required contact regularity.

## 2. Full ambient first variation of a cap

Fix a nonvertical cap

    H={ (z,x): a.z+u.x>=b },        u!=0.

For each p let

    F_p=K_p intersect {x:a.p+u.x=b}.

Assume every nonproper fiber trace satisfies H_(d-1)(F_p)=0. Here a proper trace means that its hyperplane meets int(K_p). Define

    s_p=H_(d-1)(F_p)/|u|,        S=sum_p s_p.

For a proper trace, s_p>0. When s_p>0 let g_p be the ordinary (d-1)-dimensional centroid of F_p. For d=1, a proper section is a single point and H_0 is counting measure. Empty and zero-measure sections contribute zero, with no centroid required.

For any parameter variation (a',u',b'), the directional derivative of cap mass is

    d/dt|_(t=0) mu{(a+t a').z+(u+t u').x>=b+t b'}
       =sum_p integral_(F_p) (a'.p+u'.x-b')/|u| dH_(d-1)(x)
       =sum_p s_p(a'.p+u'.g_p-b').                 (1)

The derivative is two-sided and is with respect to the full ambient normal, including the integer-coordinate coefficients a.

Proof. There are finitely many fibers, so it is enough to work on one. Choose orthogonal continuous coordinates in which u/|u| is the last coordinate direction. For sufficiently small t, the varying boundary is a graph over the original plane; solving its linear equation gives a threshold change whose first-order term is

    -t(a'.p+u'.x-b')/|u|.

For a proper section, almost every point in its (d-1)-dimensional relative interior is interior to K_p. The omitted relative boundary has (d-1)-measure zero. Along the perpendicular lines through those points, the change of the cut interval divided by t converges to the displayed affine integrand with the correct positive sign for an enlarging cap. All involved graphs and bodies are bounded. Each interval changes by at most a fixed constant times |t|, so dominated convergence on a bounded plane projection proves (1).

For a nonproper trace of zero (d-1)-measure, the entire change is contained in a slab of width O(|t|) around the original supporting plane. The supremum of its parallel section areas tends to zero. Indeed, any sequence of nearby sections has, after plane identification, every limit point in the original section; if that section has zero (d-1)-measure, bounded convex-set volume continuity forces those section areas to tend to zero. The slab therefore has volume o(|t|), yielding zero derivative. Strictly disjoint and strictly containing traces are constant for small t. This proves (1) in all the stated cases.

The zero-section condition is essential: a supporting facet with positive (d-1)-measure generally creates one-sided cap derivatives and cannot be silently included in (1).

## 3. One regular active cap exposes only one point

Suppose the cap in Section 2 has mass T, S>0, and its boundary contains a point Y in D_T. Define its mixed section centroid

    Z_H=(1/S) sum_p s_p (p,g_p).

Then Y=Z_H. Consequently

    D_T intersect boundary(H)={Z_H}.               (2)

Proof. Write v=(a,u). For every ambient perturbation w=(a',u'), the cap

    {(z,x):(v+t w).((z,x)-Y)>=0}

contains Y, and so has mass at least T. At t=0 its mass is T. The two-sided derivative must vanish. Formula (1), with b'=w.Y, gives

    0=S w.(Z_H-Y)

for every w in R^(n+d). Since S>0, this forces equality of the full ambient points. The same reasoning applies to every point of the intersection in (2).

Moreover D_T lies in the closed complementary halfspace of H. Moving the threshold above b by any sufficiently small positive amount decreases cap mass strictly, since a proper section exists and its nearby section areas are positive. Larger positive shifts have no greater mass. Thus no point of D_T can have v.Y>b. This also justifies the language of an exposed point.

At a regular base contact z_0 outside Sigma(P), (2) has an additional exact consequence:

    sum_p s_p(p-z_0)=0,
    sum_p s_p(g_p-x_0)=0.                          (3)

The bases with s_p>0 must affinely span R^n, and z_0 is in the interior of their convex hull. Otherwise z_0 lies in the convex hull of a lower-dimensional subset of P and hence in Sigma(P). In particular every such regular critical cap properly cuts at least n+1 distinct positive-volume fibers. This is a section-balance certificate, not a mass-payment inequality.

## 4. Positive-dimensional projected faces force a singular cap

Suppose an exposed face F of Q_T has positive dimension and is certified by a positive circuit of active caps as in Section 1, with the circuit's projected normal equal to a positive multiple of the normal exposing F. Let

    E=D_T intersect {ell.z=ell.z_0}.

Its projection is F. Since the complementary inequalities of all circuit caps hold on D_T and their positive sum is exactly the projected supporting inequality, equality on E forces equality in each individual cap inequality. Thus E lies in the boundary of every circuit cap.

If even one circuit cap satisfied Section 2 and had S>0, Section 3 would make E a singleton, contradicting positive dimension of its projection. Therefore every cap of such a circuit must either have zero total coarea S or have a nonproper fiber trace of positive (d-1)-measure. This includes the facet case when n>=2. A statement claiming such circuits are automatically differentiable at projected facets is false without additional hypotheses.

## 5. Strictly convex fibers and nonresonant levels

Assume d>=2 and every K_p is strictly convex. Every supporting section then contains at most one point and has zero (d-1)-measure. Hence every nonvertical cap satisfies the nonproper-section assumption of Section 2.

Assume also the finite nonresonance condition

    T not in {sum_(p in A)|K_p|: A subset P}.        (4)

A nonvertical mass-T cap must properly cut at least one fiber: otherwise every fiber contributes either its whole volume or zero, making its mass one of the forbidden subset sums. Thus S>0 for every nonvertical mass-T cap.

It follows that when n>=2, Q_T has no facet with a relative-interior point outside Sigma(P). If it had one, the regular-facet circuit theorem would supply a circuit to which Section 4 applies, whereas every cap is regular with positive S. Every facet which does occur must therefore lie in

    conv(P intersect aff(F)),

and its affine hull is a rational hyperplane spanned by actual bases. To verify this last inference directly, use the finite union defining Sigma(P). Pieces whose affine hull differs from aff(F) meet F in dimension at most n-2 and cannot cover any relatively open subset. All remaining pieces lie in conv(P intersect aff(F)). The complement of the lower-dimensional intersections is dense in relint(F), so closure proves the displayed containment; one remaining piece must have dimension n-1, proving rationality.

This is not a global strict-convexity claim for Q_T. Pure integer caps, exceptional skeleton contacts, and resonant levels are not covered by the differentiable-cap argument. For n=1 a projected endpoint is zero-dimensional, so the obstruction in Section 4 does not apply. For d=1 tangent section mass is H_0 and strict convexity of intervals does not remove it. These exclusions are necessary parts of the theorem.

## 6. Research implication and unresolved step

The ray-normal version gives actual small critical circuits at regular smooth projected contacts as well as at regular facets. Conversely, smooth fiber data at nonresonant levels rule out regular facets themselves in integer dimension at least two. Therefore one cannot routinely replace a maximal lattice-free container facet by an actual projected depth facet.

The equations (3) retain full integer-base section balance in each regular cap. No estimate converting these balances into Gamma_d times an exterior mass is proved here. Existing scalar Doignon threshold bounds, including pending `af89470c3209e9d8`, already account for the direct cap-volume superlevel argument; that argument is not claimed as a new consequence of the circuit mechanism.


## Appendix A. Complete local active-cap representation

The raw depth region equals the intersection of closed complements of all nonvertical caps of mass less than T. Indeed, a point in D_T lies strictly outside each such cap. Conversely, if a cap of mass less than T contains a point, lower its threshold slightly while retaining mass less than T by continuity from above; choose the lowered threshold to avoid the finitely many atoms in the cap-coordinate pushforward. A sufficiently small perturbation makes its continuous normal nonzero while preserving its strict containment of the point and mass less than T. That point violates a complementary closed inequality. This proves the representation, closedness, and convexity. Strict separation from the compact convex hull of supp(mu) gives depth zero outside that hull, so D_T is compact.

Fix Y_0=(z_0,x_0) with z_0 outside Sigma(P). Bad caps of mass less than T whose boundaries approach Y_0 have bounded base tilt after normalizing |u|=1. Otherwise take cap parameters (a_j,u_j,b_j), boundary points Y_j->Y_0, and |a_j|->infinity. A subsequence has a_j/|a_j|->a with |a|=1. Let P_+,P_0,P_- be the bases with positive, zero, or negative a.(p-z_0). Every late cap includes every whole P_+ fiber, hence their total mass m_+ is strictly below T. The base point z_0 is not in conv(P_0), since that convex hull is a piece of Sigma(P). Strict separation supplies v with v.(p-z_0)<0 on P_0. Choose a sufficiently large multiple Bv to exclude all P_0 fibers in a cap through Y_0 with any fixed unit continuous normal; then add a still larger multiple Aa to include every P_+ fiber and exclude every P_- fiber. If P_0 is empty omit Bv. The resulting actual cap through Y_0 has mass exactly m_+<T, a contradiction. Thus a ball around Y_0 and a finite bound on |a| exist.

Close the parameter set of these normalized bad caps whose boundaries meet that ball. It is compact: the base tilt is bounded and meeting the bounded ball bounds b. Nonvertical cap mass is continuous by dominated convergence on finitely many fibers, because each boundary hyperplane has zero d-volume there. Every limiting cap has mass at most T and its complementary inequality holds on D_T. Locally these limiting inequalities describe D_T exactly; omitted bad-cap boundaries do not meet the ball and their caps are disjoint from it, since they exclude Y_0. At an active limiting constraint, its cap contains Y_0 and therefore has mass exactly T.

Let A_0 be the compact set of active ambient normals. If it is empty, the local compact inequality family has uniform slack and Y_0 is interior. Thus at a boundary point it is nonempty. Choose G and r>0 with the ambient ball B(G,r) contained in D_T. Each active normal N satisfies

    N.(G-Y_0)<=-r|N|<=-r.

Its convex hull has the same strict bound. The positive cone over this compact convex hull is closed: the displayed dot product bounds the positive scalar in every converging sequence of cone points.

Every supporting normal q of D_T at Y_0 belongs to this cone. If not, separate it from the closed cone, obtaining v with q.v>0 and N.v<=0 for every active N. Adding a sufficiently small positive multiple of G-Y_0 preserves q.v>0 and makes the active inequalities uniformly strict. Compactness gives the same strict direction on a neighborhood of active constraints; the compact complement has uniform positive slack at Y_0. A sufficiently short move along v therefore satisfies every local inequality, putting a point of D_T on the strictly wrong side of its supporting plane, a contradiction.

The cone consists of finite positive combinations by definition. This establishes precisely the representation used in Section 1, with no facet assumption and no unpublished premise.
