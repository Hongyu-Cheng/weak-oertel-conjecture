# Exact simplex-hitting obstruction to two natural averaging selectors

Research note, 6 November 2026. The intended deficit hitting theorem remains intact. This certificate only shows that its center cannot always be taken as the volume-weighted average of the middle centroid and the midpoint-simplex centroids, or as an arbitrary-label stationary barycentric selector.

Let T=conv(0,e1,e2), V=|T|=1/2, and set

    v=2500/2997, e=497/2997=1-v, B=sqrt(v)T.

Use the following nonnegative column-stochastic barycentric vertex matrix:

    P=(1/100) [[96,15,58],
              [ 3,84, 4],
              [ 1, 1,38]].

Let Q be the triangle in B whose three vertices have barycentric columns P. The determinant is2997/10000, so

    |Q|=v (2997/10000)V=V/4.

Thus B and Q satisfy exactly the d=2 hitting data: |B|<=V, one inscribed simplex of volume2^(-2)V, and deficit weight E=eV=V-|B|. All three vertices are strictly inside B, so no containment or support-boundary pathology is involved.

For barycentric coordinates lambda0,lambda1,lambda2 of B, use

    f=(3/10)lambda1+lambda2.

Its vertex values on B are0,3/10,1. Its upper support on Q is

    h_Q(f)=max(19/1000,262/1000,392/1000)=49/125.

For a threshold t between3/10 and1, the exact triangular cap is

    |B intersect {f>=t}|=v (1-t)^2/(7/10) V.           (1)

## Weighted centroid selector

The natural weighted-centroid candidate is

    y_bar=v cg(B)+e cg(Q),

with weights summing to1. Its barycentric vector is

    lambda(y_bar)=(111331/299700,32803/99900,4498/14985).

Consequently

    f(y_bar)=1194827/2997000,
    f(y_bar)-h_Q(f)=20003/2997000>0.

The cap strictly misses Q, so it receives no hitting bonus. Formula(1) gives its normalized score

    3247827521929/7537342672440
      =4/9-102102554711/7537342672440 <4/9.

Thus this deterministic averaging selector fails the desired gamma_2 threshold despite exact simplex midpoint shape and exact deficit masses.

## Stationary barycentric selector

A different proposed selector solves the affine fixed-point equation

    lambda=v(1/3,1/3,1/3)^T+e P lambda.

The matrix I-eP is invertible: P is column stochastic and its induced l1 norm is1, while0<e<1, so the Neumann series converges. This also makes lambda nonnegative with coordinate sum1. Its exact solution for the displayed vertex labeling is

    lambda=(27331294892/72984169773,
            23903681710/72984169773,
            251491/843933).

The same cap has threshold

    t=9640099228/24328056591,
    t-h_Q(f)=12937630541/3041007073875>0,

and normalized score

    5393402287432647844225000/12416512146305476497534099
      =4/9-125047555369786154679044/12416512146305476497534099
      <4/9.

The stationary selector therefore is not valid for arbitrary vertex labeling. This does not rule out optimizing labels or a more sophisticated selection mechanism.

Every value in this note is rational apart from the irrelevant common scale sqrt(v). All cap volumes follow from the elementary exact triangle formula(1). These are counterexamples to specified center formulas, not counterexamples to existence of some successful center in the same B.
