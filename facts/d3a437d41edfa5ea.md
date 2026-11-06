---
fact_id: d3a437d41edfa5ea
kind: counterexample
author: "research-agent"
assurance: LLM-verified
subgoal_id: oct2s-full-joint-matching-tradeoff-attack
depends_on: ["8c92d1d2b1a1b7f5"]
verifier_run: 574b624cbf504414
target_match: null
---

## Statement

Use exactly the definitions of C_z, a_z, W, the half-mass metronoids K_z, eligible off-diagonal fractional same-parity matchings, and M_aff from accepted fact 8c92d1d2b1a1b7f5.

For each integer k>=4, set
\[
N=16^k,\qquad \delta=\frac{k}{N},\qquad L=2+\delta,
\]
and take n=d=N and the complete convex body
\[
C_k=\{(z,x)\in\mathbb R^N\times\mathbb R^N:
 |z_i|\le x_i\le L\quad(1\le i\le N)\}.
\]
Its entire positive lattice-fiber support, its actual fiber volumes, and its total mixed volume are
\[
Z_k=\{-2,-1,0,1,2\}^N,\qquad
a_z=\prod_{i=1}^N(L-|z_i|),\qquad
W_k=(4+5\delta)^N.
\]
There are no other nonempty lattice fibers, including no zero-volume lattice fibers. The largest fiber has volume L^N, and
\[
\frac{2^N\max_z a_z}{W_k}
=\left(\frac{4+2\delta}{4+5\delta}\right)^N
\le e^{-k/3}\longrightarrow0.
\tag{1}
\]
Furthermore
\[
\frac{\mathfrak M_{\rm aff}(C_k)}{W_k}\longrightarrow0.
\tag{2}
\]
Here is an explicit bound establishing (2). Define
\[
R=k+1,\qquad
B_k=\sum_{j=0}^{\min(16R^2,N)}\binom Nj,
\]
\[
J_k=4+4R^2\sqrt N,\qquad
F_k=(1+8\sqrt N)^{288\sqrt N}
\sum_{j=0}^{\min(J_k,N)}\binom Nj4^j,
\qquad
\beta=\frac34\,8^{1/16}<1.
\]
All the summation limits and exponents displayed here are integers because N=16^k. For every k>=4,
\[
\boxed{
\frac{\mathfrak M_{\rm aff}(C_k)}{W_k}
\le\frac1{4k}
+\frac{e^{k/4}}4
\left(\frac1{18\sqrt N}+B_k\beta^N+F_k2^{-N/32}\right).}
\tag{3}
\]
The right side tends to zero. In particular, no absolute positive lower bound on
\[
\max\left\{
\frac{2^n\max_z a_z}{W},\frac{\mathfrak M_{\rm aff}(C)}{W}
\right\}
\]
holds for all positive-mass mixed convex bodies.

## Proof

First audit the whole body and every lattice fiber. The body C_k is the Cartesian product of N compact full-dimensional triangles in R^2. It is convex and compact, and (z_i,x_i)=(0,L/2) satisfies all defining inequalities strictly, so it has nonempty interior in R^{2N}. We have 0<delta<1 and hence 2<L<3. At an integer base z, the fiber is the box product_i[|z_i|,L] if every |z_i|<=L, and is empty otherwise. Since L is strictly between consecutive integers 2 and 3, nonemptiness is equivalent to z in {-2,-1,0,1,2}^N, and every such box has all side lengths positive. This proves the complete support and the absence of zero-volume lattice fibers.

Summing the five possible side lengths independently in each coordinate gives
\[
W_k=(L+2(L-1)+2(L-2))^N=(4+5\delta)^N.
\]
The maximum volume is L^N, attained at z=0. Because
\[
\frac{2L}{4+5\delta}
=1-\frac{3\delta}{4+5\delta},\qquad N\delta=k,
\]
and 4+5delta<=9, the inequality (1) follows from 1-u<=exp(-u). Thus the full largest-fiber screening already passes, before any matching estimate.

For a parity vector v in {0,1}^N, let A_v be the actual total volume of its parity class, and let |v| count its ones. In an odd coordinate the two endpoints +/-1 each have side length 1+delta. In an even coordinate the choices 0,+/-2 have side lengths 2+delta,delta,delta. Consequently
\[
A_v=(2+3\delta)^{N-|v|}(2+2\delta)^{|v|},
\qquad \sum_vA_v=W_k.
\tag{4}
\]
In particular, with
\[
r_k:=\frac{2^N\max_vA_v}{W_k}
=\left(\frac{4+6\delta}{4+5\delta}\right)^N,
\]
we have
\[
1\le r_k\le\exp\left(\frac{N\delta}{4+5\delta}\right)
\le e^{k/4}.
\tag{5}
\]
This factor accounts for the actual, slightly unequal parity-class masses; no uniform parity law is assumed for the physical capacities.

Call a lattice base z bad if more than k^2 of its coordinates satisfy |z_i|=2. Under the probability distribution a_z/W_k, coordinates are independent, and each coordinate has probability
\[
\frac{2\delta}{4+5\delta}
\]
of being outer, that is, of having absolute value 2. The expected number of outer coordinates is therefore 2k/(4+5delta)<=k/2. Markov's inequality gives
\[
\frac{W_{\rm bad}}{W_k}
\le\frac1{2k},
\tag{6}
\]
where W_bad is the sum of actual volumes of bad fibers.

Now fix an arbitrary affinely half-metronoid realizable matching q in the exact sense of accepted fact 8c92d1d2b1a1b7f5. Fix any one of its witnessing affine maps s(m)=Am+b and any of its edge-specific contacts. Divide its edges into those having a bad endpoint and those having two good endpoints. The total mass Q_bad of the former edges obeys
\[
Q_{\rm bad}\le\sum_{z\ \mathrm{bad}}d_z(q)
\le\frac12W_{\rm bad}\le\frac{W_k}{4k}.
\tag{7}
\]
This is the original geometric endpoint ledger. Edges with two bad endpoints may be counted twice, which only enlarges its upper bound. Removing these edges leaves a realizable matching with the same affine map and the original degree constraints. Denote its mass in parity class v by Q_v and its total mass by Q_good.

We next bound every actual half-mass metronoid, with no restriction on its contacts. For a positive fiber let
\[
c_z=\frac L2\mathbf1+\frac{|z|}{2}
\]
be its centroid, where absolute values are coordinatewise. If X is uniform on that fiber, its independent coordinates are uniform on intervals of length at most L. Every y in K_z has a representation y=2E[Xf(X)] with 0<=f<=1 and E[f]=1/2. Thus Var(f)<=1/4, and for every u in R^N Cauchy-Schwarz gives
\[
|u\cdot(y-c_z)|
=2|\operatorname{Cov}(u\cdot X,f)|
\le\frac L{\sqrt{12}}\|u\|_2.
\]
Taking u=y-c_z proves
\[
K_z\subseteq c_z+\mathbb B_2^N,
\tag{8}
\]
because L<3 implies L/sqrt(12)<1. This argument applies to every permissible density, including densities depending on all coordinates.

For a parity vector v put
\[
c_v^0=\frac L2\mathbf1+\frac v2.
\]
For a good z of parity v, the difference c_z-c_v^0 is the indicator vector of its outer coordinates, and hence has Euclidean norm at most k. Consider any good positive edge e={z,z'} in class v, and let m_e=(z+z')/2. The edge-specific witness identity, (8), and the triangle inequality imply
\[
\|Am_e+b-c_v^0\|_2\le k+1=R.
\tag{9}
\]
Every such m_e is a quinary integer vector in {-2,-1,0,1,2}^N. Moreover
\[
|\operatorname{supp}(m_e)\setminus\operatorname{supp}(v)|\le2k^2,
\tag{10}
\]
because a nonzero midpoint in an even coordinate requires an outer coordinate at at least one endpoint.

For the fixed A,b define the enlarged set
\[
T_v=\left\{m\in\{-2,-1,0,1,2\}^N:
\|Am+b-c_v^0\|_2\le R,
\quad |\operatorname{supp}(m)\setminus\operatorname{supp}(v)|\le2k^2
\right\}.
\]
All good positive edge midpoints in this class lie in T_v. The set may also contain vectors having no eligible edge, which only enlarges the following upper bounds.

For m in T_v let j(m,v)=|supp(m) intersect supp(v)|. In each of these j odd coordinates an actual endpoint of an edge with midpoint m must have its sign prescribed by m: both endpoints are +1 if that coordinate of m is +1, and both are -1 if it is -1. If that coordinate of m is +/-2, there are no actual endpoints at all. In either case, the total actual volume of vertices that can be endpoints of edges with midpoint m is at most
\[
A_v2^{-j(m,v)}.
\]
Indeed, in an odd coordinate the two signs have equal actual side length, and all even coordinates and all remaining odd coordinates can be left unrestricted in this upper bound. Taking the union over all good positive edge midpoints, applying the original degree inequalities d_z(q)<=a_z/2, and counting each edge twice yields
\[
\boxed{
Q_v\le\frac{A_v}{4}
\min\left\{1,\sum_{m\in T_v}2^{-j(m,v)}\right\}.}
\tag{11}
\]
Thus the argument allows arbitrary selected edges, arbitrary fractional weights, and arbitrary correlations among endpoint choices.

Split the singular values of the completely arbitrary matrix A at epsilon=N^{-1/4}. Let h be the number strictly below epsilon, including zeros. First suppose h>=288 sqrt(N). Let P be the orthogonal projection onto their left singular subspace. It has rank h and ||PA||_{2 to 2}<=epsilon. If T_v is nonempty, choose m in it. Because ||m||_2<=2 sqrt(N), equation (9) gives
\[
\|P(c_v^0-b)\|_2\le R+2N^{1/4}\le3N^{1/4}.
\tag{12}
\]
The last inequality holds because R=k+1<=2^k=N^{1/4}.

For counting classes only, choose v uniformly from {0,1}^N. Then
\[
c_v^0=(L/2+1/4)\mathbf1+Y,
\]
where the coordinates of Y are independent, equiprobable +/-1/4. Put t=b-(L/2+1/4)1 and Xi=||P(Y-t)||_2^2. Direct expansion gives
\[
E\Xi=\frac h{16}+\|Pt\|_2^2,
\]
\[
\operatorname{Var}(\Xi)
=\frac1{64}\sum_{i<j}P_{ij}^2+\frac14\|Pt\|_2^2
\le\frac h{128}+\frac14\|Pt\|_2^2
\le\frac14E\Xi.
\tag{13}
\]
To check this calculation, the diagonal terms in Y^TPY are constant; its distinct off-diagonal products are pairwise uncorrelated and have second moment 1/256. The quadratic and linear terms are uncorrelated by symmetry. Finally, sum_{i<j}P_{ij}^2<=tr(P^2)/2=h/2.

We have E[Xi]>=h/16>=18 sqrt(N). The event (12) implies Xi<=9 sqrt(N)<=E[Xi]/2. Chebyshev's inequality therefore bounds the fraction of all parity vectors with T_v nonempty by
\[
\frac{\operatorname{Var}(\Xi)}{(E\Xi/2)^2}
\le\frac1{E\Xi}\le\frac{16}{h}
\le\frac1{18\sqrt N}.
\]
Using the actual parity masses through (5), and then (11), proves
\[
\frac{Q_{\rm good}}{W_k}\le\frac{r_k}{72\sqrt N}.
\tag{14}
\]

It remains to treat h<288 sqrt(N). Let P_s be the orthogonal projection onto the right singular subspace corresponding to singular values at least epsilon. For each v, invert these singular values on the corresponding left component of c_v^0-b, obtaining a vector m_v^0 in the range of P_s. Equation (9) then implies for every m in T_v
\[
\|P_sm-m_v^0\|_2\le R N^{1/4}=:K.
\tag{15}
\]
Thus T_v lies within distance K of the affine plane m_v^0+ker(P_s), whose dimension is h.

Here is a direct quinary-point count in this tube. If T_v is nonempty choose m_* in it, and project all its points orthogonally onto that plane. All projected points lie in a ball of radius 4 sqrt(N) about the projection of m_*, because the distance between two quinary vectors is at most 4 sqrt(N). This ball has a radius-one net containing at most (1+8 sqrt(N))^h points. A maximal set of points with pairwise distance greater than one is such a net: their radius-1/2 balls are disjoint inside the radius-(4 sqrt(N)+1/2) ball, and comparison of h-dimensional volumes proves the stated count. When h=0 the net has one point.

Assign each quinary point to a net point within distance one of its projection, and choose a representative m' in each nonempty cell. For two quinary points in one cell, the difference of their projections has norm at most two, and the difference of their normal residuals has norm at most 2K. These differences are orthogonal, so
\[
\|m-m'\|_2^2\le4+4K^2=J_k.
\]
At most J_k coordinates can therefore change, and each changed coordinate has at most four alternative quinary values. It follows that
\[
\#T_v\le (1+8\sqrt N)^h
\sum_{j=0}^{\min(J_k,N)}\binom Nj4^j\le F_k
\quad\text{for every }v.
\tag{16}
\]

For a fixed quinary m, at most B_k parity vectors can satisfy ||Am+b-c_v^0||_2<=R. In fact, if v_0 is one such vector, every other one satisfies ||c_v^0-c_{v_0}^0||_2<=2R. The square of this distance is one quarter of their Hamming distance. That distance is consequently at most 16R^2, proving the count B_k.

The number of quinary vectors with at most N/16 nonzero coordinates is at most
\[
\sum_{j=0}^{\lfloor N/16\rfloor}\binom Nj4^j
\le8^{N/16}\sum_{j=0}^N\binom Nj(4/8)^j
=8^{N/16}(3/2)^N.
\tag{17}
\]
Hence the fraction of parity classes whose T_v contains any such vector is at most B_k beta^N. The constant beta is strictly below one, since beta^{16}=3^{16}/2^{29}<1. Their total actual parity mass is at most r_k W_k B_k beta^N by (5).

In every remaining class, all m in T_v have more than N/16 nonzero coordinates. Equation (10), built into the definition of T_v, gives
\[
j(m,v)>N/16-2k^2\ge N/32,
\]
because 2k^2<=N/32 for k>=4. Combining (11) and (16) bounds Q_v in each such class by (A_v/4)F_k2^{-N/32}. Summing over all classes, and enlarging the latter term by r_k>=1, gives
\[
\frac{Q_{\rm good}}{W_k}
\le\frac{r_k}{4}
\left(B_k\beta^N+F_k2^{-N/32}\right).
\tag{18}
\]

Every affine map falls into one of the two singular-value cases. Adding their nonnegative bounds, using (7) and (5), gives exactly (3) for every admissible q. Taking the supremum over all such q proves that (3) bounds the full optimized M_aff, not just a prescribed matching or selector.

Finally, N=16^k, sqrt(N)=4^k, and R=k+1 imply
\[
\log B_k=O(k^2\log N)=O(k^3)=o(N),
\]
\[
\log F_k
=O\bigl(\sqrt N\log N+R^2\sqrt N\log N\bigr)
=O(k^3 4^k)=o(N).
\]
For these estimates one may bound each binomial term by N^j, include at most N+1 terms, and use J_k=O(k^2 sqrt(N)). Thus the second and third terms in parentheses in (3), even after multiplication by exp(k/4), tend to zero exponentially in N. The first satisfies exp(k/4)/sqrt(N)=(exp(1/4)/4)^k->0, while 1/(4k)->0. This proves (2).

The construction certifies both required full optimized ratios for actual complete bodies. It makes no inference from them to an upper bound on h_max(C_k); the locked depth conjecture requires a separate all-point argument.

## External sources

None.
