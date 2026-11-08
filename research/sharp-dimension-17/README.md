# A sharp-bound counterexample in total dimension 17

[Manuscript PDF](../../output/pdf/oertel-sharp-dimension-17.pdf) ·
[LaTeX source](oertel-sharp-dimension-17.tex)

There is a rational polytope $C\subset\mathbb R^{12}\times\mathbb R^5$
of positive mixed-integer volume such that every point of
$\mathbb Z^{12}\times\mathbb R^5$ belongs to a closed halfspace whose
intersection with $C$ has mixed-integer volume strictly less than
$(5/6)^5/2^{12}$ times that of $C$. The twelve integer coordinates
comprise ten ordinary coordinates and two selectors. Changing the signs of
four ordinary coordinates between the zero-selector and nonzero-selector
layers allows three light pools of 252 sites each. The large fibers in
these pairs are truncated simplex joins.

## Integer support

Let $e_1,e_2$ be the selector coordinate vectors. For an ordinary
mask $J\subseteq\{1,\ldots,10\}$, write $b_J$ for its indicator
vector with the first four signs reversed. At each of the three
positive selector sites $e_1,e_2,e_1+e_2$, form the candidate bases
$(b_J,s)$ for all $J$. For $z=(y,s)$, put
$$
u=\sum_{i=1}^{10}y_i,\qquad
g(z)=\delta(3u-2s_1-2s_2),\qquad
\delta=\frac{664201}{10^6}.
$$
For each candidate choose it or its negative, whichever has
$g>0$, and give the chosen base a heavy fiber. The sign is unique
because $3u\ne 2(s_1+s_2)$ on these candidates. For each candidate
with $u=1$, also give the opposite base a light fiber. Its type is
$1,2,3$ for $s=e_1,e_2,e_1+e_2$, respectively. At selector zero,
give each $(\mathbf 1_J,0)$ with $J\ne\varnothing$ a heavy fiber,
and put the origin fiber at $(0,0)$.

The three positive selector labels have distinct nonzero parities.
At each, $b_J$ has the parity of $J$, so there is one heavy per
nonzero base parity, totaling $4095$. Reversing membership in the
first four positions gives $u$ equal to the new mask size minus
four. Thus there are $\binom{10}{5}=252$ light sites per type and
$756$ corresponding paired heavies.

Take the convex hull of the generators at these bases. Any integer
selector in the projection belongs to $\{0,\pm e_1,\pm e_2,
\pm(e_1+e_2)\}$. Indeed, a coordinate of magnitude one forces that
coordinate and sign in each contributing selector. The other
coordinate is then integral only if all contributors agree in it.
The same argument shows that each nonzero selector is an exposed
vertex of the selector hexagon. At a fixed nonzero selector, the
ordinary bases lie in a signed Boolean cube. Integrality fixes
each ordinary coordinate among the contributors, and every
retained vertex of that cube is exposed within the selector layer.

For an integer base at selector zero with a nonzero ordinary
coordinate $y_i$, its value is $1$ or $-1$. Every contributing
base has this same value. Write $c_i=-1$ on the first four
ordinary coordinates and $c_i=1$ on the other six. Every
contributing base with nonzero selector has
$c_i y_i(s_1+s_2)>0$, since at positive selectors $y_i$ has
sign $c_i$ and at negative selectors the opposite sign. Such
bases cannot contribute to selector zero. The zero-selector
generators have ordinary coordinates in the ordinary positive
Boolean cube, where integrality forces agreement in all
coordinates. For exposure at a nonzero zero-selector site, first
maximize one of its ordinary coordinates equal to $1$, then
maximize $-c_i(s_1+s_2)$ on that face to fix selector zero, and
then expose the desired vertex of the remaining ordinary cube.
Successive maximization on a finite support is equivalent to
maximizing a linear combination with sufficiently large weights
on the earlier functionals. Hence all nonzero bases are exposed,
the listed sites exhaust the integer projection, and each nonzero
fiber equals its generator. There are $4095+756+1=4852$ nonempty
integer fibers, all of positive volume.

## Continuous generators

Use the standard simplex $B=\operatorname{conv}(v_1,\ldots,v_6)$
in the affine hyperplane $\sum_i x_i=1$, with $v_i$ the coordinate
vertices. Volumes are in units of $|B|$, and dilations are about
its centroid. Dropping the sixth coordinate identifies the
continuous space with $\mathbb R^5$. With $a=663/1000$, define
$$
f_j=x_j-a x_{j+1}-(1-a)x_{j+2}\qquad (j=1,2,3),
$$
where the first three indices are cyclic. The scores sum to zero
and have absolute value at most one on $B$. Each trace
$B\cap\{f_j\ge0\}$ has relative volume
$\beta=1/[(1+a)(2-a)]$, the product of the two edge fractions
from $v_j$ in the active triangle. Joining the three remaining
vertices preserves this fraction.

Write $T_j=B\cap\{f_i\le0:i\ne j\}$.
The active quadrilateral for $T_1$ has vertices
$$
v_1,\quad
w=\frac{v_1+(1-a)v_2}{2-a},\quad
c=\frac{v_1+v_2+v_3}{3},\quad
v=\frac{v_1+a v_3}{1+a}.
$$
The diagonal from $v_1$ to $c$ gives two joined simplices
$U=\operatorname{conv}(v_1,c,v,v_4,v_5,v_6)$ and
$P=\operatorname{conv}(v_1,c,w,v_4,v_5,v_6)$ of volumes
$\theta=a/[3(1+a)]$ and $\phi=(1-a)/[3(2-a)]$, by their active
triangle determinants. In the displayed vertex order let
$\lambda_0,\ldots,\lambda_5$ be the affine barycentric coordinates
of $U$. Put $\epsilon=13/20000$ and
$$
K_1=T_1\cap\{\lambda_2\ge\epsilon\lambda_2(w)\}.
$$
This cuts off the portion of $P$ with barycentric coordinate at
$w$ greater than $\epsilon$, since $\lambda_2$ vanishes
on their common facet and $\lambda_2(w)<0$. The removed portion
is a homothetic simplex of scale $1-\epsilon$. Therefore $K_1$
has volume $V=\theta+\phi[1-(1-\epsilon)^5]$.
Cyclic rotations give $K_2,K_3$.

Use $B$ at the origin. At each paired heavy of type $j$ use
$(1+\delta)K_j$, and at its light partner use $(1-\delta)T_j$.
At each unpaired heavy use a simplex of volume $h^5$, where
$h=1111946415/10^9$. The following cuts specify which simplex.

## The covering cuts

Use the three ambient cuts with continuous scores $f_1,f_2,f_3$
and thresholds $3(u-s_2),3(u-s_1),3(u-s_1-s_2)$, respectively.
Their traces cover $B$ because the scores sum to zero. On
positive-selector candidates with $u=1$, the threshold vectors
divided by three are $(1,0,0),(0,1,0),(0,0,-1)$ at
$e_1,e_2,e_1+e_2$, respectively. Choosing the heavy sign
makes the single nonzero entry positive and gives $g=\delta$.
At its opposite light, the threshold in its own row is $-3$
and the others are zero. That row contains the entire light and
the others meet it in zero volume. The paired heavy misses all
three cuts in volume, since $K_j\subseteq T_j$ and $1+\delta<3$.

At each unpaired heavy the thresholds are all at least $3$,
except for the following three layers listed before taking the
heavy sign. At $e_1,e_2$ with $u=0$, the heavy uses the
negative sign and its divided threshold vector is $(0,1,1)$ or
$(1,0,1)$. At $e_1+e_2$ with $u=2$, the heavy uses the
positive sign and its divided threshold vector is $(1,1,0)$.
These are precisely the unpaired layers with a zero threshold.
The guard is $2\delta$ there. In an all-positive-threshold
layer use $hB$, which misses the cuts and fits the guard
because $h<1+2\delta\le1+g$ at every unpaired heavy.

For an unpaired heavy with threshold zero in row $j$, replace
$v_j$ in the simplex $B$ by
$$
t v_j+(1-t)v_{j+1},\qquad t=\left(\frac{h}{1+2\delta}\right)^5.
$$
The resulting simplex has relative volume $t$ by its determinant
and is contained in $B\cap\{f_j\le0\}$ since $t<a/(1+a)$.
Dilate it by $1+2\delta$, yielding volume $h^5$.
It misses row $j$ in volume, and the other thresholds $3$
exceed $1+2\delta$, so those rows miss it as well.

Every generator at $z$ lies in the centered dilation of $B$
by $1+g(z)$. Its facet bounds are $x_i\ge -g(z)/6$. These
bounds are affine in $z$ and reduce to $x_i\ge0$ at zero, so
the origin fiber is exactly $B$. The ordinary singleton bases and the two selector-only
heavies at $-e_1,-e_2$, together with the origin simplex, give
full ambient dimension. All generators are rational.

The three ambient cuts have equal mass $\beta+L$, where
$L=252(\theta+\phi)(1-\delta)^5$. At an unpaired heavy, the six
usual barycentric caps at threshold $1/6$ cover its simplex and
each has volume $\Gamma h^5$, with $\Gamma=(5/6)^5$.
At a paired heavy, rotate and dilate the following six caps on
$K_1$:
$$
\lambda_i\ge t_i,\qquad
(t_i)_{i=0}^5=\frac1{10^9}(166735371,166735294,166324902,
                          166734811,166734811,166734811).
$$
Their thresholds sum to one, so they cover. A cap in any heavy
fiber extends to an ambient cut missing the other integer fibers.
Add to its score a sufficiently large positive multiple of the
base exposing functional minus its value at that heavy base.
All the other integer fibers are compact and finitely many.
A point outside $C$ has a containing closed halfspace disjoint
from $C$ by strict separation.

## Exact comparison

In $U$ the index-$i$ cap has volume $\theta(1-t_i)^5$.
Set $q_i=\lambda_i(w)$. Solving the barycentric equations gives
$$
q_1=\frac{3(1-a)}{2-a},\qquad
q_2=-\frac{1-a^2}{a(2-a)},\qquad
q_0=1-q_1-q_2,\qquad q_3=q_4=q_5=0.
$$
In $P$, write $p$ for the barycentric coordinate at $w$
and $z_i$ for the coordinate at a shared vertex $i\ne2$.
Then $\lambda_i=z_i+q_i p$ for $i\ne2$ and
$\lambda_2=q_2 p$. The index-two cap misses $P$.
For $i\ne2$, omit $z_i$ from the coordinates of $P$.
In $0\le p\le\epsilon$, the cap condition is
$$
(1-q_i)p+\sum_{j\ne i,2}z_j\le1-t_i,\qquad z_j\ge0.
$$
This implies $z_i\ge t_i-q_i p\ge0$. The cap contribution
from $P$ is the difference of the volumes of two weighted
simplices, the second obtained by translating $p$ by $\epsilon$.
The cap volume in $K_1$ is thus
$$
C_i=\theta(1-t_i)^5+
\phi\frac{(1-t_i)^5-[1-t_i-(1-q_i)\epsilon]^5}{1-q_i},
$$
where the second term is absent for $i=2$.

The total mixed-integer volume is
$$
W=3339h^5+756(1+\delta)^5V+1+3L.
$$
The [rational checker](check.py) verifies the signed generator census
and the inequalities used in the generator containments and cap
formulas, together with
$$
\Gamma h^5-(\beta+L)>10^{-6},\qquad
\Gamma h^5-(1+\delta)^5\max_i C_i>10^{-9},\qquad
W-4096h^5>4\cdot10^{-5}.
$$
The covering cuts have normalized mass at most
$\Gamma h^5/W<\Gamma/4096$, as claimed.

## Reproduce the verification

With Python 3 and `elan` installed, run from the repository root.
The project pins Lean 4.34.1 and mathlib commit
`d13f23b723b8a846827a245b89c10fc7d3f11612`.

```sh
python3 research/sharp-dimension-17/check.py && (
  cd lean &&
  lake exe cache get &&
  lake build &&
  lake env lean CheckAxioms.lean
)
```

The Python assertions use exact rational arithmetic. The Lean development
proves the integer-fiber census, cut and body masses, and uniform depth bound
for a compact, full-dimensional convex body. `CheckAxioms.lean` checks that
the final theorem and the listed intermediate results depend only on
`propext`, `Classical.choice`, and `Quot.sound`. See
[`SharpOC.Selector17.sharp_oc_counterexample`](../../lean/SharpOC/Selector17Counterexample.lean).

## Build the manuscript

From the repository root, use XeLaTeX and latexmk with
`DejaVuSansMono.ttf` available to XeLaTeX (included in TeX Live).

```sh
build_dir=$(mktemp -d)
latexmk -xelatex -halt-on-error -outdir="$build_dir" \
  research/sharp-dimension-17/oertel-sharp-dimension-17.tex
```

The PDF is written to `$build_dir/oertel-sharp-dimension-17.pdf`.
