import Mathlib.Tactic

/-!
# Exact constants of the rational counterexample

These lemmas verify only the numerical and scalar parts of the construction.
They do not assert that the prescribed convex body has the required fibers.
No native evaluation or new axiom is used.
-/

namespace SharpOC

noncomputable section

def contraction : ℝ := 103 / 104
def gamma : ℝ := (23 / 24) ^ 23
def massRatio : ℝ := (8192 / 6561) * contraction ^ 23
def gap : ℝ := 1 / 4992
def tilt : ℝ := 1 / 5000
def copies : ℕ := 10000 ^ 23
def integerDimension : ℕ := 3 * copies

theorem contraction_pos : 0 < contraction := by norm_num [contraction]
theorem contraction_lt_one : contraction < 1 := by norm_num [contraction]
theorem gamma_pos : 0 < gamma := by norm_num [gamma]
theorem gamma_lt_one : gamma < 1 := by norm_num [gamma]
theorem massRatio_pos : 0 < massRatio := by norm_num [massRatio, contraction]
theorem massRatio_lt_one : massRatio < 1 := by norm_num [massRatio, contraction]
theorem three_eighths_lt_gamma_massRatio : (3 : ℝ) / 8 < gamma * massRatio := by
  norm_num [gamma, massRatio, contraction]

theorem source_volume_coefficient :
    (2 : ℝ)^23 * contraction^23 / (6^8) = 4 * massRatio := by
  norm_num [massRatio]
  ring

theorem copies_eq : copies = 10^92 := by norm_num [copies]
theorem integerDimension_eq : integerDimension = 3 * 10^92 := by
  rw [integerDimension, copies_eq]

theorem tilt_lt_gap : tilt < gap := by norm_num [tilt, gap]
theorem gap_difference : gap - tilt = (1 : ℝ) / 3120000 := by
  norm_num [tilt, gap]
theorem gap_eq : gap = (1 - contraction) / 48 := by norm_num [gap, contraction]
theorem gap_pos : 0 < gap := by norm_num [gap]
theorem gap_le_one_fortyeighth : gap ≤ (1 : ℝ) / 48 := by norm_num [gap]

theorem origin_coordinate_margin :
    0 < (1 - contraction) / 72 - (1 : ℝ) / 480000 := by norm_num [contraction]
theorem inner_coordinate_margin :
    (1 : ℝ) / 120000 < contraction / 72 := by norm_num [contraction]
theorem inner_cut_margin : tilt < contraction / 48 := by norm_num [tilt, contraction]

theorem unpaid_cut_negative (k : ℕ) (hk : 1 ≤ k) :
    -2 * gap - ((k : ℝ) - 1) / 48 + (k : ℝ) * tilt < 0 := by
  have hk' : (1 : ℝ) ≤ k := by exact_mod_cast hk
  norm_num [gap, tilt]
  linarith

theorem paid_cut_negative (k n : ℕ) (hkn : k ≤ n) :
    (k : ℝ) + 1 - 3 * ((n : ℝ) + 1) + ((k : ℝ) - 1) * tilt < 0 := by
  have hkn' : (k : ℝ) ≤ n := by exact_mod_cast hkn
  have hn : (0 : ℝ) ≤ n := by positivity
  norm_num [tilt]
  linarith

theorem middle_mass_below_cap (b : ℝ) (hb : 0 < b) :
    3 * b / 2 < gamma * (4 * b * massRatio) := by
  have h := mul_lt_mul_of_pos_right three_eighths_lt_gamma_massRatio (show 0 < 4*b by positivity)
  nlinarith

/-- The final strict depth comparison, once the geometric mass bound is proved. -/
theorem strict_depth_ratio (n : ℕ) (b : ℝ) (hb : 0 < b) :
    let M := 4*b*massRatio
    let W := (2 : ℝ)^n*M + (4*b-M)
    0 < W ∧ gamma*M/W < gamma/(2 : ℝ)^n := by
  dsimp
  have hm : 0 < 4*b*massRatio := mul_pos (by positivity) massRatio_pos
  have he : 0 < 4*b - 4*b*massRatio := by
    have h := mul_lt_mul_of_pos_left massRatio_lt_one (show 0 < 4*b by positivity)
    nlinarith
  have hp : 0 < (2 : ℝ)^n := by positivity
  have hw : 0 < (2 : ℝ)^n*(4*b*massRatio) + (4*b-4*b*massRatio) := by positivity
  refine ⟨hw, (div_lt_div_iff₀ hw hp).2 ?_⟩
  have h := mul_pos gamma_pos he
  nlinarith

end
end SharpOC
