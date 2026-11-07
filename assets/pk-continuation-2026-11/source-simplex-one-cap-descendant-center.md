# A source-simplex hitting center from one bad cap and its retained centroid

Scoped research theorem, 6 November 2026. This is a sufficient-condition
result for the geometric source-simplex hitting problem. It does not assert
that every mixed-integer body satisfies this source model or volume range.

Let d>=1 and let B be a convex d-body. Fix V>0 and write |B|=vV, where
0<v<=1. Let P_1,...,P_k be full-dimensional simplices contained in B,
with |P_i|>=2^(-d)V. Assign nonnegative weights e_i with

    E:=sum_i e_i=1-v.

For a closed halfspace H define its strict-source score by

    F(H)=|B intersect H|/V
         +sum_i e_i 1{P_i intersect int(H) is nonempty}.

Put

    Gamma=(d/(d+1))^d,   q=1-Gamma,   beta=2^(1-d).

Assume the strict volume condition

    qv<beta.                                             (1)

Then there exists a deterministic point y in B such that every closed
halfspace H containing y satisfies

    F(H)>=(1-q^2 v)/2.                                   (2)

For d>=3, the right side of (2) is strictly greater than Gamma throughout
this range. Consequently, in every d>=3 this extends the sufficient volume
range v<=beta to v<beta/q. Sections 1--5 prove this open-range statement;
Section 6 supplies the additional equality geometry and includes the endpoint
v=beta/q for d>=3.

## 1. Two ordinary geometric inputs

The ordinary centroid inequality gives, for any convex d-body Q and any
closed halfspace through its centroid g_Q,

    |Q intersect H|>=Gamma |Q|.                          (3)

The inscribed-simplex moment inequality gives: if a full simplex P is
contained in Q and |P|>|Q|/2, then g_Q belongs to int(P). More precisely,
for each barycentric coordinate lambda of P,

    lambda(g_Q)>=(2-|Q|/|P|)/(d+1)>0.                    (4)

The complete first-moment proof of (4) is the ordinary simplex-containment
result, candidate/fact 7fd6b5631ad64e4c. No mixed center or source-hitting
conclusion is used as an input here. For d=1 both inputs are the corresponding
interval statements.

## 2. Deterministic selection at the original centroid

Write g=g_B and set T=(1-q^2 v)/2. For u on the unit sphere define

    H_u={x: u dot (x-g)>=0},
    h(u)=|B intersect H_u|/V,
    F_g(u)=h(u)+sum_i e_i 1{h_(P_i)(u)>u dot g},

where h_(P_i)(u)=max_{x in P_i}u dot x is the support function. The strict
support inequality is exactly the condition that the full-dimensional
source P_i meets int(H_u).

The own-cap mass h is continuous in u: if u_j tends to u, the cap indicators
converge away from the hyperplane u dot (x-g)=0, which has d-volume zero,
and bounded convergence applies on B. Each support difference is continuous.
Its positive-set indicator is lower semicontinuous. Thus F_g is lower
semicontinuous on the compact sphere and attains its minimum, with a compact
nonempty minimizing set.

If this minimum is at least T, choose y=g. Otherwise choose the
lexicographically least minimizer u, obtained by minimizing the successive
coordinates over compact sets, and put

    H=H_u,   h=h(u),   I={i: P_i intersect int(H) is empty},
    m=sum_(i in I) e_i.

These choices are deterministic after fixing the ambient orthonormal
coordinates. By construction

    h+E-m<T,   hence   m>E+h-T.                           (5)

Moreover h>=Gamma v by (3). The set I has positive total weight: if m=0,
then

    F_g(u)>=Gamma v+E=1-qv,
    1-qv-T=[1-v(2q-q^2)]/2>=Gamma^2/2>0,

contrary to F_g(u)<T.

## 3. The retained centroid receives all the missed weight

Let

    Q=B intersect {x: u dot (x-g)<=0}.

The body Q contains every source indexed by I. Its normalized volume is
v-h, because the dividing hyperplane carries no d-volume. It is a
full-dimensional convex body: it contains a full-dimensional source of
positive weight. By (1) and (3),

    |Q|=(v-h)V<=qvV<beta V,
    |P_i|>=2^(-d)V>|Q|/2   for every i in I.

Input (4) therefore puts y:=g_Q in the interior of every missed source.
In particular y is a single point of B. Every through-y closed halfspace J
strictly hits all these sources and contains an ordinary centroid cap of Q.
Using only their weights and the own B cap gives

    F(J)>=Gamma(v-h)+m
         >Gamma(v-h)+E+h-T
          =Gamma v+E+q h-T
         >=Gamma v+E+q Gamma v-T
          =1-q^2 v-T=T.                               (6)

Other sources contribute nonnegative amounts and need no compatibility or
stability estimate. Thus the chosen descendant center has a strict score
above T in every direction. Together with the first branch this proves (2)
for all through-point halfspaces.

If a closed halfspace contains y but its boundary does not contain y,
translate its boundary parallel toward y. The resulting through-y halfspace
is contained in the original halfspace, both for own mass and strict-source
hitting. Monotonicity extends (2) to every containing halfspace. There is no
omission of orientations or boundary-contact sources.

## 4. Exact comparison with Gamma in d>=3

The sequence Gamma_d decreases: for real x>0, the derivative of
x log(x/(x+1)) is log(x/(x+1))+1/(x+1)<0. Hence for d>=3,

    Gamma<=27/64,   q>=37/64,   beta<=1/4,
    beta/q<=16/37=592/1369.

Also

    (1-2Gamma)/q^2=1-(Gamma/q)^2
       >=1-(27/37)^2=640/1369.

Condition (1) yields

    v<beta/q<=592/1369<640/1369<=(1-2Gamma)/q^2.

It follows that 1-q^2v>2Gamma, exactly the strict comparison required.
There is no dimension-independent hidden loss. For d=1 or d=2 formula (2)
remains proved, but this comparison is not asserted. The earlier direct
half-volume hitting theorem can be used separately in those dimensions.

## 5. Relation to other retained-volume consumers

The number (1-q^2v)/2 resembles a two-cut average budget. The mechanism here
uses additional geometric information: after the single bad cap, every
missed simplex occupies more than half of the retained body and therefore
contains its centroid in its interior. Its entire weight is then paid in
every new direction. A scalar retained-volume estimate alone does not imply
this simultaneous source credit. No assertion is made that repeating this
argument reaches all v<=1 or resolves the full source-simplex problem.

## 6. The upper endpoint in dimensions at least three

For d>=3, the result also holds when qv=beta. Thus in those dimensions
one may replace (1) by qv<=beta, retaining the exact score (2) and its
strict comparison with Gamma. We prove the additional equality geometry
rather than treating weak containment as strict source hitting.

### 6.1 A boundary half-volume simplex forces a double simplex

Let R be a convex d-body, d>=2, and let P subset R be a d-simplex with
|P|=|R|/2=a. If g_R belongs to the boundary of P, then R is the convex hull
of at most d+2 points.

Indeed, the simplex containment inequality puts g_R in P. Choose a
barycentric coordinate lambda of P with lambda(g_R)=0. In the ordinary
moment proof, let m=|R intersect {lambda<0}| and let S be the coarea
section density of R at lambda=0. The inequalities are

    0=integral_R lambda
      >=a/(d+1)-d m^2/[(d+1)S]
      >=a/(d+1)-m^2/[(d+1)a]>=0,

since m<=a and S>=da. Equality is therefore forced throughout:

    m=a,   S=da,   R intersect {lambda>=0}=P.           (7)

The last assertion follows because that positive half-body contains P and
has the same volume. Equality of contained full-dimensional compact convex
bodies of equal volume is used here: a point outside the smaller body,
together with an interior ball of that body, would give a positive-volume
difference. The section R intersect {lambda=0} is consequently the
opposite facet F of P.

Write R_-=R intersect {lambda<=0} and t=-lambda. Its section density f has
initial value S, volume a, and maximal support length L. The comparison
cone has height A=da/S and density

    k(t)=S(1-t/A)_+^(d-1).

The one-crossing proof of the first-moment inequality gives L<=A and a
crossing c with (t-c)(f(t)-k(t))<=0 almost everywhere. Equality of the first
moments and the volumes gives integral (t-c)(f-k)=0. The nonpositive
integrand must vanish almost everywhere, so f=k almost everywhere outside
{c}. In particular L=A, since k is positive on (0,A).

Choose z in R_- attaining t=A, possible by compactness. The simplex
conv(F,z) is contained in R_- and has volume SA/d=a. Equal volume again
forces R_-=conv(F,z). The positive part is P, itself a pyramid over F.
Thus R=conv(P union {z}), with at most (d+1)+1=d+2 vertices. This deduction
uses only the explicit equality in the one-crossing integral, not an
unproved equality classification of section concavity.

### 6.2 A nontrivial pyramid frustum has too many extreme points

Let R be the portion of a full-dimensional pyramid between its base plane
and a parallel plane strictly between the base and the apex. Its two
parallel supporting faces are positive homothetic copies of the same
full-dimensional (d-1)-body. Each has at least d extreme points, by the
finite-dimensional fact that a compact convex body is the convex hull of
its extreme points. Extreme points of a face are extreme points of R.
The two faces are disjoint, so R has at least 2d extreme points. For d>=3,
2d>d+2.

Consequently, if P subset R has volume at least |R|/2, then g_R is in the
interior of P. Strictly larger volume is covered by (4); equality together
with boundary membership would contradict Section 6.1 and the extreme-point
count. This conclusion applies to arbitrary pyramid bases, including
nonpolyhedral bases.

### 6.3 Apply the frustum conclusion to the bad cap

Repeat Sections 2--3 with qv=beta. If the selected bad cap has h>Gamma v,
then |Q|<beta V and the preceding strict-volume proof applies unchanged.
If h=Gamma v, use the classical equality case of the ordinary centroid
inequality: B is a pyramid with base parallel to the cutting hyperplane,
and H is the apex-side cap. The equality characterization is stated on
page 1 of [Marin Sola and Yepes Nicolas, On Grunbaum type inequalities](https://webs.um.es/jesus.yepes/publicaciones_files/paper_grunbaum.pdf).
The orientation follows directly as well: at the centroid the apex-side
fraction is Gamma, while the base-side fraction is q>Gamma for d>=2.
For a height coordinate zero on the base and one at the apex, the centroid
height is 1/(d+1), by integrating the section density (1-t)^(d-1).

The opposite retained body Q is therefore a nontrivial frustum. Every
missed source has volume at least 2^(-d)V=|Q|/2, so Section 6.2 puts g_Q in
the interior of every missed source. The full source credit and all of (6)
are now valid, proving the same bound T at the endpoint.

The exact comparison T>Gamma at v=beta/q was already supplied by the
non-strict version of Section 4: beta/q<=592/1369<640/1369. For d=3 the
gap is exactly 3/512. The endpoint extension is restricted to d>=3 because
the strict extreme-point inequality used above fails in d=2.
