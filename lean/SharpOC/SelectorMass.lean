import SharpOC.SelectorBody
import SharpOC.SelectorMeasure

/-! Exact body volume and the exposed-simplex cuts of large fibers. -/

noncomputable section

namespace SharpOC.Selector

open Set MeasureTheory SelectorSources
open scoped BigOperators ENNReal Pointwise

theorem B_volume_real_pos : 0 < (volume B).toReal :=
  ENNReal.toReal_pos B_volume_pos.ne' B_volume_ne_top

private theorem volume_smul_real (r : ℝ) (hr : 0 ≤ r) (K : Set E) :
    (volume (r • K)).toReal = r ^ 5 * (volume K).toReal := by
  rw [Measure.addHaar_smul_of_nonneg volume hr, ENNReal.toReal_mul]
  simp [E, ENNReal.toReal_ofReal (pow_nonneg hr _)]

theorem heavy_volume (S : ↥heavyMasks) :
    (volume (fiber (some (.inl S)))).toReal = heavyMass * (volume B).toReal := by
  change (volume ((1 + delta) • U (selectedType S.val))).toReal = _
  rw [volume_smul_real _ (by norm_num [delta]), U_volume, ENNReal.toReal_mul]
  norm_num [heavyMass, a]
  ring

theorem light_volume (j : Fin 3) (J : ↥lightMasks) :
    (volume (fiber (some (.inr (j, J))))).toReal = lightMass * (volume B).toReal := by
  change (volume ((1 - delta) • T j)).toReal = _
  rw [volume_smul_real _ (by norm_num [delta]), T_volume, ENNReal.toReal_mul]
  norm_num [lightMass, beta, a]
  ring

theorem body_mass : (mixedIntegerMass body).toReal = totalMass * (volume B).toReal := by
  rw [mixedIntegerMass_body_toReal integerBase integerBase_injective integer_base_census
    fiber integer_fiber_exact fiber_compact, Fintype.sum_option, Fintype.sum_sum_type,
    Fintype.sum_prod_type]
  simp_rw [heavy_volume, light_volume]
  simp [fiber, totalMass, rowLightMass, heavyMasks_card, lightMasks_card]
  ring

theorem body_mass_pos : 0 < (mixedIntegerMass body).toReal := by
  rw [body_mass]
  exact mul_pos totalMass_pos B_volume_real_pos

theorem body_mass_finite : mixedIntegerMass body ≠ ⊤ := by
  intro h
  simpa [h] using body_mass_pos

theorem body_mass_ne_zero : mixedIntegerMass body ≠ 0 := by
  intro h
  simpa [h] using body_mass_pos

theorem actual_cut_mass (F : Ambient → ℝ) (t : ℝ) :
    (mixedIntegerMass (body ∩ {p | t ≤ F p})).toReal =
      ∑ i, (volume (fiber i ∩ {x | t ≤ F (base i, x)})).toReal := by
  rw [mixedIntegerMass_closedCut_toReal integerBase integerBase_injective integer_base_census
    fiber integer_fiber_exact fiber_compact F t]
  simp only [integerBase_cast]

theorem heavy_small_cut (S : ↥heavyMasks) (x : E) :
    ∃ F : Ambient →L[ℝ] ℝ, ∃ t : ℝ, F ≠ 0 ∧ t ≤ F (base (some (.inl S)), x) ∧
      (mixedIntegerMass (body ∩ {p | t ≤ F p})).toReal =
        gamma * heavyMass * (volume B).toReal := by
  let i : FiberIndex := some (.inl S)
  let ℓ := (signedCubeExposingFunctional (negative i) (mask i)).toContinuousLinearMap
  let b := scaledTranslatedBasis (uBasis (selectedType S.val)) (1 + delta) (0 : E)
    (by norm_num [delta])
  have hb : fiber i = convexHull ℝ (range b) := by
    rw [show fiber i = (1 + delta) • U (selectedType S.val) from rfl]
    dsimp only [b]
    rw [scaledTranslatedBasis_hull, ← U_eq_hull]
    simp only [add_zero, Set.image_smul]
  obtain ⟨F, t, hF, ht, hmass⟩ := exposed_simplex_fiber_sum_mass (d := 5)
    (by decide) (by simp [E]) volume base fiber fiber_compact i ℓ
    (base_exposed i (by simp [i])) b hb x
  refine ⟨F, t, hF, ht, ?_⟩
  rw [actual_cut_mass, ← ENNReal.toReal_sum]
  · rw [hmass, ENNReal.toReal_mul, ENNReal.toReal_ofReal (by positivity)]
    rw [show (volume (fiber i)).toReal = heavyMass * (volume B).toReal from heavy_volume S]
    norm_num [gamma]
    ring
  · exact fun j _ => measure_ne_top_of_subset inter_subset_left (fiber_compact j).measure_ne_top

end SharpOC.Selector
