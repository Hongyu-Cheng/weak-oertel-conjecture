import SharpOC.Selector17Census

/-! Strict exposure of the nonzero sites of the signed selector support. -/

noncomputable section

namespace SharpOC.Selector17

open scoped BigOperators

private theorem lex_exposes (i : FiberIndex) (l r : IntegerSpace →ₗ[ℝ] ℝ)
    (hl : ∀ j, l (base j) ≤ l (base i))
    (hr : ∀ j, j ≠ i → l (base j) = l (base i) → r (base j) < r (base i)) :
    ∃ f : IntegerSpace →ₗ[ℝ] ℝ, ∀ j, j ≠ i → f (base j) < f (base i) := by
  classical
  let q (j : FiberIndex) := max 0 ((r (base j) - r (base i)) / (l (base i) - l (base j)))
  let M := 1 + ∑ j, q j
  refine ⟨M • l + r, fun j hj => ?_⟩
  change M * l (base j) + r (base j) < M * l (base i) + r (base i)
  by_cases he : l (base j) = l (base i)
  · rw [he]
    linarith [hr j hj he]
  · have hlt : l (base j) < l (base i) := lt_of_le_of_ne (hl j) he
    have hq : q j ≤ ∑ k, q k :=
      Finset.single_le_sum (f := q) (fun k _ => le_max_left _ _) (Finset.mem_univ j)
    have hM : (r (base j) - r (base i)) / (l (base i) - l (base j)) < M :=
      lt_of_le_of_lt (le_max_right _ _) (by dsimp [M]; linarith)
    have hh := (div_lt_iff₀ (sub_pos.mpr hlt)).mp hM
    linarith [mul_sub M (l (base i)) (l (base j))]

private def selectorProjection : IntegerSpace →ₗ[ℝ] (Fin 2 → ℝ) :=
  LinearMap.pi fun j => LinearMap.proj (Sum.inr j)

private theorem selectorProjection_base (i : FiberIndex) :
    selectorProjection (base i) = signedCubeVector (negative i) (mask i).toRight := by
  ext j
  cases h : negative i <;> by_cases hj : Sum.inr j ∈ mask i <;>
    simp [selectorProjection, selector_base, orientation, h, signedCubeVector, cubeVector, hj]

private def flip : IntegerSpace →ₗ[ℝ] IntegerSpace :=
  LinearMap.pi fun j => Sum.elim ordinarySign (fun _ => 1) j • LinearMap.proj j

private theorem flip_injective : Function.Injective flip := by
  intro x y h
  ext j
  have hj := congrFun h j
  cases j with
  | inl k =>
    rcases ordinarySign_cases k with hk | hk <;> simpa [flip, hk] using hj
  | inr k => simpa [flip] using hj

private theorem flip_base {i : FiberIndex} (h : (mask i).toRight ≠ ∅) :
    flip (base i) = signedCubeVector (negative i) (mask i) := by
  ext j
  cases j with
  | inl k =>
    rcases ordinarySign_cases k with hk | hk <;> cases hs : negative i <;>
      by_cases hj : Sum.inl k ∈ mask i <;>
      simp [flip, ordinary_base, orientation, signedCubeVector, cubeVector, hk, hs, h, hj]
  | inr k =>
    cases hs : negative i <;> by_cases hj : Sum.inr k ∈ mask i <;>
      simp [flip, selector_base, orientation, signedCubeVector, cubeVector, hs, hj]

private theorem expose_nonzero_selector (i : FiberIndex) (hi : (mask i).toRight ≠ ∅) :
    ∃ f : IntegerSpace →ₗ[ℝ] ℝ, ∀ j, j ≠ i → f (base j) < f (base i) := by
  let l := (signedCubeExposingFunctional (negative i) (mask i).toRight).comp selectorProjection
  let r := (signedCubeExposingFunctional (negative i) (mask i)).comp flip
  have hs (j : FiberIndex) (h : selectorProjection (base j) ≠ selectorProjection (base i)) :
      l (base j) < l (base i) := by
    rw [selectorProjection_base, selectorProjection_base] at h
    simpa only [l, LinearMap.comp_apply, selectorProjection_base] using
      signedCube_exposes _ _ (Finset.nonempty_iff_ne_empty.mpr hi) _ _ h
  apply lex_exposes i l r
  · intro j
    by_cases h : selectorProjection (base j) = selectorProjection (base i)
    · simp [l, h]
    · exact (hs j h).le
  · intro j hj he
    have h : selectorProjection (base j) = selectorProjection (base i) := by
      by_contra h
      exact (hs j h).ne he
    rw [selectorProjection_base, selectorProjection_base] at h
    have hn : (mask j).toRight ≠ ∅ := by
      simpa [signedCubeVector_support_eq h] using hi
    have hm : (mask i).Nonempty := by
      obtain ⟨k, hk⟩ := Finset.nonempty_iff_ne_empty.mpr hi
      exact ⟨Sum.inr k, Finset.mem_toRight.mp hk⟩
    have hne : flip (base j) ≠ flip (base i) :=
      fun he => hj (base_injective (flip_injective he))
    rw [flip_base hn, flip_base hi] at hne
    simpa only [r, LinearMap.comp_apply, flip_base hn, flip_base hi] using
      signedCube_exposes _ _ hm _ _ hne

private theorem expose_zero_selector (i : FiberIndex) (hi : i ≠ none)
    (ht : (mask i).toRight = ∅) :
    ∃ f : IntegerSpace →ₗ[ℝ] ℝ, ∀ j, j ≠ i → f (base j) < f (base i) := by
  obtain ⟨q, hq⟩ := mask_nonempty i hi
  obtain ⟨k, rfl⟩ : ∃ k : Fin 10, Sum.inl k = q := by
    cases q with
    | inl k => exact ⟨k, rfl⟩
    | inr k =>
      have hk := Finset.mem_toRight.mpr hq
      simp [ht] at hk
  let l : IntegerSpace →ₗ[ℝ] ℝ :=
    (3 : ℝ) • LinearMap.proj (Sum.inl k) - ordinarySign k • selectorSum
  let r := signedCubeExposingFunctional false (mask i)
  have hli : l (base i) = 3 := by
    have hs : selectorSum (base i) = 0 := by simp [selectorSum_base, ht]
    have hk : base i (.inl k) = 1 := by simp [zero_selector_base ht, cubeVector, hq]
    simp [l, hs, hk]
  have hscore (j : FiberIndex) :
      l (base j) ≤ 3 ∧ (l (base j) = 3 → (mask j).toRight = ∅) := by
    have hc := Finset.card_le_univ (mask j).toRight
    simp only [Fintype.card_fin] at hc
    by_cases he : (mask j).toRight = ∅
    · have hu := (base_coord_bounds j (.inl k)).2
      have hsum : selectorSum (base j) = 0 := by simp [selectorSum_base, he]
      constructor
      · simp only [l, LinearMap.sub_apply, LinearMap.smul_apply, LinearMap.proj_apply,
          smul_eq_mul, hsum, mul_zero, sub_zero]
        linarith
      · exact fun _ => he
    · have hpos : 0 < (mask j).toRight.card :=
        Finset.card_pos.mpr (Finset.nonempty_iff_ne_empty.mpr he)
      have hc' : ((mask j).toRight.card : ℝ) ≤ 2 := by exact_mod_cast hc
      have hp' : 0 < ((mask j).toRight.card : ℝ) := by exact_mod_cast hpos
      have hlt : l (base j) < 3 := by
        change 3 * base j (.inl k) - ordinarySign k * selectorSum (base j) < 3
        rw [selectorSum_base, ordinary_base, ite_eq_right he]
        rcases ordinarySign_cases k with hk | hk <;>
          rcases orientation_cases j with hs | hs <;>
          by_cases hm : k ∈ (mask j).toLeft <;>
          simp only [hk, hs, hm, ite_true, ite_false] <;> linarith
      exact ⟨hlt.le, fun h => (hlt.ne h).elim⟩
  apply lex_exposes i l r
  · intro j
    simpa only [hli] using (hscore j).1
  · intro j hj he
    have htj := (hscore j).2 (he.trans hli)
    have hne : signedCubeVector false (mask j) ≠ signedCubeVector false (mask i) := by
      simpa [signedCubeVector, zero_selector_base ht, zero_selector_base htj] using
        (fun h => hj (base_injective h) : base j ≠ base i)
    simpa [r, signedCubeVector, zero_selector_base ht, zero_selector_base htj] using
      signedCube_exposes false _ (mask_nonempty i hi) false _ hne

theorem base_exposed (i : FiberIndex) (hi : i ≠ none) :
    ∃ l : IntegerSpace →ₗ[ℝ] ℝ, ∀ j, j ≠ i → l (base j) < l (base i) := by
  by_cases h : (mask i).toRight = ∅
  · exact expose_zero_selector i hi h
  · exact expose_nonzero_selector i h

theorem nonzero_base_fiber_exact {E : Type*} [AddCommGroup E] [Module ℝ E]
    (K : FiberIndex → Set E) (i : FiberIndex) (hi : i ≠ none)
    (hK : Convex ℝ (K i)) (hne : (K i).Nonempty) :
    {x | (base i, x) ∈ convexHull ℝ
      {p : IntegerSpace × E | ∃ j, p.1 = base j ∧ p.2 ∈ K j}} = K i := by
  obtain ⟨l, hl⟩ := base_exposed i hi
  exact exposed_fiber_convexHull base K i hK hne l hl

end SharpOC.Selector17
