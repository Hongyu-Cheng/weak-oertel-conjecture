import Mathlib

/-!
# Ordered-chain source simplices

This module proves the algebraic geometry of the 24-coordinate source
simplices. No statement in this file identifies a determinant with a
23-dimensional Hausdorff measure. That bridge is a separate theorem.
-/

namespace SharpOC.SourceGeometry

open scoped BigOperators

noncomputable section

/-- One ordered chain's three vertex columns, in increasing coordinate order.
The columns are the uniform suffixes of lengths three, two, and one. -/
def chainMatrix : Matrix (Fin 3) (Fin 3) ℝ :=
  !![(1/3 : ℝ), 0, 0; 1/3, 1/2, 0; 1/3, 1/2, 1]

/-- Nonnegative barycentric coefficients of an increasing chain. -/
def chainWeights (x : Fin 3 → ℝ) : Fin 3 → ℝ :=
  ![3 * x 0, 2 * (x 1 - x 0), x 2 - x 1]

theorem chainWeights_nonneg {x : Fin 3 → ℝ}
    (h0 : 0 ≤ x 0) (h01 : x 0 ≤ x 1) (h12 : x 1 ≤ x 2) :
    ∀ j, 0 ≤ chainWeights x j := by
  intro j
  fin_cases j <;> simp [chainWeights] <;> linarith

theorem chainWeights_sum (x : Fin 3 → ℝ) :
    ∑ j, chainWeights x j = ∑ j, x j := by
  simp [Fin.sum_univ_succ, chainWeights]
  ring

theorem chainMatrix_mul_weights (x : Fin 3 → ℝ) :
    chainMatrix.mulVec (chainWeights x) = x := by
  ext i
  fin_cases i <;> simp [chainMatrix, chainWeights, Matrix.mulVec,
    dotProduct, Fin.sum_univ_succ]

theorem chainMatrix_det : chainMatrix.det = (1/6 : ℝ) := by
  norm_num [chainMatrix, Matrix.det_fin_three]

theorem chainMatrix_column_sum (j : Fin 3) :
    ∑ i, chainMatrix i j = 1 := by
  fin_cases j <;> norm_num [chainMatrix, Fin.sum_univ_succ]

theorem chainMatrix_nonneg (i j : Fin 3) : 0 ≤ chainMatrix i j := by
  fin_cases i <;> fin_cases j <;> norm_num [chainMatrix]

theorem chainMatrix_ordered (j : Fin 3) :
    chainMatrix 0 j ≤ chainMatrix 1 j ∧
    chainMatrix 1 j ≤ chainMatrix 2 j := by
  fin_cases j <;> norm_num [chainMatrix]

/-- The 24 barycentric coordinates, arranged as eight ordered chains. -/
abbrev ChainCoordinate := Fin 8 × Fin 3

/-- The actual 24 source vertices in these coordinates. -/
def sourceVertex (v i : ChainCoordinate) : ℝ :=
  if i.1 = v.1 then chainMatrix i.2 v.2 else 0

/-- The standard 23-simplex in its 24 barycentric coordinates. -/
def barycentricSimplex : Set (ChainCoordinate → ℝ) :=
  {x | (∀ i, 0 ≤ x i) ∧ ∑ i, x i = 1}

/-- Its intersection with all sixteen internal ordering halfspaces. -/
def orderedSource : Set (ChainCoordinate → ℝ) :=
  {x | x ∈ barycentricSimplex ∧
    ∀ r : Fin 8, x (r, 0) ≤ x (r, 1) ∧ x (r, 1) ≤ x (r, 2)}

theorem sourceVertex_mem_orderedSource (v : ChainCoordinate) :
    sourceVertex v ∈ orderedSource := by
  constructor
  · constructor
    · intro i
      simp only [sourceVertex]
      split_ifs
      · exact chainMatrix_nonneg _ _
      · exact le_rfl
    · rw [Fintype.sum_prod_type, Finset.sum_eq_single v.1]
      · simpa [sourceVertex] using chainMatrix_column_sum v.2
      · intro r hr hne
        simp [sourceVertex, hne]
      · simp
  · intro r
    by_cases hr : r = v.1
    · simpa [sourceVertex, hr] using chainMatrix_ordered v.2
    · simp [sourceVertex, hr]

theorem orderedSource_convex : Convex ℝ orderedSource := by
  intro x hx y hy a b ha hb hab
  constructor
  · constructor
    · intro i
      exact add_nonneg (mul_nonneg ha (hx.1.1 i)) (mul_nonneg hb (hy.1.1 i))
    · change (∑ i, (a * x i + b * y i)) = 1
      rw [Finset.sum_add_distrib, ← Finset.mul_sum, ← Finset.mul_sum,
        hx.1.2, hy.1.2, mul_one, mul_one, hab]
  · intro r
    exact ⟨add_le_add (mul_le_mul_of_nonneg_left (hx.2 r).1 ha)
        (mul_le_mul_of_nonneg_left (hy.2 r).1 hb),
      add_le_add (mul_le_mul_of_nonneg_left (hx.2 r).2 ha)
        (mul_le_mul_of_nonneg_left (hy.2 r).2 hb)⟩

/-- Explicit barycentric weights for the source's 24 vertices. -/
def sourceWeights (x : ChainCoordinate → ℝ) (v : ChainCoordinate) : ℝ :=
  chainWeights (fun j => x (v.1, j)) v.2

theorem sourceWeights_nonneg {x : ChainCoordinate → ℝ}
    (hx : x ∈ orderedSource) (v : ChainCoordinate) :
    0 ≤ sourceWeights x v := by
  apply chainWeights_nonneg (hx.1.1 (v.1, 0)) (hx.2 v.1).1 (hx.2 v.1).2

theorem sourceWeights_sum {x : ChainCoordinate → ℝ}
    (hx : x ∈ orderedSource) : ∑ v, sourceWeights x v = 1 := by
  calc
    _ = ∑ r : Fin 8, ∑ j : Fin 3, x (r, j) := by
      simp only [Fintype.sum_prod_type, sourceWeights, chainWeights_sum]
    _ = 1 := by simpa only [Fintype.sum_prod_type] using hx.1.2

theorem source_reconstruction (x : ChainCoordinate → ℝ) (i : ChainCoordinate) :
    ∑ v, sourceWeights x v * sourceVertex v i = x i := by
  rw [Fintype.sum_prod_type]
  have hs : (∑ r : Fin 8, ∑ j : Fin 3,
      sourceWeights x (r, j) * sourceVertex (r, j) i) =
      ∑ j : Fin 3, sourceWeights x (i.1, j) * chainMatrix i.2 j := by
    rw [Finset.sum_eq_single i.1]
    · simp [sourceVertex]
    · intro r hr hne
      simp [sourceVertex, Ne.symm hne]
    · simp
  rw [hs]
  simpa [sourceWeights, Matrix.mulVec, dotProduct, mul_comm] using
    congrFun (chainMatrix_mul_weights (fun j => x (i.1, j))) i.2

theorem orderedSource_eq_convexHull :
    orderedSource = convexHull ℝ (Set.range sourceVertex) := by
  apply Set.Subset.antisymm
  · intro x hx
    apply mem_convexHull_of_exists_fintype (sourceWeights x) sourceVertex
      (sourceWeights_nonneg hx) (sourceWeights_sum hx) (fun v => Set.mem_range_self v)
    ext i
    simpa only [Finset.sum_apply, Pi.smul_apply, smul_eq_mul] using source_reconstruction x i
  · apply convexHull_min
    · rintro x ⟨v, rfl⟩
      exact sourceVertex_mem_orderedSource v
    · exact orderedSource_convex

/-- The source's matrix in barycentric coordinates. -/
def sourceMatrix : Matrix ChainCoordinate ChainCoordinate ℝ :=
  fun i v => sourceVertex v i

theorem sourceMatrix_eq_blockDiagonal :
    sourceMatrix = Matrix.reindex (Equiv.prodComm (Fin 3) (Fin 8))
      (Equiv.prodComm (Fin 3) (Fin 8))
      (Matrix.blockDiagonal (fun _ : Fin 8 => chainMatrix)) := by
  ext i v
  rfl

theorem sourceMatrix_det : sourceMatrix.det = (1/6 : ℝ)^8 := by
  rw [sourceMatrix_eq_blockDiagonal, Matrix.det_reindex_self, Matrix.det_blockDiagonal]
  simp [chainMatrix_det]

theorem sourceVertices_linearIndependent : LinearIndependent ℝ sourceVertex := by
  have hd : sourceMatrix.det ≠ 0 := by rw [sourceMatrix_det]; norm_num
  exact Matrix.linearIndependent_cols_of_det_ne_zero hd

theorem sourceVertices_affineIndependent : AffineIndependent ℝ sourceVertex :=
  sourceVertices_linearIndependent.affineIndependent

/-- The arithmetic average of the 24 source vertices. -/
def sourceVertexAverage (i : ChainCoordinate) : ℝ :=
  (∑ v : ChainCoordinate, sourceVertex v i) / 24

def sourceCenter (i : ChainCoordinate) : ℝ :=
  ![(1/72 : ℝ), 5/144, 11/144] i.2

theorem sourceVertexAverage_eq (i : ChainCoordinate) :
    sourceVertexAverage i = sourceCenter i := by
  rcases i with ⟨r, j⟩
  unfold sourceVertexAverage
  rw [Fintype.sum_prod_type, Finset.sum_eq_single r]
  · fin_cases j <;> norm_num [sourceVertex, sourceCenter,
      Fin.sum_univ_succ, chainMatrix]
  · intro t ht hne
    simp [sourceVertex, Ne.symm hne]
  · simp

theorem sourceCenter_min (i : ChainCoordinate) :
    (1/72 : ℝ) ≤ sourceCenter i := by
  rcases i with ⟨r, j⟩
  fin_cases j <;> norm_num [sourceCenter]

theorem sourceCenter_internal_first (r : Fin 8) :
    sourceCenter (r, 0) - sourceCenter (r, 1) = -(1/48 : ℝ) := by
  norm_num [sourceCenter]

theorem sourceCenter_internal_second (r : Fin 8) :
    sourceCenter (r, 1) - sourceCenter (r, 2) = -(1/24 : ℝ) := by
  norm_num [sourceCenter]

theorem sourceCenter_cross_edge (r t : Fin 8) :
    sourceCenter (r, 2) - sourceCenter (t, 0) = (1/16 : ℝ) := by
  norm_num [sourceCenter]

/-- Every point of an ordered source has nonpositive internal cut scores. -/
theorem orderedSource_internal_nonpos {x : ChainCoordinate → ℝ}
    (hx : x ∈ orderedSource) (r : Fin 8) :
    x (r, 0) - x (r, 1) ≤ 0 ∧ x (r, 1) - x (r, 2) ≤ 0 := by
  obtain ⟨_, horder⟩ := hx
  obtain ⟨h01, h12⟩ := horder r
  constructor <;> linarith

/-- The equal-coordinate point attains zero on every internal cut. -/
theorem equal_coordinates_mem_orderedSource :
    (fun _ : ChainCoordinate => (1/24 : ℝ)) ∈ orderedSource := by
  constructor
  · constructor
    · intro i; norm_num
    · norm_num [Fintype.card_prod]
  · intro r; constructor <;> rfl

/-- Centered contraction used in the counterexample. -/
def contractedPoint (x : ChainCoordinate → ℝ) (i : ChainCoordinate) : ℝ :=
  (1 - (103/104 : ℝ)) * sourceCenter i + (103/104 : ℝ) * x i

theorem contractedPoint_positive {x : ChainCoordinate → ℝ}
    (hx : x ∈ orderedSource) (i : ChainCoordinate) :
    (1/7488 : ℝ) ≤ contractedPoint x i := by
  have hc := sourceCenter_min i
  have hx0 := hx.1.1 i
  dsimp [contractedPoint]
  nlinarith

theorem contractedPoint_internal_first {x : ChainCoordinate → ℝ}
    (hx : x ∈ orderedSource) (r : Fin 8) :
    contractedPoint x (r, 0) - contractedPoint x (r, 1) ≤ -(1/4992 : ℝ) := by
  have h := (orderedSource_internal_nonpos hx r).1
  norm_num [contractedPoint, sourceCenter]
  linarith

theorem contractedPoint_internal_second {x : ChainCoordinate → ℝ}
    (hx : x ∈ orderedSource) (r : Fin 8) :
    contractedPoint x (r, 1) - contractedPoint x (r, 2) ≤ -(1/4992 : ℝ) := by
  have h := (orderedSource_internal_nonpos hx r).2
  norm_num [contractedPoint, sourceCenter]
  linarith

/-- A cyclic coordinate chart for each of the three shifted chain partitions. -/
def cyclicCoordinate (a : Fin 3) (j : Fin 24) : ChainCoordinate :=
  finProdFinEquiv.symm (j + ⟨a.val, by omega⟩)

/-- The eight chain-ending cuts of each source. -/
def isRoot (a : Fin 3) (j : Fin 24) : Prop := (cyclicCoordinate a j).2 = 2

instance (a : Fin 3) (j : Fin 24) : Decidable (isRoot a j) :=
  inferInstanceAs (Decidable ((cyclicCoordinate a j).2 = 2))

theorem cyclicCoordinate_bijective : ∀ a : Fin 3, Function.Bijective (cyclicCoordinate a) := by
  decide

theorem each_cut_has_one_root : ∀ j : Fin 24, ∃! a : Fin 3, isRoot a j := by
  simp only [ExistsUnique]
  decide

theorem each_source_has_eight_roots : ∀ a : Fin 3,
    (Finset.univ.filter (isRoot a)).card = 8 := by
  decide

theorem missed_edge_is_internal : ∀ a : Fin 3, ∀ j : Fin 24, ¬ isRoot a j →
    ∃ r : Fin 8,
      (cyclicCoordinate a j = (r, 0) ∧ cyclicCoordinate a (j + 1) = (r, 1)) ∨
      (cyclicCoordinate a j = (r, 1) ∧ cyclicCoordinate a (j + 1) = (r, 2)) := by
  decide

/-- Every missed cyclic cut has the same certified strict margin after contraction. -/
theorem contracted_missed_cyclic_cut {x : ChainCoordinate → ℝ}
    (hx : x ∈ orderedSource) (a : Fin 3) (j : Fin 24) (hj : ¬ isRoot a j) :
    contractedPoint x (cyclicCoordinate a j) -
      contractedPoint x (cyclicCoordinate a (j + 1)) ≤ -(1/4992 : ℝ) := by
  obtain ⟨r, h | h⟩ := missed_edge_is_internal a j hj
  · rw [h.1, h.2]
    exact contractedPoint_internal_first hx r
  · rw [h.1, h.2]
    exact contractedPoint_internal_second hx r


/-- The columns except the last are replaced by their differences from the last. -/
def columnDifferences {n : ℕ} (M : Matrix (Fin (n+1)) (Fin (n+1)) ℝ) :
    Matrix (Fin (n+1)) (Fin (n+1)) ℝ :=
  fun i j => M i j + (if j = Fin.last n then 0 else -1) * M i (Fin.last n)

theorem columnDifferences_det {n : ℕ} (M : Matrix (Fin (n+1)) (Fin (n+1)) ℝ) :
    (columnDifferences M).det = M.det := by
  rw [← Matrix.det_transpose, ← Matrix.det_transpose M]
  apply Matrix.det_eq_of_forall_row_eq_smul_add_const
    (fun j => if j = Fin.last n then 0 else -1) (Fin.last n)
  · simp
  · intro i j
    rfl

/-- The linear part of the affine chart after deleting the last barycentric row. -/
def chartMatrix {n : ℕ} (M : Matrix (Fin (n+1)) (Fin (n+1)) ℝ) :
    Matrix (Fin n) (Fin n) ℝ :=
  fun i j => M i.castSucc j.castSucc - M i.castSucc (Fin.last n)

/-- For column-stochastic matrices the ambient determinant is exactly the
23-dimensional affine chart determinant. This is dimension independent. -/
theorem chartMatrix_det {n : ℕ} (M : Matrix (Fin (n+1)) (Fin (n+1)) ℝ)
    (hM : ∀ j, ∑ i, M i j = 1) :
    (chartMatrix M).det = M.det := by
  have hzero : ∀ j ≠ Fin.last n, ∑ i, columnDifferences M i j = 0 := by
    intro j hj
    simp [columnDifferences, hj, Finset.sum_add_distrib, Finset.sum_neg_distrib, hM]
  have hlast : ∑ i, columnDifferences M i (Fin.last n) = 1 := by
    simpa [columnDifferences] using hM (Fin.last n)
  have hd := Matrix.det_eq_sum_column_mul_submatrix_succAbove_succAbove_det
    (columnDifferences M) (Fin.last n) (Fin.last n) hzero
  have hsign : (-1 : ℝ) ^ ((Fin.last n).val + (Fin.last n).val) = 1 := by
    exact (show Even (n+n) from ⟨n, rfl⟩).neg_one_pow
  rw [columnDifferences_det, hsign, hlast, one_mul, one_mul] at hd
  convert hd.symm using 1
  congr 1
  ext i j
  simp [chartMatrix, columnDifferences, Matrix.submatrix_apply, Fin.succAbove_last, sub_eq_add_neg]

/-- The ordinary standard n-simplex, without centering. -/
def standardSimplex (n : ℕ) : Set (Fin n → ℝ) :=
  convexHull ℝ (insert 0 (Set.range (fun j : Fin n => Pi.single j (1 : ℝ))))

/-- The simplex with column vertices, expressed in the first n coordinates. -/
def chartSimplex {n : ℕ} (M : Matrix (Fin (n+1)) (Fin (n+1)) ℝ) : Set (Fin n → ℝ) :=
  convexHull ℝ (Set.range (fun j i => M (Fin.castSucc i) j))

theorem chart_vertex_range {n : ℕ} (M : Matrix (Fin (n+1)) (Fin (n+1)) ℝ) :
    Set.range (fun j i => M (Fin.castSucc i) j) =
      (fun x => (fun i => M i.castSucc (Fin.last n)) + x) ''
        (insert 0 (Set.range (chartMatrix M).col)) := by
  ext x
  constructor
  · rintro ⟨j, rfl⟩
    rcases Fin.eq_castSucc_or_eq_last j with ⟨j, rfl⟩ | rfl
    · refine ⟨(chartMatrix M).col j, Set.mem_insert_of_mem _ (Set.mem_range_self j), ?_⟩
      ext i
      simp [chartMatrix, Matrix.col_apply]
    · exact ⟨0, Set.mem_insert _ _, by simp⟩
  · rintro ⟨y, hy, rfl⟩
    rcases hy with rfl | ⟨j, rfl⟩
    · exact ⟨Fin.last n, by simp⟩
    · refine ⟨j.castSucc, ?_⟩
      ext i
      simp [chartMatrix, Matrix.col_apply]

theorem chartSimplex_eq_affine_image {n : ℕ}
    (M : Matrix (Fin (n+1)) (Fin (n+1)) ℝ) :
    chartSimplex M =
      (fun x => (fun i => M i.castSucc (Fin.last n)) + x) ''
        ((Matrix.toLin' (chartMatrix M)) '' standardSimplex n) := by
  rw [standardSimplex, LinearMap.image_convexHull]
  have hlin : (Matrix.toLin' (chartMatrix M)) ''
      insert 0 (Set.range (fun j : Fin n => Pi.single j (1 : ℝ))) =
      insert 0 (Set.range (chartMatrix M).col) := by
    simp only [Set.image_insert_eq, map_zero, ← Set.range_comp, Function.comp_def,
      Matrix.toLin'_apply, Matrix.mulVec_single_one]
  rw [hlin]
  unfold chartSimplex
  rw [chart_vertex_range]
  exact (AffineEquiv.constVAdd ℝ (Fin n → ℝ)
    (fun i => M i.castSucc (Fin.last n))).toAffineMap.image_convexHull _ |>.symm

/-- A volume-preserving translation, written explicitly as a set image. -/
theorem volume_translate {n : ℕ} (p : Fin n → ℝ) (s : Set (Fin n → ℝ)) :
    MeasureTheory.volume ((fun x => p + x) '' s) = MeasureTheory.volume s := by
  have hs : (fun x => p + x) '' s = (fun x => -p + x) ⁻¹' s := by
    ext x
    constructor
    · rintro ⟨y, hy, rfl⟩
      simpa using hy
    · intro hx
      exact ⟨-p + x, hx, by simp⟩
  rw [hs]
  exact MeasureTheory.measure_preimage_add MeasureTheory.volume (-p) s

/-- The actual n-dimensional volume ratio for a column-stochastic matrix.
No Hausdorff measure in the ambient (n+1)-coordinate space is used. -/
theorem volume_chartSimplex {n : ℕ}
    (M : Matrix (Fin (n+1)) (Fin (n+1)) ℝ) (hM : ∀ j, ∑ i, M i j = 1) :
    MeasureTheory.volume (chartSimplex M) =
      ENNReal.ofReal |M.det| * MeasureTheory.volume (standardSimplex n) := by
  rw [chartSimplex_eq_affine_image, volume_translate,
    MeasureTheory.Measure.addHaar_image_linearMap, LinearMap.det_toLin', chartMatrix_det M hM]

/-- The three cyclic source vertex matrices in the original 24 coordinates. -/
def cyclicSourceMatrix (a : Fin 3) : Matrix (Fin 24) (Fin 24) ℝ :=
  fun i v => sourceVertex (finProdFinEquiv.symm v) (cyclicCoordinate a i)

/-- The cyclic chart is a genuine permutation of all 24 coordinates. -/
def cyclicCoordinateEquiv (a : Fin 3) : Fin 24 ≃ ChainCoordinate :=
  Equiv.ofBijective (cyclicCoordinate a) (cyclicCoordinate_bijective a)

theorem cyclicSourceMatrix_abs_det (a : Fin 3) :
    |(cyclicSourceMatrix a).det| = (1/6 : ℝ)^8 := by
  have h := Matrix.abs_det_submatrix_equiv_equiv
    (cyclicCoordinateEquiv a) (finProdFinEquiv : ChainCoordinate ≃ Fin 24).symm sourceMatrix
  change |(cyclicSourceMatrix a).det| = |sourceMatrix.det| at h
  rw [h, sourceMatrix_det, abs_of_pos]
  positivity

theorem cyclicSourceMatrix_column_sum (a : Fin 3) (j : Fin 24) :
    ∑ i, cyclicSourceMatrix a i j = 1 := by
  change ∑ i, sourceVertex (finProdFinEquiv.symm j) (cyclicCoordinateEquiv a i) = 1
  rw [Equiv.sum_comp]
  exact (sourceVertex_mem_orderedSource (finProdFinEquiv.symm j)).1.2

theorem cyclicSource_volume (a : Fin 3) :
    MeasureTheory.volume (chartSimplex (cyclicSourceMatrix a)) =
      ENNReal.ofReal ((1/6 : ℝ)^8) * MeasureTheory.volume (standardSimplex 23) := by
  rw [volume_chartSimplex _ (cyclicSourceMatrix_column_sum a), cyclicSourceMatrix_abs_det]


/-- The explicitly chosen center lies in its source simplex. -/
theorem sourceCenter_mem_orderedSource : sourceCenter ∈ orderedSource := by
  constructor
  · constructor
    · intro i
      exact le_trans (by norm_num) (sourceCenter_min i)
    · norm_num [sourceCenter, Fintype.sum_prod_type, Fin.sum_univ_succ]
  · intro r
    norm_num [sourceCenter]

theorem barycentricSimplex_coord_le_one {u : ChainCoordinate → ℝ}
    (hu : u ∈ barycentricSimplex) (i : ChainCoordinate) : u i ≤ 1 := by
  calc
    u i ≤ ∑ j, u j := Finset.single_le_sum (fun j _ => hu.1 j) (Finset.mem_univ i)
    _ = 1 := hu.2

theorem contractedPoint_mem_simplex {x : ChainCoordinate → ℝ}
    (hx : x ∈ orderedSource) : contractedPoint x ∈ barycentricSimplex := by
  constructor
  · intro i
    exact le_trans (by norm_num) (contractedPoint_positive hx i)
  · simp only [contractedPoint, Finset.sum_add_distrib, ← Finset.mul_sum,
      sourceCenter_mem_orderedSource.1.2, hx.1.2]
    norm_num

/-- A source point plus one half of a simplex scaled by 1/10000 stays
in the middle simplex. Offsets are expressed in centered barycentric coordinates. -/
theorem contractedPoint_add_half_small_simplex {x u : ChainCoordinate → ℝ}
    (hx : x ∈ orderedSource) (hu : u ∈ barycentricSimplex) :
    (fun i => contractedPoint x i + (1/20000 : ℝ) * (u i - 1/24)) ∈
      barycentricSimplex := by
  constructor
  · intro i
    have hp := contractedPoint_positive hx i
    have hu0 := hu.1 i
    linarith
  · simp only [Finset.sum_add_distrib, ← Finset.mul_sum, Finset.sum_sub_distrib,
      (contractedPoint_mem_simplex hx).2, hu.2, Finset.sum_const, Finset.card_univ,
      Fintype.card_prod, Fintype.card_fin, nsmul_eq_mul]
    norm_num

/-- The preimage under the source contraction of a center plus twice a
simplex scaled by 1/10000. -/
def sourceCenterPullback (u : ChainCoordinate → ℝ) (i : ChainCoordinate) : ℝ :=
  sourceCenter i + (13/64375 : ℝ) * (u i - 1/24)

theorem sourceCenterPullback_mem {u : ChainCoordinate → ℝ}
    (hu : u ∈ barycentricSimplex) : sourceCenterPullback u ∈ orderedSource := by
  constructor
  · constructor
    · intro i
      have hc := sourceCenter_min i
      have hu0 := hu.1 i
      dsimp [sourceCenterPullback]
      linarith
    · simp only [sourceCenterPullback, Finset.sum_add_distrib, ← Finset.mul_sum,
        Finset.sum_sub_distrib, sourceCenter_mem_orderedSource.1.2, hu.2,
        Finset.sum_const, Finset.card_univ, Fintype.card_prod, Fintype.card_fin,
        nsmul_eq_mul]
      norm_num
  · intro r
    have hu0 := hu.1 (r, 0)
    have hu1 := hu.1 (r, 1)
    have hu2 := hu.1 (r, 2)
    have hU0 := barycentricSimplex_coord_le_one hu (r, 0)
    have hU1 := barycentricSimplex_coord_le_one hu (r, 1)
    norm_num [sourceCenterPullback, sourceCenter]
    constructor <;> linarith

theorem contracted_sourceCenterPullback (u : ChainCoordinate → ℝ) :
    contractedPoint (sourceCenterPullback u) =
      (fun i => sourceCenter i + (1/5000 : ℝ) * (u i - 1/24)) := by
  ext i
  dsimp [contractedPoint, sourceCenterPullback]
  ring

/-- The exact existential form of the second containment: c+2A lies in P. -/
theorem sourceCenter_add_twice_small_simplex {u : ChainCoordinate → ℝ}
    (hu : u ∈ barycentricSimplex) :
    ∃ x ∈ orderedSource, contractedPoint x =
      (fun i => sourceCenter i + (1/5000 : ℝ) * (u i - 1/24)) :=
  ⟨sourceCenterPullback u, sourceCenterPullback_mem hu,
    contracted_sourceCenterPullback u⟩

end

end SharpOC.SourceGeometry
