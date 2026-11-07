# Integration review of PRs #4 through #8

Date: 2026-11-07 (UTC).

## Outcome and assurance

All five source PRs were reviewed at their exact heads and merged in dependency order with ordinary merge commits. Their combined tree on main is exactly the reviewed PR #8 tree. No blocking mathematical defect was found in the 39 newly accepted facts. One concrete defect in a supporting exact-arithmetic script was found and corrected in the follow-up [PR #9](https://github.com/Hongyu-Cheng/weak-oertel-conjecture/pull/9), which also records this audit.

This was an AI-assisted review by the lead assistant and three separate native AI reviewers. The lead personally read and checked twelve complete auxiliary proofs and coordinated integration; the others covered the remaining statements and formalizations. This is not human certification. Analytic proof review, exact finite computation, and Lean kernel verification are distinguished below. No pending import was batch-approved and no existing assurance label was upgraded.

The locked problem still asks for an unspecified absolute constant $c_0$ strictly between zero and $1/e$. The new counterexamples refute the proposed constant $1/e$ and the sharper dimension-dependent constant; they do not settle that weaker target.

## 1. Reviewed heads and completed source merges

The starting main revision was `b4713c6831e6f1d7c0271d6cbdabfe1eed22b6f0`.

| PR | Content | Reviewed head | Merge commit on main |
| --- | --- | --- | --- |
| [#4](https://github.com/Hongyu-Cheng/weak-oertel-conjecture/pull/4) | Parity-core continuation and sharp counterexample | `e5bbd45e3cb073e1c030bcc9e07726881d2af8f0` | `d48fab19170d4c2c2af0b740bc5a13df6e7eb2d3` |
| [#5](https://github.com/Hongyu-Cheng/weak-oertel-conjecture/pull/5) | Sharp-counterexample Lean proof | `00c762ccda2baf1b71fbfef0248921ce45c1085d` | `668999c226116c6256766c89193ccde9f3599dcc` |
| [#6](https://github.com/Hongyu-Cheng/weak-oertel-conjecture/pull/6) | Fixed-1/e counterexample with n=76 | `3497df590ae6f7b8abaad88a5abe853ab993582e` | `552ba734858315cf40af0b931b244b64f9b0a582` |
| [#7](https://github.com/Hongyu-Cheng/weak-oertel-conjecture/pull/7) | Fixed-1/e Lean proof and writeup | `9c8a32f22558087a07335e76e08f7066e8b36dc6` | `965985e520acd9f7a10b623468d723bc62c5dfb1` |
| [#8](https://github.com/Hongyu-Cheng/weak-oertel-conjecture/pull/8) | Integer-dimension reduction to n=52 | `2ffd469d639402e465de448fb31dd920eaf7f40a` | `5cc4e76e3823c6622819fa77c2a7bf4c1586dba0` |

Each PR received an explicitly AI-assisted review tied to its source SHA. For PRs #5 through #8, the base was moved to main only after its predecessor merged; the resulting file counts remained 25, 29, 21, and 14 respectively. Every merge used an expected-head SHA guard. A fresh fetch and `git diff --exit-code origin/main 2ffd469d639402e465de448fb31dd920eaf7f40a --` returned 0 after all five merges.

The review snapshot had no open issues, no unresolved review threads on these PRs, and no configured GitHub Actions workflows/check-runs. The computational results below are actual local executions, not a claim of GitHub CI passing.

## 2. Complete coverage of the 39 new accepted facts

The groups below are disjoint and cover all 37 new facts in PR #4 and the two later counterexamples. Complete fact/candidate SHA-256 digests, source PR assignments, and record-preservation comparisons are in [pr4-8-integration-evidence.json](pr4-8-integration-evidence.json).

| Detailed report | New facts covered | Principal obligations |
| --- | ---: | --- |
| [Lead proof review](pr4-8-lead-proof-review.md) | 12 | Actual endpoint payments, high-arity repair, active-cap reductions, capacity obstructions, and explicit parity-load budgets |
| [Triangle and sharp review](pr4-8-triangle-and-sharp-review.md) | 11 | Rigidity, local-star compactness, six planar sign classes, all-direction transfer, triangular parity cores, and the d=23 sharp counterexample |
| [Lean and capacity review](pr4-8-lean-and-capacity-review.md) | 7 | Absorption/determinant capacities, exact vertices, overlap accounting, and restricted-orientation center theorems; also both Lean formalizations |
| [Counterexample and descent review](pr4-8-counterexample-and-descent-review.md) | 9 | Seven PR #4 descent/moment/obstruction results plus both fixed-1/e constructions |

The reviews checked the actual proof text and applicability of dependencies rather than relying on stored verifier verdicts. Hypotheses concerning triangular cores, partner volumes, incoming loads, canonical directions, or fixed normal neighborhoods were retained. Obstructions to proposed proof mechanisms were not promoted to counterexamples to the weak target.

For the main counterexamples, the reviews checked the exact integer support, preservation of nonzero fibers under convexification, exact origin fiber, total actual fiber volume, proper closed ambient halfspaces, every mixed-integer query point, and a single uniform strict bound on the supremum of depth. Scalar calculations alone would not establish those properties.

## 3. Concrete issue found and repaired

The supporting checker [check_actual_sign_cone_vertex_bounds.py](../assets/pk-continuation-2026-11/check_actual_sign_cone_vertex_bounds.py) used:

    lam[r] = 1 / denominator

For an empty active set, the denominator is the Python integer 1, producing the float `1.0`. Pure-root squared norms and the final field named `exact_capacity_upper_squared` consequently became floats.

The fix uses `Q(1) / denominator` and asserts that coordinates, squared norms, and the final squared capacity bound are `Fraction` values. The regenerated [certificate](../assets/pk-continuation-2026-11/audit-actual-sign-cone-vertex-bounds.json) now stores exact rational strings.

An independently assembled Fraction-only replay checked all **480 vertices in 15 cones**, their feasibility, active constraints, distinctness, and strict squared-capacity comparisons with $1/1600$. All 15 original coarse rational table rows were unchanged. Their minimum integer comparison gap is **23,486,702,771,200**. Thus the supporting script's exactness claim needed correction, while the mathematical certificate and accepted fact remained valid.

Only the two pure-root norm strings and the final squared-bound strings changed in each report row. No source matrix, integer table entry, fact, candidate, verification record, or state entry was changed by the repair. No asset manifest references the two altered files. Full replay code and exact results are preserved in [pr4-8-lean-evidence.json](pr4-8-lean-evidence.json).

## 4. Fresh computations and formal verification

### Exact counterexample computations

All three original fixed-1/e source checkers were rerun and reproduced their tracked certificates as parsed JSON. The added [independent verifier](../scripts/check_one_over_e_independently.py) uses rational logarithm-series and exponential Taylor enclosures, explicit remainder bounds, and outward rounding. It does not reuse the source binary-power routines.

| Construction | Conservative relative gap below $1/(e2^n)$ | Conservative absolute gap |
| --- | ---: | ---: |
| $n=76,\ d=1372129+2^{94}$ | $>6.6074860325\cdot10^{-29}$ | $>3.2170817825\cdot10^{-52}$ |
| $n=76,\ d=1372131+2^{93}$ | $>7.6408794964\cdot10^{-29}$ | $>3.7202249250\cdot10^{-52}$ |
| $n=52,\ d=274784+2^{61}$ | $>1.4749400343\cdot10^{-19}$ | $>1.2048142829\cdot10^{-35}$ |

The rational endpoints, not decimal displays, justify strictness. These are lower bounds on the violation of the proposed target, not exact maximum-depth values. The [arithmetic evidence](pr4-8-independent-arithmetic.json) also records exact generator facet and cut-sign checks. The enormous full support is covered analytically, not by claimed enumeration.

The sharp-counterexample checker separately passed all three 24-vertex source constructions and eleven exact positive scalar margins.

The new [planar verifier](pr4-8-planar-fan-exact-audit.py) uses direct rational polygon clipping and exhaustive vertex-triangle capacities. All **12,002** sampled rational fans passed across the six strict sign classes, including the symmetric sharp equality example. This is finite regression evidence; universal and degenerate-fan conclusions rely on the reviewed analytic arguments.

### Fresh Lean build and axiom audit

The reviewed combined head used Lean **4.34.1** and mathlib **`d13f23b723b8a846827a245b89c10fc7d3f11612`**. After `lake clean sharpOC`, `lake build` freshly compiled all **28 project modules**, and `lake env lean CheckAxioms.lean` passed. Pinned dependency caches were retained; this does not claim that every mathlib module was rebuilt.

All **27 audited theorem statements** have exactly the standard transitive axioms `propext`, `Classical.choice`, and `Quot.sound`. No `sorryAx`, custom axiom, or native-decision oracle occurs in those dependency sets. Complete command outputs, module lists, and theorem-by-theorem results are in [pr4-8-lean-evidence.json](pr4-8-lean-evidence.json).

The semantic audit followed actual definitions and final theorem types: sums of Lebesgue fiber volumes, positive finite normalization, compactness and nonempty interior, full-dimensional nonempty fibers, nonzero normals, containing closed halfspaces, and one strict bound before quantification over query points.

| Result | Formal status checked here |
| --- | --- |
| Sharp constant, $d=23,\ n=3\cdot10^{92}$ | Complete mixed-integer-volume Lean theorem |
| Fixed 1/e, $n=76,\ d=1372131+2^{93}$ | Complete mixed-integer-volume Lean theorem |
| Fixed 1/e, $n=52,\ d=274784+2^{61}$ | Analytic proof and exact arithmetic; **not Lean-formalized** |

The final Lean theorem types do not separately assert rational polyhedrality. Their common Lebesgue normalization cancels in the depth ratio. Earlier theorem sources were unchanged by the later extension, so the fresh combined build also checks the earlier modules.

## 5. Repository integrity and preservation

The graph check passed with maximum dependency depth 44.

| Ledger | Before this stack | After this stack | Original records changed or removed |
| --- | ---: | ---: | ---: |
| Accepted facts | 1,241 | 1,280 | 0 |
| Candidates | 2,514 | 2,571 | 0 |
| Verification runs | 1,297 | 1,340 | 0 |
| Subgoals | 1,502 | 1,559 | 0 |

The problem file and its digest are unchanged. All original 1,217 pending-intake submissions remain pending. There are 1,236 pending candidates in the combined state; this review does not approve that backlog.

The intake checker passed for 1,217 pending submissions, 1,058 supporting files, and 654 historical comments. That establishes packaging and preservation, not mathematical approval of every import. The earlier parity-core checker passed its six-node review-chain/hash checks, 59 exact dimension cases, 5,334 reflection checks, and five averaging cases.

All intended relative Markdown links in the source stack resolve. The source diff and audit additions were checked for whitespace errors, accidental generated outputs, private absolute paths, and chat identifiers. Candidate-to-fact differences in two auxiliary records consist of deliberate preamble/statement normalization, with all hypotheses retained; the n=76 record's link normalization is also harmless. No historical accepted proof was silently rewritten.

## 6. Reproduction and remaining scope

From the repository root:

    python3 -B scripts/check_graph.py
    python3 -B scripts/check_pk_nov6.py
    python3 -B scripts/check_pk_parity_core.py
    python3 -B scripts/check_one_over_e_independently.py --output /tmp/oertel-independent-arithmetic.json
    python3 -B assets/pk-continuation-2026-11/check_actual_sign_cone_vertex_bounds.py --report /tmp/oertel-capacity-certificate.json
    python3 -B reviews/pr4-8-planar-fan-exact-audit.py

From `lean/`, with the pinned dependencies installed:

    lake clean sharpOC
    lake build
    lake env lean CheckAxioms.lean

The source PRs and follow-up correction preserve the research history and make the current claims auditable. The smaller-universal-constant target is still open, the n=52 improvement has no new Lean proof, and the pending intake is not a collection of newly verified facts.
