import SharpOC.AffineSimplex

/-! The centered five-simplex and the continuous sources for the signed selector. -/

noncomputable section
open Set MeasureTheory
open scoped ENNReal

namespace SharpOC.SelectorSources

open MiddleSimplex (standardBasis standardVertex standardVertex_range
  standardBasis_coord_castSucc standardBasis_coord_last)
open SourceGeometry (chartBasis chartBasis_hull chartSimplex standardSimplex
  volume_chartSimplex volume_translate)

abbrev E := Fin 5 → ℝ

def shift : E := fun _ => -(1 / 6 : ℝ)

def basis : AffineBasis (Fin 6) ℝ E := shift +ᵥ standardBasis 5

def B : Set E := convexHull ℝ (range basis)

def lambda (i : Fin 6) : E →ᵃ[ℝ] ℝ := basis.coord i

theorem lambda_castSucc (i : Fin 5) (x : E) :
    lambda i.castSucc x = x i + 1 / 6 := by
  simp [lambda, basis, AffineBasis.coord_vadd, standardBasis_coord_castSucc, shift, add_comm]

theorem lambda_last (x : E) : lambda (Fin.last 5) x = 1 / 6 - ∑ i, x i := by
  change ((shift +ᵥ standardBasis 5).coord (Fin.last 5)) x = _
  rw [AffineBasis.coord_vadd]
  change (standardBasis 5).coord (Fin.last 5) (-shift + x) = _
  rw [standardBasis_coord_last]
  simp [shift, Finset.sum_add_distrib]
  ring

@[simp] theorem lambda_zero (i : Fin 6) : lambda i 0 = 1 / 6 := by
  rcases Fin.eq_castSucc_or_eq_last i with ⟨i, rfl⟩ | rfl
  · rw [lambda_castSucc]; simp
  · rw [lambda_last]; simp

theorem lambda_sum (x : E) : ∑ i, lambda i x = 1 := basis.sum_coord_apply_eq_one x

theorem B_eq_nonneg_lambda : B = {x | ∀ i, 0 ≤ lambda i x} :=
  basis.convexHull_eq_nonneg_coord

theorem B_lambda_nonneg {x : E} (hx : x ∈ B) (i : Fin 6) : 0 ≤ lambda i x := by
  rw [B_eq_nonneg_lambda] at hx
  exact hx i

theorem B_lambda_le_one {x : E} (hx : x ∈ B) (i : Fin 6) : lambda i x ≤ 1 := by
  have h := Finset.single_le_sum (fun k _ => B_lambda_nonneg hx k) (Finset.mem_univ i)
  rwa [lambda_sum] at h

theorem B_compact : IsCompact B := (Set.finite_range basis).isCompact_convexHull ℝ

theorem B_convex : Convex ℝ B := convex_convexHull ℝ _

theorem zero_mem_interior_B : (0 : E) ∈ interior B := by
  rw [B, basis.interior_convexHull]
  intro i
  change 0 < lambda i 0
  rw [lambda_zero]
  norm_num

theorem B_volume_pos : 0 < volume B :=
  Measure.measure_pos_of_nonempty_interior volume ⟨0, zero_mem_interior_B⟩

theorem B_volume_ne_top : volume B ≠ ⊤ := B_compact.measure_ne_top

theorem B_volume : volume B = volume (standardSimplex 5) := by
  unfold B standardSimplex
  rw [← standardVertex_range]
  have hr : range basis = (fun x => shift + x) '' range (standardVertex 5) := by
    rw [← Set.range_comp]
    rfl
  rw [hr]
  have h := (AffineEquiv.constVAdd ℝ E shift).toAffineMap.image_convexHull
    (range (standardVertex 5))
  change (fun x => shift + x) '' convexHull ℝ (range (standardVertex 5)) =
    convexHull ℝ ((fun x => shift + x) '' range (standardVertex 5)) at h
  rw [← h, volume_translate]

/-- The active barycentric coordinates are the first three. -/
def active (j : Fin 3) : Fin 6 := Fin.castAdd 3 j

def f (j : Fin 3) : E →L[ℝ] ℝ :=
  ((lambda (active j)).linear - (2 / 3 : ℝ) • (lambda (active (j + 1))).linear -
    (1 / 3 : ℝ) • (lambda (active (j + 2))).linear).toContinuousLinearMap

theorem f_apply (j : Fin 3) (x : E) :
    f j x = lambda (active j) x - (2 / 3) * lambda (active (j + 1)) x -
      (1 / 3) * lambda (active (j + 2)) x := by
  have h (i : Fin 6) := congrFun (lambda i).decomp x
  simp only [Pi.add_apply, lambda_zero] at h
  change (lambda (active j)).linear x - (2 / 3) * (lambda (active (j + 1))).linear x -
    (1 / 3) * (lambda (active (j + 2))).linear x = _
  linarith [h (active j), h (active (j + 1)), h (active (j + 2))]

theorem f_nonzero (j : Fin 3) : f j ≠ 0 := by
  intro hz
  have h := congrArg (fun g : E →L[ℝ] ℝ => g (basis (active j))) hz
  have h1 : active (j + 1) ≠ active j := by fin_cases j <;> decide
  have h2 : active (j + 2) ≠ active j := by fin_cases j <;> decide
  rw [f_apply] at h
  norm_num [lambda, basis.coord_apply_ne h1, basis.coord_apply_ne h2] at h

theorem B_f_bounds {x : E} (hx : x ∈ B) (j : Fin 3) : -1 ≤ f j x ∧ f j x ≤ 1 := by
  rw [f_apply]
  constructor <;>
    linarith [B_lambda_nonneg hx (active j), B_lambda_le_one hx (active j),
      B_lambda_nonneg hx (active (j + 1)), B_lambda_le_one hx (active (j + 1)),
      B_lambda_nonneg hx (active (j + 2)), B_lambda_le_one hx (active (j + 2))]

theorem f_abs_le_one {x : E} (hx : x ∈ B) (j : Fin 3) : |f j x| ≤ 1 :=
  abs_le.mpr (B_f_bounds hx j)

theorem f_sum (x : E) : ∑ j, f j x = 0 := by
  rw [Fin.sum_univ_three]
  simp only [f_apply]
  change (lambda (active 0) x - (2 / 3) * lambda (active 1) x -
      (1 / 3) * lambda (active 2) x) +
    (lambda (active 1) x - (2 / 3) * lambda (active 2) x -
      (1 / 3) * lambda (active 0) x) +
    (lambda (active 2) x - (2 / 3) * lambda (active 0) x -
      (1 / 3) * lambda (active 1) x) = 0
  ring

theorem cyclic_cuts_cover (x : E) : ∃ j, 0 ≤ f j x := by
  by_contra h
  push Not at h
  have hs := Finset.sum_lt_sum_of_nonempty Finset.univ_nonempty (fun j _ => h j)
  simp [f_sum] at hs

theorem f_kernel_volume_zero (j : Fin 3) : volume {x : E | f j x = 0} = 0 := by
  change volume ((f j).toLinearMap.ker : Set E) = 0
  apply Measure.addHaar_submodule
  intro htop
  have hz : (f j).toLinearMap = 0 := LinearMap.ker_eq_top.mp htop
  apply f_nonzero j
  ext x
  exact congrArg (fun L : E →ₗ[ℝ] ℝ => L x) hz

def T (j : Fin 3) : Set E :=
  B ∩ ({x | f (j + 1) x ≤ 0} ∩ {x | f (j + 2) x ≤ 0})

theorem T_subset_B (j : Fin 3) : T j ⊆ B := inter_subset_left

theorem T_f_nonpos (j : Fin 3) {x : E} (hx : x ∈ T j) (i : Fin 3) (hi : i ≠ j) :
    f i x ≤ 0 := by
  have h : ∀ a b : Fin 3, a ≠ b → a = b + 1 ∨ a = b + 2 := by decide
  rcases h i j hi with rfl | rfl
  · exact hx.2.1
  · exact hx.2.2

theorem T_f_nonneg (j : Fin 3) {x : E} (hx : x ∈ T j) : 0 ≤ f j x := by
  have h := f_sum x
  rw [Fin.sum_univ_three] at h
  have h1 : f (j + 1) x ≤ 0 := hx.2.1
  have h2 : f (j + 2) x ≤ 0 := hx.2.2
  fin_cases j <;> norm_num at h1 h2 ⊢ <;> linarith

theorem T_compact (j : Fin 3) : IsCompact (T j) :=
  B_compact.inter_right
    ((isClosed_le (f (j + 1)).continuous continuous_const).inter
      (isClosed_le (f (j + 2)).continuous continuous_const))

theorem T_convex (j : Fin 3) : Convex ℝ (T j) :=
  B_convex.inter ((convex_halfSpace_le (f (j + 1)).toLinearMap.isLinear 0).inter
    (convex_halfSpace_le (f (j + 2)).toLinearMap.isLinear 0))

theorem T_nonempty (j : Fin 3) : (T j).Nonempty :=
  ⟨0, interior_subset zero_mem_interior_B, by simp, by simp⟩

def free (i : Fin 3) : Fin 6 := Fin.natAdd 3 i

private def rot (j : Fin 3) : Fin 3 ⊕ Fin 3 ≃ Fin 6 :=
  (Equiv.sumCongr (Equiv.addRight j) (Equiv.refl (Fin 3))).trans finSumFinEquiv

@[simp] private theorem rot_inl (j i : Fin 3) : rot j (.inl i) = active (j + i) := by
  simp [rot, active, add_comm] ; rfl

@[simp] private theorem rot_inr (j i : Fin 3) : rot j (.inr i) = free i := rfl

private def M (j : Fin 3) (A : Matrix (Fin 3) (Fin 3) ℝ) : Matrix (Fin 6) (Fin 6) ℝ :=
  (Matrix.fromBlocks A 0 0 (1 : Matrix (Fin 3) (Fin 3) ℝ)).submatrix
    (rot j).symm (rot 0).symm

private theorem M_rot (j : Fin 3) (A : Matrix (Fin 3) (Fin 3) ℝ)
    (i k : Fin 3 ⊕ Fin 3) :
    M j A (rot j i) (rot 0 k) = Matrix.fromBlocks A 0 0 1 i k := by
  simp [M]

private theorem M_column_sum (j : Fin 3) (A : Matrix (Fin 3) (Fin 3) ℝ)
    (hA : ∀ k, ∑ i, A i k = 1) (k : Fin 6) : ∑ i, M j A i k = 1 := by
  obtain ⟨k, rfl⟩ := (rot 0).surjective k
  rw [← (rot j).sum_comp (fun i => M j A i (rot 0 k))]
  simp only [M_rot, Fintype.sum_sum_type]
  cases k <;> simp [hA, Matrix.one_apply]

private theorem M_abs_det (j : Fin 3) (A : Matrix (Fin 3) (Fin 3) ℝ) :
    |(M j A).det| = |A.det| := by
  rw [M, Matrix.abs_det_submatrix_equiv_equiv, Matrix.det_fromBlocks_zero₂₁,
    Matrix.det_one, mul_one]

private def vertex (j : Fin 3) (A : Matrix (Fin 3) (Fin 3) ℝ) (k : Fin 6) : E :=
  shift + fun i => M j A i.castSucc k

def source (j : Fin 3) (A : Matrix (Fin 3) (Fin 3) ℝ) : Set E :=
  convexHull ℝ (range (vertex j A))

theorem source_volume (j : Fin 3) (A : Matrix (Fin 3) (Fin 3) ℝ)
    (hA : ∀ k, ∑ i, A i k = 1) :
    volume (source j A) = ENNReal.ofReal |A.det| * volume B := by
  have hr : range (vertex j A) =
      (fun x => shift + x) '' range (fun k (i : Fin 5) => M j A i.castSucc k) := by
    rw [← Set.range_comp]
    rfl
  rw [source, hr]
  have h := (AffineEquiv.constVAdd ℝ E shift).toAffineMap.image_convexHull
    (range (fun k (i : Fin 5) => M j A i.castSucc k))
  change (fun x => shift + x) '' chartSimplex (M j A) =
    convexHull ℝ ((fun x => shift + x) '' range (fun k (i : Fin 5) => M j A i.castSucc k)) at h
  rw [← h]
  change volume ((fun x => shift + x) '' chartSimplex (M j A)) = _
  rw [volume_translate, volume_chartSimplex _ (M_column_sum j A hA), M_abs_det, B_volume]

private theorem lambda_vertex (j : Fin 3) (A : Matrix (Fin 3) (Fin 3) ℝ)
    (hA : ∀ k, ∑ i, A i k = 1) (i k : Fin 6) :
    lambda i (vertex j A k) = M j A i k := by
  have hh (l : Fin 5) : lambda l.castSucc (vertex j A k) = M j A l.castSucc k := by
    rw [lambda_castSucc]
    simp [vertex, shift]
  rcases Fin.eq_castSucc_or_eq_last i with ⟨i, rfl⟩ | rfl
  · exact hh i
  · have hs := lambda_sum (vertex j A k)
    have hm := M_column_sum j A hA k
    rw [Fin.sum_univ_castSucc] at hs hm
    simp only [hh] at hs
    linarith

def sourceBasis (j : Fin 3) (A : Matrix (Fin 3) (Fin 3) ℝ)
    (hA : ∀ k, ∑ i, A i k = 1) (hd : A.det ≠ 0) : AffineBasis (Fin 6) ℝ E :=
  shift +ᵥ chartBasis (M j A) (M_column_sum j A hA) (by
    apply abs_ne_zero.mp
    rwa [M_abs_det, abs_ne_zero])

@[simp] private theorem sourceBasis_apply (j : Fin 3) (A : Matrix (Fin 3) (Fin 3) ℝ)
    (hA : ∀ k, ∑ i, A i k = 1) (hd : A.det ≠ 0) (k : Fin 6) :
    sourceBasis j A hA hd k = vertex j A k := by
  change shift + SourceGeometry.chartAffineMap (M j A) (standardVertex 5 k) = _
  rw [SourceGeometry.chartAffineMap_standardVertex]
  rfl

theorem source_eq_hull (j : Fin 3) (A : Matrix (Fin 3) (Fin 3) ℝ)
    (hA : ∀ k, ∑ i, A i k = 1) (hd : A.det ≠ 0) :
    source j A = convexHull ℝ (range (sourceBasis j A hA hd)) := by
  simp [source, show (sourceBasis j A hA hd : Fin 6 → E) = vertex j A from
    funext (sourceBasis_apply j A hA hd)]

private theorem lambda_comb (j : Fin 3) (A : Matrix (Fin 3) (Fin 3) ℝ)
    (hA : ∀ k, ∑ i, A i k = 1) (w : Fin 6 → ℝ) (hw : ∑ i, w i = 1) (i : Fin 6) :
    lambda i (Finset.univ.affineCombination ℝ (vertex j A) w) = (M j A).mulVec w i := by
  rw [Finset.univ.map_affineCombination (vertex j A) w hw,
    Finset.univ.affineCombination_eq_linear_combination _ _ hw]
  simp [lambda_vertex j A hA, Matrix.mulVec, dotProduct, mul_comm]

private theorem mem_source_iff (j : Fin 3) (A : Matrix (Fin 3) (Fin 3) ℝ)
    (hA : ∀ k, ∑ i, A i k = 1) (hd : A.det ≠ 0) (x : E) :
    x ∈ source j A ↔ ∃ w : Fin 6 → ℝ, (∀ i, 0 ≤ w i) ∧
      ∀ i, lambda i x = (M j A).mulVec w i := by
  constructor
  · let b := sourceBasis j A hA hd
    rw [source_eq_hull j A hA hd, b.convexHull_eq_nonneg_coord]
    intro hx
    let w : Fin 6 → ℝ := fun i => b.coord i x
    refine ⟨w, hx, fun i => ?_⟩
    have h := lambda_comb j A hA w (b.sum_coord_apply_eq_one x) i
    have hb : (b : Fin 6 → E) = vertex j A := funext (sourceBasis_apply j A hA hd)
    rw [← hb, b.affineCombination_coord_eq_self x] at h
    exact h
  · rintro ⟨w, hw, hcoord⟩
    have hs : ∑ i, w i = 1 := calc
      _ = ∑ k, (∑ i, M j A i k) * w k := by simp [M_column_sum j A hA]
      _ = ∑ i, (M j A).mulVec w i := by
        simp only [Matrix.mulVec, dotProduct, Finset.sum_mul]
        rw [Finset.sum_comm]
      _ = 1 := by simp_rw [← hcoord, lambda_sum]
    have heq : Finset.univ.affineCombination ℝ (vertex j A) w = x := by
      apply basis.ext_elem
      intro i
      exact (lambda_comb j A hA w hs i).trans (hcoord i).symm
    apply mem_convexHull_of_exists_fintype w (vertex j A) hw hs Set.mem_range_self
    rwa [← Finset.univ.affineCombination_eq_linear_combination _ _ hs]

private theorem M_mulVec_active (j : Fin 3) (A : Matrix (Fin 3) (Fin 3) ℝ)
    (w : Fin 6 → ℝ) (i : Fin 3) :
    (M j A).mulVec w (active (j + i)) = A.mulVec (fun k => w (active k)) i := by
  change (∑ k, M j A (active (j + i)) k * w k) = _
  rw [← (rot 0).sum_comp (fun k => M j A (active (j + i)) k * w k)]
  rw [← rot_inl j i]
  simp only [Fintype.sum_sum_type]
  simp_rw [M_rot]
  simp only [Matrix.fromBlocks_apply₁₁,
    Matrix.fromBlocks_apply₁₂, Matrix.zero_apply, zero_mul, Finset.sum_const_zero, add_zero,
    rot_inl, zero_add, Matrix.mulVec, dotProduct]

private theorem M_mulVec_free (j : Fin 3) (A : Matrix (Fin 3) (Fin 3) ℝ)
    (w : Fin 6 → ℝ) (i : Fin 3) : (M j A).mulVec w (free i) = w (free i) := by
  change (∑ k, M j A (free i) k * w k) = _
  rw [← (rot 0).sum_comp (fun k => M j A (free i) k * w k)]
  rw [← rot_inr j i]
  simp only [Fintype.sum_sum_type]
  simp_rw [M_rot]
  simp [Matrix.one_apply]

private theorem mem_source_iff_active (j : Fin 3) (A : Matrix (Fin 3) (Fin 3) ℝ)
    (hA : ∀ k, ∑ i, A i k = 1) (hd : A.det ≠ 0) (x : E) :
    x ∈ source j A ↔ (∀ i, 0 ≤ lambda (free i) x) ∧
      ∃ w : Fin 3 → ℝ, (∀ i, 0 ≤ w i) ∧
        ∀ i, lambda (active (j + i)) x = A.mulVec w i := by
  rw [mem_source_iff j A hA hd x]
  constructor
  · rintro ⟨w, hw, h⟩
    exact ⟨fun i => by rw [h, M_mulVec_free]; exact hw _,
      fun i => w (active i), fun i => hw _, fun i => by rw [h, M_mulVec_active]⟩
  · rintro ⟨hfree, w, hw, h⟩
    let v : Fin 6 → ℝ := Sum.elim w (fun i => lambda (free i) x) ∘ (rot 0).symm
    have vl (i : Fin 3) : v (active i) = w i := calc
      _ = v (rot 0 (.inl i)) := by rw [rot_inl, zero_add]
      _ = _ := by simp only [v, Function.comp_apply, Equiv.symm_apply_apply, Sum.elim_inl]
    have vr (i : Fin 3) : v (free i) = lambda (free i) x := by
      change v (rot 0 (.inr i)) = _
      simp only [v, Function.comp_apply, Equiv.symm_apply_apply, Sum.elim_inr]
    refine ⟨v, ?_, ?_⟩
    · intro i
      obtain ⟨i, rfl⟩ := (rot 0).surjective i
      cases i with
      | inl i => simpa [vl] using hw i
      | inr i => simpa [vr] using hfree i
    · intro i
      obtain ⟨i, rfl⟩ := (rot j).surjective i
      cases i with
      | inl i => simpa only [rot_inl, M_mulVec_active, vl] using h i
      | inr i => rw [rot_inr, M_mulVec_free, vr]

def coordinates (j : Fin 3) (x : E) : Fin 3 → ℝ :=
  fun i => lambda (active (j + i)) x

theorem mem_source_iff_weights (j : Fin 3) (A : Matrix (Fin 3) (Fin 3) ℝ)
    (hA : ∀ k, ∑ i, A i k = 1) (hd : A.det ≠ 0)
    (weights : (Fin 3 → ℝ) → Fin 3 → ℝ)
    (hw : ∀ x, A.mulVec (weights x) = x) (x : E) :
    x ∈ source j A ↔ (∀ i, 0 ≤ lambda (free i) x) ∧
      (∀ i, 0 ≤ weights (coordinates j x) i) := by
  rw [mem_source_iff_active j A hA hd]
  constructor
  · rintro ⟨hf, w, hn, h⟩
    refine ⟨hf, ?_⟩
    have he : weights (coordinates j x) = w :=
      Matrix.mulVec_injective_of_det_ne_zero hd ((hw _).trans (funext h))
    simpa only [he] using hn
  · rintro ⟨hf, hn⟩
    exact ⟨hf, weights (coordinates j x), hn, fun i => (congrFun (hw (coordinates j x)) i).symm⟩

/-- Inverse active weights and the unchanged free coordinates of a source simplex. -/
theorem sourceBasis_weights (j : Fin 3) (A : Matrix (Fin 3) (Fin 3) ℝ)
    (hA : ∀ k, ∑ i, A i k = 1) (hd : A.det ≠ 0)
    (weights : (Fin 3 → ℝ) → Fin 3 → ℝ)
    (hw : ∀ x, A.mulVec (weights x) = x) (x : E) :
    (∀ i, (sourceBasis j A hA hd).coord (active i) x = weights (coordinates j x) i) ∧
      ∀ i, (sourceBasis j A hA hd).coord (free i) x = lambda (free i) x := by
  let b := sourceBasis j A hA hd
  let v : Fin 6 → ℝ := fun i => b.coord i x
  have hcoord (i : Fin 6) : lambda i x = (M j A).mulVec v i := by
    have h := lambda_comb j A hA v (b.sum_coord_apply_eq_one x) i
    rw [← funext (sourceBasis_apply j A hA hd), b.affineCombination_coord_eq_self x] at h
    exact h
  have he : (fun i => v (active i)) = weights (coordinates j x) :=
    Matrix.mulVec_injective_of_det_ne_zero hd (by
      rw [hw]
      ext i
      exact (M_mulVec_active j A v i).symm.trans (hcoord _).symm)
  exact ⟨congrFun he, fun i => ((hcoord _).trans (M_mulVec_free j A v i)).symm⟩

theorem mem_B_iff_coordinates (j : Fin 3) (x : E) :
    x ∈ B ↔ (∀ i, 0 ≤ lambda (free i) x) ∧ (∀ i, 0 ≤ coordinates j x i) := by
  rw [B_eq_nonneg_lambda]
  constructor
  · intro h
    exact ⟨fun i => h _, fun i => h _⟩
  · rintro ⟨hf, ha⟩ i
    obtain ⟨i, rfl⟩ := (rot j).surjective i
    cases i with
    | inl i => simpa only [rot_inl, coordinates] using ha i
    | inr i => simpa only [rot_inr] using hf i

private theorem scores (j : Fin 3) (x : E) :
    f j x = coordinates j x 0 - (2 / 3) * coordinates j x 1 -
      (1 / 3) * coordinates j x 2 ∧
    f (j + 1) x = coordinates j x 1 - (2 / 3) * coordinates j x 2 -
      (1 / 3) * coordinates j x 0 ∧
    f (j + 2) x = coordinates j x 2 - (2 / 3) * coordinates j x 0 -
      (1 / 3) * coordinates j x 1 := by
  have h11 : (1 : Fin 3) + 1 = 2 := by decide
  have h12 : (1 : Fin 3) + 2 = 0 := by decide
  have h21 : (2 : Fin 3) + 1 = 0 := by decide
  have h22 : (2 : Fin 3) + 2 = 1 := by decide
  simp [f_apply, coordinates, add_assoc, h11, h12, h21, h22]

private def uMat : Matrix (Fin 3) (Fin 3) ℝ :=
  !![1, 1 / 3, 3 / 5; 0, 1 / 3, 0; 0, 1 / 3, 2 / 5]

private def vMat : Matrix (Fin 3) (Fin 3) ℝ :=
  !![1, 1 / 3, 3 / 4; 0, 1 / 3, 1 / 4; 0, 1 / 3, 0]

private def capMat : Matrix (Fin 3) (Fin 3) ℝ :=
  !![1, 2 / 5, 1 / 4; 0, 3 / 5, 0; 0, 0, 3 / 4]

private theorem uMat_sum (k : Fin 3) : ∑ i, uMat i k = 1 := by
  fin_cases k <;> norm_num [uMat, Fin.sum_univ_three]

private theorem vMat_sum (k : Fin 3) : ∑ i, vMat i k = 1 := by
  fin_cases k <;> norm_num [vMat, Fin.sum_univ_three]

private theorem capMat_sum (k : Fin 3) : ∑ i, capMat i k = 1 := by
  fin_cases k <;> norm_num [capMat, Fin.sum_univ_three]

private theorem uMat_det : uMat.det = 2 / 15 := by
  norm_num [uMat, Matrix.det_fin_three]

private theorem vMat_det : vMat.det = -(1 / 12) := by
  norm_num [vMat, Matrix.det_fin_three]

private theorem capMat_det : capMat.det = 9 / 20 := by
  norm_num [capMat, Matrix.det_fin_three]

/-- The simplex with active vertices e_j, the active centroid, and
the edge point on e_j–e_(j+2). Its other vertices are the free coordinate vertices. -/
def U (j : Fin 3) : Set E := source j uMat

def uBasis (j : Fin 3) : AffineBasis (Fin 6) ℝ E :=
  sourceBasis j uMat uMat_sum (by rw [uMat_det]; norm_num)

theorem U_eq_hull (j : Fin 3) : U j = convexHull ℝ (range (uBasis j)) :=
  source_eq_hull _ _ _ _

theorem U_compact (j : Fin 3) : IsCompact (U j) := by
  rw [U_eq_hull]
  exact (Set.finite_range (uBasis j)).isCompact_convexHull ℝ

theorem U_convex (j : Fin 3) : Convex ℝ (U j) := by
  rw [U_eq_hull]
  exact convex_convexHull ℝ _

theorem U_nonempty (j : Fin 3) : (U j).Nonempty := by
  rw [U_eq_hull]
  exact ⟨uBasis j 0, subset_convexHull ℝ _ (mem_range_self _)⟩

theorem U_volume (j : Fin 3) : volume (U j) = ENNReal.ofReal (2 / 15) * volume B := by
  rw [U, source_volume _ _ uMat_sum, uMat_det, abs_of_pos (by norm_num)]

theorem forall_fin_three {P : Fin 3 → Prop} :
    (∀ i, P i) ↔ P 0 ∧ P 1 ∧ P 2 := by
  refine ⟨fun h => ⟨h _, h _, h _⟩, ?_⟩
  rintro ⟨h0, h1, h2⟩ i
  fin_cases i
  · exact h0
  · exact h1
  · exact h2

private theorem U_eq_region (j : Fin 3) :
    U j = T j ∩ {x | coordinates j x 1 ≤ coordinates j x 2} := by
  ext x
  let w (a : Fin 3 → ℝ) : Fin 3 → ℝ :=
    ![a 0 + (1 / 2) * a 1 - (3 / 2) * a 2, 3 * a 1, (5 / 2) * (a 2 - a 1)]
  have hw (a : Fin 3 → ℝ) : uMat.mulVec (w a) = a := by
    ext i
    fin_cases i <;> simp [uMat, w, Matrix.mulVec, dotProduct, Fin.sum_univ_three] <;> ring
  rw [U, mem_source_iff_weights _ _ uMat_sum (by rw [uMat_det]; norm_num) w hw]
  change _ ↔ (x ∈ B ∧ f (j + 1) x ≤ 0 ∧ f (j + 2) x ≤ 0) ∧ _
  rw [mem_B_iff_coordinates j x, (scores j x).2.1, (scores j x).2.2]
  simp only [w, forall_fin_three, Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.cons_val_two, Matrix.tail_cons, Matrix.head_cons]
  change _ ↔ _ ∧ coordinates j x 1 ≤ coordinates j x 2
  constructor
  · rintro ⟨hf, h0, h1, h2⟩
    exact ⟨⟨⟨hf, by linarith, by linarith, by linarith⟩, by linarith, by linarith⟩,
      by linarith⟩
  · rintro ⟨⟨⟨hf, h0, h1, h2⟩, h3, h4⟩, h12⟩
    exact ⟨hf, by linarith, by linarith, by linarith⟩

theorem U_subset_T (j : Fin 3) : U j ⊆ T j := by
  rw [U_eq_region]
  exact inter_subset_left

theorem U_subset_B (j : Fin 3) : U j ⊆ B := (U_subset_T j).trans (T_subset_B j)

private theorem V_eq_region (j : Fin 3) :
    source j vMat = T j ∩ {x | coordinates j x 2 ≤ coordinates j x 1} := by
  ext x
  let w (a : Fin 3 → ℝ) : Fin 3 → ℝ :=
    ![a 0 - 3 * a 1 + 2 * a 2, 3 * a 2, 4 * (a 1 - a 2)]
  have hw (a : Fin 3 → ℝ) : vMat.mulVec (w a) = a := by
    ext i
    fin_cases i <;> simp [vMat, w, Matrix.mulVec, dotProduct, Fin.sum_univ_three]; ring
  rw [mem_source_iff_weights _ _ vMat_sum (by rw [vMat_det]; norm_num) w hw]
  change _ ↔ (x ∈ B ∧ f (j + 1) x ≤ 0 ∧ f (j + 2) x ≤ 0) ∧ _
  rw [mem_B_iff_coordinates j x, (scores j x).2.1, (scores j x).2.2]
  simp only [w, forall_fin_three, Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.cons_val_two, Matrix.tail_cons, Matrix.head_cons]
  change _ ↔ _ ∧ coordinates j x 2 ≤ coordinates j x 1
  constructor
  · rintro ⟨hf, h0, h1, h2⟩
    exact ⟨⟨⟨hf, by linarith, by linarith, by linarith⟩, by linarith, by linarith⟩,
      by linarith⟩
  · rintro ⟨⟨⟨hf, h0, h1, h2⟩, h3, h4⟩, h21⟩
    exact ⟨hf, by linarith, by linarith, by linarith⟩

private theorem cap_eq_region (j : Fin 3) :
    source j capMat = B ∩ {x | 0 ≤ f j x} := by
  ext x
  let w (a : Fin 3 → ℝ) : Fin 3 → ℝ :=
    ![a 0 - (2 / 3) * a 1 - (1 / 3) * a 2, (5 / 3) * a 1, (4 / 3) * a 2]
  have hw (a : Fin 3 → ℝ) : capMat.mulVec (w a) = a := by
    ext i
    fin_cases i <;> simp [capMat, w, Matrix.mulVec, dotProduct, Fin.sum_univ_three] <;> ring
  rw [mem_source_iff_weights _ _ capMat_sum (by rw [capMat_det]; norm_num) w hw]
  change _ ↔ x ∈ B ∧ 0 ≤ f j x
  rw [mem_B_iff_coordinates j x, (scores j x).1]
  simp only [w, forall_fin_three, Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.cons_val_two, Matrix.tail_cons, Matrix.head_cons]
  constructor
  · rintro ⟨hf, h0, h1, h2⟩
    exact ⟨⟨hf, by linarith, by linarith, by linarith⟩, h0⟩
  · rintro ⟨⟨hf, h0, h1, h2⟩, h⟩
    exact ⟨hf, h, by linarith, by linarith⟩

theorem positive_cap_volume (j : Fin 3) :
    volume (B ∩ {x | 0 ≤ f j x}) = ENNReal.ofReal (9 / 20) * volume B := by
  rw [← cap_eq_region, source_volume _ _ capMat_sum, capMat_det, abs_of_pos (by norm_num)]

theorem coordinate_eq_null (i k : Fin 6) (hik : i ≠ k) :
    volume {x : E | lambda i x = lambda k x} = 0 := by
  let L : E →ₗ[ℝ] ℝ := (lambda i).linear - (lambda k).linear
  have hL (x : E) : L x = lambda i x - lambda k x := by
    have hi := congrFun (lambda i).decomp x
    have hk := congrFun (lambda k).decomp x
    simp only [Pi.add_apply, lambda_zero] at hi hk
    change (lambda i).linear x - (lambda k).linear x = _
    linarith
  have hset : {x : E | lambda i x = lambda k x} = (L.ker : Set E) := by
    ext x
    change (_ = _) ↔ L x = 0
    rw [hL, sub_eq_zero]
  rw [hset]
  apply Measure.addHaar_submodule
  intro ht
  have hz := congrArg (fun l : E →ₗ[ℝ] ℝ => l (basis i)) (LinearMap.ker_eq_top.mp ht)
  rw [hL] at hz
  norm_num [lambda, basis.coord_apply_ne hik.symm] at hz

theorem T_volume (j : Fin 3) : volume (T j) = ENNReal.ofReal (13 / 60) * volume B := by
  have hu : U j ∪ source j vMat = T j := by
    rw [U_eq_region, V_eq_region]
    ext x
    change (_ ∧ coordinates j x 1 ≤ coordinates j x 2) ∨
      (_ ∧ coordinates j x 2 ≤ coordinates j x 1) ↔ x ∈ T j
    constructor
    · rintro (⟨h, _⟩ | ⟨h, _⟩) <;> exact h
    · intro h
      rcases le_total (coordinates j x 1) (coordinates j x 2) with h' | h'
      · exact Or.inl ⟨h, h'⟩
      · exact Or.inr ⟨h, h'⟩
  have hd : AEDisjoint volume (U j) (source j vMat) := by
    rw [AEDisjoint, U_eq_region, V_eq_region]
    have hne : active (j + 1) ≠ active (j + 2) := by fin_cases j <;> decide
    apply measure_mono_null _ (coordinate_eq_null _ _ hne)
    rintro x ⟨⟨_, h12⟩, ⟨_, h21⟩⟩
    exact le_antisymm h12 h21
  have hm : MeasurableSet (source j vMat) :=
    ((Set.finite_range (vertex j vMat)).isCompact_convexHull ℝ).measurableSet
  rw [← hu, measure_union₀ hm.nullMeasurableSet hd, U_volume,
    source_volume _ _ vMat_sum, vMat_det, abs_of_neg (by norm_num), neg_neg, ← add_mul,
    ← ENNReal.ofReal_add (by norm_num) (by norm_num)]
  congr 2
  norm_num

end SharpOC.SelectorSources
