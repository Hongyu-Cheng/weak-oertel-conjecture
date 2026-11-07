# What can and cannot amplify the sharp counterexample

This note records proved obstructions to amplifying the direct sharp
counterexample into a counterexample to the repository's weak target
`c_0 / 2^n` for every absolute `c_0>0`. It does not claim to settle that
target. In particular, failure of the specific constant `1/e` and failure
of every positive absolute constant are different assertions.

The starting construction and its notation are in
[the direct rational sharp counterexample](direct-rational-sharp-oc-counterexample.md).
The arguments below give:

1. a support-count obstruction applying to every body with the same
   cube-plus-negative-units integer projection, with arbitrary fibers;
2. an explicit product-repair bound for the actual sharp counterexample,
   at an actual mixed-integer point;
3. a dimension-independent extension of that repair bound to common
   continuous simplex padding;
4. a strict fiber-regrowth certificate for integer dilation of the
   differently typed source fibers.

The product argument is independent of the entropy-capacity results in
the fact graph. Its auxiliary probability measure, center, likelihood,
moment constants, and halfspace estimates are all specified below.

Review status: independent mathematical audit completed; these supporting
claims have not been separately normalized into accepted graph facts.
The fixed-support bound applies to the later n=76 construction. The product
repair theorem in Section 5 requires each outer fiber to have centroid zero;
the n=76 construction does not satisfy that hypothesis, so that theorem is
not asserted for its independent powers.

## 1. A necessary mass-distribution condition for weak counterexamples

Let `S=C intersect (Z^n x R^d)` be nonempty, let `q=dim_H(S)`, and use
the intrinsic measure `H_q`. Write

    w_z = H_q({z} x S_z),   W=sum_z w_z,   m_*=max_z w_z,
    D(C)=sup_(y in S) inf_(closed H containing y) H_q(S intersect H)/W.

There are finitely many nonempty fibers. A convex fiber of dimension
less than `q` has zero `H_q` measure; one of dimension `q` has finite,
positive measure. Consequently `0<m_*<=W<infinity`.

**Lemma 1 (largest-fiber bound).** With `Gamma_0=1` and
`Gamma_q=(q/(q+1))^q` for `q>=1`,

    D(C) >= Gamma_q m_*/W >= m_*/(e W).                  (1)

**Proof.** Choose a fiber of mass `m_*`. If `q=0`, that fiber is a
single point, whose containing halfspaces all carry mass at least
`m_*`. If `q>=1`, take the ordinary centroid in the fiber's
`q`-dimensional affine hull. It is a point of the fiber and hence of
`S`. A containing ambient halfspace restricts to either the whole
affine hull or a halfspace containing that centroid. The ordinary
`q`-dimensional Grunbaum inequality gives retained fiber mass at least
`Gamma_q m_*`. All other fiber contributions are nonnegative. This
also handles ambient halfspaces whose boundaries contain the entire
chosen fiber. Finally `Gamma_q>=1/e`. This proves (1). QED.

Define the normalized effective fiber count

    R(C) = W/(2^n m_*).

Lemma 1 has the immediate consequences

    2^n D(C) >= 1/(e R(C)),
    R(C) <= #{z:w_z>0}/2^n.                              (2)

Thus a family with `2^n D(C)->0` must have both

    W/(2^n max_z w_z) -> infinity,
    #{z:w_z>0}/2^n -> infinity.                          (3)

This is a necessary condition, not a proposed sufficient condition.
Having many tiny extra fibers does not by itself make the first
quantity large.

**Corollary 2 (the projection template has a uniform weak constant).**
Suppose `n>=1` and the nonempty integer fibers lie over

    {0,1}^n union {-e_i:1<=i<=n}.

Then, without any condition on the shapes or relative masses,

    2^n D(C) >= Gamma_q 2^n/(2^n+n) >= 2/(3e).           (4)

**Proof.** There are at most `2^n+n` positive-mass fibers, and
`n<=2^(n-1)` for every integer `n>=1`. Apply (1). QED.

In the full fiber-dimensional case, multiplying the body by any common
positive-volume continuous convex body multiplies all fiber masses by
the same factor. It leaves `R(C)` unchanged. In particular, increasing
the continuous dimension by padding cannot overcome (4).
Moreover, along any sequence in this projection template with
`n->infinity`, the first bound in (4) gives
`liminf 2^n D(C)>=1/e`, even if the continuous dimension and all the
fiber shapes vary. Thus a fixed improvement below `1/e` cannot be
amplified by merely increasing the integer dimension of this template.

For the original `d=23` sharp counterexample, the direct proof and
Lemma 1 together give the exact value

    D(C)=Gamma M/W,
    W=(2^n-1)M+4b,   Gamma=(23/24)^23.                   (5)

Indeed, `M` is the largest fiber volume: the parameter certificate
gives `Gamma M>3b/2`, while every other fiber has volume `b` or `b/N`.
The direct proof supplies the matching upper bound at every point.
Moreover, its exact parameter inequalities give

    M<4b,   Gamma M/(4b)>3/8,
    2^n D(C) > Gamma M/(4b)>3/8>1/e.                    (6)

For the first strict inequality, observe that `W/2^n` is a strict
convex combination of `M` and `4b`, and hence is less than `4b`.
For the last, the elementary exponential series gives
`e>1+1+1/2+1/6+1/24=65/24>8/3`.
Thus the original body does satisfy the particular `1/(e 2^n)` bound,
even though it violates the sharp `Gamma/2^n` bound.

## 2. A halfspace bound from fourth moments

We first give the elementary probability estimate used in the product
argument. It is about all closed halfspaces, including those carrying
boundary mass.

**Lemma 3.** Suppose a real random variable `Y` has mean zero,
variance `sigma^2>0`, and

    E[Y^4] <= K sigma^4.

Then

    P(Y>0) >= 1/(4K),   P(Y<0) >= 1/(4K).                (7)

If independent, mean-zero variables `Y_i` each obey the corresponding
fourth-moment inequality with the same `K>=3`, their sum also obeys it.

**Proof.** Holder gives

    E[Y^2] <= (E[|Y|])^(2/3) (E[Y^4])^(1/3),

so `E[|Y|]>=sigma/sqrt(K)`. Since `E[Y]=0`,
`E[Y_+]=E[|Y|]/2`. Cauchy--Schwarz gives

    E[Y_+] <= sigma sqrt(P(Y>0)),

which proves the first estimate; apply it to `-Y` for the second.
For independent centered variables, expansion gives

    E[(sum_i Y_i)^4]
      =sum_i E[Y_i^4]+6 sum_(i<j) E[Y_i^2] E[Y_j^2]
      <=K (sum_i E[Y_i^2])^2,

using `K>=3`. Variables of zero variance are zero almost surely and
cause no problem. QED.

In particular, if a probability measure has positive-definite
covariance and every centered scalar projection obeys the moment
bound, every closed halfspace containing its centroid has mass at
least `1/(4K)`. A containing halfspace includes the through-centroid
open positive halfspace, so this conclusion uses no assumption about
zero boundary mass.

## 3. An auxiliary law with an actual mixed-integer centroid

Use the exact parameters of the original sharp counterexample:

    d=23,   L=10000,   N=L^23,   n=3N,
    a=|A|=b/N,   |K_I|=M,   W=(2^n-1)M+4b.

The middle fiber is the centered simplex `B`, the negative-unit fibers
are `A=B/L`, and the positive singleton fiber at `e_i` is `2P_tau(i)`.
Each of the three types occurs exactly `N` times. The centroid of
`P_a` is `c_a`. Its barycentric coordinates are the three cyclic
rotations of `(1/72,5/144,11/144)` on each chain. Consequently

    c_0+c_1+c_2=0                                      (8)

in the centered Euclidean coordinates: at each barycentric coordinate,
the sum is `1/8=3/24`.

Set

    H=b+2n sqrt(aM),
    r_0=b/H,   r=sqrt(aM)/H.

Define a probability measure `Q` on the actual mixed-integer set by:

* middle-fiber probability `r_0`, with the uniform law on `B`;
* probability `r` at each positive-unit fiber, with its uniform law;
* probability `r` at each negative-unit fiber, with its uniform law;
* zero probability at the other nonzero cube fibers.

The probabilities sum to one. Its integer centroid is zero by pairing
`e_i` with `-e_i`. Its continuous centroid is

    2r sum_i c_tau(i)=2rN(c_0+c_1+c_2)=0.

Thus its centroid is the actual point `(0,0)` of the middle fiber.
No rounding or barycenter-to-lattice argument is being assumed.

We next give a finite, explicit fourth-moment constant for `Q`.
In the standard centered-simplex coordinates used by the construction,
every point of `B` has Euclidean norm at most one. Each `P_a` lies in
`B`; each selected positive-unit fiber lies in `2B`; and `A` lies in
`B`. Thus every point in the support of `Q` has squared ambient norm
at most five. For an ambient normal `(u,v)`,

    E_Q[(u.Z+v.X)^4] <=25 (||u||^2+||v||^2)^2.          (9)

The covariance of the uniform law on `B` gives

    E_B[(v.X)^2]
      =[24 sum_j v_j^2-(sum_j v_j)^2]/(24^2*25)
      >=||v||^2/14400.                                  (10)

For example, (10) follows directly from
`E[lambda_i]=1/24`, `E[lambda_i^2]=2/(24*25)`, and
`E[lambda_i lambda_j]=1/(24*25)` for distinct indices. These moments
are also instances of the elementary simplex integral proved in
Section 6 below.

On each negative-unit fiber the continuous centroid is zero. Its
contribution to the second moment is therefore at least `r u_i^2`.
The middle-fiber contribution is at least `r_0||v||^2/14400`. All
remaining contributions to the second moment are nonnegative. Define

    eta=min(r,r_0/14400)>0,
    K=max(3,25/eta^2).

It follows that

    E_Q[(u.Z+v.X)^2]>=eta (||u||^2+||v||^2),
    E_Q[(u.Z+v.X)^4]<=K E_Q[(u.Z+v.X)^2]^2.              (11)

For every nonzero normal the variance is positive. Lemma 3 applies to
all scalar projections, and to their sums across independent copies.

## 4. An explicit product-repair bound

Let `P` be normalized mixed-integer volume on the original body, and
let `T` be the union of the middle and signed-unit fibers selected by
`Q`. The restricted measure `P|_T` and `Q` are mutually absolutely
continuous. The likelihood `R=d(P|_T)/dQ` is constant on each selected
fiber and satisfies

    log R=log(H/W)+xi,
    xi=0        on the middle fiber,
    xi=L_0      on a positive-unit fiber,
    xi=-L_0     on a negative-unit fiber,
    L_0=(1/2)log(M/a)>0.                                 (12)

This uses the conditional uniform laws, which are the same under `P`
and `Q`. Equal paired probabilities give `E_Q[xi]=0`, while
`Var_Q(xi)<=L_0^2`.

Take `k>=1` independent copies. The normalized mixed-integer measure
on the Cartesian product body `C^k` is exactly `P^k`: its fibers are
Cartesian products, and their volumes and total volumes multiply.
Permuting coordinates to put all integer coordinates first preserves
the mixed-integer lattice and all relevant measures. The integer and
continuous dimensions are respectively `nk` and `23k`.

For any closed halfspace `G` containing the actual point `0` in this
product, (11) and Lemma 3 give

    Q^k(G)>=1/(4K).

Chebyshev's inequality applied to the independent likelihood increments
gives

    Q^k(sum_i xi_i < -L_0 sqrt(8Kk)) <=1/(8K).

The intersection of `G` with the complementary likelihood event thus
has `Q^k` mass at least `1/(8K)`. Integrating the product of the
likelihoods on this intersection proves

    P^k(G) >= (H/W)^k exp(-L_0 sqrt(8Kk))/(8K).

We have proved, at one deterministic point of the actual product set,

    D(C^k) >= (H/W)^k exp(-L_0 sqrt(8Kk))/(8K).           (13)

There is no global use of `dP/dQ`: `P` has other fibers, outside the
support of `Q`. Restricting to `T^k` is legitimate because that part
of `P^k(G)` is a lower bound on its total mass. This also explains why
discarding the other fibers causes no gap in (13).

For this construction, the exponential base in (13) is strictly
better than `2^-n`. Indeed `M>b`, `a=b/N`, and `n=3N`, so

    H>b+6b sqrt(N)>=7b,
    W/2^n=(1-2^-n)M+2^-n 4b<4b,
    rho:=2^n H/W>7/4>1.                                 (14)

Put `delta=log(rho)>0`. Multiplying (13) by `2^(nk)` gives

    2^(nk) D(C^k)
      >=exp(k delta-L_0 sqrt(8Kk))/(8K).                  (15)

Completing the square in `sqrt(k)` yields the uniform bound

    D(C^k)>=c(C) 2^(-nk)   for every k>=1,
    c(C)=exp(-2K L_0^2/delta)/(8K)>0.                    (16)

The constant is extremely small, but is independent of the number of
copies. Thus independent powers of this fixed counterexample cannot
disprove the weak absolute-constant target.

There is also an explicit eventual repair of the sharp bound. If

    k>=max(1, 32K L_0^2/delta^2, 2log(8K)/delta),         (17)

then (15) is at least one. The actual origin of `C^k` consequently has
depth at least `2^(-nk)`, which is at least
`Gamma_(23k) 2^(-nk)`. This conclusion is about all closed oblique
halfspaces in the entire product ambient space.

## 5. The same paired-fiber argument with variable outside mass

The preceding mechanism has a useful parameter version. Suppose an
actual convex-body construction has the same integer bases and the
following positive-volume fibers in some dimension `d>=1`:

* a centered standard simplex `B`, of volume `b`, at the origin;
* equal-volume fibers of volume `M` at all nonzero cube vertices;
* positive singleton fibers `2P_tau(i)`, with `P_a subset B` and
  centroids `c_a` satisfying `sum_i c_tau(i)=0`;
* negative-unit fibers `A_i` of the same volume `a=E/n`, each with
  centroid zero and contained in the Euclidean unit ball, where `E`
  is the total outside mass.

The negative-unit fibers need not have the same shape. These are
explicit hypotheses about the realized fibers, rather than an
assertion that a new family with these properties exists. Assume
also `n>=1`. The total volume and paired normalizer are

    W=(2^n-1)M+b+E,
    H=b+2sqrt(nEM).                                      (18)

The proof of (8)--(13) applies verbatim, with the covariance lower
bound in (10) replaced by `1/[(d+1)^2(d+2)]`. A choice is

    r_0=b/H,  r=sqrt((E/n)M)/H,
    eta=min(r,r_0/[(d+1)^2(d+2)]),
    K=max(3,25/eta^2),  L_0=|log(M/(E/n))|/2.             (19)

If `L_0=0`, all likelihood increments vanish; the likelihood bad event
is empty, so the same lower bounds hold directly.

A simple sufficient condition for strict product repair is

    M/4<=E<=M.                                          (20)

Under (20), `H>=b+M`, while

    W/2^n=M+(b+E-M)/2^n<M+b.

Thus `rho=2^nH/W>1`, and (15)--(17) follow with the new constants.

This applies to a source-family proposal with `M/b>4` and
`M-b<E<M`, provided its exact fiber construction and the hypotheses
above have independently been proved: that mass interval is contained
in (20). It specifically explains why adjusting the outside mass to
slightly exceed `M-b` does not turn subsequent independent products
into a weak-counterexample amplification mechanism.

The explicit `d=26` parameter family in the separate
[simplex-padding note](continuous-simplex-padding-one-over-e-counterexample.md)
satisfies these moment hypotheses. In that family the outside fibers
are `A_a=(T_a-c_a)/51`. Their centroids are zero, and their norms are
at most `2/51<1` because `T_a subset B` and `c_a in B`. The cyclic
centers sum to zero and the type counts are equal. Its exact mass
certificates imply `5b<M<6b`, while `E=25b/6`; thus (20) holds.
Consequently, once the geometric fiber census of that separate
construction is invoked, the same explicit paired-fiber product repair
applies. It is not necessary for its different outside source shapes
to coincide.

## 6. Arbitrarily large common simplex padding does not defeat repair

We need a dimension-independent moment fact.

**Lemma 4 (uniform simplex fourth moment).** If `X` is uniform on any
full-dimensional simplex and `Y` is any centered scalar affine
function of `X`, then

    E[Y^4]<=9 E[Y^2]^2.                                  (21)

**Proof.** Let the simplex have `m` vertices. Write
`Y=sum_(i=1)^m v_i lambda_i`, where the `lambda_i` are barycentric
coordinates and `sum_i v_i=0`. For nonnegative integer exponents,
the uniform-simplex moment formula is

    E[product_i lambda_i^(k_i)]
      =(m-1)! product_i k_i!/(m-1+sum_i k_i)!.            (22)

To obtain (22), use affine invariance to integrate over
`lambda_i>=0, sum_(i<m)lambda_i<=1`, with
`lambda_m=1-sum_(i<m)lambda_i`. Integrate the last coordinate using
`integral_0^A t^p(A-t)^q dt=A^(p+q+1)p!q!/(p+q+1)!`, proved by
integration by parts. Repeating in the remaining coordinates gives
the unnormalized integral `product_i k_i!/(m-1+sum_i k_i)!`.
Multiplication by the uniform density `(m-1)!` proves (22).

Put `S_j=sum_i v_i^j`. Expanding moments by (22), and using `S_1=0`,
gives

    E[Y^2]=S_2/[m(m+1)],
    E[Y^4]=(3S_2^2+6S_4)/[m(m+1)(m+2)(m+3)].             (23)

One direct way to check the fourth numerator is to expand
`product_i(1-v_i t)^(-1)`: its coefficient of `t^4`, when `S_1=0`,
is `S_2^2/8+S_4/4`, and (22) multiplies this by `4!`.
Since `S_4<=S_2^2`, (23) implies (21). The zero-variance case has
`Y=0` and is included. QED.

Let `J` be any full-dimensional continuous simplex, of any dimension,
with centroid `c_J`. On `C^k x J`, use the auxiliary law

    Q^k x U_J,

whose actual mixed-integer centroid is `(0,...,0,c_J)`. Scalar
projections split into independent centered summands from `Q` and
`U_J`. Lemmas 3 and 4 give the same projection bound with

    K'=max(K,9),

independently of the dimension or shape of `J`. The likelihood is
unchanged: both actual and auxiliary laws use the same factor `U_J`.
Consequently

    D(C^k x J)
      >=(H/W)^k exp(-L_0 sqrt(8K'k))/(8K').                (24)

The proof equally allows any finite number of independent simplex
padding factors. In particular, it covers `(C x J)^k` and permits the
dimensions of the padding simplices to depend arbitrarily on `k`.
All constants in (24) are independent of those padding dimensions.

Whenever `rho=2^nH/W>1`, (16) and (17), with `K'` in place of `K`,
therefore remain valid uniformly over this padding. Common continuous
simplex padding can lower a one-copy upper bound toward `1/e`; it
cannot make independent powers of these fixed paired-source families
violate every positive weak constant. The smaller asymptotic simplex
Grunbaum factor does not remove the actual auxiliary center or its
likelihood advantage.

## 7. A strict source of fiber regrowth under integer dilation

The support-count obstruction suggests adding more integer points,
for example by dilating the integer projection. Convexity imposes a
strong exact compatibility condition on maximal-volume fibers.

**Lemma 5 (equal-volume same-parity rigidity).** Let two integer bases
`z,z'` have the same parity, and suppose their fibers are full
`d`-dimensional convex bodies, with `d>=1`, of equal volume `M>0`. Write
`m=(z+z')/2`, an integer base. If the fiber at `m` has volume at most
`M`, the two endpoint fibers are translates. In particular, if they
are not translates, the midpoint fiber has volume strictly greater
than `M`.

**Proof.** Convexity gives

    (C_z+C_z')/2 subset C_m.

Brunn--Minkowski gives volume at least `M` on the left. If the
midpoint fiber has volume at most `M`, equality holds in
Brunn--Minkowski. Its equality characterization for positive-volume
convex bodies says that the endpoint bodies are homothetic. Equal
volumes make the homothety factor one, so they are translates. QED.

Here is an explicit nontranslation certificate for the actual source
types. Fix a row `j` that is a chain root for type `a`. The displayed
vertices of `T_a` in the direct construction show

    max_(T_a) f_j=1,    min_(T_a) f_j=-1/3,
    width_(f_j)(T_a)=4/3.                                (25)

The maximum occurs at the root vertex `e_j`. The minimum occurs at
the three-coordinate average of the next chain, where
`lambda_j=0` and `lambda_(j+1)=1/3`.
For either other type the same row is an internal chain edge.
If it is the first internal edge, inspection of the three chain
vertices gives maximum zero and minimum `-1/2`. If it is the second,
the extrema are zero and `-1`. Vertices on other chains give zero.
The two other widths are therefore

    1/2 and 1.                                          (26)

The contraction defining `P_a` multiplies every width by its common
positive factor `s`; translation does not affect widths. Thus the
three bodies `P_a` are pairwise nontranslates. The same is true of
`2P_a` and of their translates `K_I` of different types.

Now replace the integer coordinate of the actual sharp body by twice
that coordinate. This is a valid new convex body but is not a
lattice-preserving normalization. For singleton indices `i,j` of
different types, the new fibers at `2e_i` and `2e_j` are the old
fibers `2P_tau(i)` and `2P_tau(j)`, each of volume `M`. Their midpoint
`e_i+e_j` is an integer point. By Lemma 5 its fiber has volume
strictly greater than `M`.

Thus the original equal-volume source table and maximum-fiber bound
cannot survive this dilation: a new integer fiber becomes larger
than every original generating fiber. This is a rigorous regrowth
certificate, not a numerical observation. A recursive construction
using dilation must control these actual new fibers, rather than
reusing only the old parity representatives.

## 8. Consequences for further constructions

The proved restrictions distinguish three obstructions:

* Changing the outer weights or the continuous dimension within the
  original projection template cannot make `2^n D(C)` tend to zero;
  Corollary 2 applies to every such body.
* Independent powers, even with arbitrary common simplex padding,
  cannot amplify the fixed paired-source families covered by (18)--(20)
  to a weak counterexample. The explicit actual centers in (13) and
  (24) give a uniform positive constant and eventual sharp repair.
* Enlarging the lattice projection by integer dilation introduces
  larger midpoint fibers whenever it identifies different equal-volume
  source shapes in one parity class. Lemma 5 and (25)--(26) certify
  this effect for the present sources.

Any different construction intended to make `2^n D(C)->0` must
establish (3), specify the new integer-fiber census, and control cuts
at the resulting nonexposed fibers. These are necessary tests, not
unproved lemmas being proposed as a solution. No weak-counterexample
construction is asserted here.
