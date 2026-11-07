import SharpOC.MiddleSimplex

noncomputable section
open Set MeasureTheory

namespace SharpOC

variable {ι E : Type*} [Fintype ι]
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]

/-- Injective affine images of an affine basis are again an affine basis
in the same finite-dimensional ambient space. -/
def affineImageBasis (b : AffineBasis ι ℝ E) (F : E →ᵃ[ℝ] E)
    (hF : Function.Injective F) : AffineBasis ι ℝ E where
  toFun := F ∘ b
  ind' := b.ind.map' F hF
  tot' := (b.ind.map' F hF).affineSpan_eq_top_iff_card_eq_finrank_add_one.mpr
    b.card_eq_finrank_add_one

@[simp] theorem affineImageBasis_apply (b : AffineBasis ι ℝ E) (F : E →ᵃ[ℝ] E)
    (hF : Function.Injective F) (i : ι) : affineImageBasis b F hF i = F (b i) := rfl

theorem affineImageBasis_hull (b : AffineBasis ι ℝ E) (F : E →ᵃ[ℝ] E)
    (hF : Function.Injective F) :
    convexHull ℝ (range (affineImageBasis b F hF)) = F '' convexHull ℝ (range b) := by
  change convexHull ℝ (range (F ∘ b)) = _
  rw [Set.range_comp]
  exact (F.image_convexHull _).symm

def homotheticBasis (b : AffineBasis ι ℝ E) (c : E) (r : ℝ) (hr : r ≠ 0) :
    AffineBasis ι ℝ E :=
  affineImageBasis b (AffineMap.homothety c r) (AffineMap.homothety_injective c hr)

theorem homotheticBasis_hull (b : AffineBasis ι ℝ E) (c : E) (r : ℝ) (hr : r ≠ 0) :
    convexHull ℝ (range (homotheticBasis b c r hr)) =
      AffineMap.homothety c r '' convexHull ℝ (range b) :=
  affineImageBasis_hull _ _ _

def scaledTranslatedMap (r : ℝ) (c : E) : E →ᵃ[ℝ] E :=
  r • AffineMap.id ℝ E + AffineMap.const ℝ E c

theorem scaledTranslatedMap_injective (r : ℝ) (c : E) (hr : r ≠ 0) :
    Function.Injective (scaledTranslatedMap r c) := by
  intro x y h
  change r • x + c = r • y + c at h
  exact (smul_right_injective E hr) (add_right_cancel h)

def scaledTranslatedBasis (b : AffineBasis ι ℝ E) (r : ℝ) (c : E) (hr : r ≠ 0) :
    AffineBasis ι ℝ E :=
  affineImageBasis b (scaledTranslatedMap r c) (scaledTranslatedMap_injective r c hr)

theorem scaledTranslatedBasis_hull (b : AffineBasis ι ℝ E) (r : ℝ) (c : E)
    (hr : r ≠ 0) :
    convexHull ℝ (range (scaledTranslatedBasis b r c hr)) =
      (fun x => r • x + c) '' convexHull ℝ (range b) :=
  affineImageBasis_hull _ _ _

namespace SourceGeometry

def chartAffineMap {n : ℕ} (M : Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ) :
    (Fin n → ℝ) →ᵃ[ℝ] (Fin n → ℝ) :=
  AffineMap.const ℝ (Fin n → ℝ) (fun i => M i.castSucc (Fin.last n)) +
    (Matrix.toLin' (chartMatrix M)).toAffineMap

theorem chartAffineMap_injective {n : ℕ}
    (M : Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ)
    (hM : ∀ j, ∑ i, M i j = 1) (hd : M.det ≠ 0) :
    Function.Injective (chartAffineMap M) := by
  intro x y h
  apply Matrix.mulVec_injective_of_det_ne_zero (by rwa [chartMatrix_det M hM])
  change (fun i => M i.castSucc (Fin.last n)) + (chartMatrix M).mulVec x =
    (fun i => M i.castSucc (Fin.last n)) + (chartMatrix M).mulVec y at h
  exact add_left_cancel h

theorem chartAffineMap_standardVertex {n : ℕ}
    (M : Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ) (j : Fin (n + 1)) :
    chartAffineMap M (MiddleSimplex.standardVertex n j) = (fun i => M i.castSucc j) := by
  rcases Fin.eq_castSucc_or_eq_last j with ⟨j, rfl⟩ | rfl
  · ext i
    simp [chartAffineMap, MiddleSimplex.standardVertex_castSucc, Matrix.toLin'_apply,
      Matrix.mulVec_single_one, chartMatrix]
  · simp [chartAffineMap]

def chartBasis {n : ℕ} (M : Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ)
    (hM : ∀ j, ∑ i, M i j = 1) (hd : M.det ≠ 0) :
    AffineBasis (Fin (n + 1)) ℝ (Fin n → ℝ) :=
  affineImageBasis (MiddleSimplex.standardBasis n) (chartAffineMap M)
    (chartAffineMap_injective M hM hd)

theorem chartBasis_hull {n : ℕ} (M : Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ)
    (hM : ∀ j, ∑ i, M i j = 1) (hd : M.det ≠ 0) :
    convexHull ℝ (range (chartBasis M hM hd)) = chartSimplex M := by
  congr 2
  ext j i
  exact congrFun (chartAffineMap_standardVertex M j) i

end SourceGeometry
end SharpOC
