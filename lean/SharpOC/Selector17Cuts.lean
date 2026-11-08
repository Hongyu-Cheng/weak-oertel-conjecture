import SharpOC.Selector17Body
import SharpOC.SelectorMeasure

/-! The three cuts at the origin and their exact fiber volumes. -/

noncomputable section
open Set MeasureTheory
open scoped ENNReal Pointwise

namespace SharpOC.Selector17
open SelectorSources (E B)
open Selector (volume_linear_level_eq_zero)

def middleCut (j : Fin 3) : Ambient →L[ℝ] ℝ :=
  (f j).comp (ContinuousLinearMap.snd ℝ IntegerSpace E) -
    ((3 : ℝ) • (threshold j).toContinuousLinearMap).comp
      (ContinuousLinearMap.fst ℝ IntegerSpace E)

theorem middleCut_apply (j : Fin 3) (z : IntegerSpace) (x : E) :
    middleCut j (z, x) = f j x - 3 * threshold j z := rfl

@[simp] theorem middleCut_zero (j : Fin 3) (x : E) : middleCut j (0, x) = f j x := by
  simp [middleCut_apply]

theorem middleCut_nonzero (j : Fin 3) : middleCut j ≠ 0 := by
  intro hzero
  apply f_nonzero j
  ext x
  simpa using congrArg (fun F : Ambient →L[ℝ] ℝ => F (0, x)) hzero

theorem middleCut_covers_center (x : E) : ∃ j, 0 ≤ middleCut j (base none, x) := by
  simpa [base_none] using cyclic_cuts_cover x

private theorem middleCut_light_apply (j k : Fin 3) (J : ↥lightMasks) (x : E) :
    middleCut j (base (some (.inr (k, J))), x) = f j x + if j = k then 3 else 0 := by
  rw [middleCut_apply, light_threshold k J j]
  split_ifs <;> ring

theorem middleCut_covers_light (j : Fin 3) (J : ↥lightMasks) {x : E}
    (hx : x ∈ fiber (some (.inr (j, J)))) :
    0 ≤ middleCut j (base (some (.inr (j, J))), x) := by
  obtain ⟨y, hy, rfl⟩ := hx
  simp only [middleCut_light_apply, ite_true, map_smul, smul_eq_mul]
  exact add_nonneg (mul_nonneg (sub_nonneg.mpr delta_lt_one.le) (T_f_nonneg j hy)) (by norm_num)

theorem middle_center_cut_volume (j : Fin 3) :
    volume (fiber none ∩ {x | 0 ≤ middleCut j (base none, x)}) =
      ENNReal.ofReal beta * volume B := by
  simpa only [fiber, base_none, middleCut_zero] using positive_cap_volume j

private theorem f_smul_le (j : Fin 3) {r : ℝ} (hr : 0 ≤ r) {y : E} (hy : y ∈ B) :
    f j (r • y) ≤ r := by
  rw [map_smul, smul_eq_mul]
  simpa only [mul_one] using mul_le_mul_of_nonneg_left (B_f_bounds hy j).2 hr

set_option maxRecDepth 4096 in
/-- Each heavy fiber is below the cut, with at most null boundary contact. -/
theorem middle_heavy_cut_volume (j : Fin 3) (S : ↥heavyMasks) :
    volume (fiber (some (.inl S)) ∩ {x | 0 ≤ middleCut j (base (some (.inl S)), x)}) = 0 := by
  let z := base (some (.inl S))
  refine measure_mono_null ?_ (volume_linear_level_eq_zero (f j) (f_nonzero j)
    (3 * threshold j z))
  rintro x ⟨hx, hc⟩
  change 0 ≤ middleCut j (z, x) at hc
  rw [middleCut_apply, sub_nonneg] at hc
  change f j x = 3 * threshold j z
  refine le_antisymm ?_ hc
  by_cases hS : S.val ∈ balancedMasks
  · rw [fiber, ite_eq_left hS] at hx
    obtain ⟨y, hy, rfl⟩ := hx
    have hr : 0 ≤ 1 + delta := by linarith [delta_pos]
    rw [show threshold j z = _ from paired_heavy_threshold S hS j]
    by_cases hj : j = selectedType S.val
    · simp only [ite_eq_left hj, mul_one]
      exact (f_smul_le j hr (K_subset_B _ hy)).trans (by linarith [delta_lt_one])
    · simp only [ite_eq_right hj, mul_zero, map_smul, smul_eq_mul]
      exact mul_nonpos_of_nonneg_of_nonpos hr (T_f_nonpos _ (K_subset_T _ hy) j hj)
  · rw [fiber, ite_eq_right hS] at hx
    cases hn : nearType S with
    | none =>
      simp only [hn] at hx
      obtain ⟨y, hy, rfl⟩ := hx
      have hb : 1 ≤ threshold j z := regular_heavy_threshold S hS hn j
      linarith [f_smul_le j h_pos.le hy, h_lt_two]
    | some k =>
      simp only [hn] at hx
      have hb := near_heavy_threshold S hn j
      by_cases hj : j = k
      · subst j
        simp only [ite_true] at hb
        change threshold k z = 0 at hb
        simpa only [hb, mul_zero] using nearFiber_f_nonpos _ hx
      · simp only [ite_eq_right hj] at hb
        change 1 ≤ threshold j z at hb
        obtain ⟨y, hy, rfl⟩ := nearFiber_subset_roof k hx
        have hr : 0 ≤ 1 + 2 * delta := by linarith [delta_pos]
        linarith [f_smul_le j hr hy, delta_lt_one]

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
    exact mul_nonpos_of_nonneg_of_nonpos (sub_nonneg.mpr delta_lt_one.le) (T_f_nonpos k hy j h)

end SharpOC.Selector17
