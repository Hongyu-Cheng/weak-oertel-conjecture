import SharpOC.Witness1387.ActiveFibers

/-! Strict exposure for inactive baselines with one zero slot. -/

noncomputable section

namespace SharpOC.Witness1387

open Set

theorem inactive_single_exposed {b : Baseline} {i : Block}
    (hz : zeroSlots b = {i}) (hnone : activeAxis b = none) :
    ∃ L : (Coordinate → ℝ) →ₗ[ℝ] ℝ,
      ∀ s : SupportIndex, s ≠ .inl b → L (base s) < L (base (.inl b)) := by
  classical
  have hb₀ : b i = 0 := mem_zeroSlots.mp (by simp [hz])
  have hbne (k : Block) (hk : k ≠ i) : b k ≠ 0 := by
    intro he
    have hm := mem_zeroSlots.mpr he
    simpa [hz, hk] using hm
  obtain ⟨j, hj, hji⟩ : ∃ j ∈ highSlots b, j < i := by
    by_contra h
    have hall : ∀ j ∈ highSlots b, ¬j < i := fun j hj hji => h ⟨j, hj, hji⟩
    have hi := activeAxis_single_of hz hall
    simp [hnone] at hi
  obtain ⟨ell, hell⟩ := expose_nonzero_blocks b
  have hfix (s : SupportIndex) (he : ell (base s) = ell (base (.inl b)))
      (k : Block) (hk : k ≠ i) : integerBlock s k = localBase (b k) :=
    (hell s).2.mp he k (hbne k hk)
  have hbase (s : SupportIndex) (he : ell (base s) = ell (base (.inl b))) :
      ∃ c, s = .inl c := by
    cases s with
    | inl c => exact ⟨c, rfl⟩
    | inr c =>
        have hs : ∃ k, selectedFlip c.val = some k := by
          cases h : selectedFlip c.val with
          | none => exact (by simpa [h] using c.property : False).elim
          | some k => exact ⟨k, rfl⟩
        obtain ⟨k, hk⟩ := hs
        have hki : k = i := by
          by_contra hne
          have hg := integerBlock_guard_of_flip (s := .inr c) (i := k) hk
          rw [hfix (.inr c) he k hne] at hg
          linarith [localGuard_base_nonneg (b k)]
        subst k
        have hparent (k : Block) (hk' : k ≠ i) : c.val k = b k := by
          apply localBase_injective
          simpa [integerBlock, flip, parent, hk, hk'.symm] using hfix (.inr c) he k hk'
        have hcnz (k : Block) : c.val k ≠ 0 := by
          by_cases he : k = i
          · subst k
            exact selectedFlip_ne_zero hk
          · rw [hparent k he]
            exact hbne k he
        have hcz : zeroSlots c.val = ∅ := by
          ext k
          simp [mem_zeroSlots, hcnz k]
        have hj' : j ∈ highSlots c.val := by
          rw [mem_highSlots, hparent j hji.ne]
          exact mem_highSlots.mp hj
        exact (hji.not_ge (selectedFlip_ordinary_le_high hcz hk hj')).elim
  let g := -guardScore i
  have hg₀ : g (base (.inl b)) = 0 := by
    simp [g, integerBlock, hb₀]
  have hgle (s : SupportIndex) (he : ell (base s) = ell (base (.inl b))) :
      g (base s) ≤ g (base (.inl b)) := by
    obtain ⟨c, rfl⟩ := hbase s he
    rw [hg₀]
    simpa [g, integerBlock] using
      (neg_nonpos.mpr (by exact_mod_cast localGuard_base_nonneg (c i)) :
        -(localGuard (localBase (c i)) : ℝ) ≤ 0)
  obtain ⟨L, hL⟩ := combine_face_scores base (.inl b) ell g (fun s => (hell s).1) hgle
  refine ⟨L, fun s hs => lt_of_le_of_ne (hL s).1 ?_⟩
  intro he
  obtain ⟨he₁, he₂⟩ := (hL s).2.mp he
  obtain ⟨c, rfl⟩ := hbase s he₁
  have hci : c i = 0 := by
    by_contra h
    have hpos := localGuard_base_pos (c i) h
    rw [hg₀] at he₂
    have he₃ : -(localGuard (localBase (c i)) : ℝ) = 0 := by
      simpa [g, integerBlock] using he₂
    exact (ne_of_gt hpos) (by exact_mod_cast (neg_eq_zero.mp he₃))
  apply hs
  congr 1
  funext k
  by_cases hk : k = i
  · subst k
    exact hci.trans hb₀.symm
  · exact localBase_injective (by simpa [integerBlock] using hfix (.inl c) he₁ k hk)

open scoped BigOperators

/-- A light cannot survive the guard minimization when at least four
slots are zero. This exposes every such baseline without priority ties. -/
theorem inactive_many_exposed (b : Baseline) (hb : 4 ≤ (zeroSlots b).card) :
    ∃ L : (Coordinate → ℝ) →ₗ[ℝ] ℝ,
      ∀ s : SupportIndex, s ≠ .inl b → L (base s) < L (base (.inl b)) := by
  classical
  obtain ⟨ell, hell⟩ := expose_nonzero_blocks b
  let Z := zeroSlots b
  let G : (Coordinate → ℝ) →ₗ[ℝ] ℝ := -(∑ j ∈ Z, guardScore j)
  have hG (s : SupportIndex) : G (base s) =
      -(∑ j ∈ Z, (localGuard (integerBlock s j) : ℝ)) := by
    simp [G, LinearMap.sum_apply]
  have hG₀ : G (base (.inl b)) = 0 := by
    rw [hG]
    apply neg_eq_zero.mpr
    apply Finset.sum_eq_zero
    intro j hj
    have hz : b j = 0 := mem_zeroSlots.mp hj
    simp [integerBlock, hz]
  have hlight (c : {c : Baseline // (selectedFlip c).isSome})
      (he : ell (base (.inr c)) = ell (base (.inl b))) :
      G (base (.inr c)) < 0 := by
    obtain ⟨i, hi⟩ : ∃ i, selectedFlip c.val = some i := by
      cases h : selectedFlip c.val with
      | none => exact (by simpa [h] using c.property : False).elim
      | some i => exact ⟨i, rfl⟩
    have hgneg := integerBlock_guard_of_flip (s := .inr c) (i := i) hi
    have hiZ : i ∈ Z := by
      by_contra hn
      have hbi : b i ≠ 0 := fun hz => hn (mem_zeroSlots.mpr hz)
      rw [(hell (.inr c)).2.mp he i hbi] at hgneg
      linarith [localGuard_base_nonneg (b i)]
    let U := Z.erase i
    let W := U \ zeroSlots c.val
    have hU : 3 ≤ U.card := by
      change 3 ≤ (Z.erase i).card
      rw [Finset.card_erase_of_mem hiZ]
      exact Nat.le_sub_one_of_lt hb
    have hW : 2 ≤ W.card := by
      have hs : U.card ≤ W.card + (zeroSlots c.val).card :=
        Finset.card_le_card_sdiff_add_card
      have hc := selectedFlip_zeroSlots_card hi
      omega
    have hnonneg (j : Block) (hj : j ∈ U) :
        0 ≤ (localGuard (integerBlock (.inr c) j) : ℝ) := by
      have hne : j ≠ i := (Finset.mem_erase.mp hj).1
      simpa [integerBlock, flip, parent, hi, hne.symm] using
        (by exact_mod_cast localGuard_base_nonneg (c.val j) :
          0 ≤ (localGuard (localBase (c.val j)) : ℝ))
    have hpos (j : Block) (hj : j ∈ W) :
        (1 : ℝ) ≤ (localGuard (integerBlock (.inr c) j) : ℝ) := by
      have hju : j ∈ U := (Finset.mem_sdiff.mp hj).1
      have hne : j ≠ i := (Finset.mem_erase.mp hju).1
      have hcz : c.val j ≠ 0 := fun h => (Finset.mem_sdiff.mp hj).2 (mem_zeroSlots.mpr h)
      have hp := localGuard_base_pos (c.val j) hcz
      have h : (1 : ℤ) ≤ localGuard (localBase (c.val j)) := by omega
      simpa [integerBlock, flip, parent, hi, hne.symm] using
        (by exact_mod_cast h : (1 : ℝ) ≤ (localGuard (localBase (c.val j)) : ℝ))
    have hsum : (2 : ℝ) ≤ ∑ j ∈ U, (localGuard (integerBlock (.inr c) j) : ℝ) := by
      calc
        (2 : ℝ) ≤ (W.card : ℝ) := by exact_mod_cast hW
        _ = ∑ j ∈ W, (1 : ℝ) := by simp
        _ ≤ ∑ j ∈ W, (localGuard (integerBlock (.inr c) j) : ℝ) :=
          Finset.sum_le_sum hpos
        _ ≤ ∑ j ∈ U, (localGuard (integerBlock (.inr c) j) : ℝ) :=
          Finset.sum_le_sum_of_subset_of_nonneg Finset.sdiff_subset
            (fun j hj _ => hnonneg j hj)
    have hsep := Finset.sum_erase_add Z
      (fun j => (localGuard (integerBlock (.inr c) j) : ℝ)) hiZ
    change (∑ j ∈ U, _) + _ = _ at hsep
    rw [hgneg] at hsep
    rw [hG]
    norm_num at hsep
    linarith
  have hGle (s : SupportIndex) (he : ell (base s) = ell (base (.inl b))) :
      G (base s) ≤ G (base (.inl b)) := by
    rw [hG₀]
    cases s with
    | inl c =>
        rw [hG]
        apply neg_nonpos.mpr
        apply Finset.sum_nonneg
        intro j _
        simpa [integerBlock] using (by exact_mod_cast localGuard_base_nonneg (c j) :
          0 ≤ (localGuard (localBase (c j)) : ℝ))
    | inr c => exact (hlight c he).le
  obtain ⟨L, hL⟩ := combine_face_scores base (.inl b) ell G (fun s => (hell s).1) hGle
  refine ⟨L, fun s hs => lt_of_le_of_ne (hL s).1 ?_⟩
  intro he
  obtain ⟨he₁, he₂⟩ := (hL s).2.mp he
  rw [hG₀] at he₂
  cases s with
  | inr c => exact (hlight c he₁).ne he₂
  | inl c =>
      apply hs
      congr 1
      funext j
      by_cases hj : b j = 0
      · have hjZ : j ∈ Z := mem_zeroSlots.mpr hj
        rw [hj]
        have hnon (k : Block) :
            0 ≤ (localGuard (integerBlock (.inl c) k) : ℝ) := by
          simpa [integerBlock] using (by exact_mod_cast localGuard_base_nonneg (c k) :
            0 ≤ (localGuard (localBase (c k)) : ℝ))
        have hsum := neg_eq_zero.mp ((hG (.inl c)).symm.trans he₂)
        have hle := Finset.single_le_sum (f := fun k =>
          (localGuard (integerBlock (.inl c) k) : ℝ)) (fun k _ => hnon k) hjZ
        rw [hsum] at hle
        by_contra hc
        have hp : 0 < (localGuard (integerBlock (.inl c) j) : ℝ) := by
          simpa [integerBlock] using (Int.cast_pos.mpr (localGuard_base_pos (c j) hc) :
            0 < (localGuard (localBase (c j)) : ℝ))
        exact hp.not_ge hle
      · exact localBase_injective (by simpa [integerBlock] using (hell (.inl c)).2.mp he₁ j hj)

end SharpOC.Witness1387
