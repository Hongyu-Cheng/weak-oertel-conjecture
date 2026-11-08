import SharpOC.SelectorSources
import SharpOC.Selector17Arithmetic

/-! The cyclic cuts and source simplices for the selector in dimension 18. -/

noncomputable section
open Set MeasureTheory
open scoped ENNReal

namespace SharpOC.Selector17

open SelectorSources (E B basis lambda active free coordinates B_lambda_nonneg B_lambda_le_one
  B_compact B_convex source sourceBasis source_eq_hull source_volume sourceBasis_weights
  mem_source_iff_weights mem_B_iff_coordinates forall_fin_three coordinate_eq_null)

def f (j : Fin 3) : E →L[ℝ] ℝ :=
  ((lambda (active j)).linear - a • (lambda (active (j + 1))).linear -
    (1 - a) • (lambda (active (j + 2))).linear).toContinuousLinearMap

theorem f_apply (j : Fin 3) (x : E) :
    f j x = lambda (active j) x - a * lambda (active (j + 1)) x -
      (1 - a) * lambda (active (j + 2)) x := by
  have h (i : Fin 6) := congrFun (lambda i).decomp x
  simp only [Pi.add_apply, SelectorSources.lambda_zero] at h
  change (lambda (active j)).linear x - a * (lambda (active (j + 1))).linear x -
    (1 - a) * (lambda (active (j + 2))).linear x = _
  have h0 := h (active j)
  have h1 := h (active (j + 1))
  have h2 := h (active (j + 2))
  rw [h0, h1, h2]
  ring

theorem f_nonzero (j : Fin 3) : f j ≠ 0 := by
  intro hz
  have h := congrArg (fun g : E →L[ℝ] ℝ => g (basis (active j))) hz
  have h1 : active (j + 1) ≠ active j := by fin_cases j <;> decide
  have h2 : active (j + 2) ≠ active j := by fin_cases j <;> decide
  rw [f_apply] at h
  norm_num [lambda, basis.coord_apply_ne h1, basis.coord_apply_ne h2] at h

theorem B_f_bounds {x : E} (hx : x ∈ B) (j : Fin 3) : -1 ≤ f j x ∧ f j x ≤ 1 := by
  rw [f_apply]
  constructor <;> unfold a <;>
    linarith [B_lambda_nonneg hx (active j), B_lambda_le_one hx (active j),
      B_lambda_nonneg hx (active (j + 1)), B_lambda_le_one hx (active (j + 1)),
      B_lambda_nonneg hx (active (j + 2)), B_lambda_le_one hx (active (j + 2))]

theorem f_abs_le_one {x : E} (hx : x ∈ B) (j : Fin 3) : |f j x| ≤ 1 :=
  abs_le.mpr (B_f_bounds hx j)

theorem f_sum (x : E) : ∑ j, f j x = 0 := by
  rw [Fin.sum_univ_three]
  simp only [f_apply]
  change (lambda (active 0) x - a * lambda (active 1) x -
      (1 - a) * lambda (active 2) x) +
    (lambda (active 1) x - a * lambda (active 2) x -
      (1 - a) * lambda (active 0) x) +
    (lambda (active 2) x - a * lambda (active 0) x -
      (1 - a) * lambda (active 1) x) = 0
  ring

theorem cyclic_cuts_cover (x : E) : ∃ j, 0 ≤ f j x := by
  by_contra h
  push Not at h
  have hs := Finset.sum_lt_sum_of_nonempty Finset.univ_nonempty (fun j _ => h j)
  simp [f_sum] at hs

def T (j : Fin 3) : Set E :=
  B ∩ ({x | f (j + 1) x ≤ 0} ∩ {x | f (j + 2) x ≤ 0})

theorem T_subset_B (j : Fin 3) : T j ⊆ B := inter_subset_left

theorem T_f_nonpos (j : Fin 3) {x : E} (hx : x ∈ T j) (i : Fin 3) (hi : i ≠ j) :
    f i x ≤ 0 := by
  have h : ∀ k l : Fin 3, k ≠ l → k = l + 1 ∨ k = l + 2 := by decide
  rcases h i j hi with rfl | rfl
  · exact hx.2.1
  · exact hx.2.2

theorem T_f_nonneg (j : Fin 3) {x : E} (hx : x ∈ T j) : 0 ≤ f j x := by
  have h := f_sum x
  rw [Fin.sum_univ_three] at h
  have h1 : f (j + 1) x ≤ 0 := hx.2.1
  have h2 : f (j + 2) x ≤ 0 := hx.2.2
  fin_cases j <;> norm_num at h1 h2 ⊢ <;> linarith

theorem T_compact (j : Fin 3) : IsCompact (T j) :=
  B_compact.inter_right
    ((isClosed_le (f (j + 1)).continuous continuous_const).inter
      (isClosed_le (f (j + 2)).continuous continuous_const))

theorem T_convex (j : Fin 3) : Convex ℝ (T j) :=
  B_convex.inter ((convex_halfSpace_le (f (j + 1)).toLinearMap.isLinear 0).inter
    (convex_halfSpace_le (f (j + 2)).toLinearMap.isLinear 0))

theorem T_nonempty (j : Fin 3) : (T j).Nonempty :=
  ⟨0, interior_subset SelectorSources.zero_mem_interior_B, by simp, by simp⟩

private theorem scores (j : Fin 3) (x : E) :
    f j x = coordinates j x 0 - a * coordinates j x 1 - (1 - a) * coordinates j x 2 ∧
    f (j + 1) x =
      coordinates j x 1 - a * coordinates j x 2 - (1 - a) * coordinates j x 0 ∧
    f (j + 2) x =
      coordinates j x 2 - a * coordinates j x 0 - (1 - a) * coordinates j x 1 := by
  have h11 : (1 : Fin 3) + 1 = 2 := by decide
  have h12 : (1 : Fin 3) + 2 = 0 := by decide
  have h21 : (2 : Fin 3) + 1 = 0 := by decide
  have h22 : (2 : Fin 3) + 2 = 1 := by decide
  simp [f_apply, coordinates, add_assoc, h11, h12, h21, h22]

private def uMat : Matrix (Fin 3) (Fin 3) ℝ :=
  !![1, 1 / 3, 1 / (1 + a); 0, 1 / 3, 0; 0, 1 / 3, a / (1 + a)]

private def pMat : Matrix (Fin 3) (Fin 3) ℝ :=
  !![1, 1 / 3, 1 / (2 - a); 0, 1 / 3, (1 - a) / (2 - a); 0, 1 / 3, 0]

private def capMat : Matrix (Fin 3) (Fin 3) ℝ :=
  !![1, a / (1 + a), (1 - a) / (2 - a); 0, 1 / (1 + a), 0; 0, 0, 1 / (2 - a)]

private theorem uMat_sum (k : Fin 3) : ∑ i, uMat i k = 1 := by
  fin_cases k <;> norm_num [uMat, Fin.sum_univ_three, a]

private theorem pMat_sum (k : Fin 3) : ∑ i, pMat i k = 1 := by
  fin_cases k <;> norm_num [pMat, Fin.sum_univ_three, a]

private theorem capMat_sum (k : Fin 3) : ∑ i, capMat i k = 1 := by
  fin_cases k <;> norm_num [capMat, Fin.sum_univ_three, a]

private theorem uMat_det : uMat.det = theta := by
  norm_num [uMat, Matrix.det_fin_three, theta, a]

private theorem pMat_det : pMat.det = -phi := by
  norm_num [pMat, Matrix.det_fin_three, phi, a]

private theorem capMat_det : capMat.det = beta := by
  norm_num [capMat, Matrix.det_fin_three, beta, a]

private theorem uMat_nonsingular : uMat.det ≠ 0 := by rw [uMat_det]; exact theta_pos.ne'
private theorem pMat_nonsingular : pMat.det ≠ 0 := by rw [pMat_det]; exact neg_ne_zero.mpr phi_pos.ne'
private theorem capMat_nonsingular : capMat.det ≠ 0 := by rw [capMat_det]; exact beta_pos.ne'

/-- The simplex with active vertices e_j, the active centroid, and
the edge point on e_j–e_(j+2). The free vertices agree with those of B. -/
def U (j : Fin 3) : Set E := source j uMat

/-- The simplex across the common facet of U, with edge point on e_j–e_(j+1). -/
def P (j : Fin 3) : Set E := source j pMat

def uBasis (j : Fin 3) : AffineBasis (Fin 6) ℝ E :=
  sourceBasis j uMat uMat_sum uMat_nonsingular

def pBasis (j : Fin 3) : AffineBasis (Fin 6) ℝ E :=
  sourceBasis j pMat pMat_sum pMat_nonsingular

theorem U_eq_hull (j : Fin 3) : U j = convexHull ℝ (range (uBasis j)) :=
  source_eq_hull _ _ _ _

theorem P_eq_hull (j : Fin 3) : P j = convexHull ℝ (range (pBasis j)) :=
  source_eq_hull _ _ _ _

theorem U_volume (j : Fin 3) : volume (U j) = ENNReal.ofReal theta * volume B := by
  rw [U, source_volume _ _ uMat_sum, uMat_det, abs_of_pos theta_pos]

theorem P_volume (j : Fin 3) : volume (P j) = ENNReal.ofReal phi * volume B := by
  rw [P, source_volume _ _ pMat_sum, pMat_det, abs_of_neg (neg_neg_of_pos phi_pos), neg_neg]

private def uWeights (x : Fin 3 → ℝ) : Fin 3 → ℝ :=
  ![x 0 + ((1 - a) / a) * x 1 - (1 / a) * x 2, 3 * x 1, ((1 + a) / a) * (x 2 - x 1)]

private def pWeights (x : Fin 3 → ℝ) : Fin 3 → ℝ :=
  ![x 0 - (1 / (1 - a)) * x 1 + (a / (1 - a)) * x 2, 3 * x 2,
    ((2 - a) / (1 - a)) * (x 1 - x 2)]

private theorem uWeights_inv (x : Fin 3 → ℝ) : uMat.mulVec (uWeights x) = x := by
  ext i
  fin_cases i <;> norm_num [uMat, uWeights, Matrix.mulVec, dotProduct, Fin.sum_univ_three, a] <;> ring

private theorem pWeights_inv (x : Fin 3 → ℝ) : pMat.mulVec (pWeights x) = x := by
  ext i
  fin_cases i <;> norm_num [pMat, pWeights, Matrix.mulVec, dotProduct, Fin.sum_univ_three, a] <;> ring

theorem U_eq_region (j : Fin 3) :
    U j = T j ∩ {x | coordinates j x 1 ≤ coordinates j x 2} := by
  ext x
  rw [U, mem_source_iff_weights _ _ uMat_sum uMat_nonsingular uWeights uWeights_inv]
  change _ ↔ (x ∈ B ∧ f (j + 1) x ≤ 0 ∧ f (j + 2) x ≤ 0) ∧ _
  rw [mem_B_iff_coordinates j x, (scores j x).2.1, (scores j x).2.2]
  simp only [uWeights, forall_fin_three, Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.cons_val_two, Matrix.tail_cons, Matrix.head_cons]
  change _ ↔ _ ∧ coordinates j x 1 ≤ coordinates j x 2
  unfold a
  constructor
  · rintro ⟨hf, h0, h1, h2⟩
    exact ⟨⟨⟨hf, by linarith, by linarith, by linarith⟩, by linarith, by linarith⟩,
      by linarith⟩
  · rintro ⟨⟨⟨hf, h0, h1, h2⟩, h3, h4⟩, h12⟩
    exact ⟨hf, by linarith, by linarith, by linarith⟩

theorem P_eq_region (j : Fin 3) :
    P j = T j ∩ {x | coordinates j x 2 ≤ coordinates j x 1} := by
  ext x
  rw [P, mem_source_iff_weights _ _ pMat_sum pMat_nonsingular pWeights pWeights_inv]
  change _ ↔ (x ∈ B ∧ f (j + 1) x ≤ 0 ∧ f (j + 2) x ≤ 0) ∧ _
  rw [mem_B_iff_coordinates j x, (scores j x).2.1, (scores j x).2.2]
  simp only [pWeights, forall_fin_three, Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.cons_val_two, Matrix.tail_cons, Matrix.head_cons]
  change _ ↔ _ ∧ coordinates j x 2 ≤ coordinates j x 1
  unfold a
  constructor
  · rintro ⟨hf, h0, h1, h2⟩
    exact ⟨⟨⟨hf, by linarith, by linarith, by linarith⟩, by linarith, by linarith⟩,
      by linarith⟩
  · rintro ⟨⟨⟨hf, h0, h1, h2⟩, h3, h4⟩, h21⟩
    exact ⟨hf, by linarith, by linarith, by linarith⟩

theorem T_eq_union (j : Fin 3) : T j = U j ∪ P j := by
  rw [U_eq_region, P_eq_region, ← inter_union_distrib_left]
  suffices {x | coordinates j x 1 ≤ coordinates j x 2} ∪
      {x | coordinates j x 2 ≤ coordinates j x 1} = univ by rw [this, inter_univ]
  exact eq_univ_of_forall (fun x => le_total (coordinates j x 1) (coordinates j x 2))

theorem U_subset_T (j : Fin 3) : U j ⊆ T j := by
  rw [U_eq_region]
  exact inter_subset_left

theorem P_subset_T (j : Fin 3) : P j ⊆ T j := by
  rw [P_eq_region]
  exact inter_subset_left

theorem U_P_aedisjoint (j : Fin 3) : AEDisjoint volume (U j) (P j) := by
  rw [AEDisjoint, U_eq_region, P_eq_region]
  have hne : active (j + 1) ≠ active (j + 2) := by fin_cases j <;> decide
  apply measure_mono_null _ (coordinate_eq_null _ _ hne)
  rintro x ⟨⟨_, h12⟩, ⟨_, h21⟩⟩
  exact le_antisymm h12 h21

theorem P_compact (j : Fin 3) : IsCompact (P j) := by
  rw [P_eq_hull]
  exact (Set.finite_range (pBasis j)).isCompact_convexHull ℝ

theorem T_volume (j : Fin 3) : volume (T j) = ENNReal.ofReal (theta + phi) * volume B := by
  rw [T_eq_union, measure_union₀ (P_compact j).measurableSet.nullMeasurableSet
    (U_P_aedisjoint j), U_volume, P_volume, ← add_mul,
    ← ENNReal.ofReal_add theta_pos.le phi_pos.le]

private theorem cap_eq_region (j : Fin 3) :
    source j capMat = B ∩ {x | 0 ≤ f j x} := by
  ext x
  let w (z : Fin 3 → ℝ) : Fin 3 → ℝ :=
    ![z 0 - a * z 1 - (1 - a) * z 2, (1 + a) * z 1, (2 - a) * z 2]
  have hw (z : Fin 3 → ℝ) : capMat.mulVec (w z) = z := by
    ext i
    fin_cases i <;> norm_num [capMat, w, Matrix.mulVec, dotProduct, Fin.sum_univ_three, a] <;> ring
  rw [mem_source_iff_weights _ _ capMat_sum capMat_nonsingular w hw]
  change _ ↔ x ∈ B ∧ 0 ≤ f j x
  rw [mem_B_iff_coordinates j x, (scores j x).1]
  simp only [w, forall_fin_three, Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.cons_val_two, Matrix.tail_cons, Matrix.head_cons]
  unfold a
  constructor
  · rintro ⟨hf, h0, h1, h2⟩
    exact ⟨⟨hf, by linarith, by linarith, by linarith⟩, h0⟩
  · rintro ⟨⟨hf, h0, h1, h2⟩, h⟩
    exact ⟨hf, h, by linarith, by linarith⟩

theorem positive_cap_volume (j : Fin 3) :
    volume (B ∩ {x | 0 ≤ f j x}) = ENNReal.ofReal beta * volume B := by
  rw [← cap_eq_region, source_volume _ _ capMat_sum, capMat_det, abs_of_pos beta_pos]

theorem coord_u_eq_coord_p_add (j : Fin 3) (i : Fin 6) (x : E) :
    (uBasis j).coord i x = (if i = 2 then 0 else (pBasis j).coord i x) +
      s i * (pBasis j).coord 2 x := by
  have hu := sourceBasis_weights j uMat uMat_sum uMat_nonsingular uWeights uWeights_inv x
  have hp := sourceBasis_weights j pMat pMat_sum pMat_nonsingular pWeights pWeights_inv x
  have hu0 := hu.1 0
  have hu1 := hu.1 1
  have hu2 := hu.1 2
  have hp0 := hp.1 0
  have hp1 := hp.1 1
  have hp2 := hp.1 2
  change (uBasis j).coord 0 x = _ at hu0
  change (uBasis j).coord 1 x = _ at hu1
  change (uBasis j).coord 2 x = _ at hu2
  change (pBasis j).coord 0 x = _ at hp0
  change (pBasis j).coord 1 x = _ at hp1
  change (pBasis j).coord 2 x = _ at hp2
  have hf (k : Fin 3) : (uBasis j).coord (free k) x = (pBasis j).coord (free k) x :=
    (hu.2 k).trans (hp.2 k).symm
  fin_cases i <;> norm_num [s, a]
  · rw [hu0, hp0, hp2]
    norm_num [a, uWeights, pWeights]
    ring
  · rw [hu1, hp1, hp2]
    norm_num [a, uWeights, pWeights]
    ring
  · rw [hu2, hp2]
    norm_num [a, uWeights, pWeights]
    ring
  · exact hf 0
  · exact hf 1
  · exact hf 2

theorem uBasis_coord_pBasis_two (j : Fin 3) (i : Fin 6) :
    (uBasis j).coord i (pBasis j 2) = s i := by
  rw [coord_u_eq_coord_p_add, (pBasis j).coord_apply_eq]
  by_cases hi : i = 2
  · simp [hi]
  · simp [hi, (pBasis j).coord_apply_ne hi]

end SharpOC.Selector17
