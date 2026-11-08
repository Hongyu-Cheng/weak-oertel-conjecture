import Mathlib.Data.Finset.Powerset
import Mathlib.Data.Fintype.Sum
import Mathlib.Tactic

/-! Finite site counts and exact volume comparisons for the signed selector construction. -/

namespace SharpOC.Selector

abbrev Coordinate := Fin 11 ⊕ Fin 3

def heavyMasks : Finset (Finset Coordinate) := Finset.univ.powerset.erase ∅
def lightMasks : Finset (Finset (Fin 11)) := Finset.univ.powersetCard 5
def lightSites : Finset (Fin 3 × Finset (Fin 11)) := Finset.univ.product lightMasks

@[simp] theorem mem_heavyMasks (S : Finset Coordinate) : S ∈ heavyMasks ↔ S.Nonempty := by
  simp [heavyMasks, Finset.nonempty_iff_ne_empty]

@[simp] theorem mem_lightMasks (J : Finset (Fin 11)) : J ∈ lightMasks ↔ J.card = 5 := by
  simp [lightMasks, Finset.mem_powersetCard]

@[simp] theorem mem_lightSites (j : Fin 3) (J : Finset (Fin 11)) :
    (j, J) ∈ lightSites ↔ J.card = 5 := by
  simp [lightSites]

theorem coordinate_card : Fintype.card Coordinate = 14 := by norm_num [Coordinate]

theorem heavyMasks_card : heavyMasks.card = 2 ^ 14 - 1 := by
  have he : (∅ : Finset Coordinate) ∈ Finset.univ.powerset := by simp
  rw [heavyMasks, Finset.card_erase_of_mem he, Finset.card_powerset, Finset.card_univ,
    coordinate_card]

theorem lightMasks_card : lightMasks.card = Nat.choose 11 5 := by
  simp [lightMasks, Finset.card_powersetCard]

theorem lightSites_card : lightSites.card = 3 * Nat.choose 11 5 := by
  simp [lightSites, Finset.card_product, lightMasks_card]

theorem choose_count : Nat.choose 11 5 = 462 := by decide

noncomputable section

def a : ℝ := 2 / 3
def delta : ℝ := 69 / 100
def beta : ℝ := 1 / ((1 + a) * (2 - a))
def gamma : ℝ := (5 / 6) ^ 5
def heavyMass : ℝ := a / (3 * (1 + a)) * (1 + delta) ^ 5
def lightMass : ℝ := (2 / 3 - beta) * (1 - delta) ^ 5
def rowLightMass : ℝ := (Nat.choose 11 5 : ℝ) * lightMass
def totalMass : ℝ := ((2 : ℝ) ^ 14 - 1) * heavyMass + 1 + 3 * rowLightMass

theorem heavyMass_pos : 0 < heavyMass := by norm_num [heavyMass, a, delta]
theorem lightMass_pos : 0 < lightMass := by norm_num [lightMass, beta, a, delta]
theorem gamma_pos : 0 < gamma := by norm_num [gamma]
theorem totalMass_pos : 0 < totalMass := by
  norm_num [totalMass, rowLightMass, heavyMass, lightMass, beta, a, delta, choose_count]

theorem mass_margin : (21 / 1000 : ℝ) < 1 + 3 * rowLightMass - heavyMass := by
  norm_num [rowLightMass, heavyMass, lightMass, beta, a, delta, choose_count]

theorem cap_margin : (2 / 1000 : ℝ) < gamma * heavyMass - beta - rowLightMass := by
  norm_num [gamma, rowLightMass, heavyMass, lightMass, beta, a, delta, choose_count]

theorem cap_slack : beta + rowLightMass < gamma * heavyMass := by
  have h := cap_margin
  linarith

theorem scalar_depth_bound : gamma * heavyMass / totalMass < gamma / (2 : ℝ) ^ 14 := by
  have htotal : (2 : ℝ) ^ 14 * heavyMass < totalMass := by
    have h := mass_margin
    norm_num [totalMass] at h ⊢
    linarith
  apply (div_lt_div_iff₀ totalMass_pos (by positivity)).2
  calc
    gamma * heavyMass * (2 : ℝ) ^ 14 = gamma * ((2 : ℝ) ^ 14 * heavyMass) := by ring
    _ < gamma * totalMass := mul_lt_mul_of_pos_left htotal gamma_pos

theorem uniform_depth_bound :
    max (beta + rowLightMass) (gamma * heavyMass) / totalMass < gamma / (2 : ℝ) ^ 14 := by
  rw [max_eq_right cap_slack.le]
  exact scalar_depth_bound

end
end SharpOC.Selector
