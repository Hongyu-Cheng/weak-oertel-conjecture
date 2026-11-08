import SharpOC.Witness1387.Measure

/-! Exact volumes of the prescribed sources and cap bounds at strictly exposed
integer bases. -/

noncomputable section

namespace SharpOC.Witness1387

open Set MeasureTheory
open scoped ENNReal

theorem source_eq_center (b : Baseline) (h : (activeAxis b).isSome) :
    source (.inl b) = dilate (radius (poolIndex b) : ℝ) B := by
  rw [source, sourceVertices, ite_eq_left h, centerVertices_hull]

theorem source_eq_unitSector (b : Baseline) (h : ¬(activeAxis b).isSome)
    (hz : (zeroSlots b).card ≤ 1) : source (.inl b) = T (label b) := by
  rw [source, sourceVertices, ite_eq_right h, ite_eq_left hz, sectorVertices_hull]
  simp [dilate]

theorem source_eq_inactive (b : Baseline) (h : ¬(activeAxis b).isSome)
    (hz : ¬(zeroSlots b).card ≤ 1) : source (.inl b) = inactiveSimplex (inactiveMass : ℝ) := by
  rw [source, sourceVertices, ite_eq_right h, ite_eq_right hz, inactiveVertices_hull]

theorem source_eq_light (b : {b : Baseline // (selectedFlip b).isSome}) :
    source (.inr b) =
      dilate (2 * (radius (poolIndex (lightCenter b.val)) : ℝ) - 1) (T (label b.val)) := by
  rw [source, sourceVertices, sectorVertices_hull]
  push_cast
  rfl

theorem source_nonempty (i : SupportIndex) : (source i).Nonempty := by
  rcases i with b | b
  · by_cases h : (activeAxis b).isSome
    · rw [source_eq_center b h]
      exact dilate_nonempty _ B_nonempty
    · by_cases hz : (zeroSlots b).card ≤ 1
      · rw [source_eq_unitSector b h hz]
        exact T_nonempty _
      · rw [source_eq_inactive b h hz]
        exact inactiveSimplex_nonempty _
  · rw [source_eq_light]
    exact dilate_nonempty _ (T_nonempty _)

/-- The mass of a prescribed source in product-simplex volume units. -/
def sourceMass : SupportIndex → ℚ
  | .inl b =>
      if (activeAxis b).isSome then radius (poolIndex b) ^ 1178
      else if (zeroSlots b).card ≤ 1 then tau else inactiveMass
  | .inr b => lightMass (poolIndex (lightCenter b.val))

private theorem inactiveMass_pos_real : (0 : ℝ) < (inactiveMass : ℝ) := by
  exact_mod_cast (lt_trans (by norm_num [tau] : 0 < tau) tau_lt_inactiveMass)

theorem source_volume (i : SupportIndex) :
    volume (source i) = ENNReal.ofReal (sourceMass i : ℝ) * volume B := by
  rcases i with b | b
  · by_cases h : (activeAxis b).isSome
    · have hr : 0 ≤ (radius (poolIndex b) : ℝ) := by
        exact_mod_cast (le_trans (by norm_num : (0 : ℚ) ≤ 1 / 2) (radius_half_lt _).le)
      rw [source_eq_center b h, sourceMass, ite_eq_left h, dilate_volume hr, Rat.cast_pow]
    · by_cases hz : (zeroSlots b).card ≤ 1
      · rw [source_eq_unitSector b h hz, sourceMass, ite_eq_right h, ite_eq_left hz, T_volume]
        norm_num [tau]
      · rw [source_eq_inactive b h hz, sourceMass, ite_eq_right h, ite_eq_right hz,
          inactiveSimplex_volume inactiveMass_pos_real]
  · have hr : (0 : ℝ) ≤ 2 * (radius (poolIndex (lightCenter b.val)) : ℝ) - 1 := by
      exact_mod_cast (by linarith [radius_half_lt (poolIndex (lightCenter b.val))] :
        (0 : ℚ) ≤ 2 * radius (poolIndex (lightCenter b.val)) - 1)
    rw [source_eq_light, sourceMass, dilate_volume hr, T_volume, ← mul_assoc,
      ← ENNReal.ofReal_mul (by positivity)]
    congr 2
    simp only [lightMass, tau, Rat.cast_mul, Rat.cast_div, Rat.cast_ofNat, Rat.cast_pow,
      Rat.cast_sub, Rat.cast_one]
    exact mul_comm _ _

theorem exposed_source_volume (i : SupportIndex) (ell : (Coordinate → ℝ) →ₗ[ℝ] ℝ)
    (hexp : ∀ j, j ≠ i → ell (base j) < ell (base i)) :
    volume {x | (base i, x) ∈ body} =
      ENNReal.ofReal (sourceMass i : ℝ) * volume B := by
  rw [source_eq_at_exposed_base i (source_nonempty i) ell hexp, source_volume]

private theorem lift_exposed_cap (i : SupportIndex) (ell : (Coordinate → ℝ) →ₗ[ℝ] ℝ)
    (hexp : ∀ j, j ≠ i → ell (base j) < ell (base i))
    (x : E) (h : E →L[ℝ] ℝ) (t : ℝ) (hn : h ≠ 0) (hx : t ≤ h x)
    (hcap : volume (source i ∩ {y | t ≤ h y}) ≤
      ENNReal.ofReal (capBound : ℝ) * volume B) :
    ∃ F : Ambient →L[ℝ] ℝ, ∃ u : ℝ, F ≠ 0 ∧ u ≤ F (base i, x) ∧
      (Selector.mixedIntegerMass (body ∩ {p | u ≤ F p})).toReal ≤
        (capBound : ℝ) * (volume B).toReal := by
  classical
  letI : Fintype SupportIndex := Fintype.ofFinite _
  obtain ⟨F, u, hF, hcut, hout⟩ := exposed_fiber_cut base
    (fun j => integerFiber (integerBase j)) (fun j => integerFiber_compact (integerBase j))
    i ell.toContinuousLinearMap hexp h hn t
  refine ⟨F, u, hF, (hcut x).mp hx, ?_⟩
  have hbound : Selector.mixedIntegerMass (body ∩ {p | u ≤ F p}) ≤
      ENNReal.ofReal (capBound : ℝ) * volume B := by
    have hcen (w : Coordinate → ℤ) (y : E) (hy : y ∈ integerFiber w) : w ∈ range integerBase :=
      (integerFiber_nonempty_iff source_nonempty w).mp ⟨y, hy⟩
    rw [Selector.mixedIntegerMass_eq_sum_of_subset (C := body)
      inter_subset_left integerBase integerBase_injective hcen, Finset.sum_eq_single i]
    · have he : {y : E | (base i, y) ∈ body ∩ {p | u ≤ F p}} =
          source i ∩ {y | t ≤ h y} := by
        change {y | (base i, y) ∈ body} ∩ {y | u ≤ F (base i, y)} = _
        rw [source_eq_at_exposed_base i (source_nonempty i) ell hexp]
        ext y
        exact and_congr_right (fun _ => (hcut y).symm)
      change volume {y : E | (base i, y) ∈ body ∩ {p | u ≤ F p}} ≤ _
      rwa [he]
    · intro j _ hji
      have he : {y : E | (base j, y) ∈ body ∩ {p | u ≤ F p}} = ∅ :=
        eq_empty_iff_forall_notMem.mpr fun y hy => (hout j hji y hy.1).not_ge hy.2
      change volume {y : E | (base j, y) ∈ body ∩ {p | u ≤ F p}} = 0
      rw [he, measure_empty]
    · simp
  have hc : (0 : ℝ) ≤ (capBound : ℝ) := by exact_mod_cast capBound_pos.le
  have hreal := ENNReal.toReal_mono (ENNReal.mul_ne_top (by simp) B_volume_ne_top) hbound
  simpa only [ENNReal.toReal_mul, ENNReal.toReal_ofReal hc] using hreal

theorem exposed_unitSector_cap (b : Baseline) (h : ¬(activeAxis b).isSome)
    (hz : (zeroSlots b).card ≤ 1) (ell : (Coordinate → ℝ) →ₗ[ℝ] ℝ)
    (hexp : ∀ j, j ≠ .inl b → ell (base j) < ell (base (.inl b))) (x : E) :
    ∃ F : Ambient →L[ℝ] ℝ, ∃ t : ℝ, F ≠ 0 ∧ t ≤ F (base (.inl b), x) ∧
      (Selector.mixedIntegerMass (body ∩ {p | t ≤ F p})).toReal ≤
        (capBound : ℝ) * (volume B).toReal := by
  obtain ⟨g, t, hn, hx, hc⟩ := T_small_halfspace (label b) x
  apply lift_exposed_cap (.inl b) ell hexp x g t hn hx
  rw [source_eq_unitSector b h hz, hc, T_volume, ← mul_assoc,
    ← ENNReal.ofReal_mul (by positivity)]
  apply le_of_eq
  congr 2
  norm_num only [capBound, tau, Rat.cast_mul, Rat.cast_pow, Rat.cast_div, Rat.cast_ofNat]

theorem exposed_inactiveSimplex_cap (b : Baseline) (h : ¬(activeAxis b).isSome)
    (hz : ¬(zeroSlots b).card ≤ 1) (ell : (Coordinate → ℝ) →ₗ[ℝ] ℝ)
    (hexp : ∀ j, j ≠ .inl b → ell (base j) < ell (base (.inl b))) (x : E) :
    ∃ F : Ambient →L[ℝ] ℝ, ∃ t : ℝ, F ≠ 0 ∧ t ≤ F (base (.inl b), x) ∧
      (Selector.mixedIntegerMass (body ∩ {p | t ≤ F p})).toReal ≤
        (capBound : ℝ) * (volume B).toReal := by
  obtain ⟨g, t, hn, hx, hc⟩ := inactiveSimplex_small_halfspace inactiveMass_pos_real x
  apply lift_exposed_cap (.inl b) ell hexp x g t hn hx
  rw [source_eq_inactive b h hz, hc, inactiveSimplex_volume inactiveMass_pos_real,
    ← mul_assoc, ← ENNReal.ofReal_mul (by positivity)]
  have hb : (1178 / 1179 : ℝ) ^ 1178 * (inactiveMass : ℝ) ≤ (capBound : ℝ) := by
    have h' : ((gamma : ℝ) * (inactiveMass : ℝ)) ≤ (capBound : ℝ) := by
      exact_mod_cast inactiveCap_lt_capBound.le
    simpa only [gamma, Rat.cast_pow, Rat.cast_div, Rat.cast_ofNat] using h'
  exact mul_le_mul_of_nonneg_right (ENNReal.ofReal_le_ofReal hb) zero_le

theorem exposed_light_cap (b : {b : Baseline // (selectedFlip b).isSome})
    (ell : (Coordinate → ℝ) →ₗ[ℝ] ℝ)
    (hexp : ∀ j, j ≠ .inr b → ell (base j) < ell (base (.inr b))) (x : E) :
    ∃ F : Ambient →L[ℝ] ℝ, ∃ t : ℝ, F ≠ 0 ∧ t ≤ F (base (.inr b), x) ∧
      (Selector.mixedIntegerMass (body ∩ {p | t ≤ F p})).toReal ≤
        (capBound : ℝ) * (volume B).toReal := by
  apply lift_exposed_cap (.inr b) ell hexp x (f 0) (f 0 x) (f_nonzero 0) le_rfl
  apply (measure_mono inter_subset_left).trans
  rw [source_volume, sourceMass]
  have hb : (lightMass (poolIndex (lightCenter b.val)) : ℝ) ≤ (capBound : ℝ) := by
    exact_mod_cast (lightMass_lt_capBound _).le
  exact mul_le_mul_of_nonneg_right (ENNReal.ofReal_le_ofReal hb) zero_le

end SharpOC.Witness1387
