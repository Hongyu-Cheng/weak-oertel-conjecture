---
fact_id: ff5cdcf2fef03af8
kind: lemma
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-true-mixed-centroid-fixed-knot-directional-model
depends_on: []
verifier_run: 208e1a62e63d40c4
target_match: null
---

## Source

- [de17949888b969bf](../candidates/de17949888b969bf.json), de17949888b969bf:03 §4, exact fixed-knot directional model.

## Statement

Fix three compact axial intervals and a finite ordered knot list on each interval that contains both endpoints. Consider triples of planar bodies symmetric about $y=0$, with piecewise affine section-length profiles $f,g,h$ on those respective intervals. Among compatible triples with endpoint areas one, middle area in $[1,3]$, and true mixed centroid at the origin of the lift at bases $-1,0,1$ (middle profile $h$), the mass of the directional cap $\{x\ge0\}$ is represented exactly by a finite linear program in the knot heights. Its constraints are profile nonnegativity and concavity, the given area conditions, $\int x(f+g+h)(x)\,dx=0$, and
$$
h((x_i+x'_j)/2)\ \ge\ [f(x_i)+g(x'_j)]/2
$$
for each pair of endpoint-profile knots $x_i,x'_j$. Each averaged abscissa is required to lie in the given middle interval, even for zero-height endpoint knots. The objective is $\int_{x\ge0}(f+g+h)(x)\,dx$, extending each profile by zero outside its own interval for integration.

## Proof

The nonnegative concave piecewise affine profile $f$ defines the polygon $\{(x,y):x\in I_f,\ |y|\le f(x)/2\}$, and likewise for $g,h$. The constraints on heights are linear because the knots are fixed: neighboring chord slopes must decrease. The area and first moment integrals are linear by piecewise affine interpolation, including the integrals cut at zero. Positive areas make all three polygons full-dimensional.

The endpoint polygons are the convex hulls of their upper and lower knot points $(x_i,\pm f(x_i)/2)$ and $(x'_j,\pm g(x'_j)/2)$. Their Minkowski midpoint is the convex hull of all pairwise averages of those points, since one can multiply two finite convex combinations to express any average as a convex combination of pairwise averages. At each fixed averaged abscissa the largest possible absolute ordinate is $[f(x_i)+g(x'_j)]/4$, attained by the same-sign pair. Thus membership in the middle polygon for all these averages is equivalent to the displayed inequalities and support conditions. The middle polygon is convex, so the inequalities are exactly compatibility, and evaluation of its interpolant at fixed arguments is linear in the unknown heights.

The lifted hull has only the three listed integer bases. Its middle section is exactly the middle polygon by compatibility, and its endpoints are exact by extremality. Equal endpoint areas make the base centroid zero; symmetry gives zero transverse mean; the combined first moment equation gives zero axial mean. The resulting centroid is an actual point at the middle base by convexity. The displayed objective is its original closed-cap area because axial lines are area-null. Conversely any triple in the specified fixed-knot class obeys these same conditions by compatibility, the true centroid equation and integration, giving the exact model in both directions.
