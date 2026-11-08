import SharpOC.Witness1387.ExposedCaps

/-! The rational witness spans all 1387 coordinates. -/

noncomputable section

namespace SharpOC.Witness1387

open Set
open scoped BigOperators

private def zeroBaseline : Baseline := fun _ => 0

private theorem zero_base : base (.inl zeroBaseline) = 0 := by
  funext c
  simp [base, integerBase, integerBlock, zeroBaseline]

private theorem zeroSlots_card : (zeroSlots zeroBaseline).card = 19 := by
  have h : zeroSlots zeroBaseline = Finset.univ := by
    ext i
    simp [zeroBaseline]
  simp [h, Block]

private theorem zeroBaseline_inactive : ¬(activeAxis zeroBaseline).isSome := by
  have hlen : (zeroSlots zeroBaseline).sort.length = 19 := by
    rw [Finset.length_sort, zeroSlots_card]
  unfold activeAxis
  split <;> simp_all

private def axisSlot (j : Fin 11) : Slot :=
  ⟨2 ^ j.val, by fin_cases j <;> decide⟩

private theorem axisSlot_base (j k : Fin 11) :
    localBase (axisSlot j) k = if k = j then (if j.val < 8 then 1 else -1) else 0 := by
  fin_cases j <;> fin_cases k <;> decide +kernel

private def axisVector (c : Coordinate) : Coordinate → ℝ :=
  fun j => if j = c then 1 else 0

private def axisBaseline (c : Coordinate) : Baseline :=
  Function.update zeroBaseline c.1 (axisSlot c.2)

private theorem axis_base (c : Coordinate) :
    base (.inl (axisBaseline c)) =
      (if c.2.val < 8 then (1 : ℝ) else -1) • axisVector c := by
  rcases c with ⟨i, j⟩
  funext c
  rcases c with ⟨k, l⟩
  by_cases hk : k = i
  · subst k
    by_cases hl : l = j <;> simp [base, integerBase, integerBlock, axisBaseline,
      axisVector, axisSlot_base, hl]
  · simp [base, integerBase, integerBlock, axisBaseline, zeroBaseline, axisVector, hk]

private theorem linearImageSimplex_span {d : ℕ}
    (L : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (hL : Function.Injective L) :
    affineSpan ℝ (L '' BoxPadding.simplex d) = ⊤ := by
  have h : Function.Injective L.toAffineMap := fun _ _ he => hL he
  let a := affineImageBasis (MiddleSimplex.standardBasis d) L.toAffineMap h
  have ha : convexHull ℝ (range a) = L '' BoxPadding.simplex d :=
    affineImageBasis_hull _ _ _
  rw [← ha, affineSpan_convexHull]
  exact a.tot

theorem body_interior_nonempty : (interior body).Nonempty := by
  let S := affineSpan ℝ body
  have hv (x : E) : ((0 : Coordinate → ℝ), x) ∈ S := by
    let L := AffineSubspace.comap (LinearMap.inr ℝ (Coordinate → ℝ) E).toAffineMap S
    have hspan : affineSpan ℝ (source (.inl zeroBaseline)) ≤ L := by
      apply affineSpan_le.mpr
      intro y hy
      have hm := prescribed_source_mem (.inl zeroBaseline) hy
      rw [zero_base] at hm
      exact subset_affineSpan ℝ body hm
    have hsrc : source (.inl zeroBaseline) = inactiveSimplex (inactiveMass : ℝ) :=
      source_eq_inactive zeroBaseline zeroBaseline_inactive (by rw [zeroSlots_card]; decide)
    have hm : 0 < (inactiveMass : ℝ) := by exact_mod_cast
      (lt_trans (by norm_num [tau] : 0 < tau) tau_lt_inactiveMass)
    have htop : affineSpan ℝ (source (.inl zeroBaseline)) = ⊤ := by
      rw [hsrc]
      exact linearImageSimplex_span (inactiveMap _) (inactiveMap_injective hm)
    have he : L = ⊤ := top_unique (htop ▸ hspan)
    have hx : x ∈ L := by rw [he]; trivial
    exact hx
  have haxis (c : Coordinate) : (axisVector c, (0 : E)) ∈ S.direction := by
    let i : SupportIndex := .inl (axisBaseline c)
    obtain ⟨x, hx⟩ := source_nonempty i
    have hmem : (base i, x) ∈ S :=
      subset_affineSpan ℝ body (prescribed_source_mem i hx)
    have hd : (base i, (0 : E)) ∈ S.direction := by
      simpa [vsub_eq_sub] using S.vsub_mem_direction hmem (hv x)
    by_cases hc : c.2.val < 8
    · simpa [i, axis_base, hc] using hd
    · simpa [i, axis_base, hc] using S.direction.neg_mem hd
  have hS : S = ⊤ := by
    apply top_unique
    intro p _
    have hs : (∑ c : Coordinate, p.1 c • (axisVector c, (0 : E))) ∈ S.direction :=
      S.direction.sum_mem (fun c _ => S.direction.smul_mem (p.1 c) (haxis c))
    have he : (∑ c : Coordinate, p.1 c • (axisVector c, (0 : E))) = (p.1, 0) := by
      apply Prod.ext
      · funext j
        simp only [Prod.fst_sum, Prod.smul_mk, Finset.sum_apply, Pi.smul_apply,
          smul_eq_mul, axisVector]
        rw [Finset.sum_eq_single j]
        · simp
        · intro k _ hk
          simp [hk.symm]
        · simp
      · simp [Prod.snd_sum]
    rw [he] at hs
    simpa [vadd_eq_add] using S.vadd_mem_of_mem_direction hs (hv p.2)
  have hn := (interior_convexHull_nonempty_iff_affineSpan_eq_top (s := body)).mpr hS
  simpa only [body_convex.convexHull_eq] using hn

end SharpOC.Witness1387
