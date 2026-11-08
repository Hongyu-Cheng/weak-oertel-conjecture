import SharpOC.SelectorMeasure
import SharpOC.Witness1387.Body
import SharpOC.Witness1387.GlobalLattice

/-! Counting measure on the actual integer fibers of the rational body. -/

noncomputable section

namespace SharpOC.Witness1387

open Set MeasureTheory
open scoped ENNReal BigOperators
open SharpOC.Selector (mixedIntegerMass mixedIntegerMass_eq_sum_of_subset)

def integerFiber (w : Coordinate → ℤ) : Set (Fin 1178 → ℝ) :=
  {x | ((fun j => (w j : ℝ)), x) ∈ body}

def mixedVolume : ℝ≥0∞ := mixedIntegerMass body

theorem integerFiber_nonempty_iff (hne : ∀ i, (source i).Nonempty)
    (w : Coordinate → ℤ) :
    (integerFiber w).Nonempty ↔ w ∈ range integerBase := by
  constructor
  · rintro ⟨x, hx⟩
    apply (integer_census w).mp
    rw [← body_projection hne]
    exact ⟨_, hx, rfl⟩
  · rintro ⟨i, rfl⟩
    obtain ⟨x, hx⟩ := hne i
    exact ⟨x, prescribed_source_mem i hx⟩

theorem integerFiber_compact (w : Coordinate → ℤ) : IsCompact (integerFiber w) := by
  let b : Coordinate → ℝ := fun j => w j
  have he : integerFiber w = Prod.snd '' (body ∩ {p | p.1 = b}) := by
    ext x
    constructor
    · intro hx
      exact ⟨(b, x), ⟨hx, rfl⟩, rfl⟩
    · rintro ⟨⟨z, y⟩, ⟨hp, hz⟩, rfl⟩
      change z = b at hz
      subst z
      exact hp
  rw [he]
  exact (body_compact.inter_right (isClosed_eq continuous_fst continuous_const)).image continuous_snd

theorem mixedVolume_eq_fiber_sum (hne : ∀ i, (source i).Nonempty) :
    mixedVolume = ∑ i : SupportIndex, volume (integerFiber (integerBase i)) := by
  apply mixedIntegerMass_eq_sum_of_subset (Subset.rfl : body ⊆ body) integerBase integerBase_injective
  intro w x hx
  exact (integerFiber_nonempty_iff hne w).mp ⟨x, hx⟩

theorem mixedVolume_ne_top (hne : ∀ i, (source i).Nonempty) :
    mixedVolume ≠ ⊤ := by
  rw [mixedVolume_eq_fiber_sum hne]
  exact ENNReal.sum_ne_top.mpr fun i _ => (integerFiber_compact (integerBase i)).measure_ne_top


end SharpOC.Witness1387
