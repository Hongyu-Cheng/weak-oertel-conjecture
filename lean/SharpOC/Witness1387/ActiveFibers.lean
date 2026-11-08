import SharpOC.Witness1387.CenterGeometry
import SharpOC.Witness1387.ExposedCaps
import SharpOC.Witness1387.SupportExposure

/-! Exact continuous fibers at all active centers. -/

noncomputable section

namespace SharpOC.Witness1387

open Set

def guardScore (i : Block) : (Coordinate → ℝ) →ₗ[ℝ] ℝ :=
  localGuardReal.comp (restrictBlock i)

@[simp] theorem guardScore_base (i : Block) (s : SupportIndex) :
    guardScore i (base s) = (localGuard (integerBlock s i) : ℝ) := by
  rw [guardScore, LinearMap.comp_apply, restrictBlock_base, localGuardReal_localReal]

theorem active_slot_zero {b : Baseline} {i : Block} (ha : activeAxis b = some i) :
    b i = 0 := by
  apply mem_zeroSlots.mp
  rcases activeAxis_zeroSlots_cases ha with h | ⟨j, _, h⟩ <;> simp [h]

theorem active_fiber_eq {b : Baseline} {i : Block} (ha : activeAxis b = some i) :
    {x | (base (.inl b), x) ∈ body} = source (.inl b) := by
  obtain ⟨ell, hell⟩ := exposed_active_face ha
  have hbi := active_slot_zero ha
  apply active_fiber_eq_of_slice b ell (guardScore i) source_nonempty
      (source_eq_center b (by simp [ha])) (by simp [integerBlock, hbi])
      (fun s => (hell s).1)
  intro s he
  have hout := (hell s).2.mp he
  cases s with
  | inl c =>
      by_cases hc : c = b
      · exact Or.inl (by rw [hc])
      · have hfix : ∀ k, k ≠ i → c k = b k := by
          intro k hk
          apply localBase_injective
          simpa [integerBlock] using hout k hk
        have hci : c i ≠ 0 := by
          intro h
          apply hc
          funext k
          by_cases hk : k = i
          · subst k
            exact h.trans hbi.symm
          · exact hfix k hk
        obtain ⟨hnone, hcard⟩ := active_face_baseline_unit ha hfix hc
        have hg : (1 : ℤ) ≤ localGuard (localBase (c i)) := by
          have hh := localGuard_base_pos (c i) hci
          omega
        refine Or.inr (Or.inl ⟨?_, label c, source_eq_unitSector c (by simp [hnone]) hcard⟩)
        simpa [integerBlock] using (by exact_mod_cast hg :
          (1 : ℝ) ≤ (localGuard (localBase (c i)) : ℝ))
  | inr c =>
      obtain ⟨hflip, hcenter⟩ := active_face_light ha c hout
      refine Or.inr (Or.inr ⟨?_, label c.val, ?_⟩)
      · have hg := integerBlock_guard_of_flip (s := .inr c) (i := i) hflip
        simp [hg]
      · rw [source_eq_light c, hcenter]

end SharpOC.Witness1387
