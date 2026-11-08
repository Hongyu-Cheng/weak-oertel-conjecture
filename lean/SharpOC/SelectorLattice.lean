import SharpOC.LatticeGeometry

/-!
# Integer projection of signed Boolean bases

Any subfamily of the two signed Boolean cubes has no additional nonzero
integer points in its convex hull. Each nonzero base is strictly exposed
against all the other signed Boolean bases.
-/

namespace SharpOC

variable {ι : Type*} [Fintype ι] [DecidableEq ι]

/-- The sign flag is true for the negative cube. -/
def signedCubeVector (negative : Bool) (I : Finset ι) : ι → ℝ :=
  if negative then -cubeVector I else cubeVector I

omit [Fintype ι] in
@[simp] theorem signedCubeVector_apply_eq_zero_iff (negative : Bool) (I : Finset ι) (i : ι) :
    signedCubeVector negative I i = 0 ↔ i ∉ I := by
  cases negative <;> by_cases hi : i ∈ I <;> norm_num [signedCubeVector, cubeVector, hi]

omit [Fintype ι] in
theorem signedCubeVector_support_eq {s t : Bool} {I J : Finset ι}
    (h : signedCubeVector s I = signedCubeVector t J) : I = J := by
  ext i
  have hz : signedCubeVector s I i = 0 ↔ signedCubeVector t J i = 0 := by rw [h]
  simpa only [signedCubeVector_apply_eq_zero_iff, not_iff_not] using hz

omit [Fintype ι] in
theorem signedCubeVector_injective {s t : Bool} {I J : Finset ι} (hI : I.Nonempty)
    (h : signedCubeVector s I = signedCubeVector t J) : s = t ∧ I = J := by
  have hIJ := signedCubeVector_support_eq h
  subst J
  refine ⟨?_, rfl⟩
  obtain ⟨i, hi⟩ := hI
  have he := congrFun h i
  cases s <;> cases t <;> norm_num [signedCubeVector, cubeVector, hi] at he <;> rfl

omit [Fintype ι] in
@[simp] theorem signedCubeVector_eq_zero_iff (negative : Bool) (I : Finset ι) :
    signedCubeVector negative I = 0 ↔ I = ∅ := by
  constructor
  · intro h
    exact Finset.eq_empty_iff_forall_notMem.mpr fun i =>
      (signedCubeVector_apply_eq_zero_iff negative I i).mp (congrFun h i)
  · rintro rfl
    funext i
    exact (signedCubeVector_apply_eq_zero_iff negative ∅ i).mpr (Finset.notMem_empty i)

private noncomputable def signedCubeCoefficients (I : Finset ι) (i : ι) : ℝ :=
  if i ∈ I then 1 else -(1 / ((Fintype.card ι : ℝ) + 1))

/-- The normal takes value `I.card` at the chosen site. -/
noncomputable def signedCubeExposingFunctional (negative : Bool) (I : Finset ι) :
    (ι → ℝ) →ₗ[ℝ] ℝ :=
  if negative then -coordinateFunctional (signedCubeCoefficients I)
  else coordinateFunctional (signedCubeCoefficients I)

private theorem positive_exposing_value_self (I : Finset ι) :
    coordinateFunctional (signedCubeCoefficients I) (cubeVector I) = I.card := by
  change (∑ i, signedCubeCoefficients I i * cubeVector I i) = _
  have hterm (i : ι) : signedCubeCoefficients I i * cubeVector I i = cubeVector I i := by
    by_cases hi : i ∈ I <;> simp [signedCubeCoefficients, cubeVector, hi]
  simp_rw [hterm]
  simp [cubeVector]

theorem signedCube_exposing_value_self (negative : Bool) (I : Finset ι) :
    signedCubeExposingFunctional negative I (signedCubeVector negative I) = I.card := by
  cases negative <;>
    simpa [signedCubeExposingFunctional, signedCubeVector] using positive_exposing_value_self I

private theorem positive_exposes_positive (I J : Finset ι) (hJI : J ≠ I) :
    coordinateFunctional (signedCubeCoefficients I) (cubeVector J) <
      coordinateFunctional (signedCubeCoefficients I) (cubeVector I) := by
  change (∑ i, signedCubeCoefficients I i * cubeVector J i) <
    (∑ i, signedCubeCoefficients I i * cubeVector I i)
  have hε : 0 < ((Fintype.card ι : ℝ) + 1)⁻¹ := by positivity
  apply Finset.sum_lt_sum
  · intro i _
    by_cases hiI : i ∈ I <;> by_cases hiJ : i ∈ J <;>
      norm_num [signedCubeCoefficients, cubeVector, hiI, hiJ] <;> linarith
  · have hex : ∃ i, ¬ (i ∈ I ↔ i ∈ J) := by
      by_contra! h
      apply hJI
      ext i
      exact (h i).symm
    obtain ⟨i, hi⟩ := hex
    refine ⟨i, Finset.mem_univ i, ?_⟩
    by_cases hiI : i ∈ I <;> by_cases hiJ : i ∈ J <;>
      simp [hiI, hiJ] at hi <;>
      norm_num [signedCubeCoefficients, cubeVector, hiI, hiJ] <;> linarith

private theorem positive_exposes_negative (I J : Finset ι) (hI : I.Nonempty) :
    coordinateFunctional (signedCubeCoefficients I) (-cubeVector J) <
      coordinateFunctional (signedCubeCoefficients I) (cubeVector I) := by
  rw [positive_exposing_value_self]
  change (∑ i, signedCubeCoefficients I i * (-cubeVector J i)) < (I.card : ℝ)
  have hε : 0 < ((Fintype.card ι : ℝ) + 1)⁻¹ := by positivity
  calc
    _ ≤ ∑ _ : ι, 1 / ((Fintype.card ι : ℝ) + 1) := by
      apply Finset.sum_le_sum
      intro i _
      by_cases hiI : i ∈ I <;> by_cases hiJ : i ∈ J <;>
        norm_num [signedCubeCoefficients, cubeVector, hiI, hiJ] <;> linarith
    _ < 1 := by
      simp only [Finset.sum_const, Finset.card_univ, nsmul_eq_mul, mul_one_div]
      exact (div_lt_one (by positivity)).2 (by linarith)
    _ ≤ _ := by exact_mod_cast Finset.card_pos.mpr hI

/-- A nonempty signed Boolean site is strictly exposed even when the two
signed cubes are both present. The empty site may have either sign. -/
theorem signedCube_exposes (negative : Bool) (I : Finset ι) (hI : I.Nonempty)
    (otherNegative : Bool) (J : Finset ι)
    (hne : signedCubeVector otherNegative J ≠ signedCubeVector negative I) :
    signedCubeExposingFunctional negative I (signedCubeVector otherNegative J) <
      signedCubeExposingFunctional negative I (signedCubeVector negative I) := by
  cases negative <;> cases otherNegative
  · have hJI : J ≠ I := fun h => hne (congrArg (signedCubeVector false) h)
    simpa [signedCubeExposingFunctional, signedCubeVector] using positive_exposes_positive I J hJI
  · simpa [signedCubeExposingFunctional, signedCubeVector] using positive_exposes_negative I J hI
  · simpa [signedCubeExposingFunctional, signedCubeVector] using positive_exposes_negative I J hI
  · have hJI : J ≠ I := fun h => hne (congrArg (signedCubeVector true) h)
    simpa [signedCubeExposingFunctional, signedCubeVector] using positive_exposes_positive I J hJI

omit [Fintype ι] in
private theorem signedCube_bounds (negative : Bool) (I : Finset ι) (i : ι) :
    -1 ≤ signedCubeVector negative I i ∧ signedCubeVector negative I i ≤ 1 := by
  cases negative <;> by_cases hi : i ∈ I <;> norm_num [signedCubeVector, cubeVector, hi]

omit [Fintype ι] in
private theorem signedCube_gap (negative : Bool) (I : Finset ι) (i j : ι) :
    signedCubeVector negative I i - signedCubeVector negative I j ≤ 1 := by
  cases negative <;> by_cases hi : i ∈ I <;> by_cases hj : j ∈ I <;>
    norm_num [signedCubeVector, cubeVector, hi, hj]

private theorem linear_le_of_mem_convexHull_range
    {α Z : Type*} [AddCommGroup Z] [Module ℝ Z]
    {g : α → Z} {x : Z} (hx : x ∈ convexHull ℝ (Set.range g))
    (ℓ : Z →ₗ[ℝ] ℝ) (b : ℝ) (hb : ∀ a, ℓ (g a) ≤ b) : ℓ x ≤ b :=
  convexHull_min (Set.range_subset_iff.mpr hb) (convex_halfSpace_le ℓ.isLinear b) hx

/-- Complete census of nonzero lattice sites for an arbitrary family
of signed Boolean bases, without an assumption on its origin fiber. -/
theorem integer_mem_signed_projection_convexHull_iff {α : Type*}
    (g : α → ι → ℝ) (hg : ∀ a, ∃ negative I, g a = signedCubeVector negative I)
    (z : ι → ℤ) (hz : z ≠ 0) :
    (fun i => (z i : ℝ)) ∈ convexHull ℝ (Set.range g) ↔
      (fun i => (z i : ℝ)) ∈ Set.range g := by
  classical
  refine ⟨fun hx => ?_, fun h => subset_convexHull ℝ _ h⟩
  have hcoord (i : ι) : (-1 : ℤ) ≤ z i ∧ z i ≤ 1 := by
    have hl := linear_le_of_mem_convexHull_range hx (-LinearMap.proj i) 1 (fun a => by
      obtain ⟨s, I, h⟩ := hg a
      rw [h]
      simpa using neg_le_neg (signedCube_bounds s I i).1)
    have hu := linear_le_of_mem_convexHull_range hx (LinearMap.proj i) 1 (fun a => by
      obtain ⟨s, I, h⟩ := hg a
      rw [h]
      exact (signedCube_bounds s I i).2)
    constructor
    · have h : -(z i : ℝ) ≤ 1 := hl
      exact_mod_cast (show (-1 : ℝ) ≤ z i by linarith)
    · have h : (z i : ℝ) ≤ 1 := hu
      exact_mod_cast h
  have hgap (i j : ι) : z i - z j ≤ 1 := by
    let ℓ := LinearMap.proj (R := ℝ) (φ := fun _ : ι => ℝ) i - LinearMap.proj j
    have hℓ (x : ι → ℝ) : ℓ x = x i - x j := by simp [ℓ]
    have h := linear_le_of_mem_convexHull_range hx ℓ 1 (fun a => by
      obtain ⟨s, I, h⟩ := hg a
      rw [hℓ, h]
      exact signedCube_gap s I i j)
    rw [hℓ] at h
    exact_mod_cast h
  let I := Finset.univ.filter (fun i => z i ≠ 0)
  have hI : I.Nonempty := by
    by_contra h
    apply hz
    funext i
    by_contra hi
    exact h ⟨i, by simpa [I] using hi⟩
  obtain ⟨negative, hsign⟩ : ∃ negative : Bool, ∀ i, z i ≠ 0 →
      z i = (if negative then -1 else 1) := by
    by_cases hneg : ∃ j, z j = -1
    · obtain ⟨j, hj⟩ := hneg
      refine ⟨true, fun i hi => ?_⟩
      change z i = -1
      have hb := hcoord i
      have hd := hgap i j
      omega
    · refine ⟨false, fun i hi => ?_⟩
      change z i = 1
      have hb := hcoord i
      have hn : z i ≠ -1 := fun h => hneg ⟨i, h⟩
      omega
  have heq : (fun i => (z i : ℝ)) = signedCubeVector negative I := by
    funext i
    by_cases hi : z i = 0
    · cases negative <;> simp [signedCubeVector, cubeVector, I, hi]
    · have hh := hsign i hi
      cases negative <;> norm_num at hh <;> simp [signedCubeVector, cubeVector, I, hh]
  rw [heq] at hx ⊢
  by_contra hmissing
  let ℓ := signedCubeExposingFunctional negative I
  have hstrict (a : α) : ℓ (g a) < ℓ (signedCubeVector negative I) := by
    obtain ⟨s, J, h⟩ := hg a
    rw [h]
    exact signedCube_exposes negative I hI s J fun he => hmissing ⟨a, h.trans he⟩
  have hlt : ℓ (signedCubeVector negative I) < ℓ (signedCubeVector negative I) :=
    convexHull_min (Set.range_subset_iff.mpr hstrict) (convex_halfSpace_lt ℓ.isLinear _) hx
  exact (lt_irrefl _) hlt

/-- The convex hull preserves the fiber at a nonzero signed Boolean base
that occurs at a unique family index. -/
theorem signedCube_fiber_convexHull_exact
    {α E : Type*} [Fintype α] [AddCommGroup E] [Module ℝ E]
    (g : α → ι → ℝ) (hg : ∀ a, ∃ negative I, g a = signedCubeVector negative I)
    (K : α → Set E) (a₀ : α) (negative : Bool) (I : Finset ι) (hI : I.Nonempty)
    (hbase : g a₀ = signedCubeVector negative I)
    (hunique : ∀ a, g a = g a₀ → a = a₀)
    (hK : Convex ℝ (K a₀)) (hne : (K a₀).Nonempty) :
    {x | (g a₀, x) ∈ convexHull ℝ {p : (ι → ℝ) × E | ∃ a, p.1 = g a ∧ p.2 ∈ K a}} =
      K a₀ := by
  apply exposed_fiber_convexHull g K a₀ hK hne (signedCubeExposingFunctional negative I)
  intro a ha
  obtain ⟨s, J, h⟩ := hg a
  rw [h, hbase]
  exact signedCube_exposes negative I hI s J fun he => ha (hunique a (h.trans (he.trans hbase.symm)))

end SharpOC
