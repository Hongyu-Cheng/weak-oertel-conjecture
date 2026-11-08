import SharpOC.Halfspaces

/-! Mixed-integer volume of a body with an exact finite fiber census. -/

noncomputable section
open Set MeasureTheory
open scoped ENNReal BigOperators

namespace SharpOC.Selector

variable {ι α : Type*} {d : ℕ}

/-- Counting measure on the integer bases times Lebesgue measure on the fibers. -/
def mixedIntegerMass (D : Set ((ι → ℝ) × (Fin d → ℝ))) : ℝ≥0∞ :=
  ∑' w : ι → ℤ, volume {x | ((fun k => (w k : ℝ)), x) ∈ D}

section FiniteMass

variable [Fintype α]
  {C D : Set ((ι → ℝ) × (Fin d → ℝ))} (hD : D ⊆ C)
  (z : α → ι → ℤ) (hz : Function.Injective z)
  (hcensus : ∀ w x, ((fun k => (w k : ℝ)), x) ∈ C → w ∈ range z)

include hD hz hcensus in
/-- The finite census gives the exact mass of every subset of the body. -/
theorem mixedIntegerMass_eq_sum_of_subset :
    mixedIntegerMass D = ∑ a, volume {x | ((fun k => (z a k : ℝ)), x) ∈ D} := by
  apply finite_fiber_sum volume (fun w => {x | ((fun k => (w k : ℝ)), x) ∈ D}) z hz
  intro w hw
  have hempty : {x | ((fun k => (w k : ℝ)), x) ∈ D} = ∅ :=
    eq_empty_iff_forall_notMem.mpr fun x hx => hw (hcensus w x (hD hx))
  rw [hempty, measure_empty]

include hD hz hcensus in
/-- The finite sum remains exact after conversion to real volume. -/
theorem mixedIntegerMass_toReal_of_subset
    (hfin : ∀ a, volume {x | ((fun k => (z a k : ℝ)), x) ∈ C} ≠ ⊤) :
    (mixedIntegerMass D).toReal = ∑ a, (volume {x | ((fun k => (z a k : ℝ)), x) ∈ D}).toReal := by
  rw [mixedIntegerMass_eq_sum_of_subset hD z hz hcensus]
  exact ENNReal.toReal_sum fun a _ => measure_ne_top_of_subset (fun _ hx => hD hx) (hfin a)

variable (B : α → Set (Fin d → ℝ))
  (hexact : ∀ a, {x | ((fun k => (z a k : ℝ)), x) ∈ C} = B a)
  (hB : ∀ a, IsCompact (B a))

include hz hcensus hexact hB in
theorem mixedIntegerMass_body_toReal :
    (mixedIntegerMass C).toReal = ∑ a, (volume (B a)).toReal := by
  rw [mixedIntegerMass_toReal_of_subset (Subset.refl C) z hz hcensus
    (fun a => by rw [hexact a]; exact (hB a).measure_ne_top)]
  simp_rw [hexact]

include hz hcensus hexact hB in
theorem mixedIntegerMass_closedCut_toReal
    (F : ((ι → ℝ) × (Fin d → ℝ)) → ℝ) (t : ℝ) :
    (mixedIntegerMass (C ∩ {p | t ≤ F p})).toReal =
      ∑ a, (volume (B a ∩ {x | t ≤ F ((fun k => (z a k : ℝ)), x)})).toReal := by
  rw [mixedIntegerMass_toReal_of_subset inter_subset_left z hz hcensus
    (fun a => by rw [hexact a]; exact (hB a).measure_ne_top)]
  apply Finset.sum_congr rfl
  intro a _
  change (volume ({x | ((fun k => (z a k : ℝ)), x) ∈ C} ∩
    {x | t ≤ F ((fun k => (z a k : ℝ)), x)})).toReal = _
  rw [hexact a]

end FiniteMass

/-- Each level of a nonzero continuous linear form has zero Lebesgue measure. -/
theorem volume_linear_level_eq_zero
    (f : (Fin d → ℝ) →L[ℝ] ℝ) (hf : f ≠ 0) (t : ℝ) :
    volume {x | f x = t} = 0 := by
  let A : AffineSubspace ℝ (Fin d → ℝ) := ({t} : AffineSubspace ℝ ℝ).comap f.toLinearMap.toAffineMap
  have hA (x : Fin d → ℝ) : x ∈ A ↔ f x = t := by
    simp [A, AffineSubspace.mem_comap]
  have hne : A ≠ ⊤ := by
    intro h
    have heq (x : Fin d → ℝ) : f x = t := (hA x).mp (by simp [h])
    have ht : t = 0 := by simpa using (heq 0).symm
    apply hf
    ext x
    simpa [ht] using heq x
  exact measure_mono_null (fun x hx => (hA x).mpr hx)
    (Measure.addHaar_affineSubspace volume A hne)

/-- Closing the cut of any fiber leaves its volume unchanged. -/
theorem volume_inter_ge_eq_gt (B : Set (Fin d → ℝ))
    (f : (Fin d → ℝ) →L[ℝ] ℝ) (hf : f ≠ 0) (t : ℝ) :
    volume (B ∩ {x | t ≤ f x}) = volume (B ∩ {x | t < f x}) := by
  symm
  refine measure_eq_measure_of_null_sdiff ?_ ?_
  · rintro x ⟨hxB, hxlt⟩
    exact ⟨hxB, show t ≤ f x from le_of_lt hxlt⟩
  · refine measure_mono_null ?_ (volume_linear_level_eq_zero f hf t)
    rintro x ⟨⟨hxB, hxle⟩, hxgt⟩
    change ¬(x ∈ B ∧ t < f x) at hxgt
    have hnot : ¬ t < f x := fun h => hxgt ⟨hxB, h⟩
    exact le_antisymm (le_of_not_gt hnot) hxle

end SharpOC.Selector
