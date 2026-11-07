import SharpOC.BoxBody

/-! Four proper ambient cuts cover every point of the actual middle fiber. -/

noncomputable section
open Set Finset
open scoped BigOperators

namespace SharpOC.BoxCounterexample

open BoxParameters

def middleCut (j : Fin 4) : Ambient →L[ℝ] ℝ :=
  (coordinateFunctional (cutCoefficient j)).toContinuousLinearMap.comp
      (ContinuousLinearMap.fst ℝ IntegerSpace E) +
    ((BoxSources.f j).comp
      (ContinuousLinearMap.fst ℝ BoxSources.E0 FreeSpace)).comp
      (ContinuousLinearMap.snd ℝ IntegerSpace E)

theorem middleCut_apply (j : Fin 4) (z : IntegerSpace) (x : E) :
    middleCut j (z, x) = coordinateFunctional (cutCoefficient j) z + BoxSources.f j x.1 := by
  simp only [middleCut, ContinuousLinearMap.add_apply, ContinuousLinearMap.comp_apply,
    ContinuousLinearMap.coe_fst', ContinuousLinearMap.coe_snd',
    LinearMap.coe_toContinuousLinearMap']

theorem middleCut_zero (j : Fin 4) (x : E) :
    middleCut j (0, x) = BoxSources.f j x.1 := by simp [middleCut_apply]

theorem middleCut_nonzero (j : Fin 4) : middleCut j ≠ 0 := by
  intro hz
  apply BoxSources.f_nonzero j
  ext x
  have heq := congrArg (fun F : Ambient →L[ℝ] ℝ => F (0, (x, 0))) hz
  simpa only [middleCut_zero, ContinuousLinearMap.zero_apply] using heq

theorem middleCut_cover (x : E) : ∃ j, 0 ≤ middleCut j (0, x) := by
  simpa only [middleCut_zero] using BoxSources.cuts_cover x.1

theorem middleCut_outer_iff (j : Fin 4) (i : IntegerCoordinate)
    {x : E} (hx : x ∈ A i.1) :
    0 ≤ middleCut j (negativeUnit i, x) ↔ paid j i := by
  rw [middleCut_apply, integer_cut_negative]
  by_cases hp : paid j i
  · rw [show cutCoefficient j i = -penalty by simp [cutCoefficient, hp]]
    simp only [neg_neg, hp, iff_true]
    have hf := (BoxSources.f_A_bounds i.1 j hx.1).1
    have ht : 2*t < penalty := by norm_num [t, penalty]
    linarith
  · rw [show cutCoefficient j i = eta*epsilon by simp [cutCoefficient, hp]]
    simp only [hp, iff_false]
    have hm : j ≠ i.1 := Ne.symm hp
    have hf := BoxSources.f_A_missed i.1 j hm hx.1
    have ht := mul_lt_mul_of_pos_right t_lt_eta epsilon_pos
    linarith

theorem middleCut_excludes_core (j : Fin 4) (S : Finset IntegerCoordinate)
    (hS : S.Nonempty) {x : E} (hx : x ∈ K (selectedType S) S.card) :
    middleCut j (cubeVector S, x) < 0 := by
  classical
  have hk : 1 ≤ S.card := hS.card_pos
  have hkR : (1 : ℝ) ≤ S.card := by exact_mod_cast hk
  have hcard : (S.card : ℝ) ≤ 76 := by exact_mod_cast cube_card_le_dimension S
  rw [middleCut_apply]
  by_cases hp : ∃ i ∈ S, paid j i
  · have hi := paid_integer_cut j S hp
    have hf := BoxSources.f_K_le (selectedType S) j S.card hk hx.1
    have htilt : eta*epsilon ≤ 1 := by norm_num [eta, epsilon]
    have hmul := mul_le_mul_of_nonneg_left htilt (sub_nonneg.mpr hkR)
    norm_num [penalty] at hi
    linarith
  · have hm : ∀ i ∈ S, ¬ paid j i := by simpa only [not_exists, not_and] using hp
    rw [unpaid_integer_cut j S hm]
    have hf := BoxSources.f_K_missed (selectedType S) j
      (Ne.symm (selectedType_misses S hS j hm)) S.card hx.1
    norm_num [eta, epsilon, s] at hf ⊢
    linarith

theorem middleCut_B_cap_eq (j : Fin 4) :
    B ∩ {x | 0 ≤ middleCut j (0, x)} =
      (BoxSources.B0 ∩ {x | 0 ≤ BoxSources.f j x}) ×ˢ F := by
  ext x
  simp only [Set.mem_inter_iff, Set.mem_setOf_eq, B, Set.mem_prod, middleCut_zero]
  tauto

theorem fiber_cut_core_eq_empty (j : Fin 4) (S : Finset IntegerCoordinate)
    (hS : S.Nonempty) :
    fiber (.inl S) ∩ {x | 0 ≤ middleCut j (base (.inl S), x)} = ∅ := by
  rw [fiber_inl, coreFiber_of_nonempty S hS, base_inl]
  apply Set.eq_empty_iff_forall_notMem.mpr
  rintro x ⟨hx, hcut⟩
  exact (not_le_of_gt (middleCut_excludes_core j S hS hx)) hcut

theorem fiber_cut_outer_eq (j : Fin 4) (i : IntegerCoordinate) :
    fiber (.inr i) ∩ {x | 0 ≤ middleCut j (base (.inr i), x)} =
      if paid j i then A i.1 else ∅ := by
  rw [fiber_inr, base_inr]
  ext x
  by_cases hp : paid j i
  · simp only [if_pos hp, Set.mem_inter_iff, Set.mem_setOf_eq]
    exact ⟨fun hx => hx.1, fun hx => ⟨hx, (middleCut_outer_iff j i hx).mpr hp⟩⟩
  · simp only [if_neg hp, Set.mem_empty_iff_false, iff_false,
      Set.mem_inter_iff, Set.mem_setOf_eq]
    rintro ⟨hx, hcut⟩
    exact hp ((middleCut_outer_iff j i hx).mp hcut)

theorem fiber_cut_middle_eq (j : Fin 4) :
    fiber (.inl ∅) ∩ {x | 0 ≤ middleCut j (base (.inl ∅), x)} =
      (BoxSources.B0 ∩ {x | 0 ≤ BoxSources.f j x}) ×ˢ F := by
  simpa only [fiber_inl, coreFiber_empty, base_empty] using middleCut_B_cap_eq j

end SharpOC.BoxCounterexample
