# Independent publication review

Date: 2026-11-07. Reviewer: GPT-6 Astra, xhigh, as an independent LLM
mathematical reviewer. Runtime settings were checked for this review.

Verdict: **APPROVED for all three statements below**, at the exact source
hashes recorded here. No substantive mathematical gap was found. This is
an analytic proof review assisted by exact rational computation, not a
human review or formal certification. None of these three statements was
Lean-checked in this review, and graph integrity checks are not evidence
for their mathematical correctness.

## Statements approved

1. **APPROVED: four sharp-bound counterexamples.**
   [sharp-triangle-join.md](sharp-triangle-join.md) proves full-dimensional
   rational examples at $(n,d)=(132,99),(153,34),(132,82),(129,104)$.
   All nonempty integer fibers have dimension $d$. With its stated
   parameters and $W/b=(2^n-1)m+1+E$, each example satisfies

   $$
   \frac{1}{e2^n}
   <\max_{y\in S}\operatorname{depth}_S(y)
   =\frac{\Gamma_dm}{(2^n-1)m+1+E}
   <\frac{\Gamma_d}{2^n}.
   $$

   This includes the exact maximum, its attainment at every positive-fiber
   centroid, and the strict lower comparison with $1/(e2^n)$. The total
   dimension 187 belongs to $(153,34)$. No global minimality or
   counterexample with both dimensions below 100 is asserted.

2. **APPROVED: the compressed specific-$1/e$ counterexample.**
   [compress-simplex-factor.md](compress-simplex-factor.md), using the
   complete geometric lemma of [df488edae05a1702](../../facts/df488edae05a1702.md),
   proves a full-dimensional rational polytope with
   $n=52$, $d=1345226000000000003$, full-dimensional nonempty fibers,
   and $\sup_{y\in S}\operatorname{depth}_S(y)<1/(e2^{52})$ for proper
   closed ambient halfspaces. The simplex free factor supplies both
   amplification and caps. The stated lower bound for constructions
   preserving these normalized fiber masses also checks out. This does
   not refute the existence of a smaller positive absolute constant.

3. **APPROVED: the support-count obstruction.**
   [support-count-obstruction.md](support-count-obstruction.md) proves
   that a compact convex body with positive mixed-integer $d$-volume and
   $F$ positive-volume integer fibers, $d\ge1$, has a mixed-integer point
   of depth at least $\Gamma_d/F$. Thus a strict specific-$1/e$
   counterexample requires $F/2^n>e\Gamma_d>1+1/[2(d+1)]$.
   On the old support, $F\le2^{52}+32764$, even when some nonempty fibers
   have zero $d$-volume. Therefore $d\ge68,727,866,368$. The statement
   concerns arbitrary convex fiber shapes and volumes on that support,
   not just the simplex-factor construction.

## Direct mathematical checks

For the sharp examples, I checked the three source volumes, the center
weights and scores, the complete truncated-negative-subset lattice
census, the exposing functionals, and the affine facet inequalities
controlling arbitrary convex representations of the origin fiber.
The rational sum-zero coordinate identification is legitimate and has a
common Jacobian that cancels in all normalized volumes. The origin cuts
strictly exclude every unpaid fiber and cover the origin fiber. Positive
fibers admit isolated simplex caps, and negative fibers can be isolated
in their entirety. An integer-only isolating halfspace can contain its
entire selected fiber on its boundary; its positive mass is included.

The largest-barycentric-coordinate argument gives the uniform upper
bound. At a positive-fiber centroid the ordinary centroid inequality
gives the matching lower bound, also for ambient halfspaces with zero
continuous normal. For all four pairs, the exact count obeys
$L<2^n(1+3/2^{86})$ while
$e\Gamma_d>1+1/[2(d+1)]\ge1+1/210>1+3/2^{86}$.
Applying the centroid inequality to a largest fiber therefore proves
the strict weaker-bound comparison; it is not merely an untested limit
of the proposed cuts.

For the compressed example, I checked the inherited tetrahedral facet
and origin-cut formulas directly against the new parameters. Replacing
the box by the displayed simplex preserves the origin fiber through
the common affine facet envelope. All scales and exclusion gaps are
positive. The isolated cap cuts only the simplex factor, hence has the
same relative volume in the product fiber. The finite multiplier used
to exclude other fibers exists because the number of fibers is finite,
the exposure gaps are positive, and the fibers are compact. The two
uniform strict mass estimates prove a strict bound on the supremum.

For the support obstruction, a largest positive-volume fiber is a
full-dimensional convex body in its continuous affine space. Restricting
a containing ambient halfspace gives a containing continuous halfspace
or the whole fiber. Since $W\le FM$, its centroid has depth at least
$\Gamma_dM/W\ge\Gamma_d/F$. Lower-dimensional fibers have zero
$d$-volume and cause no exception. The identity
$\log(e\Gamma_d)=\int_0^1t/(d+t)\,dt$ gives the required strict bounds.
The exact rounding is
$2^{49}/8191=68,727,866,368+1024/8191$, so the strict condition on $d+1$
indeed yields the stated integer bound on $d$.

The centroid theorem was checked in the primary source, Section 3,
pp. 1259–1260 of [Grünbaum, *Partitions of mass-distributions and of
convex bodies by hyperplanes*](https://msp.org/pjm/1960/10-4/pjm-v10-n4-p18-p.pdf).
An incorrect source title in the initial support note was corrected
before the final hashes below were taken.

## Exact-arithmetic verification

The three certificate programs were copied into disposable temporary
directories and run there. Each exited successfully and reproduced its
saved JSON **byte for byte**: `sharp-triangle-join-check.py`,
`sharp-triangle-join-pareto-check.py`, and `compress-certificate.py`.
Repository certificates were not overwritten.

The separate `alternative-join-audit-check.py` was run at all four
parameter sets, replacing only its initial parameter assignments. Its
rational vertex enumeration, determinants, center reconstruction,
facet identities for every positive cardinality, strict cut gaps,
negative scales, and all three mass margins passed. The smallest origin
cut margin among these examples is approximately $1.5101\cdot10^{-7}$
at $(129,104)$; its sign was checked exactly, not from that decimal.

For compression, I also reproduced the finite-binomial enclosure from
`verify-compressed.md`, independently of the supplied binary interval
power routine. The positive expansion through degree 120 with a
geometric tail and the negative expansions through degree 180 with
alternating-tail bounds confirm the stated rational intervals for $m$
and $E$. Their widths are below $10^{-140}$ and $10^{-43}$,
respectively. The displayed mass-surplus identity, simplex-cap margin,
and necessary-dimension rational value were separately recomputed and
are correct. The upper bound on $e$ has the stated strict factorial-tail
justification. No floating-point result is used for certification.

The prior geometric and scalar audits were read as supporting evidence;
their conclusions were not substituted for these direct checks. No
proof, accepted fact, candidate, or graph state was edited by this review.

## Source binding

All hashes are SHA-256 of the publication-worktree file bytes.
Approval applies to these versions; mathematical changes require review.

| Source | SHA-256 |
| --- | --- |
| `sharp-triangle-join.md` | `00aca77dbd701c38038c7e52d59e4aa6ef6965207910aacd573ec4ea295706d8` |
| `compress-simplex-factor.md` | `730f5a3ad380ca7bd399c87384e9f1a09c52f1fc149913c0e867d91dc19de7ba` |
| `support-count-obstruction.md` | `03ab7260add2e56b4192cba0fb23f0ccf15a1eb8398d42328a00967587107f57` |
| `../../facts/df488edae05a1702.md` | `fd4f8fcd73998a71dc2ad3023e097451cc6b6a20cd4a557cb8317d6bd3f8f379` |
| `sharp-triangle-join-check.py` | `ad62b84b5504ae36efa257537bb547afe2ed75a3a45db4dd17a9bf5ee0ef52e7` |
| `sharp-triangle-join-pareto-check.py` | `817b6b65e04e8b6a662fe7a80866577ff833ccfd86e4e249e1d73dbabd205d6c` |
| `compress-certificate.py` | `e42e261697dc35a32b81b263ee1b0d69340eb8b89b6340bd42e37989661c0954` |

## Candidate binding

The final candidate statements were separately inspected and are
**APPROVED**. In particular, the support candidate explicitly qualifies
its dimension conclusion with "If such a strict counterexample has";
the bound is not asserted for every convex body on that support.
The compressed candidate correctly declares dependency on
`df488edae05a1702`; the other two statements use no graph dependency.

For every candidate, the decoded proof equals its reviewed source after
only normalization of relative Markdown links for a file in `facts/`
and removal of the trailing newline. Every normalized local target
exists. Recomputing SHA-256 of the decoded proof reproduces the recorded
`proof_sha256` below. No mathematical content changed in normalization.

| Candidate | Verdict | Decoded proof SHA-256 |
| --- | --- | --- |
| `ad3e63c52f083457` | APPROVED | `6bdbf92b96cc23465f141a2b1fcb6d2dd2ca5ba9f4eeaaa66c11cc466a9cffa8` |
| `cbe1f4518f7088a7` | APPROVED | `b81bb13f4ac39d853033abee0863977edd0412049c288000ae217fbe09a9e477` |
| `30b899ae9d94a523` | APPROVED | `004b00db360da05ac2130919afab9207b65257eeee2ea663fb5f80e5e7153246` |
