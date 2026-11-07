# Exact atomic endpoint costs and the boundary defect in hitting limits

Research note, 6 November 2026. This is an audit of a proposed limiting model, not an assertion about arbitrary mixed-integer convex bodies.

## 1. Exact optimized cost of one atomic endpoint

Let a in R^d, let C be a full-dimensional convex body of volume c, and put a point mass e>0 at a. Let f be a nonconstant affine functional, and let tau be a middle threshold. The endpoint cuts must have thresholds tau+beta and tau-beta. Define

    L(e,a,C;f,tau)
      =inf_beta [e 1{f(a)>=tau+beta}
                 +|C intersect {f>=tau-beta}|].

Then exactly

    L(e,a,C;f,tau)
      =min(e, |C intersect {f>=2tau-f(a)}|).             (1)

Proof. If the atom is included, the cost is at least e. By taking beta sufficiently negative one includes the atom and excludes C entirely, so e is attainable. If the atom is excluded, beta>f(a)-tau. Hence tau-beta<2tau-f(a), and the C-cap has volume at least the cap in (1). Conversely let beta decrease to f(a)-tau from above. Proper hyperplanes have zero d-volume in C, so cap-volume continuity shows that the C-cap volumes converge to the cap in (1). Taking the smaller of the included-atom and excluded-atom infima proves (1). All cuts in this argument are closed; only an infimum, not a minimizing excluded-atom tilt, is asserted.

Put P=(a+C)/2. Its support value is h_P(f)=(f(a)+h_C(f))/2, using affinity of f. If h_P(f)=tau then the cap in (1) is a supporting face of C and has zero d-volume. Thus L=0 even though P intersects the closed middle halfspace {f>=tau}.

If h_P(f)<tau, L=0 as well. If h_P(f)>tau, the cap has positive volume, and L=e provided e is at most that cap volume. Consequently the small-e endpoint-cost ratio tends to

    lim_(e downarrow0) L/e = 1{h_P(f)>tau}.             (2)

The strict sign in (2) is essential.

## 2. Uniform quantitative version away from contact

Let h=h_C(f), l=min_C f, and W=h-l>0. Write eta=h_P(f)-tau. If eta>0, a homothetic copy of C toward an h-maximizing point, with ratio

    r=min(1,2eta/W),

lies in {f>=2tau-f(a)}. Hence (1) implies

    L>=min(e,c min(1,2eta/W)^d).                       (3)

In particular any family of directions for which eta/W>=delta>0 receives full atomic credit whenever e/c<=min(1,2delta)^d. Formula (3) is invariant under scaling or adding a constant to f. It gives an actual uniform margin condition; a bare intersection P cap H nonempty gives none.

## 3. A strict hitting-depth supremum need not be attained

This example concerns the limiting set-valued functional itself. Take d=1, B=[0,1], P=[0,1/2], and e>0. For y in B define

    D(y)=inf_(f nonconstant affine)
       [|B intersect {f>=f(y)}|+e 1{h_P(f)>f(y)}].

Only the two orientations matter. Therefore

    D(y)=min(1-y+e 1{y<1/2}, y+e 1{y>0}).            (4)

For 0<y<1/2, (4) gives D(y)=y+e. At y=1/2 it gives

    D(1/2)=min(1/2,1/2+e)=1/2.

For y>1/2, D(y)<=1-y<1/2; at y=0, D(0)=0. Thus

    sup_(y in B) D(y)=1/2+e,

and this supremum is not attained. In particular compactness of B alone does not justify maximizing the strict hitting functional. This example does not satisfy the separate deficit restriction e<=1-|B| and is not a counterexample to any proposed hitting theorem restricted by that condition. Its purpose is to refute the unrestricted attainment claim one might otherwise use as a routine compactness step.

Replacing > with >= restores the boundary credit at y=1/2, but contradicts the exact endpoint optimization (1). Thus a proof using the weak hitting model must separately establish a strict margin, or work with finite cap costs (1) and pass to limits with the selected centers and thresholds controlled.
