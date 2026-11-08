import SharpOC.Witness1387

/-! Reject dependencies outside Lean's standard logical axioms. -/

open Lean Elab Command in
elab "#assert_standard_axioms " id:ident : command => do
  let c ← liftCoreM <| realizeGlobalConstNoOverloadWithInfo id
  let bad := (← collectAxioms c).filter (· ∉ [``propext, ``Classical.choice, ``Quot.sound])
  unless bad.isEmpty do
    throwErrorAt id "{c} depends on nonstandard axioms {bad}"
  elabCommand (← `(#print axioms $id))

#assert_standard_axioms SharpOC.Witness1387.rationalVertices_finite
#assert_standard_axioms SharpOC.Witness1387.body_interior_nonempty
#assert_standard_axioms SharpOC.Witness1387.integer_census
#assert_standard_axioms SharpOC.Witness1387.integerFiber_nonempty_iff
#assert_standard_axioms SharpOC.Witness1387.active_fiber_eq
#assert_standard_axioms SharpOC.Witness1387.mixedVolume_eq_fiber_sum
#assert_standard_axioms SharpOC.Witness1387.active_center_cap
#assert_standard_axioms SharpOC.Witness1387.exposed_inactiveSimplex_cap
#assert_standard_axioms SharpOC.Witness1387.inactive_single_exposed
#assert_standard_axioms SharpOC.Witness1387.inactive_pair_exposed
#assert_standard_axioms SharpOC.Witness1387.inactive_triple_exposed
#assert_standard_axioms SharpOC.Witness1387.inactive_many_exposed
#assert_standard_axioms SharpOC.Witness1387.sum_sourceMass_by_center
#assert_standard_axioms SharpOC.Witness1387.sourceMass_sum
#assert_standard_axioms SharpOC.Witness1387.uniformBound_lt_target
#assert_standard_axioms SharpOC.Witness1387.integer_fibers_eq
#assert_standard_axioms SharpOC.Witness1387.mixedVolume_toReal
#assert_standard_axioms SharpOC.Witness1387.strict_depth
#assert_standard_axioms SharpOC.Witness1387.one_over_e_depth
