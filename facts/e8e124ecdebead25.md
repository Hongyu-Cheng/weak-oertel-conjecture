---
fact_id: e8e124ecdebead25
kind: theorem
author: "PK-research-agent"
assurance: LLM-verified
subgoal_id: pk-intake-strict-gap-deepest-source-stratification
depends_on: ["5a8a3be74f5481a9", "155691fc3768c06f", "5aeb5916857f97a9", "d90ba05577427854"]
verifier_run: 2d72dddbc6b2b2f6
target_match: null
---

## Source

- [36607dd22d2fb045](../candidates/36607dd22d2fb045.json), §6, (17)–(20).
- [86dd5366456916a8](../candidates/86dd5366456916a8.json), §4, finite tilt clipping and right quantiles.

## Statement

In the buffered limit setting of the sampled shift and depth limit theorem, take $P$ to be a complete affine-lattice base and suppose the $h_j$ are positive. Along a further subsequence let $J$ be the fixed set of all buffered maximizing bases whose closed pure-base depth exceeds $Q_j$ at each $j$. At each $p\in J$ there is exactly one maximizing mark $Y_{j,p}$. Pass to a subsequence along which all of them converge. Set $J_0=J\cap Z$ and $J_+=J\setminus Z$.

For any convex combination of bases in $J$ whose target $r$ belongs to $P$, the base $r$ belongs to $J$, its unique mark is the same combination of the input marks, and the positive input weights at finite $j$ satisfy
$$
\frac{h_j(Y_{j,p})}{h_j(Y_{j,q})}=
\left(\frac{|K_{j,p}|}{|K_{j,q}|}\right)^{1/d}
$$
for any two positive inputs $p,q$. Their centered fibers $K_{j,p}-y_{j,p}$ are positive homothets. No such combination uses positive weights in both $J_0$ and $J_+$. Each nonempty class is a closed minor and $k(J_0)+k(J_+)\le k(J)\le k(P)$ for inherited occupied parity counts.

## Proof

At fixed $j$ omit the index $j$, put $N=d+1$, and normalize each nonzero continuous normal by $\Gamma(u)=1$. At a mark write $F=E^{1/d}$ and $s=M^{-1/N}h^{1/N}F^{d/N}$ for the scalar displacement, using the current physical weight and current energy. Along anchored combinations of own-interior marks, $F$ is concave by 5aeb5916857f97a9 and the actual fiber inclusion. Such combinations stay own-interior by the combined input balls. Concavity of $h$ and the concavity and monotonicity of the positive weighted geometric mean show concavity of $s$ along these combinations.

For fixed $a,u$ with $\Gamma(u)=1$, the raw mass above the threshold for $a\cdot z+u\cdot X$ is continuous and nonincreasing. Let $c$ be the largest threshold with mass at least $Q$. This threshold exists, since $Q>0$, the projection is bounded, and the upper tail is continuous. The condition that the buffered cap at a mark $Y$ have mass at least $Q$ is exactly $a\cdot p+u\cdot y-s(Y)\le c$. These inequalities pass to anchored combinations by concavity of $s$. Every containing closed pure-base cap at a combination of input bases contains at least one positive input, so if all input base depths are strictly larger than $Q$, the combination also has a strict pure-base gap by finiteness of traces. Thus the combination of maximizing marks over $J$ is maximizing at a strict-gap sampled base.

We justify an attaining cap with proper own trace at any strict-gap maximizing mark $Y=(p,y)$. The mark is own-interior by the shift and depth limit theorem. For attainment, choose a constant $B$ larger than all absolute continuous evaluations $|u\cdot(X-y)+s(Y)|$ over the family and $\Gamma(u)=1$. Replace each tilt $a$ by the minimum-norm solution of a finite system: keep the evaluations $a\cdot(z-p)$ in $[-B,B]$ exactly fixed and constrain each remaining evaluation to stay $\ge B$ or $\le-B$ on its original side. The replacement preserves all cap traces. Its minimum-norm point belongs to the span of active constraint rows, since small motions in either orthogonal direction are feasible. A linearly independent subset of these rows determines the point in that span with right-hand sides of absolute value at most $B$. The finitely many possible row subsets give a uniform bound on replacement tilts. Compactness of the normalized continuous normals and bounded replacement tilts, and continuity of cap mass at nonzero continuous normals, now give attainment of the nonvertical infimum. The strict gap makes this infimum equal to $Q$.

An attaining cap contains positive own volume because $y$ is interior and $s(Y)\ge0$. If it contains the whole own fiber, its margin on the own minimum of $u\cdot X$ is nonnegative. Applying 155691fc3768c06f to $-u$ gives an affine minorant of all the sampled minima of $u\cdot X$, touching the own minimum. Adding its base slope to $a$ shows that the cap contains every fiber in the resulting closed nonnegative base trace through $p$, which has mass at least the pure-base depth. This contradicts the strict gap, so the own trace is proper. The tail is then strictly decreasing locally at the active threshold: each small slab around it intersects the own interior in positive volume. The active threshold is consequently the largest threshold with mass at least $Q$.

Uniqueness follows by applying an attaining proper cap at the midpoint of two distinct maximizing marks in the same strict-gap fiber. The midpoint maximizes by the anchored-combination argument. On that fiber $F$ is strictly concave in the interior by 5aeb5916857f97a9. With positive $h,F$ the weighted geometric mean is strictly increasing in $F$, making $s$ strictly concave there. The two input threshold inequalities would then be strict at the midpoint, contradicting activity.

At any anchored combination with target $r\in P$, use the attaining cap of its maximizing mark. Its threshold equals the right $Q$-quantile as just proved. Equality there, the input threshold inequalities, and concavity of $s$ force equality in the concavity inequality for $s$. Equality for the strictly increasing weighted geometric mean forces equality in both the $h$ and $F$ concavity inequalities and a constant ratio $h/F$ among positive inputs. By 5aeb5916857f97a9, equality for $F$ implies the marked homothety of their centered bodies. Projective energy scales as volume under homothety by d90ba05577427854, giving the displayed ratio.

Restore the index $j$. At each converging source the mark is uniformly interior, so its physical weight tends to its limiting roof value, which is zero exactly over $Z$. The positive limiting volumes bound every displayed ratio above and away from zero. Hence an anchored combination cannot mix the two classes. For a combination wholly in one class, equality for the physical weight passes to the limit, putting the target in the same class. This proves closedness of the minors. Distinct classes cannot share a parity, since two inputs of the same parity have a sampled integer midpoint by lattice completeness. The parity inequalities follow.
