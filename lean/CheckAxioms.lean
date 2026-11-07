import SharpOC

/-! A reproducible check that the formal counterexample and its key interfaces
depend only on Lean's standard logical axioms. An unproved `sorry`, a custom
axiom, or `native_decide` would make this command fail. -/

open Lean Elab Command in
elab "#assert_standard_axioms " id:ident : command => do
  let c ← liftCoreM <| realizeGlobalConstNoOverloadWithInfo id
  let bad := (← collectAxioms c).filter (· ∉ [``propext, ``Classical.choice, ``Quot.sound])
  unless bad.isEmpty do
    throwErrorAt id "{c} depends on nonstandard axioms {bad}"
  elabCommand (← `(#print axioms $id))

#assert_standard_axioms SharpOC.simplex_cap_measure
#assert_standard_axioms SharpOC.exposed_simplex_fiber_sum_mass
#assert_standard_axioms SharpOC.MiddleSimplex.positive_cap_volume
#assert_standard_axioms SharpOC.SourceGeometry.volume_chartSimplex
#assert_standard_axioms SharpOC.SourceContainment.K_add_scaled_A
#assert_standard_axioms SharpOC.Counterexample.body_is_convex_body
#assert_standard_axioms SharpOC.Counterexample.fiber_exact
#assert_standard_axioms SharpOC.Counterexample.integer_point_mem_body_iff
#assert_standard_axioms SharpOC.Counterexample.totalMass_eq
#assert_standard_axioms SharpOC.Counterexample.every_fiber_point_small_cut
#assert_standard_axioms SharpOC.Counterexample.mixedIntegerMass_body_cut_toReal
#assert_standard_axioms SharpOC.Counterexample.sharp_oc_strict_violation
#assert_standard_axioms SharpOC.Counterexample.sharp_oc_counterexample
