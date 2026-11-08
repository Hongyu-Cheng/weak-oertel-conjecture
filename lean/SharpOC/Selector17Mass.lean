import SharpOC.Selector17Body
import SharpOC.Selector17Cap
import SharpOC.SelectorMeasure

/-! Exact mixed-integer volume and isolated covering cuts on large fibers. -/

noncomputable section

namespace SharpOC.Selector17

open Set MeasureTheory
open SelectorSources (E B basis B_volume_pos B_volume_ne_top)
open Selector (mixedIntegerMass mixedIntegerMass_body_toReal mixedIntegerMass_closedCut_toReal)
open scoped BigOperators ENNReal Pointwise

theorem B_volume_real_pos : 0 < (volume B).toReal :=
  ENNReal.toReal_pos B_volume_pos.ne' B_volume_ne_top

private theorem volume_smul_real (r : ℝ) (hr : 0 ≤ r) (S : Set E) :
    (volume (r • S)).toReal = r ^ 5 * (volume S).toReal := by
  rw [Measure.addHaar_smul_of_nonneg volume hr, ENNReal.toReal_mul]
  simp [E, ENNReal.toReal_ofReal (pow_nonneg hr _)]

theorem heavy_volume (S : ↥heavyMasks) :
    (volume (fiber (some (.inl S)))).toReal =
      if S.val ∈ balancedMasks then (1 + delta)^5 * V * (volume B).toReal
      else h^5 * (volume B).toReal := by
  simp only [fiber]
  split_ifs
  · rw [volume_smul_real _ (by linarith [delta_pos]), K_volume, ENNReal.toReal_mul,
      ENNReal.toReal_ofReal V_nonneg, mul_assoc]
  · cases nearType S with
    | none => exact volume_smul_real h h_pos.le B
    | some j =>
      rw [nearFiber_volume, ENNReal.toReal_mul, ENNReal.toReal_ofReal (pow_nonneg h_pos.le 5)]

theorem light_volume (j : Fin 3) (J : ↥lightMasks) :
    (volume (fiber (some (.inr (j, J))))).toReal =
      ((theta + phi) * (1 - delta)^5) * (volume B).toReal := by
  change (volume ((1 - delta) • T j)).toReal = _
  rw [volume_smul_real _ (sub_nonneg.mpr delta_lt_one.le), T_volume, ENNReal.toReal_mul,
    ENNReal.toReal_ofReal (add_nonneg theta_pos.le phi_pos.le)]
  ring

theorem body_mass : (mixedIntegerMass body).toReal = W * (volume B).toReal := by
  rw [mixedIntegerMass_body_toReal integerBase integerBase_injective integer_base_census
    fiber integer_fiber_exact fiber_compact, Fintype.sum_option, Fintype.sum_sum_type,
    Fintype.sum_prod_type]
  simp_rw [heavy_volume, light_volume]
  rw [Finset.sum_ite]
  simp only [fiber, Finset.sum_const, nsmul_eq_mul, balanced_heavy_count, unbalanced_heavy_count,
    Finset.card_univ, Fintype.card_coe, lightMasks_card, Fintype.card_fin, W, L]
  ring

theorem body_mass_pos : 0 < (mixedIntegerMass body).toReal := by
  rw [body_mass]
  exact mul_pos W_pos B_volume_real_pos

theorem body_mass_finite : mixedIntegerMass body ≠ ⊤ := by
  intro htop
  simpa [htop] using body_mass_pos

theorem body_mass_ne_zero : mixedIntegerMass body ≠ 0 := by
  intro hz
  simpa [hz] using body_mass_pos

theorem actual_cut_mass (F : Ambient → ℝ) (a₀ : ℝ) :
    (mixedIntegerMass (body ∩ {p | a₀ ≤ F p})).toReal =
      ∑ i, (volume (fiber i ∩ {x | a₀ ≤ F (base i, x)})).toReal := by
  rw [mixedIntegerMass_closedCut_toReal integerBase integerBase_injective integer_base_census
    fiber integer_fiber_exact fiber_compact F a₀]
  simp only [integerBase_cast]

/-- The mixed-integer mass of an isolated cap is precisely its continuous mass. -/
private theorem isolate_cut (i : FiberIndex) (hi : i ≠ none) (x : E)
    (g : E →L[ℝ] ℝ) (hg : g ≠ 0) (a₀ : ℝ) (hx : a₀ ≤ g x) :
    ∃ F : Ambient →L[ℝ] ℝ, ∃ b : ℝ, F ≠ 0 ∧ b ≤ F (base i, x) ∧
      (mixedIntegerMass (body ∩ {p | b ≤ F p})).toReal =
        (volume (fiber i ∩ {y | a₀ ≤ g y})).toReal := by
  classical
  obtain ⟨ell, hell⟩ := base_exposed i hi
  obtain ⟨F, b, hF, htrace, hother⟩ :=
    exposed_fiber_cut base fiber fiber_compact i ell.toContinuousLinearMap hell g hg a₀
  refine ⟨F, b, hF, (htrace x).mp hx, ?_⟩
  rw [actual_cut_mass, Finset.sum_eq_single i]
  · congr 2
    ext y
    exact and_congr_right (fun _ => (htrace y).symm)
  · intro j _ hji
    have he : fiber j ∩ {y | b ≤ F (base j, y)} = ∅ :=
      eq_empty_iff_forall_notMem.mpr (fun y ⟨hy, hc⟩ => (hother j hji y hy).not_ge hc)
    simp [he]
  · simp

set_option maxRecDepth 4096 in
theorem heavy_small_cut (S : ↥heavyMasks) (x : E)
    (hx : x ∈ fiber (some (.inl S))) :
    ∃ F : Ambient →L[ℝ] ℝ, ∃ b : ℝ, F ≠ 0 ∧ b ≤ F (base (some (.inl S)), x) ∧
      (mixedIntegerMass (body ∩ {p | b ≤ F p})).toReal ≤
        gamma * h^5 * (volume B).toReal := by
  let idx : FiberIndex := some (.inl S)
  change x ∈ fiber idx at hx
  by_cases hS : S.val ∈ balancedMasks
  · let j := selectedType S.val
    let r := 1 + delta
    have hr : 0 < r := by dsimp [r]; linarith [delta_pos]
    have hf : fiber idx = r • K j := by simp [idx, fiber, hS, r, j]
    rw [hf] at hx
    obtain ⟨y, hy, rfl⟩ := hx
    obtain ⟨i, hi⟩ := thresholds_cover j y
    let coord := (uBasis j).coord i
    let g := coord.linear.toContinuousLinearMap
    let a₀ := r * (t i - coord 0)
    have hg : g ≠ 0 := by
      intro hz
      apply simplex_coord_linear_ne_zero (d := 5) (by decide) (uBasis j) i
      apply LinearMap.ext
      intro v
      exact congrArg (fun G : E →L[ℝ] ℝ => G v) hz
    have htest (v : E) : a₀ ≤ g (r • v) ↔ t i ≤ coord v := by
      have hc : coord v = g v + coord 0 := congrFun coord.decomp v
      rw [map_smul, smul_eq_mul]
      change r * (t i - coord 0) ≤ r * g v ↔ t i ≤ coord v
      rw [mul_le_mul_iff_right₀ hr, hc]
      constructor <;> intro h <;> linarith
    obtain ⟨F, b, hF, hb, hmass⟩ := isolate_cut idx (by simp [idx]) (r • y) g hg a₀
      ((htest y).2 hi)
    refine ⟨F, b, hF, hb, ?_⟩
    have he : fiber idx ∩ {v | a₀ ≤ g v} = r • (K j ∩ {v | t i ≤ coord v}) := by
      rw [hf]
      ext v
      constructor
      · rintro ⟨⟨w, hw, rfl⟩, hc⟩
        exact ⟨w, ⟨hw, (htest w).1 hc⟩, rfl⟩
      · rintro ⟨w, ⟨hw, hc⟩, rfl⟩
        exact ⟨⟨w, hw, rfl⟩, (htest w).2 hc⟩
    rw [hmass, he, volume_smul_real _ hr.le, K_cap_volume, ENNReal.toReal_mul,
      ENNReal.toReal_ofReal (C_nonneg i), ← mul_assoc]
    exact mul_le_mul_of_nonneg_right (heavy_cap_slack i).le B_volume_real_pos.le
  · have hsimp : ∃ b : AffineBasis (Fin 6) ℝ E, fiber idx = convexHull ℝ (range b) := by
      cases hn : nearType S with
      | none =>
        let b := scaledTranslatedBasis basis h (0 : E) h_pos.ne'
        exact ⟨b, by simp only [idx, fiber, ite_eq_right hS, hn, b, scaledTranslatedBasis_hull,
          add_zero, Set.image_smul, B]⟩
      | some j =>
        exact ⟨nearBasis j, by simp only [idx, fiber, ite_eq_right hS, hn, nearFiber_eq_hull]⟩
    obtain ⟨b, hB⟩ := hsimp
    obtain ⟨g, a₀, hg, ha₀, hcap⟩ :=
      simplex_small_halfspace (d := 5) (by decide) b volume (by simp) x
    obtain ⟨F, c, hF, hc, hmass⟩ := isolate_cut idx (by simp [idx]) x g hg a₀ ha₀
    refine ⟨F, c, hF, hc, ?_⟩
    rw [hmass, hB, hcap, ← hB, ENNReal.toReal_mul, ENNReal.toReal_ofReal (by positivity)]
    change _ * (volume (fiber (some (.inl S)))).toReal ≤ _
    rw [heavy_volume, ite_eq_right hS, mul_assoc]
    norm_num [gamma]

end SharpOC.Selector17
