import SharpOC.LatticeGeometry

/-!
# Compactness and full ambient dimension of the fiber construction

These results check the topological convex-body obligations using arbitrary
finite integer-coordinate index types. They do not assume that the nonzero
cube fibers contain the continuous origin.
-/

namespace SharpOC

open Finset

variable {α ι : Type*} [Fintype α] [Fintype ι] [DecidableEq ι]

theorem subsetProjectionGenerator_injective :
    Function.Injective (subsetProjectionGenerator (ι := ι)) := by
  intro a b hab
  cases a with
  | inl I =>
    cases b with
    | inl J =>
      congr 1
      ext i
      have hi := congrFun hab i
      by_cases hI : i ∈ I <;> by_cases hJ : i ∈ J <;>
        simp_all [subsetProjectionGenerator, cubeVector]
    | inr j =>
      have hj := congrFun hab j
      by_cases hJ : j ∈ I <;>
        norm_num [subsetProjectionGenerator, cubeVector, negativeUnit, hJ] at hj
  | inr i =>
    cases b with
    | inl J =>
      have hi := congrFun hab i
      by_cases hI : i ∈ J <;>
        norm_num [subsetProjectionGenerator, cubeVector, negativeUnit, hI] at hi
    | inr j =>
      have hi := congrFun hab i
      by_cases hij : i = j
      · simp [hij]
      · simp [subsetProjectionGenerator, negativeUnit, hij] at hi

/-- The convex hull of finitely many nonempty compact convex sets is compact.
The proof uses an explicit compact parameter space of weights and selected
points, with the previously checked aggregation theorem for surjectivity. -/
theorem isCompact_convexHull_finite_convex_family
    {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
    (K : α → Set E) (hK : ∀ a, Convex ℝ (K a))
    (hne : ∀ a, (K a).Nonempty) (hcompact : ∀ a, IsCompact (K a)) :
    IsCompact (convexHull ℝ {p | ∃ a, p ∈ K a}) := by
  classical
  let W : Set (α → ℝ) := {w | (∀ a, 0 ≤ w a) ∧ ∑ a, w a = 1}
  have hW : IsCompact W := by
    have hnonneg : IsClosed {w : α → ℝ | ∀ a, 0 ≤ w a} := by
      simpa only [Set.ofPred_forall] using
        isClosed_iInter (fun a : α => isClosed_le continuous_const (continuous_apply a))
    have hsum : IsClosed {w : α → ℝ | ∑ a, w a = 1} :=
      isClosed_eq (by fun_prop) continuous_const
    apply IsCompact.of_isClosed_subset (s := Set.Icc (0 : α → ℝ) 1)
      isCompact_Icc (hnonneg.inter hsum)
    intro w hw
    refine ⟨hw.1, ?_⟩
    intro a
    calc
      w a ≤ ∑ b, w b := Finset.single_le_sum (fun b _ => hw.1 b) (Finset.mem_univ a)
      _ = 1 := hw.2
  let D : Set ((α → ℝ) × (α → E)) :=
    W ×ˢ {y | ∀ a, y a ∈ K a}
  let F : ((α → ℝ) × (α → E)) → E := fun p => ∑ a, p.1 a • p.2 a
  have hD : IsCompact D :=
    hW.prod (isCompact_pi_infinite hcompact)
  have hF : Continuous F := by
    dsimp [F]
    fun_prop
  have heq : F '' D = convexHull ℝ {p | ∃ a, p ∈ K a} := by
    ext x
    constructor
    · rintro ⟨⟨w, y⟩, ⟨hw, hy⟩, rfl⟩
      exact mem_convexHull_of_exists_fintype w y hw.1 hw.2
        (fun a => ⟨a, hy a⟩) rfl
    · intro hx
      obtain ⟨w, y, hw, hs, hy, hxy⟩ :=
        mem_convexHull_finite_convex_family K hK hne x hx
      exact ⟨(w, y), ⟨⟨hw, hs⟩, hy⟩, hxy⟩
  rw [← heq]
  exact hD.image hF

/-- Compactness specialized to compact convex fibers over finitely many bases. -/
theorem isCompact_fiber_convexHull
    {Z E : Type*} [NormedAddCommGroup Z] [NormedSpace ℝ Z]
    [NormedAddCommGroup E] [NormedSpace ℝ E]
    (g : α → Z) (K : α → Set E)
    (hK : ∀ a, Convex ℝ (K a)) (hne : ∀ a, (K a).Nonempty)
    (hcompact : ∀ a, IsCompact (K a)) :
    IsCompact (convexHull ℝ {p : Z × E | ∃ a, p.1 = g a ∧ p.2 ∈ K a}) := by
  apply isCompact_convexHull_finite_convex_family
    (fun a => ({g a} : Set Z) ×ˢ K a)
  · exact fun a => (convex_singleton (g a)).prod (hK a)
  · intro a
    obtain ⟨x, hx⟩ := hne a
    exact ⟨(g a, x), rfl, hx⟩
  · exact fun a => isCompact_singleton.prod (hcompact a)

/-- A full-dimensional middle fiber and one arbitrary lifted point over
each positive coordinate unit already give full ambient affine span. -/
theorem affineSpan_eq_top_of_vertical_and_units
    {E : Type*} [AddCommGroup E] [Module ℝ E]
    (B : Set E) (G : Set ((ι → ℝ) × E))
    (hB : affineSpan ℝ B = ⊤)
    (hmiddle : ∀ x ∈ B, ((0 : ι → ℝ), x) ∈ G)
    (hlifts : ∀ i, ∃ x, (cubeVector {i}, x) ∈ G) :
    affineSpan ℝ G = ⊤ := by
  classical
  let S := affineSpan ℝ G
  have hvertical : ∀ x : E, ((0 : ι → ℝ), x) ∈ S := by
    let T := AffineSubspace.comap (LinearMap.inr ℝ (ι → ℝ) E).toAffineMap S
    have hBT : affineSpan ℝ B ≤ T := by
      apply affineSpan_le.mpr
      intro x hx
      exact subset_affineSpan ℝ G (hmiddle x hx)
    have hT : T = ⊤ := by
      apply top_unique
      simpa only [hB] using hBT
    intro x
    have hx : x ∈ T := by rw [hT]; trivial
    exact hx
  have hunits : ∀ i, (cubeVector {i}, (0 : E)) ∈ S.direction := by
    intro i
    obtain ⟨x, hx⟩ := hlifts i
    have hp : (cubeVector {i}, x) ∈ S := subset_affineSpan ℝ G hx
    have hv := S.vsub_mem_direction hp (hvertical x)
    simpa only [vsub_eq_sub, Prod.mk_sub_mk, sub_zero, sub_self] using hv
  have hallint : ∀ z : ι → ℝ, (z, (0 : E)) ∈ S.direction := by
    intro z
    have hsum : (∑ i, z i • (cubeVector {i}, (0 : E))) ∈ S.direction :=
      S.direction.sum_mem (fun i _ => S.direction.smul_mem (z i) (hunits i))
    have heq : (∑ i, z i • (cubeVector {i}, (0 : E))) = (z, 0) := by
      ext j
      · simp [cubeVector, Prod.fst_sum, Finset.sum_apply, mul_ite]
      · simp [Prod.snd_sum]
    rwa [heq] at hsum
  apply top_unique
  intro p hp
  have h := S.vadd_mem_of_mem_direction (hallint p.1) (hvertical p.2)
  simpa only [vadd_eq_add, Prod.mk_add_mk, add_zero, zero_add, Prod.mk.eta] using h

/-- The same data give nonempty ambient interior of the actual convex hull.
In particular, no source fiber needs to contain the continuous origin. -/
theorem interior_convexHull_nonempty_of_vertical_and_units
    {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
    [FiniteDimensional ℝ E]
    (B : Set E) (G : Set ((ι → ℝ) × E))
    (hB : (interior B).Nonempty)
    (hmiddle : ∀ x ∈ B, ((0 : ι → ℝ), x) ∈ G)
    (hlifts : ∀ i, ∃ x, (cubeVector {i}, x) ∈ G) :
    (interior (convexHull ℝ G)).Nonempty := by
  apply interior_convexHull_nonempty_iff_affineSpan_eq_top.mpr
  exact affineSpan_eq_top_of_vertical_and_units B G
    (affineSpan_eq_top_of_nonempty_interior
      (hB.mono (interior_mono (subset_convexHull ℝ B)))) hmiddle hlifts

/-- The cube/negative-unit fiber construction is a genuine ambient convex
body whenever its fibers are nonempty compact convex sets and its middle
fiber has nonempty continuous interior. No common point in the other
continuous fibers is required. -/
theorem fiber_construction_is_convex_body
    {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
    [FiniteDimensional ℝ E]
    (K : Sum (Finset ι) ι → Set E)
    (hK : ∀ a, Convex ℝ (K a)) (hne : ∀ a, (K a).Nonempty)
    (hcompact : ∀ a, IsCompact (K a))
    (hmiddle : (interior (K (.inl ∅))).Nonempty) :
    let C := convexHull ℝ {p : (ι → ℝ) × E |
      ∃ a : Sum (Finset ι) ι, p.1 = subsetProjectionGenerator a ∧ p.2 ∈ K a}
    IsCompact C ∧ Convex ℝ C ∧ (interior C).Nonempty := by
  dsimp only
  refine ⟨isCompact_fiber_convexHull subsetProjectionGenerator K hK hne hcompact,
    convex_convexHull ℝ _, ?_⟩
  apply interior_convexHull_nonempty_of_vertical_and_units (K (.inl ∅)) _ hmiddle
  · intro x hx
    refine ⟨.inl ∅, ?_, hx⟩
    funext i
    simp [subsetProjectionGenerator, cubeVector]
  · intro i
    obtain ⟨x, hx⟩ := hne (.inl {i})
    exact ⟨x, .inl {i}, rfl, hx⟩

end SharpOC
