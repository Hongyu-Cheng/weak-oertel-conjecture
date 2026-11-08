import SharpOC.Witness1387.Arithmetic
import SharpOC.Witness1387.SupportExposure
import Mathlib.Algebra.BigOperators.Group.Finset.Powerset

/-! The threshold-55 census for active centers with two zero slots. -/

namespace SharpOC.Witness1387

open scoped BigOperators

private def highValues : Finset Slot :=
  Finset.univ.filter fun s => high s = true

private def lowValues : Finset Slot :=
  (insert 0 highValues)ᶜ

private theorem highValues_card : highValues.card = 220 := by
  rw [Finset.card_eq_sum_card_fiberwise (f := owner) (t := Finset.univ)
    (fun _ _ => Finset.mem_univ _)]
  simp [highValues, Finset.filter_filter, high_owner_count]

private theorem lowValues_card : lowValues.card = 1827 := by
  have h : (0 : Slot) ∉ highValues := by simp [highValues]
  rw [lowValues, Finset.card_compl, Finset.card_insert_of_notMem h, highValues_card]
  norm_num [Fintype.card_fin]

private def extraChoices (T Z : Finset Block) (k : Block) : Finset Slot :=
  if k ∈ T then if k ∈ Z then {0} else highValues else lowValues

private theorem mem_extraChoices (b : Baseline) {T Z : Finset Block} (hZ : Z ⊆ T) :
    b ∈ Fintype.piFinset (extraChoices T Z) ↔
      zeroSlots b = Z ∧ zeroSlots b ∪ highSlots b = T := by
  have h (k : Block) : b k ∈ extraChoices T Z k ↔
      (k ∈ zeroSlots b ↔ k ∈ Z) ∧ (k ∈ zeroSlots b ∪ highSlots b ↔ k ∈ T) := by
    by_cases hz : k ∈ Z
    · simpa [extraChoices, hZ hz, hz] using
        (Or.inl : b k = 0 → b k = 0 ∨ high (b k) = true)
    · by_cases ht : k ∈ T <;> by_cases hb : b k = 0 <;>
        simp [extraChoices, ht, hz, hb, highValues, lowValues]
  simp only [Fintype.mem_piFinset, h, forall_and, ← Finset.ext_iff]

private theorem card_extraChoices (T : Finset Block) {Z : Finset Block} (hZ : Z ⊆ T) :
    (Fintype.piFinset (extraChoices T Z)).card =
      220 ^ (T.card - Z.card) * 1827 ^ (19 - T.card) := by
  rw [Fintype.card_piFinset]
  simp only [extraChoices, apply_ite Finset.card, Finset.card_singleton,
    highValues_card, lowValues_card]
  rw [Finset.prod_ite, Finset.filter_mem_eq_inter, Finset.univ_inter]
  rw [Finset.prod_ite, Finset.prod_const_one, one_mul, ← Finset.sdiff_eq_filter,
    Finset.prod_const, Finset.card_sdiff_of_subset hZ]
  rw [← Finset.sdiff_eq_filter, ← Finset.compl_eq_univ_sdiff,
    Finset.prod_const, Finset.card_compl]
  rfl

private theorem highArrow_ne_sentinel {T : Finset Block} {j i : Block}
    (hj : j ∈ T) (h : highArrow j T = some i) : i ≠ j := by
  unfold highArrow at h
  rw [Finset.insert_eq_of_mem hj] at h
  match hs : T.sort with
  | [] | [_] | [_, _] => simp [hs] at h
  | a :: b :: c :: rest =>
    have hn := T.sort_nodup (· ≤ ·)
    rw [hs] at hn
    simp only [hs] at h
    split at h
    · simp at h
    · rename_i hja
      split at h
      · rename_i hjb
        have hbc := (List.nodup_cons.mp (List.nodup_cons.mp hn).2).1
        simp only [Option.some.injEq] at h
        rintro rfl
        exact hbc (by simp [← hjb, h])
      · simp only [Option.some.injEq] at h
        exact h ▸ Ne.symm hja

private theorem highArrow_count (T : Finset Block) :
    (T.filter fun j => (highArrow j T).isSome).card =
      if 3 ≤ T.card then T.card - 1 else 0 := by
  have hl := T.length_sort (· ≤ ·)
  match hs : T.sort with
  | [] | [_] | [_, _] =>
    have he : (T.filter fun j => (highArrow j T).isSome) = ∅ := by
      ext j
      rw [Finset.mem_filter]
      by_cases hj : j ∈ T
      · simp [hj, highArrow, Finset.insert_eq_of_mem hj, hs]
      · simp [hj]
    rw [hs] at hl
    simp [he, ← hl]
  | a :: b :: c :: rest =>
    have ha : a ∈ T := by rw [← Finset.mem_sort (· ≤ ·), hs]; simp
    have he : (T.filter fun j => (highArrow j T).isSome) = T.erase a := by
      ext j
      rw [Finset.mem_filter, Finset.mem_erase]
      by_cases hj : j ∈ T
      · simp only [hj, true_and, and_true, highArrow, Finset.insert_eq_of_mem hj, hs]
        by_cases hja : j = a
        · simp [hja]
        · by_cases hjb : j = b <;> simp [hja, hjb]
      · simp [hj]
    have hc : 3 ≤ T.card := by rw [← hl, hs]; simp
    rw [he, Finset.card_erase_of_mem ha, ite_eq_left hc]

private def arrowAssignments (T : Finset Block) (j : Block) : Finset Baseline :=
  match highArrow j T with
  | none => ∅
  | some i => Fintype.piFinset (extraChoices T {i, j})

private theorem union_eq_insert {b : Baseline} {i j : Block} (hz : zeroSlots b = {i, j}) :
    zeroSlots b ∪ highSlots b = insert j (insert i (highSlots b)) := by
  rw [hz, Finset.insert_union, Finset.singleton_union, Finset.insert_comm]

private theorem mem_arrowAssignments {T : Finset Block} {j : Block} (hj : j ∈ T)
    (b : Baseline) :
    b ∈ arrowAssignments T j ↔ zeroSlots b ∪ highSlots b = T ∧
      ∃ i, i ≠ j ∧ zeroSlots b = {i, j} ∧ activeAxis b = some i := by
  constructor
  · cases h : highArrow j T with
    | none => simp [arrowAssignments, h]
    | some i =>
      intro hb
      have hZ : ({i, j} : Finset Block) ⊆ T := Finset.insert_subset_iff.mpr
        ⟨highArrow_mem h, Finset.singleton_subset_iff.mpr hj⟩
      obtain ⟨hz, ht⟩ := (mem_extraChoices b hZ).mp (by simpa [arrowAssignments, h] using hb)
      have hij := highArrow_ne_sentinel hj h
      refine ⟨ht, i, hij, hz, activeAxis_pair_of_arrow hij hz ?_⟩
      simpa only [highArrow, Finset.insert_eq_of_mem hj, ← union_eq_insert hz, ht] using h
  · rintro ⟨ht, i, hij, hz, ha⟩
    have h := activeAxis_pair_arrow hij hz ha
    have h' : highArrow j T = some i := by
      simpa only [highArrow, ← union_eq_insert hz, ht, Finset.insert_eq_of_mem hj] using h
    have hZ : ({i, j} : Finset Block) ⊆ T := Finset.insert_subset_iff.mpr
      ⟨highArrow_mem h', Finset.singleton_subset_iff.mpr hj⟩
    simpa [arrowAssignments, h'] using (mem_extraChoices b hZ).mpr ⟨hz, ht⟩

private def extraAssignments (T : Finset Block) : Finset Baseline :=
  T.biUnion (arrowAssignments T)

private theorem mem_extraAssignments {T : Finset Block} (b : Baseline) :
    b ∈ extraAssignments T ↔ zeroSlots b ∪ highSlots b = T ∧
      (zeroSlots b).card = 2 ∧ (activeAxis b).isSome := by
  simp only [extraAssignments, Finset.mem_biUnion]
  constructor
  · rintro ⟨j, hj, hb⟩
    obtain ⟨ht, i, hij, hz, ha⟩ := (mem_arrowAssignments hj b).mp hb
    exact ⟨ht, by simp [hz, Finset.card_pair hij, ha]⟩
  · rintro ⟨ht, hc, ha⟩
    obtain ⟨i, hi⟩ := Option.isSome_iff_exists.mp ha
    rcases activeAxis_zeroSlots_cases hi with hz | ⟨j, hij, hz⟩
    · simp [hz] at hc
    · have hj : j ∈ T := by rw [← ht, hz]; simp
      exact ⟨j, hj, (mem_arrowAssignments hj b).mpr ⟨ht, i, hij, hz, hi⟩⟩

private theorem card_extraAssignments (T : Finset Block) :
    (extraAssignments T).card =
      (if 3 ≤ T.card then T.card - 1 else 0) *
        (220 ^ (T.card - 2) * 1827 ^ (19 - T.card)) := by
  have hd : (T : Set Block).PairwiseDisjoint (arrowAssignments T) := by
    intro j hj k hk hjk
    apply Finset.disjoint_left.mpr
    intro b hb hc
    obtain ⟨_, i, hij, hz, ha⟩ := (mem_arrowAssignments hj b).mp hb
    obtain ⟨_, i', hik, hz', ha'⟩ := (mem_arrowAssignments hk b).mp hc
    have h := Option.some.inj (ha.symm.trans ha')
    subst i'
    have hk' : k ∈ zeroSlots b := by simp [hz']
    rw [hz] at hk'
    simp [hik.symm, hjk.symm] at hk'
  rw [extraAssignments, Finset.card_biUnion hd, ← highArrow_count, ← Nat.nsmul_eq_mul,
    ← Finset.sum_const, Finset.sum_filter]
  apply Finset.sum_congr rfl
  intro j hj
  cases h : highArrow j T with
  | none => simp [arrowAssignments, h]
  | some i =>
    have hZ : ({i, j} : Finset Block) ⊆ T := Finset.insert_subset_iff.mpr
        ⟨highArrow_mem h, Finset.singleton_subset_iff.mpr hj⟩
    simp [arrowAssignments, h, card_extraChoices T hZ, Finset.card_pair (highArrow_ne_sentinel hj h)]

/-- The cumulative count at the first extra pool threshold, 55. -/
theorem extra_center_count :
    (Finset.univ.filter fun b : Baseline => (zeroSlots b).card = 2 ∧ (activeAxis b).isSome).card =
      newCount 55 := by
  let U : Finset Block := Finset.univ
  have hd : (U.powerset : Set (Finset Block)).PairwiseDisjoint extraAssignments := by
    intro T _ S _ hTS
    apply Finset.disjoint_left.mpr
    intro b hb hc
    exact hTS (((mem_extraAssignments b).mp hb).1.symm.trans ((mem_extraAssignments b).mp hc).1)
  have he : (Finset.univ.filter fun b : Baseline => (zeroSlots b).card = 2 ∧ (activeAxis b).isSome) =
      U.powerset.biUnion extraAssignments := by
    ext b
    simp [Finset.mem_biUnion, mem_extraAssignments, U]
  rw [he, Finset.card_biUnion hd]
  simp_rw [card_extraAssignments]
  let f (t : ℕ) := (if 3 ≤ t then t - 1 else 0) * (220 ^ (t - 2) * 1827 ^ (19 - t))
  change (∑ T ∈ U.powerset, f T.card) = _
  rw [Finset.sum_powerset]
  simp_rw [Finset.sum_powersetCard]
  have hU : U.card = 19 := by simp [U]
  rw [hU]
  have hI : (Finset.range 20).filter (fun t => 3 ≤ t) = Finset.Icc 3 19 := by
    ext t
    simp only [Finset.mem_filter, Finset.mem_range, Finset.mem_Icc]
    omega
  rw [newCount, ite_eq_left rfl, ← hI, Finset.sum_filter]
  apply Finset.sum_congr rfl
  intro t _
  by_cases ht : 3 ≤ t <;> simp [f, ht, mul_assoc, mul_left_comm]

end SharpOC.Witness1387
