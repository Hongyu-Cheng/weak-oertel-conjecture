import SharpOC.Witness1387.OrdinaryCount

/-! Cumulative counts of the two-zero centers whose pools contain tails. -/

namespace SharpOC.Witness1387

open scoped BigOperators

set_option Elab.async false
set_option maxHeartbeats 1000000

private def extraAllowed (r j : Block) (i : Block) : Bool :=
  decide (i < r) || decide (j < i)

private theorem extra_sort_triple {a b c : Block} (hab : a < b) (hbc : b < c) :
    (insert a (insert b ({c} : Finset Block))).sort = [a, b, c] := by
  rw [Finset.sort_insert (· ≤ ·), Finset.sort_insert (· ≤ ·)]
  · simp
  · simpa using hbc.le
  · simpa using hbc.ne
  · simp [hab.le, (hab.trans hbc).le]
  · simp [hab.ne, (hab.trans hbc).ne]

private theorem extra_arrow {i j r : Block} (hrj : r < j) (hi : extraAllowed r j i = true) :
    highArrow j (insert i ({r} : Finset Block)) = some i := by
  simp only [extraAllowed, Bool.or_eq_true, decide_eq_true_eq] at hi
  unfold highArrow
  rcases hi with hi | hi
  · have h : insert j (insert i ({r} : Finset Block)) = insert i (insert r {j}) := by
      ext x; simp only [Finset.mem_insert, Finset.mem_singleton]; tauto
    rw [h, extra_sort_triple hi hrj]
    simp [hrj.ne.symm, (hi.trans hrj).ne.symm]
  · have h : insert j (insert i ({r} : Finset Block)) = insert r (insert j {i}) := by
      ext x; simp only [Finset.mem_insert, Finset.mem_singleton]; tauto
    rw [h, extra_sort_triple hrj hi]
    simp [hrj.ne.symm]

private theorem extra_tail_update {b : Baseline} {i j : Block} {s : Slot}
    (hij : i ≠ j) (hz : zeroSlots b = insert i {j}) (hs : tail s = true) :
    zeroSlots (Function.update b i s) = {j} ∧
      highSlots (Function.update b i s) = highSlots b := by
  simp only [tail, Bool.and_eq_true, Bool.not_eq_true'] at hs
  have hne : s ≠ 0 := by rintro rfl; simp at hs
  have hi : b i = 0 := mem_zeroSlots.mp (by simp [hz])
  constructor <;> ext k
  · by_cases h : k = i
    · subst k
      simp [hne, hij]
    · have hk : b k = 0 ↔ k = j := by
        rw [← mem_zeroSlots, hz]
        simp [h]
      simp [h, hk]
  · by_cases h : k = i
    · subst k
      simp [hi, hs.2]
    · simp [h]

private theorem extra_tail_route {b : Baseline} {i j : Block} {s : Slot}
    (hij : i ≠ j) (hz : zeroSlots b = insert i {j}) (hs : tail s = true)
    (hf : selectedFlip (Function.update b i s) = some i) :
    ∃ r, highSlots b = {r} ∧ r < j ∧ extraAllowed r j i = true := by
  obtain ⟨hzu, hhu⟩ := extra_tail_update hij hz hs
  have hi : i ∉ highSlots b := by
    have hb : b i = 0 := mem_zeroSlots.mp (by simp [hz])
    simp [hb]
  unfold selectedFlip at hf
  rw [hzu, Finset.sort_singleton, hhu] at hf
  cases hh : (highSlots b).sort with
  | nil => exact (hi (highArrow_mem (by simpa [hh] using hf))).elim
  | cons r rs =>
    cases rs with
    | nil =>
      have hhr : highSlots b = {r} := by simpa using congrArg List.toFinset hh
      by_cases hrj : r < j
      · have ht : bestTail (Function.update b i s) (extraAllowed r j) = some i := by
          unfold extraAllowed
          simpa [hh, hrj] using hf
        exact ⟨r, hhr, hrj, (bestTail_spec ht).1⟩
      · simp [hh, hrj] at hf
    | cons r' rs => exact (hi (highArrow_mem (by simpa [hh] using hf))).elim

private theorem extra_selectedFlip_eq {b : Baseline} {i j r : Block} {s : Slot}
    (hij : i ≠ j) (hz : zeroSlots b = insert i {j})
    (hh : highSlots b = {r}) (hrj : r < j) (hs : tail s = true) :
    selectedFlip (Function.update b i s) = bestTail (Function.update b i s) (extraAllowed r j) := by
  obtain ⟨hzu, hhu⟩ := extra_tail_update hij hz hs
  unfold extraAllowed
  simp [selectedFlip, hzu, hhu, hh, hrj]

private theorem exists_extra_tail {b : Baseline} {i : Block}
    (ha : activeAxis b = some i) (hk : 55 < pool b 0) :
    ∃ s, tail s = true ∧ selectedFlip (Function.update b i s) = some i := by
  by_contra! h
  have hsub : poolSites b i 0 ⊆ Finset.univ.filter (fun s => high s = true ∧ owner s = 0) := by
    intro s hs
    obtain ⟨ho, hf⟩ := mem_poolSites.mp hs
    have htype : high s = true ∨ tail s = true := by
      simpa only [Function.update_self] using selectedFlip_high_or_tail hf
    rcases htype with hh | ht
    · exact Finset.mem_filter.mpr ⟨Finset.mem_univ s, hh, ho⟩
    · exact (h s ht hf).elim
  have hc := Finset.card_le_card hsub
  rw [high_owner_count] at hc
  simp only [pool, ha] at hk
  omega

private abbrev ExtraIndices := Block × Block × Block

private def extraIndices : Finset ExtraIndices :=
  Finset.univ.filter fun (i, j, r) => r < j ∧ extraAllowed r j i = true

private theorem mem_extraIndices {i j r : Block} :
    (i, j, r) ∈ extraIndices ↔ r < j ∧ (i < r ∨ j < i) := by
  simp [extraIndices, extraAllowed]

private def extraAxisCount (j r : Block) : ℕ := r.val + 18 - j.val

-- Positions count the candidate axes before i, first below r and then above j.
private def extraAxisPosition (i j r : Block) : ℕ :=
  if i < r then i.val else r.val + (i.val - j.val - 1)

private def extraBefore (i j r : Block) : Finset Block :=
  Finset.univ.filter fun l => l < i ∧ (l < r ∨ j < l)

private def extraAfter (i j r : Block) : Finset Block :=
  Finset.univ.filter fun l => i < l ∧ (l < r ∨ j < l)

private theorem extra_before_card {i j r : Block} (h : (i, j, r) ∈ extraIndices) :
    (extraBefore i j r).card = extraAxisPosition i j r := by
  obtain ⟨hrj, hi⟩ := mem_extraIndices.mp h
  rcases hi with hi | hi
  · have he : extraBefore i j r = Finset.Iio i := by
      ext l
      simp only [extraBefore, Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_Iio]
      exact and_iff_left_of_imp (fun hl => Or.inl (hl.trans hi))
    simp [he, extraAxisPosition, hi, Fin.card_Iio]
  · have hri : ¬i < r := not_lt_of_ge (hrj.trans hi).le
    have he : extraBefore i j r = Finset.Iio r ∪ Finset.Ioo j i := by
      ext l
      simp only [extraBefore, Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_union,
        Finset.mem_Iio, Finset.mem_Ioo, Fin.lt_def] at *
      omega
    have hd : Disjoint (Finset.Iio r) (Finset.Ioo j i) := by
      rw [Finset.disjoint_left]
      simp only [Finset.mem_Iio, Finset.mem_Ioo]
      exact fun _ hl hm => (not_lt_of_gt (hrj.trans hm.1)) hl
    rw [he, Finset.card_union_of_disjoint hd, Fin.card_Iio, Fin.card_Ioo,
      extraAxisPosition, ite_eq_right hri]

private theorem extra_after_card {i j r : Block} (h : (i, j, r) ∈ extraIndices) :
    (extraAfter i j r).card = extraAxisCount j r - 1 - extraAxisPosition i j r := by
  obtain ⟨hrj, hi⟩ := mem_extraIndices.mp h
  rcases hi with hi | hi
  · have he : extraAfter i j r = Finset.Ioo i r ∪ Finset.Ioi j := by
      ext l
      simp only [extraAfter, Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_union,
        Finset.mem_Ioi, Finset.mem_Ioo, Fin.lt_def] at *
      omega
    have hd : Disjoint (Finset.Ioo i r) (Finset.Ioi j) := by
      rw [Finset.disjoint_left]
      simp only [Finset.mem_Ioo, Finset.mem_Ioi]
      exact fun _ hl hm => (not_lt_of_gt (hrj.trans hm)) hl.2
    rw [he, Finset.card_union_of_disjoint hd, Fin.card_Ioo, Fin.card_Ioi,
      extraAxisCount, extraAxisPosition, ite_eq_left hi]
    simp only [Fin.lt_def] at hi hrj
    have := j.isLt
    omega
  · have hri : ¬i < r := not_lt_of_ge (hrj.trans hi).le
    have he : extraAfter i j r = Finset.Ioi i := by
      ext l
      simp only [extraAfter, Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_Ioi]
      exact and_iff_left_of_imp (fun hl => Or.inr (hi.trans hl))
    rw [he, Fin.card_Ioi, extraAxisCount, extraAxisPosition, ite_eq_right hri]
    simp only [Fin.lt_def] at hi hrj
    have := i.isLt
    omega

private theorem extra_weight_product (a b : ℕ) {i j r : Block}
    (h : (i, j, r) ∈ extraIndices) :
    (∏ l : Block, if l = i ∨ l = j then 1 else if l = r then 220 else
        if extraAllowed r j l = true then (if l < i then a else b) else 1827) =
      220 * 1827 ^ (17 - extraAxisCount j r) * a ^ extraAxisPosition i j r *
        b ^ (extraAxisCount j r - 1 - extraAxisPosition i j r) := by
  obtain ⟨hrj, hi⟩ := mem_extraIndices.mp h
  have he (l : Block) :
      (if l = i ∨ l = j then 1 else if l = r then 220 else
        if extraAllowed r j l = true then (if l < i then a else b) else 1827) =
      (if l = r then 220 else 1) * (if l ∈ Finset.Ioo r j then 1827 else 1) *
        (if l ∈ extraBefore i j r then a else 1) * (if l ∈ extraAfter i j r then b else 1) := by
    simp only [extraBefore, extraAfter, Finset.mem_filter, Finset.mem_univ, true_and,
      Finset.mem_Ioo, extraAllowed, Bool.or_eq_true, decide_eq_true_eq]
    split_ifs <;> simp_all <;> simp only [Fin.lt_def, Fin.le_def, Fin.ext_iff] at * <;> omega
  simp_rw [he, Finset.prod_mul_distrib, Fintype.prod_ite_eq', Fintype.prod_ite_mem,
    Finset.prod_const, extra_before_card h, extra_after_card h, Fin.card_Ioo]
  rw [show j.val - r.val - 1 = 17 - extraAxisCount j r by
    simp only [extraAxisCount, Fin.lt_def] at *
    have := j.isLt
    omega]

-- Reindex each triple by the number of candidates, the fixed high, and the
-- zero-based position of the varying axis among the candidates.
private def extraAxisParameters : Finset (Σ _ : ℕ, ℕ × ℕ) :=
  (Finset.Icc 1 17).sigma fun m => (Finset.range (m + 1)) ×ˢ (Finset.range m)

private def extraAxisParam (t : ExtraIndices) : Σ _ : ℕ, ℕ × ℕ :=
  ⟨extraAxisCount t.2.1 t.2.2, t.2.2.val, extraAxisPosition t.1 t.2.1 t.2.2⟩

private theorem extraAxisParam_mem (t : ExtraIndices) (ht : t ∈ extraIndices) :
    extraAxisParam t ∈ extraAxisParameters := by
  obtain ⟨i, j, r⟩ := t
  obtain ⟨hrj, hi⟩ := mem_extraIndices.mp ht
  have := i.isLt
  have := j.isLt
  simp only [extraAxisParam, extraAxisParameters, Finset.mem_sigma, Finset.mem_Icc,
    Finset.mem_product, Finset.mem_range, extraAxisCount, extraAxisPosition, Fin.lt_def] at *
  split_ifs <;> omega

private theorem extraAxisParam_inj : Set.InjOn extraAxisParam (extraIndices : Set ExtraIndices) := by
  intro t ht u hu he
  obtain ⟨i, j, r⟩ := t
  obtain ⟨i', j', r'⟩ := u
  obtain ⟨hrj, hi⟩ := mem_extraIndices.mp ht
  obtain ⟨hrj', hi'⟩ := mem_extraIndices.mp hu
  have hm := congrArg (fun x : Σ _ : ℕ, ℕ × ℕ => x.1) he
  have hr := congrArg (fun x : Σ _ : ℕ, ℕ × ℕ => x.2.1) he
  have hp := congrArg (fun x : Σ _ : ℕ, ℕ × ℕ => x.2.2) he
  have hj := j.isLt
  have hj' := j'.isLt
  simp only [extraAxisParam, extraAxisCount, extraAxisPosition, Prod.mk.injEq,
    Fin.ext_iff, Fin.lt_def] at hm hr hp hrj hi hrj' hi' ⊢
  split_ifs at hp <;> omega

private theorem extraAxisParam_surj (x : Σ _ : ℕ, ℕ × ℕ) (hx : x ∈ extraAxisParameters) :
    ∃ t ∈ extraIndices, extraAxisParam t = x := by
  obtain ⟨m, q, p⟩ := x
  simp only [extraAxisParameters, Finset.mem_sigma, Finset.mem_Icc,
    Finset.mem_product, Finset.mem_range] at hx
  let r : Block := ⟨q, by omega⟩
  let j : Block := ⟨18 + q - m, by omega⟩
  let i : Block := ⟨if p < q then p else 18 + q - m + 1 + (p - q), by split_ifs <;> omega⟩
  refine ⟨(i, j, r), mem_extraIndices.mpr ?_, ?_⟩
  · simp only [Fin.lt_def, r, j, i]
    split_ifs <;> omega
  · have hm : extraAxisCount j r = m := by simp only [extraAxisCount, j, r]; omega
    have hp : extraAxisPosition i j r = p := by
      simp only [extraAxisPosition, Fin.lt_def, r, j, i]
      split_ifs <;> omega
    simp [extraAxisParam, hm, hp, r]

private theorem extra_weight_sum (a b : ℕ) (hab : a + 4 = b) :
    (∑ t ∈ extraIndices,
      220 * 1827 ^ (17 - extraAxisCount t.2.1 t.2.2) * a ^ extraAxisPosition t.1 t.2.1 t.2.2 *
        b ^ (extraAxisCount t.2.1 t.2.2 - 1 - extraAxisPosition t.1 t.2.1 t.2.2)) =
    ∑ m ∈ Finset.Icc 1 17, (m + 1) * 220 * 1827 ^ (17 - m) * (b ^ m - a ^ m) / 4 := by
  calc
    _ = ∑ x ∈ extraAxisParameters, 220 * 1827 ^ (17 - x.1) * a ^ x.2.2 *
          b ^ (x.1 - 1 - x.2.2) := by
      exact Finset.sum_nbij extraAxisParam extraAxisParam_mem extraAxisParam_inj
        (fun x hx => extraAxisParam_surj x hx) (fun _ _ => rfl)
    _ = _ := by
      rw [extraAxisParameters, Finset.sum_sigma]
      apply Finset.sum_congr rfl
      intro m _
      rw [Finset.sum_product]
      simp only [Finset.sum_const, Finset.card_range, nsmul_eq_mul]
      simp_rw [mul_assoc, ← Finset.mul_sum]
      have hgeom : (∑ p ∈ Finset.range m, a ^ p * b ^ (m - 1 - p)) * 4 = b ^ m - a ^ m := by
        have h := geom_sum₂_mul_of_le (show a ≤ b by omega) m
        rwa [show b - a = 4 by omega] at h
      simp only [← hgeom, ← mul_assoc, Nat.mul_div_cancel _ (by decide : 0 < 4), Nat.cast_id]

private def extraChoices (n : Fin 15) (t : ExtraIndices) (l : Block) : Finset Slot :=
  if l = t.1 ∨ l = t.2.1 then {0}
  else if l = t.2.2 then Finset.univ.filter (fun s => high s = true)
  else if extraAllowed t.2.2 t.2.1 l = true then tailCut n (decide (l < t.1))
  else Finset.univ.filter (fun s => s ≠ 0 ∧ high s = false)

private theorem extra_choices_iff (n : Fin 15) (b : Baseline) {i j r : Block}
    (h : (i, j, r) ∈ extraIndices) :
    (∀ l, b l ∈ extraChoices n (i, j, r) l) ↔
      zeroSlots b = insert i {j} ∧ highSlots b = {r} ∧
      (∀ l, l ≠ i → extraAllowed r j l = true → tail (b l) = true →
        if l < i then code (b l) / 4 < tailCode n else code (b l) / 4 ≤ tailCode n) := by
  obtain ⟨hrj, hi⟩ := mem_extraIndices.mp h
  have hir : i ≠ r := by
    rintro rfl
    simp [not_lt_of_gt hrj] at hi
  simp only [Finset.ext_iff, mem_zeroSlots, mem_highSlots, Finset.mem_insert,
    Finset.mem_singleton, ← forall_and]
  apply forall_congr'
  intro l
  by_cases hli : l = i
  · subst l
    simp [extraChoices, hir]
    intro hzero
    simp [hzero]
  by_cases hlj : l = j
  · subst l
    simp [extraChoices, hrj.ne.symm, extraAllowed, not_lt_of_gt hrj]
    intro hzero
    simp [hzero]
  by_cases hlr : l = r
  · subst l
    simp [extraChoices, hli, hlj, extraAllowed, not_lt_of_gt hrj]
    intro hhigh hzero
    simp [hzero] at hhigh
  by_cases ha : extraAllowed r j l = true
  · simp [extraChoices, hli, hlj, hlr, ha, tailCut]
  · simp [extraChoices, hli, hlj, hlr, ha]

private theorem extra_indices_ne {i j r : Block} (h : (i, j, r) ∈ extraIndices) : i ≠ j := by
  obtain ⟨hrj, hi⟩ := mem_extraIndices.mp h
  rintro rfl
  simp [not_lt_of_gt hrj] at hi

private def extraFiber [Fintype Baseline] (n : Fin 15) (t : ExtraIndices) : Finset Baseline :=
  Finset.univ.filter fun b => zeroSlots b = insert t.1 {t.2.1} ∧ highSlots b = {t.2.2} ∧
    activeAxis b = some t.1 ∧ 56 + n.val ≤ pool b 0

private theorem extra_fiber_choices [Fintype Baseline] (n : Fin 15) {i j r : Block}
    (h : (i, j, r) ∈ extraIndices) :
    extraFiber n (i, j, r) = Fintype.piFinset (extraChoices n (i, j, r)) := by
  have hij := extra_indices_ne h
  obtain ⟨hrj, hi⟩ := mem_extraIndices.mp h
  have hallow : extraAllowed r j i = true := by simpa [extraAllowed] using hi
  ext b
  simp only [extraFiber, Finset.mem_filter, Finset.mem_univ, true_and,
    Fintype.mem_piFinset, extra_choices_iff n b h]
  constructor
  · rintro ⟨hz, hh, ha, hp⟩
    exact ⟨hz, hh, (tail_threshold_iff b i (extraAllowed r j) n 0 hallow
      (fun _ => extra_selectedFlip_eq hij hz hh hrj) ha).mp hp⟩
  · rintro ⟨hz, hh, hp⟩
    have ha := activeAxis_pair_of_arrow hij hz (by rw [hh]; exact extra_arrow hrj hallow)
    exact ⟨hz, hh, ha, (tail_threshold_iff b i (extraAllowed r j) n 0 hallow
      (fun _ => extra_selectedFlip_eq hij hz hh hrj) ha).mpr hp⟩

private theorem extra_fiber_count [Fintype Baseline] (n : Fin 15) (t : ExtraIndices)
    (h : t ∈ extraIndices) :
    (extraFiber n t).card =
      220 * 1827 ^ (17 - extraAxisCount t.2.1 t.2.2) *
      (1827 - 4 * (n.val + 1)) ^ extraAxisPosition t.1 t.2.1 t.2.2 *
      (1827 - 4 * n.val) ^ (extraAxisCount t.2.1 t.2.2 - 1 - extraAxisPosition t.1 t.2.1 t.2.2) := by
  obtain ⟨i, j, r⟩ := t
  rw [extra_fiber_choices n h, Fintype.card_piFinset, ← extra_weight_product _ _ h]
  apply Finset.prod_congr rfl
  intro l _
  simp only [extraChoices]
  split_ifs with hz hr ha hl
  · simp
  · exact high_count
  · rw [tail_cut_card]; simp [hl]
  · rw [tail_cut_card]; simp [hl]
  · exact nonhigh_nonzero_count

private theorem extra_fiber_disjoint [Fintype Baseline] (n : Fin 15) :
    (extraIndices : Set ExtraIndices).PairwiseDisjoint (extraFiber n) := by
  intro t ht u hu hne
  obtain ⟨i, j, r⟩ := t
  obtain ⟨i', j', r'⟩ := u
  apply Finset.disjoint_filter.mpr
  intro b _ hb hc
  obtain ⟨hz, hh, ha, _⟩ := hb
  obtain ⟨hz', hh', ha', _⟩ := hc
  have hi : i = i' := Option.some.inj (ha.symm.trans ha')
  have hr : r = r' := by simpa using hh.symm.trans hh'
  subst i'
  subst r'
  have hj : j ∈ insert i ({j'} : Finset Block) := by rw [← hz', hz]; simp
  have hje : j = j' := by simpa [Ne.symm (extra_indices_ne ht)] using hj
  exact hne (by rw [hje])

private theorem extra_tail_count_rank [Fintype Baseline] (n : Fin 15) :
    (Finset.univ.filter fun b : Baseline =>
      (zeroSlots b).card = 2 ∧ (activeAxis b).isSome ∧ 56 + n.val ≤ pool b 0).card =
      newCount (56 + n.val) := by
  have he : (Finset.univ.filter fun b : Baseline =>
      (zeroSlots b).card = 2 ∧ (activeAxis b).isSome ∧ 56 + n.val ≤ pool b 0) =
      extraIndices.biUnion (extraFiber n) := by
    ext b
    simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_biUnion, extraFiber]
    constructor
    · rintro ⟨hz, ha, hk⟩
      obtain ⟨i, hi⟩ := Option.isSome_iff_exists.mp ha
      rcases activeAxis_zeroSlots_cases hi with h | ⟨j, hij, h⟩
      · simp [h] at hz
      · obtain ⟨s, hs, hsf⟩ := exists_extra_tail hi (by omega)
        obtain ⟨r, hr, hrj, hallow⟩ := extra_tail_route hij h hs hsf
        exact ⟨(i, j, r), by simp [extraIndices, hrj, hallow], h, hr, hi, hk⟩
    · rintro ⟨⟨i, j, r⟩, ht, hz, _, ha, hk⟩
      exact ⟨by rw [hz, Finset.card_pair (extra_indices_ne ht)], by simp [ha], hk⟩
  have hn := n.isLt
  have hab : 1827 - 4 * (n.val + 1) + 4 = 1827 - 4 * n.val := by omega
  rw [he, Finset.card_biUnion (extra_fiber_disjoint n),
    Finset.sum_congr rfl (extra_fiber_count n), extra_weight_sum _ _ hab]
  simp [newCount, show 56 + n.val ≠ 55 by omega, show 56 + n.val ≤ 70 by omega,
    show 56 + n.val - 56 = n.val by omega, show 56 + n.val - 55 = n.val + 1 by omega]

private theorem extra_tail_pool_count_aux [Fintype Baseline] (k : ℕ) (hk : 56 ≤ k) (hk' : k ≤ 71) :
    (Finset.univ.filter fun b : Baseline =>
      (zeroSlots b).card = 2 ∧ (activeAxis b).isSome ∧ k ≤ pool b 0).card = newCount k := by
  by_cases h : k ≤ 70
  · let n : Fin 15 := ⟨k - 56, by omega⟩
    have hkn : 56 + n.val = k := by dsimp [n]; omega
    rw [← hkn]
    exact extra_tail_count_rank n
  · have hkn : k = 71 := by omega
    subst k
    have he : (Finset.univ.filter fun b : Baseline =>
        (zeroSlots b).card = 2 ∧ (activeAxis b).isSome ∧ 71 ≤ pool b 0) = ∅ := by
      apply Finset.filter_false_of_mem
      intro b _ hb
      have hp := pool_le_70 b 0
      omega
    rw [he, Finset.card_empty]
    rfl

/-- The cumulative count of extra centers at every tail threshold, including the empty endpoint. -/
theorem extra_tail_pool_count (k : ℕ) (hk : 56 ≤ k) (hk' : k ≤ 71) :
    (Finset.univ.filter fun b : Baseline =>
      (zeroSlots b).card = 2 ∧ (activeAxis b).isSome ∧ k ≤ pool b 0).card = newCount k :=
  extra_tail_pool_count_aux k hk hk'

end SharpOC.Witness1387
