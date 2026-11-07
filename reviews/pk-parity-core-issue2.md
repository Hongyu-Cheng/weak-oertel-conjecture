# Direct proof review: PK complete-parity-core theorem

## Verdict and scope

The six claims below are **APPROVED within their stated scope** after direct mathematical proof review by ChatGPT. The source mathematics is attributed to the PK contribution. The reviewer also edited the normalized exposition; no additional model, agent subprocess, human reviewer, or formal proof assistant was used. `LLM-verified` records this method and does not imply formal certification.

The review checked the full near-parity-core proof, its ordinary rigidity input, the determinant and actual endpoint-credit arguments, and the necessary proper-section continuity lemma. The classical single-cap equality input was checked directly in [Tanganelli Castrillon, arXiv:2410.12072v2](https://arxiv.org/html/2410.12072v2), Introduction (1.1) and the following paragraph. That input gives a cone; the stronger simplex-rigidity argument is proved in the accepted ordinary node.

There is no identified substantive gap in these normalized proofs. The result remains a restricted sharp Oertel theorem, not a resolution of the unrestricted weak conjecture. No other imported claim is approved by this review.

## Accepted nodes

| Claim | Accepted fact | Direct review |
|---|---|---|
| Ordinary depth rigidity and compact simplex normalization | [03bc771bddd39a8a](../facts/03bc771bddd39a8a.md) | [d4cfa43982975d74](../verifications/d4cfa43982975d74.json) |
| Continuity of proper section coarea densities | [d4e455a28be6cde4](../facts/d4e455a28be6cde4.md) | [df138dfb30289be3](../verifications/df138dfb30289be3.json) |
| Centered stochastic-matrix determinant margin | [724e9b2e1a3ec0bf](../facts/724e9b2e1a3ec0bf.md) | [1e5aca30b3e07e34](../verifications/1e5aca30b3e07e34.json) |
| Actual endpoint cap credit for every tilt | [67ecf7db6692fe65](../facts/67ecf7db6692fe65.md) | [acb561701b5438d2](../verifications/acb561701b5438d2.json) |
| Uniform finite-star repair near ordinary minimal depth | [287cc87c3b427501](../facts/287cc87c3b427501.md) | [dbf86066a5bd69c6](../verifications/dbf86066a5bd69c6.json) |
| Sharp Oertel bound near a complete parity core | [3fad02a5aa48ae2a](../facts/3fad02a5aa48ae2a.md) | [e3a1236c341391af](../verifications/e3a1236c341391af.json) |

The first four nodes have no pending mathematical predecessor. The star-repair node depends on precisely those four accepted nodes. The final parity-core theorem depends on ordinary rigidity/attainment and the accepted star-repair theorem. No composite pending note is silently used as an accepted premise.

## Decisive mathematical checks

The ordinary rigidity proof balances all active equality normals at a maximum-depth extremizer. The resulting pyramid heights force exactly d+1 distinct apexes. Maximum-inscribed-simplex normalization then gives a uniform compact class. This is not the invalid inference that a single equality cap implies a simplex.

The determinant margin yields enough good barycentric coordinates at every small-endpoint point. Integrating their indicators produces fixed credits without assuming a common good-coordinate set. A homothetic partner cap pays those actual credits for every real offset.

For a target group of mass $E_w$, the center displacement from the true centroid is $O(E_w/V_w)$. Proper-section density approximation is integrated only over that displacement, so the error is $O(E_w)$, not $O(E)$ and not an additive Hausdorff error. The finite-star constants are chosen independently of the number of pairs. Off-facet normals have a uniform simplex cap gap, and purely integer cuts contain the entire target fiber.

The parity midpoint of any nonempty outer fiber and its same-parity core partner must be a core base when $E<2^{-d}m$, including for null outer fibers. Partners within a target star are distinct. Failure of the target supplies all the local near-equal-volume and near-minimal-depth hypotheses without a factor of $2^n$. Averaging the resulting pointwise guarantees is legitimate and yields a strict contradiction for $E>0$; $E=0$ is handled separately.

Detailed per-node checks and resolved editorial changes appear in the six review JSON files. The changes clarify quantifiers, normal rescaling, attribution, and the constant-choice order; they do not weaken the main theorem or alter its hypothesis.

## Why the sharp conclusion is the new gain

Let $L=2^n$, $\Gamma_d=(d/(d+1))^d$, $M=\max_{w\in P_0}V_w$, and $W$ be total mass. The hypothesis already implies $W\le(L+\rho_d)M$. The largest-fiber centroid therefore gives normalized depth at least $\Gamma_d/(L+\rho_d)$. Since the proof may take $\rho_d\le1$ and $L\ge2$, this elementary estimate implies the weak bound with the absolute constant $2/(3e)<1/e$. The newly verified argument removes that loss and reaches the sharp value $\Gamma_d/L$ exactly.

Also, $W\ge Lm+E$ and $E\le\rho_dm$ imply $E/W\le\rho_d/(L+\rho_d)$. An n-independent threshold relative to the smallest core fiber is not an n-independent allowed fraction of total mass. The theorem does not derive its small-tail hypothesis for arbitrary bodies, give a numerical value of $\rho_d$, or cover d=1 by this argument.

## Registration and preservation

Six new normalized candidates, six accepted fact files, and six fresh direct-review records are registered. The existing problem, 1,235 old accepted facts, original candidate records, previous review runs, and previous subgoals are preserved. All original PK intake files retain their bytes and historical statuses. The manifest [pk-parity-core-issue2.json](pk-parity-core-issue2.json) pins source and normalized hashes.

The graph has 1,241 accepted facts, 2,514 candidates, and 1,297 review records after this registration. The 1,218 original pending records are not batch-approved: they include composite archival source notes whose extracted claims now have separate accepted nodes. This closes the specific normalization and verification work in Issue #2, not the broader research backlog.

## Finite checks and reproducibility

The two relevant source scripts were freshly rerun; exact outputs and zero exit codes are in [the finite-check record](pk-parity-core-issue2-exact-checks.json). These calculations test their stated examples and arithmetic, not arbitrary-dimensional compactness.

Run `python3 scripts/check_graph.py`, `python3 scripts/check_pk_nov6.py`, and `python3 scripts/check_pk_parity_core.py` to verify the graph, preserved intake, normalized chain, and regression checks. This review does not rely on a green hosted Actions status. Fresh local outputs are in [the integration-check record](pk-parity-core-issue2-integration-checks.json). The normalization checker normally permits unrelated future additions; `--integration-baseline` reproduces the strict one-time comparison with the imported baseline.
