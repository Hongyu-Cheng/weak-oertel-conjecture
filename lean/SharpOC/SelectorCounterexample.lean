import SharpOC.SelectorCuts
import SharpOC.SelectorMass
import Mathlib.Analysis.LocallyConvex.Separation

/-! A counterexample to the strengthened mixed-integer depth bound
in integer dimension 14 and continuous dimension 5. -/

noncomputable section

namespace SharpOC.Selector

open Set MeasureTheory SelectorSources
open scoped BigOperators ENNReal

theorem middle_mass (j : Fin 3) :
    (mixedIntegerMass (body ∩ {p | 0 ≤ middleCut j p})).toReal =
      (beta + rowLightMass) * (volume B).toReal := by
  rw [actual_cut_mass, Fintype.sum_option, Fintype.sum_sum_type, Fintype.sum_prod_type]
  simp_rw [middle_center_cut_volume, middle_heavy_cut_volume, middle_light_cut_volume]
  have hsum : (∑ k : Fin 3, ∑ J : ↥lightMasks,
      (if j = k then volume (fiber (some (.inr (k, J)))) else 0).toReal) =
      rowLightMass * (volume B).toReal := by
    rw [Finset.sum_eq_single j]
    · simp [light_volume, rowLightMass, lightMasks_card, mul_assoc]
    · intro k hk hkj
      simp [Ne.symm hkj]
    · simp
  rw [hsum]
  simp [ENNReal.toReal_mul, ENNReal.toReal_ofReal (by norm_num : (0 : ℝ) ≤ 9 / 20),
    beta, a]
  ring

private theorem origin_mem_body : ((0 : IntegerSpace), (0 : E)) ∈ body := by
  have h : (0 : E) ∈ B := interior_subset zero_mem_interior_B
  rwa [← origin_fiber_exact] at h

theorem point_has_small_cut (z : Coordinate → ℤ) (x : E) :
    ∃ F : Ambient →L[ℝ] ℝ, ∃ t : ℝ, F ≠ 0 ∧ t ≤ F ((fun j => (z j : ℝ)), x) ∧
      (mixedIntegerMass (body ∩ {p | t ≤ F p})).toReal ≤
        gamma * heavyMass * (volume B).toReal := by
  by_cases hx : ((fun j => (z j : ℝ)), x) ∈ body
  · obtain ⟨i, hi⟩ := integer_base_census z x hx
    have hb : base i = (fun j => (z j : ℝ)) := by rw [← integerBase_cast, hi]
    have hfiber : x ∈ fiber i := by
      rw [← fiber_exact i]
      simpa only [mem_ofPred_eq, hb] using hx
    rw [← hb]
    rcases i with _ | (S | ⟨j, J⟩)
    · obtain ⟨k, hk⟩ := middleCut_covers_center x
      refine ⟨middleCut k, 0, middleCut_nonzero k, hk, ?_⟩
      rw [middle_mass]
      exact mul_le_mul_of_nonneg_right cap_slack.le B_volume_real_pos.le
    · obtain ⟨F, t, hF, ht, hmass⟩ := heavy_small_cut S x
      exact ⟨F, t, hF, ht, hmass.le⟩
    · refine ⟨middleCut j, 0, middleCut_nonzero j, middleCut_covers_light j J hfiber, ?_⟩
      rw [middle_mass]
      exact mul_le_mul_of_nonneg_right cap_slack.le B_volume_real_pos.le
  · obtain ⟨F, t, hbelow, habove⟩ :=
      geometric_hahn_banach_closed_point body_convex body_compact.isClosed hx
    have hF : F ≠ 0 := by
      intro hzero
      subst F
      have ht := hbelow _ origin_mem_body
      simp only [zero_apply] at ht habove
      linarith
    refine ⟨F, t, hF, habove.le, ?_⟩
    have hempty : body ∩ {p | t ≤ F p} = ∅ :=
      eq_empty_iff_forall_notMem.mpr (fun p ⟨hp, hcut⟩ => (hbelow p hp).not_ge hcut)
    rw [hempty]
    simpa [mixedIntegerMass] using mul_nonneg (mul_nonneg gamma_pos.le heavyMass_pos.le)
      B_volume_real_pos.le

theorem strict_violation (z : Coordinate → ℤ) (x : E) :
    ∃ F : Ambient →L[ℝ] ℝ, ∃ t : ℝ, F ≠ 0 ∧ t ≤ F ((fun j => (z j : ℝ)), x) ∧
      (mixedIntegerMass (body ∩ {p | t ≤ F p})).toReal <
        (gamma / (2 : ℝ)^14) * (mixedIntegerMass body).toReal := by
  obtain ⟨F, t, hF, ht, hmass⟩ := point_has_small_cut z x
  refine ⟨F, t, hF, ht, hmass.trans_lt ?_⟩
  rw [body_mass, ← mul_assoc]
  exact mul_lt_mul_of_pos_right
    ((div_lt_iff₀ totalMass_pos).mp scalar_depth_bound) B_volume_real_pos

theorem ambient_dimension : Module.finrank ℝ Ambient = 19 := by
  simp [Ambient, IntegerSpace, Coordinate, E, Module.finrank_prod]

/-- A genuine compact, full-dimensional convex body with positive finite
mixed-integer mass and a uniform strict upper bound on its normalized depth. -/
theorem sharp_oc_counterexample :
    ∃ C : Set Ambient, IsCompact C ∧ Convex ℝ C ∧ (interior C).Nonempty ∧
      ((0 : IntegerSpace), (0 : E)) ∈ C ∧
      0 < mixedIntegerMass C ∧ mixedIntegerMass C ≠ ⊤ ∧
      ∃ r : ℝ, 0 < r ∧ r < (((5 : ℝ) / 6)^5 / (2 : ℝ)^14) ∧
        ∀ (z : Coordinate → ℤ) (x : E),
          ∃ F : Ambient →L[ℝ] ℝ, ∃ t : ℝ, F ≠ 0 ∧ t ≤ F ((fun j => (z j : ℝ)), x) ∧
            (mixedIntegerMass (C ∩ {p | t ≤ F p})).toReal /
              (mixedIntegerMass C).toReal ≤ r := by
  refine ⟨body, body_compact, body_convex, body_interior_nonempty, origin_mem_body,
    pos_iff_ne_zero.mpr body_mass_ne_zero, body_mass_finite, gamma * heavyMass / totalMass,
    div_pos (mul_pos gamma_pos heavyMass_pos) totalMass_pos, scalar_depth_bound, ?_⟩
  intro z x
  obtain ⟨F, t, hF, ht, hm⟩ := point_has_small_cut z x
  refine ⟨F, t, hF, ht, (div_le_iff₀ body_mass_pos).2 ?_⟩
  rw [body_mass, ← mul_assoc, div_mul_cancel₀ _ totalMass_pos.ne']
  exact hm

end SharpOC.Selector
