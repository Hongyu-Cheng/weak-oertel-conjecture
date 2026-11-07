import SharpOC.SourceGeometry
import SharpOC.SimplexCaps

noncomputable section
open Set MeasureTheory
open scoped ENNReal

namespace SharpOC.MiddleSimplex

def standardVertex (n : ℕ) (j : Fin (n + 1)) (i : Fin n) : ℝ :=
  if j = i.castSucc then 1 else 0

@[simp] theorem standardVertex_castSucc (n : ℕ) (j : Fin n) :
    standardVertex n j.castSucc = Pi.single j 1 := by
  ext i
  simp [standardVertex, Pi.single_apply, eq_comm]

@[simp] theorem standardVertex_last (n : ℕ) :
    standardVertex n (Fin.last n) = 0 := by
  ext i
  simp [standardVertex, Fin.ext_iff, ne_of_gt i.isLt]

theorem standardVertex_independent (n : ℕ) :
    AffineIndependent ℝ (standardVertex n) := by
  rw [affineIndependent_iff_of_fintype]
  intro w hw hs j
  rw [Finset.univ.weightedVSub_eq_linear_combination hw] at hs
  have hfirst (i : Fin n) : w i.castSucc = 0 := by
    have h := congrFun hs i
    simpa [standardVertex, Finset.sum_apply, Pi.smul_apply, smul_eq_mul,
      mul_ite] using h
  rcases Fin.eq_castSucc_or_eq_last j with ⟨i, rfl⟩ | rfl
  · exact hfirst i
  · simpa [Fin.sum_univ_castSucc, hfirst] using hw

def standardBasis (n : ℕ) : AffineBasis (Fin (n + 1)) ℝ (Fin n → ℝ) where
  toFun := standardVertex n
  ind' := standardVertex_independent n
  tot' := (standardVertex_independent n).affineSpan_eq_top_iff_card_eq_finrank_add_one.mpr
    (by simp)

theorem standardVertex_range (n : ℕ) :
    range (standardVertex n) = insert 0 (range (fun j : Fin n => Pi.single j (1 : ℝ))) := by
  ext x
  constructor
  · rintro ⟨j, rfl⟩
    rcases Fin.eq_castSucc_or_eq_last j with ⟨j, rfl⟩ | rfl <;> simp
  · rintro (rfl | ⟨j, rfl⟩)
    · exact ⟨Fin.last n, standardVertex_last n⟩
    · exact ⟨j.castSucc, standardVertex_castSucc n j⟩

@[simp] theorem standardBasis_apply (n : ℕ) (j : Fin (n + 1)) :
    standardBasis n j = standardVertex n j := rfl

theorem standardBasis_coord_castSucc (n : ℕ) (i : Fin n) (x : Fin n → ℝ) :
    (standardBasis n).coord i.castSucc x = x i := by
  have h := congrFun ((standardBasis n).linear_combination_coord_eq_self x) i
  simpa [standardVertex, Finset.sum_apply, Pi.smul_apply, smul_eq_mul,
    mul_ite] using h

theorem standardBasis_coord_last (n : ℕ) (x : Fin n → ℝ) :
    (standardBasis n).coord (Fin.last n) x = 1 - ∑ i, x i := by
  have h := (standardBasis n).sum_coord_apply_eq_one x
  rw [Fin.sum_univ_castSucc] at h
  simp_rw [standardBasis_coord_castSucc] at h
  linarith

abbrev E := Fin 23 → ℝ

def shift : E := fun _ => -(1 / 24 : ℝ)

def basis : AffineBasis (Fin 24) ℝ E := shift +ᵥ standardBasis 23

def B : Set E := convexHull ℝ (range basis)

def lambda (j : Fin 24) : E →ᵃ[ℝ] ℝ := basis.coord j

@[simp] theorem basis_apply (j : Fin 24) : basis j = shift + standardVertex 23 j := rfl

theorem lambda_castSucc (i : Fin 23) (x : E) :
    lambda i.castSucc x = x i + 1 / 24 := by
  simp [lambda, basis, AffineBasis.coord_vadd, standardBasis_coord_castSucc, shift,
    add_comm]

theorem lambda_last (x : E) :
    lambda (Fin.last 23) x = 1 / 24 - ∑ i, x i := by
  change ((shift +ᵥ standardBasis 23).coord (Fin.last 23)) x = _
  rw [AffineBasis.coord_vadd]
  change (standardBasis 23).coord (Fin.last 23) (-shift + x) = _
  rw [standardBasis_coord_last]
  simp [shift, Finset.sum_add_distrib]
  ring

@[simp] theorem lambda_zero (j : Fin 24) : lambda j 0 = 1 / 24 := by
  rcases Fin.eq_castSucc_or_eq_last j with ⟨i, rfl⟩ | rfl
  · rw [lambda_castSucc]; simp
  · rw [lambda_last]; simp

theorem lambda_sum (x : E) : ∑ j, lambda j x = 1 := basis.sum_coord_apply_eq_one x

theorem B_eq_nonneg_lambda : B = {x | ∀ j, 0 ≤ lambda j x} :=
  basis.convexHull_eq_nonneg_coord

theorem B_lambda_nonneg {x : E} (hx : x ∈ B) (j : Fin 24) : 0 ≤ lambda j x := by
  rw [B_eq_nonneg_lambda] at hx
  exact hx j

theorem B_lambda_le_one {x : E} (hx : x ∈ B) (j : Fin 24) : lambda j x ≤ 1 := by
  have h := Finset.single_le_sum (fun k _ => B_lambda_nonneg hx k) (Finset.mem_univ j)
  rwa [lambda_sum] at h

theorem B_eq_translate_standard :
    B = (fun x => shift + x) '' SharpOC.SourceGeometry.standardSimplex 23 := by
  unfold B SharpOC.SourceGeometry.standardSimplex
  rw [← standardVertex_range]
  have hr : range basis = (fun x => shift + x) '' range (standardVertex 23) := by
    rw [← Set.range_comp]
    rfl
  rw [hr]
  exact ((AffineEquiv.constVAdd ℝ E shift).toAffineMap.image_convexHull _).symm

theorem B_compact : IsCompact B := (Set.finite_range basis).isCompact_convexHull ℝ

theorem B_convex : Convex ℝ B := convex_convexHull ℝ _

theorem zero_mem_interior_B : (0 : E) ∈ interior B := by
  rw [B, basis.interior_convexHull]
  intro j
  change 0 < lambda j 0
  rw [lambda_zero]
  norm_num

theorem B_volume_pos : 0 < volume B :=
  Measure.measure_pos_of_nonempty_interior volume ⟨0, zero_mem_interior_B⟩

theorem B_volume_ne_top : volume B ≠ ⊤ := B_compact.measure_ne_top

theorem B_volume : volume B = volume (SharpOC.SourceGeometry.standardSimplex 23) := by
  rw [B_eq_translate_standard, SharpOC.SourceGeometry.volume_translate]

def f (j : Fin 24) : E →L[ℝ] ℝ :=
  ((lambda j).linear - (lambda (j + 1)).linear).toContinuousLinearMap

theorem f_apply (j : Fin 24) (x : E) : f j x = lambda j x - lambda (j + 1) x := by
  have h1 := congrFun (lambda j).decomp x
  have h2 := congrFun (lambda (j + 1)).decomp x
  simp only [Pi.add_apply, lambda_zero] at h1 h2
  change (lambda j).linear x - (lambda (j + 1)).linear x = _
  linarith

theorem f_nonzero (j : Fin 24) : f j ≠ 0 := by
  have hj : j ≠ j + 1 := by omega
  intro hz
  have h := congrArg (fun g : E →L[ℝ] ℝ => g (basis j)) hz
  rw [f_apply] at h
  simp only [lambda, basis.coord_apply_eq, basis.coord_apply_ne hj.symm,
    ContinuousLinearMap.zero_apply] at h
  norm_num at h

theorem B_f_bounds {x : E} (hx : x ∈ B) (j : Fin 24) :
    -1 ≤ f j x ∧ f j x ≤ 1 := by
  rw [f_apply]
  have h0 := B_lambda_nonneg hx j
  have h1 := B_lambda_nonneg hx (j + 1)
  have h2 := B_lambda_le_one hx j
  have h3 := B_lambda_le_one hx (j + 1)
  constructor <;> linarith

theorem f_sum (x : E) : ∑ j, f j x = 0 := by
  simp_rw [f_apply]
  rw [Finset.sum_sub_distrib]
  have h : ∑ j : Fin 24, lambda (j + 1) x = ∑ j : Fin 24, lambda j x :=
    Fintype.sum_equiv (Equiv.addRight 1) _ _ (by intro j; rfl)
  rw [h, sub_self]

theorem cyclic_cuts_cover (x : E) : ∃ j, 0 ≤ f j x := by
  by_contra h
  push Not at h
  have hs := Finset.sum_lt_sum_of_nonempty Finset.univ_nonempty (fun j _ => h j)
  simpa [f_sum] using hs

/-- Linear barycentric transposition of two adjacent vertices. Centering
makes the affine permutation linear. -/
def swapMap (j : Fin 24) : E →ₗ[ℝ] E :=
  LinearMap.id - (f j).toLinearMap.smulRight (basis j - basis (j + 1))

theorem swapMap_apply (j : Fin 24) (x : E) :
    swapMap j x = x - f j x • (basis j - basis (j + 1)) := rfl

theorem lambda_swapMap (j k : Fin 24) (x : E) :
    lambda k (swapMap j x) =
      if k = j then lambda (j + 1) x else
        if k = j + 1 then lambda j x else lambda k x := by
  have hj : j ≠ j + 1 := by omega
  have hlin := (lambda k).linearMap_vsub (basis j) (basis (j + 1))
  change (lambda k).linear (basis j - basis (j + 1)) =
    lambda k (basis j) - lambda k (basis (j + 1)) at hlin
  have hx := congrFun (lambda k).decomp x
  have hs := congrFun (lambda k).decomp (swapMap j x)
  simp only [Pi.add_apply, lambda_zero] at hx hs
  have hval : (lambda k).linear (swapMap j x) =
      (lambda k).linear x - f j x * (lambda k (basis j) - lambda k (basis (j + 1))) := by
    rw [swapMap_apply, map_sub, map_smul, hlin]
    rfl
  rw [hval] at hs
  rw [f_apply] at hs
  simp only [lambda, basis.coord_apply] at hs hx ⊢
  by_cases hkj : k = j
  · subst k
    simp only [ite_true, if_neg hj] at hs ⊢
    linarith
  · by_cases hkn : k = j + 1
    · subst k
      simp only [if_neg hkj, ite_true] at hs ⊢
      linarith
    · simp only [if_neg hkj, if_neg hkn, sub_zero, sub_self, mul_zero] at hs ⊢
      linarith

theorem f_swapMap (j : Fin 24) (x : E) : f j (swapMap j x) = -f j x := by
  have hj : j + 1 ≠ j := by omega
  rw [f_apply, lambda_swapMap, lambda_swapMap, f_apply]
  simp [hj]

theorem swapMap_involutive (j : Fin 24) : Function.Involutive (swapMap j) := by
  intro x
  rw [swapMap_apply, f_swapMap, swapMap_apply]
  module

theorem swapMap_abs_det (j : Fin 24) : |LinearMap.det (swapMap j)| = 1 := by
  have hcomp : (swapMap j).comp (swapMap j) = LinearMap.id := by
    apply LinearMap.ext
    intro x
    exact swapMap_involutive j x
  have hd := congrArg LinearMap.det hcomp
  rw [LinearMap.det_comp, LinearMap.det_id] at hd
  have habs := congrArg abs hd
  rw [abs_mul, abs_one] at habs
  nlinarith [abs_nonneg (LinearMap.det (swapMap j))]

theorem swapMap_mem_B (j : Fin 24) {x : E} (hx : x ∈ B) : swapMap j x ∈ B := by
  rw [B_eq_nonneg_lambda] at hx ⊢
  intro k
  rw [lambda_swapMap]
  split_ifs <;> exact hx _

theorem swapMap_image_positive (j : Fin 24) :
    swapMap j '' (B ∩ {x | 0 ≤ f j x}) = B ∩ {x | f j x ≤ 0} := by
  ext x
  constructor
  · rintro ⟨y, ⟨hy, hfy⟩, rfl⟩
    change 0 ≤ f j y at hfy
    refine ⟨swapMap_mem_B j hy, ?_⟩
    change f j (swapMap j y) ≤ 0
    rw [f_swapMap]
    linarith
  · rintro ⟨hx, hfx⟩
    change f j x ≤ 0 at hfx
    refine ⟨swapMap j x, ⟨swapMap_mem_B j hx, ?_⟩, swapMap_involutive j x⟩
    change 0 ≤ f j (swapMap j x)
    rw [f_swapMap]
    linarith

theorem equal_signed_cap_volume (j : Fin 24) :
    volume (B ∩ {x | 0 ≤ f j x}) = volume (B ∩ {x | f j x ≤ 0}) := by
  rw [← swapMap_image_positive, Measure.addHaar_image_linearMap, swapMap_abs_det]
  simp

theorem f_kernel_volume_zero (j : Fin 24) : volume {x : E | f j x = 0} = 0 := by
  change volume ((f j).toLinearMap.ker : Set E) = 0
  apply Measure.addHaar_submodule
  intro htop
  have hz : (f j).toLinearMap = 0 := LinearMap.ker_eq_top.mp htop
  apply f_nonzero j
  ext x
  exact congrArg (fun L : E →ₗ[ℝ] ℝ => L x) hz

theorem positive_cap_volume (j : Fin 24) :
    volume (B ∩ {x | 0 ≤ f j x}) = volume B / 2 := by
  have hzero : volume ((B ∩ {x | 0 ≤ f j x}) ∩ (B ∩ {x | f j x ≤ 0})) = 0 := by
    apply measure_mono_null _ (f_kernel_volume_zero j)
    rintro x ⟨⟨_, hpos⟩, ⟨_, hneg⟩⟩
    exact le_antisymm hneg hpos
  have hunion : (B ∩ {x | 0 ≤ f j x}) ∪ (B ∩ {x | f j x ≤ 0}) = B := by
    ext x
    simp only [mem_union, mem_inter_iff, mem_ofPred_eq]
    constructor
    · tauto
    · intro hx
      rcases le_total 0 (f j x) with h | h
      · exact Or.inl ⟨hx, h⟩
      · exact Or.inr ⟨hx, h⟩
  have hmeas : MeasurableSet (B ∩ {x | f j x ≤ 0}) :=
    B_compact.measurableSet.inter (isClosed_le (f j).continuous continuous_const).measurableSet
  have hs := measure_union_add_inter (μ := volume) (B ∩ {x | 0 ≤ f j x}) hmeas
  rw [hunion, hzero, add_zero, ← equal_signed_cap_volume] at hs
  apply (ENNReal.eq_div_iff (by norm_num) (by norm_num)).mpr
  simpa only [two_mul] using hs.symm

end SharpOC.MiddleSimplex
