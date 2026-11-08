import SharpOC.Halfspaces
import SharpOC.LatticeGeometry

/-! Fiber roofs and halfspace cuts on finite supporting slices. -/

noncomputable section

namespace SharpOC.Witness1387

open Set
open scoped BigOperators

/-- A supporting score restricts the fiber calculation to its maximizing
generators. A linear radius on that face preserves the prescribed fiber. -/
theorem fiber_eq_from_affine_roof
    {α Z E : Type*} [Fintype α]
    [AddCommGroup Z] [Module ℝ Z] [AddCommGroup E] [Module ℝ E]
    (z : α → Z) (K : α → Set E) (i : α)
    (hconv : ∀ a, Convex ℝ (K a)) (hne : ∀ a, (K a).Nonempty)
    (ell u : Z →ₗ[ℝ] ℝ)
    (hface : ∀ a, ell (z a) ≤ ell (z i))
    (hscale : ∀ a, ell (z a) = ell (z i) → 0 ≤ 1 + u (z a) - u (z i))
    (hroof : ∀ a, ell (z a) = ell (z i) → ∀ x ∈ K a,
      ∃ y ∈ K i, x = (1 + u (z a) - u (z i)) • y) :
    {x | (z i, x) ∈ convexHull ℝ
      {p : Z × E | ∃ a, p.1 = z a ∧ p.2 ∈ K a}} = K i := by
  classical
  ext x
  constructor
  · intro hx
    obtain ⟨w, v, hw, hsum, hv, hbase, hcont⟩ :=
      SharpOC.finite_convex_fiber_representation z K hconv hne (z i) x hx
    have hscore (f : Z →ₗ[ℝ] ℝ) : ∑ a, w a * f (z a) = f (z i) := by
      simpa only [map_sum, map_smul, smul_eq_mul] using congrArg f hbase
    have hzero (a : α) (ha : ell (z a) ≠ ell (z i)) : w a = 0 :=
      SharpOC.weight_eq_zero_of_average_eq_upper w (fun b => ell (z b)) (ell (z i))
        hw hsum hface (hscore ell) a (lt_of_le_of_ne (hface a) ha)
    obtain ⟨x₀, hx₀⟩ := hne i
    have hchoose (a : α) : ∃ y ∈ K i,
        w a • v a = (w a * (1 + u (z a) - u (z i))) • y := by
      by_cases ha : ell (z a) = ell (z i)
      · obtain ⟨y, hy, heq⟩ := hroof a ha (v a) (hv a)
        exact ⟨y, hy, by rw [heq, mul_smul]⟩
      · exact ⟨x₀, hx₀, by simp [hzero a ha]⟩
    choose y hy hxy using hchoose
    rw [← hcont]
    simp_rw [hxy]
    apply (hconv i).sum_mem _ _ (fun a _ => hy a)
    · intro a _
      by_cases ha : ell (z a) = ell (z i)
      · exact mul_nonneg (hw a) (hscale a ha)
      · simp [hzero a ha]
    · simp_rw [mul_sub, mul_add, mul_one]
      rw [Finset.sum_sub_distrib, Finset.sum_add_distrib, hsum, hscore u,
        ← Finset.sum_mul, hsum, one_mul]
      ring
  · intro hx
    exact subset_convexHull ℝ _ ⟨i, rfl, hx⟩

/-- A single ambient halfspace realizes an ambient score on a finite
supporting slice, and strictly excludes every other prescribed source. -/
theorem supporting_slice_cut
    {α Z E : Type*} [Fintype α]
    [NormedAddCommGroup Z] [NormedSpace ℝ Z]
    [NormedAddCommGroup E] [NormedSpace ℝ E]
    (z : α → Z) (K : α → Set E) (hK : ∀ a, IsCompact (K a))
    (i : α) (ell : Z →L[ℝ] ℝ) (hface : ∀ a, ell (z a) ≤ ell (z i))
    (h : (Z × E) →L[ℝ] ℝ) (hcont : ∃ x, h (0, x) ≠ 0) (t : ℝ) :
    ∃ F : (Z × E) →L[ℝ] ℝ, ∃ b : ℝ, F ≠ 0 ∧
      (∀ a, ell (z a) = ell (z i) → ∀ x, t ≤ h (z a, x) ↔ b ≤ F (z a, x)) ∧
      (∀ a, ell (z a) ≠ ell (z i) → ∀ x ∈ K a, F (z a, x) < b) := by
  classical
  have hcompact : IsCompact (⋃ a, ({z a} : Set Z) ×ˢ K a) :=
    isCompact_iUnion (fun a => isCompact_singleton.prod (hK a))
  obtain ⟨R, hR⟩ := (hcompact.image h.continuous).bddAbove
  let q : α → ℝ := fun a => (R - t) / (ell (z i) - ell (z a))
  obtain ⟨Q₀, hQ₀⟩ := Finite.bddAbove_range q
  let Q : ℝ := max (Q₀ + 1) 1
  have hQ (a : α) : q a < Q := by
    have ha : q a ≤ Q₀ := hQ₀ (mem_range_self a)
    exact lt_of_lt_of_le (by linarith) (le_max_left _ _)
  let F : (Z × E) →L[ℝ] ℝ :=
    h + Q • ell.comp (ContinuousLinearMap.fst ℝ Z E)
  refine ⟨F, t + Q * ell (z i), ?_, ?_, ?_⟩
  · obtain ⟨x, hx⟩ := hcont
    intro hF
    apply hx
    have heq := congrArg (fun G : (Z × E) →L[ℝ] ℝ => G (0, x)) hF
    simpa [F] using heq
  · intro a ha x
    change t ≤ h (z a, x) ↔ t + Q * ell (z i) ≤ h (z a, x) + Q * ell (z a)
    rw [ha]
    exact (add_le_add_iff_right _).symm
  · intro a ha x hx
    have hgap : 0 < ell (z i) - ell (z a) := sub_pos.mpr (lt_of_le_of_ne (hface a) ha)
    have hbound : h (z a, x) ≤ R := hR ⟨(z a, x), mem_iUnion.mpr ⟨a, rfl, hx⟩, rfl⟩
    have hlarge : R - t < Q * (ell (z i) - ell (z a)) := (div_lt_iff₀ hgap).mp (hQ a)
    change h (z a, x) + Q * ell (z a) < t + Q * ell (z i)
    nlinarith

end SharpOC.Witness1387
