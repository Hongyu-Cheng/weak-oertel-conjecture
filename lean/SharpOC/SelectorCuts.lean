import SharpOC.SelectorBody
import SharpOC.SelectorMeasure

/-! The three middle halfspaces and their exact fiber volumes. -/

noncomputable section
open Set MeasureTheory
open scoped ENNReal Pointwise

namespace SharpOC.Selector
open SelectorSources

def middleCut (j : Fin 3) : Ambient →L[ℝ] ℝ :=
  (f j).comp (ContinuousLinearMap.snd ℝ IntegerSpace E) -
    ((5 : ℝ) • balance.toContinuousLinearMap +
      (3 : ℝ) • (ContinuousLinearMap.proj (.inr j) : IntegerSpace →L[ℝ] ℝ)).comp
        (ContinuousLinearMap.fst ℝ IntegerSpace E)

theorem middleCut_apply (j : Fin 3) (z : IntegerSpace) (x : E) :
    middleCut j (z, x) = f j x - (5 * balance z + 3 * z (.inr j)) := rfl

@[simp] theorem middleCut_zero (j : Fin 3) (x : E) : middleCut j (0, x) = f j x := by
  simp [middleCut_apply]

theorem middleCut_nonzero (j : Fin 3) : middleCut j ≠ 0 := by
  intro h
  apply f_nonzero j
  ext x
  simpa using congrArg (fun F : Ambient →L[ℝ] ℝ => F (0, x)) h

theorem middleCut_covers_center (x : E) : ∃ j, 0 ≤ middleCut j (base none, x) := by
  simpa using cyclic_cuts_cover x

private theorem middleCut_light_apply (j k : Fin 3) (J : ↥lightMasks) (x : E) :
    middleCut j (base (some (.inr (k, J))), x) = f j x + if j = k then 3 else 0 := by
  have hb : balance (base (some (.inr (k, J)))) = 0 := by
    simp [base, mask, negative, signedCubeVector, balance_light]
  have hz : base (some (.inr (k, J))) (.inr j) = if j = k then -1 else 0 := by
    by_cases h : j = k <;> simp [base, mask, negative, signedCubeVector, cubeVector, lightMask, h]
  rw [middleCut_apply, hb, hz]
  split_ifs <;> ring

theorem middleCut_covers_light (j : Fin 3) (J : ↥lightMasks) {x : E}
    (hx : x ∈ fiber (some (.inr (j, J)))) :
    0 ≤ middleCut j (base (some (.inr (j, J))), x) := by
  obtain ⟨y, hy, rfl⟩ := hx
  simp only [middleCut_light_apply, ite_true, map_smul, smul_eq_mul]
  exact add_nonneg (mul_nonneg (by norm_num [delta]) (T_f_nonneg j hy)) (by norm_num)

theorem middle_center_cut_volume (j : Fin 3) :
    volume (fiber none ∩ {x | 0 ≤ middleCut j (base none, x)}) =
      ENNReal.ofReal (9 / 20) * volume B := by
  simpa only [fiber, base_none, middleCut_zero] using positive_cap_volume j

/-- Every heavy fiber is below the cut, with at most null boundary contact. -/
theorem middle_heavy_cut_volume (j : Fin 3) (S : ↥heavyMasks) :
    volume (fiber (some (.inl S)) ∩ {x | 0 ≤ middleCut j (base (some (.inl S)), x)}) = 0 := by
  let z := base (some (.inl S))
  refine measure_mono_null ?_ (volume_linear_level_eq_zero (f j) (f_nonzero j)
    (5 * balance z + 3 * z (.inr j)))
  rintro x ⟨hx, hc⟩
  change 0 ≤ middleCut j (z, x) at hc
  rw [middleCut_apply, sub_nonneg] at hc
  change f j x = 5 * balance z + 3 * z (.inr j)
  refine le_antisymm ?_ hc
  obtain ⟨y, hy, rfl⟩ := hx
  have hf : f j ((1 + delta) • y) ≤ 1 + delta := by
    rw [map_smul, smul_eq_mul]
    simpa only [mul_one] using mul_le_mul_of_nonneg_left (B_f_bounds (U_subset_B _ hy) j).2
      (show 0 ≤ 1 + delta by norm_num [delta])
  by_cases hb : balance z = 0
  · obtain ⟨hz, hS⟩ := balanced_heavy_positive S hb
    change z = cubeVector S.val at hz
    rw [hb, hz]
    by_cases hj : Sum.inr j ∈ S.val
    · simp only [cubeVector, ite_eq_left hj, mul_zero, zero_add, mul_one]
      exact hf.trans (by norm_num [delta])
    · have hs := selectedType_mem S.val (balanced_heavy_has_selector S hS)
      have hne : j ≠ selectedType S.val := fun he => hj (he.symm ▸ hs)
      have hfy := T_f_nonpos _ (U_subset_T _ hy) j hne
      simp [cubeVector, hj, map_smul, smul_eq_mul]
      exact mul_nonpos_of_nonneg_of_nonpos (by norm_num [delta]) hfy
  · have hb' : 1 ≤ balance z :=
      one_le_balance_base _ (lt_of_le_of_ne (balance_base_nonneg _) (fun h => hb h.symm))
    have hz : -1 ≤ z (.inr j) := by
      change -1 ≤ signedCubeVector (negative (some (.inl S))) S.val (.inr j)
      cases hs : negative (some (.inl S)) <;> by_cases hj : Sum.inr j ∈ S.val <;>
        norm_num [signedCubeVector, cubeVector, hs, hj]
    linarith [hf, show delta < 1 by norm_num [delta]]

theorem middle_light_cut_volume (j k : Fin 3) (J : ↥lightMasks) :
    volume (fiber (some (.inr (k, J))) ∩ {x | 0 ≤ middleCut j (base (some (.inr (k, J))), x)}) =
      if j = k then volume (fiber (some (.inr (k, J)))) else 0 := by
  by_cases h : j = k
  · subst k
    have hs : fiber (some (.inr (j, J))) ⊆
        {x | 0 ≤ middleCut j (base (some (.inr (j, J))), x)} :=
      fun _ hx => middleCut_covers_light j J hx
    simp only [ite_true, inter_eq_left.mpr hs]
  · simp only [ite_eq_right h]
    refine measure_mono_null ?_ (volume_linear_level_eq_zero (f j) (f_nonzero j) 0)
    rintro x ⟨hx, hc⟩
    change 0 ≤ middleCut j (base (some (.inr (k, J))), x) at hc
    simp only [middleCut_light_apply, ite_eq_right h, add_zero] at hc
    change f j x = 0
    refine le_antisymm ?_ hc
    obtain ⟨y, hy, rfl⟩ := hx
    rw [map_smul, smul_eq_mul]
    exact mul_nonpos_of_nonneg_of_nonpos (by norm_num [delta]) (T_f_nonpos k hy j h)

end SharpOC.Selector
