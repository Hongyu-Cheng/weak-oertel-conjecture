# Counterexample and descent proof review

Date: 2026-11-07.

Review method: a separate AI reviewer audited the proofs and ran the exact computations described below. This is not a human-review claim.

## Recommendation and exact scope

No blocking mathematical defect was found in the two research counterexamples or the seven auxiliary PR #4 facts assigned to this review. The mathematical content of PR #6 and PR #8 is suitable for merge, subject to the repository checks and separate Lean/integration reviews. The seven auxiliary facts are suitable for merge with their existing explicit hypotheses.

This is a proof audit plus fresh exact computation. It is not a complete formalization of mixed-integer Hausdorff measure and halfspace depth. The n=52 construction has not acquired a Lean proof through this review. The conclusions refute the proposed constant \(1/e\), and consequently the sharper dimension-dependent constant \((d/(d+1))^d\); they do not establish failure of every smaller unspecified universal positive constant.

The primary reviewed revisions are:

| Item | Revision | Mathematical source |
| --- | --- | --- |
| PR #4 auxiliary facts | `e5bbd45e3cb073e1c030bcc9e07726881d2af8f0` | Seven facts listed below |
| PR #6 | `3497df590ae6f7b8abaad88a5abe853ab993582e` | [a5291bca09ba4b1e](../facts/a5291bca09ba4b1e.md) |
| PR #8 | `2ffd469d639402e465de448fb31dd920eaf7f40a` | [df488edae05a1702](../facts/df488edae05a1702.md) |

The primary facts and all three source-checker implementations were read in full. The seven PR #4 fact files and the PR #6 theorem/checker bytes were also checked against their original pinned revisions; no intervening changes were silently substituted.

## 1. Fresh arithmetic evidence

All three source checkers exited successfully. Their regenerated certificates agreed with the tracked certificates as exact parsed JSON, including the retained binary-power traces where present:

- [check_barycentric_box_source_counterexample.py](../assets/pk-continuation-2026-11/check_barycentric_box_source_counterexample.py), for \(n=76\), \(d=1372129+2^{94}\).
- [check_integer_dimension_76.py](../assets/pk-continuation-2026-11/check_integer_dimension_76.py), for \(n=76\), \(d=1372131+2^{93}\).
- [check_integer_dimension_52.py](../assets/pk-continuation-2026-11/check_integer_dimension_52.py), for \(n=52\), \(d=274784+2^{61}\).

The source computations use positive rational intervals. Initial floor/ceiling bounds, multiplication, and squaring all round outwards. Binary exponentiation therefore preserves the inclusion of the exact power in the evolving interval. Positive prefactors and positive binomial-weighted sums preserve interval order. The final assertions compare rational endpoints, not floating-point displays. The explicit bounds on \(e\) use the factorial series with a geometric upper bound on its remaining positive terms.

The independent verifier now stored at [scripts/check_one_over_e_independently.py](../scripts/check_one_over_e_independently.py) does not reuse those binary-power routines. It uses
\[
\log a=2\sum_{j\geq0}\frac{y^{2j+1}}{2j+1},
\qquad y=\frac{a-1}{a+1},
\]
with a rational absolute remainder bound, followed by a degree-64 exponential Taylor enclosure at one sixty-fourth of the argument and six outward-rounded squarings. Negative logarithms are handled by interval reciprocation. Every arithmetic assertion uses Python's exact `Fraction`.

Run from the repository root:

```sh
python3 -B scripts/check_one_over_e_independently.py --output reviews/pr4-8-independent-arithmetic.json
```

The final portable version was executed successfully after normalization. Its complete rational output is [pr4-8-independent-arithmetic.json](pr4-8-independent-arithmetic.json). The independent uniform depth bounds give:

| Construction | Certified relative gap below \(1/(e2^n)\) | Certified absolute gap |
| --- | ---: | ---: |
| \(n=76\), \(h=1372126\), padding \(2^{94}\) | \(>6.6074860325\cdot10^{-29}\) | \(>3.2170817825\cdot10^{-52}\) |
| \(n=76\), \(h=1372128\), padding \(2^{93}\) | \(>7.6408794964\cdot10^{-29}\) | \(>3.7202249250\cdot10^{-52}\) |
| \(n=52\), \(h=274781\), padding \(2^{61}\) | \(>1.4749400343\cdot10^{-19}\) | \(>1.2048142829\cdot10^{-35}\) |

These are conservative lower bounds on the violation obtained from rational upper bounds on every point's depth. They are not exact values of maximum depth. The very small margins are the reason ordinary floating-point comparison would be inadequate.

For \(n=52\), the independently enclosed values are approximately
\[
m=1.463268530306766626469812490914,\quad
E=0.465669485365812944046524805678,
\]
and \(1+E-m=0.002400955059046317576712314764\). The report JSON contains rational endpoints for these quantities, \(e\), the simplex cap factor, and the final uniform bound.

The independent verifier also checks finite generator inequalities:

| Construction | Exact geometry checks |
| --- | --- |
| Each \(n=76\) parameter set | 1,024 singleton-origin facet inequalities, 1,200 mixed-type origin lower bounds, 76 free-box inclusions, 2,432 positive and 32 negative tetrahedral vertices, and 9,856 cut-sign inequalities |
| \(n=52\) | 1,664 positive and 416 negative tetrahedral vertices, 8,320 affine-facet inequalities, and 8,320 cut-sign inequalities |
| Small support calibration for the \(n=52\) exposure formula | 71,650 exact comparisons in block sizes 1 and 2 |

The minimum strict nonzero cut-sign gaps in these finite checks were respectively \(1/(2\cdot10^{16})\), \(1/(2\cdot10^{17})\), and \(1/(2\cdot10^{21})\). The small support calibration does not enumerate the actual \(2^{52}\) positive bases. The general support and exposure proofs were reviewed analytically.

The source replay and final portable verifier both exited 0 without stderr. The source-checker SHA-256 values were:

| Source checker | SHA-256 |
| --- | --- |
| Original \(n=76\) | `fda2f0440b4ad73df53a68921744426fc5e6727d701a17d5481daecd889e62b1` |
| Improved \(n=76\) | `ba88e5cf28b4a0c3ef6635e3f22fb65dc1951030bf6694ddc19c2e83183bb8f0` |
| \(n=52\) | `c77ad03cd0a17daea7f914caed3cdbe30b6544c09e84af27c58451c982e58bd9` |

## 2. PR #6: the \(n=76\) geometry

### Actual integer fibers

The integer projection is exactly \(\{0,1\}^n\cup\{-\mathbf e_i\}\). Every coordinate lies in \([-1,1]\). If an integer point has coordinate \(-1\), each generator appearing in a convex representation must have that coordinate \(-1\); the only such base is the corresponding negative unit vector. Otherwise the integer point is Boolean.

Every nonzero listed base is uniquely exposed by an explicit linear functional of the integer coordinates. Consequently convexification does not enlarge its assigned continuous fiber. This justifies using the assigned volumes in the total mass, rather than treating an arbitrary list of fibers as an actual convex source.

At the origin, cancellation of the integer coordinates forces
\(\mu_i=\sum_{I\ni i}\lambda_I\). The resulting continuous contribution decomposes into the displayed Minkowski sums
\(K(a,k)+\sum_{i\in I}A_{\tau_i}\). The singleton case uses the matching type, while the \(k\geq2\) case uses the stated uniform barycentric lower bound and the exact inequality \(2\kappa t\leq3-2s\). The free-box inclusion is checked independently. These inclusions prove that the actual origin fiber is exactly \(B\), not a larger convexification artifact.

### Four origin cuts

The four barycentric functionals sum to zero, so their nonnegative halfspaces cover every point in the origin fiber. In each row, the large negative integer coefficient excludes every positive Boolean fiber containing a paid coordinate. For the other Boolean fibers, the remaining continuous/integer support bound is strictly negative. Unpaid negative fibers are strictly excluded because \(t<\eta\); all paid negative fibers are included. Thus each cut has exactly the claimed mass \(b(\beta+N\alpha)\).

The continuous normals are nonzero. Their restrictions to the origin fiber have hyperplane boundaries of zero volume, while every intended exclusion on other fibers has a strict gap. Closed ambient halfspaces therefore have the stated masses.

### Padding and all-point bound

Each nonzero base is exposed. At every point in its product fiber, choose a simplex barycentric coordinate at least \(1/(\ell+1)\). Its containing cap has at most \(\Gamma_\ell\) of the padding simplex's volume. A sufficiently large but finite multiple of the integer exposing functional excludes every other integer fiber. Finiteness of the support and boundedness of the continuous fibers give a finite common choice for that particular cap; no limiting halfspace is required.

The source proof combines two uniform bounds: one for all origin points and one for all nonzero-fiber points. Their maximum is strictly below the target. This proves a strict bound on the supremum of depth, rather than only pointwise strict inequalities with a possibly vanishing gap.

Both displayed parameter sets satisfy the geometry, scalar inequalities, and final padded comparison. The improved continuous dimension \(1372131+2^{93}\) is consistent with the amended parameters.

## 3. PR #8: the \(n=52\) geometry

### Additional negative Boolean fibers

The negative support consists of nonempty negative Boolean subsets of a single block. If an integer point in the convex projection has a negative coordinate, all participating bases must have that coordinate \(-1\), hence must be negative generators of the same block. This excludes mixed-sign integer bases and negative subsets spanning several blocks. If there is no negative coordinate, the base is Boolean.

The positive and negative exposing functionals with \(\rho=1/(n+1)\) are strictly separating. The inequalities \(\rho N<1\) and the one-unit loss for a missing selected coordinate rule out ties with other bases. Therefore the assigned nonzero fibers survive convexification exactly.

### Origin fiber via affine inequalities

Every generator satisfies the same affine barycentric inequalities and free-box inequalities. At the origin these become precisely the defining inequalities of \(B_0\times F\). The negative selected-type facet is the potentially restrictive case; it is exactly the inequality
\[
N\bigl[\delta_s+4\epsilon(3t+1-\delta_s)\bigr]\leq1.
\]
The unselected-type inequalities use \(\delta_t>\delta_s\). These implications were checked directly from the displayed vertex formulas, independently of the source implementation. Since \(B\) is included as a generator, its actual origin fiber is exactly \(B\).

Every fiber is full-dimensional because all \(t_r\) and \(u_r\) are positive. The lifted convex hull is full-dimensional because the origin fiber spans the continuous directions and the positive unit bases span the integer-coordinate directions.

### Cuts, mass, and the sharper padding estimate

For an origin cut, every positive fiber is strictly excluded. A negative fiber is included exactly when it belongs to the paid block. Its cardinality \(r\) multiplies both the continuous support shift and the integer threshold, so the required strict sign remains valid for every \(1\leq r\leq13\). Equal block volumes yield the exact mass \(b(\beta+E/4)\).

The short rational bounds imply both the origin-cap inequality and
\[
1+E-m>\frac3{1250}
>\frac{2^{52}m}{2\ell-1}.
\]
The logarithmic integral identity
\(\log(e\Gamma_\ell)=\int_0^1 t/(\ell+t)\,dt<1/(2\ell)\),
together with \(e^x<(1-x)^{-1}\), gives
\(e\Gamma_\ell<1+1/(2\ell-1)\). All inequality directions are consistent with the required upper bound.

The same finite ambient-tilt argument handles every nonzero-fiber point. The two uniform bounds give a strict supremum bound. The independent verifier additionally evaluates the exact final gap by log/Taylor enclosures instead of relying only on the coarser displayed padding inequality.

The dimensions are \(n=52\) and
\(d=274784+2^{61}=2305843009213968736\). This substantially lowers the integer dimension relative to PR #6 but still uses an enormous continuous dimension.

## 4. Seven auxiliary PR #4 facts

### 5e8a8af95fa24a1d: equal-large-partner middle-star obstruction

[Proof](../facts/5e8a8af95fa24a1d.md).

The clipped four-simplex volume, algebraic rescaling, and midpoint inclusion are correct. The three lifted fibers are the actual fibers of the convex hull. The first group of endpoint-excluding caps localizes every hypothetical middle center in all five barycentric coordinates. The three stronger caps can simultaneously exclude both endpoints because their threshold sums have a strict support gap. The exact fourth-root lower bounds then contradict the sum of barycentric coordinates.

The centrally symmetric core of the clipped partner has the stated vertical intervals and volume. Its normalized half-volume is exactly \(2041/4576\), which exceeds the required sharp target at the displayed endpoint. The construction therefore obstructs the stronger middle-star selection claim while preserving an explicit successful endpoint. The proof does not misidentify it as an Oertel counterexample.

All printed rational volume, root-comparison, and surplus identities were recalculated exactly.

### 645f91d128f54e5b: every middle point misses the sharp target

[Proof](../facts/645f91d128f54e5b.md).

The 13-coordinate inclusion-exclusion identity in dimension 15 and the exact bound \(\rho<63/64\) are correct. The midpoint body remains inside the middle simplex, with all 13 specified coordinate support gaps uniform over the stated epsilon range.

The ambient thresholds are compatible: excluding both endpoints is equivalent to the displayed strict midpoint support inequality. The hypothetical-depth localization and the scalar function \(f\) give a contradiction with the correct derivative and second-derivative bounds. The closed-halfspace depth is upper semicontinuous, so compactness of the middle simplex upgrades the pointwise strict bound to a strict maximum bound.

The large endpoint is not a pyramid: its 29 facets are nonredundant, and each vertex lies on 15 of them, excluding a pyramid apex. The stated ordinary equality characterization therefore supplies a strict centroid surplus. The following asymmetry fact supplies a quantitative endpoint certificate for the entire explicit epsilon range. No unsupported endpoint surplus is needed for the middle-fiber obstruction itself.

### 6cab253207c34f9d: quantitative centroid surplus from asymmetry

[Proof](../facts/6cab253207c34f9d.md).

The same-mass cone comparison has the correct single-crossing order. On the positive side it bounds the first moment from above; on the negative side it gives the required density domination and retained-tail moment loss. Combining both moment losses with the centroid identity produces the displayed inequality (9), including its factor \(H^{-2}\). The split at \(H=(d+s)/2\), followed by the derivative bound for \(d+1-dp^{-1/d}\), gives the stated explicit surplus constant.

For the clipped 15-simplex, the conditional density is proportional to \(R^2\). The exact moment calculations give centroid coordinates \(529/17536\) and \(3553/17536\). The three facet ratios are \(567/529\), \(529/567\), and \(13983/3553\); testing those defining facets is sufficient for the asserted set inclusion. Their maximum is below 4. The resulting surplus \((11/32)^{16}/225>2^{-40}\) exceeds the endpoint target increment for every \(0<\epsilon\leq2^{-12}\).

These exact moment and ratio identities were recalculated. The result remains an ordinary sufficient surplus estimate, not a general mixed-integer theorem.

### 7fd6b5631ad64e4c: facet moments and partner reflection

[Proof](../facts/7fd6b5631ad64e4c.md).

The one-sided first-moment inequality follows from the same-mass cone and its single crossing. Coarea factors are included consistently. Applying it to the negative barycentric part gives
\(\lambda_i(g_B)\geq(2-|B|/|\Delta|)/(d+1)\).
The stretching-simplex example attains the coordinate bound and proves the half-volume threshold is sharp.

The reflection application quantifies over every point of the outer body, so it yields the full inclusion \(2g_B-A\subset C\), not only a centroid relation. This gives valid all-halfspace pair payments and permits summation only when the fibers are distinct.

The polytope extension uses the correct products \(S_iM_i\), which are unchanged by rescaling a facet function and scale quadratically under affine volume change. The sharp parallelotope threshold is verified by the cube-plus-pyramid moment calculation. The comparisons against the shape-free threshold are exact. Inscribed simplex volume and full partner volume are carefully distinguished throughout.

### 583b3086fe614511: actual low-middle descent

[Proof](../facts/583b3086fe614511.md).

The all-dimension inequalities establish the strict constant interval, positive surplus, and contraction factor below one. Exact evaluations at dimensions 3, 4, 15, 23, 52, and 76 also verified the printed formulas; these evaluations supplement rather than replace the all-dimension proof.

Shrinking outer bodies preserves actual midpoint compatibility. The shrunken partner simplex leaves a uniform cap-volume reserve, which pays the entire strict-hit subset whenever that subset is not already covered by the outer cap. This argument works for arbitrary ambient integer tilts because the two thresholds have the required sum.

The score minimum exists by lower semicontinuity on the sphere. If the original centroid fails, the retained body has less than twice each missed source's volume. The centroid-containment lemma therefore puts its centroid strictly inside every missed source simultaneously. The resulting strict hitting credit and ordinary retained-body depth give the target. The pure integer case is handled separately by entire-fiber contributions.

The reference \(M\) is an inscribed-partner lower bound; the fact does not silently replace it by the largest core volume or the average mass.

### c232c07c1cce4b3a: capacity-deficit range extension

[Proof](../facts/c232c07c1cce4b3a.md).

The retained maximum-simplex ratio is upper semicontinuous, so its superlevel set used in the compact minimization is closed. The cap deficit is continuous. The equality-cap obstruction therefore yields an attained strictly positive gap on the required compact set; the empty-set case is handled explicitly.

The appendix's simplex chord/projection identity is valid even when some barycentric directional derivatives vanish. The maximum chord length is the reciprocal of the sum of positive derivatives, and the projected entering facets partition the projection up to a null set. The shear-and-cylinder argument then proves the pyramid-frustum capacity bound.

The improved own-cap estimate is used only in directions that actually miss a positive-weight source. The proof establishes that such a source exists in the descent branch before invoking that estimate. The strict retained-volume inequality, interior hitting, and final score algebra are valid. The dimension-3 identities \(c=69/256\), \(v_{\rm cap}=32/69\), and target surplus \(3/512\) were checked exactly.

The parameter is nonexplicit but well-defined and positive. The theorem remains a finite weighted source-hitting theorem with an admissible range below \(1/2\).

### 0d089d25e72f4e35: three-tier parity-core repair

[Proof](../facts/0d089d25e72f4e35.md).

This proof was checked conditional on the separately reviewed ordinary rigidity and one-sided local-star facts named in its dependencies. Its compact inscription lemma uses genuine continuity of maximal inscribed simplex volume and ordinary maximal depth. Failure of the desired mixed target gives the strict ordinary depth bounds needed to invoke it.

The routing map uses parity to produce an integer midpoint. Small outside parity loads force every edge with a high partner to land in the core. At a fixed target the partners are distinct, so local star credits have no double counting. The two discarded edge sets are disjoint.

Under the failure assumption \(b_{\rm avg}>V\), every target deficit is positive and their sum is exactly the outside mass \(E\). High targets use the local-star deficit factor. Low targets retain the inscription loss through \(M_0=(1-\eta)(1-\zeta)V\), and the low-middle theorem's strict surplus pays that loss explicitly. The comparison against the global target has a positive margin. The final strict sum is valid even when the low tier is empty because the high tier contains a largest core.

The intermediate-tier incoming-load hypothesis remains essential and explicit. The proof does not claim that it follows automatically from convexity or that every parity class has a positive fiber.

## 5. Remaining review boundaries

The auxiliary exact-identity calculation exited 0 without stderr. It independently recalculated the advertised rational identities in the first three auxiliary facts and the stated constant comparisons in the moment/descent facts.

No tracked theorem or source certificate was changed by this reviewer. The additions are this report, the portable independent verifier, and its sanitized exact JSON output. General repository validation, the remaining PR #4 facts, and Lean proof/axiom scope are covered by the other reviewers. This report makes no separate PDF-presentation claim.

The important mathematical boundaries to preserve in merge descriptions are:

- The counterexamples concern the sharp and \(1/e\) targets; the unspecified smaller-positive-constant problem is not resolved here.
- The full analytic proofs are stronger evidence than the scalar checkers alone. The checkers by themselves do not establish the actual integer support, origin fiber, or all-point ambient-halfspace argument.
- Finite generator checks are exact but do not enumerate the enormous lifted bodies.
- The auxiliary sufficient theorems retain their shape, load, parity-core, or volume-range hypotheses.
- Prior review records were inspected only as reproducible material. The mathematical reasoning, source-certificate replay, independent interval computation, and final portable run described above were performed afresh.
