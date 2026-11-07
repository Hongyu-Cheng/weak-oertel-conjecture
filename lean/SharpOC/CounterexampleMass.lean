import SharpOC.ConcreteBody
import SharpOC.MiddleCuts
import SharpOC.SourceBasis
import SharpOC.Halfspaces

noncomputable section
open Set MeasureTheory
open scoped ENNReal BigOperators

namespace SharpOC.Counterexample
open MiddleSimplex SourceContainment

def b : ℝ := (volume B).toReal
def M : ℝ := 4 * b * massRatio

def totalMass : ℝ := ∑ a : FiberIndex, (volume (fiber a)).toReal

def cutMass (F : AmbientSpace →L[ℝ] ℝ) (t : ℝ) : ℝ :=
  ∑ a : FiberIndex, (volume (fiber a ∩ {x | t ≤ F (base a, x)})).toReal

theorem b_pos : 0 < b := ENNReal.toReal_pos B_volume_pos.ne' B_volume_ne_top

theorem M_pos : 0 < M := by
  unfold M
  exact mul_pos (by linarith [b_pos]) massRatio_pos

theorem copies_pos : 0 < copies := by unfold copies; positivity

theorem copies_real_pos : (0 : ℝ) < copies := Nat.cast_pos.mpr copies_pos

theorem A_real_volume : (volume A).toReal = b / copies := by
  rw [A_volume, ENNReal.toReal_mul, ENNReal.toReal_ofReal (by positivity)]
  norm_num [b, copies]
  ring

theorem K_real_volume (a : Fin 3) (k : ℕ) : (volume (K a k)).toReal = M := by
  rw [K_volume, P_volume]
  simp only [ENNReal.toReal_mul]
  rw [ENNReal.toReal_ofReal (by positivity), ENNReal.toReal_ofReal (by positivity),
    ENNReal.toReal_ofReal (by positivity)]
  change (2 : ℝ)^23 * ((103/104 : ℝ)^23 * (1/6 : ℝ)^8 * b) = 4*b*massRatio
  have h := source_volume_coefficient
  unfold contraction at h
  calc
    _ = ((2 : ℝ)^23 * (103/104 : ℝ)^23 / (6^8)) * b := by ring
    _ = _ := by rw [h]; ring

theorem coreFiber_real_volume (S : Finset IntegerCoordinate) :
    (volume (coreFiber S)).toReal = if S = ∅ then b else M := by
  classical
  by_cases hs : S = ∅
  · simp [hs, b]
  · simp [coreFiber, hs, K_real_volume]

theorem totalMass_eq : totalMass = (2 : ℝ)^integerDimension*M + (4*b - M) := by
  classical
  have hc : (∑ S : Finset IntegerCoordinate, (volume (coreFiber S)).toReal) =
      (2 : ℝ)^integerDimension*M + (b-M) := by
    calc
      _ = ∑ S : Finset IntegerCoordinate, (M + if S = ∅ then b-M else 0) := by
        apply Finset.sum_congr rfl
        intro S hS
        rw [coreFiber_real_volume]
        split_ifs <;> ring
      _ = _ := by
        rw [Finset.sum_add_distrib]
        simp only [Finset.sum_const, Finset.card_univ, core_fiber_count,
          nsmul_eq_mul, Nat.cast_pow, Nat.cast_ofNat, Finset.sum_ite_eq',
          Finset.mem_univ, ite_true]
  have ho : (∑ _i : IntegerCoordinate, (volume A).toReal) = 3*b := by
    rw [A_real_volume]
    simp only [Finset.sum_const, Finset.card_univ, integerCoordinate_card, nsmul_eq_mul]
    rw [integerDimension]
    push_cast
    field_simp [copies_real_pos.ne']
  unfold totalMass
  rw [Fintype.sum_sum_type]
  change (∑ S : Finset IntegerCoordinate, (volume (coreFiber S)).toReal) +
    (∑ _i : IntegerCoordinate, (volume A).toReal) = _
  rw [hc, ho]
  ring

theorem middle_core_cut_volume (j : Fin 24) (S : Finset IntegerCoordinate) :
    (volume (fiber (.inl S) ∩ {x | 0 ≤ middleCut j (base (.inl S), x)})).toReal =
      if S = ∅ then b/2 else 0 := by
  classical
  by_cases hs : S = ∅
  · subst S
    simp only [fiber_inl, coreFiber_empty, base_empty, if_pos rfl,
      middleCut_middle_volume, ENNReal.toReal_div]
    norm_num [b]
  · have hempty : fiber (.inl S) ∩ {x | 0 ≤ middleCut j (base (.inl S), x)} = ∅ := by
      apply eq_empty_iff_forall_notMem.mpr
      rintro x ⟨hx, hc⟩
      have hS := Finset.nonempty_iff_ne_empty.mpr hs
      rw [fiber_inl, coreFiber_of_nonempty S hS] at hx
      exact (not_le_of_gt (middleCut_excludes_core j S hS hx)) hc
    rw [hempty]
    simp only [measure_empty, ENNReal.toReal_zero, if_neg hs]

theorem middle_outer_cut_volume (j : Fin 24) (i : IntegerCoordinate) :
    (volume (fiber (.inr i) ∩ {x | 0 ≤ middleCut j (base (.inr i), x)})).toReal =
      if paid j i then b/copies else 0 := by
  classical
  by_cases hp : paid j i
  · have heq : fiber (.inr i) ∩ {x | 0 ≤ middleCut j (base (.inr i), x)} = A := by
      ext x
      change (x ∈ A ∧ 0 ≤ middleCut j (negativeUnit i, x)) ↔ x ∈ A
      exact ⟨And.left, fun hx => ⟨hx, (middleCut_outer_iff j i hx).mpr hp⟩⟩
    simp only [heq, if_pos hp, A_real_volume]
  · have hempty : fiber (.inr i) ∩ {x | 0 ≤ middleCut j (base (.inr i), x)} = ∅ := by
      apply eq_empty_iff_forall_notMem.mpr
      rintro x ⟨hx, hc⟩
      exact hp ((middleCut_outer_iff j i hx).mp hc)
    rw [hempty]
    simp only [measure_empty, ENNReal.toReal_zero, if_neg hp]

theorem middle_cut_mass (j : Fin 24) : cutMass (middleCut j) 0 = 3*b/2 := by
  classical
  unfold cutMass
  rw [Fintype.sum_sum_type]
  simp_rw [middle_core_cut_volume, middle_outer_cut_volume]
  rw [paid_sum]
  simp only [Finset.sum_ite_eq', Finset.mem_univ, if_true]
  field_simp [copies_real_pos.ne']
  ring

theorem b_lt_M : b < M := by
  have h1 : 3*b/2 < gamma*M := middle_mass_below_cap b b_pos
  have h2 : gamma*M < M := by
    have h := mul_lt_mul_of_pos_right gamma_lt_one M_pos
    simpa using h
  linarith [b_pos]

theorem A_real_volume_le_M : (volume A).toReal ≤ M := by
  rw [A_real_volume]
  apply le_trans _ b_lt_M.le
  apply (div_le_iff₀ copies_real_pos).mpr
  have hcopies : (1 : ℝ) ≤ copies := by exact_mod_cast copies_pos
  nlinarith [b_pos]

theorem endpoint_real_volume_le_M (a : FiberIndex) (ha : a ≠ .inl ∅) :
    (volume (fiber a)).toReal ≤ M := by
  cases a with
  | inl S =>
    have hs : S ≠ ∅ := fun h => ha (congrArg Sum.inl h)
    simp [fiber, coreFiber, hs, K_real_volume]
  | inr i => exact A_real_volume_le_M

theorem endpoint_affine_basis (a : FiberIndex) (ha : a ≠ .inl ∅) :
    ∃ q : AffineBasis (Fin 24) ℝ E, fiber a = convexHull ℝ (range q) := by
  cases a with
  | inl S =>
    have hs : S.Nonempty := Finset.nonempty_iff_ne_empty.mpr (fun h => ha (congrArg Sum.inl h))
    refine ⟨SourceBasis.KBasis (selectedType S) S.card, ?_⟩
    rw [SourceBasis.KBasis_hull, fiber_inl, coreFiber_of_nonempty S hs]
  | inr i => exact ⟨SourceBasis.ABasis, SourceBasis.ABasis_hull.symm⟩

theorem endpoint_exposing (a : FiberIndex) (ha : a ≠ .inl ∅) :
    ∃ ell : IntegerSpace →L[ℝ] ℝ,
      ∀ c, c ≠ a → ell (base c) < ell (base a) := by
  cases a with
  | inl S =>
    have hs : S.Nonempty := Finset.nonempty_iff_ne_empty.mpr (fun h => ha (congrArg Sum.inl h))
    refine ⟨(coordinateFunctional (cubeExposingCoefficients S)).toContinuousLinearMap, ?_⟩
    exact nonempty_cube_exposes_generator S hs
  | inr i =>
    refine ⟨(coordinateFunctional (negativeUnit i)).toContinuousLinearMap, ?_⟩
    exact negative_unit_exposes_generator i

theorem endpoint_small_cut (a : FiberIndex) (ha : a ≠ .inl ∅) (x : E) :
    ∃ F : AmbientSpace →L[ℝ] ℝ, ∃ t : ℝ,
      F ≠ 0 ∧ t ≤ F (base a, x) ∧ cutMass F t ≤ gamma*M := by
  obtain ⟨q, hq⟩ := endpoint_affine_basis a ha
  obtain ⟨ell, hexp⟩ := endpoint_exposing a ha
  obtain ⟨F, t, hF, htx, hmass⟩ := exposed_simplex_fiber_sum_mass
    (d := 23) (by norm_num) (by simp [E]) volume base fiber fiber_compact a ell hexp q hq x
  refine ⟨F, t, hF, htx, ?_⟩
  have hreal := congrArg ENNReal.toReal hmass
  rw [ENNReal.toReal_sum (fun c _ => measure_ne_top_of_subset inter_subset_left
    (fiber_compact c).measure_ne_top), ENNReal.toReal_mul,
    ENNReal.toReal_ofReal (by positivity)] at hreal
  have heq : cutMass F t = gamma * (volume (fiber a)).toReal := by
    simpa only [cutMass, gamma, Nat.cast_ofNat, show (23 : ℝ) + 1 = 24 by norm_num] using hreal
  rw [heq]
  exact mul_le_mul_of_nonneg_left (endpoint_real_volume_le_M a ha) gamma_pos.le

theorem every_fiber_point_small_cut (a : FiberIndex) (x : E) :
    ∃ F : AmbientSpace →L[ℝ] ℝ, ∃ t : ℝ,
      F ≠ 0 ∧ t ≤ F (base a, x) ∧ cutMass F t ≤ gamma*M := by
  by_cases ha : a = .inl ∅
  · subst a
    obtain ⟨j, hj⟩ := middleCut_cover x
    refine ⟨middleCut j, 0, middleCut_nonzero j, ?_, ?_⟩
    · simpa only [base_empty] using hj
    · rw [middle_cut_mass]
      exact (middle_mass_below_cap b b_pos).le
  · exact endpoint_small_cut a ha x

end SharpOC.Counterexample
