import Mathlib

/-!
# Lattice geometry of a cube with attached negative unit vectors

This file checks the finite convex-combination argument used in Section 3
of the direct rational sharp-OC counterexample. It has no dimension bound.
It includes the actual `convexHull` integer census and exposed-fiber equality.
The grouped continuous-fiber containment is checked under explicit geometric
containment hypotheses; the specific source simplices and their volumes are
separate obligations.
-/

namespace SharpOC

open Finset

variable {α ι : Type*} [Fintype α] [Fintype ι] [DecidableEq ι]

/-- If a convex average reaches a common lower bound, all generators
strictly above the bound have zero weight. -/
theorem weight_eq_zero_of_average_eq_lower
    (w f : α → ℝ) (m : ℝ)
    (hw : ∀ a, 0 ≤ w a) (hw_sum : ∑ a, w a = 1)
    (hf : ∀ a, m ≤ f a) (havg : ∑ a, w a * f a = m)
    (a : α) (ha : m < f a) : w a = 0 := by
  have hsum : ∑ b, w b * (f b - m) = 0 := by
    simp_rw [mul_sub]
    rw [Finset.sum_sub_distrib, ← Finset.sum_mul, hw_sum, one_mul, havg]
    ring
  have hnonneg : ∀ b ∈ (Finset.univ : Finset α), 0 ≤ w b * (f b - m) := by
    intro b hb
    exact mul_nonneg (hw b) (sub_nonneg.mpr (hf b))
  have hle : w a * (f a - m) ≤ 0 := by
    calc
      w a * (f a - m) ≤ ∑ b, w b * (f b - m) :=
        Finset.single_le_sum hnonneg (Finset.mem_univ a)
      _ = 0 := hsum
  have hz : w a * (f a - m) = 0 := le_antisymm hle (hnonneg a (by simp))
  exact (mul_eq_zero.mp hz).resolve_right (ne_of_gt (sub_pos.mpr ha))

/-- The analogous rigidity statement for a common upper bound. -/
theorem weight_eq_zero_of_average_eq_upper
    (w f : α → ℝ) (m : ℝ)
    (hw : ∀ a, 0 ≤ w a) (hw_sum : ∑ a, w a = 1)
    (hf : ∀ a, f a ≤ m) (havg : ∑ a, w a * f a = m)
    (a : α) (ha : f a < m) : w a = 0 := by
  apply weight_eq_zero_of_average_eq_lower w (fun b => -f b) (-m)
    hw hw_sum (fun b => neg_le_neg (hf b))
  · simpa only [mul_neg, Finset.sum_neg_distrib] using congrArg Neg.neg havg
  · exact neg_lt_neg ha

/-- The finite family indexing every cube vertex and every negative unit vector. -/
abbrev ProjectionIndex (ι : Type*) := Sum (ι → Bool) ι

def projectionGenerator (a : ProjectionIndex ι) (i : ι) : ℝ :=
  match a with
  | .inl v => if v i then 1 else 0
  | .inr j => if i = j then -1 else 0

def negativeUnit (j : ι) (i : ι) : ℝ := if i = j then -1 else 0

omit [Fintype ι] in
theorem projectionGenerator_bounds (a : ProjectionIndex ι) (i : ι) :
    -1 ≤ projectionGenerator a i ∧ projectionGenerator a i ≤ 1 := by
  cases a with
  | inl v => cases h : v i <;> simp [projectionGenerator, h]
  | inr j => by_cases h : i = j <;> simp [projectionGenerator, h]

omit [Fintype ι] in
theorem projectionGenerator_gt_neg_one (i : ι) (a : ProjectionIndex ι)
    (ha : a ≠ .inr i) : -1 < projectionGenerator a i := by
  cases a with
  | inl v => cases h : v i <;> simp [projectionGenerator, h]
  | inr j =>
    have hij : i ≠ j := by
      intro h
      apply ha
      simp [h]
    simp [projectionGenerator, hij]

/-- The coordinatewise bounds for any convex combination of the generators. -/
theorem projection_average_bounds
    (w : ProjectionIndex ι → ℝ)
    (hw : ∀ a, 0 ≤ w a) (hw_sum : ∑ a, w a = 1) (i : ι) :
    -1 ≤ ∑ a, w a * projectionGenerator a i ∧
    (∑ a, w a * projectionGenerator a i) ≤ 1 := by
  constructor
  · calc
      -1 = ∑ a, w a * (-1) := by rw [← Finset.sum_mul, hw_sum]; ring
      _ ≤ ∑ a, w a * projectionGenerator a i := by
        apply Finset.sum_le_sum
        intro a ha
        exact mul_le_mul_of_nonneg_left (projectionGenerator_bounds a i).1 (hw a)
  · calc
      (∑ a, w a * projectionGenerator a i) ≤ ∑ a, w a * 1 := by
        apply Finset.sum_le_sum
        intro a ha
        exact mul_le_mul_of_nonneg_left (projectionGenerator_bounds a i).2 (hw a)
      _ = 1 := by simpa using hw_sum

/-- Reaching -1 in coordinate i forces the entire convex combination to
equal the negative i-th unit vector. -/
theorem projection_average_eq_negative_unit
    (w : ProjectionIndex ι → ℝ)
    (hw : ∀ a, 0 ≤ w a) (hw_sum : ∑ a, w a = 1)
    (i : ι) (hi : ∑ a, w a * projectionGenerator a i = -1) :
    (fun j => ∑ a, w a * projectionGenerator a j) = negativeUnit i := by
  classical
  have hz : ∀ a, a ≠ .inr i → w a = 0 := by
    intro a ha
    exact weight_eq_zero_of_average_eq_lower w
      (fun b => projectionGenerator b i) (-1) hw hw_sum
      (fun b => (projectionGenerator_bounds b i).1) hi a
      (projectionGenerator_gt_neg_one i a ha)
  have hwi : w (.inr i) = 1 := by
    calc
      w (.inr i) = ∑ a, w a := by
        symm
        apply Finset.sum_eq_single (s := Finset.univ) (a := (Sum.inr i : ProjectionIndex ι))
        · intro a ha hne
          exact hz a hne
        · simp
      _ = 1 := hw_sum
  funext j
  calc
    (∑ a, w a * projectionGenerator a j) =
        w (.inr i) * projectionGenerator (.inr i) j := by
      apply Finset.sum_eq_single (s := Finset.univ) (a := (Sum.inr i : ProjectionIndex ι))
      · intro a ha hne
        rw [hz a hne, zero_mul]
      · simp
    _ = negativeUnit i j := by simp [hwi, projectionGenerator, negativeUnit]

/-- Complete integer-point census for the convex-combination presentation:
an integer point is either a cube vertex or a negative unit vector. -/
theorem integer_projection_census
    (w : ProjectionIndex ι → ℝ) (z : ι → ℤ)
    (hw : ∀ a, 0 ≤ w a) (hw_sum : ∑ a, w a = 1)
    (hz : ∀ i, (z i : ℝ) = ∑ a, w a * projectionGenerator a i) :
    (∀ i, z i = 0 ∨ z i = 1) ∨
    (∃ j, ∀ i, (z i : ℝ) = negativeUnit j i) := by
  by_cases hminus : ∃ i, z i = -1
  · rcases hminus with ⟨i, hi⟩
    right
    refine ⟨i, ?_⟩
    have havi : ∑ a, w a * projectionGenerator a i = -1 := by
      rw [← hz i, hi]
      norm_num
    have heq := projection_average_eq_negative_unit w hw hw_sum i havi
    intro j
    rw [hz j]
    exact congrFun heq j
  · left
    intro i
    have hbounds := projection_average_bounds w hw hw_sum i
    rw [← hz i] at hbounds
    have hl : (-1 : ℤ) ≤ z i := by exact_mod_cast hbounds.1
    have hu : z i ≤ (1 : ℤ) := by exact_mod_cast hbounds.2
    have hne : z i ≠ -1 := by
      intro hi
      exact hminus ⟨i, hi⟩
    omega

/-- For a finite indexed family, convex-hull membership has a convex
combination using all family indices, with zero weights allowed. -/
theorem mem_convexHull_range_iff_weights
    {E : Type*} [AddCommGroup E] [Module ℝ E]
    (v : α → E) (x : E) :
    x ∈ convexHull ℝ (Set.range v) ↔
      ∃ w : α → ℝ, (∀ a, 0 ≤ w a) ∧
        (∑ a, w a = 1) ∧ ∑ a, w a • v a = x := by
  classical
  constructor
  · intro hx
    rw [convexHull_range_eq_exists_affineCombination] at hx
    obtain ⟨s, w, hw, hs, hv⟩ := hx
    refine ⟨fun a => if a ∈ s then w a else 0, ?_, ?_, ?_⟩
    · intro a
      dsimp only
      split_ifs with ha
      · exact hw a ha
      · exact le_refl 0
    · simpa using hs
    · rw [Finset.affineCombination_eq_linear_combination s v w hs] at hv
      simpa only [ite_smul, zero_smul, Finset.sum_ite_mem, Finset.univ_inter] using hv
  · rintro ⟨w, hw, hs, hx⟩
    exact mem_convexHull_of_exists_fintype w v hw hs (fun a => ⟨a, rfl⟩) hx

/-- The actual convex hull has exactly the asserted integer points.
This is not conditional on an unproved convex-representation principle. -/
theorem integer_mem_projection_convexHull_iff (z : ι → ℤ) :
    (fun i => (z i : ℝ)) ∈
        convexHull ℝ (Set.range (projectionGenerator (ι := ι))) ↔
    (∀ i, z i = 0 ∨ z i = 1) ∨
    (∃ j, ∀ i, (z i : ℝ) = negativeUnit j i) := by
  classical
  constructor
  · intro hz
    obtain ⟨w, hw, hs, hx⟩ :=
      (mem_convexHull_range_iff_weights projectionGenerator _).mp hz
    apply integer_projection_census w z hw hs
    intro i
    simpa only [Finset.sum_apply, Pi.smul_apply, smul_eq_mul] using
      (congrFun hx i).symm
  · intro hz
    apply subset_convexHull ℝ _
    rcases hz with hz | ⟨j, hj⟩
    · refine ⟨.inl (fun i => decide (z i = 1)), ?_⟩
      funext i
      rcases hz i with hi | hi <;> simp [projectionGenerator, hi]
    · refine ⟨.inr j, ?_⟩
      funext i
      simpa only [projectionGenerator, negativeUnit] using (hj i).symm

/-- Incidence vectors of all subsets, including the empty subset. -/
def cubeVector (I : Finset ι) (i : ι) : ℝ := if i ∈ I then 1 else 0

/-- The integer-coordinate equation at the origin determines each negative
unit weight as the sum of incident cube weights. -/
theorem zero_coordinate_weight_balance
    (lam : Finset ι → ℝ) (μ : ι → ℝ)
    (hzero : ∀ i, (∑ I, lam I * cubeVector I i) +
      (∑ j, μ j * negativeUnit j i) = 0) :
    ∀ i, μ i = ∑ I, if i ∈ I then lam I else 0 := by
  intro i
  have hi := hzero i
  simp only [cubeVector, mul_ite, mul_one, mul_zero] at hi
  have hneg : ∑ j, μ j * negativeUnit j i = -μ i := by
    simp [negativeUnit]
  rw [hneg] at hi
  linarith

/-- Summing the coordinate balances accounts for every occurrence of a
negative unit weight. -/
theorem total_negative_weight
    (lam : Finset ι → ℝ) (μ : ι → ℝ)
    (hbalance : ∀ i, μ i = ∑ I, if i ∈ I then lam I else 0) :
    ∑ i, μ i = ∑ I, (I.card : ℝ) * lam I := by
  simp_rw [hbalance]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro I hI
  simp

/-- The exact normalization needed by the origin-fiber convexity argument. -/
theorem origin_regrouped_weights_sum_one
    (lam : Finset ι → ℝ) (μ : ι → ℝ)
    (hbalance : ∀ i, μ i = ∑ I, if i ∈ I then lam I else 0)
    (htotal : (∑ I, lam I) + (∑ i, μ i) = 1) :
    ∑ I, ((I.card : ℝ) + 1) * lam I = 1 := by
  rw [total_negative_weight lam μ hbalance] at htotal
  simpa only [add_mul, one_mul, Finset.sum_add_distrib, add_comm] using htotal

/-- The corresponding continuous-coordinate regrouping, valid in any real
module and with arbitrary zero weights. -/
theorem origin_continuous_regrouping
    {E : Type*} [AddCommGroup E] [Module ℝ E]
    (lam : Finset ι → ℝ) (μ : ι → ℝ) (u : ι → E)
    (hbalance : ∀ i, μ i = ∑ I, if i ∈ I then lam I else 0) :
    ∑ i, μ i • u i = ∑ I, lam I • ∑ i ∈ I, u i := by
  simp_rw [hbalance, Finset.sum_smul]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro I hI
  simp [Finset.smul_sum]

/-- The origin-fiber convexity argument after the grouped containments have
been supplied. The empty subset is the middle fiber, so no exceptional
case or division by a potentially zero weight is used. -/
theorem origin_continuous_mem_of_grouped_containments
    {E : Type*} [AddCommGroup E] [Module ℝ E]
    (B : Set E) (hB : Convex ℝ B)
    (lam : Finset ι → ℝ) (μ : ι → ℝ)
    (x : Finset ι → E) (u : ι → E)
    (hlam : ∀ I, 0 ≤ lam I)
    (hbalance : ∀ i, μ i = ∑ I, if i ∈ I then lam I else 0)
    (htotal : (∑ I, lam I) + (∑ i, μ i) = 1)
    (hgroup : ∀ I, ∃ y ∈ B,
      x I + ∑ i ∈ I, u i = ((I.card : ℝ) + 1) • y) :
    (∑ I, lam I • x I) + (∑ i, μ i • u i) ∈ B := by
  classical
  choose y hy hxy using hgroup
  have hnorm := origin_regrouped_weights_sum_one lam μ hbalance htotal
  have heq : (∑ I, lam I • x I) + (∑ i, μ i • u i) =
      ∑ I, (((I.card : ℝ) + 1) * lam I) • y I := by
    rw [origin_continuous_regrouping lam μ u hbalance, ← Finset.sum_add_distrib]
    apply Finset.sum_congr rfl
    intro I hI
    rw [← smul_add, hxy I, smul_smul, mul_comm]
  rw [heq]
  apply hB.sum_mem _ hnorm (fun I _ => hy I)
  intro I hI
  exact mul_nonneg (by positivity) (hlam I)

/-- An exposed base point cannot acquire extra continuous-fiber points
when taking the convex hull of a family of convex fibers. -/
theorem exposed_fiber_convexHull
    {Z E : Type*} [AddCommGroup Z] [Module ℝ Z]
    [AddCommGroup E] [Module ℝ E]
    (z : α → Z) (K : α → Set E) (a₀ : α)
    (hK : Convex ℝ (K a₀)) (hne : (K a₀).Nonempty)
    (ℓ : Z →ₗ[ℝ] ℝ)
    (hexpose : ∀ a, a ≠ a₀ → ℓ (z a) < ℓ (z a₀)) :
    {x | (z a₀, x) ∈ convexHull ℝ {p : Z × E | ∃ a, p.1 = z a ∧ p.2 ∈ K a}} =
      K a₀ := by
  classical
  ext x
  constructor
  · intro hx
    obtain ⟨β, _, w, p, hw, hs, hp, havg⟩ :=
      mem_convexHull_iff_exists_fintype.mp hx
    choose a ha hk using hp
    have hsumz : ∑ b, w b • (p b).1 = z a₀ := by
      simpa only [Prod.fst_sum, Prod.smul_def] using congrArg Prod.fst havg
    have hsumx : ∑ b, w b • (p b).2 = x := by
      simpa only [Prod.snd_sum, Prod.smul_def] using congrArg Prod.snd havg
    have hsumscore : ∑ b, w b * ℓ (z (a b)) = ℓ (z a₀) := by
      simpa only [map_sum, map_smul, smul_eq_mul, ha] using congrArg ℓ hsumz
    have hupper : ∀ b, ℓ (z (a b)) ≤ ℓ (z a₀) := by
      intro b
      by_cases hb : a b = a₀
      · simp [hb]
      · exact le_of_lt (hexpose (a b) hb)
    have hzero : ∀ b, a b ≠ a₀ → w b = 0 := by
      intro b hb
      exact weight_eq_zero_of_average_eq_upper w (fun c => ℓ (z (a c)))
        (ℓ (z a₀)) hw hs hupper hsumscore b (hexpose (a b) hb)
    obtain ⟨x₀, hx₀⟩ := hne
    let q : β → E := fun b => if a b = a₀ then (p b).2 else x₀
    have hq : ∀ b, q b ∈ K a₀ := by
      intro b
      dsimp [q]
      split_ifs with hb
      · simpa only [hb] using hk b
      · exact hx₀
    have heq : ∑ b, w b • q b = x := by
      rw [← hsumx]
      apply Finset.sum_congr rfl
      intro b hb
      by_cases ha₀ : a b = a₀
      · simp [q, ha₀]
      · simp [q, ha₀, hzero b ha₀]
    rw [← heq]
    exact hK.sum_mem (fun b _ => hw b) hs (fun b _ => hq b)
  · intro hx
    exact subset_convexHull ℝ _ ⟨a₀, rfl, hx⟩

/-- An ambient integer-coordinate linear functional. -/
def coordinateFunctional (b : ι → ℝ) : (ι → ℝ) →ₗ[ℝ] ℝ where
  toFun x := ∑ i, b i * x i
  map_add' x y := by simp [mul_add, Finset.sum_add_distrib]
  map_smul' c x := by
    simp [Finset.mul_sum, mul_left_comm]

noncomputable def cubeExposingCoefficients (I : Finset ι) (i : ι) : ℝ :=
  if i ∈ I then 1 else -(1 / 2)

omit [Fintype ι] in
theorem cube_exposing_term_le (I J : Finset ι) (i : ι) :
    cubeExposingCoefficients I i * cubeVector J i ≤ cubeVector I i := by
  by_cases hi : i ∈ I <;> by_cases hj : i ∈ J <;>
    norm_num [cubeExposingCoefficients, cubeVector, hi, hj]

theorem cube_exposing_value_self (I : Finset ι) :
    coordinateFunctional (cubeExposingCoefficients I) (cubeVector I) = I.card := by
  change ∑ i, cubeExposingCoefficients I i * cubeVector I i = _
  have hterm : ∀ i, cubeExposingCoefficients I i * cubeVector I i =
      (if i ∈ I then (1 : ℝ) else 0) := by
    intro i
    by_cases hi : i ∈ I <;> simp [cubeExposingCoefficients, cubeVector, hi]
  simp_rw [hterm]
  simp

/-- The specified normal strictly separates a cube vertex from every
other cube vertex, in every finite integer dimension. -/
theorem cube_exposing_value_other (I J : Finset ι) (hJI : J ≠ I) :
    coordinateFunctional (cubeExposingCoefficients I) (cubeVector J) <
      coordinateFunctional (cubeExposingCoefficients I) (cubeVector I) := by
  rw [cube_exposing_value_self]
  change (∑ i, cubeExposingCoefficients I i * cubeVector J i) < (I.card : ℝ)
  have hself : ∑ i, cubeVector I i = (I.card : ℝ) := by simp [cubeVector]
  rw [← hself]
  apply Finset.sum_lt_sum
  · intro i hi
    exact cube_exposing_term_le I J i
  · have hex : ∃ i, ¬ (i ∈ I ↔ i ∈ J) := by
      by_contra! h
      apply hJI
      ext i
      exact (h i).symm
    obtain ⟨i, hi⟩ := hex
    refine ⟨i, Finset.mem_univ i, ?_⟩
    by_cases hiI : i ∈ I <;> by_cases hiJ : i ∈ J <;>
      norm_num [cubeExposingCoefficients, cubeVector, hiI, hiJ] at *

/-- At any negative unit vector the same normal has value at most 1/2. -/
theorem cube_exposing_value_negative (I : Finset ι) (j : ι) :
    coordinateFunctional (cubeExposingCoefficients I) (negativeUnit j) ≤ 1 / 2 := by
  change (∑ i, cubeExposingCoefficients I i * negativeUnit j i) ≤ _
  have heq : (∑ i, cubeExposingCoefficients I i * negativeUnit j i) =
      -cubeExposingCoefficients I j := by
    simp [negativeUnit]
  rw [heq]
  by_cases hj : j ∈ I <;> norm_num [cubeExposingCoefficients, hj]

/-- Every nonempty cube vertex is strictly exposed also against all the
attached negative unit vectors. -/
theorem nonempty_cube_exposes_negative (I : Finset ι) (hI : I.Nonempty) (j : ι) :
    coordinateFunctional (cubeExposingCoefficients I) (negativeUnit j) <
      coordinateFunctional (cubeExposingCoefficients I) (cubeVector I) := by
  rw [cube_exposing_value_self]
  have hcard : (1 : ℝ) ≤ I.card := by
    exact_mod_cast Finset.card_pos.mpr hI
  have hnegative := cube_exposing_value_negative I j
  linarith

/-- A nonnegative finite weighted sum in a nonempty convex set is its
total weight times a point of that set, also when the total weight is zero. -/
theorem weighted_sum_eq_total_smul_mem
    {β E : Type*} [AddCommGroup E] [Module ℝ E]
    (s : Finset β) (w : β → ℝ) (p : β → E) (K : Set E)
    (hK : Convex ℝ K) (hne : K.Nonempty)
    (hw : ∀ b ∈ s, 0 ≤ w b) (hp : ∀ b ∈ s, p b ∈ K) :
    ∃ y ∈ K, (∑ b ∈ s, w b) • y = ∑ b ∈ s, w b • p b := by
  by_cases hz : ∑ b ∈ s, w b = 0
  · obtain ⟨y, hy⟩ := hne
    refine ⟨y, hy, ?_⟩
    have hzero : ∀ b ∈ s, w b = 0 := (Finset.sum_eq_zero_iff_of_nonneg hw).mp hz
    rw [hz, zero_smul]
    symm
    exact Finset.sum_eq_zero (fun b hb => by rw [hzero b hb, zero_smul])
  · have hpos : 0 < ∑ b ∈ s, w b :=
      lt_of_le_of_ne (Finset.sum_nonneg hw) (Ne.symm hz)
    refine ⟨s.centerMass w p, hK.centerMass_mem hw hpos hp, ?_⟩
    rw [Finset.centerMass, smul_smul, mul_inv_cancel₀ hz, one_smul]

/-- Convex hulls of finitely many nonempty convex sets admit one selected
point per set. This proves the aggregation step needed for actual fibers,
rather than assuming a finite convex combination with one point per fiber. -/
theorem mem_convexHull_finite_convex_family
    {E : Type*} [AddCommGroup E] [Module ℝ E]
    (K : α → Set E) (hK : ∀ a, Convex ℝ (K a))
    (hne : ∀ a, (K a).Nonempty) (x : E)
    (hx : x ∈ convexHull ℝ {p | ∃ a, p ∈ K a}) :
    ∃ (W : α → ℝ) (y : α → E), (∀ a, 0 ≤ W a) ∧
      (∑ a, W a = 1) ∧ (∀ a, y a ∈ K a) ∧ (∑ a, W a • y a = x) := by
  classical
  obtain ⟨β, _, w, p, hw, hs, hp, havg⟩ := mem_convexHull_iff_exists_fintype.mp hx
  choose a ha using hp
  have hgroups : ∀ c : α, ∃ y ∈ K c,
      (∑ b ∈ Finset.univ.filter (fun b => a b = c), w b) • y =
        ∑ b ∈ Finset.univ.filter (fun b => a b = c), w b • p b := by
    intro c
    apply weighted_sum_eq_total_smul_mem _ w p (K c) (hK c) (hne c)
    · exact fun b _ => hw b
    · intro b hb
      have hab : a b = c := (Finset.mem_filter.mp hb).2
      simpa only [hab] using ha b
  choose y hy heq using hgroups
  refine ⟨fun c => ∑ b ∈ Finset.univ.filter (fun b => a b = c), w b,
    y, ?_, ?_, hy, ?_⟩
  · intro c
    exact Finset.sum_nonneg (fun b _ => hw b)
  · dsimp only
    rw [Finset.sum_fiberwise Finset.univ a w]
    exact hs
  · simp_rw [heq]
    rw [Finset.sum_fiberwise Finset.univ a (fun b => w b • p b)]
    exact havg

/-- Grouped convex combinations for the convex hull of convex fibers. -/
theorem finite_convex_fiber_representation
    {Z E : Type*} [AddCommGroup Z] [Module ℝ Z]
    [AddCommGroup E] [Module ℝ E]
    (g : α → Z) (K : α → Set E)
    (hK : ∀ a, Convex ℝ (K a)) (hne : ∀ a, (K a).Nonempty)
    (z : Z) (x : E)
    (hx : (z, x) ∈ convexHull ℝ
      {p : Z × E | ∃ a, p.1 = g a ∧ p.2 ∈ K a}) :
    ∃ (W : α → ℝ) (y : α → E), (∀ a, 0 ≤ W a) ∧
      (∑ a, W a = 1) ∧ (∀ a, y a ∈ K a) ∧
      (∑ a, W a • g a = z) ∧ (∑ a, W a • y a = x) := by
  let D : α → Set (Z × E) := fun a => {p | p.1 = g a ∧ p.2 ∈ K a}
  have hD : ∀ a, Convex ℝ (D a) := by
    intro a
    exact (convex_singleton (g a)).prod (hK a)
  have hDne : ∀ a, (D a).Nonempty := by
    intro a
    obtain ⟨y, hy⟩ := hne a
    exact ⟨(g a, y), rfl, hy⟩
  obtain ⟨W, p, hW, hsum, hp, havg⟩ :=
    mem_convexHull_finite_convex_family D hD hDne (z, x) hx
  refine ⟨W, fun a => (p a).2, hW, hsum, fun a => (hp a).2, ?_, ?_⟩
  · have hbase : ∀ a, (p a).1 = g a := fun a => (hp a).1
    simpa only [Prod.fst_sum, Prod.smul_def, hbase] using congrArg Prod.fst havg
  · simpa only [Prod.snd_sum, Prod.smul_def] using congrArg Prod.snd havg

def subsetProjectionGenerator (a : Sum (Finset ι) ι) : ι → ℝ :=
  match a with
  | .inl I => cubeVector I
  | .inr i => negativeUnit i

/-- Exact origin fiber of the actual convex hull. All geometric assumptions
are explicit: convex nonempty component fibers and the grouped containment
`K_I + sum A_i ⊆ (|I|+1) B`. No convex-representation assumption is left. -/
theorem origin_fiber_convexHull_exact
    {E : Type*} [AddCommGroup E] [Module ℝ E]
    (B : Set E) (K : Finset ι → Set E) (A : ι → Set E)
    (hB : Convex ℝ B)
    (hK : ∀ I, Convex ℝ (K I)) (hKne : ∀ I, (K I).Nonempty)
    (hA : ∀ i, Convex ℝ (A i)) (hAne : ∀ i, (A i).Nonempty)
    (hempty : K ∅ = B)
    (hgroup : ∀ I, ∀ x ∈ K I, ∀ u : ι → E, (∀ i, u i ∈ A i) →
      ∃ y ∈ B, x + ∑ i ∈ I, u i = ((I.card : ℝ) + 1) • y) :
    {x | ((0 : ι → ℝ), x) ∈ convexHull ℝ
      {p : (ι → ℝ) × E | ∃ a : Sum (Finset ι) ι,
        p.1 = subsetProjectionGenerator a ∧ p.2 ∈ Sum.elim K A a}} = B := by
  classical
  ext x
  constructor
  · intro hx
    have hconv : ∀ a : Sum (Finset ι) ι, Convex ℝ (Sum.elim K A a) := by
      intro a
      cases a with
      | inl I => exact hK I
      | inr i => exact hA i
    have hnonempty : ∀ a : Sum (Finset ι) ι, (Sum.elim K A a).Nonempty := by
      intro a
      cases a with
      | inl I => exact hKne I
      | inr i => exact hAne i
    obtain ⟨W, y, hW, hs, hy, hz, hxy⟩ := finite_convex_fiber_representation
      subsetProjectionGenerator (Sum.elim K A) hconv hnonempty 0 x hx
    have hbalance : ∀ i, W (.inr i) =
        ∑ I, if i ∈ I then W (.inl I) else 0 := by
      apply zero_coordinate_weight_balance (fun I => W (.inl I)) (fun i => W (.inr i))
      intro i
      have hi := congrFun hz i
      simpa only [Fintype.sum_sum_type, Finset.sum_apply, Pi.smul_apply,
        Pi.add_apply, Pi.zero_apply, smul_eq_mul, subsetProjectionGenerator] using hi
    have htotal : (∑ I, W (.inl I)) + (∑ i, W (.inr i)) = 1 := by
      simpa only [Fintype.sum_sum_type] using hs
    have hcont : (∑ I, W (.inl I) • y (.inl I)) +
        (∑ i, W (.inr i) • y (.inr i)) = x := by
      simpa only [Fintype.sum_sum_type] using hxy
    rw [← hcont]
    apply origin_continuous_mem_of_grouped_containments B hB
      (fun I => W (.inl I)) (fun i => W (.inr i))
      (fun I => y (.inl I)) (fun i => y (.inr i))
      (fun I => hW (.inl I)) hbalance htotal
    intro I
    exact hgroup I (y (.inl I)) (hy (.inl I))
      (fun i => y (.inr i)) (fun i => hy (.inr i))
  · intro hx
    apply subset_convexHull ℝ _
    refine ⟨.inl ∅, ?_, ?_⟩
    · funext i
      simp [subsetProjectionGenerator, cubeVector]
    · simpa only [Sum.elim_inl, hempty] using hx

theorem subsetProjectionGenerator_range :
    Set.range (subsetProjectionGenerator (ι := ι)) = Set.range projectionGenerator := by
  classical
  ext x
  constructor
  · rintro ⟨a, rfl⟩
    cases a with
    | inl I =>
      refine ⟨.inl (fun i => decide (i ∈ I)), ?_⟩
      funext i
      by_cases hi : i ∈ I <;>
        simp [projectionGenerator, subsetProjectionGenerator, cubeVector, hi]
    | inr i => exact ⟨.inr i, rfl⟩
  · rintro ⟨a, rfl⟩
    cases a with
    | inl v =>
      refine ⟨.inl (Finset.univ.filter (fun i => v i = true)), ?_⟩
      funext i
      cases hi : v i <;>
        simp [projectionGenerator, subsetProjectionGenerator, cubeVector, hi]
    | inr i => exact ⟨.inr i, rfl⟩

theorem integer_mem_subset_projection_convexHull_iff (z : ι → ℤ) :
    (fun i => (z i : ℝ)) ∈
        convexHull ℝ (Set.range (subsetProjectionGenerator (ι := ι))) ↔
    (∀ i, z i = 0 ∨ z i = 1) ∨
    (∃ j, ∀ i, (z i : ℝ) = negativeUnit j i) := by
  rw [subsetProjectionGenerator_range]
  exact integer_mem_projection_convexHull_iff z

theorem nonempty_cube_exposes_generator (I : Finset ι) (hI : I.Nonempty)
    (a : Sum (Finset ι) ι) (ha : a ≠ .inl I) :
    coordinateFunctional (cubeExposingCoefficients I) (subsetProjectionGenerator a) <
      coordinateFunctional (cubeExposingCoefficients I) (cubeVector I) := by
  cases a with
  | inl J =>
    apply cube_exposing_value_other I J
    intro hJI
    exact ha (congrArg Sum.inl hJI)
  | inr i => exact nonempty_cube_exposes_negative I hI i

theorem negative_unit_functional_apply (i : ι) (x : ι → ℝ) :
    coordinateFunctional (negativeUnit i) x = -x i := by
  change (∑ j, negativeUnit i j * x j) = -x i
  simp [negativeUnit, ite_mul]

theorem negative_unit_exposes_generator (i : ι)
    (a : Sum (Finset ι) ι) (ha : a ≠ .inr i) :
    coordinateFunctional (negativeUnit i) (subsetProjectionGenerator a) <
      coordinateFunctional (negativeUnit i) (negativeUnit i) := by
  simp only [negative_unit_functional_apply]
  cases a with
  | inl I =>
    by_cases hi : i ∈ I <;>
      norm_num [subsetProjectionGenerator, cubeVector, negativeUnit, hi]
  | inr j =>
    have hij : i ≠ j := by
      intro hij
      exact ha (congrArg Sum.inr hij.symm)
    simp [subsetProjectionGenerator, negativeUnit, hij]

/-- Actual nonzero cube fibers stay exact after convexification. -/
theorem nonempty_cube_fiber_convexHull_exact
    {E : Type*} [AddCommGroup E] [Module ℝ E]
    (K : Sum (Finset ι) ι → Set E) (I : Finset ι) (hI : I.Nonempty)
    (hK : Convex ℝ (K (.inl I))) (hne : (K (.inl I)).Nonempty) :
    {x | (cubeVector I, x) ∈ convexHull ℝ
      {p : (ι → ℝ) × E | ∃ a : Sum (Finset ι) ι,
        p.1 = subsetProjectionGenerator a ∧ p.2 ∈ K a}} = K (.inl I) := by
  apply exposed_fiber_convexHull subsetProjectionGenerator K (.inl I) hK hne
    (coordinateFunctional (cubeExposingCoefficients I))
  exact nonempty_cube_exposes_generator I hI

/-- Actual negative unit fibers stay exact after convexification. -/
theorem negative_unit_fiber_convexHull_exact
    {E : Type*} [AddCommGroup E] [Module ℝ E]
    (K : Sum (Finset ι) ι → Set E) (i : ι)
    (hK : Convex ℝ (K (.inr i))) (hne : (K (.inr i)).Nonempty) :
    {x | (negativeUnit i, x) ∈ convexHull ℝ
      {p : (ι → ℝ) × E | ∃ a : Sum (Finset ι) ι,
        p.1 = subsetProjectionGenerator a ∧ p.2 ∈ K a}} = K (.inr i) := by
  apply exposed_fiber_convexHull subsetProjectionGenerator K (.inr i) hK hne
    (coordinateFunctional (negativeUnit i))
  exact negative_unit_exposes_generator i

/-- Projection of the actual fiber hull is exactly the hull of its bases.
Only nonemptiness of the component fibers is required. -/
theorem projection_of_fiber_convexHull
    {Z E : Type*} [AddCommGroup Z] [Module ℝ Z]
    [AddCommGroup E] [Module ℝ E]
    (g : α → Z) (K : α → Set E) (hne : ∀ a, (K a).Nonempty) :
    Prod.fst '' convexHull ℝ {p : Z × E | ∃ a, p.1 = g a ∧ p.2 ∈ K a} =
      convexHull ℝ (Set.range g) := by
  change (LinearMap.fst ℝ Z E) '' convexHull ℝ
    {p : Z × E | ∃ a, p.1 = g a ∧ p.2 ∈ K a} = _
  rw [LinearMap.image_convexHull]
  congr 1
  ext z
  constructor
  · rintro ⟨p, ⟨a, hp, hmem⟩, rfl⟩
    exact ⟨a, hp.symm⟩
  · rintro ⟨a, rfl⟩
    obtain ⟨x, hx⟩ := hne a
    exact ⟨(g a, x), ⟨a, rfl, hx⟩, rfl⟩

end SharpOC
