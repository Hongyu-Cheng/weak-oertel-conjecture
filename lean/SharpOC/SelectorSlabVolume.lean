import SharpOC.SimplexCaps

/-! Exact Haar volumes of a barycentric slab and its oblique simplex caps. -/

noncomputable section
open Set MeasureTheory
open scoped ENNReal Pointwise

namespace SharpOC

variable {ι E : Type*} [Fintype ι]
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E]

omit [Fintype ι] in
private theorem measure_coord_le (b : AffineBasis ι ℝ E)
    (μ : Measure E) [Measure.IsAddHaarMeasure μ] (i w : ι) (hiw : i ≠ w)
    (A : Set E) (hA : MeasurableSet A) (hfin : μ A ≠ ∞) (q : ℝ) :
    μ (A ∩ {x | b.coord w x ≤ q}) = μ A - μ (A ∩ {x | q ≤ b.coord w x}) := by
  let H := (affineSpan ℝ ({q} : Set ℝ)).comap (b.coord w)
  have hH : H ≠ ⊤ := by
    intro ht
    have hmem (x : E) : b.coord w x = q :=
      (AffineSubspace.mem_affineSpan_singleton ℝ ℝ).mp
        (show x ∈ H by simp [ht])
    have h₁ := hmem (b w)
    have h₀ := hmem (b i)
    rw [b.coord_apply_eq] at h₁
    rw [b.coord_apply_ne hiw.symm] at h₀
    linarith
  have hae := measure_eq_zero_iff_ae_notMem.mp (μ.addHaar_affineSubspace H hH)
  have heq : A ∩ {x | b.coord w x ≤ q} =ᵐ[μ] A \ (A ∩ {x | q ≤ b.coord w x}) := by
    filter_upwards [hae] with x hx
    have hne : b.coord w x ≠ q := fun h =>
      hx ((AffineSubspace.mem_affineSpan_singleton ℝ ℝ).mpr h)
    simp only [mem_inter_iff, mem_ofPred_eq, mem_sdiff]
    apply propext
    constructor
    · rintro ⟨hAx, hxq⟩
      exact ⟨hAx, fun h => hne (le_antisymm hxq h.2)⟩
    · rintro ⟨hAx, hxq⟩
      exact ⟨hAx, le_of_lt (lt_of_not_ge fun h => hxq ⟨hAx, h⟩)⟩
  rw [measure_congr heq]
  exact measure_sdiff inter_subset_left
    (hA.inter (isClosed_le continuous_const (b.coord w).continuous_of_finiteDimensional).measurableSet).nullMeasurableSet
    (ne_top_of_le_ne_top hfin (measure_mono inter_subset_left))

/-- Exact mass of a closed simplex slab, relative to its full simplex. -/
theorem simplex_slab_measure (b : AffineBasis ι ℝ E)
    (μ : Measure E) [Measure.IsAddHaarMeasure μ] (i w : ι) (hiw : i ≠ w)
    {eps : ℝ} (heps : 0 ≤ eps) (heps1 : eps < 1) :
    μ (convexHull ℝ (range b) ∩ {x | b.coord w x ≤ eps}) =
      ENNReal.ofReal (1 - (1 - eps) ^ Module.finrank ℝ E) * μ (convexHull ℝ (range b)) := by
  have hc := (finite_range b).isCompact_convexHull ℝ
  rw [measure_coord_le b μ i w hiw _ hc.measurableSet hc.measure_ne_top,
    simplex_cap_measure b μ w heps heps1]
  nth_rw 1 [← one_mul (μ (convexHull ℝ (range b)))]
  rw [← ENNReal.sub_mul (fun _ _ => hc.measure_ne_top), ← ENNReal.ofReal_one,
    ENNReal.ofReal_sub 1 (by positivity)]

private theorem simplex_two_caps_measure (b : AffineBasis ι ℝ E)
    (μ : Measure E) [Measure.IsAddHaarMeasure μ] (i w : ι) (hiw : i ≠ w)
    {t q : ℝ} (ht : 0 ≤ t) (hq : 0 ≤ q) (hr : 0 ≤ 1 - t - q) :
    μ ((convexHull ℝ (range b) ∩ {x | t ≤ b.coord i x}) ∩ {x | q ≤ b.coord w x}) =
      ENNReal.ofReal ((1 - t - q) ^ Module.finrank ℝ E) * μ (convexHull ℝ (range b)) := by
  classical
  let r := 1 - t - q
  let a (j : ι) := t * b.coord j (b i) + q * b.coord j (b w)
  let F (x : E) := r • x + (t • b i + q • b w)
  have hcoord (j : ι) (x : E) : b.coord j (F x) = r * b.coord j x + a j := by
    have hd (y : E) : b.coord j y = (b.coord j).linear y + b.coord j 0 :=
      congrFun (b.coord j).decomp y
    dsimp only [a]
    rw [hd (F x), hd x, hd (b i), hd (b w)]
    simp only [F, map_add, map_smul, smul_eq_mul]
    dsimp [r]
    ring
  have ha (j : ι) : 0 ≤ a j := by
    simp only [a, b.coord_apply]
    split_ifs <;> simp [ht, hq, add_nonneg ht hq]
  have hai : a i = t := by simp [a, b.coord_apply_ne hiw]
  have haw : a w = q := by simp [a, b.coord_apply_ne hiw.symm]
  have hs : ∑ j, a j = t + q := by
    simp only [a, Finset.sum_add_distrib, ← Finset.mul_sum, b.sum_coord_apply_eq_one, mul_one]
  have heq : ((convexHull ℝ (range b) ∩ {x | t ≤ b.coord i x}) ∩ {x | q ≤ b.coord w x}) =
      F '' convexHull ℝ (range b) := by
    rw [b.convexHull_eq_nonneg_coord]
    ext x
    change ((∀ j, 0 ≤ b.coord j x) ∧ t ≤ b.coord i x) ∧ q ≤ b.coord w x ↔ _
    constructor
    · rintro ⟨⟨hx, hxi⟩, hxw⟩
      have hxa (j : ι) : a j ≤ b.coord j x := by
        by_cases hj : j = i
        · simpa [hj, hai] using hxi
        by_cases hk : j = w
        · simpa [hk, haw] using hxw
        simpa [a, b.coord_apply_ne hj, b.coord_apply_ne hk] using hx j
      rcases eq_or_lt_of_le hr with hzero | hpos
      · have hz : r = 0 := hzero.symm
        refine ⟨b i, fun j => by rw [b.coord_apply]; split_ifs <;> norm_num, b.ext_elem fun j => ?_⟩
        rw [hcoord, hz, zero_mul, zero_add]
        have hsum : ∑ j, (b.coord j x - a j) = 0 := by
          rw [Finset.sum_sub_distrib, b.sum_coord_apply_eq_one, hs]
          dsimp [r] at hz
          linarith
        exact sub_eq_zero.mp ((Finset.sum_eq_zero_iff_of_nonneg
          (fun j _ => sub_nonneg.mpr (hxa j))).mp hsum j (Finset.mem_univ j))
          |>.symm
      · let y := r⁻¹ • (x - (t • b i + q • b w))
        have hy : F y = x := by
          have hn : r ≠ 0 := hpos.ne'
          simp [F, y, smul_smul, hn]
        refine ⟨y, fun j => nonneg_of_mul_nonneg_right ?_ hpos, hy⟩
        have hj := hcoord j y
        rw [hy] at hj
        linarith [hxa j]
    · rintro ⟨y, hy, rfl⟩
      have hl (j : ι) : a j ≤ b.coord j (F y) := by
        rw [hcoord]
        linarith [mul_nonneg hr (hy j)]
      exact ⟨⟨fun j => (ha j).trans (hl j), hai ▸ hl i⟩, haw ▸ hl w⟩
  rw [heq]
  unfold F
  rw [← image_image (fun x : E => x + (t • b i + q • b w)) (r • ·),
    image_smul, image_add_right, measure_preimage_add_right, μ.addHaar_smul_of_nonneg hr]

/-- Scaling the retained (w)-coordinate by (1-s) transfers its missing mass
to the omitted coordinate (i). The slab makes the original (i)-coordinate
constraint redundant in the transformed cap. -/
theorem simplex_slab_cap_measure (b : AffineBasis ι ℝ E)
    (μ : Measure E) [Measure.IsAddHaarMeasure μ] (i w : ι) (hiw : i ≠ w)
    {s t eps : ℝ} (hs0 : 0 ≤ s) (hs : s < 1) (heps : 0 ≤ eps)
    (hz : 0 ≤ t - s * eps) (ht : 0 ≤ 1 - t - (1 - s) * eps) :
    μ (convexHull ℝ (range b) ∩
        {x | b.coord w x ≤ eps ∧ t ≤ b.coord i x + s * b.coord w x}) =
      ENNReal.ofReal (((1 - t) ^ Module.finrank ℝ E -
          (1 - t - (1 - s) * eps) ^ Module.finrank ℝ E) / (1 - s)) *
        μ (convexHull ℝ (range b)) := by
  classical
  let S := convexHull ℝ (range b)
  let c := 1 - s
  have hc : 0 < c := sub_pos.mpr hs
  have hq : 0 ≤ c * eps := mul_nonneg hc.le heps
  have ht0 : 0 ≤ t := by linarith [mul_nonneg hs0 heps]
  let F (x : E) := x - (s * b.coord w x) • (b w - b i)
  let L := LinearMap.id - s • (b.coord w).linear.smulRight (b w - b i)
  have hcoord (j : ι) (x : E) :
      b.coord j (F x) = b.coord j x -
        s * b.coord w x * (b.coord j (b w) - b.coord j (b i)) := by
    have hv : F x = (-(s * b.coord w x)) • (b w -ᵥ b i) +ᵥ x := by
      simp [F, vadd_eq_add, vsub_eq_sub, sub_eq_add_neg, add_comm]
    rw [hv, AffineMap.map_vadd, map_smul, AffineMap.linearMap_vsub]
    simp [vadd_eq_add, sub_eq_add_neg, add_comm]
  have hw (x : E) : b.coord w (F x) = c * b.coord w x := by
    rw [hcoord, b.coord_apply_eq, b.coord_apply_ne hiw.symm]
    dsimp [c]
    ring
  have hi (x : E) : b.coord i (F x) = b.coord i x + s * b.coord w x := by
    rw [hcoord, b.coord_apply_eq, b.coord_apply_ne hiw]
    ring
  have hj (j : ι) (hji : j ≠ i) (hjw : j ≠ w) (x : E) :
      b.coord j (F x) = b.coord j x := by
    simp [hcoord, b.coord_apply_ne hji, b.coord_apply_ne hjw]
  have hF (x : E) : F x = L (x - b i) + b i := by
    have hl : (b.coord w).linear (x - b i) = b.coord w x := by
      rw [← vsub_eq_sub, AffineMap.linearMap_vsub, b.coord_apply_ne hiw.symm, vsub_eq_sub, sub_zero]
    change x - (s * b.coord w x) • (b w - b i) =
      (x - b i - s • ((b.coord w).linear (x - b i) • (b w - b i))) + b i
    rw [hl, smul_smul]
    abel
  let B := b.basisOf i
  let k : {j : ι // j ≠ i} := ⟨w, hiw.symm⟩
  have hdiag (j : {j : ι // j ≠ i}) :
      L (B j) = (if j = k then c else 1) • B j := by
    change B j - s • ((b.coord w).linear (B j) • (b w - b i)) = _
    by_cases hj : j = k
    · subst j
      have hk : B k = b w - b i := b.basisOf_apply i k
      have hlw : (b.coord w).linear (b w - b i) = 1 := by
        change (b.coord w).linear (b w -ᵥ b i) = 1
        rw [AffineMap.linearMap_vsub, b.coord_apply_eq, b.coord_apply_ne hiw.symm,
          vsub_eq_sub, sub_zero]
      rw [hk, hlw, ite_eq_left rfl, one_smul]
      simp [c, sub_smul]
    · have hjw : w ≠ (j : ι) := fun h => hj (Subtype.ext h.symm)
      have hl : (b.coord w).linear (B j) = 0 := by
        change (b.coord w).linear (b.basisOf i j) = 0
        rw [b.basisOf_apply, AffineMap.linearMap_vsub, b.coord_apply_ne hjw,
          b.coord_apply_ne hiw.symm, vsub_eq_sub, sub_zero]
      rw [hl]
      simp [hj]
  have hdet : LinearMap.det L = c := by
    rw [← LinearMap.det_toMatrix B]
    have hM : LinearMap.toMatrix B B L = Matrix.diagonal (fun j => if j = k then c else 1) := by
      ext a j
      rw [LinearMap.toMatrix_apply, hdiag]
      simp only [map_smul, Module.Basis.repr_self, Finsupp.smul_apply,
        Finsupp.single_apply, smul_eq_mul, Matrix.diagonal_apply]
      by_cases h : a = j <;> simp [h, eq_comm]
    rw [hM, Matrix.det_diagonal, Finset.prod_eq_single k]
    · simp
    · intro j _ hj
      simp [hj]
    · simp
  let A := S ∩ {x | t ≤ b.coord i x}
  let U := S ∩ {x | b.coord w x ≤ eps ∧ t ≤ b.coord i x + s * b.coord w x}
  let D := A ∩ {x | b.coord w x ≤ c * eps}
  have hmem (x : E) : x ∈ U ↔ F x ∈ D := by
    simp only [U, D, A, S, b.convexHull_eq_nonneg_coord, mem_inter_iff, mem_ofPred_eq, hw, hi]
    rw [mul_le_mul_iff_right₀ hc]
    constructor
    · rintro ⟨hx, hxu, hxt⟩
      refine ⟨⟨fun j => ?_, hxt⟩, hxu⟩
      by_cases hji : j = i
      · simpa [hji, hi] using ht0.trans hxt
      by_cases hjw : j = w
      · simpa [hjw, hw] using mul_nonneg hc.le (hx w)
      simpa [hj j hji hjw] using hx j
    · rintro ⟨⟨hx, hxt⟩, hxu⟩
      refine ⟨fun j => ?_, hxu, hxt⟩
      by_cases hji : j = i
      · subst j
        linarith [mul_le_mul_of_nonneg_left hxu hs0]
      by_cases hjw : j = w
      · have hl := hx w
        rw [hw] at hl
        simpa [hjw] using nonneg_of_mul_nonneg_right hl hc
      simpa [hj j hji hjw] using hx j
  have hD : (fun x => x + b i) ⁻¹' D = L '' ((fun x => x + b i) ⁻¹' U) := by
    ext y
    constructor
    · intro hy
      obtain ⟨x, rfl⟩ := (L.equivOfDetNeZero (hdet ▸ hc.ne')).surjective y
      exact ⟨x, (hmem (x + b i)).mpr (by simpa [hF] using hy), rfl⟩
    · rintro ⟨x, hx, rfl⟩
      simpa [hF] using (hmem (x + b i)).mp hx
  have hU : μ U = ENNReal.ofReal c⁻¹ * μ D := by
    have hh := congrArg μ hD
    rw [measure_preimage_add_right, μ.addHaar_image_linearMap, measure_preimage_add_right,
      hdet, abs_of_pos hc] at hh
    rw [hh, ← mul_assoc, ← ENNReal.ofReal_mul (inv_nonneg.mpr hc.le),
      inv_mul_cancel₀ hc.ne', ENNReal.ofReal_one, one_mul]
  have hS := (finite_range b).isCompact_convexHull ℝ
  have hA : IsCompact A :=
    hS.inter_right (isClosed_le continuous_const (b.coord i).continuous_of_finiteDimensional)
  change μ U = _
  rw [hU, measure_coord_le b μ i w hiw A hA.measurableSet hA.measure_ne_top]
  dsimp only [A, S]
  have hfirst := simplex_two_caps_measure b μ i w hiw ht0 (le_refl 0) (by linarith : 0 ≤ 1 - t - 0)
  have hA0 : ((convexHull ℝ (range b) ∩ {x | t ≤ b.coord i x}) ∩
      {x | 0 ≤ b.coord w x}) = convexHull ℝ (range b) ∩ {x | t ≤ b.coord i x} := by
    exact inter_eq_left.mpr fun x hx => (b.convexHull_eq_nonneg_coord ▸ hx.1) w
  rw [hA0, sub_zero] at hfirst
  rw [hfirst, simplex_two_caps_measure b μ i w hiw ht0 hq ht,
    ← ENNReal.sub_mul (fun _ _ => hS.measure_ne_top),
    ← ENNReal.ofReal_sub _ (by positivity : 0 ≤ (1 - t - c * eps) ^ Module.finrank ℝ E),
    ← mul_assoc, ← ENNReal.ofReal_mul (inv_nonneg.mpr hc.le), div_eq_inv_mul]

end SharpOC
