import SharpOC.BoxFree
import SharpOC.BoxFamily
import SharpOC.BoxSources

/-! The actual 76-coordinate convex body and every one of its integer fibers. -/

noncomputable section
open Set Finset

namespace SharpOC.BoxCounterexample

open BoxParameters BoxGeometry

abbrev FreeSpace := Fin h → ℝ
abbrev E := BoxSources.E0 × FreeSpace
abbrev Ambient := IntegerSpace × E

def F : Set FreeSpace := box 1
def B : Set E := BoxSources.B0 ×ˢ F
def P (a : Fin 4) : Set E := BoxSources.P a ×ˢ box q
def A (a : Fin 4) : Set E := BoxSources.A a ×ˢ box u
def K (a : Fin 4) (k : ℕ) : Set E := BoxSources.K a k ×ˢ box (2 * q)

def coreFiber (S : Finset IntegerCoordinate) : Set E :=
  if S = ∅ then B else K (selectedType S) S.card

def fiber : FiberIndex → Set E := Sum.elim coreFiber (fun i => A i.1)
def base : FiberIndex → IntegerSpace := subsetProjectionGenerator

def body : Set Ambient :=
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
@[simp] theorem fiber_inr (i : IntegerCoordinate) : fiber (.inr i) = A i.1 := rfl
@[simp] theorem base_inl (S : Finset IntegerCoordinate) : base (.inl S) = cubeVector S := rfl
@[simp] theorem base_inr (i : IntegerCoordinate) : base (.inr i) = negativeUnit i := rfl
@[simp] theorem base_empty : base (.inl ∅) = 0 := by
  ext i
  simp [base, subsetProjectionGenerator, cubeVector]

theorem integerBase_cast (a : FiberIndex) :
    (fun i => (integerBase a i : ℝ)) = base a := by
  ext i
  cases a with
  | inl S =>
    by_cases hi : i ∈ S <;>
      simp [integerBase, base, subsetProjectionGenerator, cubeVector, hi]
  | inr j =>
    by_cases hi : i = j <;>
      simp [integerBase, base, subsetProjectionGenerator, negativeUnit, hi]

theorem base_injective : Function.Injective base := subsetProjectionGenerator_injective

theorem integerBase_injective : Function.Injective integerBase := by
  intro a b hab
  apply base_injective
  rw [← integerBase_cast a, ← integerBase_cast b, hab]

theorem B_compact : IsCompact B := BoxSources.B0_compact.prod (box_compact 1)
theorem B_convex : Convex ℝ B := BoxSources.B0_convex.prod (box_convex 1)

theorem zero_mem_interior_B : (0 : E) ∈ interior B := by
  rw [B, interior_prod_eq]
  exact ⟨BoxSources.zero_mem_interior_B0, zero_mem_interior_box (by norm_num)⟩

theorem B_nonempty : B.Nonempty := ⟨0, interior_subset zero_mem_interior_B⟩
theorem B_interior_nonempty : (interior B).Nonempty := ⟨0, zero_mem_interior_B⟩

theorem P_compact (a : Fin 4) : IsCompact (P a) :=
  (BoxSources.P_compact a).prod (box_compact q)
theorem P_convex (a : Fin 4) : Convex ℝ (P a) :=
  (BoxSources.P_convex a).prod (box_convex q)

theorem P_interior_nonempty (a : Fin 4) : (interior (P a)).Nonempty := by
  rw [P, interior_prod_eq]
  exact ⟨(BoxSources.center a, 0), BoxSources.center_mem_interior_P a,
    zero_mem_interior_box q_pos⟩

theorem A_compact (a : Fin 4) : IsCompact (A a) :=
  (BoxSources.A_compact a).prod (box_compact u)
theorem A_convex (a : Fin 4) : Convex ℝ (A a) :=
  (BoxSources.A_convex a).prod (box_convex u)

theorem zero_mem_interior_A (a : Fin 4) : (0 : E) ∈ interior (A a) := by
  rw [A, interior_prod_eq]
  exact ⟨BoxSources.zero_mem_interior_A a, zero_mem_interior_box u_pos⟩

theorem zero_mem_A (a : Fin 4) : (0 : E) ∈ A a :=
  interior_subset (zero_mem_interior_A a)
theorem A_nonempty (a : Fin 4) : (A a).Nonempty := ⟨0, zero_mem_A a⟩
theorem A_interior_nonempty (a : Fin 4) : (interior (A a)).Nonempty :=
  ⟨0, zero_mem_interior_A a⟩

theorem K_compact (a : Fin 4) (k : ℕ) : IsCompact (K a k) :=
  (BoxSources.K_compact a k).prod (box_compact (2*q))
theorem K_convex (a : Fin 4) (k : ℕ) : Convex ℝ (K a k) :=
  (BoxSources.K_convex a k).prod (box_convex (2*q))

theorem K_interior_nonempty (a : Fin 4) (k : ℕ) : (interior (K a k)).Nonempty := by
  rw [K, interior_prod_eq]
  exact (BoxSources.K_interior_nonempty a k).prod
    (box_interior_nonempty (mul_pos (by norm_num) q_pos))

theorem K_nonempty (a : Fin 4) (k : ℕ) : (K a k).Nonempty :=
  (K_interior_nonempty a k).mono interior_subset

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

theorem coreFiber_interior_nonempty (S : Finset IntegerCoordinate) :
    (interior (coreFiber S)).Nonempty := by
  unfold coreFiber
  split_ifs
  · exact B_interior_nonempty
  · exact K_interior_nonempty _ _

theorem coreFiber_nonempty (S : Finset IntegerCoordinate) : (coreFiber S).Nonempty :=
  (coreFiber_interior_nonempty S).mono interior_subset

theorem fiber_convex (a : FiberIndex) : Convex ℝ (fiber a) := by
  cases a with
  | inl S => exact coreFiber_convex S
  | inr i => exact A_convex i.1

theorem fiber_compact (a : FiberIndex) : IsCompact (fiber a) := by
  cases a with
  | inl S => exact coreFiber_compact S
  | inr i => exact A_compact i.1

theorem fiber_interior_nonempty (a : FiberIndex) : (interior (fiber a)).Nonempty := by
  cases a with
  | inl S => exact coreFiber_interior_nonempty S
  | inr i => exact A_interior_nonempty i.1

theorem fiber_nonempty (a : FiberIndex) : (fiber a).Nonempty :=
  (fiber_interior_nonempty a).mono interior_subset

theorem grouped_containment (S : Finset IntegerCoordinate) (x : E) (hx : x ∈ coreFiber S)
    (v : IntegerCoordinate → E) (hv : ∀ i, v i ∈ A i.1) :
    ∃ b ∈ B, x + ∑ i ∈ S, v i = ((S.card : ℝ) + 1) • b := by
  by_cases hS : S = ∅
  · subst S
    refine ⟨x, ?_, ?_⟩
    · simpa using hx
    · simp
  · have hSne : S.Nonempty := Finset.nonempty_iff_ne_empty.mpr hS
    rw [coreFiber_of_nonempty S hSne] at hx
    have hx0 : x.1 ∈ BoxSources.K (selectedType S) S.card := hx.1
    obtain ⟨b0, hb0, heq0⟩ := BoxSources.K_add_sum_A S hSne
      (selectedType S) (fun i : IntegerCoordinate => i.1) hx0 (fun i => (v i).1)
      (fun i _ => (hv i).1)
    obtain ⟨bF, hbF, heqF⟩ := box_grouped_containment S hSne half_lt_q.le hx.2
      (fun i => (v i).2) (fun i _ => (hv i).2)
    refine ⟨(b0, bF), ⟨hb0, hbF⟩, ?_⟩
    apply Prod.ext
    · simpa only [Prod.fst_add, Prod.fst_sum, Prod.smul_mk] using heq0
    · simpa only [Prod.snd_add, Prod.snd_sum, Prod.smul_mk] using heqF

theorem origin_fiber_exact : {x | ((0 : IntegerSpace), x) ∈ body} = B := by
  exact origin_fiber_convexHull_exact B coreFiber (fun i => A i.1) B_convex
    coreFiber_convex coreFiber_nonempty (fun i => A_convex i.1)
    (fun i => A_nonempty i.1) coreFiber_empty grouped_containment

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
  simpa only [fiber_inl, coreFiber_empty] using B_interior_nonempty

theorem body_compact : IsCompact body := body_is_convex_body.1
theorem body_convex : Convex ℝ body := body_is_convex_body.2.1
theorem body_interior_nonempty : (interior body).Nonempty := body_is_convex_body.2.2

theorem zero_mem_body : (0 : Ambient) ∈ body := by
  change (0 : E) ∈ {x | ((0 : IntegerSpace), x) ∈ body}
  rw [origin_fiber_exact]
  exact interior_subset zero_mem_interior_B

theorem fiber_affineSpan_eq_top (a : FiberIndex) : affineSpan ℝ (fiber a) = ⊤ :=
  (fiber_convex a).interior_nonempty_iff_affineSpan_eq_top.mp (fiber_interior_nonempty a)

theorem integer_dimension : Module.finrank ℝ IntegerSpace = 76 := by
  simp [IntegerSpace, IntegerCoordinate]

theorem base_continuous_dimension : Module.finrank ℝ E = 3 + h := by
  simp [E, FreeSpace, BoxSources.E0]

theorem base_ambient_dimension : Module.finrank ℝ Ambient = 76 + (3 + h) := by
  rw [Module.finrank_prod, integer_dimension, base_continuous_dimension]

end SharpOC.BoxCounterexample
