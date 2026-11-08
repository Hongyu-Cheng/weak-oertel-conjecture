import SharpOC.Witness1387.SupportExposure
import SharpOC.Witness1387.GlobalLattice

/-! Strict exposure at a baseline with two inactive zero slots. -/

noncomputable section

namespace SharpOC.Witness1387

open scoped BigOperators

private theorem compatible_pair_light
    {b : Baseline} {i j : Block} (hij : i ≠ j) (hz : zeroSlots b = insert i {j})
    (hnone : activeAxis b = none) (c : {c : Baseline // (selectedFlip c).isSome})
    (hfix : ∀ l, b l ≠ 0 → integerBlock (.inr c) l = localBase (b l)) :
    ∃ r k, selectedFlip c.val = some r ∧ k ≠ r ∧ zeroSlots b = insert r {k} ∧
      zeroSlots c.val = ∅ ∧ c.val k ≠ 0 := by
  classical
  obtain ⟨r, hr⟩ : ∃ r, selectedFlip c.val = some r := by
    cases h : selectedFlip c.val with
    | none => exact (Option.isSome_iff_ne_none.mp c.property h).elim
    | some r => exact ⟨r, rfl⟩
  have hbr : b r = 0 := by
    by_contra h
    have hneg := (integerBlock_guard_neg_iff (.inr c) r).mpr (by simpa using hr)
    rw [hfix r h] at hneg
    exact (not_lt_of_ge (localGuard_base_nonneg _)) hneg
  have hrmem : r = i ∨ r = j := by
    simpa [hz] using (mem_zeroSlots.mpr hbr : r ∈ zeroSlots b)
  obtain ⟨k, hkr, hpair⟩ : ∃ k, k ≠ r ∧ zeroSlots b = insert r {k} := by
    rcases hrmem with rfl | rfl
    · exact ⟨j, hij.symm, hz⟩
    · exact ⟨i, hij, by simpa only [Finset.pair_comm] using hz⟩
  have hbk : b k = 0 := mem_zeroSlots.mp (by simp [hpair])
  have hout (l : Block) (hlr : l ≠ r) (hlk : l ≠ k) : b l ≠ 0 := by
    intro hl
    have hm : l ∈ zeroSlots b := mem_zeroSlots.mpr hl
    simp [hpair, hlr, hlk] at hm
  have hparent (l : Block) (hlr : l ≠ r) (hlk : l ≠ k) : c.val l = b l := by
    apply localBase_injective
    simpa [integerBlock, hr, hlr.symm] using hfix l (hout l hlr hlk)
  have hck : c.val k ≠ 0 := by
    intro hc
    have heq : lightCenter c.val = b := by
      rw [lightCenter_of_selectedFlip hr]
      funext l
      by_cases hlr : l = r
      · subst l
        simp [hbr]
      · rw [Function.update_of_ne hlr]
        by_cases hlk : l = k
        · subst l
          exact hc.trans hbk.symm
        · exact hparent l hlr hlk
    have ha := activeAxis_of_light hr
    simp [heq, hnone] at ha
  have hcz : zeroSlots c.val = ∅ := by
    ext l
    simp only [mem_zeroSlots, Finset.notMem_empty, iff_false]
    by_cases hlr : l = r
    · subst l
      exact selectedFlip_ne_zero hr
    by_cases hlk : l = k
    · subst l
      exact hck
    rw [hparent l hlr hlk]
    exact hout l hlr hlk
  exact ⟨r, k, hr, hkr, hpair, hcz, hck⟩

private theorem localReal_zero_eq : localReal 0 = 0 := by
  funext i
  simp [localReal]

private theorem localReal_neg_eq (z : Fin 11 → ℤ) : localReal (-z) = -localReal z := by
  funext i
  simp [localReal]

/-- The ordinary priority only needs to compare the two guard-one blocks
that survive the guard sum on this face. -/
theorem inactive_pair_exposed_of_priority {b : Baseline} {i j : Block}
    (hij : i ≠ j) (hz : zeroSlots b = insert i {j}) (hnone : activeAxis b = none)
    (priority : Block → (Fin 11 → ℝ) →ₗ[ℝ] ℝ)
    (hpriority : ∀ {c : Baseline} {r k : Block}, zeroSlots c = ∅ →
      selectedFlip c = some r → k ≠ r → eligible (c k) = true →
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
  have hP (s : SupportIndex) :
      P (base s) = ∑ l ∈ Z, priority l (localReal (integerBlock s l)) := by
    simp [P, LinearMap.sum_apply]
  have hG₀ : G (base (.inl b)) = 0 := by
    rw [hG]
    apply neg_eq_zero.mpr
    apply Finset.sum_eq_zero
    intro l hl
    simp [integerBlock, mem_zeroSlots.mp hl]
  have hP₀ : P (base (.inl b)) = 0 := by
    rw [hP]
    apply Finset.sum_eq_zero
    intro l hl
    simp [integerBlock, mem_zeroSlots.mp hl, localReal_zero_eq]
  have hbase_nonneg (c : Baseline) (l : Block) :
      0 ≤ (localGuard (integerBlock (.inl c) l) : ℝ) := by
    have h : 0 ≤ (localGuard (localBase (c l)) : ℝ) := by
      exact_mod_cast localGuard_base_nonneg (c l)
    simpa [integerBlock] using h
  have hG_light (c : {c : Baseline // (selectedFlip c).isSome}) {r k : Block}
      (hr : selectedFlip c.val = some r) (hkr : k ≠ r) (hpair : Z = insert r {k}) :
      G (base (.inr c)) = 1 - (localGuard (localBase (c.val k)) : ℝ) := by
    rw [hG, hpair, Finset.sum_insert (by simp [hkr.symm]), Finset.sum_singleton]
    have hg := (eligible_iff _).mp (selectedFlip_eligible hr)
    simp [integerBlock, hr, hkr.symm, hg]
    ring
  have hgle (s : SupportIndex) (he : f (base s) = f (base (.inl b))) :
      G (base s) ≤ G (base (.inl b)) := by
    rw [hG₀]
    cases s with
    | inl c =>
        rw [hG]
        exact neg_nonpos.mpr (Finset.sum_nonneg fun l _ => hbase_nonneg c l)
    | inr c =>
        obtain ⟨r, k, hr, hkr, hpair, _, hck⟩ :=
          compatible_pair_light hij hz hnone c ((hf (.inr c)).2.mp he)
        have hone : (1 : ℤ) ≤ localGuard (localBase (c.val k)) := by
          have := localGuard_base_pos _ hck
          omega
        rw [hG_light c hr hkr hpair]
        exact sub_nonpos.mpr (by exact_mod_cast hone)
  obtain ⟨R, hR⟩ := combine_face_scores base (.inl b) f G (fun s => (hf s).1) hgle
  have hsurvivor (s : SupportIndex) (he : R (base s) = R (base (.inl b))) :
      s = .inl b ∨ P (base s) < P (base (.inl b)) := by
    obtain ⟨hfe, hge⟩ := (hR s).2.mp he
    cases s with
    | inl c =>
        left
        congr 1
        funext l
        by_cases hb : b l = 0
        · rw [hb]
          have hsum : ∑ l ∈ Z, (localGuard (integerBlock (.inl c) l) : ℝ) = 0 := by
            rwa [hG, hG₀, neg_eq_zero] at hge
          have hl := (Finset.sum_eq_zero_iff_of_nonneg (fun l _ => hbase_nonneg c l)).mp
            hsum l (mem_zeroSlots.mpr hb)
          have hguard : localGuard (localBase (c l)) = 0 := by
            simpa [integerBlock] using hl
          by_contra hc
          exact (ne_of_gt (localGuard_base_pos _ hc)) hguard
        · exact localBase_injective (by simpa [integerBlock] using (hf (.inl c)).2.mp hfe l hb)
    | inr c =>
        right
        obtain ⟨r, k, hr, hkr, hpair, hcz, _⟩ :=
          compatible_pair_light hij hz hnone c ((hf (.inr c)).2.mp hfe)
        have hg : localGuard (localBase (c.val k)) = 1 := by
          rw [hG_light c hr hkr hpair, hG₀] at hge
          exact_mod_cast (show (localGuard (localBase (c.val k)) : ℝ) = 1 by linarith)
        have ho := hpriority hcz hr hkr ((eligible_iff _).mpr hg)
        change Z = insert r {k} at hpair
        rw [hP₀, hP, hpair, Finset.sum_insert (by simp [hkr.symm]), Finset.sum_singleton]
        simp [integerBlock, hr, hkr.symm, localReal_neg_eq]
        linarith
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

private def bitValue (n k : ℕ) : ℕ := if n.testBit k then 1 else 0

def leadingBits (n : ℕ) : ℕ := bitValue n 0 + bitValue n 1

private def remainingBits (n : ℕ) : ℕ :=
  ∑ k : Fin 6, 2 ^ k.val * bitValue n (2 + k.val)

set_option maxRecDepth 10000 in
set_option maxHeartbeats 0 in
private theorem code_arithmetic :
    ∀ n : Fin 256, (leadingBits n.val = 0 ↔ n.val % 4 = 0) ∧
      leadingBits n.val ≤ 2 ∧ remainingBits n.val = n.val / 4 := by
  decide +kernel

private def ordinarySumReal : (Fin 11 → ℝ) →ₗ[ℝ] ℝ :=
  ∑ k : Fin 8, LinearMap.proj (ordIdx k)

private def rowReal (j : Fin 4) : (Fin 11 → ℝ) →ₗ[ℝ] ℝ :=
  Fin.lastCases ordinarySumReal (fun k : Fin 3 => ordinarySumReal - LinearMap.proj (selIdx k)) j

private theorem rowReal_apply (z : Fin 11 → ℤ) (j : Fin 4) :
    rowReal j (localReal z) = (localRow z j : ℝ) := by
  refine Fin.lastCases (motive := fun j => rowReal j (localReal z) = (localRow z j : ℝ))
    ?_ (fun k => ?_) j
  · simp only [rowReal, localRow, Fin.lastCases_last]
    change ordinarySumReal (localReal z) = ((∑ k : Fin 8, z (ordIdx k)) : ℤ)
    simp [ordinarySumReal, localReal, LinearMap.sum_apply]
  · simp only [rowReal, localRow, Fin.lastCases_castSucc]
    change (ordinarySumReal - LinearMap.proj (selIdx k) :
      (Fin 11 → ℝ) →ₗ[ℝ] ℝ) (localReal z) =
      (((∑ l : Fin 8, z (ordIdx l)) - z (selIdx k)) : ℤ)
    simp [ordinarySumReal, localReal, LinearMap.sum_apply]

private def codedBitReal (k : Fin 8) : (Fin 11 → ℝ) →ₗ[ℝ] ℝ :=
  LinearMap.proj (ordIdx k) + ∑ j : Fin 4, (codeCorrection j k : ℝ) • rowReal j

private theorem codedBitReal_apply (a : Slot) (ha : eligible a = true) (k : Fin 8) :
    codedBitReal k (localReal (localBase a)) = (bitValue (code a) k.val : ℝ) := by
  have hsum : (∑ j : Fin 4, (codeCorrection j k : ℝ) * (localRow (localBase a) j : ℝ)) =
      (codeCorrection (owner a) k : ℝ) := by
    simp [eligible_row a ha, mul_ite]
  simp only [codedBitReal, LinearMap.add_apply, LinearMap.proj_apply, LinearMap.sum_apply,
    LinearMap.smul_apply, smul_eq_mul, rowReal_apply]
  rw [hsum]
  have h := (eligible_code_bit a ha k).symm
  change localBase a (ordIdx k) + codeCorrection (owner a) k =
    (if (code a).testBit k.val then (1 : ℤ) else 0) at h
  cases hb : (code a).testBit k.val <;>
    simp [hb, bitValue, localReal] at h ⊢ <;> exact_mod_cast h

private def highScale (i : Block) : ℕ := 2000 * 3 ^ (18 - i.val)

private def ordinaryRank (b : Baseline) (i : Block) : ℕ :=
  highScale i * leadingBits (code (b i)) + tailPriority b i

/-- Linear extension of a score with block-specific high scale and guard offset. -/
def priorityScore (i : Block) (scale offset : ℕ) : (Fin 11 → ℝ) →ₗ[ℝ] ℝ :=
  (scale : ℝ) • (codedBitReal 0 + codedBitReal 1) +
    (19 : ℝ) • (∑ k : Fin 6, (2 : ℝ) ^ k.val • codedBitReal (k.natAdd 2)) +
    ((18 - i.val + offset : ℕ) : ℝ) • localGuardReal

theorem priorityScore_apply (b : Baseline) (i : Block) (scale offset : ℕ)
    (ha : eligible (b i) = true) :
    priorityScore i scale offset (localReal (localBase (b i))) =
      (↑(scale * leadingBits (code (b i)) + tailPriority b i + offset : ℕ) : ℝ) := by
  have hu := (code_arithmetic ⟨code (b i), eligible_code_lt (b i) ha⟩).2.2
  have hu' : (∑ k : Fin 6, (2 : ℝ) ^ k.val * (bitValue (code (b i)) (2 + k.val) : ℝ)) =
      (↑(code (b i) / 4 : ℕ) : ℝ) := by
    exact_mod_cast hu
  have hl : (bitValue (code (b i)) 0 : ℝ) + (bitValue (code (b i)) 1 : ℝ) =
      (leadingBits (code (b i)) : ℝ) := by simp [leadingBits]
  simp only [priorityScore, LinearMap.add_apply, LinearMap.sum_apply, LinearMap.smul_apply,
    smul_eq_mul, codedBitReal_apply _ ha, Fin.val_zero, Fin.val_one, Fin.val_natAdd, localGuardReal_localReal,
    (eligible_iff _).mp ha, Int.cast_one, mul_one]
  rw [hl, hu']
  push_cast [tailPriority]
  ring

/-- On eligible sites the low part of the score is the exact tail rank.
The factor of three separates the high bands. -/
def ordinaryPriority (i : Block) : (Fin 11 → ℝ) →ₗ[ℝ] ℝ :=
  priorityScore i (highScale i) 0

private theorem ordinaryPriority_apply (b : Baseline) (i : Block) (ha : eligible (b i) = true) :
    ordinaryPriority i (localReal (localBase (b i))) = (ordinaryRank b i : ℝ) := by
  simpa [ordinaryPriority, ordinaryRank] using priorityScore_apply b i (highScale i) 0 ha

theorem leadingBits_zero_iff {a : Slot} (ha : eligible a = true) :
    leadingBits (code a) = 0 ↔ high a = false := by
  have h := (code_arithmetic ⟨code a, eligible_code_lt a ha⟩).1
  change leadingBits (code a) = 0 ↔ code a % 4 = 0 at h
  simpa [high, ha] using h

theorem leadingBits_le_two {a : Slot} (ha : eligible a = true) :
    leadingBits (code a) ≤ 2 :=
  (code_arithmetic ⟨code a, eligible_code_lt a ha⟩).2.1

private theorem highScale_min (i : Block) : 2000 ≤ highScale i := by
  have hp : 0 < (3 : ℕ) ^ (18 - i.val) := by positivity
  have hp' : 1 ≤ (3 : ℕ) ^ (18 - i.val) := by omega
  simpa [highScale] using Nat.mul_le_mul_left 2000 hp'

private theorem highScale_order {i j : Block} (h : i < j) : 3 * highScale j ≤ highScale i := by
  have hi := i.isLt
  have hj := j.isLt
  change i.val < j.val at h
  have he : (18 - j.val) + 1 ≤ 18 - i.val := by omega
  calc
    3 * highScale j = 2000 * 3 ^ ((18 - j.val) + 1) := by
      simp [highScale, pow_succ]
      ring
    _ ≤ highScale i := Nat.mul_le_mul_left _ (Nat.pow_le_pow_right (by decide) he)

theorem tailPriority_bound (c : Baseline) (i : Block) (hi : eligible (c i) = true) :
    tailPriority c i < 2000 := by
  have hc := eligible_code_lt (c i) hi
  unfold tailPriority
  omega

theorem tailPriority_ne (c : Baseline) {i j : Block} (hij : i ≠ j) :
    tailPriority c i ≠ tailPriority c j := by
  intro h
  apply hij
  apply Fin.ext
  have hi := i.isLt
  have hj := j.isLt
  unfold tailPriority at h
  omega

private theorem ordinary_rank_order {c : Baseline} {r k : Block} (hcz : zeroSlots c = ∅)
    (hr : selectedFlip c = some r) (hkr : k ≠ r) (hk : eligible (c k) = true) :
    ordinaryRank c k < ordinaryRank c r := by
  have hre := selectedFlip_eligible hr
  by_cases hh : high (c r) = true
  · have hJr : 1 ≤ leadingBits (code (c r)) := by
      by_contra! hn
      have hz : leadingBits (code (c r)) = 0 := by omega
      have hfalse := (leadingBits_zero_iff hre).mp hz
      simp [hh] at hfalse
    have hmulr : highScale r ≤ highScale r * leadingBits (code (c r)) := by
      simpa using Nat.mul_le_mul_left (highScale r) hJr
    have htk := tailPriority_bound c k hk
    by_cases hkh : high (c k) = true
    · have hle := selectedFlip_ordinary_le_high hcz hr (mem_highSlots.mpr hkh)
      have hband := highScale_order (lt_of_le_of_ne hle hkr.symm)
      have hJk := leadingBits_le_two hk
      have hmulk : highScale k * leadingBits (code (c k)) ≤ highScale k * 2 :=
        Nat.mul_le_mul_left _ hJk
      have hmin := highScale_min k
      unfold ordinaryRank
      omega
    · have hJk := (leadingBits_zero_iff hk).mpr (by simpa using hkh)
      have hmin := highScale_min r
      simp only [ordinaryRank, hJk, mul_zero, zero_add]
      omega
  · have hs : (highSlots c).sort = [] := by
      cases hsort : (highSlots c).sort with
      | nil => rfl
      | cons t ts =>
          have htr : t = r := by simpa [selectedFlip, hcz, hsort] using hr
          subst t
          have hm : r ∈ highSlots c := by rw [← Finset.mem_sort (· ≤ ·), hsort]; simp
          exact (hh (mem_highSlots.mp hm)).elim
    have hbest : bestTail c (fun _ => true) = some r := by
      simpa [selectedFlip, hcz, hs] using hr
    have hkh : high (c k) = false := by
      by_contra h
      have hm := mem_highSlots.mpr (show high (c k) = true by simpa using h)
      rw [← Finset.mem_sort (· ≤ ·), hs] at hm
      simp at hm
    have htk : tail (c k) = true := by simp [tail, hk, hkh]
    have hle := (bestTail_spec hbest).2.2 k rfl htk
    have hJr := (leadingBits_zero_iff hre).mpr (by simpa using hh)
    have hJk := (leadingBits_zero_iff hk).mpr hkh
    simpa [ordinaryRank, hJr, hJk] using lt_of_le_of_ne hle (tailPriority_ne c hkr)

theorem ordinaryPriority_order {c : Baseline} {r k : Block} (hcz : zeroSlots c = ∅)
    (hr : selectedFlip c = some r) (hkr : k ≠ r) (hk : eligible (c k) = true) :
    ordinaryPriority k (localReal (localBase (c k))) <
      ordinaryPriority r (localReal (localBase (c r))) := by
  rw [ordinaryPriority_apply c k hk, ordinaryPriority_apply c r (selectedFlip_eligible hr)]
  exact_mod_cast ordinary_rank_order hcz hr hkr hk

theorem inactive_pair_exposed {b : Baseline} {i j : Block}
    (hij : i ≠ j) (hz : zeroSlots b = insert i {j}) (hnone : activeAxis b = none) :
    ∃ L : (Coordinate → ℝ) →ₗ[ℝ] ℝ,
      ∀ s : SupportIndex, s ≠ .inl b → L (base s) < L (base (.inl b)) :=
  inactive_pair_exposed_of_priority hij hz hnone ordinaryPriority
    (fun hcz hr hkr hk => ordinaryPriority_order hcz hr hkr hk)

end SharpOC.Witness1387
