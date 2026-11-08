import SharpOC.Witness1387.InactivePair

/-! Priority scores on the guard-zero face with three zero slots. -/

noncomputable section

namespace SharpOC.Witness1387

private theorem singleton_flip {c : Baseline} {j r : Block}
    (hz : zeroSlots c = {j}) (hr : selectedFlip c = some r) :
    (highArrow j (highSlots c) = some r ∧ r ∈ highSlots c) ∨
      ∃ u, highSlots c = {u} ∧ u < j ∧
        bestTail c (fun i => decide (i < u ∨ j < i)) = some r := by
  unfold selectedFlip at hr
  rw [hz, Finset.sort_singleton] at hr
  rcases hs : (highSlots c).sort with _ | ⟨u, _ | ⟨v, l⟩⟩
  · have he : highSlots c = ∅ := by simpa using congrArg List.toFinset hs
    simp [he, highArrow] at hr
  · have he : highSlots c = {u} := by simpa using congrArg List.toFinset hs
    by_cases huj : u < j
    · exact Or.inr ⟨u, he, huj, by simpa [hs, huj] using hr⟩
    · simp [hs, huj] at hr
  · have ha : highArrow j (highSlots c) = some r := by simpa [hs] using hr
    exact Or.inl ⟨ha, highArrow_mem ha⟩

private theorem highSlots_compatible {b c : Baseline} {r k j : Block}
    (hz : zeroSlots b = {r, k, j}) (hkr : k ≠ r) (hc : ∀ l, b l ≠ 0 → c l = b l)
    (hj : c j = 0) (i : Block) :
    i ∈ highSlots c ↔ i ∈ highSlots b ∨ i = r ∧ high (c r) = true ∨
      i = k ∧ high (c k) = true := by
  have hb (l : Block) (hl : l ∈ zeroSlots b) : high (b l) = false := by
    simp [mem_zeroSlots.mp hl, high]
  by_cases hir : i = r
  · subst i
    simp [hkr.symm, hb r (by simp [hz])]
  by_cases hik : i = k
  · subst i
    simp [hir, hb k (by simp [hz])]
  by_cases hij : i = j
  · subst i
    have hj' : high (c j) = false := by simp [hj, high]
    simp [hj', hir, hik, hb j (by simp [hz])]
  have hbi : b i ≠ 0 := fun h => by
    have hm := mem_zeroSlots.mpr h
    simp [hz, hir, hik, hij] at hm
  simp [hir, hik, hc i hbi]

private theorem sorted_prefix {S : Finset Block} (hS : 3 ≤ S.card) :
    ∃ a d e l, S.sort = a :: d :: e :: l ∧ a < d ∧ d < e := by
  have hlen : 3 ≤ S.sort.length := by simpa using hS
  rcases hs : S.sort with _ | ⟨a, _ | ⟨d, _ | ⟨e, l⟩⟩⟩
  all_goals try simp [hs] at hlen
  have hp := S.sortedLT_sort.pairwise
  rw [hs] at hp
  exact ⟨a, d, e, l, hs, (List.pairwise_cons.mp hp).1 d (by simp),
    (List.pairwise_cons.mp (List.pairwise_cons.mp hp).2).1 e (by simp)⟩

/-- The first block wins unless the sentinel is second, when the third wins.
The third only needs the top rank if the second is an available sentinel. -/
private def highRank (Z : Finset Block) (a d e i : Block) : ℕ :=
  if i = e ∧ d ∈ Z then 2 else if i = a then 1 else 0

private theorem highRank_arrow {Z R : Finset Block} {a d e r k j : Block}
    {l : List Block} (hs : (R ∪ Z).sort = a :: d :: e :: l)
    (had : a < d) (hde : d < e) (hz : Z = {r, k, j}) (hkr : k ≠ r)
    {H : Finset Block} (hH : insert j H = R ∪ Z) (ha : highArrow j H = some r) :
    highRank Z a d e k < highRank Z a d e r := by
  unfold highArrow at ha
  rw [hH, hs] at ha
  change (if j = a then none else if j = d then some e else some a) = some r at ha
  by_cases hja : j = a
  · simp [hja] at ha
  by_cases hjd : j = d
  · rw [ite_eq_right hja, ite_eq_left hjd] at ha
    have hd : d ∈ Z := by simp [hz, hjd]
    obtain rfl := Option.some.inj ha
    simp [highRank, hd, hkr]
    split <;> decide
  · rw [ite_eq_right hja, ite_eq_right hjd] at ha
    obtain rfl := Option.some.inj ha
    have hn : ¬(k = e ∧ d ∈ Z) := by
      rintro ⟨rfl, hd⟩
      simp [hz, had.ne.symm, hde.ne, Ne.symm hjd] at hd
    simp [highRank, (had.trans hde).ne, hn, hkr]

private theorem highRank_tail_no_fixed {Z : Finset Block} {a d e r k j : Block}
    (hZ : Z = {a, d, e}) (hz : Z = {r, k, j}) (had : a < d) (hde : d < e)
    (hkj : k < j) (hr : r < k ∨ j < r) :
    highRank Z a d e k < highRank Z a d e r := by
  have hrZ : r ∈ Z := by simp [hz]
  have hkZ : k ∈ Z := by simp [hz]
  have hjZ : j ∈ Z := by simp [hz]
  have hda := had.ne.symm
  have hde' := hde.ne
  have hae := (had.trans hde).ne
  change a.val < d.val at had
  change d.val < e.val at hde
  change k.val < j.val at hkj
  change r.val < k.val ∨ j.val < r.val at hr
  simp only [hZ, Finset.mem_insert, Finset.mem_singleton] at hrZ hkZ hjZ
  rcases hr with hr | hr <;> rcases hrZ with rfl | rfl | rfl <;>
    rcases hkZ with rfl | rfl | rfl <;>
    rcases hjZ with rfl | rfl | rfl <;>
    first | (exfalso; omega) | simp [highRank, hZ, hde', hae, hda]

/-- With one fixed high, only the first zero slot above it can lose
while ineligible for that sentinel. -/
private def tailOffset (Z : Finset Block) (u i : Block) : ℕ :=
  if u < i ∧ ∀ l ∈ Z, u < l → i ≤ l then 0 else 2000

private theorem tailOffset_allowed {Z : Finset Block} {u j i : Block}
    (hj : j ∈ Z) (huj : u < j) (hi : i < u ∨ j < i) : tailOffset Z u i = 2000 := by
  unfold tailOffset
  apply ite_eq_right
  rintro ⟨hui, hm⟩
  exact hi.elim (fun h => h.not_gt hui) (fun h => h.not_ge (hm j hj huj))

private theorem tailOffset_disallowed {Z : Finset Block} {u j r k : Block}
    (hz : Z = {r, k, j}) (huk : u < k) (hkj : k ≤ j)
    (hr : r < u ∨ j < r) : tailOffset Z u k = 0 := by
  unfold tailOffset
  refine ite_eq_left ⟨huk, ?_⟩
  intro l hl hul
  simp only [hz, Finset.mem_insert, Finset.mem_singleton] at hl
  rcases hl with rfl | rfl | rfl
  · exact hr.elim (fun h => (h.not_gt hul).elim) (fun h => hkj.trans h.le)
  · exact le_rfl
  · exact hkj

private theorem highScale_rank_step {i j : ℕ} (h : i < j) :
    3 * (4000 * 3 ^ i) ≤ (4000 * 3 ^ j : ℕ) := by
  calc
    _ = 4000 * 3 ^ (i + 1) := by rw [pow_succ]; ring
    _ ≤ _ := Nat.mul_le_mul_left _ (Nat.pow_le_pow_right (by decide) h)

/-- Linear block priorities strictly rank the flipped site above the
other eligible site of any compatible extra light on a three-zero face. -/
theorem triple_priority {b : Baseline} (hz : (zeroSlots b).card = 3) :
    ∃ priority : Block → (Fin 11 → ℝ) →ₗ[ℝ] ℝ,
      ∀ {c : Baseline} {r k j : Block}, zeroSlots b = {r, k, j} →
        k ≠ r → j ≠ r → j ≠ k → (∀ l, b l ≠ 0 → c l = b l) →
        zeroSlots c = {j} → selectedFlip c = some r → eligible (c k) = true →
        priority k (localReal (localBase (c k))) <
          priority r (localReal (localBase (c r))) := by
  let Z := zeroSlots b
  let R := highSlots b
  have hcard : 3 ≤ (R ∪ Z).card := hz.ge.trans (Finset.card_le_card Finset.subset_union_right)
  obtain ⟨a, d, e, l, hs, had, hde⟩ := sorted_prefix hcard
  let rank := highRank Z a d e
  let scale (i : Block) : ℕ := if R = ∅ then 0 else 4000 * 3 ^ rank i
  let offset (i : Block) : ℕ :=
    if R = ∅ then 2000 * rank i else tailOffset Z (R.sort.headD 0) i
  refine ⟨fun i => priorityScore i (scale i) (offset i), ?_⟩
  intro c r k j hZ hkr _ _ hfix hcz hr hk
  have hczj : c j = 0 := mem_zeroSlots.mp (by simp [hcz])
  have hcomp (i : Block) : i ∈ highSlots c ↔ i ∈ R ∨ i = r ∧ high (c r) = true ∨
      i = k ∧ high (c k) = true := highSlots_compatible hZ hkr hfix hczj i
  have hjZ : j ∈ Z := by simp [Z, hZ]
  have hRout (i : Block) (hi : i ∈ Z) : i ∉ R := by
    simp [R, mem_zeroSlots.mp hi, high]
  have hre := selectedFlip_eligible hr
  have htk := tailPriority_bound c k hk
  have htr := tailPriority_bound c r hre
  rw [priorityScore_apply _ _ _ _ hk, priorityScore_apply _ _ _ _ hre]
  have hord :
    scale k * leadingBits (code (c k)) + tailPriority c k + offset k <
      scale r * leadingBits (code (c r)) + tailPriority c r + offset r := by
    have hboth (hrh : r ∈ highSlots c) (hkh : k ∈ highSlots c) :
        insert j (highSlots c) = R ∪ Z := by
      ext i
      simp only [Finset.mem_insert, hcomp i, Finset.mem_union, Z, hZ,
        Finset.mem_singleton, mem_highSlots.mp hrh, mem_highSlots.mp hkh, and_true,
        or_assoc, or_left_comm, or_comm]
    have hnone (hR : R = ∅) (hord : rank k < rank r) :
        scale k * leadingBits (code (c k)) + tailPriority c k + offset k <
          scale r * leadingBits (code (c r)) + tailPriority c r + offset r := by
      simp [scale, offset, hR]
      omega
    rcases singleton_flip hcz hr with ⟨ha, hrh⟩ | ⟨u, hH, huj, ht⟩
    · by_cases hR : R = ∅
      · have hkh : k ∈ highSlots c := by
          by_contra hn
          have hH : highSlots c = {r} := by
            ext i
            simp [hcomp i, hR, mem_highSlots.mp hrh,
              show high (c k) = false by simpa using hn]
          obtain ⟨i, hi, _⟩ := highArrow_fixed_blocker (R := ∅) (by simpa [hH] using ha)
          exact Finset.notMem_empty i hi
        exact hnone hR (highRank_arrow hs had hde hZ hkr (hboth hrh hkh) ha)
      · have hoff (i : Block) : offset i ≤ 2000 := by
          simp only [offset, hR, ite_false, tailOffset]
          split <;> decide
        have hJr : 1 ≤ leadingBits (code (c r)) := by
          have hne : leadingBits (code (c r)) ≠ 0 := by
            simp [(leadingBits_zero_iff hre), mem_highSlots.mp hrh]
          omega
        have hmulr := Nat.mul_le_mul_left (scale r) hJr
        have hmin (i : Block) : 4000 ≤ scale i := by
          simp only [scale, hR, ite_false]
          have hp : 0 < (3 : ℕ) ^ rank i := by positivity
          simpa using Nat.mul_le_mul_left 4000 (show 1 ≤ 3 ^ rank i by omega)
        by_cases hkh : k ∈ highSlots c
        · have hord : rank k < rank r := highRank_arrow hs had hde hZ hkr (hboth hrh hkh) ha
          have hstep : 3 * scale k ≤ scale r := by
            simpa [scale, hR] using highScale_rank_step hord
          have hmulk := Nat.mul_le_mul_left (scale k) (leadingBits_le_two hk)
          have hmin' := hmin k
          have hok := hoff k
          omega
        · have hJk := (leadingBits_zero_iff hk).mpr (by simpa using hkh)
          rw [hJk, mul_zero, zero_add]
          have hok := hoff k
          have hmin' := hmin r
          omega
    · have hspec := bestTail_spec ht
      have hru : r < u ∨ j < r := by simpa using hspec.1
      have hrh : high (c r) = false := by simpa [tail, hre] using hspec.2.1
      by_cases hR : R = ∅
      · have hu : u = k := by
          have hm : u ∈ highSlots c := by simp [hH]
          have h : u = k ∧ high (c k) = true := by simpa [hR, hrh] using (hcomp u).mp hm
          exact h.1
        subst u
        have hZs : Z.sort = a :: d :: e :: l := by simpa [hR] using hs
        have hlen := Z.length_sort (· ≤ ·)
        have hl : l = [] := by
          rw [hZs, show Z.card = 3 from hz] at hlen
          simp only [List.length_cons] at hlen
          exact List.eq_nil_of_length_eq_zero (by omega)
        have hZ' : Z = {a, d, e} := by simpa [hl] using congrArg List.toFinset hZs
        exact hnone hR (highRank_tail_no_fixed hZ' hZ had hde huj hru)
      · have hsub : R ⊆ {u} := by
          intro i hi
          have hm := (hcomp i).mpr (Or.inl hi)
          rwa [hH] at hm
        obtain ⟨v, hv⟩ := Finset.nonempty_iff_ne_empty.mpr hR
        have hvu : v = u := Finset.mem_singleton.mp (hsub hv)
        have hRu : R = {u} := Finset.Subset.antisymm hsub
          (Finset.singleton_subset_iff.mpr (hvu ▸ hv))
        have hku : k ≠ u := by
          intro he
          exact hRout k (by simp [Z, hZ]) (by simp [hRu, he])
        have hkh : high (c k) = false := by
          by_contra hn
          have hm : k ∈ highSlots c := mem_highSlots.mpr (by simpa using hn)
          exact hku (by simpa [hH] using hm)
        have hJr := (leadingBits_zero_iff hre).mpr hrh
        have hJk := (leadingBits_zero_iff hk).mpr hkh
        simp only [hJr, hJk, mul_zero, zero_add, offset, hR, ite_false]
        rw [hRu, Finset.sort_singleton, List.headD_cons]
        rw [tailOffset_allowed hjZ huj hru]
        by_cases hall : k < u ∨ j < k
        · rw [tailOffset_allowed hjZ huj hall]
          have hle := hspec.2.2 k (by simpa using hall) (by simp [tail, hk, hkh])
          exact Nat.add_lt_add_right (lt_of_le_of_ne hle (tailPriority_ne c hkr)) _
        · have huk : u < k := lt_of_le_of_ne (le_of_not_gt (fun h => hall (Or.inl h))) hku.symm
          have hkj : k ≤ j := le_of_not_gt (fun h => hall (Or.inr h))
          rw [tailOffset_disallowed hZ huk hkj hru]
          omega
  exact_mod_cast hord

end SharpOC.Witness1387
