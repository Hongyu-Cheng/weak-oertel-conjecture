import Mathlib.Analysis.Convex.Combination
import Mathlib.Analysis.Normed.Affine.AddTorsorBases
import Mathlib.MeasureTheory.Measure.Lebesgue.EqHaar
import Mathlib.Tactic

/-!
Every point of a full simplex admits a proper ambient halfspace cap of
at most the sharp simplex fraction. The proof works with any additive
Haar measure, so its normalization is irrelevant.
-/

noncomputable section
open Set MeasureTheory
open scoped ENNReal

namespace SharpOC

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]

omit [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] in
private theorem affine_homothety_coord {ι : Type*}
    (b : AffineBasis ι ℝ E) (i j : ι) (r : ℝ) (x : E) :
    b.coord j (AffineMap.homothety (b i) r x) =
      r * (b.coord j x - b.coord j (b i)) + b.coord j (b i) := by
  rw [AffineMap.homothety_apply, AffineMap.map_vadd, map_smul,
    AffineMap.linearMap_vsub]
  rfl

omit [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] in
/-- A barycentric cap is exactly a homothetic copy of the simplex. -/
theorem simplex_cap_homothety {ι : Type*} (b : AffineBasis ι ℝ E)
    (i : ι) {a : ℝ} (ha : 0 ≤ a) (ha1 : a < 1) :
    convexHull ℝ (range b) ∩ {x | a ≤ b.coord i x} =
      AffineMap.homothety (b i) (1 - a) '' convexHull ℝ (range b) := by
  classical
  have hr : 0 < 1 - a := sub_pos.mpr ha1
  rw [b.convexHull_eq_nonneg_coord]
  ext x
  constructor
  · rintro ⟨hx, hxi⟩
    refine ⟨AffineMap.homothety (b i) (1 - a)⁻¹ x, ?_, ?_⟩
    · intro j
      rw [affine_homothety_coord]
      by_cases hji : j = i
      · subst j
        simp only [b.coord_apply_eq]
        have hh : 0 ≤ (b.coord i x - a) / (1 - a) :=
          div_nonneg (sub_nonneg.mpr hxi) hr.le
        convert hh using 1
        field_simp
        ring
      · rw [b.coord_apply_ne hji]
        simp only [sub_zero, add_zero]
        exact mul_nonneg (inv_nonneg.mpr hr.le) (hx j)
    · rw [← AffineMap.homothety_mul_apply, mul_inv_cancel₀ hr.ne']
      simp
  · rintro ⟨y, hy, rfl⟩
    constructor
    · intro j
      rw [affine_homothety_coord]
      by_cases hji : j = i
      · subst j
        rw [b.coord_apply_eq]
        nlinarith [mul_nonneg hr.le (hy i)]
      · rw [b.coord_apply_ne hji]
        simp only [sub_zero, add_zero]
        exact mul_nonneg hr.le (hy j)
    · change a ≤ b.coord i (AffineMap.homothety (b i) (1 - a) y)
      rw [affine_homothety_coord, b.coord_apply_eq]
      nlinarith [mul_nonneg hr.le (hy i)]

/-- Exact cap volume for any Haar normalization. -/
theorem simplex_cap_measure {ι : Type*} (b : AffineBasis ι ℝ E)
    (μ : Measure E) [Measure.IsAddHaarMeasure μ]
    (i : ι) {a : ℝ} (ha : 0 ≤ a) (ha1 : a < 1) :
    μ (convexHull ℝ (range b) ∩ {x | a ≤ b.coord i x}) =
      ENNReal.ofReal ((1 - a) ^ Module.finrank ℝ E) *
        μ (convexHull ℝ (range b)) := by
  rw [simplex_cap_homothety b i ha ha1, μ.addHaar_image_homothety,
    abs_of_nonneg (pow_nonneg (sub_pos.mpr ha1).le _)]

omit [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] in
/-- Some barycentric coordinate is at least the reciprocal of the number
of vertices. No premise about centroids is required. -/
theorem simplex_large_coordinate {d : ℕ}
    (b : AffineBasis (Fin (d + 1)) ℝ E) (x : E) :
    ∃ i, (1 : ℝ) / (d + 1) ≤ b.coord i x := by
  by_contra hx
  push Not at hx
  have hsum := Finset.sum_lt_sum_of_nonempty (Finset.univ_nonempty)
    (fun i (_ : i ∈ Finset.univ) => hx i)
  rw [b.sum_coord_apply_eq_one] at hsum
  have hconst : (∑ _i : Fin (d + 1), (1 : ℝ) / (d + 1)) = 1 := by
    simp only [Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul,
      Nat.cast_add, Nat.cast_one]
    field_simp
  rw [hconst] at hsum
  exact (lt_irrefl 1) hsum

omit [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] in
/-- The linear part of a barycentric coordinate is nonzero as soon as
there is more than one vertex. -/
theorem simplex_coord_linear_ne_zero {d : ℕ} (hd : 0 < d)
    (b : AffineBasis (Fin (d + 1)) ℝ E) (i : Fin (d + 1)) :
    (b.coord i).linear ≠ 0 := by
  classical
  have : Nontrivial (Fin (d + 1)) := Fin.nontrivial_iff_two_le.mpr (by omega)
  obtain ⟨j, hji⟩ := exists_ne i
  intro h
  have hh := (b.coord i).linearMap_vsub (b i) (b j)
  rw [h, LinearMap.zero_apply, b.coord_apply_eq,
    b.coord_apply_ne hji.symm] at hh
  norm_num at hh

/-- Every point of a full simplex admits an actual nonzero continuous
linear halfspace with the sharp simplex fraction of its Haar measure. -/
theorem simplex_small_halfspace {d : ℕ} (hd : 0 < d)
    (b : AffineBasis (Fin (d + 1)) ℝ E)
    (μ : Measure E) [Measure.IsAddHaarMeasure μ]
    (hdim : Module.finrank ℝ E = d) (x : E) :
    ∃ h : E →L[ℝ] ℝ, ∃ t : ℝ, h ≠ 0 ∧ t ≤ h x ∧
      μ (convexHull ℝ (range b) ∩ {y | t ≤ h y}) =
        ENNReal.ofReal (((d : ℝ) / (d + 1)) ^ d) *
          μ (convexHull ℝ (range b)) := by
  obtain ⟨i, hi⟩ := simplex_large_coordinate b x
  let h : E →L[ℝ] ℝ := (b.coord i).linear.toContinuousLinearMap
  let t : ℝ := (1 : ℝ) / (d + 1) - b.coord i 0
  have hcoord (y : E) : b.coord i y = h y + b.coord i 0 := by
    exact congrFun (b.coord i).decomp y
  refine ⟨h, t, ?_, ?_, ?_⟩
  · intro hh
    apply simplex_coord_linear_ne_zero hd b i
    ext y
    have hy := congrArg (fun H : E →L[ℝ] ℝ => H y) hh
    exact hy
  · dsimp [t]
    rw [hcoord] at hi
    linarith
  · have hset : {y | t ≤ h y} = {y | (1 : ℝ) / (d + 1) ≤ b.coord i y} := by
      ext y
      change (1 / (d + 1) - b.coord i 0 ≤ h y) ↔ 1 / (d + 1) ≤ b.coord i y
      rw [hcoord y]
      constructor <;> intro hy <;> linarith
    rw [hset, simplex_cap_measure b μ i (by positivity) ?_, hdim]
    · congr 3
      field_simp
      ring
    · have hd' : (0 : ℝ) < d := Nat.cast_pos.mpr hd
      apply (div_lt_one (by positivity : (0 : ℝ) < d + 1)).mpr
      linarith

end SharpOC
