import SharpOC.Witness1387.BaselineCount
import SharpOC.Witness1387.CenterCaps
import SharpOC.Witness1387.ExtraBaseCount
import SharpOC.Witness1387.ExtraTailCount
import SharpOC.Witness1387.InactiveExposure
import SharpOC.Witness1387.InactivePair
import SharpOC.Witness1387.InactiveTriple
import SharpOC.Witness1387.MassAssembly
import SharpOC.Witness1387.OrdinaryCount
import SharpOC.Witness1387.Verification

/-! The uniform strict depth bound for the 1387-dimensional rational witness. -/

noncomputable section

namespace SharpOC.Witness1387

open Set MeasureTheory
open scoped BigOperators ENNReal

private theorem extra_pool_55_filter (U : Finset Baseline) :
    (U.filter fun b => (zeroSlots b).card = 2 ∧ (activeAxis b).isSome ∧ 55 ≤ pool b 0) =
      U.filter fun b => (zeroSlots b).card = 2 ∧ (activeAxis b).isSome := by
  ext b
  simp only [Finset.mem_filter]
  constructor
  · rintro ⟨hb, hz, ha, _⟩
    exact ⟨hb, hz, ha⟩
  · rintro ⟨hb, hz, ha⟩
    obtain ⟨i, hi⟩ := Option.isSome_iff_exists.mp ha
    exact ⟨hb, hz, ha, pool_ge_55_of_active hi 0⟩

theorem sourceMass_sum : (∑ s : SupportIndex, sourceMass s) = normalizedTotal := by
  apply sourceMass_sum_of_pool_counts ordinary_pool_count _ unit_sector_count
  intro k hlo hhi
  rcases eq_or_lt_of_le hlo with h | h
  · subst k
    rw [extra_pool_55_filter]
    exact extra_center_count
  · exact extra_tail_pool_count k (by omega) hhi

private theorem inactive_exposed
    (b : Baseline) (h : activeAxis b = none) :
    ∃ ell : (Coordinate → ℝ) →ₗ[ℝ] ℝ,
      ∀ s : SupportIndex, s ≠ .inl b → ell (base s) < ell (base (.inl b)) := by
  by_cases h0 : (zeroSlots b).card = 0
  · apply all_nonzero_baseline_exposed b
    intro i hi
    have hz := Finset.card_eq_zero.mp h0
    have hm := mem_zeroSlots.mpr hi
    simp [hz] at hm
  by_cases h1 : (zeroSlots b).card = 1
  · obtain ⟨i, hi⟩ := Finset.card_eq_one.mp h1
    exact inactive_single_exposed hi h
  by_cases h4 : 4 ≤ (zeroSlots b).card
  · exact inactive_many_exposed b h4
  by_cases h2 : (zeroSlots b).card = 2
  · obtain ⟨i, j, hij, hz⟩ := Finset.card_eq_two.mp h2
    exact inactive_pair_exposed hij hz h
  exact inactive_triple_exposed (b := b) (by omega)

theorem integer_fibers_eq
    (s : SupportIndex) : integerFiber (integerBase s) = source s := by
  change {x | (base s, x) ∈ body} = source s
  cases s with
  | inl b =>
    cases ha : activeAxis b with
    | some i => exact active_fiber_eq ha
    | none =>
      obtain ⟨ell, h⟩ := inactive_exposed b ha
      exact source_eq_at_exposed_base (.inl b) (source_nonempty _) ell h
  | inr b =>
    obtain ⟨ell, h⟩ := selected_light_exposed b
    exact source_eq_at_exposed_base (.inr b) (source_nonempty _) ell h

private theorem sourceMass_nonnegative (s : SupportIndex) : 0 ≤ sourceMass s := by
  rcases s with b | b
  · simp only [sourceMass]
    split_ifs
    · exact pow_nonneg (by linarith [radius_half_lt (poolIndex b)]) _
    · norm_num [tau]
    · exact (lt_trans (by norm_num [tau] : 0 < tau) tau_lt_inactiveMass).le
  · simp only [sourceMass, lightMass]
    apply mul_nonneg (by norm_num [tau])
    exact pow_nonneg (by linarith [radius_half_lt (poolIndex (lightCenter b.val))]) _

private theorem source_volume_sum :
    (∑ s : SupportIndex, (volume (source s)).toReal) =
      (normalizedTotal : ℝ) * (volume B).toReal := by
  have hsum : (∑ s : SupportIndex, (sourceMass s : ℝ)) = (normalizedTotal : ℝ) := by
    exact_mod_cast (show (∑ s : SupportIndex, sourceMass s) = normalizedTotal from sourceMass_sum)
  calc
    _ = ∑ s : SupportIndex, (sourceMass s : ℝ) * (volume B).toReal := by
      apply Finset.sum_congr rfl
      intro s _
      rw [source_volume, ENNReal.toReal_mul,
        ENNReal.toReal_ofReal (by exact_mod_cast sourceMass_nonnegative s)]
    _ = _ := by rw [← Finset.sum_mul, hsum]

private theorem body_census_of_mem (w : Coordinate → ℤ) (x : E)
    (h : ((fun c => (w c : ℝ)), x) ∈ body) : w ∈ range integerBase :=
  (integerFiber_nonempty_iff source_nonempty w).mp ⟨x, h⟩

theorem mixedVolume_toReal :
    mixedVolume.toReal = (normalizedTotal : ℝ) * (volume B).toReal := by
  unfold mixedVolume
  rw [Selector.mixedIntegerMass_body_toReal integerBase integerBase_injective
    body_census_of_mem source integer_fibers_eq
    source_compact, source_volume_sum]

/-- One fixed rational bound for all points, expressed as a real. -/
def uniformBound : ℝ := (36787944 / 10 ^ 8 : ℝ) / (2 : ℝ) ^ 209

theorem uniformBound_lt_target : uniformBound < 1 / (Real.exp 1 * (2 : ℝ) ^ 209) := by
  have he : (36787944 / 10 ^ 8 : ℝ) < 1 / (eUpper : ℝ) := by
    simpa only [Rat.cast_div, Rat.cast_pow, Rat.cast_ofNat, Rat.cast_one] using
      (Rat.cast_lt (K := ℝ)).2 numerical_bound_lt_inv_eUpper
  have hm : 1 / (eUpper : ℝ) ≤ 1 / Real.exp 1 :=
    one_div_le_one_div_of_le (Real.exp_pos 1) exp_one_le_eUpper
  unfold uniformBound
  rw [← div_div]
  exact div_lt_div_of_pos_right (he.trans_le hm) (by positivity)

/-- One strict depth bound applies at every mixed-integer point. -/
theorem strict_depth
    (w : Coordinate → ℤ) (x : E) :
    ∃ F : Ambient →L[ℝ] ℝ, ∃ t : ℝ, F ≠ 0 ∧ t ≤ F ((fun c => (w c : ℝ)), x) ∧
      (Selector.mixedIntegerMass (body ∩ {p | t ≤ F p})).toReal /
        mixedVolume.toReal < uniformBound := by
  have hfiber := integer_fibers_eq
  have hBpos : 0 < (volume B).toReal := ENNReal.toReal_pos B_volume_pos.ne' B_volume_ne_top
  have hNpos : 0 < (normalizedTotal : ℝ) := by exact_mod_cast normalizedTotal_pos
  have hH : 0 ≤ (capBound : ℝ) * (volume B).toReal :=
    mul_nonneg (by exact_mod_cast capBound_pos.le) hBpos.le
  have hnum : (capBound : ℝ) * (2 : ℝ) ^ 209 <
      (36787944 / 10 ^ 8 : ℝ) * (normalizedTotal : ℝ) := by
    simpa only [Rat.cast_mul, Rat.cast_div, Rat.cast_pow, Rat.cast_ofNat] using
      (Rat.cast_lt (K := ℝ)).2 numerical_depth_bound
  have hlt : (capBound : ℝ) < uniformBound * (normalizedTotal : ℝ) := by
    rw [uniformBound, div_mul_eq_mul_div]
    exact (lt_div_iff₀ (by positivity)).2 hnum
  have hthreshold : (capBound : ℝ) * (volume B).toReal <
      uniformBound * ∑ i : SupportIndex, (volume (source i)).toReal := by
    rw [source_volume_sum, ← mul_assoc]
    exact mul_lt_mul_of_pos_right hlt hBpos
  have hn : body.Nonempty := by
    let s : SupportIndex := .inl (fun _ => 0)
    obtain ⟨y, hy⟩ := source_nonempty s
    exact ⟨(base s, y), prescribed_source_mem s hy⟩
  apply strict_depth_from_exact_fibers body_compact body_convex hn integerBase_injective
    body_census_of_mem hfiber source_compact hH _ hthreshold _ w x
  · rw [source_volume_sum]
    exact mul_pos hNpos hBpos
  · intro s y _
    have lift (hc : ∃ F : Ambient →L[ℝ] ℝ, ∃ t : ℝ,
        F ≠ 0 ∧ t ≤ F (base s, y) ∧
          (Selector.mixedIntegerMass (body ∩ {p | t ≤ F p})).toReal ≤
            (capBound : ℝ) * (volume B).toReal) :
        ∃ F : Ambient →L[ℝ] ℝ, ∃ t : ℝ, F ≠ 0 ∧ t ≤ F (base s, y) ∧
          (∑ a : SupportIndex, (volume (source a ∩ {v | t ≤ F (base a, v)})).toReal) ≤
            (capBound : ℝ) * (volume B).toReal := by
      obtain ⟨F, t, hF, ht, hm⟩ := hc
      refine ⟨F, t, hF, ht, ?_⟩
      rw [Selector.mixedIntegerMass_closedCut_toReal integerBase integerBase_injective
        body_census_of_mem source hfiber source_compact F t] at hm
      exact hm
    cases s with
    | inl b =>
      cases ha : activeAxis b with
      | some i => exact active_center_cap ha y
      | none =>
        obtain ⟨ell, hell⟩ := inactive_exposed b ha
        by_cases hz : (zeroSlots b).card ≤ 1
        · exact lift (exposed_unitSector_cap b (by simp [ha]) hz ell hell y)
        · exact lift (exposed_inactiveSimplex_cap b (by simp [ha]) hz ell hell y)
    | inr b =>
      obtain ⟨ell, hell⟩ := selected_light_exposed b
      exact lift (exposed_light_cap b ell hell y)

/-- A proper closed cap below the target exists at every mixed-integer point. -/
theorem one_over_e_depth (w : Coordinate → ℤ) (x : E) :
    ∃ F : Ambient →L[ℝ] ℝ, ∃ t : ℝ, F ≠ 0 ∧ t ≤ F ((fun c => (w c : ℝ)), x) ∧
      (Selector.mixedIntegerMass (body ∩ {p | t ≤ F p})).toReal /
        mixedVolume.toReal < 1 / (Real.exp 1 * (2 : ℝ) ^ 209) := by
  obtain ⟨F, t, hF, ht, hlt⟩ := strict_depth w x
  exact ⟨F, t, hF, ht, hlt.trans uniformBound_lt_target⟩

end SharpOC.Witness1387
