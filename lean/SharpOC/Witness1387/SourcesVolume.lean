import SharpOC.BoxPadding

/-! The factorial volume formula in the standard simplex coordinate chart. -/

noncomputable section
open Set MeasureTheory
open scoped ENNReal

namespace SharpOC.Witness1387

private theorem simplex_mem {n : ℕ} (x : Fin n → ℝ) :
    x ∈ BoxPadding.simplex n ↔ (∀ i, 0 ≤ x i) ∧ ∑ i, x i ≤ 1 := by
  rw [BoxPadding.simplex, (MiddleSimplex.standardBasis n).convexHull_eq_nonneg_coord]
  change (∀ j, 0 ≤ (MiddleSimplex.standardBasis n).coord j x) ↔ _
  constructor
  · intro h
    refine ⟨fun i => ?_, ?_⟩
    · simpa only [MiddleSimplex.standardBasis_coord_castSucc] using h i.castSucc
    · simpa only [MiddleSimplex.standardBasis_coord_last, sub_nonneg] using h (Fin.last n)
  · rintro ⟨h, hs⟩ j
    rcases Fin.eq_castSucc_or_eq_last j with ⟨i, rfl⟩ | rfl
    · simpa only [MiddleSimplex.standardBasis_coord_castSucc] using h i
    · simpa only [MiddleSimplex.standardBasis_coord_last, sub_nonneg] using hs

private theorem scaled_simplex {n : ℕ} {r : ℝ} (hr : 0 ≤ r) :
    (AffineMap.homothety (0 : Fin n → ℝ) r) '' BoxPadding.simplex n =
      {x | (∀ i, 0 ≤ x i) ∧ ∑ i, x i ≤ r} := by
  ext x
  constructor
  · rintro ⟨y, hy, rfl⟩
    rw [simplex_mem] at hy
    simp only [mem_ofPred_eq, AffineMap.homothety_apply, vsub_eq_sub, sub_zero,
      vadd_eq_add, add_zero, Pi.smul_apply, smul_eq_mul, ← Finset.mul_sum]
    exact ⟨fun i => mul_nonneg hr (hy.1 i), by
      simpa using mul_le_mul_of_nonneg_left hy.2 hr⟩
  · rintro ⟨h, hs⟩
    rcases hr.eq_or_lt with rfl | hp
    · have hzero : x = 0 := by
        ext i
        exact le_antisymm ((Finset.single_le_sum (fun j _ => h j) (Finset.mem_univ i)).trans hs)
          (h i)
      subst x
      exact ⟨0, BoxPadding.zero_mem_simplex n, by simp⟩
    · refine ⟨r⁻¹ • x, (simplex_mem _).2 ⟨fun i => mul_nonneg (inv_nonneg.mpr hr) (h i), ?_⟩, ?_⟩
      · simp only [Pi.smul_apply, smul_eq_mul]
        rwa [← Finset.mul_sum, ← div_eq_inv_mul, div_le_iff₀ hp, one_mul]
      · simp [AffineMap.homothety_apply, smul_smul, mul_inv_cancel₀ hp.ne']

private theorem pow_lintegral (n : ℕ) :
    (∫⁻ t : ℝ in Icc (0 : ℝ) 1, ENNReal.ofReal ((1 - t) ^ n)) =
      ENNReal.ofReal (1 / ((n : ℝ) + 1)) := by
  have hcont : Continuous (fun t : ℝ => (1 - t) ^ n) :=
    (continuous_const.sub continuous_id).pow n
  have hpos : 0 ≤ᵐ[(volume : Measure ℝ).restrict (Icc 0 1)] fun t => (1 - t) ^ n := by
    filter_upwards [ae_restrict_mem (μ := (volume : Measure ℝ)) measurableSet_Icc] with t ht
    exact pow_nonneg (sub_nonneg.mpr ht.2) n
  rw [← ofReal_integral_eq_lintegral_ofReal hcont.integrableOn_Icc hpos]
  congr 1
  rw [setIntegral_congr_set (Ioc_ae_eq_Icc (μ := (volume : Measure ℝ))).symm,
    ← intervalIntegral.integral_of_le (by norm_num : (0 : ℝ) ≤ 1)]
  rw [intervalIntegral.integral_comp_sub_left (fun t : ℝ => t ^ n) (1 : ℝ), integral_pow]
  simp

theorem standardSimplex_volume (n : ℕ) :
    volume (BoxPadding.simplex n) = ENNReal.ofReal (1 / (n.factorial : ℝ)) := by
  induction n with
  | zero =>
      have hz : (fun i : Fin 0 => (isEmptyElim i : ℝ)) = 0 := Subsingleton.elim _ _
      rw [Measure.volume_pi_eq_dirac, hz, Measure.dirac_apply_of_mem
        (BoxPadding.zero_mem_simplex 0)]
      norm_num
  | succ n ih =>
      let e := MeasurableEquiv.piFinSuccAbove (fun _ : Fin (n + 1) => ℝ) (Fin.last n)
      let S : Set (ℝ × (Fin n → ℝ)) :=
        {p | 0 ≤ p.1 ∧ (∀ i, 0 ≤ p.2 i) ∧ p.1 + ∑ i, p.2 i ≤ 1}
      have he : e ⁻¹' S = BoxPadding.simplex (n + 1) := by
        ext x
        rw [simplex_mem]
        change (0 ≤ x (Fin.last n) ∧ (∀ i, 0 ≤ x ((Fin.last n).succAbove i)) ∧
          x (Fin.last n) + ∑ i, x ((Fin.last n).succAbove i) ≤ 1) ↔ _
        rw [Fin.sum_univ_castSucc]
        simp only [Fin.succAbove_last, add_comm (x (Fin.last n))]
        constructor
        · rintro ⟨hl, h, hs⟩
          refine ⟨fun j => ?_, hs⟩
          rcases Fin.eq_castSucc_or_eq_last j with ⟨i, rfl⟩ | rfl
          · exact h i
          · exact hl
        · rintro ⟨h, hs⟩
          exact ⟨h (Fin.last n), fun i => h i.castSucc, hs⟩
      have hs : MeasurableSet S := by
        rw [← e.image_preimage S, he, ← MeasurableEquiv.preimage_symm]
        exact e.symm.measurable ((BoxPadding.simplex_compact (n + 1)).measurableSet)
      rw [← he, (volume_preserving_piFinSuccAbove
        (fun _ : Fin (n + 1) => ℝ) (Fin.last n)).measure_preimage_equiv S]
      change ((volume : Measure ℝ).prod volume) S = _
      rw [Measure.prod_apply hs]
      have hf (t : ℝ) : volume (Prod.mk t ⁻¹' S) =
          (Icc (0 : ℝ) 1).indicator
            (fun s => ENNReal.ofReal ((1 - s) ^ n) * volume (BoxPadding.simplex n)) t := by
        by_cases ht : t ∈ Icc (0 : ℝ) 1
        · have he' : Prod.mk t ⁻¹' S =
              (AffineMap.homothety (0 : Fin n → ℝ) (1 - t)) '' BoxPadding.simplex n := by
            rw [scaled_simplex (sub_nonneg.mpr ht.2)]
            ext x
            change (0 ≤ t ∧ (∀ i, 0 ≤ x i) ∧ t + ∑ i, x i ≤ 1) ↔
              (∀ i, 0 ≤ x i) ∧ ∑ i, x i ≤ 1 - t
            simp [ht.1, le_sub_iff_add_le, add_comm t]
          rw [he', volume.addHaar_image_homothety, Set.indicator_of_mem ht]
          simp only [Module.finrank_pi, Fintype.card_fin,
            abs_of_nonneg (pow_nonneg (sub_nonneg.mpr ht.2) n)]
        · have he' : Prod.mk t ⁻¹' S = ∅ := by
            apply eq_empty_iff_forall_notMem.mpr
            intro x hx
            change 0 ≤ t ∧ (∀ i, 0 ≤ x i) ∧ t + ∑ i, x i ≤ 1 at hx
            exact ht ⟨hx.1, (le_add_of_nonneg_right
              (Finset.sum_nonneg (fun i _ => hx.2.1 i))).trans hx.2.2⟩
          rw [he', measure_empty, Set.indicator_of_notMem ht]
      simp_rw [hf]
      rw [lintegral_indicator measurableSet_Icc, lintegral_mul_const _ (by fun_prop),
        pow_lintegral, ih, ← ENNReal.ofReal_mul (by positivity), Nat.factorial_succ,
        Nat.cast_mul, Nat.cast_succ, div_mul_div_comm, one_mul]

end SharpOC.Witness1387
