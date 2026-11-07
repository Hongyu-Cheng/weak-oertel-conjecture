# Lean formalizations and seven supplementary capacity facts

Review date: 2026-11-07 (UTC).

Review method: a separate AI reviewer audited the theorem semantics and mathematical proofs, performed the fresh Lean build, and ran the exact computations described below. This is not a human-review claim.

## Verdict and scope

The Lean formalizations introduced by PRs #5 and #7 pass this independent source-semantics review, fresh project compilation, and transitive-axiom audit. The seven PR4 mathematical facts listed below also pass review of their complete statements and proofs. One concrete defect was found in the supporting exact-arithmetic checker for fact `c8fa242cfc3e441b`: pure-root coordinates were inadvertently floats. The integration correction restores rational arithmetic, adds type checks, and regenerates the affected report. An independent Fraction-only calculation confirms every entry of the original integer certificate, so the mathematical fact and its proof require no change.

This report covers those formalizations and those seven facts. The other PR4 facts, the PR6 construction, PR8's improved construction, repository-wide integrity, CI, and merge sequencing belong to the coordinated reviews recorded elsewhere. In particular, the unchanged Lean tree does not formalize PR8's new n=52 construction.

The complete sanitized execution evidence, all 27 axiom results, module list, source digests, independent replay program, and its exact output are in [pr4-8-lean-evidence.json](pr4-8-lean-evidence.json).

## 1. Exact sources and reproducibility

The fresh Lean run used commit `2ffd469d639402e465de448fb31dd920eaf7f40a`, the reviewed PR8 head. Its `lean` tree is `b8fa4bdd1df9cc5ba37932db08b23c9939fe05b2`, identical to PR7 head `9c8a32f22558087a07335e76e08f7066e8b36dc6`.

PR5 head is `00c762ccda2baf1b71fbfef0248921ce45c1085d`, with Lean tree `11e5d9e0e8d62f9d26a7d6fadb689161fc2c3604`. Comparing its existing Lean files to the reviewed head shows changes only to `CheckAxioms.lean`, `README.md`, and the root import file `SharpOC.lean`; the theorem modules, toolchain, package configuration, and dependency lockfile are unchanged. The fresh run therefore checks PR5's original theorem sources in the later superset. It was not a separate fresh build of the historical PR5 checkout.

All seven audited candidate JSON files and their corresponding fact Markdown files are byte-identical to PR4 head `e5bbd45e3cb073e1c030bcc9e07726881d2af8f0`. Each fact contains the complete audited candidate statement and proof. Their SHA-256 digests are recorded in the evidence file.

The pinned and observed environment is:

| Component | Value |
|---|---|
| Toolchain file | `leanprover/lean4:v4.34.1` |
| Actual compiler | Lean 4.34.1, Release, arm64-apple-darwin24.6.0 |
| Compiler commit | `5045d0056413266e57c625dcd7c365b10e377c52` |
| Lake | `5.0.0-src+5045d00` |
| Required and actual mathlib commit | `d13f23b723b8a846827a245b89c10fc7d3f11612` |

From the reviewed checkout's `lean` directory, the fresh execution was:

    git rev-parse HEAD
    lake clean sharpOC
    lake build
    lake env lean CheckAxioms.lean

| Command | Exit | Measured time |
|---|---:|---:|
| `git rev-parse HEAD` | 0 | 0.022 s |
| `lake clean sharpOC` | 0 | 4.821 s |
| `lake build` | 0 | 84.751 s |
| `lake env lean CheckAxioms.lean` | 0 | 6.539 s |

The combined run started at 15:21:45 UTC and finished at 15:23:22 UTC. Its retained logs are complete, with zero stderr bytes and no withheld output.

The package-specific clean removed the project's generated build outputs while retaining pinned dependency caches. The subsequent log reports fresh `Built` results for all 27 `SharpOC/` modules and the root `SharpOC` module, covering every tracked project module. Lake's total of 8,952 jobs includes dependencies; it is not a claim that all mathlib dependencies were freshly compiled. The remaining warnings are linter or deprecation warnings.

An earlier successful build was incremental and used cached targets. It is distinguished from, and is not the basis for, the fresh compilation result above.

## 2. What the Lean theorems actually prove

The review checked the final theorem types together with their definitions, the integer-fiber census, measure reduction, mass finiteness, normalization, cut construction, and concrete scalar certificates. It did not infer correctness merely from theorem names or a successful scalar calculation.

### 2.1 Sharp constant

[Counterexample.lean](../lean/SharpOC/Counterexample.lean) proves `SharpOC.Counterexample.sharp_oc_counterexample`. The concrete dimensions are d=23 and n=3*10^92. The theorem supplies a compact convex body with nonempty ambient interior, an interior point of every nonempty continuous fiber, and actual positive finite mixed-integer mass.

One positive real number r is chosen before the universal quantifiers over query points, with

    r < ((23/24)^23) / 2^n.

For every integer vector z and every continuous x for which (z,x) belongs to the body, there is a nonzero continuous linear functional F and a threshold t with t <= F(z,x). Thus the proper closed halfspace {F >= t} contains that particular query point. Its actual mixed-integer mass divided by the actual mass of the body is at most the same r. This is the uniform depth obstruction needed for the sharp constant.

### 2.2 Fixed 1/e constant

[BoxMeasure.lean](../lean/SharpOC/BoxMeasure.lean) proves `SharpOC.BoxCounterexample.one_over_e_counterexample`, with n=76 and continuous dimension `1372131 + 2^93`. It has the same essential body, fiber, finiteness, uniformity, and proper-halfspace properties, with

    r < 1 / (exp(1) * 2^76).

The padding argument uses the actual product measure. It does not replace the fiber volumes with freely chosen abstract weights.

### 2.3 Actual measure and quantifiers

[MixedIntegerMeasure.lean](../lean/SharpOC/MixedIntegerMeasure.lean) and the corresponding definitions in [BoxMeasure.lean](../lean/SharpOC/BoxMeasure.lean) define the mass as the countable sum, over all integer vectors, of the Lebesgue volume of the associated continuous fiber. The passage to a finite sum follows from the proved exact integer-fiber census. Positive mass and finiteness are established before real-valued normalization; the conclusion cannot result from taking `toReal` of an infinite denominator.

The halfspace witness is proper because F is explicitly nonzero. The final bound covers every actual mixed-integer point in the body, not just selected fiber centers or a finite sample. The conclusions have no hypothesis assuming the desired counterexample inequality.

These results refute the displayed sharp and fixed 1/e constants. They do not refute the existence of some unspecified positive absolute constant c0 in a weaker assertion. The final Lean theorem types also do not separately assert rational vertices or rational polyhedrality. Their use of a fixed canonical Lebesgue normalization is harmless for the depth ratios, since a common multiplicative normalization cancels.

## 3. Trusted axioms and coverage

[CheckAxioms.lean](../lean/CheckAxioms.lean) imports the root module, collects each named theorem's transitive axioms, and fails if an axiom is outside the allowlist

    propext
    Classical.choice
    Quot.sound

The fresh run checks 27 statements: 13 in the sharp construction and 14 in the 1/e construction. Every result is exactly that three-axiom list. The checks include both final counterexample theorems, body convexity and compactness infrastructure, exact fibers, actual mass/cut identities, full-dimensional padded fibers, the product-simplex cut argument, and the scalar depth bound.

The full theorem-by-theorem list is in the evidence JSON. No `sorryAx`, custom axiom, or native-decision oracle occurs in these dependency sets. A source scan of the project found no actual `sorry`, `admit`, `axiom`, or `native_decide` use; the textual matches were comments. The audit trusts the stated Lean kernel and pinned mathlib environment in the usual way.

## 4. Review of the seven PR4 facts

These are analytic proof reviews, with an additional finite exact-arithmetic replay for the specific matrix certificate. They are not newly formalized Lean proofs.

| Fact | Reviewed conclusion | Result |
|---|---|---|
| [2d4e949d29014223](../facts/2d4e949d29014223.md) | Absorption-sensitive retained-cone capacity, exact determinant defects, sharpness and strictness | Pass |
| [c8fa242cfc3e441b](../facts/c8fa242cfc3e441b.md) | Complete one-root vertex description and distinct-vertex capacity certificate | Pass; supporting checker corrected |
| [e96fd7e3557042b0](../facts/e96fd7e3557042b0.md) | Escape/cap-excess inequalities and explicit repeated-incidence accounting | Pass |
| [e9f4abbc5f9a4527](../facts/e9f4abbc5f9a4527.md) | Whole-cone quadratic inequality and shifted-ball capacity improvement | Pass |
| [ec5c31b8951c4417](../facts/ec5c31b8951c4417.md) | Canonical logarithmic budgets and a simultaneous canonical-direction center | Pass |
| [784cde0d72dd4319](../facts/784cde0d72dd4319.md) | Quantified nearby-orientation fan bound and simultaneous neighborhood center | Pass |
| [e8b040625fe84794](../facts/e8b040625fe84794.md) | Fixed normal neighborhood at small deficit, with explicit localization | Pass |

### 4.1 Absorption capacity: 2d4e949d29014223

For a nonnegative row-stochastic H, the proposed sum-preserving transform has determinant equal to the product of 1+1/sqrt(m_j). The domination y <= Hx yields both required quadratic bounds, and the transformed root coordinates are allowed to be negative. Hadamard therefore proves the claimed determinant/volume ratio without an unproved positive-orthant assumption.

For irreducible P, the finite-path escape argument genuinely implies convergence of the Neumann inverse of I-P_JJ, and proves the row-stochastic absorption matrix. The exact defect decomposition has only nonnegative terms. The signs in both logarithmic budgets are correct.

The sharpness construction is irreducible even though some off-diagonal entries vanish. The separate strictness claim correctly assumes strict positivity: diffuse absorption handles at least two roots, while in the one-root case only the root and uniform vector can have norm-one images. For N>=3 they cannot supply N independent columns. Compact attainment converts pointwise strictness into a strict capacity maximum. The N=2 exception is explicitly excluded.

The d=2 and d=3 fan consequences use the same stochastic matrix, the exact ordinary cap product, and strict hitting. They do not promote a fixed-centroid fan result to an all-halfspace center theorem.

### 4.2 Finite vertices: c8fa242cfc3e441b

The support/active-constraint argument proves the vertex list is complete. A nonempty surviving-root support is forced by the nonnegative inverse. At a vertex there can be only one surviving root, and every positive missed coordinate must have its inequality active; otherwise a two-sided perturbation exists within the coordinate face. Strictly positive off-diagonal entries ensure inactive missed rows are strict and all listed supports are distinct.

The rational transform with arbitrary allowed t_j satisfies the same norm estimate. Maximizing the absolute determinant separately in each column permits a maximizer at polytope vertices; nonzero volume forces distinct columns. Thus using the N largest distinct vertex norm-squares is justified.

For the displayed 6-by-6 matrix, an independent exact replay checks all 15 two-root cones, all 480 vertices, the original cone constraints and active equalities, distinctness, every table entry, and the squared bound below 1/1600. The strict capacity 1/40 is below the required relative source volume 1/32, which correctly implies at least three strict hits. The score surplus 763/7776 times E is consistent with Gamma_5=3125/7776.

The arithmetic implementation issue and its correction are detailed in Section 5.

### 4.3 Escape and overlap accounting: e96fd7e3557042b0

The one-root support condition gives X >= 1/(m+1) and 0 < u_j <= 1-e_j. The existing nonnegative defect terms then yield the stated escape lower bound. Grouped AM-GM and the logarithm inequalities give e_j >= (m+1) log_+(Gamma_m/p_j), including the separately treated m=d case.

The active-vertex resolvent identity follows by subtracting the two linear systems. The maximum-ratio estimate retains the necessary positive-denominator condition. The cap-excess tradeoff and Jensen consequence have the correct inequality directions.

In the family argument, replacing an admissible source by a capacity-maximizing simplex is used only to obtain a necessary inequality. It does not replace the actual source's hit set or score. Every repeated row incidence remains in L_j and R_*, and the final budget does not silently discard the overlap cost. The stated dependencies on the preceding capacity and vertex lemmas are applicable.

### 4.4 Shifted-ball bound: e9f4abbc5f9a4527

The escape inequality at each one-root vertex, together with Gamma_a >= Gamma_k for a <= k, proves the strengthened quadratic inequality on all vertices. Convexity extends it to the entire retained polytope. This supplies the claimed improvement without summing potentially overlapping source charges.

The hyperplane-ball determinant estimate is proved directly by orthogonal row/column changes followed by the eigenvalue AM-GM bound. The rank-one update has determinant 2^k(1+B_*), so the common positive factor cancels correctly. Nonempty relative interior of the cone, and invertibility of the map, prove strict positivity of the displayed bracket for every allowed offset.

The minimizing quadratic has positive-definite Hessian because k<N. Its threshold equation is strictly increasing, and the capped-coordinate first-order conditions give the unique minimizer. No conclusion about arbitrary fan scores is inferred from this capacity bound.

### 4.5 Canonical logarithmic budgets: ec5c31b8951c4417

Both determinant budgets follow from the actual barycentric source matrix. For the stronger budget, an actual hit row exists and is the row replaced by the all-ones row; no missed logarithmic term is lost. Nonnegative source weights and the existence of a positive-weight source justify the use of the nonnegative A_2 bound before dividing by Jensen's lower bound on the total logarithmic weight.

The Chebyshev/Jensen cap estimate, d=1 case, d=2 two-hit improvement, zero-weight case, and boundary score of one are all consistent with strict hitting. The simultaneous canonical center construction handles a jump at support value one: a_j=1 is explicitly allowed, the value at a_j is at most the target, and rescaling by A=sum a_j>1 evaluates strictly below every relevant threshold.

The derivation is self-contained; no unaccepted reference is needed to supply a missing step. The conclusion covers the positive canonical orientations only.

### 4.6 Nearby-orientation center: 784cde0d72dd4319

The inverted-simplex volume bound prevents a source from missing all perturbed caps. The source determinant bound supplies the claimed missed logarithmic budget. The face-neighborhood case strictly hits all sources and handles boundary points. The interior estimate keeps the orientation error and its constants in the correct direction.

The quantile function's finite max/min formula is valid with strict support indicators, including jumps and the endpoint cap quantile. Its continuity follows from ordinary cap continuity and strict monotonicity for nonconstant affine forms. Thus the continuous minimax problem has an attained minimum, independently of whether a discontinuous full strict-hitting depth attains its supremum.

The active-gradient certificate includes the outward normal cone at a boundary minimizer. Testing it in the direction of the missing-face barycenter excludes that case; at an interior minimizer, the missing-label argument supplies every canonical label. This validates the simultaneous conclusion for the entire compact neighborhood rather than just a finite selection. It does not extend to arbitrary orientations.

### 4.7 Fixed neighborhood: e8b040625fe84794

The proof first bounds and localizes every minimizer without assuming the desired negative minimax value. Its threshold-lowering estimate remains in a single-vertex cap region. The canonical threshold estimate then gives the stated coordinate bounds and strict interiority.

The asymmetric bounds on coordinate deviations give the sharper variance estimate 36 N E^2/(d Gamma^2). The appendix's exact cap formula and logarithmic Taylor estimate imply a quadratic loss at most d^2 times that variance. The prescribed E_d makes this loss at most E*kappa/4; the prescribed normal radius makes the logarithmic perturbation loss at most another E*kappa/4. This leaves a strict gap over the chosen target for an active cap, completing the minimax contradiction.

The dependence on the preceding quantile/minimax lemma is valid, and the needed quadratic estimate is included in full. The radius is independent of E under the stated small-deficit condition. The result remains restricted to the prescribed positive-orientation neighborhood.

## 5. Exact-arithmetic defect, repair, and validation

The original `vertices_and_bound` routine assigned

    lam[r] = 1 / denominator

When the active subset A is empty, `sum(h)` is the integer zero and `denominator` is the integer one. Python therefore returned the float 1.0. Pure-root squared norms were floats, and their presence at the front of the product converted the final squared bound to floating point. The generated report consequently labeled a decimal approximation as `exact_capacity_upper_squared`.

The original mathematical conclusion was nevertheless supported by a separate coarse certificate: the determinant lower bound and all four nonroot norm upper bounds were rational, and the script checked the strictly positive integer gap

    10^6 * a^2 - 1600 * product(q_3, q_4, q_5, q_6).

The correction changes the division to `Q(1) / denominator` and adds Fraction-type assertions for coordinates, squared norms, and the final squared bound. The regenerated report changes only the two pure-root norm strings from 1.0 to 1 and the final bound strings from decimals to exact fractions, in each of the 15 rows. Inputs, rational transforms, vertex choices, nonroot norms, and all integer table entries are unchanged.

The independent Fraction-only replay was assembled separately from the checker and reused only its inspected exact Gaussian-elimination helper. It exited 0, with all 480 vertices and all 15 table rows verified. The minimum integer comparison gap is 23,486,702,771,200. The complete replay program and rational results are preserved in the evidence JSON.

The corrected repository command also exited 0:

    python3 -B assets/pk-continuation-2026-11/check_actual_sign_cone_vertex_bounds.py --report assets/pk-continuation-2026-11/audit-actual-sign-cone-vertex-bounds.json

It reports `PASS_ACTUAL_SIMPLEX_CAPACITY_UPPER_BOUNDS`, 15 cones, 480 vertices, and strict relative capacity below 1/40. A structural comparison confirms that only the two intended report fields changed. A search of asset JSON files finds no reference to either changed filename and no manifest hash entry requiring an update.

No fact, candidate, verification, or state file was modified for this correction. No further mathematical blocker was identified in this review scope.
