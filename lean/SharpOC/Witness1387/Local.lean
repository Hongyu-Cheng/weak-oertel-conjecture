import SharpOC.LatticeGeometry

/-! The local adaptive fold used by the dimension-1387 witness. -/

namespace SharpOC.Witness1387

open scoped BigOperators

set_option Elab.async false

/-- The first eight coordinates carry the ordinary mask. -/
def ordIdx (i : Fin 8) : Fin 11 := i.castAdd 3

/-- The last three coordinates carry the selector. -/
def selIdx (j : Fin 3) : Fin 11 := j.natAdd 8

private def ordinarySum (z : Fin 11 → ℤ) : ℤ := ∑ i : Fin 8, z (ordIdx i)

private def selectorSum (z : Fin 11 → ℤ) : ℤ := ∑ j : Fin 3, z (selIdx j)

def localRow (z : Fin 11 → ℤ) (j : Fin 4) : ℤ :=
  Fin.lastCases (ordinarySum z) (fun k : Fin 3 => ordinarySum z - z (selIdx k)) j

def localGuard (z : Fin 11 → ℤ) : ℤ := 4 * ordinarySum z - selectorSum z

theorem localGuard_eq_sum_row (z : Fin 11 → ℤ) :
    localGuard z = ∑ j : Fin 4, localRow z j := by
  rw [Fin.sum_univ_castSucc]
  simp only [localRow, Fin.lastCases_castSucc, Fin.lastCases_last]
  simp [localGuard, selectorSum, Finset.sum_sub_distrib]
  ring

@[simp] theorem localGuard_zero : localGuard 0 = 0 := by
  simp [localGuard, ordinarySum, selectorSum]

@[simp] theorem localGuard_neg (z : Fin 11 → ℤ) : localGuard (-z) = -localGuard z := by
  simp [localGuard, ordinarySum, selectorSum, Finset.sum_neg_distrib]
  ring

@[simp] theorem localRow_neg (z : Fin 11 → ℤ) (j : Fin 4) :
    localRow (-z) j = -localRow z j := by
  refine Fin.lastCases (motive := fun i => localRow (-z) i = -localRow z i)
    ?_ (fun k => ?_) j
  · simp only [localRow, Fin.lastCases_last]
    simp [ordinarySum, Finset.sum_neg_distrib]
  · simp only [localRow, Fin.lastCases_castSucc]
    simp [ordinarySum, Finset.sum_neg_distrib]
    ring

def localReal (z : Fin 11 → ℤ) (i : Fin 11) : ℝ := z i

noncomputable def localGuardReal : (Fin 11 → ℝ) →ₗ[ℝ] ℝ :=
  (4 : ℝ) • (∑ i : Fin 8, LinearMap.proj (ordIdx i)) -
    ∑ j : Fin 3, LinearMap.proj (selIdx j)

@[simp] theorem localGuardReal_localReal (z : Fin 11 → ℤ) :
    localGuardReal (localReal z) = (localGuard z : ℝ) := by
  simp [localGuardReal, localReal, localGuard, ordinarySum, selectorSum, LinearMap.sum_apply]

/-- The selector-dependent linear forms determining the ordinary signs. -/
def foldForm (i : Fin 8) (s : Fin 3 → ℤ) : ℤ :=
  if i.val < 4 then 2 * s 0 + 2 * s 1 - 3 * s 2
  else if i.val < 7 then -2 * s 0 - 2 * s 1 + 3 * s 2
  else -2 * s 0 - 2 * s 1 + 5 * s 2

private def bit (a : Fin 2048) (k : ℕ) : ℤ := if a.val.testBit k then 1 else 0

private def rawSelector (a : Fin 2048) (j : Fin 3) : ℤ := bit a (8 + j.val)

private def foldSign (i : Fin 8) (s : Fin 3 → ℤ) : ℤ :=
  if s 0 = 0 ∧ s 1 = 0 ∧ s 2 = 0 then 1 else if 0 < foldForm i s then 1 else -1

private def rawPoint (a : Fin 2048) : Fin 11 → ℤ :=
  fun j => Fin.addCases (motive := fun _ => ℤ)
    (fun i : Fin 8 => foldSign i (rawSelector a) * bit a i.val) (rawSelector a) j

/-- A positive-guard orientation of each parity representative. -/
def localBase (a : Fin 2048) : Fin 11 → ℤ :=
  if localGuard (rawPoint a) < 0 then -rawPoint a else rawPoint a

def eligible (a : Fin 2048) : Bool := decide (localGuard (localBase a) = 1)

/-- The first positive row, with zero assigned to the first owner. -/
def owner (a : Fin 2048) : Fin 4 :=
  if 0 < localRow (localBase a) 0 then 0
  else if 0 < localRow (localBase a) 1 then 1
  else if 0 < localRow (localBase a) 2 then 2
  else if 0 < localRow (localBase a) 3 then 3 else 0

/-- The ordinary-coordinate correction in the ranked code. -/
def codeCorrection (j : Fin 4) (i : Fin 8) : ℤ :=
  if j.val < 2 then if i.val < 4 then 1 else 0
  else if j.val = 2 then if 4 ≤ i.val then 1 else 0
  else if 4 ≤ i.val ∧ i.val < 7 then 1 else 0

def code (a : Fin 2048) : ℕ :=
  if eligible a then
    (∑ i : Fin 8, (localBase a (ordIdx i) + codeCorrection (owner a) i) * (2 : ℤ)^i.val).toNat
  else 0

def codeBit (a : Fin 2048) (i : Fin 8) : Bool := (code a).testBit i.val

def high (a : Fin 2048) : Bool := eligible a && decide (code a % 4 ≠ 0)

@[simp] theorem eligible_iff (a : Fin 2048) :
    eligible a = true ↔ localGuard (localBase a) = 1 := by simp [eligible]

@[simp] theorem localBase_zero : localBase 0 = 0 := by decide +kernel

@[simp] theorem eligible_zero : eligible 0 = false := by decide +kernel

@[simp] theorem high_zero : high 0 = false := by simp [high]

/-- The local sites, allowing a sign flip exactly for the eligible masks. -/
def localSites : Set (Fin 11 → ℤ) :=
  Set.range localBase ∪ Set.range (fun a : {a : Fin 2048 // eligible a = true} => -localBase a.val)

theorem localSites_finite : localSites.Finite :=
  (Set.finite_range _).union (Set.finite_range _)

@[simp] private theorem rawPoint_ord (a : Fin 2048) (i : Fin 8) :
    rawPoint a (ordIdx i) = foldSign i (rawSelector a) * bit a i.val := by
  simp only [rawPoint, ordIdx, Fin.addCases_left]

@[simp] private theorem rawPoint_sel (a : Fin 2048) (j : Fin 3) :
    rawPoint a (selIdx j) = rawSelector a j := by
  simp only [rawPoint, selIdx, Fin.addCases_right]

private theorem bit_binary (a : Fin 2048) (k : ℕ) : bit a k = 0 ∨ bit a k = 1 := by
  unfold bit
  split <;> simp

private theorem foldSign_values (i : Fin 8) (s : Fin 3 → ℤ) :
    foldSign i s = 1 ∨ foldSign i s = -1 := by
  unfold foldSign
  split_ifs <;> simp

private theorem rawPoint_abs (a : Fin 2048) (i : Fin 11) :
    (rawPoint a i).natAbs = if a.val.testBit i.val then 1 else 0 := by
  refine Fin.addCases (m := 8) (n := 3) (motive := fun i => (rawPoint a i).natAbs =
    if a.val.testBit i.val then 1 else 0) ?_ ?_ i
  · intro j
    change (rawPoint a (ordIdx j)).natAbs = _
    rw [rawPoint_ord]
    rcases foldSign_values j (rawSelector a) with h | h <;>
      cases hb : a.val.testBit j.val <;> simp [h, bit, hb]
  · intro j
    change (rawPoint a (selIdx j)).natAbs = _
    rw [rawPoint_sel]
    cases hb : a.val.testBit (8 + j.val) <;> simp [rawSelector, bit, hb]

private theorem localBase_abs (a : Fin 2048) (i : Fin 11) :
    (localBase a i).natAbs = if a.val.testBit i.val then 1 else 0 := by
  unfold localBase
  split <;> simpa using rawPoint_abs a i

theorem localBase_injective : Function.Injective localBase := by
  intro a b h
  apply Fin.ext
  apply Nat.eq_of_testBit_eq
  intro k
  by_cases hk : k < 11
  · have habs := congrArg (fun v : Fin 11 → ℤ => (v ⟨k, hk⟩).natAbs) h
    simp only [localBase_abs] at habs
    change (if a.val.testBit k then 1 else 0) = (if b.val.testBit k then 1 else 0) at habs
    cases ha : a.val.testBit k <;> cases hb : b.val.testBit k <;> simp_all
  · have hpow : 2048 ≤ 2 ^ k := Nat.pow_le_pow_right (by decide : (0 : ℕ) < 2) (by omega : 11 ≤ k)
    rw [Nat.testBit_lt_two_pow (lt_of_lt_of_le a.isLt hpow),
      Nat.testBit_lt_two_pow (lt_of_lt_of_le b.isLt hpow)]

@[simp] theorem localBase_eq_zero_iff (a : Fin 2048) : localBase a = 0 ↔ a = 0 := by
  rw [← localBase_zero]
  exact localBase_injective.eq_iff

theorem localGuard_base_nonneg (a : Fin 2048) : 0 ≤ localGuard (localBase a) := by
  unfold localBase
  split <;> simp_all <;> omega

set_option maxRecDepth 20000 in
set_option maxHeartbeats 0 in
private theorem all_local_guard_pos :
    ∀ a : Fin 2048, a ≠ 0 → 0 < localGuard (localBase a) := by decide +kernel

theorem localGuard_base_pos (a : Fin 2048) (ha : a ≠ 0) : 0 < localGuard (localBase a) :=
  all_local_guard_pos a ha

set_option maxRecDepth 20000 in
set_option maxHeartbeats 0 in
private theorem all_local_row_nonneg :
    ∀ (a : Fin 2048) (j : Fin 4), 0 ≤ localRow (localBase a) j := by decide +kernel

theorem localRow_base_nonneg (a : Fin 2048) (j : Fin 4) :
    0 ≤ localRow (localBase a) j := all_local_row_nonneg a j

theorem code_eq_sum (a : Fin 2048) (ha : eligible a = true) :
    code a =
      (∑ i : Fin 8, (localBase a (ordIdx i) + codeCorrection (owner a) i) * (2 : ℤ)^i.val).toNat :=
  by simp [code, ha]

set_option maxRecDepth 20000 in
set_option maxHeartbeats 0 in
private theorem all_eligible_rows :
    ∀ (a : Fin 2048) (j : Fin 4), eligible a = true →
      localRow (localBase a) j = if j = owner a then 1 else 0 := by decide +kernel

theorem eligible_row (a : Fin 2048) (ha : eligible a = true) (j : Fin 4) :
    localRow (localBase a) j = if j = owner a then 1 else 0 :=
  all_eligible_rows a j ha

set_option maxRecDepth 20000 in
set_option maxHeartbeats 0 in
private theorem all_eligible_code_bits :
    ∀ (a : Fin 2048) (i : Fin 8), eligible a = true →
      (if codeBit a i then (1 : ℤ) else 0) =
        localBase a (ordIdx i) + codeCorrection (owner a) i := by decide +kernel

theorem eligible_code_bit (a : Fin 2048) (ha : eligible a = true) (i : Fin 8) :
    (if codeBit a i then (1 : ℤ) else 0) =
      localBase a (ordIdx i) + codeCorrection (owner a) i :=
  all_eligible_code_bits a i ha

set_option maxRecDepth 20000 in
set_option maxHeartbeats 0 in
private theorem all_eligible_code_bounds :
    ∀ a : Fin 2048, eligible a = true → code a < 256 ∧
      (Finset.univ.filter fun i : Fin 8 => codeBit a i = true).card = 4 := by decide +kernel

theorem eligible_code_lt (a : Fin 2048) (ha : eligible a = true) : code a < 256 :=
  (all_eligible_code_bounds a ha).1

theorem eligible_code_weight (a : Fin 2048) (ha : eligible a = true) :
    (Finset.univ.filter fun i : Fin 8 => codeBit a i = true).card = 4 :=
  (all_eligible_code_bounds a ha).2

/-- The selector is negative at the first three owners and positive at the fourth. -/
def ownerSelector (j : Fin 4) (k : Fin 3) : ℤ :=
  if j.val = 3 then 1 else if j.val = k.val then -1 else 0

set_option maxRecDepth 20000 in
set_option maxHeartbeats 0 in
private theorem all_eligible_selectors :
    ∀ (a : Fin 2048) (k : Fin 3), eligible a = true →
      localBase a (selIdx k) = ownerSelector (owner a) k := by decide +kernel

theorem eligible_selector (a : Fin 2048) (ha : eligible a = true) (k : Fin 3) :
    localBase a (selIdx k) = ownerSelector (owner a) k :=
  all_eligible_selectors a k ha

theorem eligible_owner_code_injective {a b : Fin 2048}
    (ha : eligible a = true) (hb : eligible b = true)
    (ho : owner a = owner b) (hc : code a = code b) : a = b := by
  apply localBase_injective
  funext i
  refine Fin.addCases (m := 8) (n := 3)
    (motive := fun i => localBase a i = localBase b i) ?_ ?_ i
  · intro j
    change localBase a (ordIdx j) = localBase b (ordIdx j)
    have hbit : codeBit a j = codeBit b j := by simp [codeBit, hc]
    have hA := eligible_code_bit a ha j
    have hB := eligible_code_bit b hb j
    rw [hbit, ho] at hA
    omega
  · intro j
    change localBase a (selIdx j) = localBase b (selIdx j)
    rw [eligible_selector a ha, eligible_selector b hb, ho]

set_option maxRecDepth 20000 in
set_option maxHeartbeats 0 in
private theorem all_owner_counts :
    ∀ j : Fin 4,
      (Finset.univ.filter fun a : Fin 2048 => eligible a = true ∧ owner a = j).card = 70 ∧
      (Finset.univ.filter fun a : Fin 2048 => high a = true ∧ owner a = j).card = 55 ∧
      (Finset.univ.filter fun a : Fin 2048 =>
        eligible a = true ∧ high a = false ∧ owner a = j).card = 15 := by decide +kernel

theorem eligible_owner_count (j : Fin 4) :
    (Finset.univ.filter fun a : Fin 2048 => eligible a = true ∧ owner a = j).card = 70 :=
  (all_owner_counts j).1

theorem high_owner_count (j : Fin 4) :
    (Finset.univ.filter fun a : Fin 2048 => high a = true ∧ owner a = j).card = 55 :=
  (all_owner_counts j).2.1

theorem tail_owner_count (j : Fin 4) :
    (Finset.univ.filter fun a : Fin 2048 =>
      eligible a = true ∧ high a = false ∧ owner a = j).card = 15 :=
  (all_owner_counts j).2.2

private def localShape (z : Fin 11 → ℤ) : Prop :=
  (∀ i, (-1 : ℤ) ≤ z i ∧ z i ≤ 1) ∧
  ((∀ j, 0 ≤ z (selIdx j)) ∨ (∀ j, z (selIdx j) ≤ 0)) ∧
  (∀ i : Fin 8, (∀ j, z (selIdx j) = 0) →
    z (ordIdx i) = 0 ∨ z (ordIdx i) = 1) ∧
  (∀ i : Fin 8, (∃ j, z (selIdx j) ≠ 0) → z (ordIdx i) ≠ 0 →
    0 < z (ordIdx i) * foldForm i (fun j => z (selIdx j)))

private instance (z : Fin 11 → ℤ) : Decidable (localShape z) := by
  unfold localShape
  infer_instance

private def maskIndex (s : Fin 8) (m : Fin 256) : Fin 2048 :=
  ⟨m.val + 256 * s.val, by have := m.isLt; have := s.isLt; omega⟩

private theorem maskIndex_surj (a : Fin 2048) : ∃ s m, maskIndex s m = a := by
  refine ⟨⟨a.val / 256, by have := a.isLt; omega⟩,
    ⟨a.val % 256, Nat.mod_lt _ (by decide)⟩, ?_⟩
  apply Fin.ext
  simp only [maskIndex]
  have := Nat.div_add_mod a.val 256
  omega

set_option maxRecDepth 20000 in
set_option maxHeartbeats 0 in
private theorem all_mask_shapes (s : Fin 8) :
    ∀ m : Fin 256, localShape (localBase (maskIndex s m)) ∧
      (eligible (maskIndex s m) = true → localShape (-localBase (maskIndex s m))) := by
  fin_cases s <;> decide +kernel

private theorem localSite_shape {z : Fin 11 → ℤ} (hz : z ∈ localSites) : localShape z := by
  rcases hz with ⟨a, rfl⟩ | ⟨a, rfl⟩
  · obtain ⟨s, m, rfl⟩ := maskIndex_surj a
    exact (all_mask_shapes s m).1
  · obtain ⟨s, m, h⟩ := maskIndex_surj a.val
    simpa [h] using (all_mask_shapes s m).2 (by simpa [h] using a.property)

private theorem weighted_upper {ι : Type*} [Fintype ι] (w f : ι → ℝ) (b : ℝ)
    (hw : ∀ a, 0 ≤ w a) (hs : ∑ a, w a = 1)
    (h : ∀ a, w a ≠ 0 → f a ≤ b) : ∑ a, w a * f a ≤ b := by
  calc
    _ ≤ ∑ a, w a * b := by
      apply Finset.sum_le_sum
      intro a _
      by_cases ha : w a = 0
      · simp [ha]
      · exact mul_le_mul_of_nonneg_left (h a ha) (hw a)
    _ = b := by rw [← Finset.sum_mul, hs, one_mul]

private theorem weighted_saturation {ι : Type*} [Fintype ι] (w f : ι → ℝ) (b : ℝ)
    (hw : ∀ a, 0 ≤ w a) (hs : ∑ a, w a = 1)
    (h : ∀ a, w a ≠ 0 → f a ≤ b) (havg : ∑ a, w a * f a = b)
    (a : ι) (ha : w a ≠ 0) : f a = b := by
  classical
  have hterm : ∀ k ∈ (Finset.univ : Finset ι), 0 ≤ w k * (b - f k) := by
    intro k _
    by_cases hk : w k = 0
    · simp [hk]
    · exact mul_nonneg (hw k) (sub_nonneg.mpr (h k hk))
  have hsum : ∑ k, w k * (b - f k) = 0 := by
    simp_rw [mul_sub]
    rw [Finset.sum_sub_distrib, ← Finset.sum_mul, hs, one_mul, havg, sub_self]
  have hz := (Finset.sum_eq_zero_iff_of_nonneg hterm).mp hsum a (Finset.mem_univ a)
  exact (sub_eq_zero.mp ((mul_eq_zero.mp hz).resolve_left ha)).symm

private theorem binary_average_support {ι : Type*} [Fintype ι]
    (w : ι → ℝ) (f : ι → ℤ) (n : ℤ) (hw : ∀ a, 0 ≤ w a) (hs : ∑ a, w a = 1)
    (hf : ∀ a, w a ≠ 0 → f a = 0 ∨ f a = 1)
    (havg : ∑ a, w a * (f a : ℝ) = (n : ℝ)) (a : ι) (ha : w a ≠ 0) : f a = n := by
  have hneg : ∑ a, w a * (-(f a : ℝ)) = -(n : ℝ) := by
    simpa only [mul_neg, Finset.sum_neg_distrib] using congrArg Neg.neg havg
  have hle (k : ι) (hk : w k ≠ 0) : (f k : ℝ) ≤ 1 := by rcases hf k hk with hh | hh <;> simp [hh]
  have hlow (k : ι) (hk : w k ≠ 0) : -(f k : ℝ) ≤ 0 := by rcases hf k hk with hh | hh <;> simp [hh]
  have h1 := weighted_upper w (fun k => (f k : ℝ)) 1 hw hs hle
  have h0 := weighted_upper w (fun k => -(f k : ℝ)) 0 hw hs hlow
  rw [havg] at h1
  rw [hneg] at h0
  have hn1 : n ≤ 1 := by exact_mod_cast h1
  have hn0 : 0 ≤ n := by exact_mod_cast (show (0 : ℝ) ≤ (n : ℝ) by linarith)
  have hn : n = 0 ∨ n = 1 := by omega
  rcases hn with rfl | rfl
  · have hh := weighted_saturation w (fun k => -(f k : ℝ)) 0 hw hs hlow (by simpa using hneg) a ha
    exact_mod_cast (show (f a : ℝ) = 0 by linarith)
  · have hh := weighted_saturation w (fun k => (f k : ℝ)) 1 hw hs hle (by simpa using havg) a ha
    exact_mod_cast hh

private noncomputable def foldFormReal (i : Fin 8) : (Fin 11 → ℝ) →ₗ[ℝ] ℝ :=
  let s (k : Fin 3) := LinearMap.proj (R := ℝ) (φ := fun _ : Fin 11 => ℝ) (selIdx k)
  if i.val < 4 then (2 : ℝ) • s 0 + (2 : ℝ) • s 1 - (3 : ℝ) • s 2
  else if i.val < 7 then (-2 : ℝ) • s 0 - (2 : ℝ) • s 1 + (3 : ℝ) • s 2
  else (-2 : ℝ) • s 0 - (2 : ℝ) • s 1 + (5 : ℝ) • s 2

@[simp] private theorem foldFormReal_apply (i : Fin 8) (z : Fin 11 → ℤ) :
    foldFormReal i (localReal z) = (foldForm i (fun j => z (selIdx j)) : ℝ) := by
  unfold foldFormReal foldForm
  split_ifs <;> simp [localReal]

private theorem foldForm_zero (i : Fin 8) (s : Fin 3 → ℤ) (h : ∀ j, s j = 0) :
    foldForm i s = 0 := by simp [foldForm, h]

private theorem int_subfamily_census {S : Set (Fin 11 → ℤ)} (hsub : S ⊆ localSites)
    (z : Fin 11 → ℤ) (hne : z ≠ 0)
    (hz : localReal z ∈ convexHull ℝ (localReal '' S)) : z ∈ S := by
  classical
  letI : Fintype S := (localSites_finite.subset hsub).fintype
  let f (a : S) := localReal a.val
  have hrange : Set.range f = localReal '' S := by
    ext v
    exact ⟨fun ⟨a, h⟩ => ⟨a.val, a.property, h⟩, fun ⟨a, ha, h⟩ => ⟨⟨a, ha⟩, h⟩⟩
  rw [← hrange] at hz
  obtain ⟨w, hw, hs, havg⟩ := (mem_convexHull_range_iff_weights f _).mp hz
  have hsite (a : S) := localSite_shape (hsub a.property)
  have havgCoord (i : Fin 11) : ∑ a, w a * (a.val i : ℝ) = (z i : ℝ) := by
    simpa only [f, localReal, Finset.sum_apply, Pi.smul_apply, smul_eq_mul] using congrFun havg i
  have havgNeg (i : Fin 11) : ∑ a, w a * (-(a.val i : ℝ)) = -(z i : ℝ) := by
    simpa only [mul_neg, Finset.sum_neg_distrib] using congrArg Neg.neg (havgCoord i)
  have hcoord (i : Fin 11) : (-1 : ℤ) ≤ z i ∧ z i ≤ 1 := by
    have hh := weighted_upper w (fun a => (a.val i : ℝ)) 1 hw hs (fun a _ => by
      exact_mod_cast (hsite a).1 i |>.2)
    have hl := weighted_upper w (fun a => -(a.val i : ℝ)) 1 hw hs (fun a _ => by
      have h := (hsite a).1 i |>.1
      exact_mod_cast (show -(a.val i) ≤ (1 : ℤ) by omega))
    rw [havgCoord] at hh
    rw [havgNeg] at hl
    exact ⟨by exact_mod_cast (show (-1 : ℝ) ≤ (z i : ℝ) by linarith), by exact_mod_cast hh⟩
  have hsat (i : Fin 11) (h : z i = 1 ∨ z i = -1) (a : S) (ha : w a ≠ 0) :
      a.val i = z i := by
    rcases h with h | h
    · have hh := weighted_saturation w (fun a => (a.val i : ℝ)) 1 hw hs (fun a _ => by
        exact_mod_cast (hsite a).1 i |>.2) (by rw [havgCoord, h]; norm_num) a ha
      rw [h]
      exact_mod_cast hh
    · have hh := weighted_saturation w (fun a => -(a.val i : ℝ)) 1 hw hs (fun a _ => by
        have h := (hsite a).1 i |>.1
        exact_mod_cast (show -(a.val i) ≤ (1 : ℤ) by omega))
        (by rw [havgNeg, h]; norm_num) a ha
      have h' : (a.val i : ℝ) = (z i : ℝ) := by rw [h]; push_cast; linarith
      exact_mod_cast h'
  have hbinary (i : Fin 11) (r : ℤ) (hr : r = 1 ∨ r = -1)
      (h : ∀ a : S, w a ≠ 0 → a.val i = 0 ∨ a.val i = r) (a : S) (ha : w a ≠ 0) :
      a.val i = z i := by
    rcases hr with rfl | rfl
    · exact binary_average_support w (fun a => a.val i) (z i) hw hs h (havgCoord i) a ha
    · have hh := binary_average_support w (fun a => -a.val i) (-z i) hw hs
        (fun a ha => by
          rcases h a ha with h0 | h1
          · simp [h0]
          · simp [h1])
        (by simpa using havgNeg i) a ha
      omega
  obtain ⟨a, ha⟩ : ∃ a, w a ≠ 0 := by
    by_contra! h
    simp [h] at hs
  suffices hm : ∀ b : S, w b ≠ 0 → b.val = z by
    rw [← hm a ha]
    exact a.property
  have allCoords (v : Fin 11 → ℤ) (hy : ∀ i, v (ordIdx i) = z (ordIdx i))
      (hs : ∀ j, v (selIdx j) = z (selIdx j)) : v = z := by
    funext i
    exact Fin.addCases (m := 8) (n := 3) (motive := fun i => v i = z i) hy hs i
  by_cases hzsel : ∃ j, z (selIdx j) ≠ 0
  · obtain ⟨j, hj⟩ := hzsel
    have hval : z (selIdx j) = 1 ∨ z (selIdx j) = -1 := by
      have := hcoord (selIdx j)
      omega
    have hselect (b : S) (hb : w b ≠ 0) (k : Fin 3) :
        b.val (selIdx k) = z (selIdx k) := by
      apply hbinary (selIdx k) (z (selIdx j)) hval _ b hb
      intro t ht
      have htj := hsat (selIdx j) hval t ht
      have htk := (hsite t).1 (selIdx k)
      rcases (hsite t).2.1 with hp | hn
      · have h1 := hp j
        have h2 := hp k
        omega
      · have h1 := hn j
        have h2 := hn k
        omega
    intro b hb
    apply allCoords b.val _ (hselect b hb)
    intro i
    let r : ℤ := if 0 < foldForm i (fun k => z (selIdx k)) then 1 else -1
    have hr : r = 1 ∨ r = -1 := by unfold r; split <;> simp
    apply hbinary (ordIdx i) r hr _ b hb
    intro t ht
    by_cases hzero : t.val (ordIdx i) = 0
    · exact Or.inl hzero
    · have hfold := (hsite t).2.2.2 i ⟨j, by rw [hselect t ht j]; exact hj⟩ hzero
      have hselEq : (fun k => t.val (selIdx k)) = (fun k => z (selIdx k)) := funext (hselect t ht)
      rw [hselEq] at hfold
      have hti := (hsite t).1 (ordIdx i)
      have htv : t.val (ordIdx i) = 1 ∨ t.val (ordIdx i) = -1 := by omega
      right
      rcases htv with h1 | h1
      · rw [h1, one_mul] at hfold
        simp [r, h1, hfold]
      · rw [h1, neg_one_mul] at hfold
        simp [r, h1, show ¬ 0 < foldForm i (fun k => z (selIdx k)) by omega]
  · have hzsel0 : ∀ j, z (selIdx j) = 0 := by simpa using hzsel
    obtain ⟨i, hi⟩ : ∃ i, z (ordIdx i) ≠ 0 := by
      by_contra! h
      exact hne (by
        funext k
        exact Fin.addCases (m := 8) (n := 3) (motive := fun k => z k = 0) h hzsel0 k)
    have hval : z (ordIdx i) = 1 ∨ z (ordIdx i) = -1 := by
      have := hcoord (ordIdx i)
      omega
    let L := -(z (ordIdx i) : ℝ) • foldFormReal i
    have hL0 : L (localReal z) = 0 := by
      simp [L, foldForm_zero i _ hzsel0]
    have havgL : ∑ a, w a * L (localReal a.val) = 0 := by
      rw [← hL0]
      simpa only [f, map_sum, map_smul, smul_eq_mul] using congrArg L havg
    have hLneg (b : S) (hb : w b ≠ 0) (ht : ∃ j, b.val (selIdx j) ≠ 0) :
        L (localReal b.val) < 0 := by
      have hbval := hsat (ordIdx i) hval b hb
      have hpos := (hsite b).2.2.2 i ht (by rw [hbval]; exact hi)
      rw [hbval] at hpos
      have hposR : 0 < (z (ordIdx i) : ℝ) * (foldForm i (fun j => b.val (selIdx j)) : ℝ) := by
        exact_mod_cast hpos
      simpa [L, neg_mul] using neg_neg_of_pos hposR
    have hLle (b : S) (hb : w b ≠ 0) : L (localReal b.val) ≤ 0 := by
      by_cases ht : ∃ j, b.val (selIdx j) ≠ 0
      · exact (hLneg b hb ht).le
      · have ht0 : ∀ j, b.val (selIdx j) = 0 := by simpa using ht
        simp [L, foldForm_zero i _ ht0]
    have hselZero (b : S) (hb : w b ≠ 0) : ∀ j, b.val (selIdx j) = 0 := by
      intro j
      by_contra ht
      have heq := weighted_saturation w (fun b : S => L (localReal b.val)) 0 hw hs hLle havgL b hb
      exact (ne_of_lt (hLneg b hb ⟨j, ht⟩)) heq
    intro b hb
    apply allCoords b.val _ (fun j => (hselZero b hb j).trans (hzsel0 j).symm)
    intro k
    exact hbinary (ordIdx k) 1 (Or.inl rfl)
      (fun t ht => (hsite t).2.2.1 k (hselZero t ht)) b hb

/-- The signed folded block has exactly the prescribed integer sites. -/
theorem local_integer_census (z : Fin 11 → ℤ) :
    localReal z ∈ convexHull ℝ (localReal '' localSites) ↔ z ∈ localSites := by
  constructor
  · intro hz
    by_cases h : z = 0
    · subst z
      exact Or.inl ⟨0, localBase_zero⟩
    · exact int_subfamily_census (Set.Subset.rfl) z h hz
  · intro hz
    exact subset_convexHull ℝ _ ⟨z, hz, rfl⟩

/-- Every nonzero local site is strictly exposed against all other sites. -/
theorem local_exposed {z : Fin 11 → ℤ} (_hz : z ∈ localSites) (hne : z ≠ 0) :
    ∃ w : (Fin 11 → ℝ) →ₗ[ℝ] ℝ,
      ∀ v ∈ localSites, v ≠ z → w (localReal v) < w (localReal z) := by
  let S := localSites \ {z}
  have hsub : S ⊆ localSites := Set.sdiff_subset
  have hn : localReal z ∉ convexHull ℝ (localReal '' S) := by
    intro h
    have hzS := int_subfamily_census hsub z hne h
    exact hzS.2 (Set.mem_singleton z)
  have hfinite : (localReal '' S).Finite := (localSites_finite.subset hsub).image localReal
  obtain ⟨F, t, hbelow, habove⟩ :=
    geometric_hahn_banach_closed_point (convex_convexHull ℝ _)
      (hfinite.isCompact_convexHull ℝ).isClosed hn
  refine ⟨F.toLinearMap, fun v hv hne => ?_⟩
  have hvS : v ∈ S := ⟨hv, by simpa using hne⟩
  exact (hbelow _ (subset_convexHull ℝ _ ⟨v, hvS, rfl⟩)).trans habove

end SharpOC.Witness1387
