import SharpOC.Selector17Bases

/-! The integer projection of the signed selector construction. -/

noncomputable section
open Finset Set
open scoped BigOperators

namespace SharpOC.Selector17

private theorem weighted_bound {ι : Type*} [Fintype ι]
    (w v : ι → ℝ) (c : ℝ) (hw : ∀ i, 0 ≤ w i) (hs : ∑ i, w i = 1)
    (h : ∀ i, 0 < w i → v i ≤ c) : ∑ i, w i * v i ≤ c := by
  calc
    ∑ i, w i * v i ≤ ∑ i, w i * c := by
      apply Finset.sum_le_sum
      intro i _
      rcases (hw i).eq_or_lt with hz | hp
      · simp [← hz]
      · exact mul_le_mul_of_nonneg_left (h i hp) (hw i)
    _ = c := by rw [← Finset.sum_mul, hs, one_mul]

private theorem active_eq_of_weighted_bound {ι : Type*} [Fintype ι]
    (w v : ι → ℝ) (c : ℝ) (hw : ∀ i, 0 ≤ w i) (hs : ∑ i, w i = 1)
    (h : ∀ i, 0 < w i → v i ≤ c) (ha : ∑ i, w i * v i = c)
    (i : ι) (hi : 0 < w i) : v i = c := by
  have hz : ∑ j, w j * (c - v j) = 0 := by
    simp_rw [mul_sub]
    rw [Finset.sum_sub_distrib, ← Finset.sum_mul, hs, one_mul, ha, sub_self]
  have hnn (j : ι) (_ : j ∈ Finset.univ) : 0 ≤ w j * (c - v j) := by
    rcases (hw j).eq_or_lt with he | hp
    · simp [← he]
    · exact mul_nonneg (hw j) (sub_nonneg.mpr (h j hp))
  have hi0 := (Finset.sum_eq_zero_iff_of_nonneg hnn).mp hz i (Finset.mem_univ i)
  rcases mul_eq_zero.mp hi0 with he | he
  · exact (hi.ne' he).elim
  · linarith

private theorem active_binary_average {ι : Type*} [Fintype ι]
    (w v : ι → ℝ) (s : ℝ) (z : ℤ) (hw : ∀ i, 0 ≤ w i)
    (hs : ∑ i, w i = 1) (ha : ∑ i, w i * v i = (z : ℝ))
    (hsign : s = 1 ∨ s = -1)
    (h : ∀ i, 0 < w i → v i = 0 ∨ v i = s)
    (i : ι) (hi : 0 < w i) : v i = (z : ℝ) := by
  rcases hsign with rfl | rfl
  · have hup : ∀ j, 0 < w j → v j ≤ 1 := fun j hj => by rcases h j hj with h | h <;> simp [h]
    have hlo : ∀ j, 0 < w j → -v j ≤ 0 := fun j hj => by rcases h j hj with h | h <;> simp [h]
    have h1 := weighted_bound w v 1 hw hs hup
    have h0 := weighted_bound w (fun j => -v j) 0 hw hs hlo
    simp only [mul_neg, Finset.sum_neg_distrib, ha] at h0
    rw [ha] at h1
    have hz0 : 0 ≤ z := by exact_mod_cast (show (0 : ℝ) ≤ z by linarith)
    have hz1 : z ≤ 1 := by exact_mod_cast h1
    have hz : z = 0 ∨ z = 1 := by omega
    rcases hz with rfl | rfl
    · have ha0 : ∑ j, w j * (-v j) = 0 := by simp [mul_neg, ha]
      have he := active_eq_of_weighted_bound w (fun j => -v j) 0 hw hs hlo ha0 i hi
      norm_num
      linarith
    · simpa using active_eq_of_weighted_bound w v 1 hw hs hup (by simpa using ha) i hi
  · have hup : ∀ j, 0 < w j → v j ≤ 0 := fun j hj => by rcases h j hj with h | h <;> simp [h]
    have hlo : ∀ j, 0 < w j → -v j ≤ 1 := fun j hj => by rcases h j hj with h | h <;> simp [h]
    have h0 := weighted_bound w v 0 hw hs hup
    have h1 := weighted_bound w (fun j => -v j) 1 hw hs hlo
    simp only [mul_neg, Finset.sum_neg_distrib, ha] at h1
    rw [ha] at h0
    have hz0 : z ≤ 0 := by exact_mod_cast h0
    have hz1 : -1 ≤ z := by exact_mod_cast (show (-1 : ℝ) ≤ z by linarith)
    have hz : z = 0 ∨ z = -1 := by omega
    rcases hz with rfl | rfl
    · simpa using active_eq_of_weighted_bound w v 0 hw hs hup (by simpa using ha) i hi
    · have ha1 : ∑ j, w j * (-v j) = 1 := by simp [mul_neg, ha]
      have he := active_eq_of_weighted_bound w (fun j => -v j) 1 hw hs hlo ha1 i hi
      norm_num
      linarith

/-- Every integer projection base is a generator base. -/
theorem integer_projection_census (z : Coordinate → ℤ)
    (hx : (fun j => (z j : ℝ)) ∈ convexHull ℝ (Set.range base)) :
    z ∈ Set.range integerBase := by
  classical
  by_cases hz : z = 0
  · subst z
    refine ⟨none, ?_⟩
    funext j
    change integerBase none j = 0
    have hzero : (integerBase none j : ℝ) = 0 :=
      (congrFun (integerBase_cast none) j).trans (congrFun base_none j)
    exact_mod_cast hzero
  obtain ⟨ι, _, w, p, hw, hs, hp, havg⟩ := mem_convexHull_iff_exists_fintype.mp hx
  choose a ha using hp
  have avg (ℓ : IntegerSpace →ₗ[ℝ] ℝ) :
      ∑ b, w b * ℓ (base (a b)) = ℓ (fun j => (z j : ℝ)) := by
    simpa only [map_sum, map_smul, smul_eq_mul, ha] using congrArg ℓ havg
  have avg_coord (j : Coordinate) :
      ∑ b, w b * base (a b) j = (z j : ℝ) := avg (LinearMap.proj j)
  have avg_neg (j : Coordinate) :
      ∑ b, w b * (-base (a b) j) = -(z j : ℝ) := avg (-LinearMap.proj j)
  have hcoord (j : Coordinate) : (-1 : ℤ) ≤ z j ∧ z j ≤ 1 := by
    have hup := weighted_bound w (fun b => base (a b) j) 1 hw hs
      (fun b _ => (base_coord_bounds (a b) j).2)
    have hlo := weighted_bound w (fun b => -base (a b) j) 1 hw hs
      (fun b _ => by linarith [(base_coord_bounds (a b) j).1])
    rw [avg_coord] at hup
    rw [avg_neg] at hlo
    exact ⟨by exact_mod_cast (show (-1 : ℝ) ≤ z j by linarith), by exact_mod_cast hup⟩
  have extreme (j : Coordinate) (hj : z j ≠ 0) (b : ι) (hb : 0 < w b) :
      base (a b) j = (z j : ℝ) := by
    have h := hcoord j
    have hpm : z j = 1 ∨ z j = -1 := by omega
    rcases hpm with hplus | hminus
    · rw [hplus]
      simpa using active_eq_of_weighted_bound w (fun b => base (a b) j) 1 hw hs
        (fun b _ => (base_coord_bounds (a b) j).2) (by simpa [hplus] using avg_coord j) b hb
    · rw [hminus]
      have he := active_eq_of_weighted_bound w (fun b => -base (a b) j) 1 hw hs
        (fun b _ => by linarith [(base_coord_bounds (a b) j).1])
        (by simpa [hminus] using avg_neg j) b hb
      norm_num
      linarith
  obtain ⟨b₀, hb₀⟩ : ∃ b : ι, 0 < w b := by
    by_contra! h
    have hw0 (b : ι) : w b = 0 := le_antisymm (h b) (hw b)
    simp [hw0] at hs
  refine ⟨a b₀, ?_⟩
  have selectorNonzero : (∃ q : Fin 2, z (.inr q) ≠ 0) ∨ ∀ q : Fin 2, z (.inr q) = 0 := by
    by_cases h : ∃ q : Fin 2, z (.inr q) ≠ 0
    · exact Or.inl h
    · exact Or.inr fun q => not_ne_iff.mp fun hq => h ⟨q, hq⟩
  have he : base (a b₀) = (fun j => (z j : ℝ)) := by
    rcases selectorNonzero with ⟨q, hq⟩ | hsel
    · let s : ℝ := z (.inr q)
      have hsign : s = 1 ∨ s = -1 := by
        have h := hcoord (.inr q)
        have hpm : z (.inr q) = 1 ∨ z (.inr q) = -1 := by omega
        rcases hpm with h | h <;> simp [s, h]
      have hn (b : ι) (hb : 0 < w b) :
          (mask (a b)).toRight ≠ ∅ ∧ orientation (a b) = s := by
        have he := extreme (.inr q) hq b hb
        rw [selector_base] at he
        by_cases hmem : q ∈ (mask (a b)).toRight
        · exact ⟨Finset.Nonempty.ne_empty ⟨q, hmem⟩, by simpa [hmem, s] using he⟩
        · exact (hq (by exact_mod_cast (show (z (.inr q) : ℝ) = 0 by simpa [hmem] using he.symm))).elim
      funext j
      cases j with
      | inr k =>
        apply active_binary_average w (fun b => base (a b) (.inr k)) s _ hw hs
          (avg_coord (.inr k)) hsign _ b₀ hb₀
        intro b hb
        rw [selector_base, (hn b hb).2]
        split_ifs <;> simp
      | inl k =>
        have hpm : s * ordinarySign k = 1 ∨ s * ordinarySign k = -1 := by
          rcases hsign with h | h <;> rcases ordinarySign_cases k with hg | hg <;> simp [h, hg]
        apply active_binary_average w (fun b => base (a b) (.inl k)) (s * ordinarySign k) _ hw hs
          (avg_coord (.inl k)) hpm _ b₀ hb₀
        intro b hb
        rw [ordinary_base, ite_eq_right (hn b hb).1, (hn b hb).2]
        split_ifs <;> simp
    · obtain ⟨k, hk⟩ : ∃ k : Fin 10, z (.inl k) ≠ 0 := by
        by_contra! h
        apply hz
        funext j
        cases j with
        | inl k => exact h k
        | inr k => exact hsel k
      let s : ℝ := z (.inl k)
      let c : ℝ := s * ordinarySign k
      have hcoeff (b : ι) (hb : 0 < w b) (hselb : (mask (a b)).toRight ≠ ∅) :
          c = orientation (a b) := by
        have he := extreme (.inl k) hk b hb
        rw [ordinary_base, ite_eq_right hselb] at he
        by_cases hm : k ∈ (mask (a b)).toLeft
        · have he' : orientation (a b) * ordinarySign k = s := by simpa [s, hm] using he
          rcases ordinarySign_cases k with hp | hp <;> simp [hp, ← he', c]
        · exact (hk (by exact_mod_cast (show (z (.inl k) : ℝ) = 0 by simpa [hm] using he.symm))).elim
      let ℓ : IntegerSpace →ₗ[ℝ] ℝ := (-c) • selectorSum
      have havg₀ : ∑ b, w b * ℓ (base (a b)) = 0 := by
        simpa [ℓ, selectorSum, hsel] using avg ℓ
      have hup (b : ι) (hb : 0 < w b) : ℓ (base (a b)) ≤ 0 := by
        by_cases hselb : (mask (a b)).toRight = ∅
        · simp [ℓ, selectorSum_base, hselb]
        · have he := hcoeff b hb hselb
          rcases orientation_cases (a b) with ho | ho <;>
            simp [ℓ, selectorSum_base, he, ho]
      have hzero (b : ι) (hb : 0 < w b) : (mask (a b)).toRight = ∅ := by
        by_contra hn
        have hv := active_eq_of_weighted_bound w (fun b => ℓ (base (a b))) 0 hw hs hup havg₀ b hb
        have hc := hcoeff b hb hn
        have hcard := Finset.card_pos.mpr (Finset.nonempty_iff_ne_empty.mpr hn)
        have hpositive : (0 : ℝ) < ((mask (a b)).toRight.card : ℝ) := by exact_mod_cast hcard
        have hneg : ℓ (base (a b)) < 0 := by
          rcases orientation_cases (a b) with ho | ho <;>
            simpa [ℓ, selectorSum_base, hc, ho] using neg_lt_zero.mpr hpositive
        exact hneg.ne hv
      funext j
      apply active_binary_average w (fun b => base (a b) j) 1 _ hw hs
        (avg_coord j) (Or.inl rfl) _ b₀ hb₀
      intro b hb
      rw [zero_selector_base (hzero b hb)]
      by_cases hm : j ∈ mask (a b) <;> simp [cubeVector, hm]
  funext j
  exact_mod_cast (congrFun (integerBase_cast (a b₀)) j).trans (congrFun he j)

end SharpOC.Selector17
