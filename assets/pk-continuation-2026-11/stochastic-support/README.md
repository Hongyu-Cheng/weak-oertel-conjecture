# Supporting research from the cyclic-source investigation

This portable bundle preserves four scoped mathematical notes, their exact
arithmetic checkers, and the certificate data needed by those checkers.
It is supporting material for a pending research-note submission. Inclusion
does not make any note an accepted fact or a formal proof-assistant result.

The direct rational mixed-integer counterexample is maintained separately
as candidate `022a26fa5001480a`; its proof is deliberately not duplicated
here. The finite source fan below explains its geometric origin, but its
own note stops at the source-fan statement. Neither the two scalar bridge
obstructions nor the source-fan note independently claims to resolve the
repository's weak absolute-constant target.

## Notation used across the notes

Let Delta be an (N-1)-simplex with barycentric coordinates lambda, and let
P be a nonnegative row-stochastic N-by-N matrix with zero diagonal. For a
set J of missed rows and its nonempty complement R, write

    K_J = {lambda >= 0, sum lambda = 1,
           lambda_j <= (P lambda)_j for j in J}.

The simplex capacity of K_J is the maximum volume of an inscribed
(N-1)-simplex divided by |Delta|. Put d=N-1 and
Gamma_d=(d/(d+1))^d. The own-cap fraction of row j is

    p_j = product_(l != j) (1+P_jl)^(-1).

A strict hit means that the source has a point with
lambda_j>(P lambda)_j. Contact alone is not a strict hit. Where pi occurs,
it is the positive stationary distribution of P.

Accepted contextual facts in the repository are `2d4e949d29014223`
(stochastic retained-cone capacity) and `c8fa242cfc3e441b` (the complete
one-root vertex formula). In particular the latter justifies the vertex
enumeration used by the enclosing-ellipsoid certificates. They are
references to existing facts, not duplicated submissions in this bundle.

## Contents and exact scope

| Note | What it establishes | What it does not establish |
|---|---|---|
| [Root-block occupancy identities](root-block-source-occupancy-identities.md) | Exact Schur-complement covariance identities, occupancy bounds, and five rational enclosing-ellipsoid certificates covering 864 retained-cone vertices. | A universal cap-excess or fan-score bound. |
| [Mean-cap bridge obstruction](actual-mean-cap-capacity-bridge-obstruction.md) | An actual rational retained simplex contradicting the proposed uniform-average capacity bound in dimension 5, with strict-margin contraction. | An Oertel counterexample or a failure of every possible weighted method. |
| [Stationary-cap bridge obstruction](actual-stationary-cap-capacity-bridge-obstruction.md) | An actual rational retained simplex contradicting the stated stationary-weighted bound under pi(R)<Gamma_5. | A different bound also requiring |R|/N<Gamma_5; that extra condition fails in this example. |
| [Cyclic-chain source fan](cyclic-chain-finite-source-fan.md) | Three actual 23-dimensional simplex sources with exact chain determinants, strict missed-row margins, and 24 scores equal to 3/8<Gamma_23. | The mixed-integer realization, which is proved separately by the direct-counterexample candidate. |

Two specific scalar proposals are therefore blocked by actual geometric
counterexamples, not just failures of a numerical relaxation:

    capacity(K_J) <= (mean_j p_j - |R|/N)
                     / [2^d (Gamma_d - |R|/N)],
        assuming |R|/N < Gamma_d;

    capacity(K_J) <= (sum_j pi_j p_j - pi(R))
                     / [2^d (Gamma_d - pi(R))],
        assuming pi(R) < Gamma_d.

The covariance identities and the five finite ellipsoid certificates remain
valid independently of those false proposals. No replacement scalar
inequality or global weighting rule is asserted here.

## Reproducing the exact checks

Only Python's standard library is required. From this directory run:

```sh
python3 -B check_stress_cone_ellipsoids.py
python3 -B check_mean_cap_bridge_obstruction.py
python3 -B check_stationary_cap_bridge_obstruction.py
python3 -B check_cyclic_chain_source_fan.py
```

All four also work when invoked by their path from another working
directory. The ellipsoid checker loads the adjacent
`stress-cone-rational-ellipsoids.json`; its optional positional argument
allows a different certificate file. The other three generate their exact
examples directly and print JSON reports. Two checkers import the adjacent
`exact_linear_algebra.py` helper, extracted unchanged from the earlier
Gaussian-elimination routine. No unpublished search array, external
package, machine-specific path, or network request is needed.

The four included `audit-*.json` files are reproducible arithmetic outputs,
not approving repository-verifier records. The notes contain the proofs;
the scripts verify the indicated finite arithmetic and source geometry.
`manifest.json` records file sizes, SHA-256 digests, source basenames,
portability edits, and the successful portability checks. It intentionally
omits private paths and search history.

Excluded material includes the duplicated direct counterexample proof,
exploratory optimizers and searches, floating-point stress arrays, private
process records, and unrelated earlier absorption-relaxation files. The
exact rational ellipsoid matrices themselves are included in full.
