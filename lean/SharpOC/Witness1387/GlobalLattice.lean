import SharpOC.LatticeGeometry
import SharpOC.Witness1387.Support

/-!
# Integer census of the 1387-dimensional witness

A nonzero target block fixes the corresponding block of every generator
with positive weight. At a target outside the baseline product, this
fixes the flip. The guard then fixes each zero target block.
-/

namespace SharpOC.Witness1387

private def realCast {ι : Type*} (z : ι → ℤ) : ι → ℝ :=
  fun i => (z i : ℝ)

private theorem realCast_zero {ι : Type*} : realCast (0 : ι → ℤ) = 0 := by
  funext i
  simp [realCast]

private theorem census_of_weights
    {α B C L : Type*} [Fintype α]
    (block : α → B → C → ℤ) (baseline : L → C → ℤ) (flipped : α → Option B)
    (sites : Set (C → ℤ)) (guard : (C → ℝ) →ₗ[ℝ] ℝ)
    (hsite : ∀ a i, block a i ∈ sites)
    (hcensus : ∀ z, realCast z ∈ convexHull ℝ (realCast '' sites) → z ∈ sites)
    (hexposed : ∀ z ∈ sites, z ≠ 0 → ∃ ℓ : (C → ℝ) →ₗ[ℝ] ℝ,
      ∀ x ∈ sites, x ≠ z → ℓ (realCast x) < ℓ (realCast z))
    (hbaseline_zero : ∃ l, baseline l = 0)
    (hguard_nonneg : ∀ l, 0 ≤ guard (realCast (baseline l)))
    (hguard_zero : ∀ l, guard (realCast (baseline l)) = 0 → baseline l = 0)
    (hnot_flipped : ∀ a i, flipped a ≠ some i → ∃ l, block a i = baseline l)
    (hbaseline_product : ∀ b : B → L, ∃ a, ∀ i, block a i = baseline (b i))
    (z : B → C → ℤ) (w : α → ℝ) (hw : ∀ a, 0 ≤ w a) (hs : ∑ a, w a = 1)
    (havg : ∀ i, ∑ a, w a • realCast (block a i) = realCast (z i)) :
    ∃ a, block a = z := by
  classical
  have hlocal (i : B) : z i ∈ sites := by
    apply hcensus
    exact mem_convexHull_of_exists_fintype w (fun a => realCast (block a i)) hw hs
      (fun a => ⟨block a i, hsite a i, rfl⟩) (havg i)
  have hfixed (a : α) (ha : 0 < w a) (i : B) (hi : z i ≠ 0) : block a i = z i := by
    obtain ⟨ℓ, hℓ⟩ := hexposed (z i) (hlocal i) hi
    have hupper (b : α) : ℓ (realCast (block b i)) ≤ ℓ (realCast (z i)) := by
      by_cases hb : block b i = z i
      · rw [hb]
      · exact le_of_lt (hℓ (block b i) (hsite b i) hb)
    have heq : ∑ b, w b * ℓ (realCast (block b i)) = ℓ (realCast (z i)) := by
      simpa only [map_sum, map_smul, smul_eq_mul] using congrArg ℓ (havg i)
    by_contra hne
    exact (ne_of_gt ha) (weight_eq_zero_of_average_eq_upper w
      (fun b => ℓ (realCast (block b i))) _ hw hs hupper heq a
      (hℓ (block a i) (hsite a i) hne))
  by_cases hbaseline : ∀ i, ∃ l, z i = baseline l
  · choose b hb using hbaseline
    obtain ⟨a, ha⟩ := hbaseline_product b
    exact ⟨a, funext fun i => (ha i).trans (hb i).symm⟩
  · push Not at hbaseline
    obtain ⟨i, hi⟩ := hbaseline
    obtain ⟨l, hl⟩ := hbaseline_zero
    have hni : z i ≠ 0 := fun h => hi l (h.trans hl.symm)
    have hflip (a : α) (ha : 0 < w a) : flipped a = some i := by
      by_contra hn
      obtain ⟨b, hb⟩ := hnot_flipped a i hn
      exact hi b ((hfixed a ha i hni).symm.trans hb)
    have hpositive : ∃ a, 0 < w a := by
      by_contra! h
      have hz (a : α) : w a = 0 := le_antisymm (h a) (hw a)
      simp [hz] at hs
    obtain ⟨a, ha⟩ := hpositive
    refine ⟨a, funext fun j => ?_⟩
    by_cases hj : z j = 0
    · have hji : j ≠ i := fun h => hni (h ▸ hj)
      have hplain (b : α) (hb : 0 < w b) : ∃ l, block b j = baseline l :=
        hnot_flipped b j fun hf => hji (Option.some.inj (hf.symm.trans (hflip b hb)))
      have hsum : ∑ b, w b * guard (realCast (block b j)) = 0 := by
        simpa only [map_sum, map_smul, smul_eq_mul, hj, realCast_zero, map_zero]
          using congrArg guard (havg j)
      have hnonneg (b : α) : 0 ≤ w b * guard (realCast (block b j)) := by
        by_cases hb : 0 < w b
        · obtain ⟨l, hl⟩ := hplain b hb
          rw [hl]
          exact mul_nonneg (hw b) (hguard_nonneg l)
        · rw [le_antisymm (le_of_not_gt hb) (hw b), zero_mul]
      have hzero := (Finset.sum_eq_zero_iff_of_nonneg (fun b _ => hnonneg b)).mp
        hsum a (Finset.mem_univ a)
      obtain ⟨l, hl⟩ := hplain a ha
      rw [hl] at hzero
      rw [hj, hl]
      exact hguard_zero l ((mul_eq_zero.mp hzero).resolve_left (ne_of_gt ha))
    · exact hfixed a ha j hj

private theorem eligible_of_flip_eq_some {s : SupportIndex} {i : Block}
    (h : flip s = some i) : eligible (parent s i) = true := by
  cases s with
  | inl b => simp at h
  | inr b => exact selectedFlip_eligible h

theorem integerBlock_mem_localSites (s : SupportIndex) (i : Block) :
    integerBlock s i ∈ localSites := by
  rw [localSites, Set.mem_union]
  by_cases h : flip s = some i
  · right
    exact ⟨⟨parent s i, eligible_of_flip_eq_some h⟩, by simp [integerBlock, h]⟩
  · left
    exact ⟨parent s i, by simp [integerBlock, h]⟩

/-- The support hull has exactly the baseline tuples and their selected lights
as integer sites. -/
theorem integer_census (z : Coordinate → ℤ) :
    (fun c => (z c : ℝ)) ∈ convexHull ℝ (Set.range base) ↔
      z ∈ Set.range integerBase := by
  classical
  constructor
  · intro hz
    obtain ⟨w, hw, hs, havg⟩ := (mem_convexHull_range_iff_weights base _).mp hz
    have havg_block (i : Block) :
        ∑ a, w a • realCast (integerBlock a i) = realCast (fun j => z (i, j)) := by
      funext j
      simpa only [Finset.sum_apply, Pi.smul_apply, base, integerBase, realCast]
        using congrFun havg (i, j)
    obtain ⟨s, hgen⟩ := census_of_weights integerBlock localBase flip localSites localGuardReal
      integerBlock_mem_localSites
      (fun z hz => (local_integer_census z).mp hz)
      (fun _ hz hn => local_exposed hz hn)
      ⟨0, localBase_zero⟩
      (fun l => by
        change 0 ≤ localGuardReal (localReal (localBase l))
        rw [localGuardReal_localReal]
        exact_mod_cast localGuard_base_nonneg l)
      (fun l h => by
        change localGuardReal (localReal (localBase l)) = 0 at h
        rw [localGuardReal_localReal] at h
        by_cases hl : l = 0
        · simpa only [hl] using localBase_zero
        · exact ((ne_of_gt (localGuard_base_pos l hl)) (by exact_mod_cast h)).elim)
      (fun a i h => ⟨parent a i, by simp [integerBlock, h]⟩)
      (fun b => ⟨.inl b, fun i => by simp [integerBlock]⟩)
      (fun i j => z (i, j)) w hw hs havg_block
    exact ⟨s, funext fun c => congrFun (congrFun hgen c.1) c.2⟩
  · rintro ⟨s, rfl⟩
    exact subset_convexHull ℝ _ ⟨s, rfl⟩

theorem integerBlock_guard_neg_iff (s : SupportIndex) (i : Block) :
    localGuard (integerBlock s i) < 0 ↔ flip s = some i := by
  constructor
  · intro hg
    by_contra hf
    rw [integerBlock, ite_eq_right hf] at hg
    exact (not_lt_of_ge (localGuard_base_nonneg _)) hg
  · intro hf
    rw [integerBlock, ite_eq_left hf, localGuard_neg, (eligible_iff _).mp (eligible_of_flip_eq_some hf)]
    norm_num

theorem integerBase_injective : Function.Injective integerBase := by
  intro a b h
  have hblock (i : Block) : integerBlock a i = integerBlock b i :=
    funext fun j => congrFun h (i, j)
  have hflip : flip a = flip b := Option.ext fun i => by
    rw [← integerBlock_guard_neg_iff a i, ← integerBlock_guard_neg_iff b i, hblock i]
  have hparent : parent a = parent b := by
    funext i
    apply localBase_injective
    by_cases ha : flip a = some i
    · have hb : flip b = some i := hflip ▸ ha
      exact neg_injective (by simpa only [integerBlock, ite_eq_left ha, ite_eq_left hb] using hblock i)
    · have hb : flip b ≠ some i := hflip ▸ ha
      simpa only [integerBlock, ite_eq_right ha, ite_eq_right hb] using hblock i
  cases a with
  | inl a =>
    cases b with
    | inl b => exact congrArg Sum.inl hparent
    | inr b => exact (Option.isSome_iff_ne_none.mp b.property hflip.symm).elim
  | inr a =>
    cases b with
    | inl b => exact (Option.isSome_iff_ne_none.mp a.property hflip).elim
    | inr b => exact congrArg Sum.inr (Subtype.ext hparent)

theorem base_injective : Function.Injective base := by
  intro a b h
  apply integerBase_injective
  funext i
  exact Int.cast_injective (congrFun h i)

/-- Restrict an ambient point to one local block. -/
def restrictBlock (i : Block) : (Coordinate → ℝ) →ₗ[ℝ] (Fin 11 → ℝ) where
  toFun z j := z (i, j)
  map_add' _ _ := rfl
  map_smul' _ _ := rfl

@[simp] theorem restrictBlock_base (i : Block) (s : SupportIndex) :
    restrictBlock i (base s) = localReal (integerBlock s i) := rfl

/-- A single score fixes all the nonzero blocks of the target. -/
theorem expose_nonzero_blocks_at (s₀ : SupportIndex) :
    ∃ ℓ : (Coordinate → ℝ) →ₗ[ℝ] ℝ,
      ∀ s : SupportIndex, ℓ (base s) ≤ ℓ (base s₀) ∧
        (ℓ (base s) = ℓ (base s₀) ↔
          ∀ i, integerBlock s₀ i ≠ 0 → integerBlock s i = integerBlock s₀ i) := by
  classical
  have hex (i : Block) : ∃ ℓ : (Fin 11 → ℝ) →ₗ[ℝ] ℝ,
      integerBlock s₀ i ≠ 0 → ∀ z ∈ localSites, z ≠ integerBlock s₀ i →
        ℓ (localReal z) < ℓ (localReal (integerBlock s₀ i)) := by
    by_cases h : integerBlock s₀ i = 0
    · exact ⟨0, fun hn => (hn h).elim⟩
    · obtain ⟨ℓ, hℓ⟩ := local_exposed (integerBlock_mem_localSites s₀ i) h
      exact ⟨ℓ, fun _ => hℓ⟩
  choose ℓ hℓ using hex
  let S : Finset Block := Finset.univ.filter fun i => integerBlock s₀ i ≠ 0
  let L : (Coordinate → ℝ) →ₗ[ℝ] ℝ := ∑ i ∈ S, (ℓ i).comp (restrictBlock i)
  refine ⟨L, fun s => ?_⟩
  have hmem (i : Block) : i ∈ S ↔ integerBlock s₀ i ≠ 0 := by simp [S]
  have hle (i : Block) (hi : i ∈ S) :
      ℓ i (localReal (integerBlock s i)) ≤ ℓ i (localReal (integerBlock s₀ i)) := by
    by_cases he : integerBlock s i = integerBlock s₀ i
    · rw [he]
    · exact (hℓ i ((hmem i).mp hi) _ (integerBlock_mem_localSites s i) he).le
  simp only [L, LinearMap.sum_apply, LinearMap.comp_apply, restrictBlock_base]
  refine ⟨Finset.sum_le_sum hle, ?_⟩
  constructor
  · intro he i hi
    by_contra hn
    exact (ne_of_lt (Finset.sum_lt_sum hle ⟨i, (hmem i).mpr hi,
      hℓ i hi _ (integerBlock_mem_localSites s i) hn⟩)) he
  · intro h
    apply Finset.sum_congr rfl
    intro i hi
    rw [h i ((hmem i).mp hi)]

theorem expose_nonzero_blocks (b : Baseline) :
    ∃ ℓ : (Coordinate → ℝ) →ₗ[ℝ] ℝ,
      ∀ s : SupportIndex, ℓ (base s) ≤ ℓ (base (.inl b)) ∧
        (ℓ (base s) = ℓ (base (.inl b)) ↔
          ∀ i, b i ≠ 0 → integerBlock s i = localBase (b i)) := by
  simpa [integerBlock] using expose_nonzero_blocks_at (.inl b)

/-- Maximize the second score on the maximizing face of the first. -/
theorem combine_face_scores {α E : Type*} [Finite α] [AddCommGroup E] [Module ℝ E]
    (z : α → E) (a₀ : α) (f g : E →ₗ[ℝ] ℝ)
    (hf : ∀ a, f (z a) ≤ f (z a₀))
    (hg : ∀ a, f (z a) = f (z a₀) → g (z a) ≤ g (z a₀)) :
    ∃ L : E →ₗ[ℝ] ℝ, ∀ a, L (z a) ≤ L (z a₀) ∧
      (L (z a) = L (z a₀) ↔ f (z a) = f (z a₀) ∧ g (z a) = g (z a₀)) := by
  let q (a : α) := (g (z a) - g (z a₀)) / (f (z a₀) - f (z a))
  obtain ⟨Q, hQ⟩ := Finite.bddAbove_range q
  let C := Q + 1
  refine ⟨C • f + g, fun a => ?_⟩
  change C * f (z a) + g (z a) ≤ C * f (z a₀) + g (z a₀) ∧
    (C * f (z a) + g (z a) = C * f (z a₀) + g (z a₀) ↔
      f (z a) = f (z a₀) ∧ g (z a) = g (z a₀))
  by_cases h : f (z a) = f (z a₀)
  · rw [h]
    exact ⟨by linarith [hg a h], by simp⟩
  · have hq : q a < C := lt_of_le_of_lt (hQ (Set.mem_range_self a)) (lt_add_one _)
    have hlarge := (div_lt_iff₀ (sub_pos.mpr (lt_of_le_of_ne (hf a) h))).mp hq
    rw [mul_sub] at hlarge
    have hlt : C * f (z a) + g (z a) < C * f (z a₀) + g (z a₀) := by linarith
    exact ⟨hlt.le, by simp [hlt.ne, h]⟩

private theorem support_eq_of_blocks_eq {s t : SupportIndex}
    (h : ∀ i, integerBlock s i = integerBlock t i) : s = t :=
  integerBase_injective (funext fun c => congrFun (h c.1) c.2)

theorem all_nonzero_baseline_exposed (b : Baseline) (hb : ∀ i, b i ≠ 0) :
    ∃ ℓ : (Coordinate → ℝ) →ₗ[ℝ] ℝ,
      ∀ s : SupportIndex, s ≠ .inl b → ℓ (base s) < ℓ (base (.inl b)) := by
  obtain ⟨ℓ, hℓ⟩ := expose_nonzero_blocks b
  refine ⟨ℓ, fun s hs => lt_of_le_of_ne (hℓ s).1 fun he => hs ?_⟩
  apply support_eq_of_blocks_eq
  intro i
  simpa [integerBlock] using (hℓ s).2.mp he i (hb i)

theorem selected_light_exposed (b : {b : Baseline // (selectedFlip b).isSome}) :
    ∃ ℓ : (Coordinate → ℝ) →ₗ[ℝ] ℝ,
      ∀ s : SupportIndex, s ≠ .inr b → ℓ (base s) < ℓ (base (.inr b)) := by
  classical
  let t : SupportIndex := .inr b
  obtain ⟨i, hi⟩ : ∃ i, flip t = some i := by
    cases h : selectedFlip b.val with
    | none => exact (Option.isSome_iff_ne_none.mp b.property h).elim
    | some i => exact ⟨i, h⟩
  have hneg := (integerBlock_guard_neg_iff t i).mpr hi
  have hni : integerBlock t i ≠ 0 := by
    intro h
    simp [h] at hneg
  obtain ⟨f, hf⟩ := expose_nonzero_blocks_at t
  let Z : Finset Block := Finset.univ.filter fun j => integerBlock t j = 0
  have hmem (j : Block) : j ∈ Z ↔ integerBlock t j = 0 := by simp [Z]
  let g : (Coordinate → ℝ) →ₗ[ℝ] ℝ :=
    -(∑ j ∈ Z, localGuardReal.comp (restrictBlock j))
  have hscore (s : SupportIndex) :
      g (base s) = -(∑ j ∈ Z, (localGuard (integerBlock s j) : ℝ)) := by
    simp only [g, LinearMap.neg_apply, LinearMap.sum_apply, LinearMap.comp_apply,
      restrictBlock_base, localGuardReal_localReal]
  have htarget : ∑ j ∈ Z, (localGuard (integerBlock t j) : ℝ) = 0 :=
    Finset.sum_eq_zero fun j hj => by simp [(hmem j).mp hj]
  have hplain (s : SupportIndex) (he : f (base s) = f (base t)) (j : Block) (hj : j ∈ Z) :
      integerBlock s j = localBase (parent s j) := by
    have hfix := (hf s).2.mp he i hni
    have hs : flip s = some i := (integerBlock_guard_neg_iff s i).mp (by rwa [hfix])
    have hji : j ≠ i := fun h => hni (h ▸ (hmem j).mp hj)
    simp [integerBlock, hs, hji.symm]
  have hnonneg (s : SupportIndex) (he : f (base s) = f (base t)) (j : Block) (hj : j ∈ Z) :
      0 ≤ (localGuard (integerBlock s j) : ℝ) := by
    rw [hplain s he j hj]
    exact_mod_cast localGuard_base_nonneg (parent s j)
  obtain ⟨L, hL⟩ := combine_face_scores base t f g (fun s => (hf s).1) (fun s he => by
    simp only [hscore, htarget, neg_zero]
    exact neg_nonpos.mpr (Finset.sum_nonneg (hnonneg s he)))
  refine ⟨L, fun s hs => lt_of_le_of_ne (hL s).1 fun hEq => hs ?_⟩
  obtain ⟨he, hge⟩ := (hL s).2.mp hEq
  apply support_eq_of_blocks_eq
  intro j
  by_cases hz : integerBlock t j = 0
  · have hj := (hmem j).mpr hz
    have hsum : ∑ j ∈ Z, (localGuard (integerBlock s j) : ℝ) = 0 := by
      simpa only [hscore, htarget, neg_zero, neg_eq_zero] using hge
    have hzero := (Finset.sum_eq_zero_iff_of_nonneg (hnonneg s he)).mp hsum j hj
    have hguard : localGuard (localBase (parent s j)) = 0 := by
      rw [hplain s he j hj] at hzero
      exact_mod_cast hzero
    have hp : parent s j = 0 := by
      by_contra hp
      exact (ne_of_gt (localGuard_base_pos _ hp)) hguard
    rw [hplain s he j hj, hp, localBase_zero, hz]
  · exact (hf s).2.mp he j hz

end SharpOC.Witness1387
