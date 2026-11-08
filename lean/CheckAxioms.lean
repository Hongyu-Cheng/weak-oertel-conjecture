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

-- The n=76 counterexample to the specific 1/e bound.
#assert_standard_axioms SharpOC.TetrahedronVolume.volume_standardSimplex_three
#assert_standard_axioms SharpOC.BoxSources.T_volume
#assert_standard_axioms SharpOC.BoxSources.K_add_sum_A
#assert_standard_axioms SharpOC.BoxSources.cap_volume
#assert_standard_axioms SharpOC.BoxCounterexample.body_is_convex_body
#assert_standard_axioms SharpOC.BoxCounterexample.integer_point_mem_body_iff
#assert_standard_axioms SharpOC.BoxCounterexample.integer_fiber_exact
#assert_standard_axioms SharpOC.BoxCounterexample.middle_cut_mass
#assert_standard_axioms SharpOC.BoxCounterexample.mixedIntegerMass_paddedBody_toReal
#assert_standard_axioms SharpOC.BoxCounterexample.padded_fibers_full_dimensional
#assert_standard_axioms SharpOC.BoxPadding.exposed_product_simplex_fiber_sum_mass
#assert_standard_axioms SharpOC.BoxParameters.scalar_depth_bound
#assert_standard_axioms SharpOC.BoxCounterexample.point_has_small_halfspace
#assert_standard_axioms SharpOC.BoxCounterexample.one_over_e_counterexample

-- The 19-dimensional counterexample to the strengthened bound.
#assert_standard_axioms SharpOC.Selector.integerBase_injective
#assert_standard_axioms SharpOC.Selector.origin_fiber_exact
#assert_standard_axioms SharpOC.Selector.fiber_exact
#assert_standard_axioms SharpOC.Selector.integer_base_census
#assert_standard_axioms SharpOC.Selector.body_mass
#assert_standard_axioms SharpOC.Selector.middle_mass
#assert_standard_axioms SharpOC.Selector.ambient_dimension
#assert_standard_axioms SharpOC.Selector.strict_violation
#assert_standard_axioms SharpOC.Selector.sharp_oc_counterexample

-- The 17-dimensional counterexample to the strengthened bound.
#assert_standard_axioms SharpOC.Selector17.integerBase_injective
#assert_standard_axioms SharpOC.Selector17.integer_projection_census
#assert_standard_axioms SharpOC.Selector17.origin_fiber_exact
#assert_standard_axioms SharpOC.Selector17.integer_fiber_exact
#assert_standard_axioms SharpOC.Selector17.nearFiber_volume
#assert_standard_axioms SharpOC.Selector17.K_cap_volume
#assert_standard_axioms SharpOC.Selector17.body_mass
#assert_standard_axioms SharpOC.Selector17.middle_mass
#assert_standard_axioms SharpOC.Selector17.ambient_dimension
#assert_standard_axioms SharpOC.Selector17.strict_violation
#assert_standard_axioms SharpOC.Selector17.sharp_oc_counterexample
