import SharpOC.SelectorLattice
import Mathlib.Data.Finset.Sum
import Mathlib.Data.Finset.SymmDiff

/-! The signed selector support and its integer threshold patterns. -/

noncomputable section

namespace SharpOC.Selector17

open Finset
open scoped BigOperators symmDiff

abbrev Coordinate := Fin 10 ⊕ Fin 2
abbrev IntegerSpace := Coordinate → ℝ

def heavyMasks : Finset (Finset Coordinate) := univ.powerset.erase ∅
def lightMasks : Finset (Finset (Fin 10)) := univ.powersetCard 5

abbrev FiberIndex := Option (↥heavyMasks ⊕ (Fin 3 × ↥lightMasks))

def reversed : Finset (Fin 10) := {0, 1, 2, 3}

def toggle (J : Finset (Fin 10)) : Finset (Fin 10) := reversed ∆ J

@[simp] theorem toggle_toggle (J : Finset (Fin 10)) : toggle (toggle J) = J := by
  ext i
  simp only [toggle, mem_symmDiff]
  tauto

def selectorMask (j : Fin 3) : Finset (Fin 2) :=
  if j = 0 then {0} else if j = 1 then {1} else {0, 1}

def selectorType (T : Finset (Fin 2)) : Option (Fin 3) :=
  if T = ∅ then none else if T = {0} then some 0 else if T = {1} then some 1 else some 2

theorem selector_cases (T : Finset (Fin 2)) :
    T = ∅ ∨ T = selectorMask 0 ∨ T = selectorMask 1 ∨ T = selectorMask 2 := by
  by_cases h0 : (0 : Fin 2) ∈ T <;> by_cases h1 : (1 : Fin 2) ∈ T
  · right; right; right
    ext i
    fin_cases i <;> simp [selectorMask, h0, h1]
  · right; left
    ext i
    fin_cases i <;> simp [selectorMask, h0, h1]
  · right; right; left
    ext i
    fin_cases i <;> simp [selectorMask, h0, h1]
  · left
    ext i
    fin_cases i <;> simp [h0, h1]

@[simp] theorem selectorType_mask (j : Fin 3) : selectorType (selectorMask j) = some j := by
  fin_cases j <;> decide

@[simp] theorem selectorMask_nonempty (j : Fin 3) : (selectorMask j).Nonempty := by
  fin_cases j <;> decide

def lightMask (j : Fin 3) (J : Finset (Fin 10)) : Finset Coordinate :=
  (toggle J).disjSum (selectorMask j)

def balancedMasks : Finset (Finset Coordinate) :=
  heavyMasks.filter fun S => S.toRight.Nonempty ∧ (toggle S.toLeft).card = 5

def unbalancedMasks : Finset (Finset Coordinate) := heavyMasks \ balancedMasks

def selectedType (S : Finset Coordinate) : Fin 3 := (selectorType S.toRight).getD 0

def nearType (S : ↥heavyMasks) : Option (Fin 3) :=
  (selectorType S.val.toRight).filter fun j =>
    (toggle S.val.toLeft).card == (if j = 2 then 6 else 4)

@[simp] theorem mem_heavyMasks (S : Finset Coordinate) : S ∈ heavyMasks ↔ S.Nonempty := by
  simp [heavyMasks, nonempty_iff_ne_empty]

@[simp] theorem mem_lightMasks (J : Finset (Fin 10)) : J ∈ lightMasks ↔ J.card = 5 := by
  simp [lightMasks, mem_powersetCard]

@[simp] theorem mem_balancedMasks (S : Finset Coordinate) :
    S ∈ balancedMasks ↔ S.toRight.Nonempty ∧ (toggle S.toLeft).card = 5 := by
  simp only [balancedMasks, mem_filter, mem_heavyMasks]
  refine ⟨And.right, fun h => ⟨?_, h⟩⟩
  obtain ⟨j, hj⟩ := h.1
  exact ⟨Sum.inr j, mem_toRight.mp hj⟩

theorem coordinate_card : Fintype.card Coordinate = 12 := by norm_num [Coordinate]

theorem heavyMasks_card : heavyMasks.card = 4095 := by
  have he : (∅ : Finset Coordinate) ∈ univ.powerset := by simp
  rw [heavyMasks, card_erase_of_mem he, card_powerset, card_univ, coordinate_card]
  decide

theorem lightMasks_card : lightMasks.card = 252 := by
  simpa [lightMasks, card_powersetCard] using (show Nat.choose 10 5 = 252 by decide)

def ordinarySign (i : Fin 10) : ℝ := if i ∈ reversed then -1 else 1

theorem ordinarySign_cases (i : Fin 10) : ordinarySign i = 1 ∨ ordinarySign i = -1 := by
  by_cases h : i ∈ reversed <;> simp [ordinarySign, h]

def raw (S : Finset Coordinate) : IntegerSpace
  | .inl i => (if S.toRight = ∅ then 1 else ordinarySign i) * cubeVector S (.inl i)
  | .inr i => cubeVector S (.inr i)

def ordinarySum : IntegerSpace →ₗ[ℝ] ℝ :=
  coordinateFunctional (Sum.elim (fun _ => 1) (fun _ => 0))

def selectorSum : IntegerSpace →ₗ[ℝ] ℝ :=
  LinearMap.proj (R := ℝ) (φ := fun _ : Coordinate => ℝ) (.inr 0) +
    LinearMap.proj (.inr 1)

def guard : IntegerSpace →ₗ[ℝ] ℝ := 3 • ordinarySum - 2 • selectorSum

def threshold (j : Fin 3) : IntegerSpace →ₗ[ℝ] ℝ :=
  ordinarySum - (if j = 0 then LinearMap.proj (Sum.inr 1)
    else if j = 1 then LinearMap.proj (Sum.inr 0) else selectorSum)

def rawScore (S : Finset Coordinate) : ℤ :=
  if S.toRight = ∅ then S.toLeft.card else (toggle S.toLeft).card - 4

def rawGuard (S : Finset Coordinate) : ℤ := 3 * rawScore S - 2 * (S.toRight.card : ℤ)

def heavyNegative (S : Finset Coordinate) : Bool := decide (rawGuard S < 0)

def mask : FiberIndex → Finset Coordinate
  | none => ∅
  | some (.inl S) => S
  | some (.inr (j, J)) => lightMask j J

def negative : FiberIndex → Bool
  | none => false
  | some (.inl S) => heavyNegative S
  | some (.inr (j, J)) => !(heavyNegative (lightMask j J))

def base (i : FiberIndex) : IntegerSpace :=
  if negative i then -raw (mask i) else raw (mask i)

def integerBase (i : FiberIndex) (j : Coordinate) : ℤ :=
  (if negative i then -1 else 1) *
    (if j ∈ mask i then
      match j with
      | .inl k => if (mask i).toRight ≠ ∅ ∧ k ∈ reversed then -1 else 1
      | .inr _ => 1
    else 0)

@[simp] theorem base_none : base none = 0 := by
  ext j
  cases j <;> simp [base, raw, mask, negative, cubeVector]

theorem integerBase_cast (i : FiberIndex) :
    (fun j => (integerBase i j : ℝ)) = base i := by
  ext j
  cases j with
  | inl k =>
    cases hs : negative i <;> by_cases hk : Sum.inl k ∈ mask i <;>
      by_cases ht : (mask i).toRight = ∅ <;> by_cases hr : k ∈ reversed <;>
      norm_num [base, raw, integerBase, ordinarySign, cubeVector, hs, hk, ht, hr]
  | inr k =>
    cases hs : negative i <;> by_cases hk : Sum.inr k ∈ mask i <;>
      norm_num [base, raw, integerBase, cubeVector, hs, hk]

theorem base_coord_bounds (i : FiberIndex) (j : Coordinate) : -1 ≤ base i j ∧ base i j ≤ 1 := by
  cases j with
  | inl k =>
    cases hs : negative i <;> by_cases hk : Sum.inl k ∈ mask i <;>
      by_cases ht : (mask i).toRight = ∅ <;> by_cases hr : k ∈ reversed <;>
      norm_num [base, raw, ordinarySign, cubeVector, hs, hk, ht, hr]
  | inr k =>
    cases hs : negative i <;> by_cases hk : Sum.inr k ∈ mask i <;>
      norm_num [base, raw, cubeVector, hs, hk]

theorem mask_nonempty (i : FiberIndex) (hi : i ≠ none) : (mask i).Nonempty := by
  cases i with
  | none => exact (hi rfl).elim
  | some i =>
    cases i with
    | inl S => exact (mem_heavyMasks S.val).mp S.property
    | inr p =>
      obtain ⟨j, hj⟩ := selectorMask_nonempty p.1
      exact ⟨Sum.inr j, by simpa [mask, lightMask] using hj⟩

@[simp] theorem base_apply_eq_zero_iff (i : FiberIndex) (j : Coordinate) :
    base i j = 0 ↔ j ∉ mask i := by
  cases j with
  | inl k =>
    cases hs : negative i <;> by_cases hk : Sum.inl k ∈ mask i <;>
      by_cases ht : (mask i).toRight = ∅ <;> by_cases hr : k ∈ reversed <;>
      norm_num [base, raw, ordinarySign, cubeVector, hs, hk, ht, hr]
  | inr k =>
    cases hs : negative i <;> by_cases hk : Sum.inr k ∈ mask i <;>
      norm_num [base, raw, cubeVector, hs, hk]

theorem base_injective : Function.Injective base := by
  intro i j h
  have hm : mask i = mask j := by
    ext k
    simpa only [base_apply_eq_zero_iff, not_iff_not] using
      (show base i k = 0 ↔ base j k = 0 by rw [h])
  cases i with
  | none =>
    cases j with
    | none => rfl
    | some j => exact ((mask_nonempty (some j) (by simp)).ne_empty hm.symm).elim
  | some i =>
    cases j with
    | none => exact ((mask_nonempty (some i) (by simp)).ne_empty hm).elim
    | some j =>
      rcases i with S | ⟨k, J⟩ <;> rcases j with T | ⟨l, K⟩
      · exact congrArg (fun x => (some (Sum.inl x) : FiberIndex)) (Subtype.ext hm : S = T)
      · have he : S.val = lightMask l K := hm
        obtain ⟨q, hq⟩ := selectorMask_nonempty l
        have hh := congrFun h (Sum.inr q)
        simp only [base, negative, mask, he] at hh
        change (if heavyNegative (lightMask l K) then -raw (lightMask l K) else raw (lightMask l K)) (.inr q) =
          (if !(heavyNegative (lightMask l K)) then -raw (lightMask l K) else raw (lightMask l K)) (.inr q) at hh
        cases hn : heavyNegative (lightMask l K) <;> rw [hn] at hh <;>
          norm_num [raw, lightMask, cubeVector, hq] at hh
      · have he : T.val = lightMask k J := hm.symm
        obtain ⟨q, hq⟩ := selectorMask_nonempty k
        have hh := congrFun h (Sum.inr q)
        simp only [base, negative, mask, he] at hh
        change (if !(heavyNegative (lightMask k J)) then -raw (lightMask k J) else raw (lightMask k J)) (.inr q) =
          (if heavyNegative (lightMask k J) then -raw (lightMask k J) else raw (lightMask k J)) (.inr q) at hh
        cases hn : heavyNegative (lightMask k J) <;> rw [hn] at hh <;>
          norm_num [raw, lightMask, cubeVector, hq] at hh
      · have hJ : J = K := by
          apply Subtype.ext
          simpa [mask, lightMask] using congrArg (toggle ∘ Finset.toLeft) hm
        have hk : k = l := by
          simpa [mask, lightMask] using congrArg (selectorType ∘ Finset.toRight) hm
        simp [hJ, hk]

theorem integerBase_injective : Function.Injective integerBase := by
  intro i j h
  apply base_injective
  rw [← integerBase_cast i, ← integerBase_cast j, h]

private theorem reversed_card : reversed.card = 4 := by decide

theorem raw_ordinarySum (S : Finset Coordinate) : ordinarySum (raw S) = (rawScore S : ℝ) := by
  have hterm (i : Fin 10) :
      ordinarySign i * cubeVector S (.inl i) =
        (if i ∈ toggle S.toLeft then (1 : ℝ) else 0) -
        (if i ∈ reversed then (1 : ℝ) else 0) := by
    by_cases hi : Sum.inl i ∈ S <;> by_cases hr : i ∈ reversed <;>
      norm_num [ordinarySign, cubeVector, toggle, mem_symmDiff, hi, hr]
  by_cases h : S.toRight = ∅
  · simp [ordinarySum, coordinateFunctional, Fintype.sum_sum_type, raw, rawScore, cubeVector, h,
      ← Finset.mem_toLeft]
  · simp [ordinarySum, coordinateFunctional, Fintype.sum_sum_type, raw, rawScore, h, hterm,
      Finset.sum_sub_distrib, reversed_card]

theorem raw_selectorSum (S : Finset Coordinate) : selectorSum (raw S) = S.toRight.card := by
  have hs : (∑ i : Fin 2, if i ∈ S.toRight then (1 : ℝ) else 0) = S.toRight.card := by
    have he : (Finset.univ.filter (· ∈ S.toRight)) = S.toRight := by ext i; simp
    simp only [Finset.sum_boole, he]
  rw [Fin.sum_univ_two] at hs
  simpa only [selectorSum, LinearMap.add_apply, LinearMap.proj_apply, raw, cubeVector,
    Finset.mem_toRight] using hs

theorem raw_guard (S : Finset Coordinate) : guard (raw S) = (rawGuard S : ℝ) := by
  simp [guard, rawGuard, raw_ordinarySum, raw_selectorSum]

private theorem raw_guard_ne_zero (S : ↥heavyMasks) : rawGuard S.val ≠ 0 := by
  have hc := Finset.card_le_univ S.val.toRight
  simp at hc
  have hs := Finset.card_pos.mpr ((mem_heavyMasks _).mp S.property)
  rw [← Finset.card_toLeft_add_card_toRight] at hs
  by_cases h : S.val.toRight = ∅
  · simp [rawGuard, rawScore, h] at hs ⊢
    exact hs.ne_empty
  · have hp : 0 < S.val.toRight.card := Finset.card_pos.mpr (Finset.nonempty_iff_ne_empty.mpr h)
    unfold rawGuard
    omega

theorem heavy_guard (S : ↥heavyMasks) : 1 ≤ guard (base (some (.inl S))) := by
  have hz := raw_guard_ne_zero S
  by_cases h : rawGuard S.val < 0
  · simpa [base, mask, negative, heavyNegative, raw_guard, h] using
      (show (1 : ℝ) ≤ -(rawGuard S.val : ℝ) by
        exact_mod_cast (show (1 : ℤ) ≤ -rawGuard S.val by omega))
  · simpa [base, mask, negative, heavyNegative, raw_guard, h] using
      (show (1 : ℝ) ≤ (rawGuard S.val : ℝ) by
        exact_mod_cast (show (1 : ℤ) ≤ rawGuard S.val by omega))

private theorem selector_eq_empty_card (S : ↥heavyMasks) (h : S.val.toRight = ∅) :
    1 ≤ S.val.toLeft.card := by
  have hs := Finset.card_pos.mpr ((mem_heavyMasks _).mp S.property)
  rw [← Finset.card_toLeft_add_card_toRight, h, Finset.card_empty, add_zero] at hs
  omega

theorem zero_selector_base {i : FiberIndex} (h : (mask i).toRight = ∅) :
    base i = cubeVector (mask i) := by
  have hn : negative i = false := by
    rcases i with _ | (S | ⟨j, J⟩)
    · rfl
    · have hc := selector_eq_empty_card S h
      have he : S.val.toRight = ∅ := h
      simp [negative, heavyNegative, rawGuard, rawScore, he]
    · have he : selectorMask j = ∅ := by simpa [mask, lightMask] using h
      exact ((selectorMask_nonempty j).ne_empty he).elim
  rw [base, hn]
  ext j
  cases j <;> simp [raw, h]

theorem lightMask_balanced (j : Fin 3) (J : ↥lightMasks) : lightMask j J ∈ balancedMasks := by
  simpa [lightMask] using (mem_lightMasks J.val).mp J.property

def pairedHeavy (j : Fin 3) (J : ↥lightMasks) : ↥heavyMasks :=
  ⟨lightMask j J, (Finset.mem_filter.mp (lightMask_balanced j J)).1⟩

theorem light_base (j : Fin 3) (J : ↥lightMasks) :
    base (some (.inr (j, J))) = -base (some (.inl (pairedHeavy j J))) := by
  cases h : heavyNegative (lightMask j J) <;> simp [base, negative, mask, pairedHeavy, h]

theorem paired_lightMask (S : ↥heavyMasks) (h : S.val ∈ balancedMasks) :
    ∃ J : ↥lightMasks, S = pairedHeavy (selectedType S.val) J := by
  have hs := (mem_balancedMasks _).mp h
  let J : ↥lightMasks := ⟨toggle S.val.toLeft, (mem_lightMasks _).mpr hs.2⟩
  rcases selector_cases S.val.toRight with he | he | he | he
  · exact (hs.1.ne_empty he).elim
  all_goals
    refine ⟨J, Subtype.ext ?_⟩
    rw [← Finset.toLeft_disjSum_toRight (u := S.val)]
    simp [pairedHeavy, lightMask, J, selectedType, he]

theorem balancedMasks_card : balancedMasks.card = 756 := by
  let e : Fin 3 × ↥lightMasks ↪ Finset Coordinate :=
    ⟨fun p => lightMask p.1 p.2, by
      rintro ⟨j, J⟩ ⟨k, K⟩ h
      have hj : j = k := by
        simpa [lightMask] using congrArg (selectorType ∘ Finset.toRight) h
      have hJ : J = K := by
        apply Subtype.ext
        simpa [lightMask] using congrArg (toggle ∘ Finset.toLeft) h
      simp [hj, hJ]⟩
  have he : balancedMasks = Finset.univ.map e := by
    ext S
    constructor
    · intro h
      obtain ⟨J, hJ⟩ := paired_lightMask ⟨S, (Finset.mem_filter.mp h).1⟩ h
      exact Finset.mem_map.mpr ⟨(selectedType S, J), Finset.mem_univ _, congrArg Subtype.val hJ.symm⟩
    · intro h
      obtain ⟨⟨j, J⟩, -, rfl⟩ := Finset.mem_map.mp h
      exact lightMask_balanced j J
  simp [he, Fintype.card_prod]
  decide

theorem unbalancedMasks_card : unbalancedMasks.card = 3339 := by
  have hs : balancedMasks ⊆ heavyMasks := filter_subset _ _
  rw [unbalancedMasks, card_sdiff_of_subset hs, heavyMasks_card, balancedMasks_card]

theorem balanced_heavy_count :
    (univ.filter fun S : ↥heavyMasks => S.val ∈ balancedMasks).card = 756 := by
  rw [Finset.univ_eq_attach, filter_attach (· ∈ balancedMasks) heavyMasks, card_map, card_attach]
  have he : heavyMasks.filter (· ∈ balancedMasks) = balancedMasks := by
    ext S
    exact ⟨fun h => (mem_filter.mp h).2, fun h => mem_filter.mpr ⟨(mem_filter.mp h).1, h⟩⟩
  rw [he, balancedMasks_card]

theorem unbalanced_heavy_count :
    (univ.filter fun S : ↥heavyMasks => S.val ∉ balancedMasks).card = 3339 := by
  rw [Finset.univ_eq_attach, filter_attach (· ∉ balancedMasks) heavyMasks, card_map, card_attach,
    ← Finset.sdiff_eq_filter]
  exact unbalancedMasks_card

def orientation (i : FiberIndex) : ℝ := if negative i then -1 else 1

theorem orientation_cases (i : FiberIndex) : orientation i = 1 ∨ orientation i = -1 := by
  cases h : negative i <;> simp [orientation, h]

theorem selector_base (i : FiberIndex) (j : Fin 2) :
    base i (.inr j) = orientation i * (if j ∈ (mask i).toRight then 1 else 0) := by
  cases h : negative i <;> by_cases hj : Sum.inr j ∈ mask i <;>
    simp [orientation, base, raw, h, cubeVector, hj]

theorem ordinary_base (i : FiberIndex) (j : Fin 10) :
    base i (.inl j) = orientation i *
      ((if (mask i).toRight = ∅ then 1 else ordinarySign j) *
        (if j ∈ (mask i).toLeft then 1 else 0)) := by
  cases h : negative i <;> by_cases hj : Sum.inl j ∈ mask i <;>
    by_cases ht : (mask i).toRight = ∅ <;>
    simp [orientation, base, raw, h, cubeVector, hj, ht]

theorem selectorSum_base (i : FiberIndex) :
    selectorSum (base i) = orientation i * ((mask i).toRight.card : ℝ) := by
  cases h : negative i <;> simp [orientation, base, h, raw_selectorSum]

private def selectorBit (T : Finset (Fin 2)) (j : Fin 2) : ℤ := if j ∈ T then 1 else 0

private def rawThreshold (S : Finset Coordinate) (j : Fin 3) : ℤ :=
  rawScore S - (if j = 0 then selectorBit S.toRight 1
    else if j = 1 then selectorBit S.toRight 0
    else selectorBit S.toRight 0 + selectorBit S.toRight 1)

private theorem raw_threshold (S : Finset Coordinate) (j : Fin 3) :
    threshold j (raw S) = (rawThreshold S j : ℝ) := by
  have hb (k : Fin 2) : raw S (.inr k) = (selectorBit S.toRight k : ℝ) := by
    by_cases h : k ∈ S.toRight <;> simp [raw, cubeVector, selectorBit, ← mem_toRight, h]
  fin_cases j <;> simp [threshold, rawThreshold, raw_ordinarySum, selectorSum, hb]

private def oriented (S : Finset Coordinate) (u : ℤ) : ℤ := if rawGuard S < 0 then -u else u

private theorem heavy_guard_cast (S : ↥heavyMasks) :
    guard (base (some (.inl S))) = (oriented S.val (rawGuard S.val) : ℝ) := by
  by_cases h : rawGuard S.val < 0 <;>
    simp [base, mask, negative, heavyNegative, raw_guard, oriented, h]

private theorem heavy_threshold_cast (S : ↥heavyMasks) (j : Fin 3) :
    threshold j (base (some (.inl S))) = (oriented S.val (rawThreshold S.val j) : ℝ) := by
  by_cases h : rawGuard S.val < 0 <;>
    simp [base, mask, negative, heavyNegative, raw_threshold, oriented, h]

set_option maxRecDepth 4096 in
private theorem integer_profiles (S : ↥heavyMasks) :
    if S.val.toRight.Nonempty ∧ (toggle S.val.toLeft).card = 5 then
      oriented S.val (rawGuard S.val) = 1 ∧
        ∀ j, oriented S.val (rawThreshold S.val j) = if j = selectedType S.val then 1 else 0
    else
      2 ≤ oriented S.val (rawGuard S.val) ∧
        ∀ j, if nearType S = some j then oriented S.val (rawThreshold S.val j) = 0
          else 1 ≤ oriented S.val (rawThreshold S.val j) := by
  rcases selector_cases S.val.toRight with h | h | h | h
  · have hp := selector_eq_empty_card S h
    simp [h, nearType, selectorType, oriented, rawGuard, rawScore,
      rawThreshold, selectorBit]
    omega
  all_goals
    simp only [h, selectorMask_nonempty, true_and, nearType, selectorType_mask,
      selectedType, Option.getD_some]
    split_ifs with hp
    · constructor
      · norm_num [oriented, rawGuard, rawScore, h, selectorMask, hp]
      · intro j
        fin_cases j <;>
          norm_num [oriented, rawGuard, rawScore, rawThreshold, h, selectorMask, hp, selectorBit]
    · constructor
      · norm_num [oriented, rawGuard, rawScore, h, selectorMask]
        split_ifs <;> omega
      · intro j
        fin_cases j <;>
          norm_num [oriented, rawGuard, rawScore, rawThreshold, h, selectorMask, selectorBit,
            Option.filter]
        all_goals split_ifs at * <;> try omega

theorem paired_heavy_guard (S : ↥heavyMasks) (h : S.val ∈ balancedMasks) :
    guard (base (some (.inl S))) = 1 := by
  have hp := integer_profiles S
  rw [ite_eq_left ((mem_balancedMasks _).mp h)] at hp
  rw [heavy_guard_cast, hp.1]
  norm_num

theorem paired_heavy_threshold (S : ↥heavyMasks) (h : S.val ∈ balancedMasks) (j : Fin 3) :
    threshold j (base (some (.inl S))) = if j = selectedType S.val then 1 else 0 := by
  have hp := integer_profiles S
  rw [ite_eq_left ((mem_balancedMasks _).mp h)] at hp
  rw [heavy_threshold_cast, hp.2 j]
  split_ifs <;> norm_num

theorem light_guard (j : Fin 3) (J : ↥lightMasks) :
    guard (base (some (.inr (j, J)))) = -1 := by
  rw [light_base, map_neg, paired_heavy_guard (pairedHeavy j J) (lightMask_balanced j J)]

theorem light_threshold (k : Fin 3) (J : ↥lightMasks) (j : Fin 3) :
    threshold j (base (some (.inr (k, J)))) = if j = k then -1 else 0 := by
  rw [light_base, map_neg, paired_heavy_threshold (pairedHeavy k J) (lightMask_balanced k J)]
  have he : selectedType (pairedHeavy k J).val = k := by simp [selectedType, pairedHeavy, lightMask]
  rw [he]
  split_ifs <;> norm_num

theorem unpaired_heavy_guard (S : ↥heavyMasks) (h : S.val ∉ balancedMasks) :
    2 ≤ guard (base (some (.inl S))) := by
  have hp := integer_profiles S
  rw [ite_eq_right (fun hh => h ((mem_balancedMasks _).mpr hh))] at hp
  rw [heavy_guard_cast]
  exact_mod_cast hp.1

theorem nearType_unpaired (S : ↥heavyMasks) {k : Fin 3} (h : nearType S = some k) :
    S.val ∉ balancedMasks := by
  intro hb
  have hc := (mem_balancedMasks _).mp hb
  unfold nearType at h
  fin_cases k <;> simp [Option.filter_eq_some_iff, hc.2] at h

theorem near_heavy_threshold (S : ↥heavyMasks) {k : Fin 3} (h : nearType S = some k)
    (j : Fin 3) : if j = k then threshold j (base (some (.inl S))) = 0
      else 1 ≤ threshold j (base (some (.inl S))) := by
  have hp := integer_profiles S
  rw [ite_eq_right (fun hh => nearType_unpaired S h ((mem_balancedMasks _).mpr hh))] at hp
  have hj := hp.2 j
  rw [h] at hj
  rw [heavy_threshold_cast]
  by_cases he : j = k
  · subst j
    simp at hj ⊢
    exact_mod_cast hj
  · simp [he, Ne.symm he] at hj ⊢
    exact_mod_cast hj

theorem regular_heavy_threshold (S : ↥heavyMasks) (hp : S.val ∉ balancedMasks)
    (hn : nearType S = none) (j : Fin 3) : 1 ≤ threshold j (base (some (.inl S))) := by
  have hh := integer_profiles S
  rw [ite_eq_right (fun h => hp ((mem_balancedMasks _).mpr h))] at hh
  have hj := hh.2 j
  rw [heavy_threshold_cast]
  simp [hn] at hj
  exact_mod_cast hj

theorem near_heavy_guard (S : ↥heavyMasks) {k : Fin 3} (h : nearType S = some k) :
    guard (base (some (.inl S))) = 2 := by
  rw [heavy_guard_cast]
  rcases selector_cases S.val.toRight with he | he | he | he
  · simp [nearType, he, selectorType] at h
  all_goals
    simp [nearType, he, Option.filter] at h
    norm_num [oriented, rawGuard, rawScore, he, selectorMask, h.1]

end SharpOC.Selector17
