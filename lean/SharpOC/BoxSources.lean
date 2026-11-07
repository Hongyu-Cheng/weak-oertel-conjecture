import SharpOC.MiddleSimplex
import SharpOC.BoxParameters
import SharpOC.TetrahedronVolume

/-! Actual tetrahedral source boxes for the 76-integer-coordinate example.
The source sets, affine images, interiors, ambient cuts, grouped origin
containments, and Lebesgue-volume identities are all proved here. -/

noncomputable section
open Set MeasureTheory
open scoped ENNReal Pointwise

namespace SharpOC.BoxSources
open BoxParameters

abbrev E0 := Fin 3 → ℝ

def shift : E0 := fun _ => -(1 / 4 : ℝ)
def basis : AffineBasis (Fin 4) ℝ E0 := shift +ᵥ MiddleSimplex.standardBasis 3
def B0 : Set E0 := convexHull ℝ (range basis)
def lambda (j : Fin 4) : E0 →ᵃ[ℝ] ℝ := basis.coord j

theorem lambda_castSucc (i : Fin 3) (x : E0) :
    lambda i.castSucc x = x i + 1 / 4 := by
  simp [lambda, basis, AffineBasis.coord_vadd,
    MiddleSimplex.standardBasis_coord_castSucc, shift, add_comm]

theorem lambda_last (x : E0) : lambda (Fin.last 3) x = 1 / 4 - ∑ i, x i := by
  change ((shift +ᵥ MiddleSimplex.standardBasis 3).coord (Fin.last 3)) x = _
  rw [AffineBasis.coord_vadd]
  change (MiddleSimplex.standardBasis 3).coord (Fin.last 3) (-shift + x) = _
  rw [MiddleSimplex.standardBasis_coord_last]
  simp [shift, Finset.sum_add_distrib]
  ring

@[simp] theorem lambda_0 (x : E0) : lambda 0 x = x 0 + 1/4 := lambda_castSucc 0 x
@[simp] theorem lambda_1 (x : E0) : lambda 1 x = x 1 + 1/4 := lambda_castSucc 1 x
@[simp] theorem lambda_2 (x : E0) : lambda 2 x = x 2 + 1/4 := lambda_castSucc 2 x
@[simp] theorem lambda_3 (x : E0) : lambda 3 x = 1/4 - ∑ i, x i := lambda_last x

@[simp] theorem lambda_zero (j : Fin 4) : lambda j 0 = 1 / 4 := by
  rcases Fin.eq_castSucc_or_eq_last j with ⟨i, rfl⟩ | rfl
  · rw [lambda_castSucc]; simp
  · rw [lambda_last]; simp

theorem lambda_sum (x : E0) : ∑ j, lambda j x = 1 := basis.sum_coord_apply_eq_one x
theorem B0_eq_nonneg_lambda : B0 = {x | ∀ j, 0 ≤ lambda j x} :=
  basis.convexHull_eq_nonneg_coord

theorem B0_lambda_nonneg {x : E0} (hx : x ∈ B0) (j : Fin 4) : 0 ≤ lambda j x := by
  rw [B0_eq_nonneg_lambda] at hx
  exact hx j

theorem B0_lambda_le_one {x : E0} (hx : x ∈ B0) (j : Fin 4) : lambda j x ≤ 1 := by
  have h := Finset.single_le_sum (fun k _ => B0_lambda_nonneg hx k) (Finset.mem_univ j)
  rwa [lambda_sum] at h

theorem B0_compact : IsCompact B0 := (Set.finite_range basis).isCompact_convexHull ℝ
theorem B0_convex : Convex ℝ B0 := convex_convexHull ℝ _
theorem zero_mem_interior_B0 : (0 : E0) ∈ interior B0 := by
  rw [B0, basis.interior_convexHull]
  intro j
  change 0 < lambda j 0
  rw [lambda_zero]
  norm_num

theorem B0_volume_pos : 0 < volume B0 :=
  Measure.measure_pos_of_nonempty_interior volume ⟨0, zero_mem_interior_B0⟩
theorem B0_volume_ne_top : volume B0 ≠ ⊤ := B0_compact.measure_ne_top

def f (j : Fin 4) : E0 →L[ℝ] ℝ := (lambda j).linear.toContinuousLinearMap

theorem f_apply (j : Fin 4) (x : E0) : f j x = lambda j x - 1 / 4 := by
  have h := congrFun (lambda j).decomp x
  simp only [Pi.add_apply, lambda_zero] at h
  change (lambda j).linear x = _
  linarith

theorem f_nonzero (j : Fin 4) : f j ≠ 0 := by
  intro h
  apply simplex_coord_linear_ne_zero (by norm_num : 0 < 3) basis j
  apply LinearMap.ext
  intro x
  exact congrArg (fun g : E0 →L[ℝ] ℝ => g x) h

theorem f_sum (x : E0) : ∑ j, f j x = 0 := by
  simp_rw [f_apply]
  rw [Finset.sum_sub_distrib, lambda_sum]
  norm_num

theorem cuts_cover (x : E0) : ∃ j, 0 ≤ f j x := by
  by_contra h
  push Not at h
  have hs := Finset.sum_lt_sum_of_nonempty Finset.univ_nonempty (fun j _ => h j)
  simp [f_sum] at hs

theorem B0_f_bounds {x : E0} (hx : x ∈ B0) (j : Fin 4) :
    -1 ≤ f j x ∧ f j x ≤ 1 := by
  rw [f_apply]
  have h0 := B0_lambda_nonneg hx j
  have h1 := B0_lambda_le_one hx j
  constructor <;> linarith

theorem cap_volume (j : Fin 4) :
    volume (B0 ∩ {x | 0 ≤ f j x}) = ENNReal.ofReal (27/64 : ℝ) * volume B0 := by
  have hs : {x : E0 | 0 ≤ f j x} = {x | (1/4 : ℝ) ≤ basis.coord j x} := by
    ext x
    rw [Set.mem_ofPred_eq, f_apply]
    change _ ↔ (1/4 : ℝ) ≤ lambda j x
    constructor <;> intro h <;> linarith
  rw [hs]
  convert simplex_cap_measure basis volume j (by norm_num : (0:ℝ) ≤ 1/4)
    (by norm_num : (1/4:ℝ) < 1) using 1 <;> norm_num [B0, E0]

def T (a : Fin 4) : Set E0 := {x | x ∈ B0 ∧ ∀ j, j ≠ a → lambda j x ≤ 1/4}

theorem T_subset_B0 (a : Fin 4) : T a ⊆ B0 := fun _ hx => hx.1

theorem T_f_missed (a j : Fin 4) (hj : j ≠ a) {x : E0} (hx : x ∈ T a) :
    f j x ≤ 0 := by
  rw [f_apply]
  linarith [hx.2 j hj]

def swapMatrix (a : Fin 4) : Matrix (Fin 3) (Fin 3) ℝ :=
  fun i j => if a = i.castSucc then -1 else if i = j then 1 else 0

def swapMap (a : Fin 4) : E0 →ₗ[ℝ] E0 := Matrix.toLin' (swapMatrix a)

theorem lambda_swapMap (a j : Fin 4) (x : E0) :
    lambda j (swapMap a x) = lambda ((Equiv.swap a (Fin.last 3)) j) x := by
  fin_cases a <;> fin_cases j <;>
    simp [swapMap, swapMatrix, Matrix.toLin'_apply, Matrix.mulVec, dotProduct,
      Fin.sum_univ_succ, Equiv.swap_apply_def] <;> ring

theorem lambda_injective {x y : E0} (h : ∀ j, lambda j x = lambda j y) : x = y := by
  ext i
  have hi := h i.castSucc
  rw [lambda_castSucc, lambda_castSucc] at hi
  linarith

theorem swapMap_involutive (a : Fin 4) : Function.Involutive (swapMap a) := by
  intro x
  apply lambda_injective
  intro j
  rw [lambda_swapMap, lambda_swapMap, Equiv.swap_apply_self]

theorem swapMap_abs_det (a : Fin 4) : |LinearMap.det (swapMap a)| = 1 := by
  have hc : (swapMap a).comp (swapMap a) = LinearMap.id := by
    apply LinearMap.ext
    intro x
    exact swapMap_involutive a x
  have hd := congrArg LinearMap.det hc
  rw [LinearMap.det_comp, LinearMap.det_id] at hd
  have ha := congrArg abs hd
  rw [abs_mul, abs_one] at ha
  nlinarith [abs_nonneg (LinearMap.det (swapMap a))]

def cube : Set E0 := Icc (fun _ => -(1/4 : ℝ)) 0

theorem T_last_eq_cube : T (Fin.last 3) = cube := by
  ext x
  constructor
  · intro hx
    constructor
    · intro i
      have h := B0_lambda_nonneg hx.1 i.castSucc
      rw [lambda_castSucc] at h
      change -(1/4 : ℝ) ≤ x i
      linarith
    · intro i
      have h := hx.2 i.castSucc (Fin.castSucc_ne_last i)
      rw [lambda_castSucc] at h
      change x i ≤ 0
      linarith
  · rintro ⟨hl, hu⟩
    constructor
    · rw [B0_eq_nonneg_lambda]
      intro j
      rcases Fin.eq_castSucc_or_eq_last j with ⟨i,rfl⟩ | rfl
      · rw [lambda_castSucc]
        have h := hl i
        change -(1/4 : ℝ) ≤ x i at h
        linarith
      · rw [lambda_last]
        have hsum : ∑ i, x i ≤ 0 := by
          simpa using Finset.sum_nonpos (fun i _ => hu i)
        linarith
    · intro j hj
      obtain ⟨i, rfl⟩ := Fin.eq_castSucc_of_ne_last hj
      rw [lambda_castSucc]
      have h := hu i
      change x i ≤ 0 at h
      linarith

theorem swapMap_mem_T (a b : Fin 4) {x : E0} (hx : x ∈ T b) :
    swapMap a x ∈ T ((Equiv.swap a (Fin.last 3)) b) := by
  constructor
  · rw [B0_eq_nonneg_lambda]
    intro j
    rw [lambda_swapMap]
    exact B0_lambda_nonneg hx.1 _
  · intro j hj
    rw [lambda_swapMap]
    apply hx.2
    intro he
    apply hj
    have hh := congrArg (Equiv.swap a (Fin.last 3)) he
    simpa using hh

theorem T_eq_image_cube (a : Fin 4) : T a = swapMap a '' cube := by
  rw [← T_last_eq_cube]
  ext x
  constructor
  · intro hx
    refine ⟨swapMap a x, ?_, swapMap_involutive a x⟩
    simpa using swapMap_mem_T a a hx
  · rintro ⟨y, hy, rfl⟩
    simpa using swapMap_mem_T a (Fin.last 3) hy

theorem T_compact (a : Fin 4) : IsCompact (T a) := by
  rw [T_eq_image_cube]
  exact isCompact_Icc.image (swapMap a).continuous_of_finiteDimensional

theorem T_convex (a : Fin 4) : Convex ℝ (T a) := by
  rw [T_eq_image_cube]
  exact (convex_Icc _ _).linear_image (swapMap a)

theorem T_absolute_volume (a : Fin 4) : volume (T a) = ENNReal.ofReal (1/64 : ℝ) := by
  rw [T_eq_image_cube, Measure.addHaar_image_linearMap, swapMap_abs_det]
  norm_num [cube, Real.volume_Icc_pi, Fin.prod_univ_succ]
  rw [← ENNReal.ofReal_pow (by norm_num : (0:ℝ) ≤ 1/4)]
  norm_num

def center (a : Fin 4) : E0 :=
  fun i => if a = i.castSucc then 3 * epsilon else -epsilon

theorem center_lambda (a j : Fin 4) :
    lambda j (center a) = if j = a then 1/4 + 3*epsilon else 1/4-epsilon := by
  fin_cases a <;> fin_cases j <;> simp [center, Fin.sum_univ_succ] <;> ring

theorem center_mem_T (a : Fin 4) : center a ∈ T a := by
  constructor
  · rw [B0_eq_nonneg_lambda]
    intro j
    rw [center_lambda]
    split_ifs <;> nlinarith [epsilon_pos, epsilon_lt_quarter]
  · intro j hj
    rw [center_lambda, ite_eq_right hj]
    linarith [epsilon_pos]

theorem center_mem_B0 (a : Fin 4) : center a ∈ B0 := (center_mem_T a).1

theorem f_center_missed (a j : Fin 4) (hj : j ≠ a) : f j (center a) = -epsilon := by
  rw [f_apply, center_lambda, ite_eq_right hj]
  ring

theorem f_center_paid (a : Fin 4) : f a (center a) = 3 * epsilon := by
  rw [f_apply, center_lambda, ite_eq_left rfl]
  ring

theorem center_mem_interior_T (a : Fin 4) : center a ∈ interior (T a) := by
  apply mem_interior_iff_mem_nhds.mpr
  have hpos : ∀ᶠ x in nhds (center a), ∀ j, 0 < lambda j x := by
    apply Filter.eventually_all.mpr
    intro j
    apply (isOpen_lt continuous_const (lambda j).continuous_of_finiteDimensional).mem_nhds
    rw [Set.mem_ofPred_eq, center_lambda]
    split_ifs <;> nlinarith [epsilon_pos, epsilon_lt_quarter]
  have hu : ∀ᶠ x in nhds (center a), ∀ j, j ≠ a → lambda j x < 1/4 := by
    apply Filter.eventually_all.mpr
    intro j
    by_cases hj : j = a
    · exact Filter.Eventually.of_forall (by simp [hj])
    · have hh : ∀ᶠ x in nhds (center a), lambda j x < 1/4 := by
        apply (isOpen_lt (lambda j).continuous_of_finiteDimensional continuous_const).mem_nhds
        rw [Set.mem_ofPred_eq, center_lambda, ite_eq_right hj]
        linarith [epsilon_pos]
      exact hh.mono (fun _ hx _ => hx)
  filter_upwards [hpos, hu] with x hx hu
  constructor
  · rw [B0_eq_nonneg_lambda]
    exact fun j => (hx j).le
  · exact fun j hj => (hu j hj).le

def P (a : Fin 4) : Set E0 := AffineMap.homothety (center a) s '' T a
def A (a : Fin 4) : Set E0 := (fun x => t • (x - center a)) '' T a
def K (a : Fin 4) (k : ℕ) : Set E0 :=
  (fun p => (2 : ℝ) • p + ((k : ℝ) - 1) • center a) '' P a

theorem P_compact (a : Fin 4) : IsCompact (P a) :=
  (T_compact a).image (AffineMap.homothety (center a) s).continuous_of_finiteDimensional
theorem A_compact (a : Fin 4) : IsCompact (A a) := (T_compact a).image (by fun_prop)
theorem K_compact (a : Fin 4) (k : ℕ) : IsCompact (K a k) :=
  (P_compact a).image (by fun_prop)
theorem P_convex (a : Fin 4) : Convex ℝ (P a) :=
  (T_convex a).affine_image (AffineMap.homothety (center a) s)

theorem A_convex (a : Fin 4) : Convex ℝ (A a) := by
  let F : E0 →ᵃ[ℝ] E0 := t • (AffineMap.id ℝ E0 - AffineMap.const ℝ E0 (center a))
  exact (T_convex a).affine_image F

theorem K_convex (a : Fin 4) (k : ℕ) : Convex ℝ (K a k) := by
  let F : E0 →ᵃ[ℝ] E0 := (2:ℝ) • AffineMap.id ℝ E0 +
    AffineMap.const ℝ E0 (((k:ℝ)-1) • center a)
  exact (P_convex a).affine_image F

theorem P_subset_B0 (a : Fin 4) : P a ⊆ B0 := by
  rintro x ⟨y, hy, rfl⟩
  have h := B0_convex (center_mem_B0 a) hy.1 (by linarith [s_lt_one]) s_pos.le
    (by ring : 1-s+s=1)
  convert h using 1
  simp [AffineMap.homothety_apply]
  module

theorem center_mem_P (a : Fin 4) : center a ∈ P a :=
  ⟨center a, center_mem_T a, by simp⟩

theorem center_mem_interior_P (a : Fin 4) : center a ∈ interior (P a) := by
  have h := (AffineMap.homothety_isOpenMap (center a) s s_pos.ne').image_interior_subset (T a)
  exact h ⟨center a, center_mem_interior_T a, by simp⟩

theorem zero_mem_interior_A (a : Fin 4) : (0 : E0) ∈ interior (A a) := by
  have hopen : IsOpenMap (fun x : E0 => t • (x - center a)) :=
    (isOpenMap_smul₀ t_pos.ne').comp (isOpenMap_sub_right (center a))
  exact hopen.image_interior_subset (T a)
    ⟨center a, center_mem_interior_T a, by simp⟩

theorem zero_mem_A (a : Fin 4) : (0 : E0) ∈ A a := interior_subset (zero_mem_interior_A a)

theorem K_interior_nonempty (a : Fin 4) (k : ℕ) : (interior (K a k)).Nonempty := by
  have hopen : IsOpenMap (fun p : E0 => (2:ℝ) • p + ((k:ℝ)-1) • center a) :=
    (isOpenMap_add_right _).comp (isOpenMap_smul₀ (by norm_num : (2:ℝ) ≠ 0))
  exact ⟨_, hopen.image_interior_subset (P a)
    ⟨center a, center_mem_interior_P a, rfl⟩⟩

theorem lambda_decomp (j : Fin 4) (x : E0) : lambda j x = f j x + 1/4 := by
  rw [f_apply]
  ring

theorem center_lambda_bounds (a j : Fin 4) :
    1/4-epsilon ≤ lambda j (center a) ∧ lambda j (center a) ≤ 1/4+3*epsilon := by
  rw [center_lambda]
  split_ifs <;> constructor <;> linarith [epsilon_pos]

theorem lambda_homothety (a j : Fin 4) (x : E0) :
    lambda j (AffineMap.homothety (center a) s x) =
      s * (lambda j x - lambda j (center a)) + lambda j (center a) := by
  rw [AffineMap.homothety_apply, AffineMap.map_vadd, map_smul, AffineMap.linearMap_vsub]
  rfl

theorem lambda_P_lower (a j : Fin 4) {p : E0} (hp : p ∈ P a) :
    (1-s)*lambda j (center a) ≤ lambda j p := by
  obtain ⟨x, hx, rfl⟩ := hp
  rw [lambda_homothety]
  nlinarith [B0_lambda_nonneg hx.1 j, s_pos]

theorem f_A_lower (a j : Fin 4) {v : E0} (hv : v ∈ A a) :
    -t * lambda j (center a) ≤ f j v := by
  obtain ⟨x, hx, rfl⟩ := hv
  rw [map_smul, map_sub, f_apply, f_apply]
  simp only [smul_eq_mul]
  nlinarith [B0_lambda_nonneg hx.1 j, t_pos]

theorem f_P_missed (a j : Fin 4) (hj : j ≠ a) {p : E0} (hp : p ∈ P a) :
    f j p ≤ -(1-s)*epsilon := by
  obtain ⟨x, hx, rfl⟩ := hp
  rw [AffineMap.homothety_apply]
  change f j (s • (x - center a) + center a) ≤ _
  rw [map_add, map_smul, map_sub, f_center_missed a j hj]
  simp only [smul_eq_mul]
  nlinarith [T_f_missed a j hj hx, s_pos]

theorem f_A_missed (a j : Fin 4) (hj : j ≠ a) {v : E0} (hv : v ∈ A a) :
    f j v ≤ t * epsilon := by
  obtain ⟨x, hx, rfl⟩ := hv
  rw [map_smul, map_sub, f_center_missed a j hj]
  simp only [smul_eq_mul]
  nlinarith [T_f_missed a j hj hx, t_pos]

theorem f_A_bounds (a j : Fin 4) {v : E0} (hv : v ∈ A a) :
    -2*t ≤ f j v ∧ f j v ≤ 2*t := by
  obtain ⟨x, hx, rfl⟩ := hv
  rw [map_smul, map_sub]
  simp only [smul_eq_mul]
  have hx := B0_f_bounds hx.1 j
  have hc := B0_f_bounds (center_mem_B0 a) j
  constructor <;> nlinarith [t_pos]

theorem f_K_missed (a j : Fin 4) (hj : j ≠ a) (k : ℕ) {x : E0} (hx : x ∈ K a k) :
    f j x ≤ -((k:ℝ)+1-2*s)*epsilon := by
  obtain ⟨p, hp, rfl⟩ := hx
  rw [map_add, map_smul, map_smul, f_center_missed a j hj]
  simp only [smul_eq_mul]
  nlinarith [f_P_missed a j hj hp]

theorem f_K_le (a j : Fin 4) (k : ℕ) (hk : 1 ≤ k) {x : E0} (hx : x ∈ K a k) :
    f j x ≤ (k:ℝ)+1 := by
  obtain ⟨p, hp, rfl⟩ := hx
  rw [map_add, map_smul, map_smul]
  simp only [smul_eq_mul]
  have hc := (B0_f_bounds (center_mem_B0 a) j).2
  have hp := (B0_f_bounds (P_subset_B0 a hp) j).2
  have hk' : (1:ℝ) ≤ k := by exact_mod_cast hk
  nlinarith

/-- The chosen rational parameters satisfy this stronger inequality, allowing
arbitrary source types even in a singleton origin group. -/
theorem all_type_origin_margin :
    t*(1/4+3*epsilon) ≤ 2*(1-s)*(1/4-epsilon) := by
  norm_num [t,s,epsilon]

theorem K_add_sum_A {ι : Type*} (I : Finset ι) (hI : I.Nonempty)
    (a : Fin 4) (τ : ι → Fin 4) {x : E0} (hx : x ∈ K a I.card)
    (v : ι → E0) (hv : ∀ i ∈ I, v i ∈ A (τ i)) :
    ∃ b ∈ B0, x + ∑ i ∈ I, v i = ((I.card:ℝ)+1) • b := by
  classical
  obtain ⟨p, hp, rfl⟩ := hx
  have hk : (1:ℝ) ≤ I.card := by exact_mod_cast hI.card_pos
  have hkpos : (0:ℝ) < (I.card:ℝ)+1 := by positivity
  let b : E0 := ((I.card:ℝ)+1)⁻¹ •
    ((2:ℝ) • p + ((I.card:ℝ)-1) • center a + ∑ i ∈ I, v i)
  refine ⟨b, ?_, ?_⟩
  · rw [B0_eq_nonneg_lambda]
    intro j
    have hsum : -(I.card:ℝ)*t*(1/4+3*epsilon) ≤ ∑ i ∈ I, f j (v i) := by
      calc
        _ = ∑ _i ∈ I, (-t*(1/4+3*epsilon)) := by simp; ring
        _ ≤ _ := Finset.sum_le_sum (fun i hi => by
          have hl := f_A_lower (τ i) j (hv i hi)
          have hc := (center_lambda_bounds (τ i) j).2
          nlinarith [t_pos])
    have hrel : ((I.card:ℝ)+1) * lambda j b =
        2*lambda j p + ((I.card:ℝ)-1)*lambda j (center a) + ∑ i ∈ I, f j (v i) := by
      simp only [b, lambda_decomp, map_smul, map_add, map_sum, smul_eq_mul]
      field_simp
      ring
    have hpl := lambda_P_lower a j hp
    have hcl := (center_lambda_bounds a j).1
    have hfactor : 0 ≤ (I.card:ℝ)+1-2*s := by linarith [s_lt_one]
    have hm := mul_le_mul_of_nonneg_left hcl hfactor
    have ht := mul_le_mul_of_nonneg_left all_type_origin_margin (by positivity : 0 ≤ (I.card:ℝ))
    have hnonneg : 0 ≤ ((I.card:ℝ)-1)*(2*s-1)*(1/4-epsilon) := by
      apply mul_nonneg
      · exact mul_nonneg (by linarith) (by linarith [half_lt_s])
      · linarith [epsilon_lt_quarter]
    nlinarith
  · dsimp [b]
    rw [smul_smul, mul_inv_cancel₀ hkpos.ne', one_smul]

theorem B0_eq_translate_standard :
    B0 = (fun x => shift + x) '' SourceGeometry.standardSimplex 3 := by
  unfold B0 SourceGeometry.standardSimplex
  rw [← MiddleSimplex.standardVertex_range]
  have hr : range basis = (fun x => shift+x) '' range (MiddleSimplex.standardVertex 3) := by
    rw [← Set.range_comp]
    rfl
  rw [hr]
  exact ((AffineEquiv.constVAdd ℝ E0 shift).toAffineMap.image_convexHull _).symm

theorem B0_volume_standard : volume B0 = volume (SourceGeometry.standardSimplex 3) := by
  rw [B0_eq_translate_standard, SourceGeometry.volume_translate]

theorem P_volume_in_T (a : Fin 4) :
    volume (P a) = ENNReal.ofReal (s^3) * volume (T a) := by
  rw [P, volume.addHaar_image_homothety]
  simp only [Module.finrank_pi, Fintype.card_fin]
  rw [abs_of_nonneg (pow_nonneg s_pos.le 3)]

theorem A_volume_in_T (a : Fin 4) :
    volume (A a) = ENNReal.ofReal (t^3) * volume (T a) := by
  have ha : A a = (fun x => -(t • center a) + x) ''
      (AffineMap.homothety (0:E0) t '' T a) := by
    rw [Set.image_image]
    apply congrArg (fun F : E0 → E0 => F '' T a)
    ext x i
    simp [AffineMap.homothety_apply, Pi.smul_apply, smul_eq_mul]
    ring
  rw [ha, SourceGeometry.volume_translate, volume.addHaar_image_homothety]
  simp only [Module.finrank_pi, Fintype.card_fin]
  rw [abs_of_nonneg (pow_nonneg t_pos.le 3)]

theorem K_volume_in_T (a : Fin 4) (k : ℕ) :
    volume (K a k) = ENNReal.ofReal ((2*s)^3) * volume (T a) := by
  have hk : K a k = (fun x => ((k:ℝ)-1) • center a + x) ''
      (AffineMap.homothety (0:E0) (2:ℝ) '' P a) := by
    rw [Set.image_image]
    apply congrArg (fun F : E0 → E0 => F '' P a)
    ext x i
    simp [AffineMap.homothety_apply, Pi.smul_apply, smul_eq_mul]
    ring
  rw [hk, SourceGeometry.volume_translate, volume.addHaar_image_homothety]
  simp only [Module.finrank_pi, Fintype.card_fin]
  rw [P_volume_in_T, ← mul_assoc, ← ENNReal.ofReal_mul (by norm_num)]
  congr 2
  norm_num
  ring

theorem B0_volume : volume B0 = ENNReal.ofReal (1/6 : ℝ) := by
  rw [B0_volume_standard, TetrahedronVolume.volume_standardSimplex_three]

theorem T_volume (a : Fin 4) : volume (T a) = ENNReal.ofReal theta * volume B0 := by
  rw [T_absolute_volume, B0_volume, ← ENNReal.ofReal_mul theta_pos.le]
  norm_num [theta]

theorem P_volume (a : Fin 4) :
    volume (P a) = ENNReal.ofReal (s^3*theta) * volume B0 := by
  rw [P_volume_in_T, T_volume, ← mul_assoc, ← ENNReal.ofReal_mul (pow_nonneg s_pos.le 3)]

theorem A_volume (a : Fin 4) :
    volume (A a) = ENNReal.ofReal (t^3*theta) * volume B0 := by
  rw [A_volume_in_T, T_volume, ← mul_assoc, ← ENNReal.ofReal_mul (pow_nonneg t_pos.le 3)]

theorem K_volume (a : Fin 4) (k : ℕ) :
    volume (K a k) = ENNReal.ofReal ((2*s)^3*theta) * volume B0 := by
  rw [K_volume_in_T, T_volume, ← mul_assoc,
    ← ENNReal.ofReal_mul (pow_nonneg (mul_nonneg (by norm_num) s_pos.le) 3)]

end SharpOC.BoxSources
