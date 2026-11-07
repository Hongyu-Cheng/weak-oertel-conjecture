import Mathlib.Analysis.InnerProductSpace.PiL2
import Mathlib.MeasureTheory.Measure.Hausdorff
import Mathlib.MeasureTheory.Measure.Lebesgue.EqHaar
import Mathlib.Topology.Order.Compact
import Mathlib.Tactic
import SharpOC.SimplexCaps

/-!
Finite exposed-fiber isolation and Hausdorff additivity.

These are general geometric lemmas; this file alone does not certify the
counterexample construction. In particular it makes no identification of
mathlib's diameter-gauge Hausdorff measure with normalized Euclidean volume.
-/

noncomputable section
open Set MeasureTheory
open scoped ENNReal

namespace SharpOC

section Exposed

variable {ι Z E : Type*} [Fintype ι]
  [NormedAddCommGroup Z] [NormedSpace ℝ Z]
  [NormedAddCommGroup E] [NormedSpace ℝ E]

/-- A compact family of fibers at a strictly exposed base can be cut by
one actual ambient continuous-linear halfspace realizing any prescribed
continuous cap on that fiber and strictly excluding every other fiber. -/
theorem exposed_fiber_cut
    (z : ι → Z) (B : ι → Set E) (hB : ∀ j, IsCompact (B j))
    (i : ι) (ell : Z →L[ℝ] ℝ)
    (hexp : ∀ j, j ≠ i → ell (z j) < ell (z i))
    (h : E →L[ℝ] ℝ) (hne : h ≠ 0) (t : ℝ) :
    ∃ F : (Z × E) →L[ℝ] ℝ, ∃ b : ℝ, F ≠ 0 ∧
      (∀ x, t ≤ h x ↔ b ≤ F (z i, x)) ∧
      (∀ j, j ≠ i → ∀ x ∈ B j, F (z j, x) < b) := by
  classical
  obtain ⟨R, hR⟩ := ((isCompact_iUnion hB).image h.continuous).bddAbove
  let q : ι → ℝ := fun j => (R - t) / (ell (z i) - ell (z j))
  obtain ⟨Q₀, hQ₀⟩ := Finite.bddAbove_range q
  let Q : ℝ := max (Q₀ + 1) 1
  have hQ (j : ι) : q j < Q := by
    have hj : q j ≤ Q₀ := hQ₀ (mem_range_self j)
    exact lt_of_lt_of_le (by linarith) (le_max_left _ _)
  let F : (Z × E) →L[ℝ] ℝ :=
    h.comp (ContinuousLinearMap.snd ℝ Z E) +
      Q • ell.comp (ContinuousLinearMap.fst ℝ Z E)
  refine ⟨F, t + Q * ell (z i), ?_, ?_, ?_⟩
  · intro hF
    apply hne
    ext x
    have hx := congrArg (fun G : (Z × E) →L[ℝ] ℝ => G (0, x)) hF
    simpa [F] using hx
  · intro x
    change t ≤ h x ↔ t + Q * ell (z i) ≤ h x + Q * ell (z i)
    exact (add_le_add_iff_right _).symm
  · intro j hji x hx
    have hgap : 0 < ell (z i) - ell (z j) := sub_pos.mpr (hexp j hji)
    have hbound : h x ≤ R := hR ⟨x, mem_iUnion.mpr ⟨j, hx⟩, rfl⟩
    have hlarge : R - t < Q * (ell (z i) - ell (z j)) :=
      (div_lt_iff₀ hgap).mp (hQ j)
    change h x + Q * ell (z j) < t + Q * ell (z i)
    nlinarith

end Exposed

section Hausdorff

variable {ι X Y : Type*} [Fintype ι]
  [MetricSpace X] [MetricSpace Y]
  [MeasurableSpace X] [BorelSpace X]
  [MeasurableSpace Y] [BorelSpace Y]

/-- Additivity for finitely many disjoint isometrically embedded compact
fibers, using precisely the same Hausdorff gauge on source and target. -/
theorem hausdorff_finite_isometric_union
    (d : ℝ) (hd : 0 ≤ d) (B : ι → Set X)
    (hB : ∀ i, IsCompact (B i)) (f : ι → X → Y)
    (hf : ∀ i, Isometry (f i))
    (hdis : Pairwise (fun i j => Disjoint (f i '' B i) (f j '' B j))) :
    Measure.hausdorffMeasure d (⋃ i, f i '' B i) =
      ∑ i, Measure.hausdorffMeasure d (B i) := by
  rw [measure_iUnion hdis (fun i => ((hB i).image (hf i).continuous).measurableSet),
    tsum_fintype]
  exact Finset.sum_congr rfl (fun i _ => (hf i).hausdorffMeasure_image (Or.inl hd) _)

end Hausdorff

section ProductFibers

variable {ι Z E : Type*} [Fintype ι]
  [MetricSpace Z] [MetricSpace E]
  [MeasurableSpace Z] [BorelSpace Z]
  [MeasurableSpace E] [BorelSpace E]
  [BorelSpace (Z × E)]

omit [BorelSpace Z] in
/-- Exact Hausdorff fiber additivity in an ambient product. The product
norm does not change the metric induced on an individual fiber. -/
theorem hausdorff_product_fibers
    (d : ℝ) (hd : 0 ≤ d) (z : ι → Z) (hinj : Function.Injective z)
    (B : ι → Set E) (hB : ∀ i, IsCompact (B i)) :
    Measure.hausdorffMeasure d (⋃ i, ({z i} : Set Z) ×ˢ B i) =
      ∑ i, Measure.hausdorffMeasure d (B i) := by
  have hf (i : ι) : Isometry (fun x : E => (z i, x)) := by
    intro x y
    simp [Prod.edist_eq]
  have hdis : Pairwise (fun i j =>
      Disjoint ((fun x : E => (z i, x)) '' B i)
        ((fun x : E => (z j, x)) '' B j)) := by
    intro i j hij
    apply Set.disjoint_left.mpr
    rintro p ⟨x, hx, hpx⟩ ⟨y, hy, hpy⟩
    apply hij
    apply hinj
    exact congrArg Prod.fst (hpx.trans hpy.symm)
  convert hausdorff_finite_isometric_union d hd B hB
    (fun i x => (z i, x)) hf hdis using 1
  congr 1
  ext p
  simp only [mem_iUnion, mem_prod, mem_singleton_iff, mem_image]
  constructor
  · rintro ⟨i, hi, hx⟩
    exact ⟨i, p.2, hx, Prod.ext hi.symm rfl⟩
  · rintro ⟨i, x, hx, rfl⟩
    exact ⟨i, rfl, hx⟩

end ProductFibers

section ClosedCutMass

variable {ι Z E : Type*} [Fintype ι]
  [NormedAddCommGroup Z] [NormedSpace ℝ Z]
  [NormedAddCommGroup E] [NormedSpace ℝ E]
  [MeasurableSpace Z] [BorelSpace Z]
  [MeasurableSpace E] [BorelSpace E]
  [BorelSpace (Z × E)]

omit [BorelSpace Z] in
/-- The exact fiber sum after intersection with any closed ambient
halfspace, including oblique halfspaces and boundary mass. -/
theorem hausdorff_product_fibers_closed_cut
    (d : ℝ) (hd : 0 ≤ d) (z : ι → Z) (hinj : Function.Injective z)
    (B : ι → Set E) (hB : ∀ i, IsCompact (B i))
    (F : (Z × E) →L[ℝ] ℝ) (t : ℝ) :
    Measure.hausdorffMeasure d
        ((⋃ i, ({z i} : Set Z) ×ˢ B i) ∩ {p | t ≤ F p}) =
      ∑ i, Measure.hausdorffMeasure d (B i ∩ {x | t ≤ F (z i, x)}) := by
  have hcomp (i : ι) : IsCompact (B i ∩ {x | t ≤ F (z i, x)}) :=
    (hB i).inter_right (isClosed_le continuous_const
      (F.continuous.comp (continuous_const.prodMk continuous_id)))
  have hset : ((⋃ i, ({z i} : Set Z) ×ˢ B i) ∩ {p | t ≤ F p}) =
      ⋃ i, ({z i} : Set Z) ×ˢ (B i ∩ {x | t ≤ F (z i, x)}) := by
    ext p
    simp only [mem_inter_iff, mem_iUnion, mem_prod, mem_singleton_iff, mem_ofPred_eq]
    constructor
    · rintro ⟨⟨i, hi, hx⟩, hp⟩
      exact ⟨i, hi, hx, by simpa [← hi] using hp⟩
    · rintro ⟨i, hi, hx, hp⟩
      exact ⟨⟨i, hi, hx⟩, by simpa [← hi] using hp⟩
  rw [hset]
  exact hausdorff_product_fibers d hd z hinj _ hcomp

end ClosedCutMass

section FiberSum

variable {ι Z E : Type*} [Fintype ι] [MeasurableSpace E]

/-- The exact counting-times-measure mass of a finite list of distinct
fibers, with zero mass outside that list. No ambient-volume substitution
is used. -/
theorem finite_fiber_sum (μ : Measure E) (S : Z → Set E)
    (z : ι → Z) (hinj : Function.Injective z)
    (hzero : ∀ w, w ∉ range z → μ (S w) = 0) :
    (∑' w, μ (S w)) = ∑ i, μ (S (z i)) := by
  have hs : Function.support (fun w => μ (S w)) ⊆ range z := by
    intro w hw
    by_contra hz
    exact hw (hzero w hz)
  exact (hinj.tsum_eq hs).symm.trans (tsum_fintype _)

end FiberSum

section ExposedSimplex

variable {ι Z E : Type*} [Fintype ι]
  [NormedAddCommGroup Z] [NormedSpace ℝ Z]
  [NormedAddCommGroup E] [NormedSpace ℝ E]
  [FiniteDimensional ℝ E]
  [MeasurableSpace Z] [MeasurableSpace E] [BorelSpace E]
  [BorelSpace (Z × E)]

/-- A complete all-point small-cap statement for an exposed simplex
fiber, with the actual ambient halfspace and its exact Hausdorff mass.
The other fibers may be arbitrary compact sets. -/
theorem exposed_simplex_halfspace_mass
    {d : ℕ} (hd : 0 < d) (hdim : Module.finrank ℝ E = d)
    (z : ι → Z) (hinj : Function.Injective z)
    (B : ι → Set E) (hB : ∀ i, IsCompact (B i))
    (i : ι) (ell : Z →L[ℝ] ℝ)
    (hexp : ∀ j, j ≠ i → ell (z j) < ell (z i))
    (b : AffineBasis (Fin (d + 1)) ℝ E)
    (hBi : B i = convexHull ℝ (range b)) (x : E) :
    ∃ F : (Z × E) →L[ℝ] ℝ, ∃ t : ℝ, F ≠ 0 ∧ t ≤ F (z i, x) ∧
      Measure.hausdorffMeasure (d : ℝ)
          ((⋃ j, ({z j} : Set Z) ×ˢ B j) ∩ {p | t ≤ F p}) =
        ENNReal.ofReal (((d : ℝ) / (d + 1)) ^ d) *
          Measure.hausdorffMeasure (d : ℝ) (B i) := by
  classical
  obtain ⟨h, a, hne, hax, hcap⟩ := simplex_small_halfspace hd b
    (Measure.hausdorffMeasure (Module.finrank ℝ E)) hdim x
  have hcap' : Measure.hausdorffMeasure (d : ℝ) (B i ∩ {y | a ≤ h y}) =
      ENNReal.ofReal (((d : ℝ) / (d + 1)) ^ d) *
        Measure.hausdorffMeasure (d : ℝ) (B i) := by
    simpa only [hdim, hBi] using hcap
  obtain ⟨F, t, hF, hexact, hout⟩ := exposed_fiber_cut z B hB i ell hexp h hne a
  refine ⟨F, t, hF, (hexact x).mp hax, ?_⟩
  rw [hausdorff_product_fibers_closed_cut (d : ℝ) (by positivity) z hinj B hB F t]
  rw [Finset.sum_eq_single i]
  · convert hcap' using 1
    congr 1
    ext y
    exact and_congr_right (fun _ => (hexact y).symm)
  · intro j hj hji
    have hempty : B j ∩ {y | t ≤ F (z j, y)} = ∅ := by
      apply eq_empty_iff_forall_notMem.mpr
      rintro y ⟨hy, hty⟩
      exact (not_le_of_gt (hout j hji y hy)) hty
    rw [hempty, measure_empty]
  · intro hi
    exact (hi (Finset.mem_univ i)).elim

/-- The same exposed-simplex cut, stated directly as counting measure
over the bases times continuous Haar measure. -/
theorem exposed_simplex_fiber_sum_mass
    {d : ℕ} (hd : 0 < d) (hdim : Module.finrank ℝ E = d)
    (μ : Measure E) [Measure.IsAddHaarMeasure μ]
    (z : ι → Z) (B : ι → Set E) (hB : ∀ i, IsCompact (B i))
    (i : ι) (ell : Z →L[ℝ] ℝ)
    (hexp : ∀ j, j ≠ i → ell (z j) < ell (z i))
    (b : AffineBasis (Fin (d + 1)) ℝ E)
    (hBi : B i = convexHull ℝ (range b)) (x : E) :
    ∃ F : (Z × E) →L[ℝ] ℝ, ∃ t : ℝ, F ≠ 0 ∧ t ≤ F (z i, x) ∧
      (∑ j, μ (B j ∩ {y | t ≤ F (z j, y)})) =
        ENNReal.ofReal (((d : ℝ) / (d + 1)) ^ d) * μ (B i) := by
  classical
  obtain ⟨h, a, hne, hax, hcap⟩ := simplex_small_halfspace hd b μ hdim x
  obtain ⟨F, t, hF, hexact, hout⟩ := exposed_fiber_cut z B hB i ell hexp h hne a
  refine ⟨F, t, hF, (hexact x).mp hax, ?_⟩
  rw [Finset.sum_eq_single i]
  · rw [hBi]
    convert hcap using 1
    congr 1
    ext y
    exact and_congr_right (fun _ => (hexact y).symm)
  · intro j hj hji
    have hempty : B j ∩ {y | t ≤ F (z j, y)} = ∅ := by
      apply eq_empty_iff_forall_notMem.mpr
      rintro y ⟨hy, hty⟩
      exact (not_le_of_gt (hout j hji y hy)) hty
    rw [hempty, measure_empty]
  · intro hi
    exact (hi (Finset.mem_univ i)).elim

end ExposedSimplex

end SharpOC
