import SharpOC.AffineSimplex
import SharpOC.SourceContainment

noncomputable section
open Set MeasureTheory
open SharpOC.MiddleSimplex SharpOC.SourceGeometry SharpOC.SourceContainment

namespace SharpOC.SourceBasis

theorem cyclic_det_ne_zero (a : Fin 3) : (cyclicSourceMatrix a).det ≠ 0 := by
  intro h
  have hh := cyclicSourceMatrix_abs_det a
  rw [h, abs_zero] at hh
  norm_num at hh

def rawBasis (a : Fin 3) : AffineBasis (Fin 24) ℝ E :=
  chartBasis (cyclicSourceMatrix a) (cyclicSourceMatrix_column_sum a) (cyclic_det_ne_zero a)

theorem rawBasis_hull (a : Fin 3) :
    convexHull ℝ (range (rawBasis a)) = chartSimplex (cyclicSourceMatrix a) :=
  chartBasis_hull _ _ _

def TBasis (a : Fin 3) : AffineBasis (Fin 24) ℝ E :=
  scaledTranslatedBasis (rawBasis a) 1 shift (by norm_num)

theorem TBasis_hull (a : Fin 3) : convexHull ℝ (range (TBasis a)) = T a := by
  rw [TBasis, scaledTranslatedBasis_hull, rawBasis_hull, T_eq_translate_chartSimplex]
  simp [add_comm]

def PBasis (a : Fin 3) : AffineBasis (Fin 24) ℝ E :=
  homotheticBasis (TBasis a) (center a) (103/104 : ℝ) (by norm_num)

theorem PBasis_hull (a : Fin 3) : convexHull ℝ (range (PBasis a)) = P a := by
  rw [PBasis, homotheticBasis_hull, TBasis_hull]
  rfl

def KBasis (a : Fin 3) (k : ℕ) : AffineBasis (Fin 24) ℝ E :=
  scaledTranslatedBasis (PBasis a) 2 (((k : ℝ) - 1) • center a) (by norm_num)

theorem KBasis_hull (a : Fin 3) (k : ℕ) :
    convexHull ℝ (range (KBasis a k)) = K a k := by
  rw [KBasis, scaledTranslatedBasis_hull, PBasis_hull]
  rfl

def ABasis : AffineBasis (Fin 24) ℝ E :=
  scaledTranslatedBasis basis (1/10000 : ℝ) 0 (by norm_num)

theorem ABasis_hull : convexHull ℝ (range ABasis) = A := by
  rw [ABasis, scaledTranslatedBasis_hull]
  simp only [add_zero]
  rfl

theorem K_interior_nonempty (a : Fin 3) (k : ℕ) : (interior (K a k)).Nonempty := by
  rw [← KBasis_hull]
  exact ⟨_, (KBasis a k).centroid_mem_interior_convexHull⟩

theorem A_interior_nonempty : (interior A).Nonempty := by
  rw [← ABasis_hull]
  exact ⟨_, ABasis.centroid_mem_interior_convexHull⟩

end SharpOC.SourceBasis
