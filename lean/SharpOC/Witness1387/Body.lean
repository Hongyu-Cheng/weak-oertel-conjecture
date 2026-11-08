import SharpOC.LatticeGeometry
import SharpOC.Witness1387.Arithmetic
import SharpOC.Witness1387.Support
import SharpOC.Witness1387.Vertices

/-! Finite rational vertices for the separated-sentinel witness. -/

noncomputable section

namespace SharpOC.Witness1387

open Set

abbrev Ambient := (Coordinate → ℝ) × (Fin 1178 → ℝ)
abbrev RationalAmbient := (Coordinate → ℚ) × (Fin 1178 → ℚ)

/-- Active pools have sizes from 55 to 70. The endpoints also give a total
definition on inactive tuples, where this index is unused. -/
def poolIndex (b : Baseline) : Fin 16 :=
  ⟨min 15 (pool b 0 - 55), lt_of_le_of_lt (min_le_left _ _) (by decide)⟩

def sourceVertices : SupportIndex → Finset (Fin 1178 → ℚ)
  | .inl b =>
      if (activeAxis b).isSome then centerVertices (radius (poolIndex b))
      else if (zeroSlots b).card ≤ 1 then sectorVertices (label b) 1
      else inactiveVertices inactiveMass
  | .inr b =>
      sectorVertices (label b.val) (2 * radius (poolIndex (lightCenter b.val)) - 1)

def rationalLift (i : SupportIndex) (v : Fin 1178 → ℚ) : RationalAmbient :=
  (fun j => (integerBase i j : ℚ), v)

def castVertex (p : RationalAmbient) : Ambient :=
  (fun j => (p.1 j : ℝ), ratToReal p.2)

def rationalVertices : Set RationalAmbient :=
  ⋃ i : SupportIndex, rationalLift i '' (sourceVertices i : Set (Fin 1178 → ℚ))

theorem rationalVertices_finite : rationalVertices.Finite :=
  Set.finite_iUnion (fun i => (sourceVertices i).finite_toSet.image (rationalLift i))

def body : Set Ambient := convexHull ℝ (castVertex '' rationalVertices)

def source (i : SupportIndex) : Set (Fin 1178 → ℝ) :=
  convexHull ℝ (ratToReal '' (sourceVertices i : Set (Fin 1178 → ℚ)))

theorem ambient_dimension : Module.finrank ℝ Ambient = 1387 := by
  simp [Ambient, Coordinate, Block, Module.finrank_prod]

theorem body_compact : IsCompact body :=
  (rationalVertices_finite.image castVertex).isCompact_convexHull ℝ

theorem body_convex : Convex ℝ body := convex_convexHull ℝ _

theorem source_convex (i : SupportIndex) : Convex ℝ (source i) := convex_convexHull ℝ _

theorem source_compact (i : SupportIndex) : IsCompact (source i) :=
  ((sourceVertices i).finite_toSet.image ratToReal).isCompact_convexHull ℝ

@[simp] theorem cast_rationalLift (i : SupportIndex) (v : Fin 1178 → ℚ) :
    castVertex (rationalLift i v) = (base i, ratToReal v) := by
  apply Prod.ext
  · funext j
    simp [castVertex, rationalLift, base]
  · rfl

theorem lifted_vertex_mem (i : SupportIndex) {v : Fin 1178 → ℚ}
    (hv : v ∈ sourceVertices i) :
    (base i, ratToReal v) ∈ castVertex '' rationalVertices := by
  exact ⟨rationalLift i v, mem_iUnion.mpr ⟨i, ⟨v, hv, rfl⟩⟩, cast_rationalLift i v⟩

/-- Taking each source hull before lifting does not change the rational
polytope. The inclusion from a prescribed source is unconditional. -/
theorem prescribed_source_mem (i : SupportIndex) {x : Fin 1178 → ℝ}
    (hx : x ∈ source i) : (base i, x) ∈ body := by
  have hconv : Convex ℝ {y : Fin 1178 → ℝ | (base i, y) ∈ body} := by
    intro x₁ hx₁ x₂ hx₂ a b ha hb hab
    change (base i, a • x₁ + b • x₂) ∈ body
    have heq : a • (base i, x₁) + b • (base i, x₂) =
        (base i, a • x₁ + b • x₂) := by
      apply Prod.ext
      · change a • base i + b • base i = base i
        rw [← add_smul, hab, one_smul]
      · rfl
    rw [← heq]
    exact body_convex hx₁ hx₂ ha hb hab
  apply convexHull_min ?_ hconv hx
  rintro _ ⟨v, hv, rfl⟩
  exact subset_convexHull ℝ _ (lifted_vertex_mem i hv)

theorem body_eq_source_hull :
    body = convexHull ℝ {p : Ambient | ∃ i, p.1 = base i ∧ p.2 ∈ source i} := by
  classical
  apply le_antisymm
  · apply convexHull_min _ (convex_convexHull ℝ _)
    rintro _ ⟨q, hq, rfl⟩
    obtain ⟨i, v, hv, rfl⟩ := mem_iUnion.mp hq
    rw [cast_rationalLift]
    exact subset_convexHull ℝ _ ⟨i, rfl, subset_convexHull ℝ _ ⟨v, hv, rfl⟩⟩
  · apply convexHull_min _ body_convex
    rintro ⟨_, x⟩ ⟨i, rfl, hx⟩
    exact prescribed_source_mem i hx

theorem body_projection (hne : ∀ i, (source i).Nonempty) :
    Prod.fst '' body = convexHull ℝ (range base) := by
  rw [body_eq_source_hull]
  exact projection_of_fiber_convexHull base source hne

theorem source_eq_at_exposed_base (i : SupportIndex) (hne : (source i).Nonempty)
    (f : (Coordinate → ℝ) →ₗ[ℝ] ℝ)
    (hexpose : ∀ j, j ≠ i → f (base j) < f (base i)) :
    {x | (base i, x) ∈ body} = source i := by
  rw [body_eq_source_hull]
  exact exposed_fiber_convexHull base source i (source_convex i) hne f hexpose

end SharpOC.Witness1387
