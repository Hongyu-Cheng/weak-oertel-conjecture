import SharpOC.Selector17Sources

/-! A simplex of mass h⁵ supported on the nonpositive side of a selector cut. -/

noncomputable section

namespace SharpOC.Selector17

open Set MeasureTheory
open scoped ENNReal Pointwise
open SelectorSources (E B coordinates source sourceBasis source_eq_hull source_volume
  mem_source_iff_weights mem_B_iff_coordinates forall_fin_three)

private def eta : ℝ := (h / (1 + 2 * delta)) ^ 5

private theorem near_scale_pos : 0 < 1 + 2 * delta := by linarith [delta_pos]

private theorem eta_pos : 0 < eta :=
  pow_pos (div_pos h_pos near_scale_pos) _

private theorem eta_le : eta ≤ a / (1 + a) := by
  norm_num [eta, h, delta, a]

/-- Replace active vertex zero by a point on the edge to active vertex one. -/
private def nearMat : Matrix (Fin 3) (Fin 3) ℝ :=
  !![eta, 0, 0; 1 - eta, 1, 0; 0, 0, 1]

private theorem nearMat_sum (k : Fin 3) : ∑ i, nearMat i k = 1 := by
  fin_cases k <;> norm_num [nearMat, Fin.sum_univ_three]

private theorem nearMat_det : nearMat.det = eta := by
  simp [nearMat, Matrix.det_fin_three]

private theorem nearMat_nonsingular : nearMat.det ≠ 0 := by
  rw [nearMat_det]
  exact eta_pos.ne'

def nearBasis (j : Fin 3) : AffineBasis (Fin 6) ℝ E :=
  scaledTranslatedBasis (sourceBasis j nearMat nearMat_sum nearMat_nonsingular)
    (1 + 2 * delta) 0 near_scale_pos.ne'

def nearFiber (j : Fin 3) : Set E := convexHull ℝ (range (nearBasis j))

theorem nearFiber_eq_hull (j : Fin 3) : nearFiber j = convexHull ℝ (range (nearBasis j)) :=
  rfl

private theorem nearFiber_eq_smul (j : Fin 3) : nearFiber j = (1 + 2 * delta) • source j nearMat := by
  rw [nearFiber, nearBasis, scaledTranslatedBasis_hull, ← source_eq_hull]
  simp only [add_zero, Set.image_smul]

theorem nearFiber_convex (j : Fin 3) : Convex ℝ (nearFiber j) := convex_convexHull ℝ _

theorem nearFiber_compact (j : Fin 3) : IsCompact (nearFiber j) :=
  (Set.finite_range (nearBasis j)).isCompact_convexHull ℝ

theorem nearFiber_nonempty (j : Fin 3) : (nearFiber j).Nonempty :=
  ⟨nearBasis j 0, subset_convexHull ℝ _ (mem_range_self _)⟩

private theorem near_source_subset (j : Fin 3) : source j nearMat ⊆ B ∩ {x | f j x ≤ 0} := by
  let w (z : Fin 3 → ℝ) : Fin 3 → ℝ := ![z 0 / eta, z 1 - (1 - eta) * (z 0 / eta), z 2]
  have hw (z : Fin 3 → ℝ) : nearMat.mulVec (w z) = z := by
    ext i
    fin_cases i <;> simp [nearMat, w, Matrix.mulVec, dotProduct, Fin.sum_univ_three]
    exact mul_div_cancel₀ _ eta_pos.ne'
  intro x hx
  rw [mem_source_iff_weights _ _ nearMat_sum nearMat_nonsingular w hw] at hx
  obtain ⟨hf, hn⟩ := hx
  have h0 : 0 ≤ w (coordinates j x) 0 := hn 0
  have h1 : 0 ≤ w (coordinates j x) 1 := hn 1
  have h2 : 0 ≤ w (coordinates j x) 2 := hn 2
  have he0 : coordinates j x 0 = eta * w (coordinates j x) 0 := by
    simpa [nearMat, Matrix.mulVec, dotProduct, Fin.sum_univ_three] using
      (congrFun (hw (coordinates j x)) 0).symm
  have he1 : coordinates j x 1 =
      (1 - eta) * w (coordinates j x) 0 + w (coordinates j x) 1 := by
    simpa [nearMat, Matrix.mulVec, dotProduct, Fin.sum_univ_three] using
      (congrFun (hw (coordinates j x)) 1).symm
  have hle : eta ≤ a * (1 - eta) := by
    have h := (le_div_iff₀ (by linarith [a_pos] : 0 < 1 + a)).mp eta_le
    linarith
  have heta : 0 ≤ 1 - eta := nonneg_of_mul_nonneg_right (eta_pos.le.trans hle) a_pos
  have hz2 : 0 ≤ coordinates j x 2 := h2
  constructor
  · rw [mem_B_iff_coordinates j x]
    exact ⟨hf, forall_fin_three.mpr ⟨by rw [he0]; exact mul_nonneg eta_pos.le h0,
      by rw [he1]; exact add_nonneg (mul_nonneg heta h0) h1, hz2⟩⟩
  · change f j x ≤ 0
    rw [show f j x = coordinates j x 0 - a * coordinates j x 1 - (1 - a) * coordinates j x 2 by
      simpa [coordinates] using f_apply j x]
    rw [he0, he1]
    nlinarith [mul_le_mul_of_nonneg_right hle h0, mul_nonneg a_pos.le h1,
      mul_nonneg (sub_nonneg.mpr a_lt_one.le) hz2]

theorem nearFiber_subset_roof (j : Fin 3) : nearFiber j ⊆ (1 + 2 * delta) • B := by
  rw [nearFiber_eq_smul]
  exact smul_set_mono ((near_source_subset j).trans inter_subset_left)

theorem nearFiber_f_nonpos (j : Fin 3) {x : E} (hx : x ∈ nearFiber j) : f j x ≤ 0 := by
  rw [nearFiber_eq_smul] at hx
  obtain ⟨y, hy, rfl⟩ := hx
  rw [map_smul, smul_eq_mul]
  exact mul_nonpos_of_nonneg_of_nonpos near_scale_pos.le (near_source_subset j hy).2

theorem nearFiber_volume (j : Fin 3) :
    volume (nearFiber j) = ENNReal.ofReal (h ^ 5) * volume B := by
  rw [nearFiber_eq_smul, Measure.addHaar_smul_of_nonneg volume near_scale_pos.le,
    source_volume _ _ nearMat_sum, nearMat_det, abs_of_pos eta_pos, ← mul_assoc,
    ← ENNReal.ofReal_mul (pow_nonneg near_scale_pos.le _)]
  congr 2
  have hdim : Module.finrank ℝ E = 5 := by simp [E]
  rw [hdim, eta, ← mul_pow, mul_div_cancel₀]
  exact near_scale_pos.ne'

end SharpOC.Selector17
