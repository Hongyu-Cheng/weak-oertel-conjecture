import SharpOC.BodyGeometry

/-! An affine radius on a supporting face determines the origin fiber. -/

namespace SharpOC

open Set Finset
open scoped BigOperators

theorem origin_fiber_of_affine_radius
    {α Z E : Type*} [Fintype α]
    [AddCommGroup Z] [Module ℝ Z] [AddCommGroup E] [Module ℝ E]
    (z : α → Z) (K : α → Set E) (a₀ : α)
    (hz₀ : z a₀ = 0)
    (hK : ∀ a, Convex ℝ (K a)) (hne : ∀ a, (K a).Nonempty)
    (r u : Z →ₗ[ℝ] ℝ) (hr : ∀ a, 0 ≤ r (z a))
    (hs : ∀ a, r (z a) = 0 → 0 ≤ 1 + u (z a))
    (hroof : ∀ a, r (z a) = 0 → ∀ x ∈ K a,
      ∃ y ∈ K a₀, x = (1 + u (z a)) • y) :
    {x | ((0 : Z), x) ∈ convexHull ℝ
      {p : Z × E | ∃ a, p.1 = z a ∧ p.2 ∈ K a}} = K a₀ := by
  classical
  ext x
  constructor
  · intro hx
    obtain ⟨w, v, hw, hsum, hv, hbase, hcont⟩ :=
      finite_convex_fiber_representation z K hK hne 0 x hx
    have hscore (f : Z →ₗ[ℝ] ℝ) : ∑ a, w a * f (z a) = 0 := by
      simpa only [map_sum, map_smul, smul_eq_mul, map_zero] using congrArg f hbase
    have hzero (a : α) (ha : r (z a) ≠ 0) : w a = 0 :=
      weight_eq_zero_of_average_eq_lower w (fun b => r (z b)) 0 hw hsum hr
        (hscore r) a (lt_of_le_of_ne (hr a) (Ne.symm ha))
    obtain ⟨x₀, hx₀⟩ := hne a₀
    have hchoose (a : α) : ∃ y ∈ K a₀,
        w a • v a = (w a * (1 + u (z a))) • y := by
      by_cases ha : r (z a) = 0
      · obtain ⟨y, hy, heq⟩ := hroof a ha (v a) (hv a)
        exact ⟨y, hy, by rw [heq, mul_smul]⟩
      · exact ⟨x₀, hx₀, by simp [hzero a ha]⟩
    choose y hy hy_eq using hchoose
    rw [← hcont]
    simp_rw [hy_eq]
    apply (hK a₀).sum_mem _ _ (fun a _ => hy a)
    · intro a ha
      by_cases h : r (z a) = 0
      · exact mul_nonneg (hw a) (hs a h)
      · simp [hzero a h]
    · simp_rw [mul_add, mul_one]
      rw [sum_add_distrib, hsum, hscore u, add_zero]
  · intro hx
    exact subset_convexHull ℝ _ ⟨a₀, hz₀.symm, hx⟩

end SharpOC
