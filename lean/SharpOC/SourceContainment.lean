import SharpOC.MiddleSimplex
import SharpOC.Constants

noncomputable section
open Set MeasureTheory
open scoped Pointwise

namespace SharpOC.SourceContainment
open SharpOC.SourceGeometry SharpOC.MiddleSimplex

/-- Centered continuous coordinates for a shifted chain partition. -/
def centeredChart (a : Fin 3) (v : ChainCoordinate → ℝ) : E :=
  fun i => v (cyclicCoordinate a i.castSucc) - 1/24

def chartLinear (a : Fin 3) : (ChainCoordinate → ℝ) →ₗ[ℝ] E where
  toFun v i := v (cyclicCoordinate a i.castSucc)
  map_add' _ _ := rfl
  map_smul' _ _ := rfl

def chartAffine (a : Fin 3) : (ChainCoordinate → ℝ) →ᵃ[ℝ] E where
  toFun := centeredChart a
  linear := chartLinear a
  map_vadd' x v := by
    ext i
    simp [centeredChart, chartLinear]
    ring

def T (a : Fin 3) : Set E := centeredChart a '' orderedSource

def center (a : Fin 3) : E := centeredChart a sourceCenter

def P (a : Fin 3) : Set E := AffineMap.homothety (center a) (103/104 : ℝ) '' T a

def A : Set E := (fun x : E => (1/10000 : ℝ) • x) '' B

/-- Pull a middle-simplex point back to ordered-chain indexing. -/
def barycentricPullback (a : Fin 3) (x : E) (i : ChainCoordinate) : ℝ :=
  lambda ((cyclicCoordinateEquiv a).symm i) x

theorem barycentricPullback_mem (a : Fin 3) {x : E} (hx : x ∈ B) :
    barycentricPullback a x ∈ barycentricSimplex := by
  constructor
  · intro i
    rw [B_eq_nonneg_lambda] at hx
    exact hx _
  · change (∑ i, lambda ((cyclicCoordinateEquiv a).symm i) x) = 1
    rw [Equiv.sum_comp (cyclicCoordinateEquiv a).symm (fun j => lambda j x)]
    exact lambda_sum x

theorem centeredChart_barycentricPullback (a : Fin 3) (x : E) :
    centeredChart a (barycentricPullback a x) = x := by
  ext i
  change lambda ((cyclicCoordinateEquiv a).symm (cyclicCoordinateEquiv a i.castSucc)) x - 1/24 = x i
  rw [Equiv.symm_apply_apply, lambda_castSucc]
  ring

theorem lambda_centeredChart (a : Fin 3) {v : ChainCoordinate → ℝ}
    (hv : ∑ i, v i = 1) (j : Fin 24) :
    lambda j (centeredChart a v) = v (cyclicCoordinate a j) := by
  rcases Fin.eq_castSucc_or_eq_last j with ⟨i, rfl⟩ | rfl
  · rw [lambda_castSucc]
    simp [centeredChart]
  · have hs : (∑ j : Fin 24, v (cyclicCoordinate a j)) = 1 := by
      change (∑ j, v (cyclicCoordinateEquiv a j)) = 1
      rw [Equiv.sum_comp]
      exact hv
    rw [Fin.sum_univ_castSucc] at hs
    rw [lambda_last]
    simp only [centeredChart, Finset.sum_sub_distrib, Finset.sum_const,
      Finset.card_univ, Fintype.card_fin, nsmul_eq_mul]
    linarith

theorem centeredChart_mem_B (a : Fin 3) {v : ChainCoordinate → ℝ}
    (hv : v ∈ barycentricSimplex) : centeredChart a v ∈ B := by
  rw [B_eq_nonneg_lambda]
  intro j
  rw [lambda_centeredChart a hv.2 j]
  exact hv.1 _

theorem centeredChart_contractedPoint (a : Fin 3) (x : ChainCoordinate → ℝ) :
    centeredChart a (contractedPoint x) =
      AffineMap.homothety (center a) (103/104 : ℝ) (centeredChart a x) := by
  ext i
  simp [centeredChart, contractedPoint, center, AffineMap.homothety_apply]
  ring

theorem mem_P_iff (a : Fin 3) (p : E) :
    p ∈ P a ↔ ∃ x ∈ orderedSource, centeredChart a (contractedPoint x) = p := by
  constructor
  · rintro ⟨y, ⟨x, hx, rfl⟩, rfl⟩
    exact ⟨x, hx, centeredChart_contractedPoint a x⟩
  · rintro ⟨x, hx, rfl⟩
    exact ⟨centeredChart a x, ⟨x, hx, rfl⟩, (centeredChart_contractedPoint a x).symm⟩

theorem T_subset_B (a : Fin 3) : T a ⊆ B := by
  rintro x ⟨v, hv, rfl⟩
  exact centeredChart_mem_B a hv.1

theorem P_subset_B (a : Fin 3) : P a ⊆ B := by
  intro p hp
  obtain ⟨x, hx, rfl⟩ := (mem_P_iff a p).1 hp
  exact centeredChart_mem_B a (contractedPoint_mem_simplex hx)

theorem center_mem_T (a : Fin 3) : center a ∈ T a :=
  ⟨sourceCenter, sourceCenter_mem_orderedSource, rfl⟩

theorem center_mem_P (a : Fin 3) : center a ∈ P a := by
  refine ⟨center a, center_mem_T a, ?_⟩
  simp

theorem T_convex (a : Fin 3) : Convex ℝ (T a) :=
  orderedSource_convex.affine_image (chartAffine a)

theorem P_convex (a : Fin 3) : Convex ℝ (P a) :=
  (T_convex a).affine_image (AffineMap.homothety (center a) (103/104 : ℝ))

theorem T_compact (a : Fin 3) : IsCompact (T a) := by
  have hc : IsCompact orderedSource := by
    rw [orderedSource_eq_convexHull]
    exact (Set.finite_range sourceVertex).isCompact_convexHull ℝ
  exact hc.image (chartAffine a).continuous_of_finiteDimensional

theorem P_compact (a : Fin 3) : IsCompact (P a) :=
  (T_compact a).image (AffineMap.homothety (center a) (103/104 : ℝ)).continuous_of_finiteDimensional

theorem A_convex : Convex ℝ A := by
  exact B_convex.linear_image (LinearMap.lsmul ℝ E (1/10000 : ℝ))

theorem A_compact : IsCompact A := B_compact.image (by fun_prop)

theorem zero_mem_A : (0 : E) ∈ A :=
  ⟨0, interior_subset zero_mem_interior_B, by simp⟩

/-- First actual containment, with the same centered chart as the middle simplex. -/
theorem P_add_half_A (a : Fin 3) {p u : E} (hp : p ∈ P a) (hu : u ∈ A) :
    p + (1/2 : ℝ) • u ∈ B := by
  obtain ⟨x, hx, rfl⟩ := (mem_P_iff a p).1 hp
  obtain ⟨b, hb, rfl⟩ := hu
  have h := centeredChart_mem_B a
    (contractedPoint_add_half_small_simplex hx (barycentricPullback_mem a hb))
  convert h using 1
  ext i
  simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul, centeredChart,
    barycentricPullback]
  change contractedPoint x (cyclicCoordinate a i.castSucc) - 1/24 +
    (1/2 : ℝ) * ((1/10000 : ℝ) * b i) =
    contractedPoint x (cyclicCoordinate a i.castSucc) + (1/20000 : ℝ) *
    (lambda ((cyclicCoordinateEquiv a).symm (cyclicCoordinateEquiv a i.castSucc)) b - 1/24) - 1/24
  rw [Equiv.symm_apply_apply, lambda_castSucc]
  ring

/-- Second actual containment, including all source ordering inequalities. -/
theorem center_add_twice_A (a : Fin 3) {u : E} (hu : u ∈ A) :
    center a + (2 : ℝ) • u ∈ P a := by
  obtain ⟨b, hb, rfl⟩ := hu
  obtain ⟨x, hx, heq⟩ := sourceCenter_add_twice_small_simplex (barycentricPullback_mem a hb)
  apply (mem_P_iff a _).2
  refine ⟨x, hx, ?_⟩
  rw [heq]
  ext i
  simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul, centeredChart, center,
    barycentricPullback]
  change sourceCenter (cyclicCoordinate a i.castSucc) + (1/5000 : ℝ) *
    (lambda ((cyclicCoordinateEquiv a).symm (cyclicCoordinateEquiv a i.castSucc)) b - 1/24) - 1/24 =
    sourceCenter (cyclicCoordinate a i.castSucc) - 1/24 + (2 : ℝ) * ((1/10000 : ℝ) * b i)
  rw [Equiv.symm_apply_apply, lambda_castSucc]
  ring


/-- The centered source is the column simplex already measured in SourceGeometry. -/
theorem T_eq_translate_chartSimplex (a : Fin 3) :
    T a = (fun x => shift + x) '' chartSimplex (cyclicSourceMatrix a) := by
  change (chartAffine a) '' orderedSource = _
  rw [orderedSource_eq_convexHull, (chartAffine a).image_convexHull, ← Set.range_comp']
  have hr : range (fun v => chartAffine a (sourceVertex v)) =
      (fun x : E => shift + x) ''
        range (fun j i => cyclicSourceMatrix a (Fin.castSucc i) j) := by
    ext x
    constructor
    · rintro ⟨v, rfl⟩
      refine ⟨fun i => cyclicSourceMatrix a i.castSucc (finProdFinEquiv v),
        ⟨finProdFinEquiv v, rfl⟩, ?_⟩
      ext i
      simp [chartAffine, centeredChart, cyclicSourceMatrix, shift, sub_eq_add_neg, add_comm]
    · rintro ⟨y, ⟨j, rfl⟩, rfl⟩
      refine ⟨finProdFinEquiv.symm j, ?_⟩
      ext i
      simp [chartAffine, centeredChart, cyclicSourceMatrix, shift, sub_eq_add_neg, add_comm]
  rw [hr]
  exact ((AffineEquiv.constVAdd ℝ E shift).toAffineMap.image_convexHull _).symm

theorem T_volume (a : Fin 3) :
    volume (T a) = ENNReal.ofReal ((1/6 : ℝ)^8) * volume B := by
  rw [T_eq_translate_chartSimplex, volume_translate, cyclicSource_volume, ← B_volume]

theorem P_volume (a : Fin 3) :
    volume (P a) = ENNReal.ofReal ((103/104 : ℝ)^23) *
      ENNReal.ofReal ((1/6 : ℝ)^8) * volume B := by
  rw [P, volume.addHaar_image_homothety]
  simp only [Module.finrank_pi, Fintype.card_fin]
  rw [abs_of_nonneg (by positivity), T_volume, mul_assoc]

theorem A_volume : volume A = ENNReal.ofReal ((1/10000 : ℝ)^23) * volume B := by
  have hA : A = AffineMap.homothety (0 : E) (1/10000 : ℝ) '' B := by
    unfold A
    apply congrArg (fun f : E → E => f '' B)
    ext x i
    simp [AffineMap.homothety_apply]
  rw [hA, volume.addHaar_image_homothety]
  simp only [Module.finrank_pi, Fintype.card_fin]
  rw [abs_of_nonneg (by positivity)]

theorem f_P_missed (a : Fin 3) (j : Fin 24) (hj : ¬ isRoot a j)
    {p : E} (hp : p ∈ P a) : f j p ≤ -gap := by
  obtain ⟨x, hx, rfl⟩ := (mem_P_iff a p).1 hp
  rw [f_apply, lambda_centeredChart a (contractedPoint_mem_simplex hx).2,
    lambda_centeredChart a (contractedPoint_mem_simplex hx).2]
  exact contracted_missed_cyclic_cut hx a j hj

theorem f_center_missed (a : Fin 3) (j : Fin 24) (hj : ¬ isRoot a j) :
    f j (center a) ≤ -(1/48 : ℝ) := by
  rw [center, f_apply, lambda_centeredChart a sourceCenter_mem_orderedSource.1.2,
    lambda_centeredChart a sourceCenter_mem_orderedSource.1.2]
  obtain ⟨r, h | h⟩ := missed_edge_is_internal a j hj
  · rw [h.1, h.2, sourceCenter_internal_first]
  · rw [h.1, h.2, sourceCenter_internal_second]
    norm_num

/-- The fiber at a nonzero cube base with k selected indices. -/
def K (a : Fin 3) (k : ℕ) : Set E :=
  (fun p => (2 : ℝ) • p + ((k : ℝ) - 1) • center a) '' P a

theorem K_compact (a : Fin 3) (k : ℕ) : IsCompact (K a k) :=
  (P_compact a).image (by fun_prop)

theorem K_volume (a : Fin 3) (k : ℕ) :
    volume (K a k) = ENNReal.ofReal ((2 : ℝ)^23) * volume (P a) := by
  have heq : K a k =
      (fun x => ((k : ℝ) - 1) • center a + x) ''
        (AffineMap.homothety (0 : E) (2 : ℝ) '' P a) := by
    unfold K
    rw [Set.image_image]
    apply congrArg (fun f : E → E => f '' P a)
    ext p i
    simp [AffineMap.homothety_apply, add_comm]
  rw [heq, volume_translate, volume.addHaar_image_homothety]
  simp only [Module.finrank_pi, Fintype.card_fin]
  rw [abs_of_nonneg (by positivity)]

/-- The grouped Minkowski containment for a single average outer point.
Finite sums of k outer points are reduced to this by convexity of A. -/
theorem K_add_scaled_A (a : Fin 3) {k : ℕ} (hk : 1 ≤ k)
    {q u : E} (hq : q ∈ K a k) (hu : u ∈ A) :
    ∃ b ∈ B, q + (k : ℝ) • u = ((k : ℝ) + 1) • b := by
  obtain ⟨p, hp, rfl⟩ := hq
  rcases eq_or_lt_of_le hk with rfl | hk2
  · refine ⟨p + (1/2 : ℝ) • u, P_add_half_A a hp hu, ?_⟩
    ext i
    simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul, Nat.cast_one, sub_self,
      zero_mul, add_zero]
    ring
  · have hkreal : (1 : ℝ) < k := by exact_mod_cast hk2
    let t : ℝ := (k : ℝ) / (2 * ((k : ℝ) - 1))
    have ht : t ∈ Icc (0 : ℝ) 1 := by
      dsimp [t]
      constructor
      · positivity
      · apply (div_le_one (by linarith : 0 < 2 * ((k : ℝ) - 1))).2
        have hkreal2 : (2 : ℝ) ≤ k := by exact_mod_cast hk2
        linarith
    have hv : t • u ∈ A := A_convex.smul_mem_of_zero_mem zero_mem_A hu ht
    have hr : center a + (2 : ℝ) • (t • u) ∈ P a := center_add_twice_A a hv
    let b : E := (2 / ((k : ℝ) + 1)) • p +
      (((k : ℝ) - 1) / ((k : ℝ) + 1)) • (center a + (2 : ℝ) • (t • u))
    have hb : b ∈ P a := by
      apply P_convex a hp hr
      · positivity
      · positivity
      · field_simp
        ring
    refine ⟨b, P_subset_B a hb, ?_⟩
    ext i
    dsimp [b, t]
    field_simp [show ((k : ℝ) - 1) ≠ 0 by linarith,
      show ((k : ℝ) + 1) ≠ 0 by linarith]
    ring

theorem f_P_le_one (a : Fin 3) (j : Fin 24) {p : E} (hp : p ∈ P a) : f j p ≤ 1 :=
  (B_f_bounds (P_subset_B a hp) j).2

theorem f_center_le_one (a : Fin 3) (j : Fin 24) : f j (center a) ≤ 1 :=
  f_P_le_one a j (center_mem_P a)

theorem f_A_bounds (j : Fin 24) {u : E} (hu : u ∈ A) :
    -(1/10000 : ℝ) ≤ f j u ∧ f j u ≤ (1/10000 : ℝ) := by
  obtain ⟨b, hb, rfl⟩ := hu
  obtain ⟨hlo, hhi⟩ := B_f_bounds hb j
  rw [map_smul]
  change -(1/10000 : ℝ) ≤ (1/10000 : ℝ) * f j b ∧
    (1/10000 : ℝ) * f j b ≤ (1/10000 : ℝ)
  constructor <;> linarith

/-- The average of finitely many outer-fiber points is still in A. -/
theorem sum_A_eq_card_smul {ι : Type*} {s : Finset ι} (hs : s.Nonempty)
    (u : ι → E) (hu : ∀ i ∈ s, u i ∈ A) :
    ∃ b ∈ A, (∑ i ∈ s, u i) = (s.card : ℝ) • b := by
  have hcpos : (0 : ℝ) < s.card := by exact_mod_cast Finset.card_pos.mpr hs
  have hcne : (s.card : ℝ) ≠ 0 := ne_of_gt hcpos
  let b : E := (s.card : ℝ)⁻¹ • (∑ i ∈ s, u i)
  refine ⟨b, ?_, ?_⟩
  · have hb := A_convex.sum_mem (t := s) (w := fun _ => (s.card : ℝ)⁻¹)
      (z := u) (by intros; positivity) (by simp [nsmul_eq_mul, hcne]) hu
    simpa only [← Finset.smul_sum] using hb
  · dsimp [b]
    rw [smul_smul, mul_inv_cancel₀ hcne, one_smul]

/-- The finite-sum form needed to identify the origin fiber exactly. -/
theorem K_add_sum_A {ι : Type*} (a : Fin 3) {s : Finset ι} (hs : s.Nonempty)
    {q : E} (hq : q ∈ K a s.card) (u : ι → E) (hu : ∀ i ∈ s, u i ∈ A) :
    ∃ b ∈ B, q + (∑ i ∈ s, u i) = ((s.card : ℝ) + 1) • b := by
  obtain ⟨v, hv, heq⟩ := sum_A_eq_card_smul hs u hu
  rw [heq]
  exact K_add_scaled_A a (Finset.card_pos.mpr hs) hq hv

end SharpOC.SourceContainment
