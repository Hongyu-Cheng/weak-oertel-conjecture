import SharpOC.Witness1387.Arithmetic
import SharpOC.Witness1387.SupportExposure
import Mathlib.Order.Interval.Finset.Fin

/-! Cumulative counts for ordinary centers, with the shared tail-rank cutoff. -/

namespace SharpOC.Witness1387

open scoped BigOperators

/-- The fifteen tail codes in descending priority, with their last two bits removed. -/
def tailCode (r : Fin 15) : ℕ :=
  ![60, 58, 57, 54, 53, 51, 46, 45, 43, 39, 30, 29, 27, 23, 15] r

private theorem tailCode_anti : StrictAnti tailCode := by
  change ∀ a b : Fin 15, a < b → tailCode b < tailCode a
  decide +kernel

private theorem tail_parts {s : Slot} (hs : tail s = true) :
    eligible s = true ∧ high s = false ∧ code s % 4 = 0 := by
  have ⟨he, hh⟩ : eligible s = true ∧ high s = false := by simpa [tail] using hs
  exact ⟨he, hh, by simpa [high, he] using hh⟩

private theorem tail_code_rank {s : Slot} (hs : tail s = true) :
    ∃ r : Fin 15, code s / 4 = tailCode r := by
  have h : ∀ a : Fin 256, a.val % 4 = 0 →
      (Finset.univ.filter fun i : Fin 8 => a.val.testBit i.val = true).card = 4 →
      ∃ r : Fin 15, a.val / 4 = tailCode r := by decide +kernel
  have ⟨he, _, hm⟩ := tail_parts hs
  exact h ⟨code s, eligible_code_lt s he⟩ hm (eligible_code_weight s he)

private noncomputable def tailRank (s : Slot) : Fin 15 :=
  if h : tail s = true then Classical.choose (tail_code_rank h) else 0

private theorem tailRank_spec {s : Slot} (hs : tail s = true) :
    code s / 4 = tailCode (tailRank s) := by
  simpa only [tailRank, dite_eq_left hs] using Classical.choose_spec (tail_code_rank hs)

private theorem tailRank_inj {s t : Slot} (hs : tail s = true) (ht : tail t = true)
    (ho : owner s = owner t) (hr : tailRank s = tailRank t) : s = t := by
  have hc : code s / 4 = code t / 4 := by
    rw [tailRank_spec hs, tailRank_spec ht, hr]
  have hm := (tail_parts hs).2.2
  have hm' := (tail_parts ht).2.2
  exact eligible_owner_code_injective (tail_parts hs).1 (tail_parts ht).1 ho (by omega)

private theorem tail_filter_card (row : Fin 4) (p : ℕ → Prop) [DecidablePred p] :
    (Finset.univ.filter fun s : Slot => tail s = true ∧ owner s = row ∧ p (code s / 4)).card =
      (Finset.univ.filter fun r : Fin 15 => p (tailCode r)).card := by
  let S := Finset.univ.filter fun s : Slot => tail s = true ∧ owner s = row
  have hS (s : Slot) : s ∈ S ↔ tail s = true ∧ owner s = row := by simp [S]
  have hinj : Set.InjOn tailRank (S : Set Slot) := by
    intro s hs t ht hr
    have ⟨hs, hso⟩ := (hS s).mp hs
    have ⟨ht, hto⟩ := (hS t).mp ht
    exact tailRank_inj hs ht (hso.trans hto.symm) hr
  have hall : S.image tailRank = Finset.univ := by
    apply Finset.eq_of_subset_of_card_le (Finset.subset_univ _)
    rw [Finset.card_image_of_injOn hinj]
    simpa [S, tail, Bool.and_eq_true, and_assoc] using (tail_owner_count row).ge
  apply Finset.card_bij (fun s _ => tailRank s)
  · intro s hs
    simp only [Finset.mem_filter, Finset.mem_univ, true_and] at hs ⊢
    rw [← tailRank_spec hs.1]
    exact hs.2.2
  · intro s hs t ht hr
    exact hinj ((hS s).mpr ⟨(Finset.mem_filter.mp hs).2.1, (Finset.mem_filter.mp hs).2.2.1⟩)
      ((hS t).mpr ⟨(Finset.mem_filter.mp ht).2.1, (Finset.mem_filter.mp ht).2.2.1⟩) hr
  · intro r hr
    have hr' : r ∈ S.image tailRank := by rw [hall]; exact Finset.mem_univ _
    obtain ⟨s, hs, hsr⟩ := Finset.mem_image.mp hr'
    have ⟨hst, hso⟩ := (hS s).mp hs
    exact ⟨s, Finset.mem_filter.mpr ⟨Finset.mem_univ _, hst, hso,
      by simpa only [tailRank_spec hst, hsr] using (Finset.mem_filter.mp hr).2⟩, hsr⟩

private theorem card_by_owner (p : Slot → Prop) [DecidablePred p] :
    (Finset.univ.filter p).card =
      ∑ j : Fin 4, (Finset.univ.filter fun s => p s ∧ owner s = j).card := by
  let S (j : Fin 4) := Finset.univ.filter fun s => p s ∧ owner s = j
  have hd : ((Finset.univ : Finset (Fin 4)) : Set (Fin 4)).PairwiseDisjoint S := by
    intro i _ j _ hij
    apply Finset.disjoint_filter.mpr
    intro s _ hi hj
    exact hij (hi.2.symm.trans hj.2)
  have hU : Finset.univ.biUnion S = Finset.univ.filter p := by
    ext s
    simp [S]
  rw [← hU, Finset.card_biUnion hd]

theorem high_count : (Finset.univ.filter fun s : Slot => high s = true).card = 220 := by
  rw [card_by_owner]
  simp [high_owner_count]

theorem nonhigh_nonzero_count :
    (Finset.univ.filter fun s : Slot => s ≠ 0 ∧ high s = false).card = 1827 := by
  let S : Finset Slot := Finset.univ.erase 0
  let H := Finset.univ.filter fun s : Slot => high s = true
  have hs : S.card = 2047 := by simp [S, Finset.card_erase_of_mem]
  have hsub : H ⊆ S := by
    intro s hs
    have hh := (Finset.mem_filter.mp hs).2
    have hn : s ≠ 0 := by rintro rfl; simp at hh
    simp [S, hn]
  have he : (Finset.univ.filter fun s : Slot => s ≠ 0 ∧ high s = false) = S \ H := by
    ext s
    cases h : high s <;> simp [S, H, h]
  rw [he, Finset.card_sdiff_of_subset hsub, hs, high_count]

/-- Nonzero, nonhigh slots whose tail code is below the given cutoff
(strictly below when the competing block is earlier). -/
def tailCut (r : Fin 15) (strict : Bool) : Finset Slot :=
  Finset.univ.filter fun s => s ≠ 0 ∧ high s = false ∧
    (tail s = true → if strict then code s / 4 < tailCode r else code s / 4 ≤ tailCode r)

set_option maxRecDepth 4000 in

theorem tail_cut_card (r : Fin 15) (strict : Bool) :
    (tailCut r strict).card = 1827 - 4 * (r.val + if strict then 1 else 0) := by
  let p : ℕ → Prop := fun c => ¬ (if strict then c < tailCode r else c ≤ tailCode r)
  let S := Finset.univ.filter fun s : Slot => s ≠ 0 ∧ high s = false
  let E := Finset.univ.filter fun s : Slot => tail s = true ∧ p (code s / 4)
  have hsub : E ⊆ S := by
    intro s hs
    have ht := (Finset.mem_filter.mp hs).2.1
    have hn : s ≠ 0 := by rintro rfl; simp [tail] at ht
    exact Finset.mem_filter.mpr ⟨Finset.mem_univ _, hn, (tail_parts ht).2.1⟩
  have he : tailCut r strict = S \ E := by
    ext s
    simp [tailCut, S, E, p, and_assoc]
  have hc : E.card = 4 * (r.val + if strict then 1 else 0) := by
    have hr : (Finset.univ.filter fun a : Fin 15 => p (tailCode a)).card =
        r.val + if strict then 1 else 0 := by
      cases strict
      · have he : (Finset.univ.filter fun a : Fin 15 => p (tailCode a)) = Finset.Iio r := by
          ext a
          simp [p, tailCode_anti.lt_iff_gt]
        simp [he, Fin.card_Iio]
      · have he : (Finset.univ.filter fun a : Fin 15 => p (tailCode a)) = Finset.Iic r := by
          ext a
          simp [p, tailCode_anti.le_iff_ge]
        simp [he, Fin.card_Iic]
    rw [card_by_owner (fun s => tail s = true ∧ p (code s / 4))]
    have hrow (j : Fin 4) : (Finset.univ.filter fun s : Slot =>
        (tail s = true ∧ p (code s / 4)) ∧ owner s = j).card =
        r.val + if strict then 1 else 0 := by
      simpa only [and_assoc, and_comm, and_left_comm] using (tail_filter_card j p).trans hr
    simp [hrow, Nat.mul_comm]
  rw [he, Finset.card_sdiff_of_subset hsub, nonhigh_nonzero_count, hc]

private theorem priority_le_iff (i j : Block) (a c : ℕ) :
    19 * a + (18 - j.val) ≤ 19 * c + (18 - i.val) ↔
      if j < i then a < c else a ≤ c := by
  have hi := i.isLt
  have hj := j.isLt
  by_cases h : j < i
  · have h' : j.val < i.val := h
    simp only [h, ite_true]
    omega
  · have h' : ¬ j.val < i.val := h
    simp only [h, ite_false]
    omega

private theorem bestTail_eq_some_iff (b : Baseline) (allowed : Block → Bool) (i : Block) :
    bestTail b allowed = some i ↔ allowed i = true ∧ tail (b i) = true ∧
      ∀ j, allowed j = true → tail (b j) = true → tailPriority b j ≤ tailPriority b i := by
  refine ⟨bestTail_spec, ?_⟩
  rintro ⟨hi, ht, hm⟩
  cases he : bestTail b allowed with
  | none =>
    exfalso
    have h := List.find?_eq_none.mp he i (List.mem_finRange i)
    apply h
    simp only [hi, ht, Bool.and_self, Bool.true_and]
    apply List.all_eq_true.mpr
    intro j _
    by_cases hj : allowed j = true <;> by_cases ht' : tail (b j) = true <;>
      simp [hj, ht', hm j]
  | some j =>
    obtain ⟨hj, ht', hm'⟩ := bestTail_spec he
    have hp := le_antisymm (hm j hj ht') (hm' i hi ht)
    congr
    apply Fin.ext
    have hi' := i.isLt
    have hj' := j.isLt
    unfold tailPriority at hp
    omega

private theorem tail_win_iff (b : Baseline) (i : Block) (allowed : Block → Bool)
    (hi : allowed i = true) {s : Slot} (hs : tail s = true) :
    bestTail (Function.update b i s) allowed = some i ↔
      ∀ j, j ≠ i → allowed j = true → tail (b j) = true →
        if j < i then code (b j) / 4 < code s / 4 else code (b j) / 4 ≤ code s / 4 := by
  rw [bestTail_eq_some_iff]
  simp only [hi, Function.update_self, hs, true_and]
  constructor
  · intro h j hj hj' ht
    have hp := h j hj' (by simpa [hj] using ht)
    exact (priority_le_iff i j _ _).mp (by simpa [tailPriority, hj] using hp)
  · intro h j hj ht
    by_cases he : j = i
    · subst j
      exact le_rfl
    · have hp := (priority_le_iff i j _ _).mpr (h j he hj (by simpa [he] using ht))
      simpa [tailPriority, he] using hp

/-- Once the tail routing uses a fixed candidate set, a pool reaches
the given threshold exactly when the indicated ranked tail wins. -/
theorem tail_threshold_iff (b : Baseline) (i : Block) (allowed : Block → Bool)
    (r : Fin 15) (row : Fin 4) (hi : allowed i = true)
    (hroute : ∀ s, tail s = true →
      selectedFlip (Function.update b i s) = bestTail (Function.update b i s) allowed)
    (ha : activeAxis b = some i) :
    56 + r.val ≤ pool b row ↔
      ∀ j, j ≠ i → allowed j = true → tail (b j) = true →
        if j < i then code (b j) / 4 < tailCode r else code (b j) / 4 ≤ tailCode r := by
  classical
  let p (c : ℕ) : Prop := ∀ j : Block, j ≠ i → allowed j = true → tail (b j) = true →
    if j < i then code (b j) / 4 < c else code (b j) / 4 ≤ c
  let H := Finset.univ.filter fun s : Slot => high s = true ∧ owner s = row
  let T := Finset.univ.filter fun s : Slot => tail s = true ∧ owner s = row ∧ p (code s / 4)
  have hU : poolSites b i row = H ∪ T := by
    ext s
    simp only [mem_poolSites, Finset.mem_union, H, T, Finset.mem_filter, Finset.mem_univ, true_and]
    constructor
    · rintro ⟨ho, hf⟩
      have h := selectedFlip_high_or_tail hf
      simp only [Function.update_self] at h
      rcases h with hh | ht
      · exact Or.inl ⟨hh, ho⟩
      · rw [hroute s ht, tail_win_iff b i allowed hi ht] at hf
        exact Or.inr ⟨ht, ho, hf⟩
    · rintro (⟨hh, ho⟩ | ⟨ht, ho, hp⟩)
      · exact ⟨ho, selectedFlip_update_high ha hh⟩
      · exact ⟨ho, (hroute s ht).trans ((tail_win_iff b i allowed hi ht).mpr hp)⟩
  have hd : Disjoint H T := by
    apply Finset.disjoint_filter.mpr
    intro s _ hh ht
    have h := (tail_parts ht.1).2.1
    simp [hh.1] at h
  have hcard : pool b row = 55 + (Finset.univ.filter fun a : Fin 15 => p (tailCode a)).card := by
    rw [pool, ha]
    change (poolSites b i row).card = _
    rw [hU, Finset.card_union_of_disjoint hd]
    exact congrArg₂ (· + ·) (high_owner_count row) (tail_filter_card row p)
  have hm {a a' : Fin 15} (hle : a ≤ a') (h : p (tailCode a')) : p (tailCode a) := by
    have hcode := tailCode_anti.antitone hle
    intro j hji hj ht
    specialize h j hji hj ht
    by_cases hjlt : j < i <;> simp only [hjlt, ite_true, ite_false] at h ⊢
    · exact h.trans_le hcode
    · exact h.trans hcode
  rw [hcard]
  constructor
  · intro h
    by_contra hn
    have hsub : (Finset.univ.filter fun a : Fin 15 => p (tailCode a)) ⊆ Finset.Iio r := by
      intro a ha'
      simp only [Finset.mem_Iio]
      exact lt_of_not_ge (fun hle => hn (hm hle (Finset.mem_filter.mp ha').2))
    have hc := Finset.card_le_card hsub
    rw [Fin.card_Iio] at hc
    omega
  · intro h
    have hsub : Finset.Iic r ⊆ (Finset.univ.filter fun a : Fin 15 => p (tailCode a)) := by
      intro a ha'
      exact Finset.mem_filter.mpr ⟨Finset.mem_univ _, hm (Finset.mem_Iic.mp ha') h⟩
    have hc := Finset.card_le_card hsub
    rw [Fin.card_Iic] at hc
    omega


private theorem ordinary_update_zeroSlots {b : Baseline} {i : Block} {s : Slot}
    (hz : zeroSlots b = {i}) (hs : s ≠ 0) :
    zeroSlots (Function.update b i s) = ∅ := by
  ext j
  by_cases hji : j = i
  · simp [hji, hs]
  · have h : b j ≠ 0 := by simpa [hji, hz] using (mem_zeroSlots (b := b) (i := j)).mpr
    simp [hji, h]

private theorem ordinary_update_highSlots {b : Baseline} {i : Block} {s : Slot}
    (hz : zeroSlots b = {i}) (hs : high s = false) :
    highSlots (Function.update b i s) = highSlots b := by
  have hi : b i = 0 := mem_zeroSlots.mp (by simp [hz])
  ext j
  by_cases hji : j = i <;> simp [hji, hi, hs]

private theorem ordinary_pool_le_of_high {b : Baseline} {i : Block}
    (hz : zeroSlots b = {i}) (ha : activeAxis b = some i)
    (hh : highSlots b ≠ ∅) : pool b 0 ≤ 55 := by
  rw [pool, ha]
  change (poolSites b i 0).card ≤ 55
  rw [← high_owner_count 0]
  apply Finset.card_le_card
  intro s hs
  obtain ⟨ho, hf⟩ := mem_poolSites.mp hs
  simp only [Finset.mem_filter, Finset.mem_univ, true_and]
  refine ⟨?_, ho⟩
  by_contra h
  have hfalse : high s = false := Bool.eq_false_of_not_eq_true h
  have hu := ordinary_update_highSlots hz hfalse
  have hn := selectedFlip_ne_zero hf
  simp only [Function.update_self] at hn
  have hzu := ordinary_update_zeroSlots hz hn
  unfold selectedFlip at hf
  rw [hzu, Finset.sort_empty, hu] at hf
  cases hsort : (highSlots b).sort with
  | nil =>
    apply hh
    simpa using congrArg List.toFinset hsort
  | cons j js =>
    have hji : j = i := by simpa [hsort] using hf
    have hj : j ∈ highSlots b := by rw [← Finset.mem_sort (· ≤ ·), hsort]; simp
    have hi : b i = 0 := mem_zeroSlots.mp (by simp [hz])
    simp [hji, hi] at hj

private theorem ordinary_tail_threshold {b : Baseline} {i : Block} (r : Fin 15)
    (hz : zeroSlots b = {i}) (hh : highSlots b = ∅) (ha : activeAxis b = some i) :
    56 + r.val ≤ pool b 0 ↔
      ∀ j, j ≠ i → tail (b j) = true →
        if j < i then code (b j) / 4 < tailCode r else code (b j) / 4 ≤ tailCode r := by
  have hr (s : Slot) (hs : tail s = true) :
      selectedFlip (Function.update b i s) = bestTail (Function.update b i s) (fun _ => true) := by
    have hn : s ≠ 0 := by rintro rfl; simp [tail] at hs
    rw [selectedFlip, ordinary_update_zeroSlots hz hn,
      ordinary_update_highSlots hz (tail_parts hs).2.1, hh, Finset.sort_empty]
  simpa using tail_threshold_iff b i (fun _ => true) r 0 rfl hr ha

private def ordinaryTailChoices (r : Fin 15) (i j : Block) : Finset Slot :=
  if j = i then {0} else tailCut r (decide (j < i))

private theorem ordinary_tail_choices_iff (b : Baseline) (i : Block) (r : Fin 15) :
    (zeroSlots b = {i} ∧ activeAxis b = some i ∧ 56 + r.val ≤ pool b 0) ↔
      ∀ j, b j ∈ ordinaryTailChoices r i j := by
  constructor
  · rintro ⟨hz, ha, hp⟩
    have hh : highSlots b = ∅ := by
      by_contra hn
      have h := ordinary_pool_le_of_high hz ha hn
      omega
    have ht := (ordinary_tail_threshold r hz hh ha).mp hp
    intro j
    by_cases hji : j = i
    · subst j
      have hi : b i = 0 := mem_zeroSlots.mp (by simp [hz])
      simp [ordinaryTailChoices, hi]
    · have hne : b j ≠ 0 := by
        intro h
        have hm := mem_zeroSlots.mpr h
        simp [hz, hji] at hm
      have hnh : high (b j) = false := by
        apply Bool.eq_false_of_not_eq_true
        intro h
        have hm := mem_highSlots.mpr h
        simp [hh] at hm
      simpa [ordinaryTailChoices, hji, tailCut, hne, hnh] using ht j hji
  · intro hc
    have hi : b i = 0 := by simpa [ordinaryTailChoices] using hc i
    have hj (j : Block) (hji : j ≠ i) : b j ≠ 0 ∧ high (b j) = false ∧
        (tail (b j) = true →
          if j < i then code (b j) / 4 < tailCode r else code (b j) / 4 ≤ tailCode r) := by
      simpa [ordinaryTailChoices, hji, tailCut] using hc j
    have hz : zeroSlots b = {i} := by
      ext j
      by_cases hji : j = i
      · simp [hji, hi]
      · simp [hji, (hj j hji).1]
    have hh : highSlots b = ∅ := by
      ext j
      by_cases hji : j = i
      · simp [hji, hi]
      · simp [(hj j hji).2.1]
    have ha : activeAxis b = some i := activeAxis_single_of hz (by simp [hh])
    exact ⟨hz, ha, (ordinary_tail_threshold r hz hh ha).mpr (fun j hji => (hj j hji).2.2)⟩

private theorem ordinary_tail_choices_count (r : Fin 15) (i j : Block) :
    (ordinaryTailChoices r i j).card =
      if j = i then 1 else if j < i then 1827 - 4 * (r.val + 1) else 1827 - 4 * r.val := by
  by_cases hji : j = i
  · simp [ordinaryTailChoices, hji]
  · by_cases hlt : j < i <;> simp [ordinaryTailChoices, hji, hlt, tail_cut_card]

set_option maxRecDepth 10000 in
private theorem ordinary_tail_count_at_axis [Fintype Baseline] (r : Fin 15) (i : Block) :
    (Finset.univ.filter fun b : Baseline =>
      zeroSlots b = {i} ∧ activeAxis b = some i ∧ 56 + r.val ≤ pool b 0).card =
    ∏ j : Block, if j = i then 1 else if j < i then 1827 - 4 * (r.val + 1) else 1827 - 4 * r.val := by
  have he : (Finset.univ.filter fun b : Baseline =>
      zeroSlots b = {i} ∧ activeAxis b = some i ∧ 56 + r.val ≤ pool b 0) =
        Fintype.piFinset (ordinaryTailChoices r i) := by
    ext b
    simpa only [Finset.mem_filter, Finset.mem_univ, true_and, Fintype.mem_piFinset] using
      ordinary_tail_choices_iff b i r
  rw [he, Fintype.card_piFinset]
  exact Finset.prod_congr rfl (fun j _ => ordinary_tail_choices_count r i j)

set_option maxRecDepth 10000 in
private theorem ordinary_pool_count_tail [Fintype Baseline] (r : Fin 15) :
    (Finset.univ.filter fun b : Baseline =>
      (zeroSlots b).card = 1 ∧ (activeAxis b).isSome ∧ 56 + r.val ≤ pool b 0).card =
      oldCount (56 + r.val) := by
  classical
  rw [Finset.card_eq_sum_card_fiberwise (f := fun b => (activeAxis b).getD 0)
    (t := Finset.univ) (fun _ _ => Finset.mem_univ _)]
  calc
    _ = ∑ i : Block, (Finset.univ.filter fun b : Baseline =>
        zeroSlots b = {i} ∧ activeAxis b = some i ∧ 56 + r.val ≤ pool b 0).card := by
      apply Finset.sum_congr rfl
      intro i _
      congr 1
      ext b
      simp only [Finset.mem_filter, Finset.mem_univ, true_and]
      constructor
      · rintro ⟨⟨hz, ha, hp⟩, hi⟩
        obtain ⟨j, hj⟩ := Option.isSome_iff_exists.mp ha
        have hji : j = i := by simpa [hj] using hi
        subst j
        rcases activeAxis_zeroSlots_cases hj with h | ⟨j, hij, h⟩
        · exact ⟨h, hj, hp⟩
        · simp [h, Finset.card_pair hij] at hz
      · rintro ⟨hz, ha, hp⟩
        simp [hz, ha, hp]
    _ = ∑ i : Block, ∏ j : Block,
        if j = i then 1 else if j < i then 1827 - 4 * (r.val + 1) else 1827 - 4 * r.val :=
      Finset.sum_congr rfl fun i _ => ordinary_tail_count_at_axis r i
    _ = oldCount (56 + r.val) := by fin_cases r <;> decide +kernel

set_option maxRecDepth 10000 in
/-- The number of ordinary active centers meeting each pool threshold. -/
theorem ordinary_pool_count (k : ℕ) (hk : 55 ≤ k) (hk' : k ≤ 71) :
    (Finset.univ.filter fun b : Baseline =>
      (zeroSlots b).card = 1 ∧ (activeAxis b).isSome ∧ k ≤ pool b 0).card = oldCount k := by
  rcases eq_or_lt_of_le hk with rfl | hlt
  · have he (b : Baseline) : ((zeroSlots b).card = 1 ∧ (activeAxis b).isSome ∧ 55 ≤ pool b 0) ↔
        (zeroSlots b).card = 1 ∧ (activeAxis b).isSome := by
      refine ⟨fun h => ⟨h.1, h.2.1⟩, fun h => ⟨h.1, h.2, ?_⟩⟩
      obtain ⟨i, hi⟩ := Option.isSome_iff_exists.mp h.2
      exact pool_ge_55_of_active hi 0
    simp_rw [he]
    exact ordinary_center_count
  · rcases eq_or_lt_of_le hk' with rfl | hlt'
    · have he (b : Baseline) : ¬ ((zeroSlots b).card = 1 ∧ (activeAxis b).isSome ∧ 71 ≤ pool b 0) :=
        fun h => (by have hu := pool_le_70 b 0; omega)
      simp [he, oldCount]
    · let r : Fin 15 := ⟨k - 56, by omega⟩
      have hr : 56 + r.val = k := by dsimp [r]; omega
      rw [← hr]
      exact ordinary_pool_count_tail r

end SharpOC.Witness1387
