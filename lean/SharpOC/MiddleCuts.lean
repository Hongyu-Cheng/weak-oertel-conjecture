import SharpOC.FamilyCombinatorics
import SharpOC.SourceContainment

/-! The twenty-four actual ambient halfspaces used at the middle fiber. -/

noncomputable section
set_option maxRecDepth 4096
open Set MeasureTheory
open scoped BigOperators

namespace SharpOC
open MiddleSimplex SourceContainment

abbrev IntegerSpace := IntegerCoordinate → ℝ
abbrev AmbientSpace := IntegerSpace × MiddleSimplex.E

def middleCut (j : Fin 24) : AmbientSpace →L[ℝ] ℝ :=
  (coordinateFunctional (cutCoefficient j)).toContinuousLinearMap.comp
      (ContinuousLinearMap.fst ℝ IntegerSpace E) +
    (f j).comp (ContinuousLinearMap.snd ℝ IntegerSpace E)

theorem middleCut_apply (j : Fin 24) (z : IntegerSpace) (x : E) :
    middleCut j (z, x) = coordinateFunctional (cutCoefficient j) z + f j x := by
  simp only [middleCut, ContinuousLinearMap.add_apply, ContinuousLinearMap.comp_apply,
    ContinuousLinearMap.coe_fst', ContinuousLinearMap.coe_snd',
    LinearMap.coe_toContinuousLinearMap']

theorem middleCut_zero (j : Fin 24) (x : E) : middleCut j (0, x) = f j x := by
  simp [middleCut_apply]

theorem middleCut_nonzero (j : Fin 24) : middleCut j ≠ 0 := by
  intro hz
  apply f_nonzero j
  ext x
  have h := congrArg (fun F : AmbientSpace →L[ℝ] ℝ => F (0, x)) hz
  simpa only [middleCut_zero, ContinuousLinearMap.zero_apply] using h

theorem middleCut_cover (x : E) : ∃ j, 0 ≤ middleCut j (0, x) := by
  simpa only [middleCut_zero] using cyclic_cuts_cover x

theorem outer_f_bounds {x : E} (hx : x ∈ A) (j : Fin 24) :
    -(1 / 10000 : ℝ) ≤ f j x ∧ f j x ≤ (1 / 10000 : ℝ) := by
  obtain ⟨b, hb, rfl⟩ := hx
  have h := B_f_bounds hb j
  simp only [map_smul, smul_eq_mul]
  constructor <;> linarith [h.1, h.2]

theorem middleCut_outer_iff (j : Fin 24) (i : IntegerCoordinate)
    {x : E} (hx : x ∈ A) :
    0 ≤ middleCut j (negativeUnit i, x) ↔ paid j i := by
  rw [middleCut_apply, integer_cut_negative]
  have h := outer_f_bounds hx j
  by_cases hp : paid j i
  · simp only [cutCoefficient, if_pos hp, neg_neg, hp, iff_true]
    have hn : (0 : ℝ) ≤ integerDimension := by positivity
    dsimp [penalty]
    linarith [h.1]
  · simp only [cutCoefficient, if_neg hp, hp, iff_false]
    norm_num [tilt]
    linarith [h.2]

theorem source_f_upper (a : Fin 3) (k : ℕ) (hk : 1 ≤ k)
    {x : E} (hx : x ∈ K a k) (j : Fin 24) : f j x ≤ (k : ℝ) + 1 := by
  obtain ⟨p, hp, rfl⟩ := hx
  have hp' := (B_f_bounds (P_subset_B a hp) j).2
  have hc := (B_f_bounds (P_subset_B a (center_mem_P a)) j).2
  have hk' : (0 : ℝ) ≤ (k : ℝ) - 1 := by
    have hk'' : (1 : ℝ) ≤ k := by exact_mod_cast hk
    linarith
  simp only [map_add, map_smul, smul_eq_mul]
  nlinarith [mul_le_mul_of_nonneg_left hc hk']

theorem source_f_missed (a : Fin 3) (k : ℕ) (hk : 1 ≤ k)
    {x : E} (hx : x ∈ K a k) (j : Fin 24) (hj : ¬ SourceGeometry.isRoot a j) :
    f j x ≤ -2 * gap - ((k : ℝ) - 1) / 48 := by
  obtain ⟨p, hp, rfl⟩ := hx
  have hp' := f_P_missed a j hj hp
  have hc := f_center_missed a j hj
  have hk' : (0 : ℝ) ≤ (k : ℝ) - 1 := by
    have hk'' : (1 : ℝ) ≤ k := by exact_mod_cast hk
    linarith
  simp only [map_add, map_smul, smul_eq_mul]
  nlinarith [mul_le_mul_of_nonneg_left hc hk']

theorem middleCut_excludes_core (j : Fin 24) (S : Finset IntegerCoordinate)
    (hS : S.Nonempty) {x : E} (hx : x ∈ K (selectedType S) S.card) :
    middleCut j (cubeVector S, x) < 0 := by
  classical
  have hk : 1 ≤ S.card := hS.card_pos
  rw [middleCut_apply]
  by_cases hp : ∃ i ∈ S, paid j i
  · have hi := paid_integer_cut j S hp
    have hf := source_f_upper (selectedType S) S.card hk hx j
    have hneg := paid_cut_negative S.card integerDimension (cube_card_le_dimension S)
    dsimp [penalty] at hi
    linarith
  · have hm : ∀ i ∈ S, ¬ paid j i := by simpa only [not_exists, not_and] using hp
    rw [unpaid_integer_cut j S hm]
    have hf := source_f_missed (selectedType S) S.card hk hx j (selectedType_misses S hS j hm)
    have hneg := unpaid_cut_negative S.card hk
    linarith

theorem middleCut_middle_volume (j : Fin 24) :
    volume (B ∩ {x | 0 ≤ middleCut j (0, x)}) = volume B / 2 := by
  simpa only [middleCut_zero] using positive_cap_volume j

end SharpOC
