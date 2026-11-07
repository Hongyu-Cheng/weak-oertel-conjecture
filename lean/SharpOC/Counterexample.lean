import SharpOC.CounterexampleMass
import SharpOC.MixedIntegerMeasure

/-!
# Counterexample to the sharp mixed-integer Grünbaum bound

This is the final theorem about the actual convex body and the sum of
Lebesgue measures over all integer fibers. The integer-coordinate index
type has cardinality `3 * 10^92`; the continuous dimension is 23.
The upper bound is uniform over all mixed-integer points and strictly
smaller than the sharp proposed constant. No statement about the weak
absolute-constant conjecture is asserted here.
-/

noncomputable section
open Set MeasureTheory

namespace SharpOC.Counterexample
open MiddleSimplex

/-- A fixed strict upper bound for every point's normalized halfspace depth. -/
def depthBound : ℝ := gamma * M / totalMass

theorem totalMass_pos : 0 < totalMass := by
  unfold totalMass
  rw [← mixedIntegerMass_body_toReal]
  exact mixedIntegerMass_body_toReal_pos

theorem depthBound_pos : 0 < depthBound := by
  exact div_pos (mul_pos gamma_pos M_pos) totalMass_pos

theorem depthBound_lt_sharp : depthBound < gamma / (2 : ℝ)^integerDimension := by
  have h := strict_depth_ratio integerDimension b b_pos
  simpa only [depthBound, totalMass_eq, M] using h.2

/-- Every actual mixed-integer point has an actual proper closed ambient
halfspace with the same uniform upper bound. -/
theorem point_has_small_halfspace (z : IntegerCoordinate → ℤ) (x : E)
    (hx : ((fun i => (z i : ℝ)), x) ∈ body) :
    ∃ F : AmbientSpace →L[ℝ] ℝ, ∃ t : ℝ,
      F ≠ 0 ∧ t ≤ F ((fun i => (z i : ℝ)), x) ∧
      (mixedIntegerMass (body ∩ {p | t ≤ F p})).toReal /
          (mixedIntegerMass body).toReal ≤ depthBound := by
  obtain ⟨a, ha⟩ := integer_base_census z x hx
  obtain ⟨F, t, hF, ht, hmass⟩ := every_fiber_point_small_cut a x
  refine ⟨F, t, hF, ?_, ?_⟩
  · simpa only [← ha, integerBase_cast] using ht
  · rw [mixedIntegerMass_body_cut_toReal, mixedIntegerMass_body_toReal]
    change cutMass F t / totalMass ≤ gamma * M / totalMass
    exact div_le_div_of_nonneg_right hmass totalMass_pos.le

theorem origin_mem_body : ((0 : IntegerSpace), (0 : E)) ∈ body := by
  have h : (0 : E) ∈ B := interior_subset zero_mem_interior_B
  rwa [← origin_fiber_exact] at h

/-- All nonempty integer fibers of the counterexample have full continuous
dimension. In particular the volume formulation is nondegenerate. -/
theorem integer_fibers_full_dimensional (z : IntegerCoordinate → ℤ)
    (hz : {x : E | ((fun i => (z i : ℝ)), x) ∈ body}.Nonempty) :
    (interior {x : E | ((fun i => (z i : ℝ)), x) ∈ body}).Nonempty := by
  obtain ⟨x, hx⟩ := hz
  obtain ⟨a, rfl⟩ := integer_base_census z x hx
  rw [integer_fiber_exact]
  exact fiber_interior_nonempty a

/-- Direct strict violation at every possible candidate center. The
halfspace includes the candidate and has strictly insufficient mass. -/
theorem sharp_oc_strict_violation (z : IntegerCoordinate → ℤ) (x : E)
    (hx : ((fun i => (z i : ℝ)), x) ∈ body) :
    ∃ F : AmbientSpace →L[ℝ] ℝ, ∃ t : ℝ,
      F ≠ 0 ∧ t ≤ F ((fun i => (z i : ℝ)), x) ∧
      (mixedIntegerMass (body ∩ {p | t ≤ F p})).toReal <
        (gamma / (2 : ℝ)^integerDimension) * (mixedIntegerMass body).toReal := by
  obtain ⟨F, t, hF, ht, hmass⟩ := point_has_small_halfspace z x hx
  refine ⟨F, t, hF, ht, ?_⟩
  exact (div_lt_iff₀ mixedIntegerMass_body_toReal_pos).mp
    (lt_of_le_of_lt hmass depthBound_lt_sharp)

/-- Complete existential counterexample in the full-dimensional
mixed-integer-volume formulation. Every hypothesis about the concrete
body, the selected halfspaces, and the measure is proved above. -/
theorem sharp_oc_counterexample :
    ∃ C : Set AmbientSpace,
      IsCompact C ∧ Convex ℝ C ∧ (interior C).Nonempty ∧
      ((0 : IntegerSpace), (0 : E)) ∈ C ∧
      0 < mixedIntegerMass C ∧ mixedIntegerMass C ≠ ⊤ ∧
      (∀ z : IntegerCoordinate → ℤ,
        {x : E | ((fun i => (z i : ℝ)), x) ∈ C}.Nonempty →
        (interior {x : E | ((fun i => (z i : ℝ)), x) ∈ C}).Nonempty) ∧
      ∃ r : ℝ, 0 < r ∧ r < gamma / (2 : ℝ)^integerDimension ∧
        ∀ (z : IntegerCoordinate → ℤ) (x : E),
          ((fun i => (z i : ℝ)), x) ∈ C →
          ∃ F : AmbientSpace →L[ℝ] ℝ, ∃ t : ℝ,
            F ≠ 0 ∧ t ≤ F ((fun i => (z i : ℝ)), x) ∧
            (mixedIntegerMass (C ∩ {p | t ≤ F p})).toReal /
                (mixedIntegerMass C).toReal ≤ r := by
  exact ⟨body, body_compact, body_convex, body_interior_nonempty, origin_mem_body,
    mixedIntegerMass_body_pos, mixedIntegerMass_body_ne_top,
    integer_fibers_full_dimensional, depthBound, depthBound_pos,
    depthBound_lt_sharp, point_has_small_halfspace⟩

end SharpOC.Counterexample
