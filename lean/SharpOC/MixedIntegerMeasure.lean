import SharpOC.ConcreteBody
import SharpOC.SourceBasis

/-! Exact counting-times-Lebesgue mass of the actual mixed-integer body. -/

noncomputable section
open Set Finset MeasureTheory
open scoped ENNReal

namespace SharpOC.Counterexample

open SharpOC.MiddleSimplex SharpOC.SourceContainment

def mixedIntegerMass (D : Set ((IntegerCoordinate → ℝ) × E)) : ℝ≥0∞ :=
  ∑' z : IntegerCoordinate → ℤ, volume {x | ((fun i => (z i : ℝ)), x) ∈ D}

/-- Finite support is proved from the actual integer-base census, even
for arbitrary subsets of the body. -/
theorem mixedIntegerMass_eq_sum_of_subset_body
    (D : Set ((IntegerCoordinate → ℝ) × E)) (hD : D ⊆ body) :
    mixedIntegerMass D = ∑ a : FiberIndex, volume {x | (base a, x) ∈ D} := by
  classical
  let s : Finset (IntegerCoordinate → ℤ) := Finset.univ.image integerBase
  have hzero : ∀ z ∉ s, volume {x | ((fun i => (z i : ℝ)), x) ∈ D} = 0 := by
    intro z hz
    have hempty : {x | ((fun i => (z i : ℝ)), x) ∈ D} = ∅ := by
      apply Set.eq_empty_iff_forall_notMem.mpr
      intro x hx
      obtain ⟨a, ha⟩ := integer_base_census z x (hD hx)
      apply hz
      exact Finset.mem_image.mpr ⟨a, Finset.mem_univ a, ha⟩
    rw [hempty, measure_empty]
  unfold mixedIntegerMass
  rw [tsum_eq_sum hzero]
  dsimp [s]
  rw [Finset.sum_image (fun a _ b _ hab => integerBase_injective hab)]
  simp only [integerBase_cast]

theorem mixedIntegerMass_body :
    mixedIntegerMass body = ∑ a : FiberIndex, volume (fiber a) := by
  rw [mixedIntegerMass_eq_sum_of_subset_body body (Subset.refl body)]
  simp_rw [fiber_exact]

/-- Exact mass for every ambient cut. The function is allowed to be
arbitrary here; the counterexample uses nonzero continuous linear ones. -/
theorem mixedIntegerMass_body_cut
    (F : ((IntegerCoordinate → ℝ) × E) → ℝ) (t : ℝ) :
    mixedIntegerMass (body ∩ {p | t ≤ F p}) =
      ∑ a : FiberIndex, volume (fiber a ∩ {x | t ≤ F (base a, x)}) := by
  rw [mixedIntegerMass_eq_sum_of_subset_body _ Set.inter_subset_left]
  apply Finset.sum_congr rfl
  intro a ha
  change volume ({x | (base a, x) ∈ body} ∩ {x | t ≤ F (base a, x)}) = _
  rw [fiber_exact]

theorem fiber_volume_ne_top (a : FiberIndex) : volume (fiber a) ≠ ⊤ :=
  (fiber_compact a).measure_ne_top

theorem fiber_cut_volume_ne_top
    (F : ((IntegerCoordinate → ℝ) × E) → ℝ) (t : ℝ) (a : FiberIndex) :
    volume (fiber a ∩ {x | t ≤ F (base a, x)}) ≠ ⊤ :=
  ne_of_lt (lt_of_le_of_lt (measure_mono Set.inter_subset_left)
    (fiber_compact a).measure_lt_top)

theorem mixedIntegerMass_body_ne_top : mixedIntegerMass body ≠ ⊤ := by
  rw [mixedIntegerMass_body]
  exact ENNReal.sum_ne_top.mpr (fun a _ => fiber_volume_ne_top a)

theorem mixedIntegerMass_body_cut_ne_top
    (F : ((IntegerCoordinate → ℝ) × E) → ℝ) (t : ℝ) :
    mixedIntegerMass (body ∩ {p | t ≤ F p}) ≠ ⊤ := by
  rw [mixedIntegerMass_body_cut]
  exact ENNReal.sum_ne_top.mpr (fun a _ => fiber_cut_volume_ne_top F t a)

theorem mixedIntegerMass_body_toReal :
    (mixedIntegerMass body).toReal = ∑ a : FiberIndex, (volume (fiber a)).toReal := by
  rw [mixedIntegerMass_body]
  exact ENNReal.toReal_sum (fun a _ => fiber_volume_ne_top a)

theorem mixedIntegerMass_body_cut_toReal
    (F : ((IntegerCoordinate → ℝ) × E) → ℝ) (t : ℝ) :
    (mixedIntegerMass (body ∩ {p | t ≤ F p})).toReal =
      ∑ a : FiberIndex, (volume (fiber a ∩ {x | t ≤ F (base a, x)})).toReal := by
  rw [mixedIntegerMass_body_cut]
  exact ENNReal.toReal_sum (fun a _ => fiber_cut_volume_ne_top F t a)

theorem mixedIntegerMass_body_pos : 0 < mixedIntegerMass body := by
  rw [mixedIntegerMass_body]
  apply lt_of_lt_of_le B_volume_pos
  calc
    volume B = volume (fiber (.inl ∅)) := by simp
    _ ≤ ∑ a : FiberIndex, volume (fiber a) :=
      Finset.single_le_sum (f := fun a : FiberIndex => volume (fiber a))
        (fun a _ => bot_le) (Finset.mem_univ (Sum.inl (∅ : Finset IntegerCoordinate) : FiberIndex))

theorem mixedIntegerMass_body_toReal_pos : 0 < (mixedIntegerMass body).toReal :=
  ENNReal.toReal_pos (ne_of_gt mixedIntegerMass_body_pos) mixedIntegerMass_body_ne_top

theorem fiber_interior_nonempty (a : FiberIndex) : (interior (fiber a)).Nonempty := by
  cases a with
  | inl S =>
    by_cases hS : S = ∅
    · subst S
      simpa only [fiber_inl, coreFiber_empty] using
        (show (interior B).Nonempty from ⟨0, zero_mem_interior_B⟩)
    · rw [fiber_inl, coreFiber_of_nonempty S (Finset.nonempty_iff_ne_empty.mpr hS)]
      exact SourceBasis.K_interior_nonempty _ _
  | inr i => exact SourceBasis.A_interior_nonempty

theorem fiber_affineSpan_eq_top (a : FiberIndex) : affineSpan ℝ (fiber a) = ⊤ :=
  (fiber_convex a).interior_nonempty_iff_affineSpan_eq_top.mp (fiber_interior_nonempty a)

theorem continuous_dimension : Module.finrank ℝ E = 23 := by simp [E]

theorem integer_dimension : Module.finrank ℝ (IntegerCoordinate → ℝ) = integerDimension := by
  simp [integerDimension]

theorem ambient_dimension :
    Module.finrank ℝ ((IntegerCoordinate → ℝ) × E) = integerDimension + 23 := by
  rw [Module.finrank_prod, integer_dimension, continuous_dimension]

end SharpOC.Counterexample
