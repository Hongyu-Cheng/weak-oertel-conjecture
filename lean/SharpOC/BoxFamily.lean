import SharpOC.BoxParameters
import SharpOC.LatticeGeometry

/-! The 76 integer coordinates and their four paid cut classes. -/

noncomputable section
open Finset
open scoped BigOperators

namespace SharpOC.BoxCounterexample

open BoxParameters

abbrev IntegerCoordinate := Fin 4 × Fin 19
abbrev FiberIndex := Sum (Finset IntegerCoordinate) IntegerCoordinate
abbrev IntegerSpace := IntegerCoordinate → ℝ

theorem integerCoordinate_card : Fintype.card IntegerCoordinate = 76 := by
  simp [IntegerCoordinate]

def selectedCoordinate (S : Finset IntegerCoordinate) (hS : S.Nonempty) :
    IntegerCoordinate := Classical.choose hS

theorem selectedCoordinate_mem (S : Finset IntegerCoordinate) (hS : S.Nonempty) :
    selectedCoordinate S hS ∈ S := Classical.choose_spec hS

def selectedType (S : Finset IntegerCoordinate) : Fin 4 :=
  if hS : S.Nonempty then (selectedCoordinate S hS).1 else 0

theorem selectedType_eq (S : Finset IntegerCoordinate) (hS : S.Nonempty) :
    selectedType S = (selectedCoordinate S hS).1 := by simp [selectedType, hS]

def paid (j : Fin 4) (i : IntegerCoordinate) : Prop := i.1 = j

instance paidDecidable (j : Fin 4) (i : IntegerCoordinate) : Decidable (paid j i) :=
  inferInstanceAs (Decidable (i.1 = j))

def penalty : ℝ := 3 * (76 + 1)

def cutCoefficient (j : Fin 4) (i : IntegerCoordinate) : ℝ :=
  if paid j i then -penalty else eta * epsilon

theorem penalty_pos : 0 < penalty := by norm_num [penalty]

theorem cutCoefficient_le_tilt (j : Fin 4) (i : IntegerCoordinate) :
    cutCoefficient j i ≤ eta * epsilon := by
  unfold cutCoefficient
  split_ifs
  · have hp := penalty_pos
    have he := mul_pos eta_pos epsilon_pos
    linarith
  · exact le_rfl

theorem selectedType_misses (S : Finset IntegerCoordinate) (hS : S.Nonempty)
    (j : Fin 4) (hmiss : ∀ i ∈ S, ¬ paid j i) : selectedType S ≠ j := by
  rw [selectedType_eq S hS]
  exact hmiss _ (selectedCoordinate_mem S hS)

theorem integer_cut_cube (j : Fin 4) (S : Finset IntegerCoordinate) :
    coordinateFunctional (cutCoefficient j) (cubeVector S) =
      ∑ i ∈ S, cutCoefficient j i := by
  classical
  simp [coordinateFunctional, cubeVector, mul_ite]

theorem integer_cut_negative (j : Fin 4) (i : IntegerCoordinate) :
    coordinateFunctional (cutCoefficient j) (negativeUnit i) = -cutCoefficient j i := by
  classical
  simp [coordinateFunctional, negativeUnit, mul_ite]

theorem unpaid_integer_cut (j : Fin 4) (S : Finset IntegerCoordinate)
    (hmiss : ∀ i ∈ S, ¬ paid j i) :
    coordinateFunctional (cutCoefficient j) (cubeVector S) =
      (S.card : ℝ) * (eta * epsilon) := by
  rw [integer_cut_cube]
  calc
    _ = ∑ _i ∈ S, eta * epsilon :=
      Finset.sum_congr rfl (fun i hi => by simp [cutCoefficient, hmiss i hi])
    _ = _ := by simp

theorem paid_integer_cut (j : Fin 4) (S : Finset IntegerCoordinate)
    (hpaid : ∃ i ∈ S, paid j i) :
    coordinateFunctional (cutCoefficient j) (cubeVector S) ≤
      -penalty + ((S.card : ℝ) - 1) * (eta * epsilon) := by
  classical
  obtain ⟨i, hi, hp⟩ := hpaid
  rw [integer_cut_cube, ← Finset.sum_erase_add _ _ hi]
  have hsum : (∑ k ∈ S.erase i, cutCoefficient j k) ≤
      ((S.erase i).card : ℝ) * (eta * epsilon) := by
    calc
      _ ≤ ∑ _k ∈ S.erase i, eta * epsilon :=
        Finset.sum_le_sum (fun k _ => cutCoefficient_le_tilt j k)
      _ = _ := by simp
  have hc : ((S.erase i).card : ℝ) = (S.card : ℝ) - 1 := by
    have hh : ((S.erase i).card : ℝ) + 1 = S.card := by
      exact_mod_cast Finset.card_erase_add_one hi
    linarith
  rw [show cutCoefficient j i = -penalty by simp [cutCoefficient, hp]]
  rw [hc] at hsum
  linarith

theorem cube_card_le_dimension (S : Finset IntegerCoordinate) : S.card ≤ 76 := by
  rw [← integerCoordinate_card]
  exact Finset.card_le_univ S

theorem paid_sum (j : Fin 4) (v : ℝ) :
    (∑ i : IntegerCoordinate, if paid j i then v else 0) = 19 * v := by
  classical
  change (∑ i : Fin 4 × Fin 19, if i.1 = j then v else 0) = 19 * v
  simp only [Fintype.sum_prod_type]
  rw [Finset.sum_comm]
  simp

theorem core_fiber_count : Fintype.card (Finset IntegerCoordinate) = 2 ^ 76 := by
  rw [Fintype.card_finset, integerCoordinate_card]

end SharpOC.BoxCounterexample
