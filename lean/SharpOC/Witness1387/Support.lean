import SharpOC.Witness1387.Local
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Basic.Real.Basic
import Mathlib.Data.Finset.Sort
import Mathlib.Data.Finset.Sum

/-! The baseline tuples, selected flips, and active pools of the 1387-dimensional witness. -/

namespace SharpOC.Witness1387

open scoped BigOperators

abbrev Block := Fin 19
abbrev Slot := Fin 2048
abbrev Coordinate := Block × Fin 11
abbrev Baseline := Block → Slot

def zeroSlots (b : Baseline) : Finset Block :=
  Finset.univ.filter fun i => b i = 0

def highSlots (b : Baseline) : Finset Block :=
  Finset.univ.filter fun i => high (b i)

def tail (s : Slot) : Bool :=
  eligible s && !high s

/-- The last six coded bits, followed by the reverse block index. -/
def tailPriority (b : Baseline) (i : Block) : ℕ :=
  19 * (code (b i) / 4) + (18 - i.val)

def bestTail (b : Baseline) (allowed : Block → Bool) : Option Block :=
  (List.finRange 19).find? fun i =>
    allowed i && tail (b i) && (List.finRange 19).all fun j =>
      !(allowed j && tail (b j)) || decide (tailPriority b j ≤ tailPriority b i)

/-- A sentinel with at least two high outsiders skips the least high precisely
when it lies between the first two highs. -/
def highArrow (j : Block) (highs : Finset Block) : Option Block :=
  match (insert j highs).sort with
  | a :: b :: c :: _ => if j = a then none else if j = b then some c else some a
  | _ => none

/-- Each tuple adds at most one light, at its selected block's negative site. -/
def selectedFlip (b : Baseline) : Option Block :=
  match (zeroSlots b).sort with
  | [] =>
    match (highSlots b).sort with
    | i :: _ => some i
    | [] => bestTail b (fun _ => true)
  | [j] =>
    match (highSlots b).sort with
    | [r] => if r < j then bestTail b (fun i => decide (i < r ∨ j < i)) else none
    | _ => highArrow j (highSlots b)
  | _ => none

abbrev SupportIndex := Baseline ⊕ {b : Baseline // (selectedFlip b).isSome}

def parent : SupportIndex → Baseline
  | .inl b => b
  | .inr b => b.val

def flip : SupportIndex → Option Block
  | .inl _ => none
  | .inr b => selectedFlip b.val

def integerBlock (s : SupportIndex) (i : Block) : Fin 11 → ℤ :=
  if flip s = some i then -localBase (parent s i) else localBase (parent s i)

def integerBase (s : SupportIndex) (c : Coordinate) : ℤ :=
  integerBlock s c.1 c.2

def base (s : SupportIndex) (c : Coordinate) : ℝ :=
  integerBase s c

/-- The center associated with a selected light is obtained by zeroing its
flipped block. -/
def lightCenter (b : Baseline) : Baseline :=
  match selectedFlip b with
  | some i => Function.update b i 0
  | none => b

/-- The varying block at a one- or two-zero active center. -/
def activeAxis (b : Baseline) : Option Block :=
  match (zeroSlots b).sort with
  | [i] =>
    match (highSlots b).sort with
    | r :: _ => if r < i then none else some i
    | [] => some i
  | [i, j] =>
    if highArrow j (insert i (highSlots b)) = some i then some i
    else if highArrow i (insert j (highSlots b)) = some j then some j
    else none
  | _ => none

def poolSites (b : Baseline) (i : Block) (row : Fin 4) : Finset Slot :=
  Finset.univ.filter fun s =>
    owner s = row ∧ selectedFlip (Function.update b i s) = some i

/-- The number of lights in a row of the active center's varying slice. -/
def pool (b : Baseline) (row : Fin 4) : ℕ :=
  match activeAxis b with
  | some i => (poolSites b i row).card
  | none => 0

/-- The modular sum of the local owners selects the continuous sector. -/
def label (b : Baseline) : Fin 4 :=
  ⟨(∑ i : Block, (owner (b i)).val) % 4, Nat.mod_lt _ (by decide)⟩


@[simp] theorem mem_zeroSlots {b : Baseline} {i : Block} :
    i ∈ zeroSlots b ↔ b i = 0 := by
  simp [zeroSlots]

@[simp] theorem mem_highSlots {b : Baseline} {i : Block} :
    i ∈ highSlots b ↔ high (b i) = true := by
  simp [highSlots]

theorem bestTail_spec {b : Baseline} {allowed : Block → Bool} {i : Block}
    (h : bestTail b allowed = some i) :
    allowed i = true ∧ tail (b i) = true ∧
      ∀ j, allowed j = true → tail (b j) = true → tailPriority b j ≤ tailPriority b i := by
  have htest := List.find?_some h
  simp only [Bool.and_eq_true] at htest
  refine ⟨htest.1.1, htest.1.2, ?_⟩
  intro j hj ht
  have hmax := List.all_eq_true.mp htest.2 j (List.mem_finRange j)
  simpa [hj, ht] using hmax

theorem highArrow_mem {j i : Block} {S : Finset Block} (h : highArrow j S = some i) :
    i ∈ S := by
  unfold highArrow at h
  cases hs : (insert j S).sort with
  | nil => simp [hs] at h
  | cons a l =>
    cases l with
    | nil => simp [hs] at h
    | cons b l =>
      cases l with
      | nil => simp [hs] at h
      | cons c l =>
        have hnodup := (insert j S).sort_nodup (· ≤ ·)
        rw [hs] at hnodup
        have ha : a ∈ insert j S := by
          rw [← Finset.mem_sort (· ≤ ·), hs]
          simp
        have hc : c ∈ insert j S := by
          rw [← Finset.mem_sort (· ≤ ·), hs]
          simp
        rw [hs] at h
        by_cases hja : j = a
        · simp [hja] at h
        · by_cases hjb : j = b
          · have hci : c = i := by
              change (if j = a then none else if j = b then some c else some a) = some i at h
              rw [ite_eq_right hja, ite_eq_left hjb] at h
              exact Option.some.inj h
            have hbc : b ≠ c := by
              intro heq
              exact (List.nodup_cons.mp (List.nodup_cons.mp hnodup).2).1 (by simp [heq])
            exact hci ▸ ((Finset.mem_insert.mp hc).resolve_left (by rw [hjb]; exact Ne.symm hbc))
          · have hai : a = i := by simpa [hja, hjb] using h
            exact hai ▸ ((Finset.mem_insert.mp ha).resolve_left (Ne.symm hja))

theorem highArrow_no_reverse {i j : Block} {R : Finset Block} (hij : i ≠ j)
    (h : highArrow j (insert i R) = some i) :
    highArrow i (insert j R) ≠ some j := by
  unfold highArrow at h ⊢
  rw [Finset.insert_comm i j]
  cases hs : (insert j (insert i R)).sort with
  | nil => simp [hs] at h
  | cons a l =>
    cases l with
    | nil => simp [hs] at h
    | cons b l =>
      cases l with
      | nil => simp [hs] at h
      | cons c l =>
        have hnodup := (insert j (insert i R)).sort_nodup (· ≤ ·)
        rw [hs] at hnodup
        have hac : a ≠ c := by
          intro heq
          exact (List.nodup_cons.mp hnodup).1 (by simp [heq])
        have hbc : b ≠ c := by
          intro heq
          exact (List.nodup_cons.mp (List.nodup_cons.mp hnodup).2).1 (by simp [heq])
        rw [hs] at h
        by_cases hja : j = a
        · simp [hja] at h
        · by_cases hjb : j = b
          · have hci : c = i := by
              change (if j = a then none else if j = b then some c else some a) = some i at h
              rw [ite_eq_right hja, ite_eq_left hjb] at h
              exact Option.some.inj h
            subst i
            subst j
            simp [hbc.symm, hac.symm, Ne.symm hja]
          · have hai : a = i := by simpa [hja, hjb] using h
            subst i
            simp

theorem selectedFlip_high_or_tail {b : Baseline} {i : Block}
    (h : selectedFlip b = some i) : high (b i) = true ∨ tail (b i) = true := by
  unfold selectedFlip at h
  cases hz : (zeroSlots b).sort with
  | nil =>
    cases hh : (highSlots b).sort with
    | nil =>
      exact Or.inr (bestTail_spec (by simpa [hz, hh] using h)).2.1
    | cons r rs =>
      have hri : r = i := by simpa [hz, hh] using h
      subst i
      apply Or.inl
      apply mem_highSlots.mp
      rw [← Finset.mem_sort (· ≤ ·), hh]
      simp
  | cons j js =>
    cases js with
    | nil =>
      cases hh : (highSlots b).sort with
      | nil =>
        have he : highSlots b = ∅ := by
          have he := congrArg List.toFinset hh
          simpa using he
        simp [hz, highArrow, he] at h
      | cons r rs =>
        cases rs with
        | nil =>
          by_cases hr : r < j
          · exact Or.inr (bestTail_spec (by simpa [hz, hh, hr] using h)).2.1
          · simp [hz, hh, hr] at h
        | cons s ss =>
          exact Or.inl (mem_highSlots.mp (highArrow_mem (by simpa [hz, hh] using h)))
    | cons j' js => simp [hz] at h

theorem selectedFlip_eligible {b : Baseline} {i : Block}
    (h : selectedFlip b = some i) : eligible (b i) = true := by
  rcases selectedFlip_high_or_tail h with hh | ht
  · simp only [high, Bool.and_eq_true] at hh
    exact hh.1
  · simp only [tail, Bool.and_eq_true] at ht
    exact ht.1

theorem selectedFlip_ne_zero {b : Baseline} {i : Block}
    (h : selectedFlip b = some i) : b i ≠ 0 := by
  intro hz
  have he := selectedFlip_eligible h
  simp [hz] at he

theorem selectedFlip_zeroSlots_card {b : Baseline} {i : Block}
    (h : selectedFlip b = some i) : (zeroSlots b).card ≤ 1 := by
  rw [← Finset.length_sort (s := zeroSlots b) (· ≤ ·)]
  unfold selectedFlip at h
  cases hz : (zeroSlots b).sort with
  | nil => simp
  | cons j js =>
    cases js with
    | nil => simp
    | cons j' js => simp [hz] at h

@[simp] theorem flip_inl (b : Baseline) : flip (.inl b) = none := rfl

@[simp] theorem flip_inr (b : {b : Baseline // (selectedFlip b).isSome}) :
    flip (.inr b) = selectedFlip b.val := rfl

@[simp] theorem parent_inl (b : Baseline) : parent (.inl b) = b := rfl

@[simp] theorem parent_inr (b : {b : Baseline // (selectedFlip b).isSome}) :
    parent (.inr b) = b.val := rfl

theorem lightCenter_of_selectedFlip {b : Baseline} {i : Block}
    (h : selectedFlip b = some i) : lightCenter b = Function.update b i 0 := by
  simp [lightCenter, h]

@[simp] theorem mem_poolSites {b : Baseline} {i : Block} {row : Fin 4} {s : Slot} :
    s ∈ poolSites b i row ↔ owner s = row ∧ selectedFlip (Function.update b i s) = some i := by
  simp [poolSites]

end SharpOC.Witness1387
