# A counterexample to the specific 1/e bound in total dimension 1387

There is a full-dimensional rational polytope
$C\subset\mathbb R^{209}\times\mathbb R^{1178}$ such that every point of
$\mathbb Z^{209}\times\mathbb R^{1178}$ lies in a proper closed halfspace $H$ with
$\mu(C\cap H)/\mu(C)<36787944/(10^8\,2^{209})<1/(e\,2^{209})$, where $\mu$ sums
the 1178-dimensional fiber volumes over the integer bases. The
[analytic proof](../../facts/a02d398c0677c03a.md) is an accepted fact with the
`LLM-verified` label, and the Lean theorem below proves the same bound. The
example refutes the constant $1/e$, not the weak statement of the
[problem](../../problem_statement.md), which allows any smaller constant.

## Reproduce the verification

From the repository root, run the exact certificate and build with the
pinned Lean toolchain and mathlib revision. Lake and Elan must be on the
path, and the first run needs access to the mathlib dependency and its
cache.

```sh
python3 -I -B research/one-over-e-dimension-1387/check.py
cd lean
lake exe cache get
lake build
lake env lean CheckAxioms.lean
lake env lean CheckWitness1387Axioms.lean
```

## What Lean proves

The witness lives in the `SharpOC.Witness1387` namespace. The Lean body
is the real convex hull of a finite set of rational generating points. Lean
proves its full dimension, the exact census of integer bases of
nonempty fibers, and the finite fiber-sum representation of its actual
mixed-integer volume. It also proves the exact active-center fibers,
the cap bounds at the exposed sources and active centers, the pool
census, and the strict rational inequalities. Lean stretches the
inactive simplex along the last continuous coordinate, as in
equation (6) of the [analytic proof](../../facts/a02d398c0677c03a.md).

The final theorem `SharpOC.Witness1387.one_over_e_depth` gives a
proper closed halfspace of relative mass below the target at every
mixed-integer point, including boundary and exterior points. The
theorem `strict_depth` proves the stronger rational bound. Both are
in [DepthBound.lean](../../lean/SharpOC/Witness1387/DepthBound.lean).

- `inactive_triple_exposed` constructs a strict exposing linear form
  at every inactive baseline with exactly three zero slots, using
  the priority comparisons from Section 5 of
  [the proof](../../facts/a02d398c0677c03a.md#5-exposing-baselines-with-three-or-more-zero-blocks).
  See [InactiveTriple.lean](../../lean/SharpOC/Witness1387/InactiveTriple.lean).
- `sourceMass_sum` evaluates the exact sum over `SupportIndex` using
  the ordinary and extra active-center pool counts and the count of
  inactive baseline sources. Each light contributes to the pool of
  its active center. This is the census in Section 8 of the proof.

The axiom audit includes both results and the final theorem. It
rejects dependencies outside `propext`, `Classical.choice`, and
`Quot.sound`.
