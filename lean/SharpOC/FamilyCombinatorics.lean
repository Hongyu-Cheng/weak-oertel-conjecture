import SharpOC.Constants
import SharpOC.LatticeGeometry
import SharpOC.SourceGeometry

/-! Finite indexing and the integer part of the middle-fiber cuts. -/

noncomputable section
open Finset
open scoped BigOperators

namespace SharpOC

abbrev IntegerCoordinate := Fin 3 × Fin copies
abbrev FiberIndex := Sum (Finset IntegerCoordinate) IntegerCoordinate

theorem integerCoordinate_card : Fintype.card IntegerCoordinate = integerDimension := by
  simp [IntegerCoordinate, integerDimension]

def selectedCoordinate (S : Finset IntegerCoordinate) (hS : S.Nonempty) :
    IntegerCoordinate := Classical.choose hS

theorem selectedCoordinate_mem (S : Finset IntegerCoordinate) (hS : S.Nonempty) :
    selectedCoordinate S hS ∈ S := Classical.choose_spec hS

def selectedType (S : Finset IntegerCoordinate) : Fin 3 :=
  if hS : S.Nonempty then (selectedCoordinate S hS).1 else 0

theorem selectedType_eq (S : Finset IntegerCoordinate) (hS : S.Nonempty) :
    selectedType S = (selectedCoordinate S hS).1 := by simp [selectedType, hS]

def paid (j : Fin 24) (i : IntegerCoordinate) : Prop :=
  SourceGeometry.isRoot i.1 j

instance paidDecidable (j : Fin 24) (i : IntegerCoordinate) : Decidable (paid j i) :=
  Classical.propDecidable _

def penalty : ℝ := 3 * ((integerDimension : ℝ) + 1)

def cutCoefficient (j : Fin 24) (i : IntegerCoordinate) : ℝ :=
  if paid j i then -penalty else tilt

theorem penalty_pos : 0 < penalty := by unfold penalty; positivity

theorem cutCoefficient_le_tilt (j : Fin 24) (i : IntegerCoordinate) :
    cutCoefficient j i ≤ tilt := by
  unfold cutCoefficient
  split_ifs
  · have hp := penalty_pos
    norm_num [tilt]
    linarith
  · exact le_rfl

theorem selectedType_misses (S : Finset IntegerCoordinate) (hS : S.Nonempty)
    (j : Fin 24) (hmiss : ∀ i ∈ S, ¬ paid j i) :
    ¬ SourceGeometry.isRoot (selectedType S) j := by
  rw [selectedType_eq S hS]
  exact hmiss _ (selectedCoordinate_mem S hS)

theorem integer_cut_cube (j : Fin 24) (S : Finset IntegerCoordinate) :
    coordinateFunctional (cutCoefficient j) (cubeVector S) =
      ∑ i ∈ S, cutCoefficient j i := by
  classical
  simp [coordinateFunctional, cubeVector, mul_ite]

theorem integer_cut_negative (j : Fin 24) (i : IntegerCoordinate) :
    coordinateFunctional (cutCoefficient j) (negativeUnit i) = -cutCoefficient j i := by
  classical
  simp [coordinateFunctional, negativeUnit, mul_ite]

theorem unpaid_integer_cut (j : Fin 24) (S : Finset IntegerCoordinate)
    (hmiss : ∀ i ∈ S, ¬ paid j i) :
    coordinateFunctional (cutCoefficient j) (cubeVector S) = (S.card : ℝ) * tilt := by
  rw [integer_cut_cube]
  calc
    _ = ∑ _i ∈ S, tilt := Finset.sum_congr rfl (fun i hi => by simp [cutCoefficient, hmiss i hi])
    _ = _ := by simp

theorem paid_integer_cut (j : Fin 24) (S : Finset IntegerCoordinate)
    (hpaid : ∃ i ∈ S, paid j i) :
    coordinateFunctional (cutCoefficient j) (cubeVector S) ≤
      -penalty + ((S.card : ℝ) - 1) * tilt := by
  classical
  obtain ⟨i, hi, hp⟩ := hpaid
  rw [integer_cut_cube, ← Finset.sum_erase_add _ _ hi]
  have hsum : (∑ k ∈ S.erase i, cutCoefficient j k) ≤
      ((S.erase i).card : ℝ) * tilt := by
    calc
      _ ≤ ∑ _k ∈ S.erase i, tilt := Finset.sum_le_sum (fun k _ => cutCoefficient_le_tilt j k)
      _ = _ := by simp
  have hc : ((S.erase i).card : ℝ) = (S.card : ℝ) - 1 := by
    have h : ((S.erase i).card : ℝ) + 1 = S.card := by
      exact_mod_cast Finset.card_erase_add_one hi
    linarith
  rw [show cutCoefficient j i = -penalty by simp [cutCoefficient, hp]]
  rw [hc] at hsum
  linarith

theorem cube_card_le_dimension (S : Finset IntegerCoordinate) :
    S.card ≤ integerDimension := by
  rw [← integerCoordinate_card]
  exact Finset.card_le_univ S

theorem paid_sum (j : Fin 24) (v : ℝ) :
    (∑ i : IntegerCoordinate, if paid j i then v else 0) = (copies : ℝ) * v := by
  classical
  obtain ⟨a, ha, hu⟩ := SourceGeometry.each_cut_has_one_root j
  have heq (b : Fin 3) : SourceGeometry.isRoot b j ↔ b = a :=
    ⟨fun hb => hu b hb, fun h => h ▸ ha⟩
  simp only [paid, Fintype.sum_prod_type, heq]
  rw [Finset.sum_comm]
  simp

theorem core_fiber_count : Fintype.card (Finset IntegerCoordinate) = 2 ^ integerDimension := by
  rw [Fintype.card_finset, integerCoordinate_card]

end SharpOC
