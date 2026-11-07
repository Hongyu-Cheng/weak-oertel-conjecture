# Independent audit of the current 52-variable counterexample

Date: 2026-11-07. Audited source: [fact df488edae05a1702](../../facts/df488edae05a1702.md), [review](../../reviews/pk-n52-counterexample.md), and [exact checker](../../assets/pk-continuation-2026-11/check_integer_dimension_52.py), at commit `635ad260847e3a986502dd54cb465a614e77ce5b`.

The stated counterexample is mathematically supported by the supplied proof. I found no gap in the lattice census, actual-fiber argument, closed-halfspace construction, or scalar certificate. This is an independent mathematical audit assisted by exact arithmetic, not a formal proof. It establishes failure of the specific constant $1/e$, not failure of every smaller absolute constant in `problem_statement.md`.

## Geometry checked

1. **Integer census.** Every projected coordinate lies in $[-1,1]$. If an integer projection has a coordinate equal to $-1$, every generator contributing to that convex combination has that coordinate equal to $-1$. Such generators all belong to the same negative block; therefore the resulting integer projection is a negative Boolean vector in that block. If there is no negative coordinate, the projection is Boolean. This controls arbitrary convex combinations, including overlapping negative subsets.

2. **Nonzero fibers are actual fibers.** For a positive base, the proposed integer exposing functional takes its unique maximum there: the negative-base score is at most $N/(n+1)<1$. For a negative base, the positive-base score is less than $1$, and all other negative bases have strictly smaller score. Equality in an exposed-face convex combination therefore forces every contributing generator to have that same base.

3. **Origin fiber.** The barycentric coordinates are affine, so their constant terms must be retained when checking scaled and translated tetrahedra. On a positive fiber of cardinality $k$, writing $y\in T_a$ gives

   $$
   \lambda_j(x)=(1+\delta_s)\lambda_j(y)+(k-\delta_s)\lambda_j(c_a)-k/4.
   $$

   On a negative fiber of cardinality $r$, the corresponding formula is $\lambda_j(x)=t_r\lambda_j(y)-rt\lambda_j(c_a)+r/4$. These formulas give exactly the minima in the accepted proof. In particular, for $j\ne a$ the excess above $rv$ is $r(\delta_t-\delta_s)(1/4-\epsilon)>0$; for $j=a$, the remaining condition is the displayed parameter inequality (6). The box inequalities are also preserved. At the origin base they define precisely $B_0\times F$, while that whole fiber was included explicitly. Thus the origin fiber is exactly $B$.

4. **Origin cuts.** A positive Boolean fiber meeting the selected block has score at most $2k-R<0$. A positive fiber avoiding the block has score at most $[k\eta-(k-\delta_s)]\epsilon<0$. A negative fiber from a different block has score at most $r(t-\eta)\epsilon<0$; one from the selected block has positive minimum $r(R-3t\epsilon)$. Each cut therefore contains exactly its tetrahedral cap and one full negative block. The four cuts cover the origin fiber because the four centered barycentric functions sum to zero.

5. **Every point and closed boundaries.** At a nonzero base, the largest barycentric coordinate of the simplex gives a containing closed cap of relative mass at most $\Gamma_\ell$. A finite positive multiple of the integer exposing functional excludes every other fiber: there are finitely many strictly positive exposing gaps, and the simplex functional is bounded on the compact product. This tilt leaves the cap unchanged on the selected fiber. The continuous normal is nonzero, including a cap through a simplex vertex, so the halfspace remains proper. The proof has uniform strict mass bounds; hence it bounds the supremum of depth strictly, rather than merely proving a pointwise non-strict inequality.

6. **Dimension and measure.** The positive unit bases span all integer directions, and the origin fiber spans all continuous directions. Every assigned fiber is full dimensional because every displayed scale is positive. The finite sum of the fiber Lebesgue measures equals standard-normalized Euclidean Hausdorff measure on the mixed-integer set.

## Scalar verification

Running the supplied checker reproduced its committed JSON byte for byte. The graph integrity checker passed with 1,280 facts, 2,571 candidates, and 1,340 verification runs; that check concerns record integrity only.

I also checked the scalar enclosures independently by evaluating the fourteen powers as exact integers, without the supplied outward-rounding algorithm. With $h=274781$, use the common denominator and integer numerators

$$
\begin{aligned}
D&=32\cdot10^{27}\cdot100000^h,\\
M&=3(10^9+2)^3\,100001^h,\\
A&=12\sum_{r=1}^{13}\binom{13}{r}(10^9-3r)^3(100000-r)^h.
\end{aligned}
$$

Then $m=M/D$ and $E=A/D$. Direct integer comparisons confirmed all four strict bounds $1463268/10^6<m<1463269/10^6$ and $465669/10^6<E<465670/10^6$. This took approximately three seconds with standard Python integer arithmetic. The exact short reproduction is:

```python
from math import comb
h = 274781
D = 32 * 10**27 * 100000**h
M = 3 * (10**9 + 2)**3 * 100001**h
A = 12 * sum(comb(13, r) * (10**9 - 3*r)**3
             * (100000-r)**h for r in range(1, 14))
assert 1463268*D < 10**6*M < 1463269*D
assert 465669*D < 10**6*A < 465670*D
```

The supplied power algorithm is valid as well: all intermediate quantities are nonnegative, floor and ceiling divisions preserve enclosure under multiplication, and binary exponentiation preserves the exact-power invariant. Its scalar parameters, exponential-series tail bound, and strict rational margins were checked. The finite-dimensional estimate follows from

$$
\log(e\Gamma_\ell)=\int_0^1\frac{t}{\ell+t}\,dt<\frac1{2\ell},
\qquad
\exp(x)<\frac1{1-x}\quad(0<x<1).
$$

Thus $e\Gamma_\ell<1+1/(2\ell-1)$, with the required strictness.

## Why dimensions below 100 need different geometry

There is a necessary obstruction stronger than the limitations of the chosen padding estimate. For any finite mixed-integer support, let $a$ be the volume of a largest full-dimensional continuous fiber and let $W$ be the total mixed-integer volume. The centroid of that fiber has normalized ambient halfspace depth at least $\Gamma_d a/W$. Indeed, intersecting a containing ambient halfspace with the fiber yields either a containing halfspace in its continuous affine space or the whole fiber, and Grünbaum's centroid inequality applies. The exact centroid statement is proved in Section 3 of [Grünbaum, *Partitions of Mass-Distributions and of Convex Bodies by Hyperplanes*](https://msp.org/pjm/1960/10-4/pjm-v10-n4-p18-p.pdf), pp. 1259–1260; I checked this primary source.

Consequently, a strict $1/(e2^n)$ counterexample must have $W/a>e\Gamma_d2^n$. Also

$$
e\Gamma_d-1>\log(e\Gamma_d)
=\int_0^1\frac{t}{d+t}\,dt
>\frac1{2(d+1)}.
$$

There are two useful consequences.

* **The current support alone forces a large dimension.** If there are $L$ nonempty fibers, then $W/a\le L$, so a counterexample requires $L>e\Gamma_d2^n$. Here $L=2^{52}+4(2^{13}-1)$. Therefore

  $$
  d+1>\frac{2^{51}}{4(2^{13}-1)}
  =\frac{2^{49}}{8191}>6.87\cdot10^{10}.
  $$

  This obstruction survives arbitrary changes to the fiber volumes and shapes while keeping the same support and full continuous dimension. It is not specific to simplex padding. For $d\le99$, any successful support must contain more than $1.005\cdot2^n$ nonempty fibers; the current support has only about $7.28\cdot10^{-12}$ relative excess over $2^{52}$.

* **The current masses force a much stronger bound.** Here the largest fiber has volume $mb$ and $W/b=2^{52}m+\Delta$, where $\Delta=1+E-m$. The verified enclosures imply $0.002400<\Delta<0.002402$. Any convex-fiber construction preserving this normalized largest-fiber mass must therefore satisfy

  $$
  d+1>\frac{2^{51}m}{\Delta}
  >\frac{1647493304885792735232}{1201}
  >1.3717\cdot10^{18}.
  $$

  In particular, replacing the common simplex by another common factor, or improving only the estimate on $\Gamma_\ell$, cannot reach $d<100$. The existing choice $d\approx2.3058\cdot10^{18}$ is already within a factor below 1.69 of this necessary bound for the certified mass distribution.

The unpadded positive fibers are parallelotopes, because $T_a$ is an affine cube. Their centers have halfspace depth at least half their own mass. Removing the simplex factor entirely therefore does not preserve the counterexample. The large box dimension is another cost of the chosen volume parameters, but the largest-fiber and support obstructions show that optimizing it alone cannot achieve the requested low dimensions.

These bounds do not rule out other constructions with $n,d<100$. They show that such a search must change the support and mass distribution substantially. No accepted graph record was changed by this audit.
