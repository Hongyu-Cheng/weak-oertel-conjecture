# Continuum source weights in the descendant hitting construction

Scoped extension, 6 November 2026. This supplies the measure-theoretic step
needed for translated shrunken partner simplices; it makes no independent
claim about their actual mixed-fiber realization.

Let I be a compact metric space with a finite nonnegative Borel measure nu.
Let P_i subset B be full-dimensional simplices, indexed by i in I, such
that the map i -> P_i is continuous in the Hausdorff metric. Assume

    |B|=vV, |P_i|>=2^(-d)V, nu(I)=1-v.

Replace the finite strict-source sum by

    F(H)=|B intersect H|/V
          +integral_I 1{P_i intersect int(H) is nonempty} dnu(i).

Then the one-cap descendant theorem, including its d>=3 endpoint, and the
capacity-deficit extension remain valid with exactly the same hypotheses,
constants, deterministic centers, and every-containing-halfspace conclusion.

For a unit normal u through g_B, the strict-source indicator is

    1{h_(P_i)(u)>u dot g_B}.

Its support-function difference is jointly continuous in (i,u): the bodies
all lie in the common compact B, so the standard support estimate is
|h_P(u)-h_Q(w)|<=d_H(P,Q)+R|u-w| after enclosing B in a radius-R ball.
Thus the integrand is Borel measurable and lower semicontinuous. If u_j
converges to u, the pointwise lower-semicontinuity and Fatou's lemma yield

    integral f(i,u) dnu <=liminf_j integral f(i,u_j) dnu.

Adding the continuous own-cap mass makes F lower semicontinuous on the
compact sphere. Its minimum is attained; the lexicographically least
minimizer remains a deterministic choice.

For a selected bad cap, the missed index set

    I_0={i:h_(P_i)(u)<=u dot g_B}

is closed, hence measurable. Its mass m replaces the finite sum of missed
weights. The original algebra gives m>0, so I_0 is nonempty and its retained
body contains a full-dimensional source. When that body's volume is below
the half-volume threshold, the ordinary simplex-containment inequality puts
the retained centroid in int(P_i) for EVERY i in I_0. Hence each of their
strict-source indicators equals one for every through-centroid halfspace;
the full m is credited at once. No selection of individual indices and no
interchange of infima with integrals occurs.

At the endpoint the same assertion follows either from the proved
half-volume-frustum interior lemma or from the impossibility of a sharp
ordinary centroid cap missing such a large source, using the exact frustum
simplex capacity. The capacity-deficit extension likewise uses only the
existence of one missed source to invoke its ordinary deficit bound, and
then credits every index in I_0. All remaining inequalities are unchanged.

For the intended translated-source form, take I to be a finite disjoint
union of compact convex bodies A_j, give each component a nonnegative
constant multiple of Lebesgue measure, and put

    P_p=(p+C_j^theta)/2, p in A_j,

where C_j^theta is a fixed full-dimensional simplex. Translation makes
p -> P_p continuous. Clipping the weights by constants in [0,1] preserves
all hypotheses once their total mass is set to 1-v. The argument establishes
only this continuum hitting statement; the actual endpoint-cap lower bound
must be proved separately in its mixed-fiber consumer.
