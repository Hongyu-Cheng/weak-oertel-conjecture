# Exact singleton capacities in a symmetric oblique triangle fan

Research support note, 6 November 2026. The calculations below isolate a useful source-shape mechanism, and also refute an overly strong scalar shortcut. They do not solve arbitrary oblique fans or the full two-dimensional hitting-selection problem.

## 1. Geometric normalization

Take the triangle

    B_0=conv{(-1,0),(1,0),(0,1)},       |B_0|=1.

Fix y=(0,h) with 0<h<1 and k>0. Consider the three concurrent closed halfspaces

    H_0={Y>=h},
    H_+={X-kY>=-kh},
    H_-={-X-kY>=-kh}.

Their normals positively balance with coefficients 2k,1,1. Write p_j=|B_0 intersect H_j|. To fit the deficit model, choose v in (0,1], use reference volume V=1/v, and let simplex sources P_i subset B_0 have areas at least V/4=1/(4v). Give them weights e_i summing to E=1-v. The normalized score of H_j is

    S_j=vp_j+sum_i e_i 1{P_i strictly hits H_j}.

Strict hitting means that P_i contains a point on the strict positive side. Equality at a source support is a miss.

For j in {0,+,-}, define the singleton-hit region

    R_j=B_0 intersect intersection_(l!=j) H_l^opp,

where H_l^opp is the opposite closed halfspace. A full-dimensional source hits only H_j precisely when it lies in R_j. Let b_j be the largest area of a triangle contained in R_j. These maxima exist: each R_j is a compact polygon, and the maximum-area inscribed triangle can be chosen at polygon vertices. Indeed, with two vertices fixed, its absolute area is the absolute value of an affine function of the third vertex, so its maximum over a polygon occurs at a vertex; applying this successively to a maximizing triple proves the claim.

## 2. Exact own-cap areas

The top cap is a similar triangle:

    p_0=(1-h)^2.                                   (1)

If kh<=1, the positive side cap contains only the right bottom vertex. Its edge-intercept fractions are (1+kh)/2 and (1+kh)/(1+k), so

    p_+=p_-=(1+kh)^2/[2(1+k)].                     (2)

If kh>=1, necessarily k>1, and the complement is a cap at the top vertex. Its two edge-intercept fractions give

    p_+=p_-=1-k^2(1-h)^2/(k^2-1).                  (3)

The formulas agree at kh=1.

## 3. Exact singleton capacities

The top singleton region is the quadrilateral with vertices

    y=(0,h),
    (a,s), (-a,s),
    (0,1),

where

    s=(1+kh)/(1+k),       a=k(1-h)/(1+k).

The four vertex-triangle areas are

    k(1-h)^2/(1+k)^2,
    k^2(1-h)^2/(1+k)^2,
    k(1-h)^2/[2(1+k)]  (twice).

The third value lies between the first two. Therefore

    b_0=(1-h)^2 k max(k,1)/(1+k)^2.                (4)

For the right singleton region, the defining inequalities are

    Y<=h,       X>=k(h-Y),       (X,Y) in B_0.

If kh<=1, it is the trapezoid with vertices

    (kh,0), (1,0), (1-h,h), (0,h).

The largest triangle in this trapezoid has half its height times its longer parallel edge. Thus

    b_+=b_-=(h/2) max(1-kh,1-h),       kh<=1.       (5)

If kh>=1, the region is a triangle whose upper edge has length 1-h and whose height is (1-h)/(k-1). Hence

    b_+=b_-=(1-h)^2/[2(k-1)],          kh>=1.       (6)

All capacities are exact and allow vertices on the fan boundaries.

In particular, for k>=1,

    b_+=b_-<=1/8.                                  (7)

For kh<=1 this follows from (5), which becomes h(1-h)/2<=1/8. For kh>=1, one has k>=1/h, so (6) is at most h(1-h)/2<=1/8. Since every source has area at least 1/(4v)>=1/4, no qualifying source can have singleton-hit pattern + or - in this parameter range.

## 4. A feasible top singleton forces a strong pair certificate

Assume k>=1, that the top singleton region is feasible for a source, so b_0>=1/(4v), and that its own cap alone is below Gamma_2=4/9, so vp_0<4/9. By (4),

    1/4<=vb_0=vp_0 k^2/(k+1)^2
          <(4/9)k^2/(k+1)^2.

Therefore k/(k+1)>3/4, or

    k>3.                                          (8)

We claim that for k>3,

    p_0+p_+>=16/17.                                (9)

When kh<=1, substitute (1)-(2) and minimize the resulting quadratic in h over the whole real line. The minimum is

    (k+1)^2/(k^2+2k+2)
       =1-1/[(k+1)^2+1]>16/17.

Explicitly, the quadratic coefficient is (k^2+2k+2)/(2(k+1)), its linear coefficient is -(k+2)/(k+1), and its constant coefficient is (2k+3)/(2(k+1)); completing the square gives the stated minimum.

When kh>=1, equations (1) and (3) give

    p_0+p_+=1-p_0/(k^2-1).

Since h>=1/k,

    p_0/(k^2-1)<=(k-1)/[k^2(k+1)]<=1/18

for k>=3. The last function decreases for k>=3; its logarithmic derivative is 1/(k-1)-2/k-1/(k+1)<0. Thus p_0+p_+>=17/18>16/17. This proves (9).

Every qualifying source strictly hits H_0 or H_+: otherwise it would be contained in R_-, whose capacity is at most 1/8 by (7). Consequently

    S_0+S_+>=v(p_0+p_+)+E
             >=(16/17)v+1-v
             >=16/17.

At least one of these two scores is therefore at least

    8/17>4/9.                                     (10)

This is a noncanonical source-capacity repair. A feasible singleton source plus a below-target own cap forces a geometrically uneven fan, and a two-direction average then gives more than the target. It does not rely on equal source weights, source centroid selectors, or a fixed source arrangement.

## 5. An exact failure of a scalar fan shortcut

The following tempting ordinary triangle inequality is false:

    sum_j p_j+(3/2)max_j p_j>=2

for every positive three-fan. Here is a rational certificate. Take the standard triangle

    T=conv{(0,0),(1,0),(0,1)},
    y=(9/10,1/20),

and fan normals

    u_1=(1,2),       u_2=(-1,-19/10),       u_3=(0,-1).

They balance with positive coefficients 1,1,1/10. The halfspaces are u_j.x>=u_j.y. Their area fractions relative to T are

    p_1=1/2,
    p_2=(199/200)^2/(19/10)=39601/76000,
    p_3=1-(19/20)^2=39/400.

The first follows from the projection values 0,1,2 with threshold 1. The second cap is the lower cap x+(19/10)y<=199/200, whose intercepts are 199/200 and 199/380. The third is the bottom strip y<=1/20. The maximum is p_2, and

    sum_j p_j+(3/2)max_j p_j
       =288825/152000<2,

with exact gap 15175/152000=607/6080.

This is only a scalar obstruction. It does not refute the simplicial-capacity fan problem: the first two caps have a large sum, and their common missed region cannot contain a qualifying large triangle. Any successful scalar inequality must retain such source-capacity information or allow a different pair/triple weighting.

## 6. Remaining exact geometric question

The calculations prove the capacity formulas and the repair (10) only for the displayed reflection-symmetric fan family, with the repair assuming k>=1 and a feasible top singleton. The remaining configurations with one or two feasible singleton patterns and arbitrary non-symmetric fans are not resolved by Sections 1–5. The no-singleton regime is resolved independently in Section 7 below.

A complete two-dimensional fan proof would need an exact relation between the own-cap areas and the maximal triangle capacities of the relevant intersections. The retained object is a maximum-area inscribed triangle, not merely the area of the retained polygon. Replacing that capacity by polygon area discards the shape information used above.


## 7. Exact positive-fan sector consequences and pattern reduction

This section uses the ordinary positive-fan sector inequality in accepted fact
`2a8c2bc6d7992c5e`, whose original standard source is Tsintsifas's planar
six-sector theorem. Let B be ANY planar convex body, y an interior point,
and H_1,H_2,H_3 a full positive fan through y. Write A=|B| and, for
{i,j,k}={1,2,3},

    c_i=|B cap H_i|,
    s_i=|B minus (H_j union H_k)|,
    D_i=|B cap H_j cap H_k|.

Boundary lines have zero area. All six sector areas are positive, and the
accepted theorem gives

    A=sum_i(s_i+D_i),
    c_j+c_k=A+D_i-s_i,
    sum_i D_i/s_i>=3/2.                         (11)

First, some singleton sector has area at most 2A/9. Otherwise
A=sum_i s_i(1+D_i/s_i)>(2A/9)(3+3/2)=A.
Thus its maximal inscribed triangle has area at most 2A/9, in particular
strictly less than A/4. Consequently, if A=vV<=V and source triangles
have area at least V/4, at least one singleton hit pattern is impossible.
This conclusion includes equality v=1, and it does not require B to be a
triangle.

Second, the sum of the two largest cap areas is at least 8A/9. Suppose,
to the contrary, all three pair sums were less than 8A/9. Put
x_i=s_i-D_i. Then (11) gives x_i>A/9 for every i. Since
A=sum_i x_i+2 sum_i D_i, put D=sum_i D_i<A/3. The function
f(t)=t/(t+A/9), t>=0, is increasing and concave, as follows either by
its first two derivatives or by writing f(t)=1-(A/9)/(t+A/9).
Therefore

    sum_i D_i/s_i
      <sum_i D_i/(D_i+A/9)
      <=3 (D/3)/(D/3+A/9)
      =3D/(D+A/3)
      <3/2.

This contradicts (11), proving

    max_{j!=k}(c_j+c_k)>=8A/9.                 (12)

Now let source triangles P_i subset B have area at least V/4 and weights
e_i>=0 summing to E=1-v. For each direction define the strict-hitting
score in units V by

    S_j=c_j/V+sum_i e_i 1{P_i intersects int H_j}.

Assume NO singleton hit pattern is possible: no triangle in B of area
at least V/4 strictly hits just one of the three halfplanes. A source
cannot hit none, since the three complementary closed halfplanes have
intersection {y}, of area zero. Hence each source hits at least two.
Choose the pair of cap indices attaining (12). Every source hits at
least one direction in this pair, so

    max_j S_j >= (S_j+S_k)/2
              >=4v/9+E/2
               =4/9+E/18.                    (13)

The equality-boundary case is harmless: a source which touches a cap only
on its boundary does not strictly hit it and lies in its closed opposite
halfplane. The area/capacity obstruction used above is for those closed
opposite intersections. Thus all statements retain strict hitting
exactly; no boundary source credit is inserted.

For the finite positive-fan source-pattern LP, there are consequently
only two unresolved geometric regimes: exactly one feasible singleton
pattern, or exactly two. Feasibility here means that the closed retained
region contains a triangle of area at least V/4. The conclusion (13) is
only a fan certificate at the fixed point y. No compactness or global
strict-hitting center claim is being inferred.
