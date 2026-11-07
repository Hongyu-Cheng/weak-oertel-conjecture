# A rational sharp-bound counterexample with (n,d)=(167,99)

Research result, 7 November 2026. This refines the symmetric (168,99)
construction by using unequal block sizes and an asymmetric triangular
fan. All arithmetic predicates used below are rational. The result is
not a Lean formalization. It refutes the sharp constant Gamma_99, not
the smaller constant 1/e or the existence of some universal positive
constant.

## Statement

There is a full-dimensional rational convex polytope C in
R^167 times R^99, with every nonempty integer fiber of continuous
dimension 99, such that

\[
 \sup_{\mathbf y\in C\cap(\mathbb Z^{167}\times\mathbb R^{99})}
 \operatorname{depth}(\mathbf y)
 <\frac{(99/100)^{99}}{2^{167}}.
\]

Depth uses all containing proper closed ambient halfspaces and the
normalized sum of the 99-dimensional volumes of the integer fibers.

## 1. A fully rational triangular fan

In planar coordinates let u_0=(0,0), u_1=(1,0), u_2=(0,1), and put

\[
 \mathbf p=(334371,332129)/10^6,
 \quad
 (\mathbf n_0,\mathbf n_1,\mathbf n_2)
 =\frac1{10^6}\bigl((-599637,-800272),(971233,238130),
                         (-310548,950558)\bigr).
\]

Set

\[
 w_0=1,\qquad w_1=\frac{58465186893}{71226006661},\qquad
 w_2=\frac{317229508283}{498582046627}.
\]

These weights are positive and satisfy sum_a w_a n_a=0. Define
g_a(u)=w_a n_a dot (u-p). At u_a, g_a is positive; at the other
two triangle vertices it is negative. Each pair of normals is independent.

The following rational points lie on g_(a+1)=0, with indices cyclic:

\[
 \mathbf q_0=\left(\frac{403842028213}{971233000000},0\right),\quad
 \mathbf q_1=\left(\frac{52763454809}{90079000000},
                    \frac{37315545191}{90079000000}\right),\quad
 \mathbf q_2=\left(0,\frac{93258952483}{160054400000}\right).
\]

Let theta_a^max be the positive number
|det(u_a-p,q_a-p)|, the area ratio of conv(p,u_a,q_a) to the
unit-coordinate triangle. On this source triangle, every missed row
g_j, j different from a, is nonpositive and the own row g_a is
nonnegative. All these statements follow by exact evaluation at its
three displayed vertices.

Choose the common positive-fiber volume ratio and three dilations

\[
 m=\frac{660847}{200000},\qquad
 (\delta_0,\delta_1,\delta_2)
 =\left(\frac{325903}{10^7},\frac{6517257}{200000000},
                              \frac{50753}{1562500}\right).
\]

Define, using rational operations only,

\[
 \theta_a=\frac{m}{(1+\delta_a)^{99}},\quad
 k_a=\frac{\theta_a}{\theta_a^{\max}},\quad
 \widehat{\mathbf q}_a=\mathbf p+k_a(\mathbf q_a-\mathbf p).
\]

Exact arithmetic gives 0<k_a<1. Thus the contracted triangle
conv(p,u_a,qhat_a) is still in the same source cone, has area ratio
theta_a, and has the same two rays at p. This rational contraction
ensures exactly equal positive-fiber volumes despite the unequal deltas.

For each a, let b,c be the other two indices and define

\[
 \beta_a=
 \frac{g_a(\mathbf u_a)}{g_a(\mathbf u_a)-g_a(\mathbf u_b)}
 \frac{g_a(\mathbf u_a)}{g_a(\mathbf u_a)-g_a(\mathbf u_c)}.
\]

The positive g_a cap in the planar triangle has area ratio beta_a:
the two displayed fractions are its edge-length ratios from u_a.

## 2. Join with 97 free simplex vertices

For a planar point u=(u_x,u_y), write
u-bar=(1-u_x-u_y,u_x,u_y,0,...,0) in R^100. Put

\[
 \mathbf o_j=\begin{cases}(3/100)\overline{\mathbf p}_j,&j=0,1,2,\\
                    1/100,&3\le j\le99.
              \end{cases}
\]

Every coordinate of o is positive and their sum is one. Work in
L={x in R^100: sum_j x_j=0}, with barycentric coordinates
lambda_j(x)=x_j+o_j. Let

\[
 B=\operatorname{conv}\{\mathbf e_j-\mathbf o:0\le j\le99\},\quad
 T_a=\operatorname{conv}\{\overline{\mathbf p}-\mathbf o,
          \overline{\mathbf u}_a-\mathbf o,
          \overline{\widehat{\mathbf q}}_a-\mathbf o,
          \mathbf e_3-\mathbf o,\ldots,\mathbf e_{99}-\mathbf o\}.
\]

These are full-dimensional 99-simplices. If b=|B|, then |T_a|=theta_a b:
the barycentric vertex determinant has the indicated 3-by-3 planar block
and a 97-by-97 identity block.

For x in L define

\[
 f_a(\mathbf x)=\sum_{i=0}^2g_a(\mathbf u_i)\lambda_i(\mathbf x).
\]

These functions are linear: their value on the barycentric vector o is
(3/100)g_a(p)=0. Their sum is zero. On T_a their own minimum and each
missed maximum are zero. Their absolute values on B are at most one,
as can be checked at its vertices. The cap B intersect {f_a>=0} is
the join of the planar cap with the 97 free vertices. Its volume is
beta_a b by the same determinant calculation.

Let epsilon=10^(-20). For each a, define d_a in R^100 as the unique
vector supported on coordinates 0,1,2 satisfying

\[
 \sum_{j=0}^2(d_a)_j=0,\qquad
 \sum_{i=0}^2g_j(\mathbf u_i)(d_a)_i
       =\begin{cases}2,&j=a,\\-1,&j\ne a.\end{cases}
\]

One of the three row equations is redundant; the other two and the
zero-sum condition give an invertible rational system. Put c_a=epsilon d_a
as a vector in L. Then f_a(c_a)=2epsilon and f_j(c_a)=-epsilon for j!=a.
The exact checker verifies |(d_a)_i|<3. It also expresses the planar
direction ((d_a)_1,(d_a)_2) as

\[
 U_a(\mathbf u_a-\mathbf p)+V_a(\widehat{\mathbf q}_a-\mathbf p),
 \qquad U_a>0,\quad V_a>0,\quad U_a+V_a<6.
\]

Consequently c_a is in the interior of T_a: its coefficients are
3/100-epsilon(U_a+V_a), epsilon U_a, epsilon V_a, and 1/100
on each of the 97 free vertices. All coefficients are positive and sum
to one. In particular |lambda_j(c_a)-o_j|<=10epsilon for every j.

## 3. The generating fibers

Partition the 167 integer-coordinate indices into three blocks of sizes
(N_0,N_1,N_2)=(56,56,55). Put

\[
 \delta'_a=\delta_a+10^{-12},\qquad
 t_a=1-\delta'_a,\qquad
 \eta_a=1-\frac{\delta_a+\delta'_a}{2}.
\]

Thus 0<t_a<eta_a<1-delta_a, and 1-30delta'_a>0.
At integer base zero put B. At every nonempty positive Boolean base
1_I, choose the type a(I) of the least index in I and let k=|I|. Put

\[
 K_I=(1+\delta_{a(I)})T_{a(I)}+(k-\delta_{a(I)})\mathbf c_{a(I)}.
\]

At every negative base -1_J with J in block a and 1<=r=|J|<=30 put

\[
 G_{a,r}=(1-r\delta'_a)T_a-r t_a\mathbf c_a.
\]

Let C be the convex hull of these generating fibers. They are finite in
number, rational, and full-dimensional in L. The middle fiber and positive
unit bases span all 99+167 ambient directions, so C has nonempty interior.

The integer projection is exactly the listed positive Boolean cube and
the listed negative Boolean vertices. All projected coordinates lie in
[-1,1]. If an integer point has a coordinate -1, every generator used in
its convex representation must be a negative vertex from the same block
and must include that coordinate. At each other coordinate the integer
value, zero or -1, forces respectively exclusion or inclusion in every
used subset. All used vertices are therefore the same listed vertex.
If there is no negative coordinate, the point is a positive Boolean vertex.

Every nonzero listed base is exposed. With rho=1/168, give coefficients
1 on a prescribed support and -rho elsewhere for a positive base; negate
these coefficients for a negative base. Among bases of its own sign the
desired Boolean vertex is the unique maximizer. Bases of the opposite
sign have value at most rho*167<1, whereas the desired value is the
positive support size. The zero base also has smaller value. Thus all
noncentral actual fibers are exactly their prescribed fibers.

## 4. The actual origin fiber

For an integer coordinate i of type a define the facet price

\[
 v_{i,j}=\delta_a o_j+10(1-\delta_a)\varepsilon,
                  \qquad 0\le j\le99.
\]

Every generating point (z,x) satisfies
lambda_j(x)+sum_i v_(i,j) z_i>=0. To prove this at a positive base I
with chosen type a, use lambda_j>=0 on T_a and the bound on c_a.
The coefficients in K_I sum to k+1, so its barycentric coordinates are
bounded below by -delta_a o_j-10(k-delta_a)epsilon. Adding the facet
price gives at least

\[
 \left(\sum_{i\in I}\delta_{\operatorname{type}(i)}-\delta_a\right)
              (o_j-10\varepsilon)\ge0.
\]

The first factor is nonnegative because I contains a coordinate of type a.
The second is positive.

At a negative base of type a and size r, the fiber coefficients sum to
1-r. Its barycentric coordinates are at least
r[delta'_a o_j-10t_a epsilon]. Subtracting its r facet prices leaves
at least r times

\[
 (\delta'_a-\delta_a)o_j
       -10(2-\delta_a-\delta'_a)\varepsilon>0.
\]

Indeed o_j>99/10000 and delta'_a-delta_a=10^(-12), while epsilon=10^(-20).
Middle generators satisfy the inequalities as well. They are affine, so
hold on C. At z=0 they impose exactly lambda_j>=0, hence the actual
origin fiber is contained in B. The reverse containment is prescribed.
This controls all balanced combinations, including overlapping subsets.

## 5. Three cuts cover every middle point

Put R=3(167+1)=504. For row j, use continuous functional f_j, integer
coefficient -R on block j and eta_a epsilon on each other block a.
Let H_j be its nonnegative closed halfspace.

If a positive support I meets block j, its continuous score is at most
k+1 because T_a and c_a lie in B and f_j<=1 there. Its integer score
is at most -R+k-1. Thus it is strictly excluded. If I misses block j,
its source type a differs from j and its maximum total score is

\[
 \varepsilon\left[\delta_a-
                \sum_{i\in I}(1-\eta_{\operatorname{type}(i)})\right]<0.
\]

Strictness follows from 1-eta_b>delta_b and the presence of type a in I.
For a negative fiber of unpaid type a!=j, the maximum score is
r(t_a-eta_a)epsilon<0. For a paid negative fiber, the minimum is
r(R-2t_a epsilon)>0. Consequently each cut contains precisely its
own middle cap and its own block of negative fibers. These three cuts
cover B, since sum_j f_j=0. The exclusions are strict and the cuts closed.

## 6. Exact mass inequalities and the every-point bound

Let Gamma=(99/100)^99 and define the exact rational sums

\[
 E_a=\theta_a\sum_{r=1}^{30}\binom{N_a}{r}(1-r\delta'_a)^{99},
 \qquad E=E_0+E_1+E_2.
\]

Every positive fiber has volume mb exactly. Every negative fiber has
volume at most theta_a b<mb. The total mixed-integer volume is
W=b[(2^167-1)m+1+E], and cut H_a has mass b(beta_a+E_a).
Exact fraction comparisons give

\[
 1+E-m>\frac8{100000},\qquad
 \Gamma m-\beta_a-E_a>\frac8{100000}\quad(a=0,1,2).
\]

For orientation, the surplus is approximately 0.0000867647347 and the
three cut margins are 0.0000906987327, 0.0000859337881, and
0.0000882177570. No floating-point value is a premise of these inequalities.

Every point of the middle fiber belongs to one of the three cuts, of
mass strictly below Gamma mb. A noncentral fiber is a 99-simplex.
At any of its points, some barycentric coordinate is at least 1/100.
The vertex cap through that coordinate has volume at most
(99/100)^99 times the fiber volume, hence at most Gamma mb. Write the
cap as a(x)>=0 and let h expose its base z_0. Use the affine halfspace
a(x)+Q[h(z)-h(z_0)]>=0. Subtracting h(z_0) leaves the chosen cap
unchanged. A sufficiently large finite positive Q strictly excludes every
other integer fiber: the exposing gaps are positive, and the finitely many
compact fibers have bounded scores.
The resulting ambient halfspace is proper and closed.

Thus all points have a common uniform upper bound

\[
 \sup_{\mathbf y}\operatorname{depth}(\mathbf y)
 \le\frac{\Gamma m}{(2^{167}-1)m+1+E}
 <\frac{\Gamma}{2^{167}}.
\]

By ordinary Grünbaum in a positive simplex fiber, its centroid attains
the first upper bound, so that expression is also the exact maximum depth.
This optional equality shows, using the exact comparison
2^167 Gamma m/[(2^167-1)m+1+E]>24/65>1/e, that this body is not a
counterexample to the smaller 1/e bound. The last inequality follows from
e>sum_(j=0)^4 1/j!=65/24.

A rational linear identification L with R^99 preserves halfspaces and
multiplies all fiber volumes by the same positive factor. The normalized
fiber-volume sum agrees with normalized 99-dimensional Hausdorff measure
on the disjoint actual fibers. This proves the stated rational-polytope
and intrinsic-measure conclusions.

## Scope

The continuous target d<100 is achieved. The integer target n<100 remains
open in this research task. No optimality is claimed for n=167, and no
conclusion about the weaker universal-constant conjecture follows.
