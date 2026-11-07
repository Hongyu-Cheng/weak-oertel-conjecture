import SharpOC.BodyGeometry

/-! Closed free-coordinate boxes and their exact grouped containment. -/

noncomputable section
open Set Finset

namespace SharpOC.BoxGeometry

variable {ι κ : Type*} [Fintype ι] [DecidableEq κ]

def box (r : ℝ) : Set (ι → ℝ) := {x | ∀ i, -r ≤ x i ∧ x i ≤ r}

theorem box_eq_Icc (r : ℝ) :
    box (ι := ι) r = Set.Icc (fun _ => -r) (fun _ => r) := by
  ext x
  simp [box, Set.mem_Icc, Pi.le_def, forall_and]

theorem box_compact (r : ℝ) : IsCompact (box (ι := ι) r) := by
  rw [box_eq_Icc]
  exact isCompact_Icc

theorem box_convex (r : ℝ) : Convex ℝ (box (ι := ι) r) := by
  rw [box_eq_Icc]
  exact convex_Icc _ _

theorem zero_mem_box {r : ℝ} (hr : 0 ≤ r) : (0 : ι → ℝ) ∈ box r := by
  intro i
  constructor <;> simpa using hr

theorem box_nonempty {r : ℝ} (hr : 0 ≤ r) : (box (ι := ι) r).Nonempty :=
  ⟨0, zero_mem_box hr⟩

theorem zero_mem_interior_box {r : ℝ} (hr : 0 < r) :
    (0 : ι → ℝ) ∈ interior (box r) := by
  rw [mem_interior_iff_mem_nhds]
  apply Metric.mem_nhds_iff.mpr
  refine ⟨r, hr, ?_⟩
  intro x hx i
  have hnorm : ‖x‖ < r := by simpa only [Metric.mem_ball, dist_zero_right] using hx
  have hi := (pi_norm_lt_iff hr).mp hnorm i
  rw [Real.norm_eq_abs] at hi
  exact ⟨(abs_lt.mp hi).1.le, (abs_lt.mp hi).2.le⟩

theorem box_interior_nonempty {r : ℝ} (hr : 0 < r) :
    (interior (box (ι := ι) r)).Nonempty := ⟨0, zero_mem_interior_box hr⟩

theorem box_mono {r s : ℝ} (hrs : r ≤ s) : box (ι := ι) r ⊆ box s := by
  intro x hx i
  exact ⟨(neg_le_neg hrs).trans (hx i).1, (hx i).2.trans hrs⟩

theorem add_sum_mem_box (I : Finset κ) {r u : ℝ} {x : ι → ℝ}
    (hx : x ∈ box r) (v : κ → ι → ℝ) (hv : ∀ i ∈ I, v i ∈ box u) :
    x + ∑ i ∈ I, v i ∈ box (r + (I.card : ℝ) * u) := by
  intro j
  have hlo : -(I.card : ℝ) * u ≤ ∑ i ∈ I, v i j := by
    calc
      -(I.card : ℝ) * u = ∑ _i ∈ I, -u := by simp
      _ ≤ ∑ i ∈ I, v i j := Finset.sum_le_sum (fun i hi => (hv i hi j).1)
  have hhi : ∑ i ∈ I, v i j ≤ (I.card : ℝ) * u := by
    calc
      _ ≤ ∑ _i ∈ I, u := Finset.sum_le_sum (fun i hi => (hv i hi j).2)
      _ = _ := by simp
  simp only [Pi.add_apply, Finset.sum_apply]
  constructor <;> linarith [(hx j).1, (hx j).2]

/-- The free-coordinate part of the origin grouping. -/
theorem box_grouped_containment (I : Finset κ) (hI : I.Nonempty)
    {q : ℝ} (hq : (1 : ℝ) / 2 ≤ q)
    {x : ι → ℝ} (hx : x ∈ box (2 * q))
    (v : κ → ι → ℝ) (hv : ∀ i ∈ I, v i ∈ box (2 * (1 - q))) :
    ∃ b ∈ box (ι := ι) 1,
      x + ∑ i ∈ I, v i = ((I.card : ℝ) + 1) • b := by
  have hk : (1 : ℝ) ≤ I.card := by exact_mod_cast Finset.card_pos.mpr hI
  have hc : 0 < (I.card : ℝ) + 1 := by positivity
  have hbound : 2 * q + (I.card : ℝ) * (2 * (1 - q)) ≤ (I.card : ℝ) + 1 := by
    nlinarith [mul_nonneg (sub_nonneg.mpr hk) (show 0 ≤ 2 * q - 1 by linarith)]
  have hs := add_sum_mem_box I hx v hv
  have hs' := box_mono hbound hs
  refine ⟨((I.card : ℝ) + 1)⁻¹ • (x + ∑ i ∈ I, v i), ?_, ?_⟩
  · intro j
    change -1 ≤ ((I.card : ℝ) + 1)⁻¹ * (x + ∑ i ∈ I, v i) j ∧
      ((I.card : ℝ) + 1)⁻¹ * (x + ∑ i ∈ I, v i) j ≤ 1
    have hlo := mul_le_mul_of_nonneg_left (hs' j).1 (inv_nonneg.mpr hc.le)
    have hhi := mul_le_mul_of_nonneg_left (hs' j).2 (inv_nonneg.mpr hc.le)
    simpa only [mul_neg, inv_mul_cancel₀ hc.ne', neg_one_mul] using And.intro hlo hhi
  · rw [smul_smul, mul_inv_cancel₀ hc.ne', one_smul]

end SharpOC.BoxGeometry
