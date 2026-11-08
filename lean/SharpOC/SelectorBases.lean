import SharpOC.SelectorArithmetic
import SharpOC.SelectorLattice
import Mathlib.Data.Finset.Sum

/-! The finite signed bases of the shared-selector construction. -/

noncomputable section

namespace SharpOC.Selector

open Finset
open scoped BigOperators

abbrev IntegerSpace := Coordinate → ℝ
abbrev FiberIndex := Option (↥heavyMasks ⊕ (Fin 3 × ↥lightMasks))

def balance : IntegerSpace →ₗ[ℝ] ℝ :=
  coordinateFunctional (Sum.elim (fun _ => 1) (fun _ => -5))

def roofTilt : IntegerSpace →ₗ[ℝ] ℝ :=
  coordinateFunctional (Sum.elim (fun _ => 0) (fun _ => delta))

def heavyNegative (S : Finset Coordinate) : Bool :=
  decide (balance (cubeVector S) < 0)

def lightMask (j : Fin 3) (J : Finset (Fin 11)) : Finset Coordinate :=
  J.disjSum {j}

def mask : FiberIndex → Finset Coordinate
  | none => ∅
  | some (.inl S) => S
  | some (.inr (j, J)) => lightMask j J

def negative : FiberIndex → Bool
  | none => false
  | some (.inl S) => heavyNegative S
  | some (.inr _) => true

def base (i : FiberIndex) : IntegerSpace :=
  signedCubeVector (negative i) (mask i)

def integerBase (i : FiberIndex) (j : Coordinate) : ℤ :=
  if j ∈ mask i then (if negative i then -1 else 1) else 0

@[simp] theorem base_none : base none = 0 := by
  ext i
  simp [base, mask, negative, signedCubeVector, cubeVector]

theorem integerBase_cast (i : FiberIndex) :
    (fun j => (integerBase i j : ℝ)) = base i := by
  ext j
  cases h : negative i <;> by_cases hj : j ∈ mask i <;>
    simp [integerBase, base, signedCubeVector, cubeVector, h, hj]

theorem balance_cube (S : Finset Coordinate) :
    balance (cubeVector S) = (S.toLeft.card : ℝ) - 5 * (S.toRight.card : ℝ) := by
  have hl : (Finset.univ.filter (fun j : Fin 11 => Sum.inl j ∈ S)) = S.toLeft := by
    ext j
    simp
  have hr : (Finset.univ.filter (fun j : Fin 3 => Sum.inr j ∈ S)) = S.toRight := by
    ext j
    simp
  simp [balance, coordinateFunctional, Fintype.sum_sum_type, cubeVector,
    ← Finset.mul_sum, sub_eq_add_neg, hl, hr]

theorem balance_cube_integral (S : Finset Coordinate) :
    balance (cubeVector S) = ((S.toLeft.card : ℤ) - 5 * (S.toRight.card : ℤ) : ℤ) := by
  rw [balance_cube]
  push_cast
  rfl

theorem roofTilt_cube (S : Finset Coordinate) :
    roofTilt (cubeVector S) = delta * (S.toRight.card : ℝ) := by
  have hr : (Finset.univ.filter (fun j : Fin 3 => Sum.inr j ∈ S)) = S.toRight := by
    ext j
    simp
  simp [roofTilt, coordinateFunctional, Fintype.sum_sum_type, cubeVector,
    ← Finset.mul_sum, hr]

theorem balance_light (j : Fin 3) (J : ↥lightMasks) :
    balance (cubeVector (lightMask j J)) = 0 := by
  have hj := (mem_lightMasks J.val).mp J.property
  simp [lightMask, balance_cube, hj]

theorem balance_base_nonneg (i : FiberIndex) : 0 ≤ balance (base i) := by
  cases i with
  | none => simp
  | some i =>
    cases i with
    | inl S =>
      by_cases h : balance (cubeVector S.val) < 0
      · simpa [base, mask, negative, heavyNegative, signedCubeVector, h] using neg_nonneg.mpr h.le
      · simpa [base, mask, negative, heavyNegative, signedCubeVector, h] using le_of_not_gt h
    | inr p => rcases p with ⟨j, J⟩; simp [base, mask, negative, signedCubeVector, balance_light]

theorem balanced_heavy_positive (S : ↥heavyMasks)
    (h : balance (base (some (.inl S))) = 0) :
    base (some (.inl S)) = cubeVector S.val ∧ balance (cubeVector S.val) = 0 := by
  by_cases hneg : balance (cubeVector S.val) < 0
  · simp [base, mask, negative, heavyNegative, signedCubeVector, hneg] at h
    linarith
  · simpa [base, mask, negative, heavyNegative, signedCubeVector, hneg] using h

theorem balanced_heavy_has_selector (S : ↥heavyMasks)
    (h : balance (cubeVector S.val) = 0) : ∃ j : Fin 3, Sum.inr j ∈ S.val := by
  by_contra! hn
  have hz : S.val.toRight = ∅ := by
    ext j
    simp [Finset.mem_toRight, hn]
  have hl : S.val.toLeft = ∅ := by
    rw [balance_cube, hz] at h
    have hc : S.val.toLeft.card = 0 := by exact_mod_cast (show (S.val.toLeft.card : ℝ) = 0 by simpa using h)
    exact card_eq_zero.mp hc
  have hempty : S.val = ∅ := by
    rw [← Finset.toLeft_disjSum_toRight (u := S.val), hz, hl]
    rfl
  exact ((mem_heavyMasks S.val).mp S.property).ne_empty hempty

def selectedType (S : Finset Coordinate) : Fin 3 :=
  if h : ∃ j : Fin 3, Sum.inr j ∈ S then Classical.choose h else 0

theorem selectedType_mem (S : Finset Coordinate)
    (h : ∃ j : Fin 3, Sum.inr j ∈ S) : Sum.inr (selectedType S) ∈ S := by
  simp [selectedType, h, Classical.choose_spec h]

theorem mask_nonempty (i : FiberIndex) (hi : i ≠ none) : (mask i).Nonempty := by
  cases i with
  | none => exact (hi rfl).elim
  | some i =>
    cases i with
    | inl S => exact (mem_heavyMasks S.val).mp S.property
    | inr p => exact ⟨Sum.inr p.1, by simp [mask, lightMask]⟩

theorem base_injective : Function.Injective base := by
  intro i j hij
  have hmask : mask i = mask j := signedCubeVector_support_eq hij
  cases i with
  | none =>
    cases j with
    | none => rfl
    | some j =>
      exact ((mask_nonempty (some j) (by simp)).ne_empty hmask.symm).elim
  | some i =>
    cases j with
    | none =>
      exact ((mask_nonempty (some i) (by simp)).ne_empty hmask).elim
    | some j =>
      have hsign := (signedCubeVector_injective (mask_nonempty (some i) (by simp)) hij).1
      rcases i with S | ⟨k, J⟩ <;> rcases j with T | ⟨l, K⟩
      · have hST : S = T := Subtype.ext hmask
        simp [hST]
      · have hm : S.val = lightMask l K := hmask
        simp [negative, heavyNegative, hm, balance_light] at hsign
      · have hm : T.val = lightMask k J := hmask.symm
        simp [negative, heavyNegative, hm, balance_light] at hsign
      · have hJ : J = K := by
          apply Subtype.ext
          simpa [mask, lightMask] using congrArg Finset.toLeft hmask
        have hk : k = l := by
          simpa [mask, lightMask] using congrArg Finset.toRight hmask
        simp [hJ, hk]

theorem integerBase_injective : Function.Injective integerBase := by
  intro i j h
  apply base_injective
  rw [← integerBase_cast i, ← integerBase_cast j, h]

theorem balance_base_integral (i : FiberIndex) : ∃ z : ℤ, balance (base i) = z := by
  let z : ℤ := ((mask i).toLeft.card : ℤ) - 5 * ((mask i).toRight.card : ℤ)
  have hz : balance (cubeVector (mask i)) = (z : ℝ) := balance_cube_integral (mask i)
  cases h : negative i
  · exact ⟨z, by simpa [base, signedCubeVector, h] using hz⟩
  · exact ⟨-z, by simpa [base, signedCubeVector, h] using congrArg Neg.neg hz⟩

theorem one_le_balance_base (i : FiberIndex) (h : 0 < balance (base i)) :
    1 ≤ balance (base i) := by
  obtain ⟨z, hz⟩ := balance_base_integral i
  rw [hz] at h ⊢
  have hp : 0 < z := by exact_mod_cast h
  exact_mod_cast (show (1 : ℤ) ≤ z by omega)

end SharpOC.Selector
