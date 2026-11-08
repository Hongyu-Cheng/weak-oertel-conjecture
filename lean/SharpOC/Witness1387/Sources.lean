import SharpOC.BoxSources
import SharpOC.AffineSimplex
import SharpOC.Witness1387.SourcesVolume

/-! Continuous fibers and their cap volumes for the 1387-dimensional witness. -/

noncomputable section
open Set MeasureTheory
open scoped ENNReal

namespace SharpOC.Witness1387

abbrev E := Fin 1178 → ℝ
abbrev FreeSpace := Fin 1175 → ℝ

/-- The first three coordinates are active, and the others are free. -/
def split : E ≃L[ℝ] BoxSources.E0 × FreeSpace :=
  (ContinuousLinearEquiv.piCongrLeft ℝ (fun _ : Fin 1178 => ℝ)
    (finSumFinEquiv : Fin 3 ⊕ Fin 1175 ≃ Fin 1178)).symm.trans
    (ContinuousLinearEquiv.sumPiEquivProdPi ℝ (Fin 3) (Fin 1175) (fun _ => ℝ))

theorem split_measurePreserving : MeasurePreserving split volume volume := by
  exact (volume_measurePreserving_sumPiEquivProdPi (fun _ : Fin 3 ⊕ Fin 1175 => ℝ)).comp
    ((volume_measurePreserving_piCongrLeft (fun _ : Fin 1178 => ℝ)
      (finSumFinEquiv : Fin 3 ⊕ Fin 1175 ≃ Fin 1178)).symm _)

private theorem volume_split_preimage (S : Set (BoxSources.E0 × FreeSpace)) :
    volume (split ⁻¹' S) = volume S :=
  split_measurePreserving.measure_preimage_emb
    split.toHomeomorph.toMeasurableEquiv.measurableEmbedding S

def freeShift : FreeSpace := fun _ => -(1 / 1176 : ℝ)
def freeBasis : AffineBasis (Fin 1176) ℝ FreeSpace :=
  freeShift +ᵥ MiddleSimplex.standardBasis 1175

def J : Set FreeSpace := convexHull ℝ (range freeBasis)

@[simp] theorem freeBasis_coord_zero (i : Fin 1176) : freeBasis.coord i 0 = 1 / 1176 := by
  rcases Fin.eq_castSucc_or_eq_last i with ⟨i, rfl⟩ | rfl
  · simp [freeBasis, AffineBasis.coord_vadd, MiddleSimplex.standardBasis_coord_castSucc,
      freeShift]
  · rw [freeBasis, AffineBasis.coord_vadd]
    change (MiddleSimplex.standardBasis 1175).coord (Fin.last 1175) (-freeShift + 0) = _
    rw [MiddleSimplex.standardBasis_coord_last]
    norm_num [freeShift, Finset.sum_const, nsmul_eq_mul]

theorem J_compact : IsCompact J := (Set.finite_range freeBasis).isCompact_convexHull ℝ
theorem J_convex : Convex ℝ J := convex_convexHull ℝ _
theorem J_volume : volume J = ENNReal.ofReal (1 / (Nat.factorial 1175 : ℝ)) := by
  have hr : range freeBasis =
      (fun x => freeShift + x) '' range (MiddleSimplex.standardBasis 1175) := by
    rw [← Set.range_comp]
    rfl
  have hi := (AffineEquiv.constVAdd ℝ FreeSpace freeShift).toAffineMap.image_convexHull
    (range (MiddleSimplex.standardBasis 1175))
  change (fun x => freeShift + x) '' BoxPadding.simplex 1175 =
    convexHull ℝ ((fun x => freeShift + x) '' range (MiddleSimplex.standardBasis 1175)) at hi
  rw [J, hr, ← hi, SourceGeometry.volume_translate, standardSimplex_volume]

theorem zero_mem_interior_J : (0 : FreeSpace) ∈ interior J := by
  rw [J, freeBasis.interior_convexHull]
  intro i
  change 0 < freeBasis.coord i 0
  rw [freeBasis_coord_zero]
  norm_num

def B : Set E := split ⁻¹' (BoxSources.B0 ×ˢ J)
def T (j : Fin 4) : Set E := split ⁻¹' (BoxSources.T j ×ˢ J)

theorem B_compact : IsCompact B :=
  split.toHomeomorph.isCompact_preimage.2 (BoxSources.B0_compact.prod J_compact)
theorem B_convex : Convex ℝ B :=
  (BoxSources.B0_convex.prod J_convex).linear_preimage split.toLinearEquiv.toLinearMap
theorem zero_mem_interior_B : (0 : E) ∈ interior B := by
  change (0 : E) ∈ interior (split.toHomeomorph ⁻¹' (BoxSources.B0 ×ˢ J))
  rw [← split.toHomeomorph.preimage_interior, interior_prod_eq]
  change split 0 ∈ interior BoxSources.B0 ×ˢ interior J
  rw [map_zero]
  exact ⟨BoxSources.zero_mem_interior_B0, zero_mem_interior_J⟩
theorem B_nonempty : B.Nonempty := ⟨0, interior_subset zero_mem_interior_B⟩
theorem B_volume_pos : 0 < volume B :=
  Measure.measure_pos_of_nonempty_interior volume ⟨0, zero_mem_interior_B⟩
theorem B_volume_ne_top : volume B ≠ ⊤ := B_compact.measure_ne_top

theorem T_compact (j : Fin 4) : IsCompact (T j) :=
  split.toHomeomorph.isCompact_preimage.2 ((BoxSources.T_compact j).prod J_compact)
theorem T_convex (j : Fin 4) : Convex ℝ (T j) :=
  ((BoxSources.T_convex j).prod J_convex).linear_preimage split.toLinearEquiv.toLinearMap
theorem T_subset_B (j : Fin 4) : T j ⊆ B :=
  fun _ hx => ⟨BoxSources.T_subset_B0 j hx.1, hx.2⟩
theorem T_nonempty (j : Fin 4) : (T j).Nonempty := by
  refine ⟨0, ?_⟩
  change split 0 ∈ BoxSources.T j ×ˢ J
  rw [map_zero]
  exact ⟨⟨interior_subset BoxSources.zero_mem_interior_B0,
    by intro i hi; simp⟩, interior_subset zero_mem_interior_J⟩

theorem B_volume : volume B = volume BoxSources.B0 * volume J := by
  rw [B, volume_split_preimage, Measure.volume_eq_prod, Measure.prod_prod]

theorem T_volume (j : Fin 4) : volume (T j) = ENNReal.ofReal (3 / 32 : ℝ) * volume B := by
  rw [T, volume_split_preimage, Measure.volume_eq_prod, Measure.prod_prod,
    BoxSources.T_volume, B_volume, mul_assoc]
  rfl

def f (j : Fin 4) : E →L[ℝ] ℝ :=
  (BoxSources.f j).comp ((ContinuousLinearMap.fst ℝ BoxSources.E0 FreeSpace).comp
    split.toContinuousLinearMap)

def g (j : Fin 1176) : E →L[ℝ] ℝ :=
  (freeBasis.coord j).linear.toContinuousLinearMap.comp
    ((ContinuousLinearMap.snd ℝ BoxSources.E0 FreeSpace).comp split.toContinuousLinearMap)

theorem f_apply (j : Fin 4) (x : E) :
    f j x = BoxSources.lambda j (split x).1 - 1 / 4 := BoxSources.f_apply _ _

theorem g_apply (j : Fin 1176) (x : E) :
    g j x = freeBasis.coord j (split x).2 - 1 / 1176 := by
  have h := congrFun (freeBasis.coord j).decomp (split x).2
  simp only [Pi.add_apply, freeBasis_coord_zero] at h
  change (freeBasis.coord j).linear (split x).2 = _
  linarith

theorem f_sum (x : E) : ∑ j, f j x = 0 := BoxSources.f_sum (split x).1
theorem cuts_cover (x : E) : ∃ j, 0 ≤ f j x := BoxSources.cuts_cover (split x).1

theorem f_nonzero (j : Fin 4) : f j ≠ 0 := by
  intro h
  apply BoxSources.f_nonzero j
  ext x
  have hh := congrArg (fun L : E →L[ℝ] ℝ => L (split.symm (x, 0))) h
  simpa [f] using hh

theorem f_kernel_volume_zero (j : Fin 4) : volume {x : E | f j x = 0} = 0 := by
  change volume ((f j).toLinearMap.ker : Set E) = 0
  apply Measure.addHaar_submodule
  intro htop
  have hz : (f j).toLinearMap = 0 := LinearMap.ker_eq_top.mp htop
  apply f_nonzero j
  ext x
  exact congrArg (fun L : E →ₗ[ℝ] ℝ => L x) hz

theorem B_f_bounds {x : E} (hx : x ∈ B) (j : Fin 4) : -1 ≤ f j x ∧ f j x ≤ 1 :=
  BoxSources.B0_f_bounds hx.1 j

theorem T_f_missed (a j : Fin 4) (hj : j ≠ a) {x : E} (hx : x ∈ T a) :
    f j x ≤ 0 := BoxSources.T_f_missed a j hj hx.1

theorem cap_volume (j : Fin 4) :
    volume (B ∩ {x | 0 ≤ f j x}) = ENNReal.ofReal (27 / 64 : ℝ) * volume B := by
  have he : B ∩ {x | 0 ≤ f j x} =
      split ⁻¹' ((BoxSources.B0 ∩ {u | 0 ≤ BoxSources.f j u}) ×ˢ J) := by
    ext x
    change (((split x).1 ∈ BoxSources.B0 ∧ (split x).2 ∈ J) ∧ 0 ≤ f j x) ↔
      (((split x).1 ∈ BoxSources.B0 ∧ 0 ≤ f j x) ∧ (split x).2 ∈ J)
    tauto
  rw [he, volume_split_preimage, Measure.volume_eq_prod, Measure.prod_prod,
    BoxSources.cap_volume, B_volume, mul_assoc]

theorem B_eq_bounds : B = {x | (∀ j, -(1 / 4 : ℝ) ≤ f j x) ∧
    (∀ j, -(1 / 1176 : ℝ) ≤ g j x)} := by
  ext x
  change ((split x).1 ∈ BoxSources.B0 ∧ (split x).2 ∈ J) ↔ _
  rw [BoxSources.B0_eq_nonneg_lambda, J, freeBasis.convexHull_eq_nonneg_coord]
  change ((∀ j, 0 ≤ BoxSources.lambda j (split x).1) ∧
    (∀ j, 0 ≤ freeBasis.coord j (split x).2)) ↔ _
  simp only [Set.mem_ofPred_eq, f_apply, g_apply, le_sub_iff_add_le, neg_add_cancel]

def dilate (r : ℝ) (S : Set E) : Set E := (r • ·) '' S

theorem dilate_compact (r : ℝ) {S : Set E} (hS : IsCompact S) : IsCompact (dilate r S) :=
  hS.image (by fun_prop)

theorem dilate_convex (r : ℝ) {S : Set E} (hS : Convex ℝ S) : Convex ℝ (dilate r S) := by
  simpa [dilate] using hS.linear_image (r • (LinearMap.id : E →ₗ[ℝ] E))

theorem dilate_nonempty (r : ℝ) {S : Set E} (hS : S.Nonempty) : (dilate r S).Nonempty :=
  hS.image _

theorem dilate_volume {r : ℝ} (hr : 0 ≤ r) (S : Set E) :
    volume (dilate r S) = ENNReal.ofReal (r ^ 1178) * volume S := by
  have he : dilate r S = AffineMap.homothety (0 : E) r '' S := by
    unfold dilate
    congr 1
    funext x
    simp [AffineMap.homothety_apply]
  rw [he, volume.addHaar_image_homothety]
  simp only [Module.finrank_pi, Fintype.card_fin]
  rw [abs_of_nonneg (pow_nonneg hr _)]

theorem dilate_B_eq_bounds {r : ℝ} (hr : 0 < r) :
    dilate r B = {x | (∀ j, -r / 4 ≤ f j x) ∧ (∀ j, -r / 1176 ≤ g j x)} := by
  ext x
  constructor
  · rintro ⟨y, hy, rfl⟩
    rw [B_eq_bounds] at hy
    change _ ∧ _
    constructor
    · intro j
      rw [map_smul, smul_eq_mul]
      nlinarith [mul_le_mul_of_nonneg_left (hy.1 j) hr.le]
    · intro j
      rw [map_smul, smul_eq_mul]
      nlinarith [mul_le_mul_of_nonneg_left (hy.2 j) hr.le]
  · intro hx
    refine ⟨r⁻¹ • x, ?_, ?_⟩
    · rw [B_eq_bounds]
      constructor
      · intro j
        rw [map_smul, smul_eq_mul, ← div_eq_inv_mul, le_div_iff₀ hr]
        have h := hx.1 j
        linarith
      · intro j
        rw [map_smul, smul_eq_mul, ← div_eq_inv_mul, le_div_iff₀ hr]
        have h := hx.2 j
        linarith
    · change r • (r⁻¹ • x) = x
      rw [smul_smul, mul_inv_cancel₀ hr.ne', one_smul]

/-- Every point of an exposed unit sector is covered by a free-simplex cap. -/
theorem T_small_halfspace (j : Fin 4) (x : E) :
    ∃ h : E →L[ℝ] ℝ, ∃ t : ℝ, h ≠ 0 ∧ t ≤ h x ∧
      volume (T j ∩ {y | t ≤ h y}) =
        ENNReal.ofReal ((1175 / 1176 : ℝ) ^ 1175) * volume (T j) := by
  obtain ⟨h, t, hn, hx, hc⟩ := simplex_small_halfspace (by norm_num : 0 < 1175)
    freeBasis volume (by simp) (split x).2
  let H := h.comp ((ContinuousLinearMap.snd ℝ BoxSources.E0 FreeSpace).comp
    split.toContinuousLinearMap)
  refine ⟨H, t, ?_, hx, ?_⟩
  · intro hz
    apply hn
    ext u
    have hh := congrArg (fun L : E →L[ℝ] ℝ => L (split.symm (0, u))) hz
    simpa [H] using hh
  · have he : T j ∩ {y | t ≤ H y} =
        split ⁻¹' (BoxSources.T j ×ˢ (J ∩ {u | t ≤ h u})) := by
      ext y
      change (((split y).1 ∈ BoxSources.T j ∧ (split y).2 ∈ J) ∧ t ≤ H y) ↔
        ((split y).1 ∈ BoxSources.T j ∧ ((split y).2 ∈ J ∧ t ≤ H y))
      tauto
    have hc' : volume (J ∩ {u | t ≤ h u}) =
        ENNReal.ofReal ((1175 / 1176 : ℝ) ^ 1175) * volume J := by
      simpa only [J, Nat.cast_ofNat, show (1175 : ℝ) + 1 = 1176 by norm_num] using hc
    rw [he, volume_split_preimage, T, volume_split_preimage]
    simp only [Measure.volume_eq_prod, Measure.prod_prod, hc']
    ac_rfl

/-- A rational one-coordinate dilation gives the prescribed inactive mass. -/
def inactiveScale (m : ℝ) : ℝ :=
  (m * (Nat.factorial 1178 : ℝ)) / ((Nat.factorial 3 : ℝ) * (Nat.factorial 1175 : ℝ))

/-- The last continuous coordinate, as in the written construction. -/
def inactiveStretchAxis : Fin 1178 := Fin.last 1177

def inactiveMap (m : ℝ) : E →ₗ[ℝ] E :=
  Matrix.toLin' (Matrix.diagonal (fun i => if i = inactiveStretchAxis then inactiveScale m else 1))

theorem inactiveMap_apply (m : ℝ) (x : E) (i : Fin 1178) :
    inactiveMap m x i = (if i = inactiveStretchAxis then inactiveScale m else 1) * x i := by
  simp [inactiveMap, Matrix.toLin'_apply, Matrix.mulVec_diagonal]

theorem inactiveScale_pos {m : ℝ} (hm : 0 < m) : 0 < inactiveScale m := by
  unfold inactiveScale
  positivity

theorem inactiveMap_det (m : ℝ) : LinearMap.det (inactiveMap m) = inactiveScale m := by
  rw [inactiveMap, LinearMap.det_toLin', Matrix.det_diagonal,
    Finset.prod_eq_single inactiveStretchAxis]
  · simp
  · intro i hi h0
    simp [h0]
  · simp

theorem inactiveMap_injective {m : ℝ} (hm : 0 < m) : Function.Injective (inactiveMap m) := by
  intro x y h
  ext i
  have hi := congrFun h i
  rw [inactiveMap_apply, inactiveMap_apply] at hi
  have hne : (if i = inactiveStretchAxis then inactiveScale m else 1) ≠ 0 := by
    split_ifs <;> simp [(inactiveScale_pos hm).ne']
  exact mul_left_cancel₀ hne hi

def inactiveSimplex (m : ℝ) : Set E := inactiveMap m '' BoxPadding.simplex 1178

theorem inactiveSimplex_compact (m : ℝ) : IsCompact (inactiveSimplex m) :=
  (BoxPadding.simplex_compact 1178).image (inactiveMap m).continuous_of_finiteDimensional

theorem inactiveSimplex_convex (m : ℝ) : Convex ℝ (inactiveSimplex m) :=
  (BoxPadding.simplex_convex 1178).linear_image _

theorem inactiveSimplex_nonempty (m : ℝ) : (inactiveSimplex m).Nonempty :=
  ⟨0, 0, BoxPadding.zero_mem_simplex 1178, map_zero _⟩

theorem inactiveSimplex_volume {m : ℝ} (hm : 0 < m) :
    volume (inactiveSimplex m) = ENNReal.ofReal m * volume B := by
  rw [inactiveSimplex, Measure.addHaar_image_linearMap, inactiveMap_det,
    abs_of_pos (inactiveScale_pos hm), standardSimplex_volume, B_volume,
    BoxSources.B0_volume, J_volume,
    ← ENNReal.ofReal_mul (inactiveScale_pos hm).le,
    ← ENNReal.ofReal_mul (by norm_num : (0 : ℝ) ≤ 1 / 6),
    ← ENNReal.ofReal_mul hm.le]
  congr 1
  unfold inactiveScale
  rw [show (Nat.factorial 3 : ℝ) = 6 by norm_num [Nat.factorial]]
  have h (a b : ℝ) (ha : a ≠ 0) (hb : b ≠ 0) :
      m * a / (6 * b) * (1 / a) = m * (1 / 6 * (1 / b)) := by
    field_simp
  exact h _ _ (by positivity) (by positivity)

private theorem linearImageSimplex {d : ℕ}
    (L : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (hL : Function.Injective L) :
    ∃ b : AffineBasis (Fin (d + 1)) ℝ (Fin d → ℝ),
      convexHull ℝ (range b) = L '' BoxPadding.simplex d := by
  have h : Function.Injective L.toAffineMap := fun _ _ he => hL he
  exact ⟨affineImageBasis (MiddleSimplex.standardBasis d) L.toAffineMap h,
    affineImageBasis_hull _ _ _⟩

theorem inactiveSimplex_small_halfspace {m : ℝ} (hm : 0 < m) (x : E) :
    ∃ h : E →L[ℝ] ℝ, ∃ t : ℝ, h ≠ 0 ∧ t ≤ h x ∧
      volume (inactiveSimplex m ∩ {y | t ≤ h y}) =
        ENNReal.ofReal ((1178 / 1179 : ℝ) ^ 1178) * volume (inactiveSimplex m) := by
  obtain ⟨b, hb⟩ := linearImageSimplex (inactiveMap m) (inactiveMap_injective hm)
  change convexHull ℝ (range b) = inactiveSimplex m at hb
  rw [← hb]
  simpa only [Nat.cast_ofNat, show (1178 : ℝ) + 1 = 1179 by norm_num] using
    simplex_small_halfspace (by norm_num : 0 < 1178) b volume (by simp) x

end SharpOC.Witness1387
