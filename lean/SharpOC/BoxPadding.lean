import SharpOC.MiddleSimplex
import SharpOC.Halfspaces
import Mathlib.MeasureTheory.Measure.Prod

/-! Actual finite-dimensional simplex padding. These geometric and measure
identities are generic; `BoxMeasure` instantiates them with the concrete body. -/

noncomputable section
open Set MeasureTheory
open scoped ENNReal

namespace SharpOC.BoxPadding

def simplex (d : ℕ) : Set (Fin d → ℝ) :=
  convexHull ℝ (range (MiddleSimplex.standardBasis d))

theorem simplex_compact (d : ℕ) : IsCompact (simplex d) :=
  (Set.finite_range (MiddleSimplex.standardBasis d)).isCompact_convexHull ℝ

theorem simplex_convex (d : ℕ) : Convex ℝ (simplex d) := convex_convexHull ℝ _

theorem simplex_interior_nonempty (d : ℕ) : (interior (simplex d)).Nonempty :=
  ⟨_, (MiddleSimplex.standardBasis d).centroid_mem_interior_convexHull⟩

theorem simplex_volume_pos (d : ℕ) : 0 < volume (simplex d) :=
  Measure.measure_pos_of_nonempty_interior volume (simplex_interior_nonempty d)

theorem simplex_volume_ne_top (d : ℕ) : volume (simplex d) ≠ ⊤ :=
  (simplex_compact d).measure_ne_top

theorem zero_mem_simplex (d : ℕ) : (0 : Fin d → ℝ) ∈ simplex d := by
  apply subset_convexHull ℝ _
  refine ⟨Fin.last d, ?_⟩
  exact MiddleSimplex.standardVertex_last d

section Products

variable {Z E V : Type*}
  [NormedAddCommGroup Z] [NormedSpace ℝ Z]
  [NormedAddCommGroup E] [NormedSpace ℝ E]
  [NormedAddCommGroup V] [NormedSpace ℝ V]

def padded (C : Set (Z × E)) (J : Set V) : Set (Z × (E × V)) :=
  {p | (p.1, p.2.1) ∈ C ∧ p.2.2 ∈ J}

theorem padded_eq_image (C : Set (Z × E)) (J : Set V) :
    padded C J = (ContinuousLinearEquiv.prodAssoc ℝ Z E V) '' (C ×ˢ J) := by
  ext p
  constructor
  · intro hp
    exact ⟨((p.1, p.2.1), p.2.2), hp, rfl⟩
  · rintro ⟨⟨⟨z, x⟩, v⟩, hp, rfl⟩
    exact hp

theorem padded_compact {C : Set (Z × E)} {J : Set V}
    (hC : IsCompact C) (hJ : IsCompact J) : IsCompact (padded C J) := by
  rw [padded_eq_image]
  exact (hC.prod hJ).image (ContinuousLinearEquiv.prodAssoc ℝ Z E V).continuous

theorem padded_convex {C : Set (Z × E)} {J : Set V}
    (hC : Convex ℝ C) (hJ : Convex ℝ J) : Convex ℝ (padded C J) := by
  rw [padded_eq_image]
  exact (hC.prod hJ).linear_image (ContinuousLinearEquiv.prodAssoc ℝ Z E V).toLinearMap

theorem padded_interior_nonempty {C : Set (Z × E)} {J : Set V}
    (hC : (interior C).Nonempty) (hJ : (interior J).Nonempty) :
    (interior (padded C J)).Nonempty := by
  rw [padded_eq_image]
  change (interior ((ContinuousLinearEquiv.prodAssoc ℝ Z E V).toHomeomorph ''
    (C ×ˢ J))).Nonempty
  rw [← Homeomorph.image_interior, interior_prod_eq]
  exact (hC.prod hJ).image _

theorem padded_fiber (C : Set (Z × E)) (J : Set V) (z : Z) :
    {p | (z, p) ∈ padded C J} = {x | (z, x) ∈ C} ×ˢ J := rfl

/-- Extend a genuine ambient cut by ignoring the new continuous factor. -/
def extendCut (F : (Z × E) →L[ℝ] ℝ) : (Z × (E × V)) →L[ℝ] ℝ :=
  F.comp ((ContinuousLinearMap.fst ℝ Z (E × V)).prod
    ((ContinuousLinearMap.fst ℝ E V).comp (ContinuousLinearMap.snd ℝ Z (E × V))))

@[simp] theorem extendCut_apply (F : (Z × E) →L[ℝ] ℝ) (z : Z) (x : E) (v : V) :
    extendCut F (z, (x, v)) = F (z, x) := rfl

theorem extendCut_ne_zero {F : (Z × E) →L[ℝ] ℝ} (hF : F ≠ 0) :
    (extendCut F : (Z × (E × V)) →L[ℝ] ℝ) ≠ 0 := by
  intro hz
  apply hF
  apply ContinuousLinearMap.ext
  intro p
  have hp := congrArg (fun G : (Z × (E × V)) →L[ℝ] ℝ => G (p.1, (p.2, 0))) hz
  exact hp

theorem extended_cut_fiber (B : Set E) (J : Set V) (z : Z)
    (F : (Z × E) →L[ℝ] ℝ) (t : ℝ) :
    (B ×ˢ J) ∩ {p | t ≤ extendCut F (z, p)} =
      (B ∩ {x | t ≤ F (z, x)}) ×ˢ J := by
  ext p
  change ((p.1 ∈ B ∧ p.2 ∈ J) ∧ t ≤ F (z, p.1)) ↔
    ((p.1 ∈ B ∧ t ≤ F (z, p.1)) ∧ p.2 ∈ J)
  tauto

end Products

section ProductMeasure

variable {E V : Type*} [MeasurableSpace E] [MeasurableSpace V]

theorem product_cut_sum {ι Z : Type*} [Fintype ι]
    [NormedAddCommGroup Z] [NormedSpace ℝ Z]
    [NormedAddCommGroup E] [NormedSpace ℝ E]
    [NormedAddCommGroup V] [NormedSpace ℝ V]
    (μ : Measure E) (ν : Measure V) [SFinite ν]
    (z : ι → Z) (B : ι → Set E) (J : Set V)
    (F : (Z × E) →L[ℝ] ℝ) (t : ℝ) :
    (∑ i, (μ.prod ν) ((B i ×ˢ J) ∩ {p | t ≤ extendCut F (z i, p)})) =
      (∑ i, μ (B i ∩ {x | t ≤ F (z i, x)})) * ν J := by
  simp_rw [extended_cut_fiber, Measure.prod_prod]
  exact (Finset.sum_mul _ _ _).symm

end ProductMeasure

section Exposed

variable {ι Z E : Type*} [Fintype ι]
  [NormedAddCommGroup Z] [NormedSpace ℝ Z]
  [NormedAddCommGroup E] [NormedSpace ℝ E] [MeasurableSpace E]

/-- A cap in the common simplex factor can be isolated at an exposed
integer base. The other continuous factor may be any compact set. -/
theorem exposed_product_simplex_fiber_sum_mass
    {d : ℕ} (hd : 0 < d) (μ : Measure E)
    (z : ι → Z) (B : ι → Set E) (hB : ∀ j, IsCompact (B j))
    (i : ι) (ell : Z →L[ℝ] ℝ)
    (hexp : ∀ j, j ≠ i → ell (z j) < ell (z i))
    (x : E × (Fin d → ℝ)) :
    ∃ F : (Z × (E × (Fin d → ℝ))) →L[ℝ] ℝ, ∃ t : ℝ,
      F ≠ 0 ∧ t ≤ F (z i, x) ∧
      (∑ j, (μ.prod volume) ((B j ×ˢ simplex d) ∩ {y | t ≤ F (z j, y)})) =
        ENNReal.ofReal (((d : ℝ) / (d + 1)) ^ d) * μ (B i) * volume (simplex d) := by
  classical
  obtain ⟨h, a, hne, hax, hcap⟩ := simplex_small_halfspace hd
    (MiddleSimplex.standardBasis d) volume (by simp) x.2
  let g : (E × (Fin d → ℝ)) →L[ℝ] ℝ :=
    h.comp (ContinuousLinearMap.snd ℝ E (Fin d → ℝ))
  have hgne : g ≠ 0 := by
    intro hg
    apply hne
    ext v
    have hv := congrArg (fun f : (E × (Fin d → ℝ)) →L[ℝ] ℝ => f (0, v)) hg
    simpa [g] using hv
  obtain ⟨F, t, hF, hexact, hout⟩ := exposed_fiber_cut z
    (fun j => B j ×ˢ simplex d) (fun j => (hB j).prod (simplex_compact d))
    i ell hexp g hgne a
  refine ⟨F, t, hF, (hexact x).mp hax, ?_⟩
  rw [Finset.sum_eq_single i]
  · have hset : (B i ×ˢ simplex d) ∩ {y | t ≤ F (z i, y)} =
        B i ×ˢ (simplex d ∩ {v | a ≤ h v}) := by
      ext y
      simp only [mem_inter_iff, mem_prod, mem_setOf_eq, ← hexact y]
      change ((y.1 ∈ B i ∧ y.2 ∈ simplex d) ∧ a ≤ h y.2) ↔ _
      tauto
    rw [hset, Measure.prod_prod]
    change μ (B i) * volume (simplex d ∩ {v | a ≤ h v}) = _
    rw [show volume (simplex d ∩ {v | a ≤ h v}) =
      ENNReal.ofReal (((d : ℝ) / (d + 1)) ^ d) * volume (simplex d) from hcap]
    ac_rfl
  · intro j hj hji
    have hempty : (B j ×ˢ simplex d) ∩ {y | t ≤ F (z j, y)} = ∅ := by
      apply eq_empty_iff_forall_notMem.mpr
      rintro y ⟨hy, hty⟩
      exact (not_le_of_gt (hout j hji y hy)) hty
    rw [hempty, measure_empty]
  · intro hi
    exact (hi (Finset.mem_univ i)).elim

end Exposed

end SharpOC.BoxPadding
