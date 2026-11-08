import SharpOC.Witness1387.Body
import SharpOC.Witness1387.Faces
import SharpOC.Witness1387.Sources

/-! Geometry of an active fiber on its supporting slice. -/

noncomputable section

namespace SharpOC.Witness1387

open Set MeasureTheory
open scoped ENNReal Pointwise

private theorem dilate_dilate (a b : ℝ) (S : Set E) :
    dilate a (dilate b S) = dilate (a * b) S := by
  simp only [dilate, image_image, smul_smul]

private theorem dilate_subset_of_subset (r : ℝ) {S U : Set E} (h : S ⊆ U) :
    dilate r S ⊆ dilate r U := image_mono h

private theorem dilate_B_mono {r s : ℝ} (hr : 0 ≤ r) (hs : 0 < s) (hrs : r ≤ s) :
    dilate r B ⊆ dilate s B := by
  rintro _ ⟨y, hy, rfl⟩
  refine ⟨(r / s) • y, B_convex.smul_mem_of_zero_mem
    (interior_subset zero_mem_interior_B) hy
    ⟨div_nonneg hr hs.le, (div_le_one hs).mpr hrs⟩, ?_⟩
  change s • ((r / s) • y) = r • y
  rw [smul_smul]
  congr 1
  field_simp [hs.ne']

/-- Once a supporting slice has the stated integer roles, its affine guard
envelope proves exact equality of the actual and prescribed center fibers. -/
theorem active_fiber_eq_of_slice
    (b : Baseline) (ell guard : (Coordinate → ℝ) →ₗ[ℝ] ℝ)
    (hne : ∀ i, (source i).Nonempty)
    (hcenter : source (.inl b) = dilate (radius (poolIndex b) : ℝ) B)
    (hzero : guard (base (.inl b)) = 0)
    (hface : ∀ a, ell (base a) ≤ ell (base (.inl b)))
    (hroles : ∀ a, ell (base a) = ell (base (.inl b)) →
      a = .inl b ∨
        (1 ≤ guard (base a) ∧ ∃ j, source a = T j) ∨
        (guard (base a) = -1 ∧
          ∃ j, source a = dilate (2 * (radius (poolIndex b) : ℝ) - 1) (T j))) :
    {x | (base (.inl b), x) ∈ body} = source (.inl b) := by
  let r : ℝ := radius (poolIndex b)
  have hpos : 0 < 2 * r - 1 := by
    dsimp only [r]
    exact_mod_cast (by linarith [radius_half_lt (poolIndex b)] :
      (0 : ℚ) < 2 * radius (poolIndex b) - 1)
  have hr : 0 < r := by linarith
  have hr1 : r < 1 := by
    change (radius (poolIndex b) : ℝ) < 1
    exact_mod_cast radius_lt_one (poolIndex b)
  let u : (Coordinate → ℝ) →ₗ[ℝ] ℝ := ((1 - r) / r) • guard
  have hformula (a : SupportIndex) :
      r * (1 + u (base a) - u (base (.inl b))) = r + (1 - r) * guard (base a) := by
    simp only [u, LinearMap.smul_apply, smul_eq_mul, hzero, mul_zero, sub_zero]
    field_simp [hr.ne']
    <;> ring
  rw [body_eq_source_hull]
  letI : Fintype SupportIndex := Fintype.ofFinite _
  apply fiber_eq_from_affine_roof base source (.inl b) source_convex hne ell u hface
  · intro a ha
    apply nonneg_of_mul_nonneg_right _ hr
    rw [hformula]
    rcases hroles a ha with rfl | ⟨hg, _⟩ | ⟨hg, _⟩
    · simp [hzero, hr.le]
    · exact add_nonneg hr.le (mul_nonneg (sub_nonneg.mpr hr1.le) (by linarith))
    · rw [hg]
      linarith
  · intro a ha x hx
    let q := 1 + u (base a) - u (base (.inl b))
    have hmem : x ∈ dilate q (source (.inl b)) := by
      rw [hcenter]
      change x ∈ dilate q (dilate r B)
      rw [dilate_dilate, mul_comm q r, hformula]
      rcases hroles a ha with rfl | ⟨hg, j, hj⟩ | ⟨hg, j, hj⟩
      · rw [hzero, mul_zero, add_zero]
        simpa [hcenter] using hx
      · rw [hj] at hx
        have hs : 1 ≤ r + (1 - r) * guard (base a) := by
          nlinarith [mul_nonneg (sub_nonneg.mpr hr1.le) (sub_nonneg.mpr hg)]
        exact dilate_B_mono zero_le_one (zero_lt_one.trans_le hs) hs
          ⟨x, T_subset_B j hx, one_smul ℝ x⟩
      · rw [hj] at hx
        rw [hg, mul_neg_one, sub_eq_add_neg]
        convert dilate_subset_of_subset (2 * r - 1) (T_subset_B j) hx using 1
        congr 1
        ring
    rcases hmem with ⟨y, hy, heq⟩
    exact ⟨y, hy, heq.symm⟩

theorem dilated_center_row_volume {r : ℝ} (hr : 0 < r) (j : Fin 4) :
    volume (dilate r B ∩ {x | 0 ≤ f j x}) =
      ENNReal.ofReal ((27 / 64 : ℝ) * r ^ 1178) * volume B := by
  have he : dilate r B ∩ {x | 0 ≤ f j x} = dilate r (B ∩ {x | 0 ≤ f j x}) := by
    ext x
    constructor
    · rintro ⟨⟨y, hy, rfl⟩, hf⟩
      change 0 ≤ f j (r • y) at hf
      rw [map_smul, smul_eq_mul] at hf
      exact ⟨y, ⟨hy, nonneg_of_mul_nonneg_right hf hr⟩, rfl⟩
    · rintro ⟨y, ⟨hy, hf⟩, rfl⟩
      exact ⟨⟨y, hy, rfl⟩, by simpa [map_smul, smul_eq_mul] using mul_nonneg hr.le hf⟩
  rw [he, dilate_volume hr.le, cap_volume, ← mul_assoc, ← ENNReal.ofReal_mul (by positivity)]
  ring_nf

end SharpOC.Witness1387
