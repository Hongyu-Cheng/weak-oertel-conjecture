# The induced cap section and an exact obstruction to lifting its center

Research draft, 6 November 2026. This note verifies the dimension-reduced mixed source on a nonvertical cap section, then gives an exact obstruction to the direct induction step that would lift a deepest point of that section without paying an ambient cap loss. It does not refute OC or every possible induction on continuous dimension.

## 1. Exact lower-dimensional induced source and measure

Let C be a convex body in R^n x R^d, d>=2. For this section assume every nonempty integer fiber K_p is full-dimensional; more generally it suffices that every zero-d-volume original fiber has zero (d-1)-measure in the cutting hyperplane. This assumption is needed to identify the induced section measure with the original cap coarea, as the final example below shows. Let

    H_0={ (z,x):a.z+u.x=b },       u!=0.

Suppose H_0 properly cuts at least one positive fiber. Rotate only the continuous coordinates to write x=(s,t), s in R^(d-1), with u.x=|u|t. The affine map

    Phi(z,s)=(z,s,(b-a.z)/|u|)

maps R^n x R^(d-1) bijectively onto H_0 and preserves every integer base. Put

    C_0=Phi^(-1)(C intersect H_0),
    S_0=C_0 intersect (Z^n x R^(d-1)).

The section is proper in the full ambient body: the properly cut fiber supplies points of C on both sides, which implies H_0 meets int(C). Therefore C_0 is a full-dimensional compact convex body in R^(n+d-1). The induced mixed intersection is exactly Phi(S_0)=C intersect H_0 intersect (Z^n x R^d).

On each fixed base p, Phi is an isometry in the d-1 continuous variables. Thus the intrinsic mixed section measure is exactly

    nu=sum_p H_(d-1)|[K_p intersect (H_0)_p].

In particular, no extra factor involving the base tilt a appears in the fiber measure. If every positive original fiber is either properly cut or has a nonproper section of zero (d-1)-measure, the full two-sided first-variation formula applies and uses nu/|u|, a common scalar multiple, so its normalized centroid is the same as the centroid of nu. This extra regularity condition is needed for a derivative statement: a supporting positive-area facet can otherwise create unequal one-sided derivatives. The geometric induced-section identity above remains valid regardless of that regularity. Ambient H_(n+d-1) on H_0 is not being substituted for this mixed section measure.

If a positive section coarea exists, the section has q_0=d-1 and finite positive total nu mass. Lower-dimensional section fibers contribute zero to nu. The affine map takes every halfspace with a nonzero normal in the new coordinates to an intersection of H_0 with an ambient halfspace. Conversely, an ambient halfspace whose defining affine function restricts nonconstantly to H_0 induces such a halfspace in the new coordinates. A constant restriction instead gives all of H_0 or the empty set; these trivial restrictions do not lower the depth of a point in the section. Thus the affine bijection gives an exact dimension reduction of the source and its relevant halfspace family.

## 2. The full first-variation balance causes a strict lifting loss

Use the finite-fiber cap measure mu from the original source. Let

    H={X:v.X>=b},       v=(a,u),       u!=0,
    mu(H)=T,

and suppose the cap has the full ambient first-variation formula

    d/dt|_0 mu{(v+t w).X>=b+t c}
       =S(w.Y_0-c),       S>0,                    (1)

where Y_0 is the normalized mixed section centroid. Formula (1) is proved directly for proper sections and nonproper sections of zero (d-1)-measure in Sections 2--3 of the companion contact note. It includes variation of the integer-coordinate normal coefficients, not only rotations within continuous space.

Suppose Y_0 lies in boundary(H). For every other point Z on boundary(H), set w=Z-Y_0. The halfspaces

    H_t(Z)={X:(v+t w).(X-Z)>=0}

are genuine nonvertical ambient closed halfspaces for all sufficiently small positive t. Their boundaries contain Z. At t=0 they equal H, since v.Z=b. Equation (1) gives

    mu(H_t(Z))=T-t S|Z-Y_0|^2+o(t)<T             (2)

for all sufficiently small positive t. Consequently the original ambient depth of Z is strictly below T.

If Y_0 is an active regular contact with a noninteger base, every actual point of its induced section differs from Y_0. Thus every such actual point has original ambient depth below T, regardless of how large its depth is within the induced section. A proof using an induction hypothesis on S_0 must account for the loss in (2); section depth alone cannot remove this linear normal-variation term.

## 3. A complete product certificate with an optimal lower-dimensional center

Take n=1,d=2 and

    C=[0,1] x D,
    D={(x_1,x_2):x_1^2+x_2^2<=1}.

This is an actual full-dimensional convex body. Its induced source consists of exactly two unit disks, at bases 0 and 1, of total mixed area 2pi.

Define the disk cap function

    f(t)=|D intersect {x_2>=t}|.

It equals pi for t<=-1, zero for t>=1, and for -1<=t<=1 it is

    f(t)=pi/2-arcsin(t)-t sqrt(1-t^2).

It satisfies f(-t)=pi-f(t), is decreasing, and is globally 2-Lipschitz. On the interior of its support,

    f'(t)=-2 sqrt(1-t^2),

with derivative zero outside [-1,1]; the displayed derivative extends continuously to the endpoints.

Put

    Y_0=(1/2,0,1/2),
    H={x_2>=1/2},
    T=2 f(1/2)=2pi/3-sqrt(3)/2.                   (3)

We verify that Y_0 has original ambient depth exactly T. For any nonzero continuous normal, normalize it to a unit vector e. A through-Y_0 cap has disk thresholds t+h and t-h on its two fibers, where t=(1/2)e_2 belongs to [-1/2,1/2] and h is an arbitrary real integer-tilt parameter. Its total mass is f(t+h)+f(t-h).

For t>=0, this sum is minimized at h=0. By symmetry assume h>=0. Its derivative in h is f'(t+h)-f'(t-h)>=0, since |t+h|>=|t-h| and sqrt((1-s^2)_+) decreases with |s|. Hence the mass is at least 2f(t)>=2f(1/2)=T. For t<=0 it is at least pi: indeed for s=-t>=0, monotonicity and f(-r)=pi-f(r) give f(s+h)+f(s-h)<=pi, and the negative-t sum is its complement in 2pi. Pure integer through-point caps contain one whole disk and have mass at least pi>T. Containing halfspaces reduce to through-point halfspaces. The particular H in (3) attains T, proving the claim.

The depth region D_T has nonempty ambient interior, so the example also fits that requirement of the regular projected-contact framework. To see this without assuming continuity of mixed depth, take Y=(z,x) with |z-1/2|<=epsilon and |x|<=epsilon, where epsilon<1/8. Normalize the continuous normal to unit length. If the absolute integer coefficient is at least 4, the two disk thresholds lie strictly beyond opposite endpoints -1 and 1, so the cap mass is pi. If that coefficient has absolute value at most 4, the common threshold displacement from its value through (1/2,0,0) is at most 5epsilon. Global 2-Lipschitz continuity of f on each of two fibers gives cap mass at least pi-20epsilon. Choose additionally epsilon<(pi-T)/20. Every such point then has depth greater than T; pure integer caps again have mass pi. Thus a neighborhood of (1/2,0,0) lies in D_T.

The section H_0=boundary(H) has, in coordinates (z,x_1), the induced body

    C_0=[0,1] x [-sqrt(3)/2,sqrt(3)/2].

Its mixed source is two equal intervals, each of length sqrt(3). Its exact maximal mixed halfspace depth is sqrt(3)/2, attained at the two actual interval centers

    Z_0=(0,0,1/2),       Z_1=(1,0,1/2).

For a lower bound, any containing section halfspace at an interval center captures at least half that own interval, including pure integer directions. For the upper bound at any actual point, an arbitrarily large integer tilt isolates the own interval while its continuous trace captures the shorter of the two parts cut at that point; this has length at most sqrt(3)/2. Equality is possible only at the interval center. Hence these are exactly the section maximizers, attaining the sharp n=1,d=1 fraction 1/4 of the section's total mass.

Nevertheless neither point has original ambient depth T. At Z_0 use

    H_t^0={x_2-tz>=1/2},       0<t<1/2.

Its mass is f(1/2)+f(1/2+t)<T. At Z_1 use

    H_t^1={x_2+t(z-1)>=1/2},

with the same mass. More precisely both masses equal

    T-sqrt(3)t+o(t).

The original cap section has total coarea 2sqrt(3) and centroid Y_0, so this loss agrees exactly with (1). The active boundary properly cuts both strictly convex fibers; there are no supporting-facet derivative ambiguities, vertical boundary atoms, missing fibers, or approximation limits.

The example is not an OC counterexample. The original fiber centers (0,0,0) and (1,0,0) each have mixed depth at least pi/2, which exceeds the sharp OC target 4pi/9 for total mass 2pi. It only disproves the proposed bridge from an optimal induced-section center to the active parent level T.


## 4. Boundary-fiber birth can also change the section measure

If the assumption in Section 1 concerning zero-volume original fibers is omitted, the dimension-reduced induced measure need not equal the first-variation measure. Here is an exact example with a regular active cap and a depth region with ambient interior.

Let D' be the unit disk centered at (0,-1/2), and let

    I'={ (s,0): |s|<=sqrt(3)/2 } subset D'.

Take the actual convex body

    C'=conv[ ({-1} x D') union ({0} x D') union ({1} x I') ].

Its integer fibers are exactly D' at -1 and 0 and I' at 1. At the extreme bases this follows from extremality. At the middle base, the only additional points arise from averaging the two extreme fibers, and (D'+I')/2 subset D' because I' subset D' and D' is convex. The body has ambient interior because it contains [-1,0] x D'.

Its original mixed area is therefore 2pi; the last fiber contributes zero. The original mixed measure is an affine translate of the two-disk measure in Section 3. In particular the cap H'={x_2>=0} has mass T from (3), is active at

    Y'_0=(-1/2,0,0),

and its depth region D_T has nonempty ambient interior. Its two proper positive-fiber sections each have length sqrt(3). Thus its original cap coarea measure has total mass 2sqrt(3) and centroid Y'_0. The zero-area original fiber contributes nothing to this derivative, for any perturbation.

But the actual induced section C' intersect {x_2=0} is the rectangle

    [-1,1] x [-sqrt(3)/2,sqrt(3)/2]

in (z,x_1) coordinates: the containment follows from C' subset [-1,1] x D', and all three matching segment fibers and their convex hull are present. Its induced mixed section has THREE intervals of length sqrt(3), so its measure has total mass 3sqrt(3) and centroid

    Z'=(0,0,0).

This point is actual and has section depth exactly 3sqrt(3)/2, half the section total. For a nonzero continuous normal, the two outer interval cap masses sum to one full interval length by symmetry, and the middle cap contributes half; pure integer through-center caps contain two whole intervals. Opposite nonvertical caps have boundary measure zero and total equal to the section mass, giving the matching upper bound.

Despite this maximally deep actual section centroid, its original ambient depth is strictly below T. The caps

    {x_2+t z>=0},       0<t<1/2,

contain Z'. On the positive original fibers their masses sum to f(1/2+t)+f(1/2)<T, and the degenerate last fiber still contributes zero original area.

Thus the actual lower-dimensional section may acquire positive intrinsic mass from a fiber which had zero mass before taking the section. In general the induced section measure equals the geometric section measure of the original positive fibers PLUS these new boundary-fiber contributions. Under the regularity condition stated in Section 1, the former agrees, up to the common |u| factor, with the original cap first-variation measure. An induction using the true induced section must either control this extra measure or explicitly exclude it. Treating its centroid as the original cap's section centroid is incorrect.
