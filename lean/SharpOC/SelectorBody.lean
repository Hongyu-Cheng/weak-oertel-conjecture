import SharpOC.SelectorBases
import SharpOC.SelectorRoof
import SharpOC.SelectorSources

/-! The convex hull of the signed selector fibers and its integer census. -/

noncomputable section

namespace SharpOC.Selector

open Set Finset
open scoped BigOperators Pointwise
open SelectorSources

abbrev Ambient := IntegerSpace × E

def fiber : FiberIndex → Set E
  | none => B
  | some (.inl S) => (1 + delta) • U (selectedType S.val)
  | some (.inr (j, _)) => (1 - delta) • T j

def generators : Set Ambient :=
  {p | ∃ i : FiberIndex, p.1 = base i ∧ p.2 ∈ fiber i}

def body : Set Ambient := convexHull ℝ generators

theorem fiber_convex (i : FiberIndex) : Convex ℝ (fiber i) := by
  rcases i with _ | (S | ⟨j, J⟩)
  · exact B_convex
  · exact (U_convex _).smul _
  · exact (T_convex _).smul _

theorem fiber_compact (i : FiberIndex) : IsCompact (fiber i) := by
  rcases i with _ | (S | ⟨j, J⟩)
  · exact B_compact
  · exact (U_compact _).smul _
  · exact (T_compact _).smul _

theorem fiber_nonempty (i : FiberIndex) : (fiber i).Nonempty := by
  rcases i with _ | (S | ⟨j, J⟩)
  · exact ⟨0, interior_subset zero_mem_interior_B⟩
  · exact (U_nonempty _).smul_set
  · exact (T_nonempty _).smul_set

theorem body_compact : IsCompact body :=
  isCompact_fiber_convexHull base fiber fiber_convex fiber_nonempty fiber_compact

theorem body_convex : Convex ℝ body := convex_convexHull ℝ _

theorem roof_heavy (S : ↥heavyMasks)
    (h : balance (base (some (.inl S))) = 0) :
    1 + delta ≤ 1 + roofTilt (base (some (.inl S))) := by
  obtain ⟨hbase, hbalance⟩ := balanced_heavy_positive S h
  obtain ⟨j, hj⟩ := balanced_heavy_has_selector S hbalance
  have hc : 1 ≤ S.val.toRight.card :=
    Finset.card_pos.mpr ⟨j, Finset.mem_toRight.mpr hj⟩
  rw [hbase, roofTilt_cube]
  have hc' : (1 : ℝ) ≤ S.val.toRight.card := by exact_mod_cast hc
  have hd : 0 ≤ delta := by norm_num [delta]
  nlinarith

theorem roof_light (j : Fin 3) (J : ↥lightMasks) :
    roofTilt (base (some (.inr (j, J)))) = -delta := by
  simp [base, mask, negative, signedCubeVector, roofTilt_cube, lightMask]

theorem origin_fiber_exact : {x | ((0 : IntegerSpace), x) ∈ body} = B := by
  apply origin_fiber_of_affine_radius base fiber none base_none fiber_convex fiber_nonempty
    balance roofTilt balance_base_nonneg
  · intro i hi
    rcases i with _ | (S | ⟨j, J⟩)
    · simp
    · have h := roof_heavy S hi
      have hd : 0 ≤ delta := by norm_num [delta]
      linarith
    · rw [roof_light]
      norm_num [delta]
  · intro i hi x hx
    rcases i with _ | (S | ⟨j, J⟩)
    · exact ⟨x, hx, by simp⟩
    · obtain ⟨y, hy, rfl⟩ := hx
      have hr := roof_heavy S hi
      have hd : 0 < 1 + delta := by norm_num [delta]
      have hs : 0 < 1 + roofTilt (base (some (.inl S))) := hd.trans_le hr
      let s := 1 + roofTilt (base (some (.inl S)))
      have hs' : s ≠ 0 := hs.ne'
      refine ⟨((1 + delta) / s) • y, ?_, ?_⟩
      · exact B_convex.smul_mem_of_zero_mem
          (interior_subset zero_mem_interior_B) (U_subset_B _ hy)
          ⟨div_nonneg hd.le hs.le, (div_le_one hs).mpr hr⟩
      · rw [← mul_smul]
        change (1 + delta) • y = (s * ((1 + delta) / s)) • y
        rw [← mul_div_assoc, mul_div_cancel_left₀ _ hs']
    · obtain ⟨y, hy, rfl⟩ := hx
      exact ⟨y, hy.1, by simp [roof_light, sub_eq_add_neg]⟩

theorem signed_base (i : FiberIndex) :
    ∃ s S, base i = signedCubeVector s S := ⟨negative i, mask i, rfl⟩

theorem fiber_exact (i : FiberIndex) : {x | (base i, x) ∈ body} = fiber i := by
  by_cases h : i = none
  · subst i
    simpa [fiber] using origin_fiber_exact
  · exact signedCube_fiber_convexHull_exact base signed_base fiber i (negative i) (mask i)
      (mask_nonempty i h) rfl (fun j hj => base_injective hj)
      (fiber_convex i) (fiber_nonempty i)

theorem integer_fiber_exact (i : FiberIndex) :
    {x | ((fun j => (integerBase i j : ℝ)), x) ∈ body} = fiber i := by
  simp only [integerBase_cast]
  exact fiber_exact i

theorem integer_base_census (z : Coordinate → ℤ) (x : E)
    (h : ((fun j => (z j : ℝ)), x) ∈ body) : z ∈ range integerBase := by
  by_cases hz : z = 0
  · subst z
    exact ⟨none, by ext j; simp [integerBase, mask]⟩
  · have hp : (fun j => (z j : ℝ)) ∈ convexHull ℝ (range base) := by
      rw [← projection_of_fiber_convexHull base fiber fiber_nonempty]
      exact ⟨_, h, rfl⟩
    obtain ⟨i, hi⟩ := (integer_mem_signed_projection_convexHull_iff base signed_base z hz).mp hp
    refine ⟨i, ?_⟩
    rw [← integerBase_cast] at hi
    funext j
    exact_mod_cast congrFun hi j

theorem base_exposed (i : FiberIndex) (h : i ≠ none) :
    ∀ j, j ≠ i →
      signedCubeExposingFunctional (negative i) (mask i) (base j) <
      signedCubeExposingFunctional (negative i) (mask i) (base i) := by
  intro j hj
  exact signedCube_exposes _ _ (mask_nonempty i h) _ _
    (fun he => hj (base_injective he))

theorem body_interior_nonempty : (interior body).Nonempty := by
  apply interior_convexHull_nonempty_iff_affineSpan_eq_top.mpr
  let S := affineSpan ℝ generators
  have hv : ∀ x : E, ((0 : IntegerSpace), x) ∈ S := by
    let L := AffineSubspace.comap (LinearMap.inr ℝ IntegerSpace E).toAffineMap S
    have hBL : affineSpan ℝ B ≤ L := by
      apply affineSpan_le.mpr
      intro x hx
      exact subset_affineSpan ℝ generators ⟨none, base_none.symm, hx⟩
    have hBtop : affineSpan ℝ B = ⊤ :=
      affineSpan_eq_top_of_nonempty_interior
        ⟨0, interior_mono (subset_convexHull ℝ B) zero_mem_interior_B⟩
    have hLtop : L = ⊤ := top_unique (hBtop ▸ hBL)
    intro x
    have h : x ∈ L := by rw [hLtop]; trivial
    exact h
  have hu (j : Coordinate) : (cubeVector {j}, (0 : E)) ∈ S.direction := by
    let i : FiberIndex := some (.inl ⟨{j}, by simp⟩)
    obtain ⟨x, hx⟩ := fiber_nonempty i
    have hbx : (base i, x) ∈ S :=
      subset_affineSpan ℝ generators ⟨i, rfl, hx⟩
    have hb : (base i, (0 : E)) ∈ S.direction := by
      simpa [vsub_eq_sub] using S.vsub_mem_direction hbx (hv x)
    rcases hsign : negative i with _ | _
    · simpa [base, hsign, signedCubeVector, mask, i] using hb
    · simpa [base, hsign, signedCubeVector, mask, i] using S.direction.neg_mem hb
  apply top_unique
  intro p hp
  have hs : (∑ j : Coordinate, p.1 j • (cubeVector {j}, (0 : E))) ∈ S.direction :=
    S.direction.sum_mem (fun j _ => S.direction.smul_mem (p.1 j) (hu j))
  have he : (∑ j : Coordinate, p.1 j • (cubeVector {j}, (0 : E))) = (p.1, 0) := by
    ext j
    · simp only [Prod.fst_sum, Prod.smul_mk, Finset.sum_apply, Pi.smul_apply,
        smul_eq_mul, cubeVector, Finset.mem_singleton]
      rw [Finset.sum_eq_single j]
      · simp
      · intro k hk hkj
        simp [Ne.symm hkj]
      · simp
    · simp [Prod.snd_sum]
  rw [he] at hs
  simpa [vadd_eq_add] using S.vadd_mem_of_mem_direction hs (hv p.2)

end SharpOC.Selector
