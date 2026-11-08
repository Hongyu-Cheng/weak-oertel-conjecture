import SharpOC.Witness1387.SupportExposure
import SharpOC.Witness1387.Arithmetic

/-! Counts of baseline tuples and inactive unit-sector sources. -/

namespace SharpOC.Witness1387

open scoped BigOperators

theorem baseline_count : Fintype.card Baseline = 2048 ^ 19 := by
  simp [Baseline]

private theorem zero_slots_count (Z : Finset Block) :
    (Finset.univ.filter fun b : Baseline => zeroSlots b = Z).card = 2047 ^ (19 - Z.card) := by
  let S (j : Block) : Finset Slot := if j ∈ Z then {0} else Finset.univ.erase 0
  have hset : (Finset.univ.filter fun b : Baseline => zeroSlots b = Z) = Fintype.piFinset S := by
    ext b
    simp only [Finset.mem_filter, Finset.mem_univ, true_and, Fintype.mem_piFinset, Finset.ext_iff,
      mem_zeroSlots]
    apply forall_congr'
    intro j
    by_cases hj : j ∈ Z <;> simp [S, hj]
  rw [hset, Fintype.card_piFinset]
  calc
    _ = ∏ j : Block, if j ∈ Z then 1 else 2047 := by
      apply Finset.prod_congr rfl
      intro j _
      by_cases hj : j ∈ Z <;> simp [S, hj, Finset.card_erase_of_mem]
    _ = _ := by
      rw [Finset.prod_ite, Finset.prod_const_one, one_mul, Finset.prod_const,
        Finset.filter_notMem_eq_sdiff, Finset.card_sdiff_of_subset (Finset.subset_univ Z)]
      simp

private theorem one_zero_count :
    (Finset.univ.filter fun b : Baseline => (zeroSlots b).card = 1).card = 19 * 2047 ^ 18 := by
  let S (i : Block) := Finset.univ.filter fun b : Baseline => zeroSlots b = {i}
  have hdis : ((Finset.univ : Finset Block) : Set Block).PairwiseDisjoint S := by
    intro i _ j _ hij
    apply Finset.disjoint_filter.mpr
    intro b _ hi hj
    exact hij (Finset.singleton_injective (hi.symm.trans hj))
  have hset : (Finset.univ.filter fun b : Baseline => (zeroSlots b).card = 1) =
      Finset.univ.biUnion S := by
    ext b
    simp [S, Finset.card_eq_one]
  rw [hset, Finset.card_biUnion hdis]
  simp [S, zero_slots_count]

private theorem inactive_one_zero_count :
    (Finset.univ.filter fun b : Baseline => (zeroSlots b).card = 1 ∧ ¬(activeAxis b).isSome).card =
      resetCount := by
  let A := Finset.univ.filter fun b : Baseline => (zeroSlots b).card = 1 ∧ (activeAxis b).isSome
  let Z := Finset.univ.filter fun b : Baseline => (zeroSlots b).card = 1
  have hsub : A ⊆ Z := Finset.monotone_filter_right _ (fun _ _ h => h.1)
  have hset : (Finset.univ.filter fun b : Baseline =>
      (zeroSlots b).card = 1 ∧ ¬(activeAxis b).isSome) = Z \ A := by
    ext b
    by_cases h : (zeroSlots b).card = 1 <;> simp [A, Z, h]
  calc
    _ = Z.card - A.card := (congrArg Finset.card hset).trans (Finset.card_sdiff_of_subset hsub)
    _ = resetCount := congrArg₂ (· - ·) one_zero_count ordinary_center_count

/-- The unit sectors come from all-nonzero baselines and the inactive one-zero baselines. -/
theorem unit_sector_count :
    (Finset.univ.filter fun b : Baseline => ¬(activeAxis b).isSome ∧ (zeroSlots b).card ≤ 1).card =
      2047 ^ 19 + resetCount := by
  have hset : (Finset.univ.filter fun b : Baseline =>
      ¬(activeAxis b).isSome ∧ (zeroSlots b).card ≤ 1) =
      Finset.univ.filter (fun b : Baseline => zeroSlots b = ∅) ∪
        Finset.univ.filter (fun b : Baseline => (zeroSlots b).card = 1 ∧ ¬(activeAxis b).isSome) := by
    ext b
    simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_union]
    by_cases hz : zeroSlots b = ∅
    · simp [hz, activeAxis]
    · have hpos := Finset.card_pos.mpr (Finset.nonempty_iff_ne_empty.mpr hz)
      have hcard : (zeroSlots b).card ≤ 1 ↔ (zeroSlots b).card = 1 := by omega
      simp [hz, hcard, and_comm]
  have hdis : Disjoint (Finset.univ.filter (fun b : Baseline => zeroSlots b = ∅))
      (Finset.univ.filter (fun b : Baseline => (zeroSlots b).card = 1 ∧ ¬(activeAxis b).isSome)) := by
    apply Finset.disjoint_filter.mpr
    intro b _ hzero hone
    simp [hzero] at hone
  rw [hset, Finset.card_union_of_disjoint hdis, zero_slots_count, inactive_one_zero_count]
  simp

end SharpOC.Witness1387
