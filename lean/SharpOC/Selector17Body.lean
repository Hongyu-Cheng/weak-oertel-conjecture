import SharpOC.Selector17Lattice
import SharpOC.Selector17Near
import SharpOC.Selector17SourceGeometry
import SharpOC.SelectorRoof

/-! The signed-selector convex hull, its affine roof and its integer fibers. -/

noncomputable section

namespace SharpOC.Selector17

open Set Finset
open scoped Pointwise
open SelectorSources (E B B_convex B_compact zero_mem_interior_B)

abbrev Ambient := IntegerSpace × E

def fiber : FiberIndex → Set E
  | none => B
  | some (.inl S) =>
    if S.val ∈ balancedMasks then (1 + delta) • K (selectedType S.val)
    else match nearType S with
      | some j => nearFiber j
      | none => h • B
  | some (.inr (j, _)) => (1 - delta) • T j

def generators : Set Ambient :=
  {p | ∃ i : FiberIndex, p.1 = base i ∧ p.2 ∈ fiber i}

def body : Set Ambient := convexHull ℝ generators

theorem fiber_convex (i : FiberIndex) : Convex ℝ (fiber i) := by
  rcases i with _ | (S | ⟨j, J⟩)
  · exact B_convex
  · simp only [fiber]
    split_ifs
    · exact (K_convex _).smul _
    · cases nearType S
      · exact B_convex.smul _
      · exact nearFiber_convex _
  · exact (T_convex _).smul _

theorem fiber_compact (i : FiberIndex) : IsCompact (fiber i) := by
  rcases i with _ | (S | ⟨j, J⟩)
  · exact B_compact
  · simp only [fiber]
    split_ifs
    · exact (K_compact _).smul _
    · cases nearType S
      · exact B_compact.smul _
      · exact nearFiber_compact _
  · exact (T_compact _).smul _

theorem fiber_nonempty (i : FiberIndex) : (fiber i).Nonempty := by
  rcases i with _ | (S | ⟨j, J⟩)
  · exact ⟨0, interior_subset zero_mem_interior_B⟩
  · simp only [fiber]
    split_ifs
    · exact (K_nonempty _).smul_set
    · cases nearType S
      · exact (show B.Nonempty from ⟨0, interior_subset zero_mem_interior_B⟩).smul_set
      · exact nearFiber_nonempty _
  · exact (T_nonempty _).smul_set

theorem body_compact : IsCompact body :=
  isCompact_fiber_convexHull base fiber fiber_convex fiber_nonempty fiber_compact

theorem body_convex : Convex ℝ body := convex_convexHull ℝ _

private theorem radius_pos (i : FiberIndex) : 0 < 1 + delta * guard (base i) := by
  rcases i with _ | (S | ⟨j, J⟩)
  · simp
  · have h := mul_le_mul_of_nonneg_left (heavy_guard S) delta_pos.le
    linarith [delta_pos]
  · rw [light_guard]
    linarith [delta_lt_one]

theorem fiber_subset_roof (i : FiberIndex) : fiber i ⊆ (1 + delta * guard (base i)) • B := by
  rcases i with _ | (S | ⟨j, J⟩)
  · simp [fiber]
  · simp only [fiber]
    split_ifs with hS
    · rw [paired_heavy_guard S hS, mul_one]
      exact smul_set_mono (K_subset_B _)
    · cases hn : nearType S with
      | some k =>
        rw [near_heavy_guard S hn, mul_comm delta 2]
        exact nearFiber_subset_roof k
      | none =>
        let r := 1 + delta * guard (base (some (.inl S)))
        have hr : 0 < r := radius_pos _
        have hle : h ≤ r := h_le_one_add_delta.trans (by
          have hb := mul_le_mul_of_nonneg_left (heavy_guard S) delta_pos.le
          dsimp [r]
          linarith)
        rintro _ ⟨y, hy, rfl⟩
        refine ⟨(h / r) • y, B_convex.smul_mem_of_zero_mem
          (interior_subset zero_mem_interior_B) hy
          ⟨div_nonneg h_pos.le hr.le, (div_le_one hr).mpr hle⟩, ?_⟩
        change r • ((h / r) • y) = h • y
        rw [← mul_smul, mul_div_cancel₀ _ hr.ne']
  · rw [light_guard]
    simpa only [fiber, mul_neg, mul_one, ← sub_eq_add_neg] using
      smul_set_mono (a := 1 - delta) (T_subset_B j)

theorem origin_fiber_exact : {x | ((0 : IntegerSpace), x) ∈ body} = B := by
  apply origin_fiber_of_affine_radius base fiber none base_none fiber_convex fiber_nonempty
    0 (delta • guard) (by simp)
  · intro i _
    simpa only [LinearMap.smul_apply, smul_eq_mul] using (radius_pos i).le
  · intro i _ x hx
    obtain ⟨y, hy, he⟩ := fiber_subset_roof i hx
    exact ⟨y, hy, by simpa only [LinearMap.smul_apply, smul_eq_mul] using he.symm⟩

theorem fiber_exact (i : FiberIndex) : {x | (base i, x) ∈ body} = fiber i := by
  by_cases hi : i = none
  · subst i
    simpa [fiber] using origin_fiber_exact
  · exact nonzero_base_fiber_exact fiber i hi (fiber_convex i) (fiber_nonempty i)

theorem integer_fiber_exact (i : FiberIndex) :
    {x | ((fun j => (integerBase i j : ℝ)), x) ∈ body} = fiber i := by
  simp only [integerBase_cast]
  exact fiber_exact i

theorem integer_base_census (z : Coordinate → ℤ) (x : E)
    (hx : ((fun j => (z j : ℝ)), x) ∈ body) : z ∈ range integerBase := by
  apply integer_projection_census
  rw [← projection_of_fiber_convexHull base fiber fiber_nonempty]
  exact ⟨_, hx, rfl⟩

set_option maxRecDepth 4096 in
theorem body_interior_nonempty : (interior body).Nonempty := by
  apply interior_convexHull_nonempty_iff_affineSpan_eq_top.mpr
  let S := affineSpan ℝ generators
  have hs (x : E) (hx : x ∈ B) : ((0 : IntegerSpace), x) ∈ S :=
    subset_affineSpan ℝ generators ⟨none, base_none.symm, hx⟩
  have hBtop : affineSpan ℝ B = ⊤ :=
    affineSpan_eq_top_of_nonempty_interior
      ⟨0, interior_mono (subset_convexHull ℝ B) zero_mem_interior_B⟩
  have hv (x : E) : ((0 : IntegerSpace), x) ∈ S := by
    let A := AffineSubspace.comap (LinearMap.inr ℝ IntegerSpace E).toAffineMap S
    have hBA : affineSpan ℝ B ≤ A := affineSpan_le.mpr hs
    have hA : A = ⊤ := top_unique (hBtop ▸ hBA)
    have hmem : x ∈ A := by rw [hA]; trivial
    exact hmem
  have htop : affineSpan ℝ (S : Set Ambient) = ⊤ := by
    apply affineSpan_eq_top_of_vertical_and_units B (S : Set Ambient) hBtop hs
    intro j
    let i : FiberIndex := some (.inl ⟨{j}, (mem_heavyMasks _).2 (Finset.singleton_nonempty j)⟩)
    obtain ⟨x, hx⟩ := fiber_nonempty i
    have hb : (base i, x) ∈ S := subset_affineSpan ℝ generators ⟨i, rfl, hx⟩
    have hd : (base i, (0 : E)) ∈ S.direction := by
      simpa only [vsub_eq_sub, Prod.mk_sub_mk, sub_zero, sub_self] using S.vsub_mem_direction hb (hv x)
    have hraw : raw {j} = cubeVector {j} := by
      ext k
      cases j with
      | inl q =>
        have hq : ({Sum.inl q} : Finset Coordinate).toRight = ∅ := by ext p; simp
        cases k <;> simp [raw, hq]
      | inr q => cases k <;> simp [raw, cubeVector]
    have hbase : base i = signedCubeVector (negative i) {j} := by
      change (if negative i then -raw {j} else raw {j}) = _
      rw [hraw]
      rfl
    have hu : (cubeVector {j}, (0 : E)) ∈ S.direction := by
      rcases hsign : negative i with _ | _
      · simpa [hbase, hsign, signedCubeVector] using hd
      · simpa [hbase, hsign, signedCubeVector] using S.direction.neg_mem hd
    refine ⟨0, (AffineSubspace.mem_coe _ _).2 ?_⟩
    simpa only [vadd_eq_add, Prod.mk_add_mk, add_zero] using S.vadd_mem_of_mem_direction hu (hv 0)
  rwa [S.affineSpan_coe] at htop

end SharpOC.Selector17
