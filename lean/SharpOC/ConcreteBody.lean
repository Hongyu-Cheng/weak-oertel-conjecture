import SharpOC.BodyGeometry
import SharpOC.FamilyCombinatorics
import SharpOC.SourceContainment

/-! The actual counterexample body, its integer bases, and its exact fibers. -/

noncomputable section
open Set Finset

namespace SharpOC.Counterexample

open SharpOC.MiddleSimplex SharpOC.SourceContainment

def coreFiber (S : Finset IntegerCoordinate) : Set E :=
  if S = ∅ then B else K (selectedType S) S.card

def fiber : FiberIndex → Set E := Sum.elim coreFiber (fun _ => A)

def base : FiberIndex → IntegerCoordinate → ℝ := subsetProjectionGenerator

def body : Set ((IntegerCoordinate → ℝ) × E) :=
  convexHull ℝ {p | ∃ a : FiberIndex, p.1 = base a ∧ p.2 ∈ fiber a}

def integerBase (a : FiberIndex) (i : IntegerCoordinate) : ℤ :=
  match a with
  | .inl S => if i ∈ S then 1 else 0
  | .inr j => if i = j then -1 else 0

@[simp] theorem coreFiber_empty : coreFiber ∅ = B := by simp [coreFiber]

theorem coreFiber_of_nonempty (S : Finset IntegerCoordinate) (hS : S.Nonempty) :
    coreFiber S = K (selectedType S) S.card := by
  simp [coreFiber, hS.ne_empty]

@[simp] theorem fiber_inl (S : Finset IntegerCoordinate) : fiber (.inl S) = coreFiber S := rfl
@[simp] theorem fiber_inr (i : IntegerCoordinate) : fiber (.inr i) = A := rfl
@[simp] theorem base_inl (S : Finset IntegerCoordinate) : base (.inl S) = cubeVector S := rfl
@[simp] theorem base_inr (i : IntegerCoordinate) : base (.inr i) = negativeUnit i := rfl
@[simp] theorem base_empty : base (.inl ∅) = 0 := by ext i; simp [base, subsetProjectionGenerator, cubeVector]

theorem integerBase_cast (a : FiberIndex) :
    (fun i => (integerBase a i : ℝ)) = base a := by
  ext i
  cases a with
  | inl S => by_cases hi : i ∈ S <;> simp [integerBase, base, subsetProjectionGenerator, cubeVector, hi]
  | inr j => by_cases hi : i = j <;> simp [integerBase, base, subsetProjectionGenerator, negativeUnit, hi]

theorem base_injective : Function.Injective base := subsetProjectionGenerator_injective

theorem integerBase_injective : Function.Injective integerBase := by
  intro a b hab
  apply base_injective
  rw [← integerBase_cast a, ← integerBase_cast b, hab]

def coreMap (a : Fin 3) (k : ℕ) : E →ᵃ[ℝ] E where
  toFun p := (2 : ℝ) • p + ((k : ℝ) - 1) • center a
  linear := (2 : ℝ) • LinearMap.id
  map_vadd' p v := by
    ext i
    simp [smul_add]
    ring

theorem K_convex (a : Fin 3) (k : ℕ) : Convex ℝ (K a k) :=
  (P_convex a).affine_image (coreMap a k)

theorem K_nonempty (a : Fin 3) (k : ℕ) : (K a k).Nonempty :=
  ⟨(2 : ℝ) • center a + ((k : ℝ) - 1) • center a,
    center a, center_mem_P a, rfl⟩

theorem coreFiber_convex (S : Finset IntegerCoordinate) : Convex ℝ (coreFiber S) := by
  unfold coreFiber
  split_ifs
  · exact B_convex
  · exact K_convex _ _

theorem coreFiber_compact (S : Finset IntegerCoordinate) : IsCompact (coreFiber S) := by
  unfold coreFiber
  split_ifs
  · exact B_compact
  · exact K_compact _ _

theorem coreFiber_nonempty (S : Finset IntegerCoordinate) : (coreFiber S).Nonempty := by
  unfold coreFiber
  split_ifs
  · exact ⟨0, interior_subset zero_mem_interior_B⟩
  · exact K_nonempty _ _

theorem fiber_convex (a : FiberIndex) : Convex ℝ (fiber a) := by
  cases a with
  | inl S => exact coreFiber_convex S
  | inr i => exact A_convex

theorem fiber_compact (a : FiberIndex) : IsCompact (fiber a) := by
  cases a with
  | inl S => exact coreFiber_compact S
  | inr i => exact A_compact

theorem fiber_nonempty (a : FiberIndex) : (fiber a).Nonempty := by
  cases a with
  | inl S => exact coreFiber_nonempty S
  | inr i => exact ⟨0, zero_mem_A⟩

/-- Every actual finite outer-fiber sum satisfies the required grouped
containment; the averaging step is checked, including the empty subset. -/
theorem grouped_containment (S : Finset IntegerCoordinate) (q : E) (hq : q ∈ coreFiber S)
    (u : IntegerCoordinate → E) (hu : ∀ i, u i ∈ A) :
    ∃ b ∈ B, q + ∑ i ∈ S, u i = ((S.card : ℝ) + 1) • b := by
  by_cases hS : S = ∅
  · subst S
    refine ⟨q, ?_, ?_⟩
    · simpa using hq
    · simp
  · have hSne : S.Nonempty := Finset.nonempty_iff_ne_empty.mpr hS
    obtain ⟨avg, havg, heq⟩ := weighted_sum_eq_total_smul_mem S (fun _ => (1 : ℝ)) u A
      A_convex ⟨0, zero_mem_A⟩ (fun _ _ => by norm_num) (fun i _ => hu i)
    have hsum : (S.card : ℝ) • avg = ∑ i ∈ S, u i := by simpa using heq
    rw [coreFiber_of_nonempty S hSne] at hq
    obtain ⟨b, hb, hqb⟩ := K_add_scaled_A (selectedType S)
      (Finset.card_pos.mpr hSne) hq havg
    exact ⟨b, hb, by simpa only [hsum] using hqb⟩

theorem origin_fiber_exact : {x | ((0 : IntegerCoordinate → ℝ), x) ∈ body} = B := by
  exact origin_fiber_convexHull_exact B coreFiber (fun _ => A) B_convex
    coreFiber_convex coreFiber_nonempty (fun _ => A_convex) (fun _ => ⟨0, zero_mem_A⟩)
    coreFiber_empty grouped_containment

/-- Complete exact-fiber assertion at every indexed base. -/
theorem fiber_exact (a : FiberIndex) : {x | (base a, x) ∈ body} = fiber a := by
  cases a with
  | inl S =>
    by_cases hS : S = ∅
    · subst S
      simpa only [base_empty, fiber_inl, coreFiber_empty] using origin_fiber_exact
    · exact nonempty_cube_fiber_convexHull_exact fiber S
        (Finset.nonempty_iff_ne_empty.mpr hS) (fiber_convex (.inl S)) (fiber_nonempty (.inl S))
  | inr i =>
    exact negative_unit_fiber_convexHull_exact fiber i
      (fiber_convex (.inr i)) (fiber_nonempty (.inr i))

theorem integer_fiber_exact (a : FiberIndex) :
    {x | ((fun i => (integerBase a i : ℝ)), x) ∈ body} = fiber a := by
  rw [integerBase_cast]
  exact fiber_exact a

theorem projection_exact : Prod.fst '' body = convexHull ℝ (Set.range base) :=
  projection_of_fiber_convexHull base fiber fiber_nonempty

theorem integer_base_census (z : IntegerCoordinate → ℤ) (x : E)
    (hx : ((fun i => (z i : ℝ)), x) ∈ body) : ∃ a, integerBase a = z := by
  have hp : (fun i => (z i : ℝ)) ∈ convexHull ℝ (Set.range base) := by
    rw [← projection_exact]
    exact ⟨((fun i => (z i : ℝ)), x), hx, rfl⟩
  obtain hz | ⟨j, hj⟩ := (integer_mem_subset_projection_convexHull_iff z).mp hp
  · refine ⟨.inl (Finset.univ.filter (fun i => z i = 1)), ?_⟩
    funext i
    rcases hz i with hi | hi <;> simp [integerBase, hi]
  · refine ⟨.inr j, ?_⟩
    have heq : (fun i => (integerBase (.inr j) i : ℝ)) = fun i => (z i : ℝ) := by
      rw [integerBase_cast]
      funext i
      exact (hj i).symm
    funext i
    exact_mod_cast congrFun heq i

/-- No extra integer fibers arise in the actual body. -/
theorem integer_point_mem_body_iff (z : IntegerCoordinate → ℤ) (x : E) :
    ((fun i => (z i : ℝ)), x) ∈ body ↔
      ∃ a : FiberIndex, integerBase a = z ∧ x ∈ fiber a := by
  constructor
  · intro hx
    obtain ⟨a, ha⟩ := integer_base_census z x hx
    refine ⟨a, ha, ?_⟩
    rw [← ha] at hx
    change x ∈ {x | ((fun i => (integerBase a i : ℝ)), x) ∈ body} at hx
    rwa [integer_fiber_exact a] at hx
  · rintro ⟨a, rfl, hx⟩
    change x ∈ {x | ((fun i => (integerBase a i : ℝ)), x) ∈ body}
    rwa [integer_fiber_exact a]

theorem body_is_convex_body : IsCompact body ∧ Convex ℝ body ∧ (interior body).Nonempty := by
  apply fiber_construction_is_convex_body fiber fiber_convex fiber_nonempty fiber_compact
  simpa only [fiber_inl, coreFiber_empty] using
    (show (interior B).Nonempty from ⟨0, zero_mem_interior_B⟩)

theorem body_compact : IsCompact body := body_is_convex_body.1
theorem body_convex : Convex ℝ body := body_is_convex_body.2.1
theorem body_interior_nonempty : (interior body).Nonempty := body_is_convex_body.2.2

end SharpOC.Counterexample
