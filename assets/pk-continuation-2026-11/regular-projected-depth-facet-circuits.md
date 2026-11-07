# Exact critical circuits away from the rational base skeleton

Research draft, 6 November 2026. This is an auxiliary regularity and contact-certificate theorem, not a sharp mixed-integer depth bound. All measure in this note is full fiber volume. No intrinsic lower-dimensional extension is asserted.

Let n,d>=1. Let P be a finite subset of Z^n, and for p in P let K_p be a compact convex d-dimensional body in R^d. Put

    mu = sum_(p in P) delta_p x Lebesgue_d|K_p,
    M = mu(R^(n+d)).

The theorem does not require that the family come from one ambient convex body. Define raw ambient closed-halfspace depth and its superlevel by

    h(y)=inf_{closed ambient halfspaces H containing y} mu(H),
    D_T={y:h(y)>=T},           0<T<M.

Assume D_T has nonempty ambient interior. It is compact and convex. Let Q_T be its projection to R^n. Define the finite rational base skeleton

    Sigma(P)=union {conv(A): A subset P, affdim(A)<n}.

Empty A can be omitted. This is a finite union of compact polytopes of dimension at most n-1. In particular it is closed.

## 1. The local bounded-tilt theorem

Fix y_0=(z_0,x_0) in D_T with z_0 not in Sigma(P). Then there are rho>0 and L<infinity such that every nonvertical cap

    H={ (z,x): a.z+u.x>=b },       |u|=1,

of mass mu(H)<T whose boundary meets the ball B(y_0,rho) satisfies |a|<=L.

Proof. Otherwise there are such caps H_k, points y_k=(z_k,x_k) on their boundaries with y_k->y_0, and |a_k|->infinity. Passing to a subsequence gives a_k/|a_k|->a, |a|=1. Set

    P_+={p:a.(p-z_0)>0},
    P_0={p:a.(p-z_0)=0},
    P_-={p:a.(p-z_0)<0}.

For each p in P_+, the entire bounded fiber K_p lies in H_k for all sufficiently large k. Indeed its margin divided by |a_k| tends uniformly on that fiber to a.(p-z_0)>0; use b_k=a_k.z_k+u_k.x_k and |u_k|=1. Finiteness of P makes the assertion simultaneous. Consequently

    m_+:=sum_(p in P_+) |K_p| < T.

The inequality is strict because one sufficiently late H_k already contains every P_+ fiber and has mass strictly below T.

The affine hull of P_0 has dimension at most n-1. Thus z_0 is not in conv(P_0). If P_0 is nonempty, strict separation from its compact convex hull supplies v in R^n such that

    v.(p-z_0)<0 for every p in P_0.

Choose any unit continuous normal u. First choose B>0 large enough that

    B v.(p-z_0)+u.(x-x_0)<0

for all p in P_0 and x in K_p. Then choose A>0 large enough that the finite cap through y_0 with margin

    A a.(p-z_0)+B v.(p-z_0)+u.(x-x_0)

is strictly positive throughout every P_+ fiber and strictly negative throughout every P_- fiber. Its P_0 margins remain strictly negative. If P_0 is empty, omit Bv. This is a genuine nonvertical ambient cap containing y_0, with mass exactly m_+<T, contradicting y_0 in D_T. QED.

Notice that the argument uses the convex hull of the boundary bases, not merely their affine hull: the secondary finite tilt must put all of those actual bases on the excluded side. The hypothesis z_0 outside Sigma(P) guarantees precisely the needed strict separation for every possible limiting direction.

## 2. A compact local description by actual cap limits

A nonvertical cap has boundary mu-measure zero, and its mass is continuous in its parameters while its continuous normal remains nonzero. This follows by dominated convergence on the finitely many fibers.

The depth region satisfies

    D_T = intersection_{nonvertical H, mu(H)<T} {a.z+u.x<=b},

where H is written a.z+u.x>=b. To verify this, a point in D_T lies strictly outside each bad closed cap. Conversely, if a bad cap contains a point, first lower its threshold slightly while preserving mass<T, using continuity from above. The point then lies strictly inside. Choose the lower threshold so that its boundary has zero mu-mass, which is possible because there are only finitely many atoms in the one-dimensional pushforward. A sufficiently small perturbation of the normal gives a nonvertical bad cap still containing the point strictly. Thus that point violates one of the displayed closed complementary inequalities. This also proves closedness and convexity. A point outside conv(supp mu) has depth zero by strict separation, so D_T is compact.

Take rho,L from Section 1. Retain all normalized bad caps whose boundaries meet B(y_0,rho), and close their parameter set. The result, denoted A, is compact: |a|<=L, |u|=1, and the boundary-intersection condition bounds b. Every limit still has continuous normal of norm one, mass<=T, and its complementary halfspace contains D_T.

Inside B(y_0,rho), the inequalities indexed by A describe D_T exactly. An omitted bad cap has boundary disjoint from this ball. Since it does not contain y_0, it is disjoint from the entire ball and its complementary inequality is redundant there.

Let A_0 be the subfamily active at y_0, meaning b=a.z_0+u.x_0. Every active limiting cap has mass exactly T: its mass is at most T by continuity, and at least T because it is a closed cap containing y_0 in D_T.

## 3. Exact normal-cone representation

Write N=a,u for each ambient normal in A. Every supporting normal of D_T at y_0 belongs to the cone generated by the active normals in A_0.

Here is a direct proof, including the closure issue. Choose g in int(D_T), and r>0 with B(g,r) contained in D_T. For every active normal N,

    N.(g-y_0)<=-r|N|<=-r.

The active normals form a compact set. Their convex hull also satisfies the last strict inequality. Its positive cone is closed: in any convergent sequence t_k v_k with v_k in that convex hull, the displayed inequality bounds t_k, after which compactness gives a convergent subsequence of both factors.

If a supporting normal q were outside this closed cone, separation gives a vector v with q.v>0 and N.v<=0 for every active N. Replacing v by v+epsilon(g-y_0) for sufficiently small epsilon preserves q.v>0 and makes every active dot product uniformly negative. Compactness then supplies a neighborhood of A_0 in the parameter set on which the same strict inequality holds. On its compact complement the slack b-N.y_0 has a positive minimum. For sufficiently small t>0, all inequalities in A therefore hold at y_0+t v. Also this point stays inside B(y_0,rho). Section 2 puts it in D_T, contradicting the supporting inequality q.v>0. This proves the claim.

Finite-dimensional conic Caratheodory gives a representation by at most n+d active normals. For completeness, start with any finite conic representation; if it uses more than n+d nonzero vectors, a linear dependence permits changing the positive coefficients until one becomes zero, retaining nonnegativity and the same sum. Repetition gives the bound. The cone is the union of finite conic combinations by its definition.

## 4. A projected facet has one exact small critical circuit

Suppose F is a facet of Q_T and choose

    z_0 in relint(F) outside Sigma(P),
    y_0=(z_0,x_0) in D_T.

Let ell.z<=c define its outward supporting inequality. The lifted vector (ell,0) is a supporting normal of D_T at y_0. Section 3 represents it as a positive combination of finitely many active cap normals (a_i,u_i). In particular the coefficient vector lambda satisfies

    sum_i lambda_i u_i=0.

Decompose this nonnegative continuous-normal dependence into minimal positive dependences. An elementary elimination proves the decomposition: find a nonzero nonnegative kernel vector of minimal support within the current support, subtract its largest allowable positive multiple, remove a zero coordinate, and repeat. Minimal supports have size at most d+1, and their kernel is one-dimensional. Otherwise an independent kernel perturbation of the positive coefficient vector would reach a zero coordinate and contradict support minimality.

Take one of these minimal positive circuits, with positive weights theta_i, and put

    ell'=sum_i theta_i a_i,
    c'=sum_i theta_i b_i.

The corresponding sum of valid complementary cap inequalities yields ell'.z<=c' on Q_T and is tight at z_0. Moreover ell' is nonzero: if it were zero, the weighted sum of the active ambient normals would vanish, contradicting their strictly negative dot products with g-y_0 from Section 3. Since z_0 is in the relative interior of a facet of the full-dimensional Q_T, its nonzero supporting normal ell' is a positive multiple of ell.

Thus F has an exact certificate consisting of k<=d+1 actual nonvertical ambient closed caps H_i of mass exactly T, all passing through the SAME lifted point y_0, with strictly positive weights such that

    sum_i theta_i u_i=0,
    sum_i theta_i a_i is a positive multiple of ell,
    sum_i theta_i b_i=(sum_i theta_i a_i).z_0.

The normals u_i form a minimal positive dependence. No limit cap with vertical boundary mass is being treated as a mass-T cap: |u_i|=1 remains true in every limit used in this proof.

## 5. Every possible exceptional facet is rational and supported on actual bases

A facet lacking a relative-interior point outside Sigma(P) must satisfy

    F subset conv(P intersect aff(F)).

In particular aff(F) is a rational affine hyperplane generated by integer points of P.

To prove this, use the finite union defining Sigma(P). Its pieces whose affine hull does not equal aff(F) have intersections with F of dimension at most n-2. They cannot cover a relatively open portion of F. Every remaining piece is contained in conv(P intersect aff(F)), a closed set. The complement of the lower-dimensional intersections is dense in relint(F), so closure gives the asserted containment of all F. At least one remaining piece has dimension n-1, proving rationality of its affine hull.

For n=1, Sigma(P)=P. Consequently, if Q_T avoids Z, BOTH endpoints of its interval have exact two-or-more, at most d+1, critical circuits as in Section 4. This conclusion still assumes nonempty ambient interior of D_T. It does not by itself give the sharp one-integer-variable bound.

## 6. Scope and comparison with the existing finite certificates

The finite approximation and projection-elimination arguments in candidates 207a0b33a5d3a235 and d2b290ebd8e35052 produce small circuits at auxiliary polytope contacts, with cap budget approaching T and possibly degenerating integer tilts. The present statement gives an exact mass-T certificate at an ACTUAL projected depth facet away from the explicit finite base skeleton. It also locates every possible failure of this argument on a rational hyperplane carrying actual positive source bases.

The obstruction in candidate abe945997ae088f4 is consistent with the theorem: its exceptional facet z_1=0 lies in conv{(0,0),(0,1)}, a piece of Sigma(P). At a point of that facet the depth can exceed T, so no exact mass-T active cap certificate is possible there.

The theorem proves no improvement over the union-bound constant. It does not assert that facets of an arbitrary maximal lattice-free container are facets of Q_T, that exceptional faces can be discarded, that D_T is always full-dimensional at a desired target, or that per-facet cap groups can be paid independently by Gamma_d. Those remain separate obligations.
