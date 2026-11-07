# Independent review of the triangular parity-core theorem and sharp counterexample

Date: 2026-11-07

Review method: a separate AI reviewer audited the proofs, checked the cited external premises, and ran the exact computations described below. This is not a human-review claim.

Reviewed PR: [#4](https://github.com/Hongyu-Cheng/weak-oertel-conjecture/pull/4)

Pinned PR head: `e5bbd45e3cb073e1c030bcc9e07726881d2af8f0`

Pinned PR base: `b4713c6831e6f1d7c0271d6cbdabfe1eed22b6f0`

## Verdict and scope

**No blocking mathematical defect was found in the 11 new accepted facts listed below. I recommend merging this part of PR #4, subject to the separate repository integration checks. No source-proof correction is required by this review.**

This is a fresh review of the statements and actual proof text. It does not rely on the old verifier PASS records. All 11 statements below were read in full and their arguments checked. The review also checked the baseline metronoid lemma in full and the ordinary sector inequality actually used from the baseline three-slice theorem. It does not claim a fresh audit of the full three-slice theorem or of all 37 new PR #4 facts.

| New fact | Main claim | Review coverage |
| --- | --- | --- |
| [a4ad1f5074d149c4](../facts/a4ad1f5074d149c4.md) | Complete triangular parity cores under a small outside load per parity class | Full proof, constants, retained-edge accounting, high/low target split |
| [c77c6c94c4f34008](../facts/c77c6c94c4f34008.md) | One-sided local-star improvement near the ordinary simplex minimum | Full compactness proof, determinant estimate, fixed source credits, center displacement, all directions |
| [ea91e021ff1f4416](../facts/ea91e021ff1f4416.md) | Ordinary simplex rigidity and a normalized stability gap | Full proof and equality-case premise |
| [20a50fadbdf54b5a](../facts/20a50fadbdf54b5a.md) | Actual triangular middle-fiber transfer at every volume ratio | Full continuum limit, endpoint payment, and ambient halfspace argument |
| [cba04fbe065c480a](../facts/cba04fbe065c480a.md) | One center controlling all strict source-hit directions | Full sign classification, degenerate-fan extension, continuous quantiles, minimax argument |
| [dc15f4248ddf4742](../facts/dc15f4248ddf4742.md) | All-one-positive-vertex planar fans | Full capacity and own-cap estimates |
| [41c932533ed549c7](../facts/41c932533ed549c7.md) | All-two-positive-vertex planar fans | Full singleton geometry and covering-pair selection |
| [d20149eea01b4245](../facts/d20149eea01b4245.md) | Repeated-apex mixed fans and their reversals | Full lobe and scalar estimates |
| [58879ca8313c4b41](../facts/58879ca8313c4b41.md) | Distinct-apex (1,1,2) fans | Full case split, source capacities, and inherited ordinary-sector premise |
| [d2ae261ff7d54656](../facts/d2ae261ff7d54656.md) | Distinct-apex (1,2,2) fans | Full case split and scalar estimates |
| [022a26fa5001480a](../facts/022a26fa5001480a.md) | Direct rational counterexample to the sharp dimension-dependent bound | Full construction, exact fiber census, all-point separating cuts, normalization |

The triangular theorem's relevant dependency closure is accounted for: the new local-star/rigidity branch, the five fan leaves, the all-direction source-center theorem, the actual transfer theorem, and the two already accepted inputs discussed below. No pending candidate is needed for this chain.

## 1. Complete triangular parity cores

Location: `facts/a4ad1f5074d149c4.md`, Sections 1–5.

The proof correctly distinguishes the small partner band from the wider high-target band. That distinction is essential: the low-target estimate needs a positive separation between the minimum retained partner area and the area of a low target.

I checked the constants with \(\Gamma=4/9\), local-star coefficient \(A=5/9\), and
\[
\eta_H=\rho/8,\qquad \eta_P=\eta_H/34,\qquad
\epsilon=\min\{\eta_P/72,\eta_H^2/46656\}.
\]

Under hypothetical failure, the largest core triangle's centroid gives \(E>\Delta\), hence \(V<b_{\rm avg}\le(1+\epsilon)V\). In particular every deficit \(d_w=b_{\rm avg}-V_w\) is positive and their sum is exactly \(E\).

For an outside fiber, the midpoint with its unique core parity representative is an integer base. If the partner is retained, its half translate forces the midpoint area to be at least \(M/4\), where \(M=(1-\eta_P)V\). Since an outside target would have area at most \(\epsilon V<M/4\), this target is in the core. At a fixed target the partners are distinct: the partner is determined by reflection of the outside base. Outside fibers, core partners, and the middle fiber therefore do not cause double counting in the star estimate.

The bad-partner discard satisfies \(D_{\rm bad}\le\Delta/72\). Thus retained mass is strictly greater than \(71E/72\).

For a high target, shrinking the incoming pieces to total area \((4/5)d_w\) preserves inclusion and invokes the one-sided local-star theorem. Its conclusion reaches exactly \(\Gamma b_{\rm avg}\). The partner depth and area hypotheses and the small total incoming-area requirement hold with the stated constants.

For a low target, \(D=M-V_w\ge(\eta_H-\eta_P)V\ge\eta_H V/2\). The outside-piece bound satisfies the actual-transfer requirement
\[
|A_i|\le\epsilon V\le\frac{D^2}{11664M}.
\]
An incoming load at least \(17D/18\) gives raw depth at least \(\Gamma M+D/36\). This exceeds the target because \(\eta_P=\eta_H/34\) leaves a surplus \(\eta_H V/72\) above \(\Gamma V\), larger than \(\Gamma\epsilon V\).

Consequently failure forces incoming load less than \((17/18)d_w\) at every target. Summing gives retained mass less than \(17E/18=68E/72\), contradicting the strictly larger \(71E/72\) lower bound. The proof handles zero-area outside fibers and the pure integer-normal halfspaces as stated. It establishes the theorem under its triangular-core hypothesis; it does not prove such cores exist for arbitrary bodies.

The formula for \(\epsilon\) is explicit in a valid local-star constant \(\rho\). The local-star argument establishes existence of \(\rho\) by compactness; this chain does not provide a numerical value for it.

## 2. Local-star improvement and ordinary rigidity

### Ordinary simplex rigidity

Location: `facts/ea91e021ff1f4416.md`, Sections 2–6.

I checked the step from equality in the maximal ordinary depth to a simplex, rather than merely a pyramid. At the centroid, the equality normals must have zero in their convex hull: otherwise a separating displacement increases all active cap volumes and preserves the positive gap away from them. The uniform section bounds used here are valid because the centroid is interior and the body is compact.

A minimal positive dependence uses at most \(d+1\) equality directions. Grünbaum equality gives a pyramid for each direction. Distinct directions have distinct apexes, and every other extreme point is in the corresponding base. The resulting affine heights satisfy \(\lambda_i(v_j)=\delta_{ij}\). Balancing the gradients makes their positive weighted sum constant; evaluating at the apexes shows that all weights are equal. Taking centroid averages then forces exactly \(d+1\) apexes. These are affinely independent and their simplex equals the body.

The normalized stability conclusion follows from genuine compactness and continuity. With a common inner ball and bounded outer ball, the convex-body family has no degenerate limit. Hausdorff convergence gives convergence in volume of symmetric differences and hence convergence of normalized halfspace depth, uniformly over halfspaces. Distance from the compact family of simplices is continuous. A positive gap away from simplices follows.

The equality premise was checked in the cited primary research text, Luca Tanganelli Castrillón, [An improved stability result for Grünbaum's inequality](https://arxiv.org/html/2410.12072v2), Introduction, immediately after (1.1). It states the cone equality characterization with the cutting hyperplane parallel to the base. For \(d\ge2\), the cap attaining the smaller Grünbaum value is the apex side, as the elementary cone-volume calculation shows.

### One-sided local star

Location: `facts/c77c6c94c4f34008.md`, Sections 2–6.

I checked the compactness argument with families of arbitrarily many reflected pairs. Hypothetical failure and small total incoming mass force the middle body's ordinary depth to approach the simplex minimum. Normalization by a maximal inscribed simplex gives a common compact region, and the rigidity lemma forces the limit to be that simplex.

The partner-to-middle inclusions give uniform bounds after translating each reflected pair. The partner volume lower bound and depth upper bound imply uniformly large inscribed partner simplices. This conclusion is uniform over the varying partner index: a contrary sequence of partners has a compact subsequential limit, to which the rigidity result applies.

The stochastic-matrix determinant estimate is consistent with the claimed exponent. After replacing one row by the row of ones and centering the others, Hadamard gives
\[
|\det P|\le N^{N/2}2^{-d}r_J^{N-J+1}.
\]
There are exactly \(N-J+1\) remaining row maxima bounded by the \(J\)-th largest maximum. The resulting margin is positive because \(N<2(N-J+1)\).

The credits assigned to the \(J\) sufficiently exposed canonical directions are fixed before choosing the final halfspace. The partner-cap payment estimate is uniform in the arbitrary offset on each reflected pair. The small tilt, small center shift, and incoming-to-partner-volume ratio leave a positive support margin.

Finally, the center displacement cancels the differences between directional credits. The coarea estimate applies uniformly in small neighborhoods of the canonical simplex normals, where the limiting sections are interior and nondegenerate. All other directions have a uniform positive ordinary-cap gap in the simplex limit. This covers every nonconstant continuous linear functional and every choice of reflected-pair offsets at one point. The proof is not restricted to a finite fan.

## 3. From strict source hits to actual endpoint mass

### All-direction source center

Location: `facts/cba04fbe065c480a.md`, Sections 2–6.

The strict sign patterns are exhaustive: (1,1,1), (2,2,2), repeated and distinct apex cases of (1,1,2), and the corresponding repeated and distinct cases of (1,2,2). The proof invokes the correct orientation of the repeated-apex lemma.

The extension to zero original vertex values and boundary centers treats discontinuity in the right direction. Shrinking a full-dimensional source toward its own centroid turns every old support miss into a strict miss. Simultaneously replacing \(V\) by \((1-\delta)^2V\) and rescaling the credits preserves the hypotheses. An assumed strict counterexample persists under this small normalization change. Further perturbation of the center and a positively balanced fan cannot introduce a hit on any old missed source. Thus the strict fan bounds extend to these boundary configurations.

The directional threshold argument does not incorrectly assume continuity of the source indicators. The cap-plus-credit function is nonincreasing and right continuous. Its threshold admits a finite maximum/minimum formula over source subsets using ordinary cap quantiles and source support functions. This formula proves that the threshold itself is continuous.

The minimax problem therefore has an attained solution. If its optimum were nonnegative, the active directions together with the outward normal cone of the triangle would contain a minimal positive circuit of two or three normals. An opposite pair has combined score at least one. A three-normal circuit is controlled by the extended fan theorem. Both contradict the strict slack obtained from \(\eta<1/18\). The minimizer is interior and controls all directions. The case \(V=b\) correctly reduces to the ordinary centroid bound.

### Actual triangular transfer

Location: `facts/20a50fadbdf54b5a.md`, Sections 2–6.

The continuum passage is made after integrating over the small incoming bodies. Uniform strip-area control gives uniform quadrature error over all directions and thresholds. The resulting integrated score is jointly continuous; compactness permits the limiting coefficient \(1/18\). This does not pass a limit through the discontinuous finite strict-hit indicator without justification.

With \(V=M-\xi D\), the partners' inscribed triangles are shrunk by a common factor to support the source model. The shrinkage distance is at least \(\xi D/(2M)\). If a source credit is not paid by the incoming endpoint cap, the reflected threshold forces a cap of the partner triangle. The centroid-to-support distance of a triangle is at least one third of its width, so that cap has area at least
\[
\frac{\xi^2D^2}{36M},
\]
which pays the entire incoming piece under the hypothesis. All inequalities remain valid with equality in the permitted incoming area. Distinct endpoint bases prevent double counting.

For pure integer normals the middle fiber and at least one endpoint of each reflected pair are retained; their mass is larger than the asserted target. Thus the proof covers all closed ambient halfspaces, including those with zero continuous component.

## 4. The five planar fan leaves

All five proofs use closed missed-source regions, so a source with support maximum zero is correctly treated as a miss. The necessary exclusions are strict capacity bounds below one quarter of the original triangle's area. The actual source threshold is at least this large.

| Fact and proof location | Details checked |
| --- | --- |
| `dc15f4248ddf4742`, Sections 2–3 | The missed region for the maximal-coordinate singleton is the stated quadrilateral. Its four vertex-triangle capacities are strictly below one quarter. The complementary own caps sum to at least eight ninths, using separate maximal-coordinate ranges below and above one half. |
| `41c932533ed549c7`, Sections 2–5 | The singleton region is the exact triangle determined by the two complementary corner caps. Two potentially qualifying singleton indices force the third barycentric coordinate to be the smallest. If the smallest coordinate qualifies, it is unique. The selected pair then has own-cap sum strictly greater than one, including the monotonicity calculation for \(h t^2/(t-L)\). |
| `d20149eea01b4245`, Sections 1–3 | The smaller same-apex lobe has the stated exact expression and upper bound \(3-2\sqrt2<1/4\). Concurrent corner-cap area is strictly convex in its edge intercept. The bound \(\min(p_1,p_2)-p_0<1/9\) includes both coordinate orders and the endpoint cases. The lobe-containment step for a minimum-area outer cap follows from concurrency and the monotonic other intercept. Both fan orientations receive the correct covering pair. |
| `58879ca8313c4b41`, Sections 2–5 | Positive balance forces the intercept ordering. The missed-region capacity test and the maximal-coordinate case split are correct. In the matched-maximum case, the two troublesome singleton regions cannot both qualify because their product is strictly below \(1/16\). The branch estimates \(p_0-p_1<1/18\), including the two rational endpoint bounds, have positive denominators on their stated domains. |
| `d2ae261ff7d54656`, Sections 2–4 | The three missed-pair regions and exact quadrilateral capacity \(Z\max(D,a)\) are correct. The cap-order and coordinate-order branches are exhaustive. The remaining branch \(b>c>a\) correctly switches pairs when the first missed region has capacity at least one quarter. The one-variable maxima used in the final bounds give the stated \(3/32<1/9\) and \(1/8<1/4\) bounds. |

The only non-elementary input in these leaves is the ordinary sector inequality in the (1,1,2) proof. The baseline fact [2a8c2bc6d7992c5e](../facts/2a8c2bc6d7992c5e.md) explicitly includes this auxiliary assertion. I checked the application and the primary publisher PDF of George Tsintsifas, [Two inequalities for planar convex sets](https://doi.org/10.4153/CMB-1985-005-5), Canadian Mathematical Bulletin 28(1) (1985), 60–66.

The original PDF's printed pages 60 and 61 were inspected as page images. Figure 1 has alternating numerator regions paired with their opposite denominator regions. The displayed definition and Theorem 1 state \(\sum_i |X_i|/|Y_i|\ge3/2\), with a non-strict inequality. The required correspondence \(X_i=D_i\), \(Y_i=A_i\) is valid, and there is no extra centroid or angle hypothesis. Only that ordinary sector assertion is used here; no mixed-integer conclusion is imported into the fan proof.

I also checked [6769574fc1bd9f8d](../facts/6769574fc1bd9f8d.md) in full. Weak-star compactness, the top-cap support maximization, the two depth-region inclusions, and the full-mass centroid specialization are consistent. Its use of the ordinary Grünbaum inequality is standard and explicitly cited in that fact.

## 5. Direct rational sharp counterexample

Location: `facts/022a26fa5001480a.md`, Sections 1–6.

The construction has \(d=23\), \(L=10000\), \(N=L^{23}\), and \(n=3N=3\cdot10^{92}\). The very large finite dimension causes no logical problem: the proof uses formulas valid for every subset, rather than claiming to enumerate all fibers.

I checked the following geometric obligations.

1. The three source simplices have the stated barycentric vertex description. The ordered three-coordinate blocks have determinant \(1/6\), giving total relative volume \(6^{-8}\). The centroid coordinates and cyclic functional values agree with the chain description.

2. Contracting by \(103/104\) gives a strict negative margin on every unpaid row. The inequalities \(P_a+A/2\subset B\) and \(c_a+2A\subset P_a\) hold with the stated rational margins. The latter implies the required inclusions for every subset size \(k\ge2\).

3. The projection has exactly the origin, all nonzero cube vertices, and the negative coordinate bases as integer points. An integer projection with a coordinate \(-1\) must be the corresponding negative coordinate vertex. All remaining integer projections are cube vertices.

4. Nonzero cube bases and negative coordinate bases are exposed, so the specified fibers there are exact. At the origin, the integer-coordinate balance gives the exact convex weights. The verified inclusions show that every possible convex combination lies in \(B\), and the construction already includes \(B\). Hence there is no unnoticed enlargement of the origin fiber.

5. Every nonempty integer fiber is a full-dimensional simplex. The body itself is full dimensional, and its total mixed volume is exactly
   \[
   W=(2^n-1)M+4b=2^nM+(4b-M).
   \]

6. For each cyclic row, exactly \(N\) outer fibers are paid. Every nonzero cube fiber is strictly excluded: the all-unpaid and at-least-one-paid subset bounds both hold for every \(1\le k\le n\). The middle trace has area \(b/2\), so the cut has mass exactly \(3b/2<\Gamma M\). Since the cyclic functionals sum to zero, every middle-fiber point belongs to at least one such cut.

7. At any other fiber, a simplex cap of volume at most \(\Gamma\) times its fiber volume can be isolated from all other fibers using its exposed integer base and a sufficiently large finite integer-direction coefficient. This is a closed ambient halfspace with a nonzero normal and strictly excludes the other fibers.

Thus every point has a containing halfspace of mass at most \(\Gamma M\), whereas
\[
\frac{\Gamma W}{2^n}
=\Gamma M+\frac{\Gamma(4b-M)}{2^n}>\Gamma M.
\]
The argument bounds the supremum directly and does not need maximum-depth attainment.

This particular fact refutes the sharp dimension-dependent value \(2^{-n}(23/24)^{23}\). It does not itself refute the weaker fixed \(1/(e2^n)\) value, and it does not refute the repository's unspecified absolute-constant target. The later fixed-\(1/e\) constructions belong to the separate review of PRs #6–#8.

## 6. Exact computational checks performed

### Existing sharp-construction checker

The pinned version of
`assets/pk-continuation-2026-11/check_direct_rational_sharp_oc_counterexample.py`
was read and rerun from a temporary directory so it could not overwrite its tracked report.

Result: exit status 0.

```text
PASS_EXACT_DIRECT_RATIONAL_CONSTRUCTION_SCALAR_AND_SOURCE_CHECKS
Three 24-vertex sources and all 11 exact positive scalar margins passed.
```

The checker uses rational arithmetic for source determinants, contraction determinants, centroid entries, support signs, containment margins, and the displayed integer certificates. Its scope is fixed source geometry and scalar obligations. The exponentially many fiber census, exact origin fiber, all-subset exclusion and all-point cut argument were reviewed analytically above.

### Independent planar fan check

A new, independent verifier is included at
[pr4-8-planar-fan-exact-audit.py](pr4-8-planar-fan-exact-audit.py).

It directly clips the reference triangle with rational halfplanes, computes own-cap areas by the shoelace formula, and computes the maximum area of an inscribed triangle in each missed-pair polygon by enumerating all vertex triples. It tests all three row pairs. It does not reuse the proofs' selected pairs, coordinate case splits, or scalar capacity formulas.

With seed 20261107, it checked 12,000 nondegenerate randomly generated rational fans plus the symmetric sharp fan and its reversal. All computations use Python `Fraction`.

Result: exit status 0; all 12,002 fans passed.

| Strict sign class | Number checked | Pair requirement checked |
| --- | ---: | --- |
| (1,1,1) | 885 | Own-cap sum at least \(8/9\), missed capacity below \(1/4\) |
| (2,2,2) | 859 | Own-cap sum greater than 1, missed capacity below \(1/4\) |
| (1,1,2), repeated apex | 1,784 | Own-cap sum greater than 1, missed capacity below \(1/4\) |
| (1,1,2), distinct apex | 3,456 | Own-cap sum at least \(8/9\), missed capacity below \(1/4\) |
| (1,2,2), repeated apex | 1,685 | Own-cap sum greater than \(8/9\), missed capacity below \(1/4\) |
| (1,2,2), distinct apex | 3,333 | Own-cap sum greater than \(8/9\), missed capacity below \(1/4\) |

The symmetric (1,1,1) example attains the exact \(8/9\) pair sum, so the verifier also exercises the non-strict boundary of that claim. These finite checks provide independent regression evidence. The universal statements, degenerate sign cases and all-direction selection depend on the analytic proofs audited above.

Reproduce the independent check with:

```sh
python3 reviews/pr4-8-planar-fan-exact-audit.py
```

## 7. Pinned content and assurance

Proofs were read from the detached combined review tree at
`2ffd469d639402e465de448fb31dd920eaf7f40a`.
A separate `git diff --exit-code` against the pinned PR #4 head returned 0 for all 11 reviewed new fact files, both baseline fact files named above, and the sharp-construction checker. Their contents are therefore identical to the pinned PR #4 versions reviewed here.

This review found no missing premise in the stated triangular dependency chain and no incorrect use of a pending fact. The repository-wide state, candidate-to-fact normalization, record preservation, and verifier hash audit are handled by the integration review; this document does not duplicate or claim those global checks.

The findings support the repository's existing mathematical-review assurance level. Neither the finite rational fan sample nor the sharp source/scalar checker is a formal proof of the entire geometric theorem. No change to the assurance labels is recommended.
