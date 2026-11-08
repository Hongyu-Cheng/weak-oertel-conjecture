import SharpOC.Witness1387.CenterGeometry
import SharpOC.Witness1387.ExposedCaps
import SharpOC.Witness1387.SupportExposure

/-! Active-center caps from the maximizing slice and its row counts. -/

noncomputable section

namespace SharpOC.Witness1387

open Set MeasureTheory
open scoped BigOperators ENNReal

private theorem unit_row_volume_zero (j l : Fin 4) (a : ℝ) (ha : 0 ≤ a)
    (howner : j = l → 1 ≤ a) :
    volume (T l ∩ {x | 3 * a ≤ f j x}) = 0 := by
  apply measure_mono_null _ (f_kernel_volume_zero j)
  rintro x ⟨hx, hc⟩
  change 3 * a ≤ f j x at hc
  by_cases hj : j = l
  · exfalso
    linarith [howner hj, (B_f_bounds (T_subset_B l hx) j).2]
  · change f j x = 0
    linarith [T_f_missed l j hj hx]

private theorem light_other_row_volume_zero {s : ℝ} (hs : 0 ≤ s)
    (j l : Fin 4) (hj : j ≠ l) :
    volume (dilate s (T l) ∩ {x | 0 ≤ f j x}) = 0 := by
  apply measure_mono_null _ (f_kernel_volume_zero j)
  rintro x ⟨⟨y, hy, rfl⟩, hc⟩
  change 0 ≤ f j (s • y) at hc
  change f j (s • y) = 0
  rw [map_smul, smul_eq_mul] at hc ⊢
  exact le_antisymm (mul_nonpos_of_nonneg_of_nonpos hs (T_f_missed l j hj hy)) hc

private theorem light_owner_row_trace {s : ℝ} (hs : 0 ≤ s) (hs1 : s ≤ 1) (j : Fin 4) :
    dilate s (T j) ∩ {x | 3 * (-1 : ℝ) ≤ f j x} = dilate s (T j) := by
  refine Subset.antisymm inter_subset_left ?_
  rintro x ⟨y, hy, rfl⟩
  refine ⟨⟨y, hy, rfl⟩, ?_⟩
  change 3 * (-1 : ℝ) ≤ f j (s • y)
  rw [map_smul, smul_eq_mul]
  nlinarith [mul_le_mul_of_nonneg_left (B_f_bounds (T_subset_B j hy) j).1 hs]

open Classical in
/-- Each supporting slice supplies four containing cuts. Only the chosen
row's lights contribute outside the center. The fiber family can be the
prescribed sources or the actual fibers when those agree on the slice. -/
theorem active_center_cap_of_slice [Fintype SupportIndex]
    (K : SupportIndex → Set E) (hK : ∀ a, IsCompact (K a))
    (b : Baseline) (ell : (Coordinate → ℝ) →L[ℝ] ℝ)
    (row : Fin 4 → (Coordinate → ℝ) →L[ℝ] ℝ) (labelRow : Equiv.Perm (Fin 4))
    (hface : ∀ a, ell (base a) ≤ ell (base (.inl b)))
    (hcenter : K (.inl b) = dilate (radius (poolIndex b) : ℝ) B)
    (hzero : ∀ j, row j (base (.inl b)) = 0)
    (hroles : ∀ a, ell (base a) = ell (base (.inl b)) → a ≠ .inl b →
      (∃ l, K a = T (labelRow l) ∧ ∀ j, 0 ≤ row j (base a) ∧
          (j = l → 1 ≤ row j (base a))) ∨
        (∃ l, K a = dilate (2 * (radius (poolIndex b) : ℝ) - 1) (T (labelRow l)) ∧
          ∀ j, row j (base a) = if j = l then -1 else 0))
    (hcount : ∀ j, (Finset.univ.filter (fun a : SupportIndex =>
      ell (base a) = ell (base (.inl b)) ∧ row j (base a) = -1)).card ≤
        poolSize (poolIndex b))
    (x : E) :
    ∃ F : Ambient →L[ℝ] ℝ, ∃ t : ℝ, F ≠ 0 ∧ t ≤ F (base (.inl b), x) ∧
      (∑ a, (volume (K a ∩ {y | t ≤ F (base a, y)})).toReal) ≤
        (capBound : ℝ) * (volume B).toReal := by
  classical
  let k := poolIndex b
  let r : ℝ := radius k
  have hs : 0 ≤ 2 * r - 1 := by
    dsimp only [r]
    exact_mod_cast (by linarith [radius_half_lt k] : (0 : ℚ) ≤ 2 * radius k - 1)
  have hr : 0 < r := by linarith
  have hr1 : r < 1 := by
    dsimp only [r]
    exact_mod_cast radius_lt_one k
  have hs1 : 2 * r - 1 ≤ 1 := by linarith
  obtain ⟨l, hx⟩ := cuts_cover x
  let j := labelRow.symm l
  have hj : labelRow j = l := labelRow.apply_symm_apply l
  let h : Ambient →L[ℝ] ℝ :=
    (f (labelRow j)).comp (ContinuousLinearMap.snd ℝ (Coordinate → ℝ) E) -
      (3 : ℝ) • (row j).comp (ContinuousLinearMap.fst ℝ (Coordinate → ℝ) E)
  have hcont : ∃ y, h (0, y) ≠ 0 := by
    by_contra! hz
    apply f_nonzero (labelRow j)
    ext y
    simpa [h, smul_eq_mul] using hz y
  obtain ⟨F, t, hF, hcut, hout⟩ :=
    supporting_slice_cut base K hK (.inl b) ell hface h hcont 0
  have hscore (a : SupportIndex) (y : E) : (0 : ℝ) ≤ h (base a, y) ↔
      3 * row j (base a) ≤ f (labelRow j) y := by
    simp [h, smul_eq_mul, sub_nonneg]
  have htrace (a : SupportIndex) (ha : ell (base a) = ell (base (.inl b))) :
      K a ∩ {y | t ≤ F (base a, y)} = K a ∩ {y | 3 * row j (base a) ≤ f (labelRow j) y} := by
    ext y
    exact and_congr_right (fun _ => (hcut a ha y).symm.trans (hscore a y))
  refine ⟨F, t, hF, (hcut (.inl b) rfl x).mp ((hscore _ x).mpr ?_), ?_⟩
  · simpa only [hzero j, mul_zero, hj] using hx
  let lights := Finset.univ.filter (fun a : SupportIndex =>
    ell (base a) = ell (base (.inl b)) ∧ row j (base a) = -1)
  let C := ((beta : ℝ) * r ^ 1178) * (volume B).toReal
  let L := (lightMass k : ℝ) * (volume B).toReal
  have hlight : (lightMass k : ℝ) = (3 / 32 : ℝ) * (2 * r - 1) ^ 1178 := by
    norm_num only [lightMass, tau, r, Rat.cast_mul, Rat.cast_pow, Rat.cast_div,
      Rat.cast_ofNat, Rat.cast_sub]
  have hL : 0 ≤ L := by
    dsimp [L]
    rw [hlight]
    exact mul_nonneg (mul_nonneg (by norm_num) (pow_nonneg hs _)) ENNReal.toReal_nonneg
  have hterm (a : SupportIndex) :
      (volume (K a ∩ {y | t ≤ F (base a, y)})).toReal =
        (if a = .inl b then C else 0) + (if a ∈ lights then L else 0) := by
    by_cases ha : a = .inl b
    · subst a
      rw [htrace _ rfl, hcenter, hzero, mul_zero, dilated_center_row_volume hr]
      simp [lights, hzero, C, beta, ENNReal.toReal_mul,
        ENNReal.toReal_ofReal (by positivity : 0 ≤ (27 / 64 : ℝ) * r ^ 1178)]
    · by_cases he : ell (base a) = ell (base (.inl b))
      · rw [htrace a he, ite_eq_right ha, zero_add]
        rcases hroles a he ha with ⟨l', hsrc, hrow⟩ | ⟨l', hsrc, hrow⟩
        · have hmiss : row j (base a) ≠ -1 := by linarith [(hrow j).1]
          rw [hsrc, unit_row_volume_zero _ _ _ (hrow j).1
            (fun h => (hrow j).2 (labelRow.injective h))]
          simp [lights, hmiss]
        · rw [hsrc, hrow j]
          by_cases hown : j = l'
          · subst l'
            rw [ite_eq_left rfl, light_owner_row_trace hs hs1, dilate_volume hs, T_volume]
            simp only [lights, Finset.mem_filter, Finset.mem_univ, he, hrow j,
              and_self, ite_true, ENNReal.toReal_mul,
              ENNReal.toReal_ofReal (pow_nonneg hs _),
              ENNReal.toReal_ofReal (by norm_num : 0 ≤ (3 / 32 : ℝ)), L, hlight]
            ac_rfl
          · have hne : labelRow j ≠ labelRow l' := fun h => hown (labelRow.injective h)
            rw [ite_eq_right hown, mul_zero, light_other_row_volume_zero hs _ _ hne]
            simp [lights, hrow j, hown]
      · have hempty : K a ∩ {y | t ≤ F (base a, y)} = ∅ :=
          eq_empty_iff_forall_notMem.mpr fun y hy => (hout a he y hy.1).not_ge hy.2
        simp [hempty, lights, ha, he]
  have hsum :
      (∑ a, (volume (K a ∩ {y | t ≤ F (base a, y)})).toReal) =
        C + (lights.card : ℝ) * L := by
    simp_rw [hterm]
    rw [Finset.sum_add_distrib]
    congr 1
    · simp
    · rw [← Finset.sum_filter]
      simp [nsmul_eq_mul]
  have hc : (lights.card : ℝ) ≤ (poolSize k : ℝ) := by
    exact Nat.cast_le.mpr (show lights.card ≤ poolSize k from hcount j)
  have hbudget : (beta : ℝ) * r ^ 1178 + (poolSize k : ℝ) * (lightMass k : ℝ) <
      (capBound : ℝ) := by
    dsimp only [r]
    exact_mod_cast activeCap_lt_capBound k
  rw [hsum]
  calc
    _ ≤ C + (poolSize k : ℝ) * L := add_le_add (le_refl C) (mul_le_mul_of_nonneg_right hc hL)
    _ = ((beta : ℝ) * r ^ 1178 + (poolSize k : ℝ) * (lightMass k : ℝ)) *
        (volume B).toReal := by simp only [C, L, add_mul, mul_assoc]
    _ ≤ _ := mul_le_mul_of_nonneg_right hbudget.le ENNReal.toReal_nonneg

/-- Extend the local integer row to a linear form on the full base space. -/
def activeRow (i : Block) (j : Fin 4) : (Coordinate → ℝ) →L[ℝ] ℝ :=
  let u : (Coordinate → ℝ) →ₗ[ℝ] ℝ := ∑ k : Fin 8, LinearMap.proj (i, ordIdx k)
  (Fin.lastCases (motive := fun _ => (Coordinate → ℝ) →ₗ[ℝ] ℝ) u
    (fun k => u - LinearMap.proj (i, selIdx k)) j).toContinuousLinearMap

@[simp] theorem activeRow_base (i : Block) (j : Fin 4) (a : SupportIndex) :
    activeRow i j (base a) = (localRow (integerBlock a i) j : ℝ) := by
  rcases Fin.eq_castSucc_or_eq_last j with ⟨j, rfl⟩ | rfl
  · simp only [activeRow, localRow, LinearMap.coe_toContinuousLinearMap', Fin.lastCases_castSucc,
      LinearMap.sub_apply, LinearMap.sum_apply, LinearMap.proj_apply]
    change (∑ k : Fin 8, (integerBlock a i (ordIdx k) : ℝ)) -
      (integerBlock a i (selIdx j) : ℝ) =
      (((∑ k : Fin 8, integerBlock a i (ordIdx k)) - integerBlock a i (selIdx j) : ℤ) : ℝ)
    push_cast
    rfl
  · simp only [activeRow, LinearMap.coe_toContinuousLinearMap', Fin.lastCases_last,
      LinearMap.sum_apply, LinearMap.proj_apply]
    change (∑ k : Fin 8, (integerBlock a i (ordIdx k) : ℝ)) =
      ((∑ k : Fin 8, integerBlock a i (ordIdx k) : ℤ) : ℝ)
    push_cast
    rfl

private theorem owner_row_pos {s : Slot} (hs : s ≠ 0) :
    1 ≤ localRow (localBase s) (owner s) := by
  have hg := localGuard_base_pos s hs
  rw [localGuard_eq_sum_row, Fin.sum_univ_four] at hg
  unfold owner
  split_ifs <;> omega

private theorem label_fixed_blocks {b c : Baseline} {i : Block} (hi : b i = 0)
    (hc : ∀ k, k ≠ i → c k = b k) : label c = label b + owner (c i) := by
  have hsum (u : Baseline) : (∑ k : Block, (owner (u k)).val) =
      (∑ k ∈ (Finset.univ : Finset Block).erase i, (owner (u k)).val) + (owner (u i)).val :=
    (Finset.sum_erase_add _ _ (Finset.mem_univ i)).symm
  have hfix : (∑ k ∈ (Finset.univ : Finset Block).erase i, (owner (c k)).val) =
      ∑ k ∈ (Finset.univ : Finset Block).erase i, (owner (b k)).val := by
    apply Finset.sum_congr rfl
    intro k hk
    rw [hc k (Finset.mem_erase.mp hk).1]
  apply Fin.ext
  rw [Fin.val_add]
  change (∑ k : Block, (owner (c k)).val) % 4 =
    ((∑ k : Block, (owner (b k)).val) % 4 + (owner (c i)).val) % 4
  rw [hsum c, hfix, hsum b, hi, show owner 0 = 0 by decide]
  simp [Nat.mod_add_mod]

/-- The actual selector face supplies all four local cuts. -/
theorem active_center_cap [Fintype SupportIndex] {b : Baseline} {i : Block}
    (ha : activeAxis b = some i) (x : E) :
    ∃ F : Ambient →L[ℝ] ℝ, ∃ t : ℝ, F ≠ 0 ∧ t ≤ F (base (.inl b), x) ∧
      (∑ a, (volume (source a ∩ {y | t ≤ F (base a, y)})).toReal) ≤
        (capBound : ℝ) * (volume B).toReal := by
  classical
  obtain ⟨ell, hell⟩ := exposed_active_face ha
  have hi : b i = 0 := by
    apply mem_zeroSlots.mp
    rcases activeAxis_zeroSlots_cases ha with h | ⟨j, _, h⟩ <;> simp [h]
  have hface (a : SupportIndex) (he : ell (base a) = ell (base (.inl b))) :
      ∀ k, k ≠ i → integerBlock a k = localBase (b k) := (hell a).2.mp he
  have hbaseline (c : Baseline) (he : ell (base (.inl c)) = ell (base (.inl b))) :
      ∀ k, k ≠ i → c k = b k := by
    intro k hk
    apply localBase_injective
    simpa [integerBlock] using hface (.inl c) he k hk
  have hlight (c : {c : Baseline // (selectedFlip c).isSome})
      (he : ell (base (.inr c)) = ell (base (.inl b))) :
      selectedFlip c.val = some i ∧ lightCenter c.val = b ∧ ∀ k, k ≠ i → c.val k = b k := by
    obtain ⟨hf, hc⟩ := active_face_light ha c (hface (.inr c) he)
    refine ⟨hf, hc, fun k hk => ?_⟩
    rw [← hc, lightCenter_of_selectedFlip hf, Function.update_of_ne hk]
  have hrow_light (c : {c : Baseline // (selectedFlip c).isSome})
      (hf : selectedFlip c.val = some i) (j : Fin 4) :
      activeRow i j (base (.inr c)) = if j = owner (c.val i) then -1 else 0 := by
    rw [activeRow_base, integerBlock, ite_eq_left (show flip (.inr c) = some i from hf),
      localRow_neg]
    change ((-(localRow (localBase (c.val i)) j) : ℤ) : ℝ) = _
    rw [eligible_row _ (selectedFlip_eligible hf)]
    split_ifs <;> norm_num
  refine active_center_cap_of_slice source source_compact b ell.toContinuousLinearMap
    (activeRow i) (Equiv.addLeft (label b)) (fun a => (hell a).1)
    (source_eq_center b (by simp [ha])) ?_ ?_ ?_ x
  · intro j
    rw [activeRow_base]
    have hn := localRow_neg (0 : Fin 11 → ℤ) j
    simp only [neg_zero] at hn
    have hz : localRow 0 j = 0 := by omega
    simp [integerBlock, hi, hz]
  · intro a he hne
    change ell (base a) = ell (base (.inl b)) at he
    rcases a with c | c
    · have hc : c ≠ b := fun h => hne (congrArg Sum.inl h)
      have hout := hbaseline c he
      obtain ⟨hn, hz⟩ := active_face_baseline_unit ha hout hc
      have hci : c i ≠ 0 := by
        intro hc0
        apply hc
        funext k
        by_cases hk : k = i
        · simpa [hk, hi] using hc0
        · exact hout k hk
      left
      refine ⟨owner (c i), ?_, fun j => ⟨?_, ?_⟩⟩
      · rw [source_eq_unitSector c (by simp [hn]) hz, label_fixed_blocks hi hout]
        rfl
      · rw [activeRow_base]
        exact_mod_cast localRow_base_nonneg (c i) j
      · rintro rfl
        rw [activeRow_base]
        exact_mod_cast owner_row_pos hci
    · obtain ⟨hf, hc, hout⟩ := hlight c he
      right
      refine ⟨owner (c.val i), ?_, hrow_light c hf⟩
      rw [source_eq_light, hc, label_fixed_blocks hi hout]
      rfl
  · intro j
    let L := Finset.univ.filter fun a : SupportIndex =>
      ell (base a) = ell (base (.inl b)) ∧ activeRow i j (base a) = -1
    change L.card ≤ _
    have hmem (a : SupportIndex) (hm : a ∈ L) :
        ∃ c : {c : Baseline // (selectedFlip c).isSome}, a = .inr c ∧
          (∀ k, k ≠ i → c.val k = b k) ∧ c.val i ∈ poolSites b i j := by
      obtain ⟨he, hneg⟩ := (Finset.mem_filter.mp hm).2
      rcases a with c | c
      · rw [activeRow_base] at hneg
        have hp : 0 ≤ (localRow (integerBlock (.inl c) i) j : ℝ) := by
          exact_mod_cast localRow_base_nonneg (c i) j
        linarith
      · obtain ⟨hf, _, hout⟩ := hlight c he
        have hu : Function.update b i (c.val i) = c.val := by
          funext k
          by_cases hk : k = i
          · subst k; simp
          · rw [Function.update_of_ne hk, hout k hk]
        have ho : j = owner (c.val i) := by
          rw [hrow_light c hf j] at hneg
          by_contra hn
          norm_num [hn] at hneg
        exact ⟨c, rfl, hout, mem_poolSites.mpr ⟨ho.symm, by rwa [hu]⟩⟩
    have hmaps : Set.MapsTo (fun a : SupportIndex => parent a i) (L : Set SupportIndex)
        (poolSites b i j : Set Slot) := by
      intro a hm
      obtain ⟨c, rfl, _, hc⟩ := hmem a hm
      exact hc
    have hinj : (L : Set SupportIndex).InjOn (fun a => parent a i) := by
      intro a hm a' hm' he
      obtain ⟨c, rfl, hc, _⟩ := hmem a hm
      obtain ⟨c', rfl, hc', _⟩ := hmem a' hm'
      apply congrArg Sum.inr
      apply Subtype.ext
      funext k
      by_cases hk : k = i
      · subst k; exact he
      · rw [hc k hk, hc' k hk]
    calc
      _ ≤ (poolSites b i j).card := Finset.card_le_card_of_injOn _ hmaps hinj
      _ = pool b j := by simp [pool, ha]
      _ ≤ _ := by
        rw [pool_eq_of_rows b j 0]
        have hp := pool_le_70 b 0
        change pool b 0 ≤ 55 + min 15 (pool b 0 - 55)
        rw [min_eq_right (by omega : pool b 0 - 55 ≤ 15)]
        omega

end SharpOC.Witness1387
