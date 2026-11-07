import SharpOC.BoxPadding
import SharpOC.BoxFree
import SharpOC.BoxParameters
import SharpOC.BoxCuts
import SharpOC.BoxArithmetic

/-! Actual Lebesgue product volumes and counting-times-Lebesgue mass for
 the barycentric-box construction and its common simplex padding. -/

noncomputable section
open Set Finset MeasureTheory
open scoped ENNReal

namespace SharpOC.BoxGeometry

variable {ι : Type*} [Fintype ι]

theorem box_volume (r : ℝ) :
    volume (box (ι := ι) r) = ENNReal.ofReal (2 * r) ^ Fintype.card ι := by
  rw [box_eq_Icc, Real.volume_Icc_pi]
  simp [sub_neg_eq_add, ← two_mul]

theorem box_volume_toReal {r : ℝ} (hr : 0 ≤ r) :
    (volume (box (ι := ι) r)).toReal = (2 * r) ^ Fintype.card ι := by
  rw [box_volume, ENNReal.toReal_pow, ENNReal.toReal_ofReal (by positivity)]

end SharpOC.BoxGeometry

namespace SharpOC.BoxPadding

variable {I E : Type*} [MeasureSpace E]

/-- Counting measure on all integer coordinates times the actual Lebesgue
measure of each continuous fiber. There is no replacement by a convex hull. -/
def integerMass (C : Set ((I → ℝ) × E)) : ℝ≥0∞ :=
  ∑' z : I → ℤ, volume {x | ((fun i => (z i : ℝ)), x) ∈ C}

theorem integerMass_eq_sum {ι : Type*} [Fintype ι]
    (D : Set ((I → ℝ) × E)) (integerBase : ι → I → ℤ)
    (hinj : Function.Injective integerBase)
    (hcensus : ∀ (z : I → ℤ) (x : E), ((fun i => (z i : ℝ)), x) ∈ D →
      ∃ a, integerBase a = z) :
    integerMass D =
      ∑ a : ι, volume {x | ((fun i => (integerBase a i : ℝ)), x) ∈ D} := by
  classical
  let s : Finset (I → ℤ) := Finset.univ.image integerBase
  have hzero : ∀ z ∉ s, volume {x | ((fun i => (z i : ℝ)), x) ∈ D} = 0 := by
    intro z hz
    have hempty : {x | ((fun i => (z i : ℝ)), x) ∈ D} = ∅ := by
      apply Set.eq_empty_iff_forall_notMem.mpr
      intro x hx
      obtain ⟨a, ha⟩ := hcensus z x hx
      apply hz
      exact Finset.mem_image.mpr ⟨a, Finset.mem_univ a, ha⟩
    rw [hempty, measure_empty]
  unfold integerMass
  rw [tsum_eq_sum hzero]
  dsimp [s]
  exact Finset.sum_image (fun a _ b _ hab => hinj hab)

section ProductMass

variable [Fintype I] [NormedAddCommGroup E] [NormedSpace ℝ E]
  {V : Type*} [NormedAddCommGroup V] [NormedSpace ℝ V]
  [MeasureSpace V] [SFinite (volume : Measure V)]

theorem integerMass_padded (C : Set ((I → ℝ) × E)) (J : Set V) :
    integerMass (padded C J) = integerMass C * volume J := by
  unfold integerMass
  simp_rw [padded_fiber]
  change (∑' z : I → ℤ, (volume.prod volume)
    ({x | ((fun i => (z i : ℝ)), x) ∈ C} ×ˢ J)) = _
  simp_rw [Measure.prod_prod]
  exact ENNReal.tsum_mul_right

theorem padded_cut_eq (C : Set ((I → ℝ) × E)) (J : Set V)
    (F : ((I → ℝ) × E) →L[ℝ] ℝ) (t : ℝ) :
    padded C J ∩ {p | t ≤ extendCut F p} = padded (C ∩ {p | t ≤ F p}) J := by
  ext p
  change ((p.1, p.2.1) ∈ C ∧ p.2.2 ∈ J) ∧ t ≤ F (p.1, p.2.1) ↔
    ((p.1, p.2.1) ∈ C ∧ t ≤ F (p.1, p.2.1)) ∧ p.2.2 ∈ J
  tauto

theorem integerMass_padded_cut (C : Set ((I → ℝ) × E)) (J : Set V)
    (F : ((I → ℝ) × E) →L[ℝ] ℝ) (t : ℝ) :
    integerMass (padded C J ∩ {p | t ≤ extendCut F p}) =
      integerMass (C ∩ {p | t ≤ F p}) * volume J := by
  rw [padded_cut_eq, integerMass_padded]

end ProductMass

theorem volume_prod_toReal {U W : Type*} [MeasureSpace U] [MeasureSpace W]
    [SFinite (volume : Measure W)] (A : Set U) (J : Set W) :
    (volume (A ×ˢ J)).toReal = (volume A).toReal * (volume J).toReal := by
  change ((volume.prod volume) (A ×ˢ J)).toReal = _
  rw [Measure.prod_prod, ENNReal.toReal_mul]

end SharpOC.BoxPadding

namespace SharpOC.BoxCounterexample

open BoxParameters BoxGeometry BoxPadding

abbrev PaddedE := E × (Fin ell → ℝ)
abbrev PaddedAmbient := IntegerSpace × PaddedE

def J : Set (Fin ell → ℝ) := simplex ell
def paddedBody : Set PaddedAmbient := padded body J
def paddedFiber (a : FiberIndex) : Set PaddedE := fiber a ×ˢ J

def mixedIntegerMass (D : Set PaddedAmbient) : ℝ≥0∞ := integerMass D

def b : ℝ := (volume B).toReal
def jvol : ℝ := (volume J).toReal
def W : ℝ := (2 : ℝ)^76 * m + (1 + 76*alpha - m)
def gamma : ℝ := ((ell : ℝ) / (ell + 1))^ell

def totalMass : ℝ := ∑ a : FiberIndex, (volume (fiber a)).toReal

def cutMass (F : Ambient →L[ℝ] ℝ) (t : ℝ) : ℝ :=
  ∑ a : FiberIndex, (volume (fiber a ∩ {x | t ≤ F (base a, x)})).toReal

theorem b_pos : 0 < b := ENNReal.toReal_pos
  (Measure.measure_pos_of_nonempty_interior volume B_interior_nonempty).ne'
  B_compact.measure_ne_top

theorem jvol_pos : 0 < jvol :=
  ENNReal.toReal_pos (simplex_volume_pos ell).ne' (simplex_volume_ne_top ell)

theorem gamma_pos : 0 < gamma := by
  unfold gamma
  have : (0 : ℝ) < ell := Nat.cast_pos.mpr ell_pos
  positivity

theorem b_eq : b = (volume BoxSources.B0).toReal * (2 : ℝ)^h := by
  unfold b B F
  rw [volume_prod_toReal, box_volume_toReal (by norm_num : (0:ℝ) ≤ 1)]
  simp

theorem K_real_volume (a : Fin 4) (k : ℕ) : (volume (K a k)).toReal = b * m := by
  unfold K
  rw [volume_prod_toReal, BoxSources.K_volume, ENNReal.toReal_mul,
    ENNReal.toReal_ofReal (mul_nonneg (pow_nonneg (mul_nonneg (by norm_num) s_pos.le) 3) theta_pos.le),
    box_volume_toReal (mul_nonneg (by norm_num) q_pos.le)]
  rw [b_eq]
  simp only [Fintype.card_fin]
  unfold m
  simp only [mul_pow]
  ring

theorem A_real_volume (a : Fin 4) : (volume (A a)).toReal = b * alpha := by
  unfold A
  rw [volume_prod_toReal, BoxSources.A_volume, ENNReal.toReal_mul,
    ENNReal.toReal_ofReal (mul_nonneg (pow_nonneg t_pos.le 3) theta_pos.le), box_volume_toReal u_pos.le]
  rw [b_eq]
  simp only [Fintype.card_fin]
  rw [mul_pow]
  unfold alpha
  ring

theorem alpha_le_m : alpha ≤ m := alpha_lt_m.le

theorem coreFiber_real_volume (S : Finset IntegerCoordinate) :
    (volume (coreFiber S)).toReal = if S = ∅ then b else b*m := by
  classical
  by_cases hs : S = ∅
  · simp [hs, b]
  · simp [coreFiber, hs, K_real_volume]

theorem totalMass_eq : totalMass = b * W := by
  classical
  have hc : (∑ S : Finset IntegerCoordinate, (volume (coreFiber S)).toReal) =
      (2 : ℝ)^76*(b*m) + (b-b*m) := by
    calc
      _ = ∑ S : Finset IntegerCoordinate, (b*m + if S = ∅ then b-b*m else 0) := by
        apply Finset.sum_congr rfl
        intro S hS
        rw [coreFiber_real_volume]
        split_ifs <;> ring
      _ = _ := by
        rw [Finset.sum_add_distrib]
        simp only [Finset.sum_const, Finset.card_univ, core_fiber_count,
          nsmul_eq_mul, Nat.cast_pow, Nat.cast_ofNat, Finset.sum_ite_eq',
          Finset.mem_univ, ite_true]
  have ho : (∑ i : IntegerCoordinate, (volume (A i.1)).toReal) = 76*(b*alpha) := by
    simp only [A_real_volume, Finset.sum_const, Finset.card_univ,
      integerCoordinate_card, nsmul_eq_mul, Nat.cast_ofNat]
  unfold totalMass
  rw [Fintype.sum_sum_type]
  change (∑ S : Finset IntegerCoordinate, (volume (coreFiber S)).toReal) +
    (∑ i : IntegerCoordinate, (volume (A i.1)).toReal) = _
  rw [hc, ho]
  unfold W
  ring

theorem W_pos : 0 < W := by
  have hm := m_pos
  have ha := alpha_pos
  have hp : (1:ℝ) ≤ 2^76 := by norm_num
  unfold W
  nlinarith

theorem fiber_volume_ne_top (a : FiberIndex) : volume (fiber a) ≠ ⊤ :=
  (fiber_compact a).measure_ne_top

theorem fiber_cut_volume_ne_top
    (F : Ambient → ℝ) (t : ℝ) (a : FiberIndex) :
    volume (fiber a ∩ {x | t ≤ F (base a, x)}) ≠ ⊤ :=
  ne_of_lt (lt_of_le_of_lt (measure_mono Set.inter_subset_left)
    (fiber_compact a).measure_lt_top)

theorem integerMass_body : integerMass body = ∑ a : FiberIndex, volume (fiber a) := by
  rw [integerMass_eq_sum body integerBase integerBase_injective integer_base_census]
  simp_rw [integerBase_cast, fiber_exact]

theorem integerMass_body_toReal : (integerMass body).toReal = b*W := by
  rw [integerMass_body, ENNReal.toReal_sum (fun a _ => fiber_volume_ne_top a)]
  exact totalMass_eq

theorem integerMass_body_cut
    (F : Ambient → ℝ) (t : ℝ) :
    integerMass (body ∩ {p | t ≤ F p}) =
      ∑ a : FiberIndex, volume (fiber a ∩ {x | t ≤ F (base a, x)}) := by
  rw [integerMass_eq_sum _ integerBase integerBase_injective
    (fun z x hx => integer_base_census z x hx.1)]
  simp_rw [integerBase_cast]
  apply Finset.sum_congr rfl
  intro a ha
  change volume ({x | (base a, x) ∈ body} ∩ {x | t ≤ F (base a, x)}) = _
  rw [fiber_exact]

theorem integerMass_body_cut_toReal (F : Ambient →L[ℝ] ℝ) (t : ℝ) :
    (integerMass (body ∩ {p | t ≤ F p})).toReal = cutMass F t := by
  rw [integerMass_body_cut, ENNReal.toReal_sum (fun a _ => fiber_cut_volume_ne_top F t a)]
  rfl

theorem paddedBody_compact : IsCompact paddedBody :=
  padded_compact body_compact (simplex_compact ell)
theorem paddedBody_convex : Convex ℝ paddedBody :=
  padded_convex body_convex (simplex_convex ell)
theorem paddedBody_interior_nonempty : (interior paddedBody).Nonempty :=
  padded_interior_nonempty body_interior_nonempty (simplex_interior_nonempty ell)

theorem paddedFiber_compact (a : FiberIndex) : IsCompact (paddedFiber a) :=
  (fiber_compact a).prod (simplex_compact ell)

theorem padded_fiber_exact (a : FiberIndex) :
    {x | (base a, x) ∈ paddedBody} = paddedFiber a := by
  change {x | (base a, x) ∈ body} ×ˢ J = fiber a ×ˢ J
  rw [fiber_exact]

theorem padded_integer_fiber_exact (a : FiberIndex) :
    {x | ((fun i => (integerBase a i : ℝ)), x) ∈ paddedBody} = paddedFiber a := by
  rw [integerBase_cast, padded_fiber_exact]

theorem padded_integer_base_census (z : IntegerCoordinate → ℤ) (x : PaddedE)
    (hx : ((fun i => (z i : ℝ)), x) ∈ paddedBody) : ∃ a, integerBase a = z :=
  integer_base_census z x.1 hx.1

theorem mixedIntegerMass_eq_sum_of_subset
    (D : Set PaddedAmbient) (hD : D ⊆ paddedBody) :
    mixedIntegerMass D = ∑ a : FiberIndex, volume {x | (base a, x) ∈ D} := by
  unfold mixedIntegerMass
  rw [integerMass_eq_sum _ integerBase integerBase_injective
    (fun z x hx => padded_integer_base_census z x (hD hx))]
  simp_rw [integerBase_cast]

theorem mixedIntegerMass_paddedBody :
    mixedIntegerMass paddedBody = ∑ a : FiberIndex, volume (paddedFiber a) := by
  rw [mixedIntegerMass_eq_sum_of_subset _ (Subset.refl _)]
  simp_rw [padded_fiber_exact]

theorem mixedIntegerMass_paddedBody_toReal :
    (mixedIntegerMass paddedBody).toReal = b * W * jvol := by
  change (integerMass (padded body J)).toReal = _
  rw [integerMass_padded, ENNReal.toReal_mul, integerMass_body_toReal]
  rfl

theorem mixedIntegerMass_paddedBody_ne_top : mixedIntegerMass paddedBody ≠ ⊤ := by
  rw [mixedIntegerMass_paddedBody]
  exact ENNReal.sum_ne_top.mpr (fun a _ => (paddedFiber_compact a).measure_ne_top)

theorem mixedIntegerMass_paddedBody_toReal_pos : 0 < (mixedIntegerMass paddedBody).toReal := by
  rw [mixedIntegerMass_paddedBody_toReal]
  exact mul_pos (mul_pos b_pos W_pos) jvol_pos

theorem mixedIntegerMass_paddedBody_pos : 0 < mixedIntegerMass paddedBody :=
  ENNReal.toReal_pos_iff.mp mixedIntegerMass_paddedBody_toReal_pos |>.1

theorem mixedIntegerMass_paddedBody_cut
    (F : PaddedAmbient → ℝ) (t : ℝ) :
    mixedIntegerMass (paddedBody ∩ {p | t ≤ F p}) =
      ∑ a : FiberIndex, volume (paddedFiber a ∩ {x | t ≤ F (base a, x)}) := by
  rw [mixedIntegerMass_eq_sum_of_subset _ Set.inter_subset_left]
  apply Finset.sum_congr rfl
  intro a ha
  change volume ({x | (base a, x) ∈ paddedBody} ∩ {x | t ≤ F (base a, x)}) = _
  rw [padded_fiber_exact]

theorem middle_cut_mass (j : Fin 4) : cutMass (middleCut j) 0 = b*(27/64+19*alpha) := by
  classical
  have hm : (volume (fiber (.inl ∅) ∩
      {x | 0 ≤ middleCut j (base (.inl ∅), x)})).toReal = b*(27/64) := by
    rw [fiber_cut_middle_eq, volume_prod_toReal, BoxSources.cap_volume,
      ENNReal.toReal_mul, ENNReal.toReal_ofReal (by norm_num)]
    unfold b B
    rw [volume_prod_toReal]
    ring
  have hc : ∀ S : Finset IntegerCoordinate,
      (volume (fiber (.inl S) ∩ {x | 0 ≤ middleCut j (base (.inl S), x)})).toReal =
        if S = ∅ then b*(27/64) else 0 := by
    intro S
    by_cases hs : S = ∅
    · subst S; simpa using hm
    · rw [fiber_cut_core_eq_empty j S (Finset.nonempty_iff_ne_empty.mpr hs)]
      simp [hs]
  have ho : ∀ i : IntegerCoordinate,
      (volume (fiber (.inr i) ∩ {x | 0 ≤ middleCut j (base (.inr i), x)})).toReal =
        if paid j i then b*alpha else 0 := by
    intro i
    rw [fiber_cut_outer_eq]
    split_ifs <;> simp [A_real_volume]
  unfold cutMass
  rw [Fintype.sum_sum_type]
  simp_rw [hc, ho]
  rw [paid_sum]
  simp only [Finset.sum_ite_eq', Finset.mem_univ, ite_true]
  ring

theorem endpoint_real_volume_le (a : FiberIndex) (ha : a ≠ .inl ∅) :
    (volume (fiber a)).toReal ≤ b*m := by
  cases a with
  | inl S =>
    have hs : S ≠ ∅ := fun h => ha (congrArg Sum.inl h)
    simp [fiber, coreFiber, hs, K_real_volume]
  | inr i =>
    rw [fiber_inr, A_real_volume]
    exact mul_le_mul_of_nonneg_left alpha_le_m b_pos.le

theorem endpoint_exposing (a : FiberIndex) (ha : a ≠ .inl ∅) :
    ∃ ell : IntegerSpace →L[ℝ] ℝ,
      ∀ c, c ≠ a → ell (base c) < ell (base a) := by
  cases a with
  | inl S =>
    have hs : S.Nonempty := Finset.nonempty_iff_ne_empty.mpr (fun h => ha (congrArg Sum.inl h))
    refine ⟨(coordinateFunctional (cubeExposingCoefficients S)).toContinuousLinearMap, ?_⟩
    exact nonempty_cube_exposes_generator S hs
  | inr i =>
    refine ⟨(coordinateFunctional (negativeUnit i)).toContinuousLinearMap, ?_⟩
    exact negative_unit_exposes_generator i

theorem endpoint_padded_small_cut (a : FiberIndex) (ha : a ≠ .inl ∅) (x : PaddedE) :
    ∃ F : PaddedAmbient →L[ℝ] ℝ, ∃ t : ℝ,
      F ≠ 0 ∧ t ≤ F (base a, x) ∧
      (mixedIntegerMass (paddedBody ∩ {p | t ≤ F p})).toReal ≤ b*jvol*(gamma*m) := by
  obtain ⟨ellF, hexp⟩ := endpoint_exposing a ha
  obtain ⟨F, t, hF, htx, hmass⟩ := exposed_product_simplex_fiber_sum_mass
    ell_pos volume base fiber fiber_compact a ellF hexp x
  refine ⟨F, t, hF, htx, ?_⟩
  have heq : mixedIntegerMass (paddedBody ∩ {p | t ≤ F p}) =
      ENNReal.ofReal gamma * volume (fiber a) * volume J := by
    rw [mixedIntegerMass_paddedBody_cut]
    exact hmass
  rw [heq, ENNReal.toReal_mul, ENNReal.toReal_mul,
    ENNReal.toReal_ofReal gamma_pos.le]
  change gamma * (volume (fiber a)).toReal * jvol ≤ _
  have hb := endpoint_real_volume_le a ha
  nlinarith [mul_le_mul_of_nonneg_right
    (mul_le_mul_of_nonneg_left hb gamma_pos.le) jvol_pos.le]

/-- Every point over every actual base has a containing proper ambient
closed halfspace with the fixed numerator bound. -/
theorem every_padded_fiber_point_small_cut (a : FiberIndex) (x : PaddedE) :
    ∃ F : PaddedAmbient →L[ℝ] ℝ, ∃ t : ℝ,
      F ≠ 0 ∧ t ≤ F (base a, x) ∧
      (mixedIntegerMass (paddedBody ∩ {p | t ≤ F p})).toReal ≤
        b*jvol*uniformNumerator := by
  by_cases ha : a = .inl ∅
  · subst a
    obtain ⟨j, hj⟩ := middleCut_cover x.1
    refine ⟨extendCut (middleCut j), 0, extendCut_ne_zero (middleCut_nonzero j), ?_, ?_⟩
    · rw [base_empty]
      change 0 ≤ middleCut j (0, x.1)
      exact hj
    · change (integerMass (padded body J ∩ {p | 0 ≤ extendCut (middleCut j) p})).toReal ≤ _
      rw [integerMass_padded_cut, ENNReal.toReal_mul, integerMass_body_cut_toReal,
        middle_cut_mass]
      change b*(27/64+19*alpha)*jvol ≤ _
      have h := mul_le_mul_of_nonneg_left
        (le_max_left (27/64+19*alpha) (paddingGamma*m))
        (mul_nonneg b_pos.le jvol_pos.le)
      unfold uniformNumerator
      nlinarith
  · obtain ⟨F,t,hF,ht,hm⟩ := endpoint_padded_small_cut a ha x
    refine ⟨F,t,hF,ht,hm.trans ?_⟩
    exact mul_le_mul_of_nonneg_left (le_max_right _ _)
      (mul_nonneg b_pos.le jvol_pos.le)

def depthBound : ℝ := uniformNumerator / normalizedTotal

theorem depthBound_pos : 0 < depthBound :=
  div_pos uniformNumerator_pos normalizedTotal_pos

theorem depthBound_lt_one_over_e : depthBound < 1/(Real.exp 1*(2:ℝ)^76) :=
  scalar_depth_bound

theorem point_has_small_halfspace (z : IntegerCoordinate → ℤ) (x : PaddedE)
    (hx : ((fun i => (z i : ℝ)), x) ∈ paddedBody) :
    ∃ F : PaddedAmbient →L[ℝ] ℝ, ∃ t : ℝ,
      F ≠ 0 ∧ t ≤ F ((fun i => (z i : ℝ)), x) ∧
      (mixedIntegerMass (paddedBody ∩ {p | t ≤ F p})).toReal /
        (mixedIntegerMass paddedBody).toReal ≤ depthBound := by
  obtain ⟨a, ha⟩ := padded_integer_base_census z x hx
  obtain ⟨F,t,hF,ht,hm⟩ := every_padded_fiber_point_small_cut a x
  refine ⟨F,t,hF,?_,?_⟩
  · simpa only [← ha, integerBase_cast] using ht
  · apply (div_le_iff₀ mixedIntegerMass_paddedBody_toReal_pos).mpr
    rw [mixedIntegerMass_paddedBody_toReal]
    change _ ≤ (uniformNumerator / W) * (b * W * jvol)
    have heq : (uniformNumerator / W) * (b * W * jvol) = b*jvol*uniformNumerator := by
      field_simp [W_pos.ne']

    rw [heq]
    exact hm

theorem origin_mem_paddedBody : ((0 : IntegerSpace), (0 : PaddedE)) ∈ paddedBody := by
  constructor
  · have h0 : (0 : E) ∈ B := interior_subset zero_mem_interior_B
    rwa [← origin_fiber_exact] at h0
  · exact zero_mem_simplex ell

theorem padded_fibers_full_dimensional (z : IntegerCoordinate → ℤ)
    (hz : {x : PaddedE | ((fun i => (z i : ℝ)), x) ∈ paddedBody}.Nonempty) :
    (interior {x : PaddedE | ((fun i => (z i : ℝ)), x) ∈ paddedBody}).Nonempty := by
  obtain ⟨x,hx⟩ := hz
  obtain ⟨a,rfl⟩ := padded_integer_base_census z x hx
  rw [padded_integer_fiber_exact]
  change (interior (fiber a ×ˢ J)).Nonempty
  rw [interior_prod_eq]
  exact (fiber_interior_nonempty a).prod (simplex_interior_nonempty ell)

theorem continuous_dimension : Module.finrank ℝ PaddedE = continuousDimension := by
  simp [PaddedE, E, BoxSources.E0, FreeSpace, continuousDimension, Module.finrank_prod]

theorem continuous_dimension_numeric :
    Module.finrank ℝ PaddedE = 1372131 + 2^93 := by
  rw [continuous_dimension]
  norm_num [continuousDimension, h, ell]

/-- A fully instantiated counterexample to the exact 1/(e*2^76)
claim, in finite continuous dimension 3+h+ell. The mass is the sum of
actual Lebesgue fiber volumes over every integer point. -/
theorem one_over_e_counterexample :
    Module.finrank ℝ IntegerSpace = 76 ∧
    Module.finrank ℝ PaddedE = 1372131 + 2^93 ∧
    ∃ C : Set PaddedAmbient,
      IsCompact C ∧ Convex ℝ C ∧ (interior C).Nonempty ∧
      ((0 : IntegerSpace), (0 : PaddedE)) ∈ C ∧
      0 < mixedIntegerMass C ∧ mixedIntegerMass C ≠ ⊤ ∧
      (∀ z : IntegerCoordinate → ℤ,
        {x : PaddedE | ((fun i => (z i : ℝ)), x) ∈ C}.Nonempty →
        (interior {x : PaddedE | ((fun i => (z i : ℝ)), x) ∈ C}).Nonempty) ∧
      ∃ r : ℝ, 0 < r ∧ r < 1/(Real.exp 1*(2:ℝ)^76) ∧
        ∀ (z : IntegerCoordinate → ℤ) (x : PaddedE),
          ((fun i => (z i : ℝ)), x) ∈ C →
          ∃ F : PaddedAmbient →L[ℝ] ℝ, ∃ t : ℝ,
            F ≠ 0 ∧ t ≤ F ((fun i => (z i : ℝ)), x) ∧
            (mixedIntegerMass (C ∩ {p | t ≤ F p})).toReal /
                (mixedIntegerMass C).toReal ≤ r := by
  exact ⟨integer_dimension, continuous_dimension_numeric, paddedBody, paddedBody_compact, paddedBody_convex, paddedBody_interior_nonempty,
    origin_mem_paddedBody, mixedIntegerMass_paddedBody_pos, mixedIntegerMass_paddedBody_ne_top,
    padded_fibers_full_dimensional, depthBound, depthBound_pos, depthBound_lt_one_over_e,
    point_has_small_halfspace⟩

end SharpOC.BoxCounterexample
