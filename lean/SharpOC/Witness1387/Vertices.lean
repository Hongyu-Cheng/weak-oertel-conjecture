import SharpOC.Witness1387.Sources

/-! Rational vertex sets of the three continuous sources. -/

noncomputable section
open Set
open scoped Pointwise

namespace SharpOC.Witness1387

abbrev RatE := Fin 1178 → ℚ

def ratToReal (v : RatE) : Fin 1178 → ℝ := fun i => v i

private def join {K : Type*} (x : Fin 3 → K) (y : Fin 1175 → K) : Fin 1178 → K :=
  fun i => Sum.elim x y (finSumFinEquiv.symm i)

private abbrev joinMap :=
  split.symm.toLinearEquiv.toLinearMap

private theorem joinMap_apply (p : BoxSources.E0 × FreeSpace) (i : Fin 1178) :
    joinMap p i = join p.1 p.2 i := by
  change Equiv.piCongrLeft (fun _ : Fin 1178 => ℝ)
    (finSumFinEquiv : Fin 3 ⊕ Fin 1175 ≃ Fin 1178) (Sum.elim p.1 p.2) i = _
  simp [Equiv.piCongrLeft_apply_eq_cast, join]

private def simplexVertex (n : ℕ) (j : Fin (n + 1)) (i : Fin n) : ℚ :=
  if j = i.castSucc then 1 else 0

private def centeredVertex (n : ℕ) (j : Fin (n + 1)) (i : Fin n) : ℚ :=
  simplexVertex n j i - 1 / ((n + 1 : ℕ) : ℚ)

private def cubeVertex (b : Fin 3 → Bool) (i : Fin 3) : ℚ :=
  if b i then 0 else -1 / 4

private def sectorVertex (j : Fin 4) (b : Fin 3 → Bool) : Fin 3 → ℚ :=
  (Matrix.toLin' (fun i k : Fin 3 => if j = i.castSucc then -1 else if i = k then 1 else 0))
    (cubeVertex b)

def centerVertices (r : ℚ) : Finset RatE :=
  Finset.univ.image fun p : Fin 4 × Fin 1176 =>
    r • join (centeredVertex 3 p.1) (centeredVertex 1175 p.2)

def sectorVertices (j : Fin 4) (r : ℚ) : Finset RatE :=
  Finset.univ.image fun p : (Fin 3 → Bool) × Fin 1176 =>
    r • join (sectorVertex j p.1) (centeredVertex 1175 p.2)

private def stretchFactor (m : ℚ) : ℚ :=
  m * ((1178 : ℕ).factorial : ℚ) / (((3 : ℕ).factorial : ℚ) * ((1175 : ℕ).factorial : ℚ))

def inactiveVertices (m : ℚ) : Finset RatE :=
  Finset.univ.image fun j : Fin 1179 => fun i =>
    (if i = inactiveStretchAxis then stretchFactor m else 1) * simplexVertex 1178 j i

private theorem image_ratVertices {ι : Type*} [Fintype ι] (v : ι → RatE) :
    ratToReal '' (↑(Finset.univ.image v) : Set RatE) = range (ratToReal ∘ v) := by
  simp [Finset.coe_image, Set.range_comp]

private theorem cast_simplexVertex (n : ℕ) (j : Fin (n + 1)) (i : Fin n) :
    (simplexVertex n j i : ℝ) = MiddleSimplex.standardVertex n j i := by
  simp [simplexVertex, MiddleSimplex.standardVertex, apply_ite (fun x : ℚ => (x : ℝ))]

private theorem cast_centeredVertex (n : ℕ) (j : Fin (n + 1)) :
    (fun i => (centeredVertex n j i : ℝ)) =
      (fun _ => -(1 / ((n + 1 : ℕ) : ℝ))) + MiddleSimplex.standardVertex n j := by
  ext i
  simp [centeredVertex, cast_simplexVertex, sub_eq_add_neg, add_comm]

private theorem cubeVertex_hull :
    convexHull ℝ (range (fun b => fun i => (cubeVertex b i : ℝ))) = BoxSources.cube := by
  have h : range (fun b => fun i => (cubeVertex b i : ℝ)) =
      (univ : Set (Fin 3)).pi (fun _ => {-(1 / 4 : ℝ), 0}) := by
    ext x
    constructor
    · rintro ⟨b, rfl⟩ i _
      cases h : b i <;> norm_num [cubeVertex, h]
    · intro hx
      refine ⟨fun i => decide (x i = 0), ?_⟩
      ext i
      rcases (show x i = -(1 / 4 : ℝ) ∨ x i = 0 by simpa using hx i (mem_univ i)) with h | h
      · simp [cubeVertex, h]
        norm_num
      · simp [cubeVertex, h]
  rw [h, convexHull_pi]
  simp_rw [convexHull_pair, segment_eq_Icc (by norm_num : -(1 / 4 : ℝ) ≤ 0)]
  exact Set.pi_univ_Icc _ _

private theorem cast_sectorVertex (j : Fin 4) (b : Fin 3 → Bool) :
    (fun i => (sectorVertex j b i : ℝ)) = BoxSources.swapMap j (fun i => (cubeVertex b i : ℝ)) := by
  ext i
  change ((∑ k : Fin 3, (if j = i.castSucc then (-1 : ℚ) else if i = k then 1 else 0) *
    cubeVertex b k : ℚ) : ℝ) =
    ∑ k : Fin 3, (if j = i.castSucc then (-1 : ℝ) else if i = k then 1 else 0) *
      (cubeVertex b k : ℝ)
  simp only [Rat.cast_sum, Rat.cast_mul]
  apply Finset.sum_congr rfl
  intro k _
  split_ifs <;> norm_num

private theorem sectorVertex_hull (j : Fin 4) :
    convexHull ℝ (range (fun b => fun i => (sectorVertex j b i : ℝ))) = BoxSources.T j := by
  rw [show (fun (b : Fin 3 → Bool) i => (sectorVertex j b i : ℝ)) = _ from
    funext (cast_sectorVertex j)]
  rw [BoxSources.T_eq_image_cube, ← cubeVertex_hull, LinearMap.image_convexHull, ← Set.range_comp]
  rfl

private theorem product_hull {ι κ : Type*} (x : ι → Fin 3 → ℚ) (y : κ → Fin 1175 → ℚ) (r : ℚ) :
    convexHull ℝ (range (fun p : ι × κ => ratToReal (r • join (x p.1) (y p.2)))) =
      (fun z : Fin 1178 → ℝ => (r : ℝ) • z) ''
        (joinMap '' (convexHull ℝ (range (fun a i => (x a i : ℝ))) ×ˢ
          convexHull ℝ (range (fun b i => (y b i : ℝ))))) := by
  rw [← convexHull_prod, LinearMap.image_convexHull]
  rw [show (fun z : Fin 1178 → ℝ => (r : ℝ) • z) = ((r : ℝ) • LinearMap.id :
    (Fin 1178 → ℝ) →ₗ[ℝ] (Fin 1178 → ℝ)) from rfl, LinearMap.image_convexHull]
  congr 1
  rw [Set.image_image, ← Set.range_prodMap, ← Set.range_comp]
  congr 1
  ext p i
  simp only [ratToReal, Pi.smul_apply, smul_eq_mul, Rat.cast_mul, Function.comp_apply,
    LinearMap.smul_apply, LinearMap.id_apply, joinMap_apply, Prod.map_fst, Prod.map_snd, join]
  cases (finSumFinEquiv : Fin 3 ⊕ Fin 1175 ≃ Fin 1178).symm i <;> rfl

private theorem centeredVertex3_hull :
    convexHull ℝ (range (fun (j : Fin 4) i => (centeredVertex 3 j i : ℝ))) =
      BoxSources.B0 := by
  unfold BoxSources.B0
  congr 2
  funext j
  change _ = (fun _ : Fin 3 => -(1 / 4 : ℝ)) + MiddleSimplex.standardVertex 3 j
  simpa only [show (3 + 1 : ℕ) = 4 by decide, Nat.cast_ofNat] using
    cast_centeredVertex 3 j

private theorem centeredVertex1175_hull :
    convexHull ℝ (range (fun (j : Fin 1176) i => (centeredVertex 1175 j i : ℝ))) = J := by
  unfold J
  congr 2
  funext j
  change _ = (fun _ : Fin 1175 => -(1 / 1176 : ℝ)) + MiddleSimplex.standardVertex 1175 j
  simpa only [show (1175 + 1 : ℕ) = 1176 by decide, Nat.cast_ofNat] using
    cast_centeredVertex 1175 j

theorem centerVertices_hull (r : ℚ) :
    convexHull ℝ (ratToReal '' (centerVertices r : Set RatE)) = dilate (r : ℝ) B := by
  rw [centerVertices, image_ratVertices]
  change convexHull ℝ (range (fun p : Fin 4 × Fin 1176 =>
    ratToReal (r • join (centeredVertex 3 p.1) (centeredVertex 1175 p.2)))) = _
  rw [product_hull, centeredVertex3_hull, centeredVertex1175_hull]
  change dilate (r : ℝ) (split.symm '' (BoxSources.B0 ×ˢ J)) = _
  rw [split.image_symm_eq_preimage]
  rfl

theorem sectorVertices_hull (j : Fin 4) (r : ℚ) :
    convexHull ℝ (ratToReal '' (sectorVertices j r : Set RatE)) = dilate (r : ℝ) (T j) := by
  rw [sectorVertices, image_ratVertices]
  change convexHull ℝ (range (fun p : (Fin 3 → Bool) × Fin 1176 =>
    ratToReal (r • join (sectorVertex j p.1) (centeredVertex 1175 p.2)))) = _
  rw [product_hull, sectorVertex_hull, centeredVertex1175_hull]
  change dilate (r : ℝ) (split.symm '' (BoxSources.T j ×ˢ J)) = _
  rw [split.image_symm_eq_preimage]
  rfl

set_option maxRecDepth 2048 in
theorem inactiveVertices_hull (m : ℚ) :
    convexHull ℝ (ratToReal '' (inactiveVertices m : Set RatE)) = inactiveSimplex (m : ℝ) := by
  rw [inactiveVertices, image_ratVertices, inactiveSimplex, BoxPadding.simplex,
    LinearMap.image_convexHull, ← Set.range_comp]
  apply congrArg (convexHull ℝ)
  apply congrArg range
  funext j i
  change (((if i = inactiveStretchAxis then stretchFactor m else 1) *
    simplexVertex 1178 j i : ℚ) : ℝ) = inactiveMap (m : ℝ) (MiddleSimplex.standardBasis 1178 j) i
  rw [inactiveMap_apply, Rat.cast_mul, cast_simplexVertex, MiddleSimplex.standardBasis_apply]
  congr 1
  split_ifs <;>
    simp only [stretchFactor, inactiveScale, Rat.cast_div, Rat.cast_mul, Rat.cast_natCast,
      Rat.cast_one]

end SharpOC.Witness1387
