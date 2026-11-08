import SharpOC.Witness1387.GlobalLattice
import Mathlib.Data.Fintype.BigOperators

/-! Routing and exposed-slice facts for the 1387-dimensional witness. -/

namespace SharpOC.Witness1387

theorem zeroSlots_update_zero (b : Baseline) (i : Block) :
    zeroSlots (Function.update b i 0) = insert i (zeroSlots b) := by
  ext j
  by_cases h : j = i
  · subst j
    simp
  · simp [h]

theorem highSlots_update_zero (b : Baseline) (i : Block) :
    highSlots (Function.update b i 0) = (highSlots b).erase i := by
  ext j
  by_cases h : j = i
  · subst j
    simp
  · simp [h]

private theorem eq_empty_of_sort_nil {S : Finset Block} (h : S.sort = []) : S = ∅ := by
  have h' := congrArg List.toFinset h
  simpa using h'

private theorem eq_singleton_of_sort_singleton {S : Finset Block} {i : Block}
    (h : S.sort = [i]) : S = {i} := by
  have h' := congrArg List.toFinset h
  simpa using h'

private theorem sort_head_min {S : Finset Block} {r j : Block} {rs : List Block}
    (h : S.sort = r :: rs) (hj : j ∈ S) : r ≤ j := by
  have hm : j ∈ r :: rs := by
    rw [← h]
    exact (Finset.mem_sort (· ≤ ·)).mpr hj
  rcases List.mem_cons.mp hm with h' | h'
  · simp [h']
  · have hs := S.pairwise_sort (· ≤ ·)
    rw [h] at hs
    exact (List.pairwise_cons.mp hs).1 j h'

private theorem sort_pair_of_lt {i j : Block} (h : i < j) :
    (insert i ({j} : Finset Block)).sort = [i, j] := by
  rw [Finset.sort_insert (· ≤ ·)]
  · simp
  · simpa using h.le
  · simpa using h.ne

private theorem sort_triple_of_lt {i j k : Block} (h : i < j) (h' : j < k) :
    (insert i (insert j ({k} : Finset Block))).sort = [i, j, k] := by
  rw [Finset.sort_insert (· ≤ ·)]
  · rw [sort_pair_of_lt h']
  · intro l hl
    simp only [Finset.mem_insert, Finset.mem_singleton] at hl
    rcases hl with rfl | rfl
    · exact h.le
    · exact (h.trans h').le
  · simp [h.ne, (h.trans h').ne]

theorem activeAxis_single_of {b : Baseline} {i : Block} (hz : zeroSlots b = {i})
    (hn : ∀ j ∈ highSlots b, ¬j < i) : activeAxis b = some i := by
  unfold activeAxis
  rw [hz, Finset.sort_singleton]
  cases hh : (highSlots b).sort with
  | nil => rfl
  | cons r rs =>
    have hm : r ∈ highSlots b := by
      rw [← Finset.mem_sort (· ≤ ·), hh]
      simp
    simp [hn r hm]

theorem activeAxis_pair_of_arrow {b : Baseline} {i j : Block} (hij : i ≠ j)
    (hz : zeroSlots b = insert i {j})
    (ha : highArrow j (insert i (highSlots b)) = some i) : activeAxis b = some i := by
  by_cases h : i < j
  · simp [activeAxis, hz, sort_pair_of_lt h, ha]
  · have hj : j < i := lt_of_le_of_ne (le_of_not_gt h) (Ne.symm hij)
    have hz' : zeroSlots b = insert j {i} := by
      simpa only [Finset.pair_comm] using hz
    have hr := highArrow_no_reverse hij ha
    simp [activeAxis, hz', sort_pair_of_lt hj, hr, ha]

private theorem highArrow_lone_high {i j r : Block} (hrj : r < j)
    (hi : i < r ∨ j < i) : highArrow j (insert i ({r} : Finset Block)) = some i := by
  unfold highArrow
  rcases hi with hi | hi
  · have hset : insert j (insert i ({r} : Finset Block)) = insert i (insert r {j}) := by
      ext k
      simp only [Finset.mem_insert, Finset.mem_singleton]
      tauto
    rw [hset, sort_triple_of_lt hi hrj]
    simp [(hi.trans hrj).ne.symm, hrj.ne.symm]
  · have hset : insert j (insert i ({r} : Finset Block)) = insert r (insert j {i}) := by
      ext k
      simp only [Finset.mem_insert, Finset.mem_singleton]
      tauto
    rw [hset, sort_triple_of_lt hrj hi]
    simp [hrj.ne.symm]

/-- On an all-nonzero tuple, the selected block is no later than any high block. -/
theorem selectedFlip_ordinary_le_high {b : Baseline} {i j : Block}
    (hz : zeroSlots b = ∅) (h : selectedFlip b = some i) (hj : j ∈ highSlots b) :
    i ≤ j := by
  unfold selectedFlip at h
  rw [hz, Finset.sort_empty] at h
  cases hh : (highSlots b).sort with
  | nil => simp [eq_empty_of_sort_nil hh] at hj
  | cons r rs =>
    have heq : r = i := by simpa [hh] using h
    rw [← heq]
    exact sort_head_min hh hj

/-- A selected light belongs to the active slice obtained by zeroing its flip. -/
theorem activeAxis_of_light {b : Baseline} {i : Block} (h : selectedFlip b = some i) :
    activeAxis (lightCenter b) = some i := by
  have hne := selectedFlip_ne_zero h
  rw [lightCenter_of_selectedFlip h]
  cases hz : (zeroSlots b).sort with
  | nil =>
    have hz' := eq_empty_of_sort_nil hz
    apply activeAxis_single_of (by simp [zeroSlots_update_zero, hz'])
    intro j hj hjlt
    rw [highSlots_update_zero] at hj
    exact (not_le_of_gt hjlt) (selectedFlip_ordinary_le_high hz' h (Finset.mem_erase.mp hj).2)
  | cons j js =>
    cases js with
    | nil =>
      have hz' := eq_singleton_of_sort_singleton hz
      have hij : i ≠ j := by
        intro he
        have hm : j ∈ zeroSlots b := by simp [hz']
        exact hne (he ▸ mem_zeroSlots.mp hm)
      apply activeAxis_pair_of_arrow hij (by rw [zeroSlots_update_zero, hz'])
      rw [highSlots_update_zero]
      have hs : selectedFlip b = some i := h
      unfold selectedFlip at hs
      rw [hz] at hs
      cases hh : (highSlots b).sort with
      | nil =>
        have hh' := eq_empty_of_sort_nil hh
        simp [highArrow, hh'] at hs
      | cons r rs =>
        cases rs with
        | nil =>
          have hh' := eq_singleton_of_sort_singleton hh
          by_cases hrj : r < j
          · have ht : bestTail b (fun k => decide (k < r ∨ j < k)) = some i := by
              simpa [hh, hrj] using hs
            have hi : i < r ∨ j < i := by simpa using (bestTail_spec ht).1
            have ht' := (bestTail_spec ht).2.1
            have hni : i ∉ highSlots b := by
              simp only [tail, Bool.and_eq_true] at ht'
              simpa using ht'.2
            rw [Finset.erase_eq_of_notMem hni, hh']
            exact highArrow_lone_high hrj hi
          · simp [hh, hrj] at hs
        | cons r' rs =>
          have ha : highArrow j (highSlots b) = some i := by simpa [hh] using hs
          rwa [Finset.insert_erase (highArrow_mem ha)]
    | cons j' js =>
      unfold selectedFlip at h
      simp [hz] at h

/-- The selected light contributes to the pool of its own local row. -/
theorem mem_own_poolSites {b : Baseline} {i : Block} (h : selectedFlip b = some i) :
    b i ∈ poolSites (lightCenter b) i (owner (b i)) := by
  rw [mem_poolSites, lightCenter_of_selectedFlip h, Function.update_idem, Function.update_eq_self]
  exact ⟨rfl, h⟩


theorem activeAxis_pair_arrow {b : Baseline} {i j : Block} (hij : i ≠ j)
    (hz : zeroSlots b = insert i {j}) (ha : activeAxis b = some i) :
    highArrow j (insert i (highSlots b)) = some i := by
  by_cases h : i < j
  · unfold activeAxis at ha
    rw [hz, sort_pair_of_lt h] at ha
    change (if highArrow j (insert i (highSlots b)) = some i then some i
      else if highArrow i (insert j (highSlots b)) = some j then some j else none) = some i at ha
    split at ha
    · assumption
    · split at ha <;> simp [hij.symm] at ha
  · have hj : j < i := lt_of_le_of_ne (le_of_not_gt h) (Ne.symm hij)
    have hz' : zeroSlots b = insert j {i} := by
      simpa only [Finset.pair_comm] using hz
    unfold activeAxis at ha
    rw [hz', sort_pair_of_lt hj] at ha
    change (if highArrow i (insert j (highSlots b)) = some j then some j
      else if highArrow j (insert i (highSlots b)) = some i then some i else none) = some i at ha
    split at ha
    · simp [hij.symm] at ha
    · split at ha
      · assumption
      · simp at ha

/-- An arrow toward a donor has an earlier high outsider at the sentinel. -/
theorem highArrow_fixed_blocker {i j : Block} {R : Finset Block}
    (h : highArrow j (insert i R) = some i) : ∃ k ∈ R, k < j := by
  unfold highArrow at h
  cases hs : (insert j (insert i R)).sort with
  | nil => simp [hs] at h
  | cons a l =>
    cases l with
    | nil => simp [hs] at h
    | cons b l =>
      cases l with
      | nil => simp [hs] at h
      | cons c l =>
        have hp := (insert j (insert i R)).sortedLT_sort.pairwise
        rw [hs] at hp
        have ha := (List.pairwise_cons.mp hp).1
        have hb := (List.pairwise_cons.mp (List.pairwise_cons.mp hp).2).1
        have hab : a < b := ha b (by simp)
        have hac : a < c := ha c (by simp)
        have hmem (x : Block) (hx : x ∈ a :: b :: c :: l) (hxj : x ≠ j) (hxi : x ≠ i) :
            x ∈ R := by
          have hxt : x ∈ insert j (insert i R) := by
            rw [← Finset.mem_sort (· ≤ ·), hs]
            exact hx
          exact (Finset.mem_insert.mp ((Finset.mem_insert.mp hxt).resolve_left hxj)).resolve_left hxi
        have hj : j ∈ a :: b :: c :: l := by
          rw [← hs, Finset.mem_sort]
          simp
        rw [hs] at h
        change (if j = a then none else if j = b then some c else some a) = some i at h
        by_cases hja : j = a
        · simp [hja] at h
        · by_cases hjb : j = b
          · rw [ite_eq_right hja, ite_eq_left hjb] at h
            have hci := Option.some.inj h
            subst j
            subst i
            exact ⟨a, hmem a (by simp) hab.ne hac.ne, hab⟩
          · rw [ite_eq_right hja, ite_eq_right hjb] at h
            have hai := Option.some.inj h
            have hjtail : j ∈ c :: l := (List.mem_cons.mp ((List.mem_cons.mp hj).resolve_left hja)).resolve_left hjb
            have hbj := hb j hjtail
            subst i
            exact ⟨b, hmem b (by simp) hbj.ne hab.ne.symm, hbj⟩

/-- The sentinel of an active two-zero slice cannot be flipped by a
compatible light. The parent of the light is compatible when it agrees
with the center outside its two zero blocks. -/
theorem activeAxis_pair_no_sentinel_flip {b c : Baseline} {i j : Block} (hij : i ≠ j)
    (hz : zeroSlots b = insert i {j}) (ha : activeAxis b = some i)
    (hc : ∀ k, k ≠ i → k ≠ j → c k = b k) : selectedFlip c ≠ some j := by
  intro hflip
  have hnj := selectedFlip_ne_zero hflip
  have hbi : b i = 0 := mem_zeroSlots.mp (by simp [hz])
  have hbj : b j = 0 := mem_zeroSlots.mp (by simp [hz])
  by_cases hci : c i = 0
  · have he : lightCenter c = b := by
      rw [lightCenter_of_selectedFlip hflip]
      funext k
      by_cases hkj : k = j
      · subst k
        simp [hbj]
      · by_cases hki : k = i
        · subst k
          simp [hkj, hci, hbi]
        · simpa [hkj] using hc k hki hkj
    have haxis := activeAxis_of_light hflip
    rw [he, ha] at haxis
    exact hij (Option.some.inj haxis)
  · have hcz : zeroSlots c = ∅ := by
      ext k
      simp only [mem_zeroSlots, Finset.notMem_empty, iff_false]
      intro hck
      have hki : k ≠ i := fun h => hci (h ▸ hck)
      have hkj : k ≠ j := fun h => hnj (h ▸ hck)
      have hbk : k ∈ zeroSlots b := mem_zeroSlots.mpr ((hc k hki hkj).symm.trans hck)
      simp [hz, hki, hkj] at hbk
    obtain ⟨r, hr, hrj⟩ := highArrow_fixed_blocker (activeAxis_pair_arrow hij hz ha)
    have hbr := mem_highSlots.mp hr
    have hri : r ≠ i := by
      intro he
      simp [he, hbi] at hbr
    have hrj' : r ≠ j := hrj.ne
    have hcr : r ∈ highSlots c := mem_highSlots.mpr (by simpa only [hc r hri hrj'] using hbr)
    exact (not_le_of_gt hrj) (selectedFlip_ordinary_le_high hcz hflip hcr)


theorem activeAxis_zeroSlots_cases {b : Baseline} {i : Block} (h : activeAxis b = some i) :
    zeroSlots b = {i} ∨ ∃ j, i ≠ j ∧ zeroSlots b = insert i {j} := by
  unfold activeAxis at h
  cases hz : (zeroSlots b).sort with
  | nil => simp [hz] at h
  | cons j l =>
    cases l with
    | nil =>
      have he := eq_singleton_of_sort_singleton hz
      rw [hz] at h
      cases hh : (highSlots b).sort with
      | nil =>
        have hji : j = i := by simpa [hh] using h
        exact Or.inl (hji ▸ he)
      | cons r rs =>
        by_cases hr : r < j
        · simp [hh, hr] at h
        · have hji : j = i := by simpa [hh, hr] using h
          exact Or.inl (hji ▸ he)
    | cons k l =>
      cases l with
      | nil =>
        have he : zeroSlots b = insert j {k} := by
          have he' := congrArg List.toFinset hz
          simpa using he'
        have hjk : j ≠ k := by
          have hn := (zeroSlots b).sort_nodup (· ≤ ·)
          rw [hz] at hn
          simpa using hn
        rw [hz] at h
        change (if highArrow k (insert j (highSlots b)) = some j then some j
          else if highArrow j (insert k (highSlots b)) = some k then some k else none) = some i at h
        split at h
        · have hji := Option.some.inj h
          subst j
          exact Or.inr ⟨k, hjk, he⟩
        · split at h
          · have hki := Option.some.inj h
            subst k
            exact Or.inr ⟨j, hjk.symm, by simpa only [Finset.pair_comm] using he⟩
          · simp at h
      | cons k' l => simp [hz] at h


@[simp] private theorem integerBlock_baseline (b : Baseline) (i : Block) :
    integerBlock (.inl b) i = localBase (b i) := by simp [integerBlock]

private theorem eligible_of_support_flip {s : SupportIndex} {i : Block}
    (h : flip s = some i) : eligible (parent s i) = true := by
  cases s with
  | inl b => simp at h
  | inr b => exact selectedFlip_eligible h

theorem integerBlock_guard_of_flip {s : SupportIndex} {i : Block}
    (h : flip s = some i) : localGuard (integerBlock s i) = -1 := by
  have hg := (eligible_iff _).mp (eligible_of_support_flip h)
  simp [integerBlock, h, hg]

private theorem parent_eq_of_block_eq {s : SupportIndex} {b : Baseline} {i : Block}
    (h : integerBlock s i = localBase (b i)) : parent s i = b i := by
  have hn : flip s ≠ some i := by
    intro hf
    have hg := integerBlock_guard_of_flip hf
    rw [h] at hg
    linarith [localGuard_base_nonneg (b i)]
  apply localBase_injective
  simpa [integerBlock, hn] using h

/-- The active slice is precisely the support face with all blocks other
than its varying axis fixed to the baseline values. -/
theorem exposed_active_face {b : Baseline} {i : Block} (ha : activeAxis b = some i) :
    ∃ ℓ : (Coordinate → ℝ) →ₗ[ℝ] ℝ,
      ∀ s : SupportIndex, ℓ (base s) ≤ ℓ (base (.inl b)) ∧
        (ℓ (base s) = ℓ (base (.inl b)) ↔
          ∀ k, k ≠ i → integerBlock s k = localBase (b k)) := by
  classical
  obtain ⟨ℓ, hℓ⟩ := expose_nonzero_blocks b
  rcases activeAxis_zeroSlots_cases ha with hz | ⟨j, hij, hz⟩
  · have he (k : Block) : b k ≠ 0 ↔ k ≠ i := by
      simpa only [hz, Finset.mem_singleton] using
        (mem_zeroSlots (b := b) (i := k)).not.symm
    exact ⟨ℓ, fun s => by simpa only [he] using hℓ s⟩
  · have he (k : Block) : b k ≠ 0 ↔ k ≠ i ∧ k ≠ j := by
      simpa only [hz, Finset.mem_insert, Finset.mem_singleton, not_or] using
        (mem_zeroSlots (b := b) (i := k)).not.symm
    have hj : b j = 0 := mem_zeroSlots.mp (by simp [hz])
    let g : (Coordinate → ℝ) →ₗ[ℝ] ℝ := -localGuardReal.comp (restrictBlock j)
    have hg_apply (s : SupportIndex) : g (base s) = -(localGuard (integerBlock s j) : ℝ) := by
      simp [g]
    have hg₀ : g (base (.inl b)) = 0 := by simp [hg_apply, hj]
    have hno (s : SupportIndex) (hf : ℓ (base s) = ℓ (base (.inl b))) :
        flip s ≠ some j := by
      have hfixed := (hℓ s).2.mp hf
      cases s with
      | inl b' => simp
      | inr c =>
        apply activeAxis_pair_no_sentinel_flip hij hz ha
        intro k hki hkj
        exact parent_eq_of_block_eq (hfixed k ((he k).mpr ⟨hki, hkj⟩))
    have hscore (s : SupportIndex) (hf : ℓ (base s) = ℓ (base (.inl b))) :
        g (base s) ≤ g (base (.inl b)) := by
      have hn := hno s hf
      rw [hg_apply, hg₀, integerBlock, ite_eq_right hn]
      have hpos : 0 ≤ (localGuard (localBase (parent s j)) : ℝ) := by
        exact_mod_cast localGuard_base_nonneg (parent s j)
      linarith
    obtain ⟨L, hL⟩ := combine_face_scores base (.inl b) ℓ g (fun s => (hℓ s).1) hscore
    refine ⟨L, fun s => ⟨(hL s).1, ?_⟩⟩
    rw [(hL s).2]
    constructor
    · rintro ⟨hf, hg⟩ k hk
      by_cases hkj : k = j
      · subst k
        have hn := hno s hf
        rw [hg_apply, hg₀, integerBlock, ite_eq_right hn] at hg
        have hz' : parent s j = 0 := by
          by_contra hn'
          have hpos : 0 < (localGuard (localBase (parent s j)) : ℝ) :=
            Int.cast_pos.mpr (localGuard_base_pos _ hn')
          linarith
        simp [integerBlock, hn, hz', hj]
      · exact (hℓ s).2.mp hf k ((he k).mpr ⟨hk, hkj⟩)
    · intro h
      have hf := (hℓ s).2.mpr (fun k hk => h k ((he k).mp hk).1)
      refine ⟨hf, ?_⟩
      rw [hg_apply, hg₀, h j hij.symm, hj]
      simp


private theorem activeAxis_zero {b : Baseline} {i : Block} (ha : activeAxis b = some i) :
    b i = 0 := by
  apply mem_zeroSlots.mp
  rcases activeAxis_zeroSlots_cases ha with hz | ⟨j, _, hz⟩ <;> simp [hz]

private theorem activeAxis_single_none_of_high {b : Baseline} {i r : Block}
    (hz : zeroSlots b = {i}) (hr : r ∈ highSlots b) (hri : r < i) :
    activeAxis b = none := by
  unfold activeAxis
  rw [hz, Finset.sort_singleton]
  cases hh : (highSlots b).sort with
  | nil => simp [eq_empty_of_sort_nil hh] at hr
  | cons s ss =>
    have hsi := lt_of_le_of_lt (sort_head_min hh hr) hri
    simp [hsi]

/-- Any other positive baseline in an active slice is an inactive sector. -/
theorem active_face_baseline_unit {b c : Baseline} {i : Block}
    (ha : activeAxis b = some i) (hc : ∀ k, k ≠ i → c k = b k) (hne : c ≠ b) :
    activeAxis c = none ∧ (zeroSlots c).card ≤ 1 := by
  have hbi := activeAxis_zero ha
  have hci : c i ≠ 0 := by
    intro h
    apply hne
    funext k
    by_cases hk : k = i
    · subst k
      exact h.trans hbi.symm
    · exact hc k hk
  have hz : zeroSlots c = (zeroSlots b).erase i := by
    ext k
    by_cases hk : k = i
    · subst k
      simp [hci]
    · simp [hk, hc k hk]
  rcases activeAxis_zeroSlots_cases ha with hb | ⟨j, hij, hb⟩
  · have hz' : zeroSlots c = ∅ := by simp [hz, hb]
    simp [activeAxis, hz']
  · have hz' : zeroSlots c = {j} := by
      rw [hz, hb, Finset.erase_insert]
      simpa using hij
    obtain ⟨r, hr, hrj⟩ := highArrow_fixed_blocker (activeAxis_pair_arrow hij hb ha)
    have hbr := mem_highSlots.mp hr
    have hri : r ≠ i := by
      intro he
      simp [he, hbi] at hbr
    have hcr : r ∈ highSlots c := mem_highSlots.mpr (by simpa only [hc r hri] using hbr)
    exact ⟨activeAxis_single_none_of_high hz' hcr hrj, by simp [hz']⟩

/-- A light in an active slice flips its axis and is centered at that slice. -/
theorem active_face_light {b : Baseline} {i : Block} (ha : activeAxis b = some i)
    (c : {c : Baseline // (selectedFlip c).isSome})
    (hc : ∀ k, k ≠ i → integerBlock (.inr c) k = localBase (b k)) :
    selectedFlip c.val = some i ∧ lightCenter c.val = b := by
  obtain ⟨j, hj⟩ := Option.isSome_iff_exists.mp c.property
  have hji : j = i := by
    by_contra hne
    have hg := integerBlock_guard_of_flip (s := .inr c) hj
    rw [hc j hne] at hg
    linarith [localGuard_base_nonneg (b j)]
  subst j
  refine ⟨hj, ?_⟩
  rw [lightCenter_of_selectedFlip hj]
  funext k
  by_cases hk : k = i
  · subst k
    simpa using (activeAxis_zero ha).symm
  · simpa [hk] using parent_eq_of_block_eq (hc k hk)


/-- Every high mask on the varying axis is selected at an active center. -/
theorem selectedFlip_update_high {b : Baseline} {i : Block} {s : Slot}
    (ha : activeAxis b = some i) (hs : high s = true) :
    selectedFlip (Function.update b i s) = some i := by
  have hs' : s ≠ 0 := by
    intro h
    simp [h] at hs
  have hzero : zeroSlots (Function.update b i s) = (zeroSlots b).erase i := by
    ext j
    by_cases h : j = i
    · subst j
      simp [hs']
    · simp [h]
  have hhigh : highSlots (Function.update b i s) = insert i (highSlots b) := by
    ext j
    by_cases h : j = i
    · subst j
      simp [hs]
    · simp [h]
  have hnot : i ∉ highSlots b := by simp [activeAxis_zero ha]
  rcases activeAxis_zeroSlots_cases ha with hz | ⟨j, hij, hz⟩
  · have hm (r : Block) (hr : r ∈ highSlots b) : i ≤ r := by
      by_contra! h
      have hn := activeAxis_single_none_of_high hz hr h
      rw [ha] at hn
      simp at hn
    unfold selectedFlip
    rw [hzero, hz]
    simp only [Finset.erase_singleton, Finset.sort_empty, hhigh]
    rw [Finset.sort_insert (· ≤ ·) hm hnot]
  · have hArrow := activeAxis_pair_arrow hij hz ha
    obtain ⟨r, hr, _⟩ := highArrow_fixed_blocker hArrow
    have hcard : 2 ≤ (highSlots (Function.update b i s)).card := by
      rw [hhigh, Finset.card_insert_of_notMem hnot]
      exact Nat.succ_le_succ (Finset.card_pos.mpr ⟨r, hr⟩)
    have hzs : zeroSlots (Function.update b i s) = {j} := by
      rw [hzero, hz, Finset.erase_insert (by simpa using hij)]
    unfold selectedFlip
    rw [hzs, Finset.sort_singleton]
    rw [← Finset.length_sort (· ≤ ·)] at hcard
    cases hh : (highSlots (Function.update b i s)).sort with
    | nil => simp [hh] at hcard
    | cons r l =>
      cases l with
      | nil => simp [hh] at hcard
      | cons r' l => simpa [hhigh] using hArrow

theorem pool_le_70 (b : Baseline) (row : Fin 4) : pool b row ≤ 70 := by
  cases ha : activeAxis b with
  | none => simp [pool, ha]
  | some i =>
    rw [pool, ha, ← eligible_owner_count row]
    apply Finset.card_le_card
    intro s hs
    obtain ⟨ho, hf⟩ := mem_poolSites.mp hs
    have he := selectedFlip_eligible hf
    simp only [Finset.mem_filter, Finset.mem_univ, true_and]
    exact ⟨by simpa using he, ho⟩

theorem pool_ge_55_of_active {b : Baseline} {i : Block}
    (ha : activeAxis b = some i) (row : Fin 4) : 55 ≤ pool b row := by
  rw [pool, ha, ← high_owner_count row]
  apply Finset.card_le_card
  intro s hs
  simp only [Finset.mem_filter, Finset.mem_univ, true_and] at hs
  exact mem_poolSites.mpr ⟨hs.2, selectedFlip_update_high ha hs.1⟩

private theorem selectedFlip_congr {b c : Baseline}
    (hz : zeroSlots b = zeroSlots c) (hh : highSlots b = highSlots c)
    (ht : ∀ i, tail (b i) = tail (c i)) (hp : ∀ i, tailPriority b i = tailPriority c i) :
    selectedFlip b = selectedFlip c := by
  have he (allowed : Block → Bool) : bestTail b allowed = bestTail c allowed := by
    unfold bestTail
    simp_rw [ht, hp]
  unfold selectedFlip
  rw [hz, hh]
  split
  · split <;> simp [he]
  · split <;> simp [he]
  · rfl

theorem selectedFlip_update_eq_of_code {b : Baseline} {i : Block} {s t : Slot}
    (hs : eligible s = true) (ht : eligible t = true) (hc : code s = code t) :
    selectedFlip (Function.update b i s) = selectedFlip (Function.update b i t) := by
  have hs' : s ≠ 0 := by
    intro h
    simp [h] at hs
  have ht' : t ≠ 0 := by
    intro h
    simp [h] at ht
  have he (j : Block) : eligible (Function.update b i s j) = eligible (Function.update b i t j) := by
    by_cases h : j = i
    · subst j
      simp [hs, ht]
    · simp [h]
  have hcode (j : Block) : code (Function.update b i s j) = code (Function.update b i t j) := by
    by_cases h : j = i
    · subst j
      simp [hc]
    · simp [h]
  have hhigh (j : Block) : high (Function.update b i s j) = high (Function.update b i t j) := by
    simp only [high, he j, hcode j]
  apply selectedFlip_congr
  · ext j
    by_cases h : j = i
    · subst j
      simp [hs', ht']
    · simp [h]
  · ext j
    simp only [mem_highSlots, hhigh j]
  · intro j
    simp only [tail, he j, hhigh j]
  · intro j
    simp only [tailPriority, hcode j]

private def validCodes : Finset ℕ :=
  (Finset.range 256).filter fun k =>
    (Finset.univ.filter fun i : Fin 8 => k.testBit i.val = true).card = 4

set_option maxRecDepth 10000 in
private theorem validCodes_card : validCodes.card = 70 := by decide

private theorem code_mem_validCodes {s : Slot} (hs : eligible s = true) :
    code s ∈ validCodes := by
  simp only [validCodes, Finset.mem_filter, Finset.mem_range]
  refine ⟨eligible_code_lt s hs, ?_⟩
  have he : (Finset.univ.filter fun i : Fin 8 => (code s).testBit i.val = true) =
      (Finset.univ.filter fun i : Fin 8 => codeBit s i = true) := by
    ext i
    simp only [Finset.mem_filter, Finset.mem_univ, true_and]
    rfl
  rw [he]
  exact eligible_code_weight s hs

private theorem exists_owner_of_code {s : Slot} (hs : eligible s = true) (row : Fin 4) :
    ∃ t : Slot, eligible t = true ∧ owner t = row ∧ code t = code s := by
  let S := Finset.univ.filter fun t : Slot => eligible t = true ∧ owner t = row
  have hm (t : Slot) : t ∈ S ↔ eligible t = true ∧ owner t = row := by simp [S]
  have hsub : S.image code ⊆ validCodes := by
    intro k hk
    obtain ⟨t, ht, rfl⟩ := Finset.mem_image.mp hk
    exact code_mem_validCodes ((hm t).mp ht).1
  have hinj : Set.InjOn code (S : Set Slot) := by
    intro t ht u hu he
    obtain ⟨hte, hto⟩ := (hm t).mp ht
    obtain ⟨hue, huo⟩ := (hm u).mp hu
    exact eligible_owner_code_injective hte hue (hto.trans huo.symm) he
  have hcard : (S.image code).card = 70 := by
    rw [Finset.card_image_of_injOn hinj]
    exact eligible_owner_count row
  have hS := Finset.eq_of_subset_of_card_le hsub (by rw [validCodes_card, hcard])
  have hk : code s ∈ S.image code := hS ▸ code_mem_validCodes hs
  obtain ⟨t, ht, hcode⟩ := Finset.mem_image.mp hk
  exact ⟨t, (hm t).mp ht |>.1, (hm t).mp ht |>.2, hcode⟩

/-- The pool in each owner row has the same coded masks and the same size. -/
theorem pool_eq_of_rows (b : Baseline) (row row' : Fin 4) : pool b row = pool b row' := by
  cases ha : activeAxis b with
  | none => simp [pool, ha]
  | some i =>
    rw [pool, pool, ha]
    have he (j : Fin 4) {s : Slot} (hs : s ∈ poolSites b i j) : eligible s = true := by
      exact (by simpa using selectedFlip_eligible (mem_poolSites.mp hs).2)
    have hsub (j j' : Fin 4) : (poolSites b i j).image code ⊆ (poolSites b i j').image code := by
      intro k hk
      obtain ⟨s, hs, rfl⟩ := Finset.mem_image.mp hk
      obtain ⟨t, hte, hto, hcode⟩ := exists_owner_of_code (he j hs) j'
      have hflip := (mem_poolSites.mp hs).2
      rw [selectedFlip_update_eq_of_code (he j hs) hte hcode.symm] at hflip
      exact Finset.mem_image.mpr ⟨t, mem_poolSites.mpr ⟨hto, hflip⟩, hcode⟩
    have hinj (j : Fin 4) : Set.InjOn code (poolSites b i j : Set Slot) := by
      intro s hs t ht hcode
      exact eligible_owner_code_injective (he j hs) (he j ht)
        ((mem_poolSites.mp hs).1.trans (mem_poolSites.mp ht).1.symm) hcode
    have heq := Finset.Subset.antisymm (hsub row row') (hsub row' row)
    simpa only [Finset.card_image_of_injOn (hinj row), Finset.card_image_of_injOn (hinj row')]
      using congrArg Finset.card heq


open scoped BigOperators

private def nonzeroSlots : Finset Slot := Finset.univ.erase 0

private def nonhighNonzeroSlots : Finset Slot :=
  nonzeroSlots.filter fun s => high s = false

private theorem card_nonzeroSlots : nonzeroSlots.card = 2047 := by
  simp [nonzeroSlots, Finset.card_erase_of_mem]

private theorem card_nonhighNonzeroSlots : nonhighNonzeroSlots.card = 1827 := by
  let S : Fin 4 → Finset Slot := fun j => Finset.univ.filter fun s => high s = true ∧ owner s = j
  have hd : ((Finset.univ : Finset (Fin 4)) : Set (Fin 4)).PairwiseDisjoint S := by
    intro i _ j _ hij
    apply Finset.disjoint_left.mpr
    intro s hi hj
    exact hij ((Finset.mem_filter.mp hi).2.2.symm.trans (Finset.mem_filter.mp hj).2.2)
  have hu : Finset.univ.biUnion S = nonzeroSlots.filter (fun s => high s = true) := by
    ext s
    simp only [Finset.mem_biUnion, Finset.mem_univ, true_and, S, Finset.mem_filter,
      nonzeroSlots, Finset.mem_erase, and_true]
    constructor
    · rintro ⟨j, hs, _⟩
      refine ⟨?_, hs⟩
      intro h
      simp [h] at hs
    · rintro ⟨_, hs⟩
      exact ⟨owner s, hs, rfl⟩
  have hc : (nonzeroSlots.filter (fun s => high s = true)).card = 220 := by
    rw [← hu, Finset.card_biUnion hd]
    simp [S, high_owner_count]
  have hdis : Disjoint (nonzeroSlots.filter fun s => high s = true) nonhighNonzeroSlots := by
    apply Finset.disjoint_left.mpr
    intro s hs ht
    have hhigh := (Finset.mem_filter.mp hs).2
    simp [nonhighNonzeroSlots, hhigh] at ht
  have hU : (nonzeroSlots.filter fun s => high s = true) ∪ nonhighNonzeroSlots = nonzeroSlots := by
    ext s
    cases h : high s <;> simp [nonhighNonzeroSlots, h]
  have hpart := Finset.card_union_of_disjoint hdis
  rw [hU, card_nonzeroSlots, hc] at hpart
  omega

/-- Independent choices for the baseline coordinates of an ordinary center. -/
def ordinaryChoices (i j : Block) : Finset Slot :=
  if j = i then {0} else if j < i then nonhighNonzeroSlots else nonzeroSlots

theorem ordinaryChoices_card (i j : Block) :
    (ordinaryChoices i j).card = if j = i then 1 else if j < i then 1827 else 2047 := by
  unfold ordinaryChoices
  split
  · simp
  · split
    · exact card_nonhighNonzeroSlots
    · exact card_nonzeroSlots

theorem ordinary_axis_iff_independent_choices (b : Baseline) (i : Block) :
    (zeroSlots b = {i} ∧ activeAxis b = some i) ↔ ∀ j, b j ∈ ordinaryChoices i j := by
  constructor
  · rintro ⟨hz, ha⟩ j
    by_cases he : j = i
    · subst j
      have hz' : b i = 0 := mem_zeroSlots.mp (by simp [hz])
      simp [ordinaryChoices, hz']
    · have hn : b j ≠ 0 := by
        intro h
        have hm : j ∈ zeroSlots b := mem_zeroSlots.mpr h
        simp [hz, he] at hm
      by_cases hj : j < i
      · have hnh : high (b j) = false := by
          cases hh : high (b j)
          · rfl
          · have hnone := activeAxis_single_none_of_high hz (mem_highSlots.mpr hh) hj
            simp [ha] at hnone
        simp [ordinaryChoices, he, hj, nonhighNonzeroSlots, nonzeroSlots, hn, hnh]
      · simp [ordinaryChoices, he, hj, nonzeroSlots, hn]
  · intro hc
    have hz : zeroSlots b = {i} := by
      ext j
      have h := hc j
      by_cases he : j = i
      · subst j
        simpa [ordinaryChoices] using h
      · by_cases hj : j < i
        · simpa [ordinaryChoices, he, hj, nonhighNonzeroSlots, nonzeroSlots] using
            (show b j ≠ 0 from (by simpa [ordinaryChoices, he, hj, nonhighNonzeroSlots,
              nonzeroSlots] using h : b j ≠ 0 ∧ high (b j) = false).1)
        · simpa [ordinaryChoices, he, hj, nonzeroSlots] using
            (show b j ≠ 0 from by simpa [ordinaryChoices, he, hj, nonzeroSlots] using h)
    refine ⟨hz, activeAxis_single_of hz ?_⟩
    intro j hj hji
    have h := hc j
    have h' : b j ≠ 0 ∧ high (b j) = false := by
      simpa [ordinaryChoices, hji.ne, hji, nonhighNonzeroSlots, nonzeroSlots] using h
    simp [h'.2] at hj

/-- The ordinary centers at one axis are a product of independent slot sets. -/
theorem ordinary_center_count_at_axis (i : Block) :
    (Finset.univ.filter fun b : Baseline => zeroSlots b = {i} ∧ activeAxis b = some i).card =
      ∏ j : Block, if j = i then 1 else if j < i then 1827 else 2047 := by
  classical
  have he : (Finset.univ.filter fun b : Baseline => zeroSlots b = {i} ∧ activeAxis b = some i) =
      Fintype.piFinset (ordinaryChoices i) := by
    ext b
    simpa [Fintype.mem_piFinset] using ordinary_axis_iff_independent_choices b i
  rw [he, Fintype.card_piFinset]
  exact Finset.prod_congr rfl (fun j _ => ordinaryChoices_card i j)

private theorem ordinary_partition_count (U : Finset Baseline) :
    (U.filter fun b => (zeroSlots b).card = 1 ∧ (activeAxis b).isSome).card =
      ∑ i : Block, (U.filter fun b => zeroSlots b = {i} ∧ activeAxis b = some i).card := by
  classical
  let S (i : Block) := U.filter fun b => zeroSlots b = {i} ∧ activeAxis b = some i
  have hd : ((Finset.univ : Finset Block) : Set Block).PairwiseDisjoint S := by
    intro i _ j _ hij
    apply Finset.disjoint_filter.mpr
    intro b _ hi hj
    exact hij (Option.some.inj (hi.2.symm.trans hj.2))
  have he : (U.filter fun b => (zeroSlots b).card = 1 ∧ (activeAxis b).isSome) =
      Finset.univ.biUnion S := by
    ext b
    simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_biUnion, S]
    constructor
    · rintro ⟨hb, hc, ha⟩
      obtain ⟨i, hi⟩ := Option.isSome_iff_exists.mp ha
      rcases activeAxis_zeroSlots_cases hi with h | ⟨j, hij, h⟩
      · exact ⟨i, hb, h, hi⟩
      · simp [h, Finset.card_pair hij] at hc
    · rintro ⟨i, hb, hi, ha⟩
      simp [hb, hi, ha]
  rw [he, Finset.card_biUnion hd]

set_option maxRecDepth 10000 in
/-- The cumulative count at the first ordinary pool threshold, 55. -/
theorem ordinary_center_count :
    (Finset.univ.filter fun b : Baseline => (zeroSlots b).card = 1 ∧ (activeAxis b).isSome).card =
      (2047 ^ 19 - 1827 ^ 19) / 220 := by
  rw [ordinary_partition_count]
  calc
    _ = ∑ i : Block, ∏ j : Block, if j = i then 1 else if j < i then 1827 else 2047 :=
      Finset.sum_congr rfl (fun i _ => ordinary_center_count_at_axis i)
    _ = (2047 ^ 19 - 1827 ^ 19) / 220 := by decide +kernel

end SharpOC.Witness1387
