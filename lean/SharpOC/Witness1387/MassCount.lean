import SharpOC.Witness1387.ActiveFibers
import SharpOC.Witness1387.ExposedCaps

/-! Counting the lights by their actual active center. -/

noncomputable section

namespace SharpOC.Witness1387

open scoped BigOperators

private abbrev Light := {b : Baseline // (selectedFlip b).isSome}

set_option maxRecDepth 10000 in
private theorem light_center_card [Fintype Light] {b : Baseline} {i : Block}
    (hi : activeAxis b = some i) :
    (Finset.univ.filter fun c : Light => lightCenter c.val = b).card =
      4 * poolSize (poolIndex b) := by
  let S : Finset Light := Finset.univ.filter fun c => lightCenter c.val = b
  let P : Finset Slot := Finset.univ.filter fun s =>
    selectedFlip (Function.update b i s) = some i
  have hfrom (c : Light) (hc : c ∈ S) :
      Function.update b i (c.val i) = c.val ∧ selectedFlip c.val = some i := by
    have hcb : lightCenter c.val = b := (Finset.mem_filter.mp hc).2
    obtain ⟨j, hj⟩ := Option.isSome_iff_exists.mp c.property
    have hij := Option.some.inj (hi.symm.trans (hcb ▸ activeAxis_of_light hj))
    subst j
    refine ⟨?_, hj⟩
    rw [← hcb, lightCenter_of_selectedFlip hj, Function.update_idem, Function.update_eq_self]
  have hcard : S.card = P.card := by
    refine Finset.card_bij (fun c _ => c.val i) ?_ ?_ ?_
    · intro c hc
      obtain ⟨he, hf⟩ := hfrom c hc
      exact Finset.mem_filter.mpr ⟨Finset.mem_univ _, by rwa [he]⟩
    · intro c hc d hd h
      apply Subtype.ext
      exact (hfrom c hc).1.symm.trans (h ▸ (hfrom d hd).1)
    · intro s hs
      have hf := (Finset.mem_filter.mp hs).2
      let c : Light := ⟨Function.update b i s, by simp [hf]⟩
      have hcb : lightCenter c.val = b := by
        change lightCenter (Function.update b i s) = b
        rw [lightCenter_of_selectedFlip hf, Function.update_idem, ← active_slot_zero hi,
          Function.update_eq_self]
      exact ⟨c, Finset.mem_filter.mpr ⟨Finset.mem_univ _, hcb⟩, by simp [c]⟩
  have hrows : P.card = ∑ j : Fin 4, (poolSites b i j).card := by
    calc
      _ = ∑ j : Fin 4, (P.filter fun s => owner s = j).card :=
        Finset.card_eq_sum_card_fiberwise (fun _ _ => Finset.mem_univ _)
      _ = _ := by
        apply Finset.sum_congr rfl
        intro j _
        apply congrArg Finset.card
        ext s
        simp [P, and_comm]
  have hpool : pool b 0 = poolSize (poolIndex b) := by
    have hl := pool_ge_55_of_active hi 0
    have hu := pool_le_70 b 0
    change pool b 0 = 55 + min 15 (pool b 0 - 55)
    omega
  change S.card = _
  rw [hcard, hrows]
  simp [← hpool, ← show ∀ j : Fin 4, pool b j = (poolSites b i j).card from
    fun j => by simp [pool, hi], pool_eq_of_rows b _ 0]

set_option maxRecDepth 10000 in
/-- The contribution of all selected lights can be grouped by their active
center. The count in each group is the sum of the four owner pools. -/
private theorem sum_lightMass_by_center [Fintype Light] [Fintype Baseline] :
    (∑ c : Light, lightMass (poolIndex (lightCenter c.val))) =
      ∑ b : Baseline, if (activeAxis b).isSome then
        4 * (poolSize (poolIndex b) : ℚ) * lightMass (poolIndex b) else 0 := by
  rw [← Finset.sum_fiberwise Finset.univ (fun c : Light => lightCenter c.val)]
  refine Finset.sum_congr rfl fun b _ => ?_
  cases hi : activeAxis b with
  | none =>
      have h : (Finset.univ.filter fun c : Light => lightCenter c.val = b) = ∅ := by
        apply Finset.eq_empty_iff_forall_notMem.mpr
        intro c hc
        have hcb := (Finset.mem_filter.mp hc).2
        obtain ⟨i, hf⟩ := Option.isSome_iff_exists.mp c.property
        have hactive := activeAxis_of_light hf
        rw [hcb, hi] at hactive
        contradiction
      simp [h]
  | some i =>
      rw [Finset.sum_congr rfl (g := fun _ => lightMass (poolIndex b))]
      · simp [Finset.sum_const, light_center_card hi, nsmul_eq_mul]
      · intro c hc
        rw [(Finset.mem_filter.mp hc).2]

set_option maxRecDepth 10000 in
/-- Pair every light's mass with its active center, leaving a sum over
the original baseline tuples. -/
theorem sum_sourceMass_by_center [Fintype Light] [Fintype Baseline] :
    (∑ s : SupportIndex, sourceMass s) =
      ∑ b : Baseline, if (activeAxis b).isSome then
        radius (poolIndex b) ^ 1178 + 4 * (poolSize (poolIndex b) : ℚ) *
          lightMass (poolIndex b)
      else if (zeroSlots b).card ≤ 1 then tau else inactiveMass := by
  rw [Fintype.sum_sum_type]
  change (∑ b : Baseline, sourceMass (.inl b)) +
    (∑ c : Light, lightMass (poolIndex (lightCenter c.val))) = _
  rw [sum_lightMass_by_center, ← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun b _ => ?_
  by_cases h : (activeAxis b).isSome <;> simp [sourceMass, h]

end SharpOC.Witness1387
