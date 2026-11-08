import SharpOC.Selector17SourceGeometry
import SharpOC.SelectorSlabVolume

/-! Exact volumes of the truncated balanced sources and their covering caps. -/

noncomputable section
open Set MeasureTheory
open scoped ENNReal

namespace SharpOC.Selector17

open SelectorSources (E B)

private theorem slab_measurable (j : Fin 3) :
    MeasurableSet (P j ∩ {x | (pBasis j).coord 2 x ≤ epsilon}) :=
  (P_compact j).measurableSet.inter
    (isClosed_le ((pBasis j).coord 2).continuous_of_finiteDimensional continuous_const).measurableSet

private theorem slab_weight_nonneg : 0 ≤ phi * (1 - (1 - epsilon) ^ 5) :=
  mul_nonneg phi_pos.le (sub_nonneg.mpr
    (pow_le_one₀ (sub_nonneg.mpr epsilon_lt_one.le) (by linarith [epsilon_pos])))

theorem V_nonneg : 0 ≤ V := add_nonneg theta_pos.le slab_weight_nonneg

theorem K_volume (j : Fin 3) : volume (K j) = ENNReal.ofReal V * volume B := by
  have hslab := simplex_slab_measure (pBasis j) volume 0 2 (by decide)
    epsilon_pos.le epsilon_lt_one
  simp only [Module.finrank_pi, Fintype.card_fin, ← P_eq_hull j] at hslab
  rw [K_eq_union, measure_union₀ (slab_measurable j).nullMeasurableSet
      ((U_P_aedisjoint j).mono (Subset.refl _) inter_subset_left),
    hslab, U_volume, P_volume, ← mul_assoc, mul_comm (ENNReal.ofReal (1 - (1 - epsilon) ^ 5)),
    ← ENNReal.ofReal_mul phi_pos.le, ← add_mul, ← ENNReal.ofReal_add theta_pos.le slab_weight_nonneg]
  rfl

private theorem P_slab_cap_volume (j : Fin 3) (i : Fin 6) :
    volume ((P j ∩ {x | (pBasis j).coord 2 x ≤ epsilon}) ∩
      {x | t i ≤ (uBasis j).coord i x}) = ENNReal.ofReal
        (if i = 2 then 0 else
          phi * ((1 - t i) ^ 5 - (1 - t i - (1 - s i) * epsilon) ^ 5) / (1 - s i)) * volume B := by
  by_cases hi : i = 2
  · subst i
    have hempty : ((P j ∩ {x | (pBasis j).coord 2 x ≤ epsilon}) ∩
        {x | t 2 ≤ (uBasis j).coord 2 x}) = ∅ := by
      refine eq_empty_iff_forall_notMem.mpr fun x hx => ?_
      have hp : 0 ≤ (pBasis j).coord 2 x := by
        have hp := hx.1.1
        rw [P_eq_hull, (pBasis j).convexHull_eq_nonneg_coord] at hp
        exact hp 2
      have hcut : t 2 ≤ (uBasis j).coord 2 x := hx.2
      simp only [coord_u_eq_coord_p_add, ite_true, zero_add] at hcut
      exact (t_pos 2).not_ge (hcut.trans (mul_nonpos_of_nonpos_of_nonneg s_v_neg.le hp))
    simp [hempty]
  · have hset : ((P j ∩ {x | (pBasis j).coord 2 x ≤ epsilon}) ∩
        {x | t i ≤ (uBasis j).coord i x}) = P j ∩
          {x | (pBasis j).coord 2 x ≤ epsilon ∧
            t i ≤ (pBasis j).coord i x + s i * (pBasis j).coord 2 x} := by
      ext x
      simp [inter_assoc, coord_u_eq_coord_p_add, hi]
    have hcap := simplex_slab_cap_measure (pBasis j) volume i 2 hi
      (s_nonneg i hi) (s_lt_one i) epsilon_pos.le (shifted_t_nonneg i) (shifted_complement_nonneg i)
    simp only [Module.finrank_pi, Fintype.card_fin, ← P_eq_hull j] at hcap
    rw [hset, hcap, P_volume, ← mul_assoc, mul_comm _ (ENNReal.ofReal phi),
      ← ENNReal.ofReal_mul phi_pos.le, mul_div_assoc]
    simp [hi]

private theorem simplex_cap_weight_nonneg (i : Fin 6) : 0 ≤ theta * (1 - t i) ^ 5 :=
  mul_nonneg theta_pos.le (pow_nonneg (sub_nonneg.mpr (t_lt_one i).le) _)

private theorem slab_cap_weight_nonneg (i : Fin 6) : 0 ≤ if i = 2 then 0 else
    phi * ((1 - t i) ^ 5 - (1 - t i - (1 - s i) * epsilon) ^ 5) / (1 - s i) := by
  split_ifs
  · exact le_rfl
  have hs := sub_pos.mpr (s_lt_one i)
  exact div_nonneg (mul_nonneg phi_pos.le (sub_nonneg.mpr (pow_le_pow_left₀
    (shifted_complement_nonneg i) (sub_le_self _ (mul_nonneg hs.le epsilon_pos.le)) _))) hs.le

theorem C_nonneg (i : Fin 6) : 0 ≤ C i :=
  add_nonneg (simplex_cap_weight_nonneg i) (slab_cap_weight_nonneg i)

theorem K_cap_volume (j : Fin 3) (i : Fin 6) :
    volume (K j ∩ {x | t i ≤ (uBasis j).coord i x}) = ENNReal.ofReal (C i) * volume B := by
  have hm : MeasurableSet ((P j ∩ {x | (pBasis j).coord 2 x ≤ epsilon}) ∩
      {x | t i ≤ (uBasis j).coord i x}) := (slab_measurable j).inter
    (isClosed_le continuous_const ((uBasis j).coord i).continuous_of_finiteDimensional).measurableSet
  have hu := simplex_cap_measure (uBasis j) volume i (t_pos i).le (t_lt_one i)
  simp only [Module.finrank_pi, Fintype.card_fin, ← U_eq_hull j] at hu
  rw [K_eq_union, union_inter_distrib_right, measure_union₀ hm.nullMeasurableSet
      ((U_P_aedisjoint j).mono inter_subset_left (inter_subset_left.trans inter_subset_left)),
    hu, P_slab_cap_volume, U_volume, ← mul_assoc, mul_comm _ (ENNReal.ofReal theta),
    ← ENNReal.ofReal_mul theta_pos.le, ← add_mul,
    ← ENNReal.ofReal_add (simplex_cap_weight_nonneg i) (slab_cap_weight_nonneg i)]
  rfl

theorem thresholds_cover (j : Fin 3) (x : E) : ∃ i, t i ≤ (uBasis j).coord i x := by
  by_contra! h
  have hs := Finset.sum_lt_sum_of_nonempty Finset.univ_nonempty (fun i _ => h i)
  rw [(uBasis j).sum_coord_apply_eq_one, sum_t] at hs
  exact (lt_irrefl 1) hs

end SharpOC.Selector17
