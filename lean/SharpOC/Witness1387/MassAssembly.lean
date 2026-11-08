import SharpOC.Witness1387.BaselineCount
import SharpOC.Witness1387.MassCount

/-! From the active-pool census to the normalized total mass. -/

noncomputable section

namespace SharpOC.Witness1387

open scoped BigOperators

private abbrev baselineFintype : Fintype Baseline := inferInstance

private theorem pool_ge_55_of_some {b : Baseline} (h : (activeAxis b).isSome) :
    55 ≤ pool b 0 := by
  obtain ⟨i, hi⟩ := Option.isSome_iff_exists.mp h
  exact pool_ge_55_of_active hi 0

private theorem poolSize_poolIndex {b : Baseline} (h : (activeAxis b).isSome) :
    poolSize (poolIndex b) = pool b 0 := by
  have h₁ := pool_ge_55_of_some h
  have h₂ := pool_le_70 b 0
  change 55 + min 15 (pool b 0 - 55) = pool b 0
  omega

variable [baselineType : Fintype Baseline]

private def activeCenters : Finset Baseline :=
  Finset.univ.filter fun b => (activeAxis b).isSome

private def atLeastPool (k : ℕ) : Finset Baseline :=
  activeCenters.filter fun b => k ≤ pool b 0

private def unitSectors : Finset Baseline :=
  Finset.univ.filter fun b => ¬(activeAxis b).isSome ∧ (zeroSlots b).card ≤ 1

private def inactiveSimplices : Finset Baseline :=
  Finset.univ.filter fun b => ¬(activeAxis b).isSome ∧ ¬(zeroSlots b).card ≤ 1

set_option maxRecDepth 10000 in
private theorem active_count_at_least (k : ℕ)
    (h₁ : (Finset.univ.filter fun b : Baseline =>
      (zeroSlots b).card = 1 ∧ (activeAxis b).isSome ∧ k ≤ pool b 0).card = oldCount k)
    (h₂ : (Finset.univ.filter fun b : Baseline =>
      (zeroSlots b).card = 2 ∧ (activeAxis b).isSome ∧ k ≤ pool b 0).card = newCount k) :
    (atLeastPool k).card = oldCount k + newCount k := by
  let O := Finset.univ.filter fun b : Baseline =>
    (zeroSlots b).card = 1 ∧ (activeAxis b).isSome ∧ k ≤ pool b 0
  let E := Finset.univ.filter fun b : Baseline =>
    (zeroSlots b).card = 2 ∧ (activeAxis b).isSome ∧ k ≤ pool b 0
  have hdis : Disjoint O E := by
    apply Finset.disjoint_left.mpr
    intro b ho he
    have h₁' := (Finset.mem_filter.mp ho).2.1
    have h₂' := (Finset.mem_filter.mp he).2.1
    omega
  have hsplit : atLeastPool k = O ∪ E := by
    ext b
    simp only [atLeastPool, activeCenters, O, E, Finset.mem_filter, Finset.mem_univ,
      Finset.mem_union, true_and]
    constructor
    · rintro ⟨ha, hk⟩
      obtain ⟨i, hi⟩ := Option.isSome_iff_exists.mp ha
      rcases activeAxis_zeroSlots_cases hi with h | ⟨j, hij, h⟩
      · exact Or.inl ⟨by simp [h], ha, hk⟩
      · exact Or.inr ⟨by simp [h, Finset.card_pair hij], ha, hk⟩
    · rintro (⟨_, ha, hk⟩ | ⟨_, ha, hk⟩) <;> exact ⟨ha, hk⟩
  rw [hsplit, Finset.card_union_of_disjoint hdis, h₁, h₂]

set_option maxRecDepth 10000 in
private theorem active_histogram
    (hcounts : ∀ k : ℕ, 55 ≤ k → k ≤ 71 → (atLeastPool k).card = oldCount k + newCount k)
    (k : Fin 16) :
    (activeCenters.filter fun b => poolIndex b = k).card = centerCount k := by
  have hlo : 55 ≤ poolSize k := by simp [poolSize]
  have hhi : poolSize k + 1 ≤ 71 := by
    have := k.isLt
    unfold poolSize
    omega
  have hsub : atLeastPool (poolSize k + 1) ⊆ atLeastPool (poolSize k) := by
    intro b hb
    obtain ⟨ha, hp⟩ := Finset.mem_filter.mp hb
    exact Finset.mem_filter.mpr ⟨ha, by omega⟩
  have he : activeCenters.filter (fun b => poolIndex b = k) =
      atLeastPool (poolSize k) \ atLeastPool (poolSize k + 1) := by
    ext b
    simp only [atLeastPool, Finset.mem_filter, Finset.mem_sdiff]
    constructor
    · rintro ⟨ha, hindex⟩
      have hp := poolSize_poolIndex ((Finset.mem_filter.mp ha).2)
      rw [hindex] at hp
      exact ⟨⟨ha, hp.le⟩, fun h => by omega⟩
    · rintro ⟨⟨ha, hlow⟩, hhigh⟩
      have h : pool b 0 = poolSize k := by
        have hn : ¬poolSize k + 1 ≤ pool b 0 := fun hh => hhigh ⟨ha, hh⟩
        omega
      refine ⟨ha, Fin.ext ?_⟩
      have hp := poolSize_poolIndex ((Finset.mem_filter.mp ha).2)
      rw [h] at hp
      unfold poolSize at hp
      omega
  rw [he, Finset.card_sdiff_of_subset hsub, hcounts _ (by omega) hhi,
    hcounts _ hlo (by omega)]
  have hm := poolCounts_nonincreasing k
  unfold centerCount
  omega

set_option maxRecDepth 10000 in
private theorem inactive_simplex_count
    (hactive : activeCenters.card = oldCount 55 + newCount 55)
    (hunit : unitSectors.card = 2047 ^ 19 + resetCount) :
    inactiveSimplices.card = inactiveCount := by
  have hd : Disjoint activeCenters unitSectors := by
    apply Finset.disjoint_left.mpr
    intro b ha hu
    exact (Finset.mem_filter.mp hu).2.1 (Finset.mem_filter.mp ha).2
  have he : inactiveSimplices = Finset.univ \ (activeCenters ∪ unitSectors) := by
    ext b
    simp only [inactiveSimplices, activeCenters, unitSectors, Finset.mem_filter,
      Finset.mem_univ, Finset.mem_sdiff, Finset.mem_union, true_and]
    by_cases h : (activeAxis b).isSome <;> simp [h]
  have hcard : (Finset.univ : Finset Baseline).card = 2048 ^ 19 := by
    exact (@Fintype.card_congr Baseline Baseline baselineType baselineFintype
      (Equiv.refl Baseline)).trans baseline_count
  rw [he, Finset.card_sdiff_of_subset (Finset.subset_univ _), Finset.card_union_of_disjoint hd,
    hcard, hactive, hunit]
  unfold inactiveCount
  omega

set_option maxRecDepth 10000 in
/-- The ordinary and extra pool counts evaluate the actual source-mass sum. -/
theorem sourceMass_sum_of_pool_counts
    [Fintype {b : Baseline // (selectedFlip b).isSome}]
    (hordinary : ∀ k : ℕ, 55 ≤ k → k ≤ 71 →
      (Finset.univ.filter fun b : Baseline =>
        (zeroSlots b).card = 1 ∧ (activeAxis b).isSome ∧ k ≤ pool b 0).card = oldCount k)
    (hextra : ∀ k : ℕ, 55 ≤ k → k ≤ 71 →
      (Finset.univ.filter fun b : Baseline =>
        (zeroSlots b).card = 2 ∧ (activeAxis b).isSome ∧ k ≤ pool b 0).card = newCount k)
    (hunit : (Finset.univ.filter fun b : Baseline =>
      ¬(activeAxis b).isSome ∧ (zeroSlots b).card ≤ 1).card = 2047 ^ 19 + resetCount) :
    (∑ s : SupportIndex, sourceMass s) = normalizedTotal := by
  have hcounts (k : ℕ) (hk : 55 ≤ k) (hk' : k ≤ 71) :
      (atLeastPool k).card = oldCount k + newCount k :=
    active_count_at_least k (hordinary k hk hk') (hextra k hk hk')
  have ha : atLeastPool 55 = activeCenters := by
    exact Finset.filter_true_of_mem fun b hb => pool_ge_55_of_some (Finset.mem_filter.mp hb).2
  have hactive : activeCenters.card = oldCount 55 + newCount 55 := by
    rw [← ha]
    exact hcounts 55 (by decide) (by decide)
  let weight (k : Fin 16) : ℚ :=
    radius k ^ 1178 + 4 * (poolSize k : ℚ) * lightMass k
  have hweight : (∑ b ∈ activeCenters, weight (poolIndex b)) =
      ∑ k : Fin 16, (centerCount k : ℚ) * weight k := by
    rw [← Finset.sum_fiberwise activeCenters poolIndex]
    refine Finset.sum_congr rfl fun k _ => ?_
    rw [Finset.sum_congr rfl (g := fun _ => weight k)]
    · simp [Finset.sum_const, active_histogram hcounts k, nsmul_eq_mul]
    · intro b hb
      rw [(Finset.mem_filter.mp hb).2]
  rw [sum_sourceMass_by_center]
  change (∑ b : Baseline, if (activeAxis b).isSome then weight (poolIndex b)
    else if (zeroSlots b).card ≤ 1 then tau else inactiveMass) = _
  calc
    _ = ∑ b : Baseline,
        ((if ¬(activeAxis b).isSome ∧ (zeroSlots b).card ≤ 1 then tau else 0) +
        (if ¬(activeAxis b).isSome ∧ ¬(zeroSlots b).card ≤ 1 then inactiveMass else 0) +
        (if (activeAxis b).isSome then weight (poolIndex b) else 0)) := by
      apply Finset.sum_congr rfl
      intro b _
      by_cases ha : (activeAxis b).isSome <;>
        by_cases hz : (zeroSlots b).card ≤ 1 <;> simp [ha, hz]
    _ = (unitSectors.card : ℚ) * tau + (inactiveSimplices.card : ℚ) * inactiveMass +
        ∑ b ∈ activeCenters, weight (poolIndex b) := by
      simp only [Finset.sum_add_distrib, ← Finset.sum_filter, Finset.sum_const, nsmul_eq_mul,
        unitSectors, inactiveSimplices, activeCenters]
    _ = _ := by
      change unitSectors.card = _ at hunit
      rw [hunit, inactive_simplex_count hactive hunit, hweight]
      rfl

end SharpOC.Witness1387
