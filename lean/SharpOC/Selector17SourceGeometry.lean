import SharpOC.Selector17Sources

/-! The heavy source is a convex truncation of the union of the two source simplices. -/

noncomputable section
open Set

namespace SharpOC.Selector17

open SelectorSources (E B)

def K (j : Fin 3) : Set E :=
  T j ∩ {x | epsilon * s 2 ≤ (uBasis j).coord 2 x}

theorem K_subset_T (j : Fin 3) : K j ⊆ T j := inter_subset_left

theorem K_subset_B (j : Fin 3) : K j ⊆ B := (K_subset_T j).trans (T_subset_B j)

theorem K_eq_union (j : Fin 3) :
    K j = U j ∪ (P j ∩ {x | (pBasis j).coord 2 x ≤ epsilon}) := by
  rw [K, T_eq_union, Set.union_inter_distrib_right]
  have hu : U j ⊆ {x | epsilon * s 2 ≤ (uBasis j).coord 2 x} := by
    rw [U_eq_hull, (uBasis j).convexHull_eq_nonneg_coord]
    intro x hx
    exact (mul_nonpos_of_nonneg_of_nonpos epsilon_pos.le s_v_neg.le).trans (hx 2)
  rw [inter_eq_left.mpr hu]
  congr 1
  ext x
  change (x ∈ P j ∧ epsilon * s 2 ≤ (uBasis j).coord 2 x) ↔
    x ∈ P j ∧ (pBasis j).coord 2 x ≤ epsilon
  rw [coord_u_eq_coord_p_add]
  simp only [ite_true, zero_add]
  rw [mul_comm (s 2), mul_le_mul_right_of_neg s_v_neg]

theorem K_convex (j : Fin 3) : Convex ℝ (K j) :=
  (T_convex j).inter ((convex_Ici _).affine_preimage ((uBasis j).coord 2))

theorem K_compact (j : Fin 3) : IsCompact (K j) :=
  (T_compact j).inter_right
    (isClosed_le continuous_const ((uBasis j).coord 2).continuous_of_finiteDimensional)

theorem K_nonempty (j : Fin 3) : (K j).Nonempty := by
  rw [K_eq_union]
  refine ⟨uBasis j 0, Or.inl ?_⟩
  rw [U_eq_hull]
  exact subset_convexHull ℝ _ (mem_range_self _)

end SharpOC.Selector17
