# Dimension reduction: exact constructions and obstructions

Research checkpoint, 7 November 2026.

## Results and scope

Let Gamma_d=(d/(d+1))^d and let D(C) be the maximum normalized
mixed-integer halfspace depth of C. The two constants Gamma_d and 1/e
are different targets. Neither a counterexample to the sharp constant nor
one to the specific constant 1/e disproves the conjecture that some smaller
positive absolute constant works in all dimensions.

| Result | Integer dimension n | Continuous dimension d | Strict bound disproved |
|---|---:|---:|---|
| Existing accepted witness, independently replayed | 52 | 2,305,843,009,213,968,736 | 1/(e 2^n), and consequently Gamma_d/2^n |
| New parameter improvement of that witness | 52 | 1,350,000,000,002,747,789 | 1/(e 2^n), and consequently Gamma_d/2^n |
| New symmetric simplex join | 168 | 99 | Gamma_99/2^168 |
| New asymmetric simplex join | 167 | 99 | Gamma_99/2^167 |

**The target n,d<100 has not been achieved.** The simplex joins reach
d<100 but do not violate 1/e. The new n=52 specialization reduces its
continuous dimension by about 41.45%, but that dimension remains enormous.
No unrestricted minimal-dimension claim is made.

The complete new arguments are:

- [Asymmetric (167,99) construction](sharp-n167-d99.md).
- [Simpler symmetric (168,99) construction](sharp-n168-d99.md).
- [Improved n=52 counterexample to 1/e](improved-n52.md).
- [Support and sufficient-inequality obstructions](support-dimension-obstruction.md).
- [Verification of the original counterexamples](existing-counterexample-verification.md).

## Why the new sharp construction uses only 99 continuous variables

The old n=52 construction uses source boxes and a huge common simplex
factor. The factor provides a cap with fraction Gamma_ell, which must be
so close to 1/e that its error fits a tiny effective-count surplus.

The new construction makes every noncentral fiber a 99-simplex from the
start. A two-dimensional triangular source is joined to 97 additional
simplex vertices. This preserves its source-volume and middle-cap ratios,
while allowing the exact ordinary simplex constant Gamma_99 at every
point of a noncentral fiber. Three middle cuts handle the central simplex.

For the (167,99) witness, split the integer coordinates into blocks of
sizes (56,56,55). Use all positive Boolean bases and all negative Boolean
subsets of sizes at most 30 inside one block. The source triangles have
slightly different shapes. Contracting one source vertex by a rational
factor makes every positive fiber have exactly the same volume mb, with
m=660847/200000 and b the middle-simplex volume. This exact equality is
essential: approximate equality would not suffice at this scale.

If E_a b is the total negative-fiber volume in block a and beta_a b the
corresponding middle cap, exact fractions establish

\[
 1+\sum_a E_a-m>8\cdot10^{-5},\qquad
 \Gamma_{99}m-\beta_a-E_a>8\cdot10^{-5}\quad(a=0,1,2).
\]

The actual total mass is W=b[(2^167-1)m+1+sum_a E_a]. The proof controls
every actual fiber using affine facet inequalities, rather than assuming
the prescribed middle fiber survives the convex hull. Every noncentral
base is exposed, so its simplex cap can be isolated by a finite integer
tilt. The three middle cuts cover the middle fiber. These facts give

\[
 D(C)=\frac{\Gamma_{99}m}{(2^{167}-1)m+1+\sum_a E_a}
       <\frac{\Gamma_{99}}{2^{167}}.
\]

The equality uses ordinary Grunbaum at the centroid of a positive fiber;
the strict counterexample itself needs only the proved upper bound.
The exact certificate also shows 2^167 D(C)>24/65>1/e, so the distinction
between the sharp and 1/e targets is substantive.

## Why further tuning the old support cannot meet the target

If a body has F positive-volume integer fibers of common dimension d,
largest fiber volume M and total volume W, its largest-fiber centroid gives

\[
 D(C)\ge\Gamma_d M/W\ge\Gamma_d/F.
\]

A strict 1/e violation therefore requires F/2^n>e Gamma_d. Since
log(e Gamma_d)=integral_0^1 t/(d+t) dt>1/[2(d+1)], it requires
F/2^n>1+1/[2(d+1)]. The n=52 support has F=2^52+32764. Thus every
1/e counterexample using this support, even with completely redesigned
convex fiber shapes, must satisfy

\[
 d\ge68,727,866,368.
\]

This is a rigorous obstruction for the support, not a numerical failure
of a parameter optimizer. It does not restrict unrelated lattice supports
or sharp-bound counterexamples. The same note proves that the current
equal-block construction's pair of sufficient scalar inequalities needs
N>=13, hence n>=52. That latter claim concerns the proof mechanism only.

To reach n,d<100 for the 1/e target, the support and its cut-incidence
pattern must change. At d=99, one needs over roughly 0.5% more
positive-volume fibers than 2^n; the old n=52 support exceeds 2^52 by
only about 7.3e-12 in relative terms. Dense negative codes are compatible
with the basic lattice projection, but each added fiber must also respect
the exact central-fiber inclusions and the budgets of every middle cut.

## Verification and independent work

The work used seven distinct model subagents, with roles split across
repository context, original-proof verification, low-dimensional source
geometry, finite optimization, lower bounds and the 1/e target, a separate
full join audit, and asymmetric finite-dimensional refinement. Several
reviewed one another's constructions. These are model mathematical reviews
and executable exact-arithmetic checks, not human certification or Lean
formalizations.

The original n=52 certificate was independently regenerated byte-for-byte.
The n=52 and n=76 source checkers and the direct d=23 checker passed. A
separate rational log/exp Taylor implementation also reproduced the recorded
1/e witnesses and the new n=52 parameters, independently of binary-power
interval arithmetic.

The symmetric (168,99) construction has a separate audit with over one
million exact rational predicates and a full analytic proof review. The
new asymmetric construction has its own exact geometry/scalar checker and
complete analytic proof. A separate reviewer independently recomputed its
parameters and geometric predicates from the proof without importing that
checker, and found no mathematical gap. Its record is
`low_d_audit_n167.json`. Independent final review notes are stored alongside
the proofs. The finite checks supplement the general lattice census,
origin-fiber and every-point arguments; they do not enumerate 2^167 bases.

### Reproduce the exact checks

From the repository root, using Python's standard library only:

```sh
python3 -B research/dimension-reduction-20261107/check_asymmetric_n167.py
python3 -B research/dimension-reduction-20261107/check_sharp_join.py
python3 -B research/dimension-reduction-20261107/join_audit_checker.py
python3 -B research/dimension-reduction-20261107/check_improved_n52.py
python3 -B research/dimension-reduction-20261107/check_improved_n52_independently.py
python3 -B research/dimension-reduction-20261107/check_support_obstruction.py
```

The independent Taylor replay imports
`scripts/check_one_over_e_independently.py`, introduced by the repository's
integration audit. Source checkers and their replay outputs are preserved
for comparison. The optional simplified parameters of the symmetric
construction can be checked with `check_sharp_join.py --variant simplified`;
the complete symmetric proof and main independent audit use the original
parameters.

## Search record and limitations

Files ending in `_search.py` and their JSON outputs are exploratory and
use floating-point SciPy optimization. They are not certificates or
exclusion theorems. Searches included general triangular fans, symmetric
polygonal fans, three-cut tetrahedral sources, four-cut tetrahedral fans,
and asymmetric box sources. The ideal triangular search already permits
arbitrary common interior points and positively spanning triples of normals.

The asymmetric finite search found positive margins at total n=167 and
negative local optima at n=166 and 165. This does not prove that n=167
is optimal, even within all triangular variants. The present source-cone
and support families remain too restrictive to resolve the requested
range. Multi-type negative subsets, denser codes and jointly designed
source/cut patterns remain open directions; none is asserted to work here.

A useful necessary constraint for a denser code is already available from
the actual central fiber. If a negative support J has size r, then
A_J+sum_(i in J) K_(e_i) is contained in (r+1)B. When the singleton
fibers all have volume mb and the negative fiber has volume alpha b,
Brunn-Minkowski gives alpha^(1/d)+r m^(1/d)<=r+1 and hence
alpha m^r<=1. These conditions can reject infeasible volume assignments
before attempting a full geometric realization.

## Repository provenance

The initial main snapshot was `5cc4e76e3823c6622819fa77c2a7bf4c1586dba0`.
The research branch is based on the integration-audit main commit
`635ad260847e3a986502dd54cb465a614e77ce5b`. Accepted fact
[`df488edae05a1702`](../../facts/df488edae05a1702.md) supplies the existing
1/e construction and its generalized geometric lemma. The source geometry
and exact all-point arguments for the new sharp witnesses are supplied
here in full. New graph entries are pending submissions; the locked
problem statement and existing accepted facts are unchanged.

| Pending candidate | Claim |
|---|---|
| [a9ad2d2aba5c43ef](../../candidates/a9ad2d2aba5c43ef.json) | Sharp counterexample at (167,99) |
| [057b74eccf884a48](../../candidates/057b74eccf884a48.json) | Improved n=52 counterexample to 1/e |
| [b5350f9ff9ff4403](../../candidates/b5350f9ff9ff4403.json) | Support obstruction and scoped sufficient-inequality barrier |
