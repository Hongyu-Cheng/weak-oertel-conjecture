# A sharp-bound counterexample with 168 integer and 99 continuous variables

Research result, 7 November 2026. The exact scalar checks below pass. The
geometric argument is supplied in full for independent review. This is not
a Lean formalization. The target is the sharp constant
\(\Gamma_{99}2^{-168}\), not the smaller constant \(1/(e2^{168})\).

## Statement

There is a full-dimensional rational convex polytope \(C\) in
\(\mathbb R^{168}\times\mathbb R^{99}\) whose every nonempty integer fiber
has dimension 99 and whose normalized mixed-integer halfspace depth satisfies

\[
 \sup_{\mathbf y\in C\cap(\mathbb Z^{168}\times\mathbb R^{99})}
 \operatorname{depth}(\mathbf y)<\frac{(99/100)^{99}}{2^{168}}.
\]

The construction replaces the product of a source with a box and a huge
simplex padding factor by a simplex join. Every noncentral fiber is itself
a 99-simplex, so its exact ordinary simplex depth constant is available.
Negative Boolean subsets supply many outer fibers without assigning a new
integer coordinate to each one. Only subsets of size at most 30 are used.

## 1. The middle simplex, three cuts, and source simplices

Work in the 99-dimensional rational linear subspace
\(L=\{\mathbf x\in\mathbb R^{100}:\sum_{i=0}^{99}x_i=0\}\).
Put \(\mathbf o=(1/100,\ldots,1/100)\),
\(\mathbf v_i=\mathbf e_i-\mathbf o\),
\(B=\operatorname{conv}\{\mathbf v_0,\ldots,\mathbf v_{99}\}\), and
\(\lambda_i(\mathbf x)=x_i+1/100\). A rational linear identification of
\(L\) with \(\mathbb R^{99}\) preserves all volume ratios and halfspaces.
Let \(b=|B|\).

Indices \(a\), \(a+1\), \(a+2\) in the next formulas are cyclic modulo 3.
Define

\[
 f_a=\lambda_a-\frac27\lambda_{a+1}-\frac57\lambda_{a+2},\qquad
 \mathbf p=\frac{\mathbf e_0+\mathbf e_1+\mathbf e_2}{3}-\mathbf o,
 \qquad
 \mathbf q_a=\frac{7\mathbf e_a+5\mathbf e_{a+1}}{12}-\mathbf o.
\]

The \(f_a\) are linear on \(L\), are nonzero, and sum to zero. Define the
99-simplex

\[
 T_a=\operatorname{conv}\{\mathbf p,\mathbf v_a,\mathbf q_a,
                                  \mathbf v_3,\ldots,\mathbf v_{99}\}.
\]

Its barycentric vertex determinant is the 3-by-3 determinant of
\(( (1/3,1/3,1/3),\mathbf e_a,(7\mathbf e_a+5\mathbf e_{a+1})/12 )\)
times an identity determinant. Consequently
\(\theta:=|T_a|/b=5/36\). On \(T_a\), each missed row \(f_j\), \(j\ne a\),
has maximum zero, and \(f_a\) has minimum zero. These claims follow by
checking the displayed vertices. On all of \(B\), \(-1\le f_j\le1\).

The cap \(B\cap\{f_a\ge0\}\) is the join of a triangle in the first
three-coordinate face and the remaining 97 vertices. Its edge ratios from
\(\mathbf v_a\) are \(7/9\) and \(7/12\). Therefore its exact volume is
\(\beta b\), where \(\beta=49/108\). This also follows from its
100-by-100 barycentric vertex determinant, whose nontrivial block has size 3.

Set \(\varepsilon=10^{-14}\). Choose \(\mathbf c_a\) by

\[
 \lambda_a(\mathbf c_a)=\frac1{100}+\frac{49}{39}\varepsilon,
 \quad \lambda_{a+1}(\mathbf c_a)=\frac1{100}-\frac{14}{39}\varepsilon,
 \quad \lambda_{a+2}(\mathbf c_a)=\frac1{100}-\frac{35}{39}\varepsilon,
\]

with every other coordinate equal to \(1/100\). Then
\(f_a(\mathbf c_a)=2\varepsilon\) and
\(f_j(\mathbf c_a)=-\varepsilon\) for \(j\ne a\).
This point is in the interior of \(T_a\): its coefficients on
\(\mathbf p,\mathbf v_a,\mathbf q_a\) are respectively
\(3/100-35\varepsilon/13,7\varepsilon/5,84\varepsilon/65\), and its
coefficients on each other vertex are \(1/100\). All are positive.

## 2. Rational parameters and generating fibers

Put

\[
 \delta=\frac{3258435}{10^8},\qquad
 \delta'=\delta+10^{-10},\qquad t=1-\delta',\qquad
 \eta=1-\frac{\delta+\delta'}2,\qquad N=56,\quad n=3N=168.
\]

Partition the integer-coordinate indices into three blocks \(I_a\) of
size 56. At the base \(\mathbf0\), put \(B\). For every nonempty Boolean
set \(I\subseteq\{1,\ldots,n\}\), select one member of \(I\), let
\(a(I)\) be its block type and \(k=|I|\), and put at \(\mathbf1_I\)

\[
 K_I=(1+\delta)T_{a(I)}+(k-\delta)\mathbf c_{a(I)}.
\]

For every nonempty \(J\subseteq I_a\) with \(r=|J|\le30\), put at
\(-\mathbf1_J\)

\[
 t_r=1-r\delta'>0,\qquad
 G_{a,r}=t_r T_a-rt\mathbf c_a.
\]

Take \(C\) to be the convex hull of these finitely many generating fibers.
All generators are rational full-dimensional 99-simplices. The origin
fiber spans \(L\), and the positive unit bases span all 168 projected
directions, so \(C\) has full ambient dimension and nonempty interior.

## 3. Exact integer projection and noncentral fibers

Its integer projection points are exactly

\[
 Z=\{0,1\}^{168}\ \cup\
 \{-\mathbf1_J:\varnothing\ne J\subseteq I_a,\ |J|\le30,\ a=0,1,2\}.
\]

Every projected coordinate lies in \([-1,1]\). If an integer point has
coordinate \(-1\) at an index in \(I_a\), every generator in any convex
representation must be a negative Boolean vertex from that same block
with that coordinate \(-1\). At every other coordinate, an integer value
is either \(-1\), forcing inclusion in every used subset, or zero,
forcing exclusion from every used subset. Thus every used generator is
the same listed negative vertex. If no coordinate is negative, the point
belongs to the positive Boolean cube. This proves the census, including
the fact that omitted larger negative subsets do not appear.

Every nonzero listed base is exposed. Put \(\rho=1/(n+1)\). For
\(\mathbf1_I\), use coefficients 1 on \(I\) and \(-\rho\) elsewhere;
its value is \(|I|\), and every negative generator has value at most
\(\rho n<1\). For \(-\mathbf1_J\), negate that functional for the set
\(J\). Its value is \(|J|\); every other negative Boolean vertex has a
strictly smaller value, and every positive one has value at most
\(\rho(n-|J|)<1\). These functionals also strictly beat the zero base.
Thus the actual fibers at all nonzero bases equal their prescribed fibers.

## 4. The origin fiber is exactly the prescribed simplex

Define

\[
 v=\frac\delta{100}+(1-\delta)\frac{35}{39}\varepsilon.
\]

Every generating point \((\mathbf z,\mathbf x)\) satisfies the 100
affine inequalities

\[
 \lambda_j(\mathbf x)+v\sum_i z_i\ge0\qquad(0\le j\le99).
\]

For a positive base of size \(k\), all barycentric coordinates on its
fiber are bounded below by

\[
 -\frac\delta{100}-(k-\delta)\frac{35}{39}\varepsilon\ge-kv.
\]

The difference between the two sides is
\((k-1)\delta(1/100-35\varepsilon/39)\ge0\).
Here the affine constant is accounted for by the fact that the two
coefficients in \(K_I\) sum to \(k+1\).

For a negative base of size \(r\), the coefficients defining \(G_{a,r}\)
sum to \(1-r\). Thus every barycentric coordinate is at least

\[
 r\left[\frac{\delta'}{100}-t\frac{49}{39}\varepsilon\right]>rv.
\]

The strict scalar difference after division by \(r\) is

\[
 \frac{\delta'-\delta}{100}
 -\left[(1-\delta)\frac{35}{39}+t\frac{49}{39}\right]\varepsilon
 =\frac{38187370854049}{39000000000000000000000000}>0.
\]

The middle generators satisfy these inequalities as well. Convexity
preserves them, and at \(\mathbf z=0\) they say precisely
\(\lambda_j(\mathbf x)\ge0\) for every \(j\). The actual origin fiber
is therefore contained in \(B\), and the reverse containment was included
among the generators. This controls every balanced convex combination,
including overlapping negative subsets and mixed source types.

## 5. Three ambient cuts cover the middle fiber

For row \(j\in\{0,1,2\}\), set \(R=3(n+1)\) and choose integer
coefficients \(-R\) on \(I_j\), \(\eta\varepsilon\) on the other two
blocks. Let \(H_j\) be the proper closed halfspace where \(f_j\) plus
this integer linear functional is nonnegative.

Every positive Boolean fiber is strictly excluded. If its support meets
\(I_j\), its largest continuous score is at most \(k+1\) and its integer
score is at most \(-R+k-1\); their sum is negative. Otherwise its source
type differs from \(j\), so its largest total score is exactly
\([k\eta-(k-\delta)]\varepsilon<0\), since \(\eta<1-\delta\).

On a negative fiber in an unpaid block, the largest continuous score is
\(rt\varepsilon\) and the integer score is \(-r\eta\varepsilon\).
Their sum is strictly negative because \(t<\eta\). On a negative fiber
in the paid block, its continuous score is at least \(-2rt\varepsilon\)
and its integer score is \(rR\), so the entire fiber is included.

Each cut therefore contains precisely its own middle cap and one block
of negative fibers. The three cuts cover the middle fiber because
\(f_0+f_1+f_2=0\). Boundary points are included; all exclusions are strict.

## 6. Exact volume inequalities

Define the rational numbers

\[
 m=\frac5{36}(1+\delta)^{99},\qquad
 E=3\frac5{36}\sum_{r=1}^{30}\binom{56}{r}(1-r\delta')^{99},\qquad
 \Gamma=\left(\frac{99}{100}\right)^{99}.
\]

Every positive fiber has volume \(mb\), and every negative fiber has
volume at most \(\theta b<mb\). The total mixed-integer volume is
\(W=b[(2^{168}-1)m+1+E]\), while each middle cut has volume
\(b(\beta+E/3)\). Exact rational arithmetic gives

\[
 1+E-m>\frac{38}{100000},\qquad
 \Gamma m-\beta-E/3>\frac{38}{100000}.
\]

For orientation only, \(m\approx3.3212060323\),
\(E\approx2.3215877422\), and the two margins are approximately
0.0003817099 and 0.0003820184. The checker compares integer numerators;
the proof does not depend on decimal approximations.

## 7. Every point and the strict sharp-bound violation

At a point of the middle fiber, one of the three displayed cuts contains
the point and has mass strictly below \(\Gamma mb\).

At any point in a noncentral fiber, that fiber is a 99-simplex. One of its
100 barycentric coordinates is at least \(1/100\). The vertex cap through
that coordinate has relative volume at most \(\Gamma\). Its integer
base is exposed. Write the cap as a(x)>=0 and let h expose its base z_0.
Use the affine halfspace a(x)+Q[h(z)-h(z_0)]>=0. Subtracting h(z_0)
leaves the chosen cap unchanged on this fiber. A sufficiently large finite
positive Q strictly excludes every other fiber: all exposing gaps are
positive and the finitely many compact fibers have bounded cap scores.
This yields a proper closed ambient halfspace of mass
at most \(\Gamma mb\).

Consequently every point has a containing halfspace of mass at most
\(\Gamma mb\), and

\[
 \sup_{\mathbf y}\operatorname{depth}(\mathbf y)
 \le\frac{\Gamma m}{(2^{168}-1)m+1+E}
 <\frac{\Gamma}{2^{168}}.
\]

In fact equality holds in the first inequality: at the centroid of a
positive simplex fiber, every ambient containing halfspace retains at
least a \(\Gamma\)-fraction of that fiber by the ordinary Grünbaum
inequality, and the other contributions are nonnegative. The uniform
upper bound just established matches it. This equality is not needed
for the counterexample itself.

All fibers have full continuous dimension and there are finitely many.
Normalized Euclidean Hausdorff measure on their disjoint affine subspaces
agrees with the fiber Lebesgue-volume sum. A rational linear coordinate
identification multiplies every fiber volume by the same constant, which
cancels in normalized depth.

## Scope

This proves a sharp-bound counterexample with continuous dimension below
100 and integer dimension 168. It does not attain both dimensions below
100. Its effective fiber-count surplus is extremely small relative to
\(2^{168}m\), so it does not violate the smaller \(1/(e2^{168})\) bound.
The repository's weak conjecture for some positive absolute constant is
unchanged. The source construction and its exact verification must not
be described as Lean-formalized or human-certified.
