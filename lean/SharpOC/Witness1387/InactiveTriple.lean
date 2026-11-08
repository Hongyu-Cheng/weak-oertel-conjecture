import SharpOC.Witness1387.TriplePriority

/-! Strict exposure at a baseline with three zero slots. -/

noncomputable section

namespace SharpOC.Witness1387

open scoped BigOperators

private theorem compatible_triple_light
    {b : Baseline} (hz : (zeroSlots b).card = 3)
    (c : {c : Baseline // (selectedFlip c).isSome})
    (hfix : ∀ l, b l ≠ 0 → integerBlock (.inr c) l = localBase (b l)) :
    ∃ r k j, selectedFlip c.val = some r ∧ k ≠ r ∧ j ≠ r ∧ j ≠ k ∧
      zeroSlots b = {r, k, j} ∧ c.val k ≠ 0 ∧ (∀ l, b l ≠ 0 → c.val l = b l) := by
  classical
  obtain ⟨r, hr⟩ := Option.isSome_iff_exists.mp c.property
  have hbr : b r = 0 := by
    by_contra h
    have hneg := (integerBlock_guard_neg_iff (.inr c) r).mpr (by simpa using hr)
    rw [hfix r h] at hneg
    exact (not_lt_of_ge (localGuard_base_nonneg _)) hneg
  have hrZ := mem_zeroSlots.mpr hbr
  have hparent (l : Block) (hl : b l ≠ 0) : c.val l = b l := by
    have hrl : r ≠ l := by
      rintro rfl
      exact hl hbr
    exact localBase_injective (by simpa [integerBlock, hr, hrl] using hfix l hl)
  have htwo : ((zeroSlots b).erase r).card = 2 := by
    rw [Finset.card_erase_of_mem hrZ, hz]
  obtain ⟨k, j, hkj, hpair⟩ := Finset.card_eq_two.mp htwo
  have hk : k ∈ (zeroSlots b).erase r := by simp [hpair]
  have hj : j ∈ (zeroSlots b).erase r := by simp [hpair]
  have hkr := (Finset.mem_erase.mp hk).1
  have hjr := (Finset.mem_erase.mp hj).1
  have htriple : zeroSlots b = {r, k, j} := by
    rw [← hpair, Finset.insert_erase hrZ]
  by_cases hck : c.val k = 0
  · have hcj : c.val j ≠ 0 := by
      intro hcj
      have hsub : ({k, j} : Finset Block) ⊆ zeroSlots c.val := by
        simp [Finset.insert_subset_iff, hck, hcj]
      have hcard := Finset.card_le_card hsub
      simp [hkj] at hcard
      have hmax := selectedFlip_zeroSlots_card hr
      omega
    exact ⟨r, j, k, hr, hjr, hkr, hkj,
      by simpa only [Finset.pair_comm k j] using htriple, hcj, hparent⟩
  · exact ⟨r, k, j, hr, hkr, hjr, hkj.symm, htriple, hck, hparent⟩

@[local simp] private theorem localReal_zero_eq : localReal 0 = 0 := by
  funext i
  simp [localReal]

@[local simp] private theorem localReal_neg_eq (z : Fin 11 → ℤ) : localReal (-z) = -localReal z := by
  funext i
  simp [localReal]

/-- Minimizing the total guard leaves only the target and lights with one
sentinel and two eligible sites. The priority separates those lights. -/
theorem inactive_triple_exposed_of_priority {b : Baseline} (hz : (zeroSlots b).card = 3)
    (priority : Block → (Fin 11 → ℝ) →ₗ[ℝ] ℝ)
    (hpriority : ∀ {c : Baseline} {r k j : Block}, zeroSlots b = {r, k, j} →
      k ≠ r → j ≠ r → j ≠ k → (∀ l, b l ≠ 0 → c l = b l) →
      zeroSlots c = {j} → selectedFlip c = some r → eligible (c k) = true →
        priority k (localReal (localBase (c k))) < priority r (localReal (localBase (c r)))) :
    ∃ L : (Coordinate → ℝ) →ₗ[ℝ] ℝ,
      ∀ s : SupportIndex, s ≠ .inl b → L (base s) < L (base (.inl b)) := by
  classical
  obtain ⟨f, hf⟩ := expose_nonzero_blocks b
  let Z := zeroSlots b
  let G : (Coordinate → ℝ) →ₗ[ℝ] ℝ :=
    -(∑ l ∈ Z, localGuardReal.comp (restrictBlock l))
  let P : (Coordinate → ℝ) →ₗ[ℝ] ℝ := ∑ l ∈ Z, (priority l).comp (restrictBlock l)
  have hG (s : SupportIndex) :
      G (base s) = -(∑ l ∈ Z, (localGuard (integerBlock s l) : ℝ)) := by
    simp [G, LinearMap.sum_apply]
  have hG₀ : G (base (.inl b)) = 0 := by
    rw [hG]
    apply neg_eq_zero.mpr
    exact Finset.sum_eq_zero fun l hl => by simp [integerBlock, mem_zeroSlots.mp hl]
  have hP (s : SupportIndex) :
      P (base s) = ∑ l ∈ Z, priority l (localReal (integerBlock s l)) := by
    simp [P, LinearMap.sum_apply]
  have hP₀ : P (base (.inl b)) = 0 := by
    rw [hP]
    exact Finset.sum_eq_zero fun l hl => by simp [integerBlock, mem_zeroSlots.mp hl]
  have hG_light (c : {c : Baseline // (selectedFlip c).isSome}) {r k j : Block}
      (hr : selectedFlip c.val = some r) (hkr : k ≠ r) (hjr : j ≠ r) (hjk : j ≠ k)
      (htriple : Z = {r, k, j}) :
      G (base (.inr c)) =
        1 - (localGuard (localBase (c.val k)) : ℝ) - (localGuard (localBase (c.val j)) : ℝ) := by
    rw [hG, htriple, Finset.sum_insert (by simp [hkr.symm, hjr.symm]),
      Finset.sum_insert (by simp [hjk.symm]), Finset.sum_singleton]
    simp [integerBlock, hr, hkr.symm, hjr.symm, (eligible_iff _).mp (selectedFlip_eligible hr)]
    ring
  have hbase_nonneg (c : Baseline) (l : Block) :
      0 ≤ (localGuard (integerBlock (.inl c) l) : ℝ) := by
    have h : 0 ≤ (localGuard (localBase (c l)) : ℝ) := by
      exact_mod_cast localGuard_base_nonneg (c l)
    simpa [integerBlock] using h
  have hguard_one {a : Slot} (ha : a ≠ 0) : (1 : ℝ) ≤ localGuard (localBase a) := by
    have := localGuard_base_pos a ha
    exact_mod_cast (show (1 : ℤ) ≤ localGuard (localBase a) by omega)
  have hguard (s : SupportIndex) (hfe : f (base s) = f (base (.inl b))) :
      G (base s) ≤ G (base (.inl b)) ∧
        (G (base s) = G (base (.inl b)) →
          s = .inl b ∨ P (base s) < P (base (.inl b))) := by
    rw [hG₀]
    cases s with
    | inl c =>
        rw [hG]
        refine ⟨neg_nonpos.mpr (Finset.sum_nonneg fun l _ => hbase_nonneg c l), ?_⟩
        intro hge
        left
        congr 1
        funext l
        by_cases hb : b l = 0
        · rw [hb]
          have hl := (Finset.sum_eq_zero_iff_of_nonneg (fun l _ => hbase_nonneg c l)).mp
            (neg_eq_zero.mp hge) l (mem_zeroSlots.mpr hb)
          by_contra hc
          have hpos := hguard_one hc
          simp only [integerBlock, flip_inl, parent_inl, reduceCtorEq, ite_false] at hl
          linarith
        · exact localBase_injective (by simpa [integerBlock] using (hf (.inl c)).2.mp hfe l hb)
    | inr c =>
        obtain ⟨r, k, j, hr, hkr, hjr, hjk, htriple, hck, hparent⟩ :=
          compatible_triple_light hz c ((hf (.inr c)).2.mp hfe)
        rw [hG_light c hr hkr hjr hjk htriple]
        have hk := hguard_one hck
        have hj : 0 ≤ (localGuard (localBase (c.val j)) : ℝ) := by
          exact_mod_cast localGuard_base_nonneg (c.val j)
        refine ⟨by linarith, ?_⟩
        intro hge
        right
        have hcj : c.val j = 0 := by
          by_contra hn
          linarith [hguard_one hn]
        have hcz : zeroSlots c.val = {j} := by
          symm
          apply Finset.eq_of_subset_of_card_le
          · simpa using (mem_zeroSlots.mpr hcj : j ∈ zeroSlots c.val)
          · simpa using selectedFlip_zeroSlots_card hr
        have hg : localGuard (localBase (c.val k)) = 1 := by
          simp [hcj] at hge
          exact_mod_cast (show (localGuard (localBase (c.val k)) : ℝ) = 1 by linarith)
        have ho := hpriority htriple hkr hjr hjk hparent hcz hr ((eligible_iff _).mpr hg)
        change Z = {r, k, j} at htriple
        rw [hP₀, hP, htriple, Finset.sum_insert (by simp [hkr.symm, hjr.symm]),
          Finset.sum_insert (by simp [hjk.symm]), Finset.sum_singleton]
        simp [integerBlock, hr, hkr.symm, hjr.symm, hcj]
        linarith
  obtain ⟨R, hR⟩ := combine_face_scores base (.inl b) f G (fun s => (hf s).1)
    (fun s he => (hguard s he).1)
  have hsurvivor (s : SupportIndex) (he : R (base s) = R (base (.inl b))) :
      s = .inl b ∨ P (base s) < P (base (.inl b)) := by
    obtain ⟨hfe, hge⟩ := (hR s).2.mp he
    exact (hguard s hfe).2 hge
  obtain ⟨L, hL⟩ := combine_face_scores base (.inl b) R P (fun s => (hR s).1) (fun s he => by
    rcases hsurvivor s he with rfl | hlt
    · exact le_rfl
    · exact hlt.le)
  refine ⟨L, fun s hs => lt_of_le_of_ne (hL s).1 ?_⟩
  intro he
  obtain ⟨hre, hpe⟩ := (hL s).2.mp he
  rcases hsurvivor s hre with hs' | hlt
  · exact hs hs'
  · exact hlt.ne hpe

theorem inactive_triple_exposed {b : Baseline} (hz : (zeroSlots b).card = 3) :
    ∃ L : (Coordinate → ℝ) →ₗ[ℝ] ℝ,
      ∀ s : SupportIndex, s ≠ .inl b → L (base s) < L (base (.inl b)) := by
  obtain ⟨priority, hpriority⟩ := triple_priority hz
  exact inactive_triple_exposed_of_priority hz priority hpriority

end SharpOC.Witness1387
