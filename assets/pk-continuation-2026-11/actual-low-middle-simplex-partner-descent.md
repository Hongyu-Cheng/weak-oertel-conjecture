# Actual low-middle repair by shrunken simplex sources and one-cap descent

This is a sufficient-condition theorem for actual reflected fiber stars. It
covers every ambient halfspace, with arbitrary coupling between integer and
continuous coordinates. It does not prove that every source has such a star.
In particular, the common partner reference M is a lower bound on inscribed
simplex volumes, not automatically the largest core fiber volume.

## 1. Exact statement and constants

Fix d>=3, n>=1, and write

    Gamma=(d/(d+1))^d,  q=1-Gamma,  beta=2^(1-d),
    a_star=2 Gamma beta/[q(1-beta q)],
    a=(beta+a_star)/2,
    L=1-2 Gamma-q^2 a,
    delta=L/4,  theta=delta/d,
    sigma=[theta/(d+1)]^d,
    lambda=2 Gamma+(Gamma^2 a+delta)/(1-a).

All these constants are explicit, and

    beta<a<a_star<beta/q<1,  L>0,  0<theta<1,  lambda<1.   (1)

Let w,u_i,v_i (1<=i<=k) be pairwise distinct integer points in Z^n,
with u_i+v_i=2w. Let B,A_i,C_i be full-dimensional compact convex
bodies in R^d placed at these respective bases. Assume

    (A_i+C_i)/2 subset B.

Fix M>0 and suppose each C_i contains a d-simplex Q_i of volume c_i>=M.
Write b=|B| and a_i=|A_i|, and assume

    0<b<=a M,       a_i<=sigma M for every i,
    sum_i a_i >= r(b):=(2 Gamma+delta)M-(1-q^2)b.          (2)

Then there is a single deterministic y in B such that every closed ambient
halfspace containing (w,y) has, on this actual star alone, d-dimensional
fiber-sum mass at least

    (Gamma+delta/2)M.                                   (3)

Other fibers, if present, only increase this mass. Moreover

    0<r(b)<=lambda(M-b),  lambda<1.                      (4)

Thus an incoming mass strictly smaller than the full volume deficit M-b
suffices, with a dimension-dependent uniform factor. The theorem extends
beyond the direct half-volume reflection range b<=beta M, but covers only
the stated interval b<=a M and the stated small-per-fiber hypothesis.
It is not a middle-fiber assertion for all possible volume ratios.

## 2. Verification of constants

The usual Gamma_d decreases with d and is strictly greater than 1/e>1/3.
For completeness, x log(x/(x+1)) has derivative
log(x/(x+1))+1/(x+1)<0, and log(1+1/d)<1/d gives Gamma_d>1/e.
The elementary series for e gives e<3. For d>=3,
Gamma<=27/64 and beta<=1/4. The function
1-2 Gamma-beta(1-Gamma) decreases in both Gamma and beta, so

    1-2 Gamma-beta q >= 1-54/64-37/256=3/256>0.          (5)

Also 2 Gamma-q(1-beta q)=3 Gamma-1+beta q^2>0.
These two inequalities give respectively a_star<beta/q and a_star>beta.
Since beta/q<=16/37<1, (1) follows except for lambda<1.
We have L>1-2 Gamma-beta q>0 and L<1, so 0<delta<1/4
and 0<theta<1. Finally

    (1-a)(1-lambda)=1-2 Gamma-q^2 a-delta=L-delta>0.

If t=b/M<=a, then

    r(b)/(M-b)=2 Gamma+(Gamma^2 t+delta)/(1-t)
               <=2 Gamma+(Gamma^2 a+delta)/(1-a)=lambda.

Positivity of r follows from the same formula. This proves (4).

## 3. Clip the actual incoming bodies to the required total

If sum_i a_i exceeds r(b), put s=(r(b)/sum_i a_i)^(1/d) and replace
each A_i by its homothetic copy of ratio s about its centroid. Every
replacement is a full-dimensional convex subset of the original body,
the midpoint inclusion persists, all per-fiber bounds persist, and the
new volumes sum to r(b). A mass lower bound for these subsets is a lower
bound for the original star. This choice is deterministic. Henceforth
A_i and a_i denote these subsets and their volumes.

Set

    V=b+sum_i a_i=(2 Gamma+delta)M+q^2 b,
    E=sum_i a_i=V-b.

The required source-volume and retained-volume comparisons are strict:

    V/M<=2 Gamma+delta+q^2 a=1-3 delta,
    (1-theta)^d>=1-d theta=1-delta,
    q b < beta V.                                      (6)

For the last inequality, b/M<=a<a_star gives
q(1-beta q)b<2 Gamma beta M<beta(2 Gamma+delta)M.
Rearranging is exactly q b<beta V.

## 4. Shrunken simplex sources pay actual pair mass

Let g_i be the ordinary centroid of Q_i, and define

    Q_i^theta=g_i+(1-theta)(Q_i-g_i),
    P_i(p)=(p+Q_i^theta)/2  for p in A_i.

Each P_i(p) lies in B by the midpoint inclusion, and by (6)

    |P_i(p)|=2^(-d)(1-theta)^d c_i >= 2^(-d)V.            (7)

For a nonzero continuous normal u, a point y in B, and the through-y
halfspace J={x:u dot x>=u dot y}, define the measurable hit set

    G_i(y,u)={p in A_i: h_(Q_i^theta)(u)+u dot p>2 u dot y}.

This strict inequality is exactly P_i(p) meeting int(J). Let an actual
through-(w,y) ambient halfspace have continuous normal u and arbitrary
integer component. Its restrictions at u_i and v_i have thresholds t_A,t_C
with

    t_A+t_C=2 u dot y.                                 (8)

We claim that its total mass on A_i and C_i is at least |G_i(y,u)|.
If all G_i lies in the closed A_i cap, this is immediate. Otherwise choose
p in G_i with u dot p<t_A. Then (8) implies

    t_C<2 u dot y-u dot p<h_(Q_i^theta)(u).

Write h=h_(Q_i)(u), m=min_(x in Q_i)u dot x and W=h-m>0.
Since the centroid of a simplex is the average of its d+1 vertices,

    h-u dot g_i >= W/(d+1).

Consequently h_(Q_i^theta)(u)<=h-theta W/(d+1).
Choose a vertex z attaining h. The copy
z+[theta/(d+1)](Q_i-z) lies in Q_i and in the closed C_i cap, because
its smallest u-value is h-theta W/(d+1)>t_C. Its volume is

    [theta/(d+1)]^d c_i >= sigma M >= a_i >= |G_i(y,u)|.

This proves the pair-payment claim. The dichotomy includes arbitrary
integer tilts, equality on the actual cap boundary, and all nonzero u.
The distinct-base assumption permits summing these payments without
counting any fiber twice.

It suffices, therefore, to find y in B for which all unit u satisfy

    F_y(u):=|B cap {x:u dot(x-y)>=0}|+sum_i |G_i(y,u)|
             >= (Gamma+delta/2)M.                      (9)

## 5. One-cap descent for the continuum of sources

Define T=(V-q^2 b)/2=(Gamma+delta/2)M and let g=g_B.
The function u -> F_g(u) is lower semicontinuous on the unit sphere.
Indeed, the own-cap volume is continuous by bounded convergence, since
its dividing hyperplane has zero d-volume. The source support expressions
are continuous in (p,u); their strict-positive indicators are lower
semicontinuous. Fatou's lemma, applied on each finite-volume A_i, proves
the assertion for the hit-set volumes. Thus F_g attains a minimum, and
its minimizing set is compact. Select the lexicographically least unit
minimizer by successive coordinate minima.

If min F_g>=T, choose y=g. Otherwise let u be the selected minimizer,
H={x:u dot(x-g)>=0}, and set

    h=|B cap H|,  D_i=A_i minus G_i(g,u),
    m=sum_i |D_i|,  Q=B cap {x:u dot(x-g)<=0}.

Ordinary Grunbaum gives h>=Gamma b. Failure at g means

    h+E-m<T,  hence m>E+h-T.                            (10)

In particular m>0: with m=0, the score is at least Gamma b+E=V-qb,
and V-qb-T=[V-(2q-q^2)b]/2>0 because V>b and 2q-q^2<1.
Each D_i is a closed subset of A_i, and every P_i(p) for p in D_i lies
in Q. This follows from its nonpositive support difference, with no
credit for boundary-only contact. The retained body Q is full-dimensional
because m>0 ensures at least one such full-dimensional contained simplex.
By (6), (7), and the ordinary centroid inequality,

    |Q|=b-h<=qb<beta V,
    |P_i(p)|>=2^(-d)V>|Q|/2  for p in D_i.

Accepted ordinary simplex-containment fact 7fd6b5631ad64e4c now puts
g_Q in the INTERIOR of every P_i(p), simultaneously for all p in all D_i.
Explicitly, each barycentric coordinate of g_Q in that simplex is at least
[2-|Q|/|P_i(p)|]/(d+1)>0. Thus every through-g_Q halfspace strictly hits
all those source simplices. Its B mass is at least its Q mass, which is
at least Gamma(b-h) by the ordinary centroid inequality. Therefore for
every unit u' we have

    F_(g_Q)(u')>=Gamma(b-h)+m
                >Gamma(b-h)+E+h-T
                 =Gamma b+E+q h-T
                >=Gamma b+E+q Gamma b-T
                 =V-q^2 b-T=T.                         (11)

Choose y=g_Q in this second branch. The choice is deterministic and is
a single point of B, not an averaged point or a distribution. Combining
(9) with the actual pair-payment lemma proves (3) for all nonzero
continuous normals through (w,y).

## 6. Pure integer directions and general containing halfspaces

For a through-(w,y) halfspace with continuous normal zero, the entire
middle fiber is included. The two integer offsets of a reflected pair
are opposite, so at least one of its endpoint fibers is entirely
included. Each endpoint has volume at least a_i: this is automatic for
A_i, while |C_i|>=c_i>=M>a_i since sigma<1. Its mass on the star is
therefore at least b+sum_i a_i=V>T.

Finally, a closed ambient halfspace containing (w,y) contains the parallel
closed halfspace with boundary through (w,y). The previous inequalities
for that smaller halfspace imply the same bounds for the original one.
No open/closed replacement of the mixed measure, arbitrary affine change
of the integer lattice, or approximation of the actual bodies occurs.

The nonstandard dependency is only the accepted ordinary first-moment
simplex-containment fact 7fd6b5631ad64e4c. Ordinary Grunbaum and simplex
centroid formulas are classical background. The proof uses no mixed
centerpoint or theorem equivalent to OC.
