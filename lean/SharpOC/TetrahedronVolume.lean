import SharpOC.MiddleSimplex

/-! The volume of the standard tetrahedron, by a six-piece cube triangulation. -/
noncomputable section
open Set MeasureTheory
open scoped ENNReal
namespace SharpOC.TetrahedronVolume
open SharpOC.SourceGeometry SharpOC.MiddleSimplex
abbrev V := Fin 3 → ℝ

private theorem standard_mem (x : V) : x ∈ standardSimplex 3 ↔
    0 ≤ x 0 ∧ 0 ≤ x 1 ∧ 0 ≤ x 2 ∧ x 0 + x 1 + x 2 ≤ 1 := by
  have heq : standardSimplex 3 = convexHull ℝ (range (standardBasis 3)) := by
    change convexHull ℝ (insert 0 (range (fun j : Fin 3 => Pi.single j (1 : ℝ)))) =
      convexHull ℝ (range (standardVertex 3))
    rw [standardVertex_range]
  rw [heq, (standardBasis 3).convexHull_eq_nonneg_coord]
  change (∀ j : Fin 4, 0 ≤ (standardBasis 3).coord j x) ↔ _
  have h0 : (standardBasis 3).coord (0 : Fin 4) x = x 0 := standardBasis_coord_castSucc 3 0 x
  have h1 : (standardBasis 3).coord (1 : Fin 4) x = x 1 := standardBasis_coord_castSucc 3 1 x
  have h2 : (standardBasis 3).coord (2 : Fin 4) x = x 2 := standardBasis_coord_castSucc 3 2 x
  have h3 : (standardBasis 3).coord (3 : Fin 4) x = 1-∑i,x i := standardBasis_coord_last 3 x
  constructor
  · intro hh
    have a := hh 0; have b := hh 1; have c := hh 2; have d := hh 3
    rw [h0] at a; rw [h1] at b; rw [h2] at c; rw [h3] at d
    norm_num [Fin.sum_univ_succ] at d
    exact ⟨a,b,c,by linarith⟩
  · rintro ⟨a,b,c,d⟩ j
    fin_cases j <;> norm_num only [Fin.reduceFinMk]
    · simpa only [h0] using a
    · simpa only [h1] using b
    · simpa only [h2] using c
    · rw [h3]; norm_num [Fin.sum_univ_succ]; linarith

private def order (i : Fin 6) : Fin 3 → Fin 3 :=
  ![![0,1,2], ![0,2,1], ![1,0,2], ![1,2,0], ![2,0,1], ![2,1,0]] i
private def mat (i : Fin 6) : Matrix (Fin 3) (Fin 3) ℝ :=
  ![!![1,0,0;1,1,0;1,1,1], !![1,0,0;1,1,1;1,1,0],
    !![1,1,0;1,0,0;1,1,1], !![1,1,1;1,0,0;1,1,0],
    !![1,1,0;1,1,1;1,0,0], !![1,1,1;1,1,0;1,0,0]] i
private def region (i : Fin 6) : Set V := {x |
  0 ≤ x (order i 0) ∧ x (order i 0) ≤ x (order i 1) ∧
    x (order i 1) ≤ x (order i 2) ∧ x (order i 2) ≤ 1}

private theorem region_image (i : Fin 6) :
    region i = (Matrix.toLin' (mat i)) '' standardSimplex 3 := by
  ext x
  constructor
  · intro hx
    refine ⟨![x (order i 0), x (order i 1)-x (order i 0),
      x (order i 2)-x (order i 1)], ?_, ?_⟩
    · rw [standard_mem]
      change 0 ≤ x (order i 0) ∧ 0 ≤ x (order i 1)-x (order i 0) ∧
        0 ≤ x (order i 2)-x (order i 1) ∧
        x (order i 0)+(x (order i 1)-x (order i 0))+(x (order i 2)-x (order i 1)) ≤ 1
      rcases hx with ⟨h0,h1,h2,h3⟩
      exact ⟨h0, sub_nonneg.mpr h1, sub_nonneg.mpr h2, by linarith⟩
    · ext j
      fin_cases i <;> fin_cases j <;>
        norm_num [mat, order, Matrix.toLin'_apply, Matrix.mulVec, dotProduct,
          Fin.sum_univ_succ] <;> ring
  · rintro ⟨y, hy, rfl⟩
    rw [standard_mem] at hy
    rcases hy with ⟨h0,h1,h2,h3⟩
    fin_cases i <;>
      simp [region,order,mat,Matrix.toLin'_apply,Matrix.mulVec,dotProduct,
        Fin.sum_univ_succ] <;> constructor <;> try linarith
    all_goals constructor <;> try linarith
    all_goals constructor <;> linarith

private theorem region_compact (i : Fin 6) : IsCompact (region i) := by
  rw [region_image]
  exact (((finite_range _).insert 0).isCompact_convexHull ℝ).image
    (LinearMap.continuous_of_finiteDimensional _)

private theorem region_volume (i : Fin 6) : volume (region i) = volume (standardSimplex 3) := by
  rw [region_image, Measure.addHaar_image_linearMap, LinearMap.det_toLin']
  have hd : |(mat i).det| = 1 := by fin_cases i <;> norm_num [mat,Matrix.det_fin_three]
  rw [hd]
  simp

private theorem union_region : (⋃ i, region i) = Icc (0 : V) 1 := by
  ext x
  simp only [mem_iUnion, mem_Icc]
  constructor
  · rintro ⟨i,hi⟩
    fin_cases i <;> norm_num [region,order] at hi
    all_goals
      constructor <;> intro j <;> fin_cases j <;> norm_num <;> linarith [hi.1,hi.2.1,hi.2.2.1,hi.2.2.2]
  · rintro ⟨h0,h1⟩
    have h00 := h0 0; have h01 := h0 1; have h02 := h0 2
    have h10 := h1 0; have h11 := h1 1; have h12 := h1 2
    simp only [Pi.zero_apply,Pi.one_apply] at h00 h01 h02 h10 h11 h12
    by_cases hA : x 0 ≤ x 1 <;> by_cases hB : x 0 ≤ x 2 <;> by_cases hC : x 1 ≤ x 2
    all_goals first
      | exact ⟨0, by norm_num [region,order]; exact ⟨by linarith, by linarith, by linarith, by linarith⟩⟩
      | exact ⟨1, by norm_num [region,order]; exact ⟨by linarith, by linarith, by linarith, by linarith⟩⟩
      | exact ⟨2, by norm_num [region,order]; exact ⟨by linarith, by linarith, by linarith, by linarith⟩⟩
      | exact ⟨3, by norm_num [region,order]; exact ⟨by linarith, by linarith, by linarith, by linarith⟩⟩
      | exact ⟨4, by norm_num [region,order]; exact ⟨by linarith, by linarith, by linarith, by linarith⟩⟩
      | exact ⟨5, by norm_num [region,order]; exact ⟨by linarith, by linarith, by linarith, by linarith⟩⟩

private theorem equal_coordinate_null (i j : Fin 3) (hij : i ≠ j) :
    volume {x : V | x i = x j} = 0 := by
  let L : V →ₗ[ℝ] ℝ :=
    { toFun := fun x => x i - x j
      map_add' := by intros; simp; ring
      map_smul' := by intros; simp; ring }
  have hs : {x : V | x i = x j} = (L.ker : Set V) := by
    ext x; simp [L,LinearMap.mem_ker,sub_eq_zero]
  rw [hs]
  apply Measure.addHaar_submodule
  intro ht
  have hz := LinearMap.ker_eq_top.mp ht
  have hh := congrArg (fun f : V →ₗ[ℝ] ℝ => f (Pi.single i 1)) hz
  simp [L,hij,hij.symm] at hh

private theorem region_pairwise : Pairwise (fun i j => AEDisjoint volume (region i) (region j)) := by
  intro i j hij
  have hz : volume ({x : V | x 0 = x 1} ∪ {x : V | x 0 = x 2} ∪ {x : V | x 1 = x 2}) = 0 := by
    apply measure_union_null
    · exact measure_union_null (equal_coordinate_null 0 1 (by decide))
        (equal_coordinate_null 0 2 (by decide))
    · exact equal_coordinate_null 1 2 (by decide)
  change volume (region i ∩ region j) = 0
  apply measure_mono_null _ hz
  intro x hx
  by_contra hn
  have hneq : x 0 ≠ x 1 ∧ x 0 ≠ x 2 ∧ x 1 ≠ x 2 := by
    simpa only [mem_union,mem_setOf_eq,not_or,and_assoc] using hn
  rcases hx with ⟨hi,hj⟩
  fin_cases i <;> fin_cases j <;> norm_num [region,order] at hi hj hij
  all_goals rcases hi with ⟨ha,hb,hc,hd⟩; rcases hj with ⟨he,hf,hg,hh⟩
  all_goals rcases hneq with ⟨hn0,hn1,hn2⟩
  all_goals first | exact hn0 (by linarith) | exact hn1 (by linarith) | exact hn2 (by linarith)

theorem volume_standardSimplex_three :
    volume (standardSimplex 3) = ENNReal.ofReal (1/6 : ℝ) := by
  have heq := measure_iUnion₀ region_pairwise (fun i => (region_compact i).measurableSet.nullMeasurableSet)
  rw [union_region,Real.volume_Icc_pi] at heq
  simp only [Pi.one_apply,Pi.zero_apply,sub_zero,ENNReal.ofReal_one,
    Finset.prod_const_one,tsum_fintype,region_volume,Finset.sum_const,
    Finset.card_univ,Fintype.card_fin] at heq
  have heq' : (6 : ℝ≥0∞) * volume (standardSimplex 3) = 1 := by
    simpa only [nsmul_eq_mul,Nat.cast_ofNat] using heq.symm
  have hh : volume (standardSimplex 3) = (1:ℝ≥0∞)/6 :=
    (ENNReal.eq_div_iff (by norm_num : (6 : ℝ≥0∞) ≠ 0) (by norm_num : (6 : ℝ≥0∞) ≠ ⊤)).mpr (by simpa [mul_comm] using heq')
  simpa using hh

end SharpOC.TetrahedronVolume
