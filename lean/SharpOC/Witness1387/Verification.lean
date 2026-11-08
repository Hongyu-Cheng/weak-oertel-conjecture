import SharpOC.SelectorMeasure
import Mathlib.Analysis.LocallyConvex.Separation

/-! Passing from exact finite fibers and a cap budget to a uniform strict bound. -/

noncomputable section

namespace SharpOC.Witness1387

open Set MeasureTheory
open scoped BigOperators ENNReal
open SharpOC.Selector (mixedIntegerMass mixedIntegerMass_body_toReal
  mixedIntegerMass_closedCut_toReal)

variable {ι α : Type*} [Fintype ι] [Fintype α] {d : ℕ}
  {C : Set ((ι → ℝ) × (Fin d → ℝ))}
  {z : α → ι → ℤ} {S : α → Set (Fin d → ℝ)}

/-- An exact integer-fiber census reduces the normalized all-point bound to
the cap sums on those fibers. Outside points use strict separation. -/
theorem strict_depth_from_exact_fibers
    (hcompact : IsCompact C) (hconvex : Convex ℝ C) (hnonempty : C.Nonempty)
    (hz : Function.Injective z)
    (hcensus : ∀ w x, ((fun j => (w j : ℝ)), x) ∈ C → w ∈ range z)
    (hfiber : ∀ i, {x | ((fun j => (z i j : ℝ)), x) ∈ C} = S i)
    (hS : ∀ i, IsCompact (S i))
    {H R : ℝ} (hH : 0 ≤ H)
    (hmass : 0 < ∑ i, (volume (S i)).toReal)
    (hstrict : H < R * ∑ i, (volume (S i)).toReal)
    (hcuts : ∀ i x, x ∈ S i →
      ∃ F : ((ι → ℝ) × (Fin d → ℝ)) →L[ℝ] ℝ, ∃ t : ℝ,
        F ≠ 0 ∧ t ≤ F ((fun j => (z i j : ℝ)), x) ∧
        (∑ a, (volume (S a ∩ {y | t ≤ F ((fun j => (z a j : ℝ)), y)})).toReal) ≤ H)
    (w : ι → ℤ) (x : Fin d → ℝ) :
    ∃ F : ((ι → ℝ) × (Fin d → ℝ)) →L[ℝ] ℝ, ∃ t : ℝ,
      F ≠ 0 ∧ t ≤ F ((fun j => (w j : ℝ)), x) ∧
      (mixedIntegerMass (C ∩ {p | t ≤ F p})).toReal /
        (mixedIntegerMass C).toReal < R := by
  have htotal := mixedIntegerMass_body_toReal z hz hcensus S hfiber hS
  by_cases hx : ((fun j => (w j : ℝ)), x) ∈ C
  · obtain ⟨i, rfl⟩ := hcensus w x hx
    have hx' : x ∈ S i := by rw [← hfiber i]; exact hx
    obtain ⟨F, t, hF, ht, hcap⟩ := hcuts i x hx'
    refine ⟨F, t, hF, ht, ?_⟩
    rw [mixedIntegerMass_closedCut_toReal z hz hcensus S hfiber hS F t, htotal]
    exact (div_lt_iff₀ hmass).2 (hcap.trans_lt hstrict)
  · obtain ⟨F, t, hbelow, habove⟩ :=
      geometric_hahn_banach_closed_point hconvex hcompact.isClosed hx
    have hF : F ≠ 0 := by
      intro heq
      obtain ⟨p, hp⟩ := hnonempty
      have h := hbelow p hp
      subst F
      simp only [zero_apply] at h habove
      exact (not_lt_of_ge habove.le) h
    have hempty : C ∩ {p | t ≤ F p} = ∅ :=
      eq_empty_iff_forall_notMem.mpr fun p ⟨hp, ht⟩ => (hbelow p hp).not_ge ht
    refine ⟨F, t, hF, habove.le, ?_⟩
    rw [hempty, htotal]
    have hzero : mixedIntegerMass (∅ : Set ((ι → ℝ) × (Fin d → ℝ))) = 0 := by
      simp [mixedIntegerMass]
    rw [hzero, ENNReal.toReal_zero, zero_div]
    exact pos_of_mul_pos_left (hH.trans_lt hstrict) hmass.le

end SharpOC.Witness1387
