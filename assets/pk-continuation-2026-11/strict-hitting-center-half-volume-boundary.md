# A strict source-simplex hitting center at the half-volume boundary

Scoped research lemma, 6 November 2026. The source-simplex hitting problem
for arbitrary middle bodies remains unresolved outside the parameter range
below. The point of this note is to close the strict-support boundary case;
weak containment of the centroid alone is not silently used as strict hitting.

Let B be a convex d-body, d>=1, with |B|=vV, V>0, and

    0<v<=2^(1-d).

Let P_1,...,P_k be full-dimensional simplices contained in B, each with
volume at least 2^(-d)V. Give them nonnegative normalized weights e_i
summing to E=1-v. For every closed halfspace H define its score

    F(H)=|B intersect H|/V
           +sum_i e_i 1{P_i intersect int(H) is nonempty}.

Then there is a single deterministic point y in B such that

    F(H)>=Gamma_d,    Gamma_d=(d/(d+1))^d,             (1)

for every closed halfspace containing y. When d>=2 the score has a uniform
strict surplus above Gamma_d; the same is true for d=1 and v<1. The case
d=1, v=1 permits equality. Zero-weight sources can be discarded.
All assertions are in the continuous d-space; no full mixed OC conclusion is
asserted.

The ordinary geometric input is the proved inscribed-simplex containment
inequality: if P subset B is a simplex of volume a and lambda is one of its
barycentric coordinates, then

    lambda(g_B)>=(2-|B|/a)/(d+1).                     (2)

Its first-moment proof additionally gives, when lambda(g_B)=0 and
|P|=|B|/2,

    |B intersect {lambda<0}|=|P|,
    B intersect {lambda>=0}=P.                       (3)

For clarity, the equality deduction in (3) requires no unstated equality
classification: if m=|B intersect {lambda<0}|, that proof gives
0>=a/(d+1)-m^2/[(d+1)a] and m<=|B|-a=a. Hence m=a. The other half
of B has volume a and contains P, so the two compact convex full-dimensional
bodies are equal. This is the already proved ordinary moment lemma, not an
assumption of a mixed hitting principle.

If v<2^(1-d), every P_i has volume strictly greater than |B|/2. Equation
(2) puts g_B in the interior of every P_i. Every through-g_B halfspace
therefore strictly hits every source, while the own cap has normalized mass
at least Gamma_d v. Consequently

    F(H)>=Gamma_d v+E
         =Gamma_d+(1-Gamma_d)(1-v)>Gamma_d.

Containing halfspaces reduce to through-point halfspaces by monotonicity.

It remains to handle v=2^(1-d). For d=1 this means v=1 and E=0, so the
midpoint of the interval B gives (1) directly. Hence assume d>=2; then
Gamma:=Gamma_d<1/2. Equation (2) puts g:=g_B in every P_i.

A source having g in its interior is strictly hit by every through-g halfspace.
If g is on its boundary, (2) forces |P_i|=|B|/2. Take a facet of P_i through
g and apply (3). Thus P_i is exactly one half of B cut by that facet. Since
g is an interior point of B, it is in the relative interior of this facet of
P_i. In particular there is only one oriented through-g halfspace which
fails to strictly hit P_i, namely the exterior halfspace across this facet.
This uniqueness also follows locally: near g the source agrees with the
intersection of an open ball and one closed halfspace.

It follows that any through-g halfspace which misses at least one source has
own normalized B mass v/2. All sources it misses coincide with the same
half-body P=B intersect H^-, by (3) and equality of their volumes. Let m
be the sum of the weights of this coincident-source class. The score of that
halfspace at g is exactly

    v/2+E-m.

If all these finitely many class scores are strictly greater than Gamma,
take y=g. Every other orientation hits all sources and has score at least
Gamma v+E=Gamma+(1-Gamma)E>Gamma. The minimum of this positive gap and
the finitely many positive class-score gaps is a uniform strict surplus.
If there are no boundary classes, only the first positive gap is needed.

Otherwise choose the class with the first input index among those with

    m>=v/2+E-Gamma=1-v/2-Gamma.

This is a deterministic choice from a finite family. Crucially,

    (1-v/2-Gamma)-Gamma E
      =(1-2Gamma)(1-v/2)>0.                          (4)

Therefore delta:=m-Gamma E>0. The selected simplex P has g on its boundary;
write g_P for its centroid and ell=|g_P-g|>0. Choose R>0 with B subset
g+R B_2^d, and put

    L=vol_(d-1)(B_2^(d-1)) R^(d-1)/V,
    t=min{1/2,delta/(2L ell)},
    y=(1-t)g+t g_P.                                  (5)

Then y is in the interior of P and hence belongs to B. In every unit-normal
direction, moving the through-point threshold from g to y changes the
normalized B-cap volume by at most L|y-g|: integrate the section areas,
each of which is at most vol_(d-1)(B_2^(d-1))R^(d-1). Thus every through-y
halfspace has own normalized B mass at least Gamma v-delta/2.

Every such halfspace now strictly hits every source in the selected class,
because y is in their common interior. That class alone contributes m,
so for all through-y halfspaces

    F(H)>=Gamma v-delta/2+m=Gamma+delta/2>Gamma.        (6)

All other sources have nonnegative contributions and need no stability
analysis. Monotonicity again extends (6) to containing halfspaces. This
proves (1) with a uniform strict surplus, including exact equality in the
source volume threshold for d>=2.

The explicit displacement in (5) is the reason a boundary source can be
repaired without treating boundary contact as strict support. The result
does not address the range 2^(1-d)<v<=1, which is the remaining substantial
part of the general source-simplex hitting problem.
