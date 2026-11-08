import Mathlib.Data.Fintype.Sum
import Mathlib.Data.Fin.VecNotation
import Mathlib.Tactic

/-! Exact rational comparisons for the signed selector in dimension 18. -/

namespace SharpOC.Selector17

noncomputable section

def a : ℝ := 663 / 1000
def delta : ℝ := 664201 / 1000000
def epsilon : ℝ := 13 / 20000
def h : ℝ := 1111946415 / 1000000000

def gamma : ℝ := (5 / 6) ^ 5
def theta : ℝ := a / (3 * (1 + a))
def phi : ℝ := (1 - a) / (3 * (2 - a))
def beta : ℝ := 1 / ((1 + a) * (2 - a))

def L : ℝ := 252 * (theta + phi) * (1 - delta) ^ 5
def V : ℝ := theta + phi * (1 - (1 - epsilon) ^ 5)
def W : ℝ := 3339 * h ^ 5 + 756 * (1 + delta) ^ 5 * V + 1 + 3 * L

def t : Fin 6 → ℝ :=
  ![166735371 / 1000000000, 166735294 / 1000000000, 166324902 / 1000000000,
    166734811 / 1000000000, 166734811 / 1000000000, 166734811 / 1000000000]

def s : Fin 6 → ℝ :=
  ![1 - 3 * (1 - a) / (2 - a) + (1 - a ^ 2) / (a * (2 - a)),
    3 * (1 - a) / (2 - a), -(1 - a ^ 2) / (a * (2 - a)), 0, 0, 0]

def C (i : Fin 6) : ℝ :=
  theta * (1 - t i) ^ 5 +
    if i = 2 then 0 else
      phi * ((1 - t i) ^ 5 - (1 - t i - (1 - s i) * epsilon) ^ 5) / (1 - s i)

theorem a_pos : 0 < a := by norm_num [a]
theorem a_lt_one : a < 1 := by norm_num [a]
theorem delta_pos : 0 < delta := by norm_num [delta]
theorem delta_lt_one : delta < 1 := by norm_num [delta]
theorem epsilon_pos : 0 < epsilon := by norm_num [epsilon]
theorem epsilon_lt_one : epsilon < 1 := by norm_num [epsilon]
theorem h_pos : 0 < h := by norm_num [h]
theorem h_lt_two : h < 2 := by norm_num [h]
theorem h_le_one_add_delta : h ≤ 1 + delta := by norm_num [h, delta]
theorem gamma_pos : 0 < gamma := by norm_num [gamma]
theorem theta_pos : 0 < theta := by norm_num [theta, a]
theorem phi_pos : 0 < phi := by norm_num [phi, a]
theorem beta_pos : 0 < beta := by norm_num [beta, a]

theorem theta_add_phi : theta + phi = 2 / 3 - beta := by
  norm_num [theta, phi, beta, a]

theorem sum_t : ∑ i, t i = 1 := by norm_num [Fin.sum_univ_succ, t]

theorem t_pos (i : Fin 6) : 0 < t i := by fin_cases i <;> norm_num [t]

theorem t_lt_one (i : Fin 6) : t i < 1 := by fin_cases i <;> norm_num [t]

theorem sum_s : ∑ i, s i = 1 := by norm_num [Fin.sum_univ_succ, s, a]

theorem s_v_neg : s 2 < 0 := by norm_num [s, a]

theorem s_nonneg (i : Fin 6) (hi : i ≠ 2) : 0 ≤ s i := by
  revert hi
  fin_cases i <;> norm_num [s, a]

theorem s_lt_one (i : Fin 6) : s i < 1 := by
  fin_cases i <;> norm_num [s, a]

theorem shifted_t_nonneg (i : Fin 6) : 0 ≤ t i - s i * epsilon := by
  fin_cases i <;> norm_num [t, s, a, epsilon]

theorem shifted_complement_nonneg (i : Fin 6) : 0 ≤ 1 - t i - (1 - s i) * epsilon := by
  fin_cases i <;> norm_num [t, s, a, epsilon]

theorem cap_slack : beta + L < gamma * h ^ 5 := by
  norm_num [beta, L, theta, phi, a, delta, gamma, h]

theorem heavy_cap_slack (i : Fin 6) : (1 + delta) ^ 5 * C i < gamma * h ^ 5 := by
  fin_cases i <;> norm_num [delta, C, theta, phi, t, s, epsilon, a, gamma, h]

theorem mass_slack : 4096 * h ^ 5 < W := by
  norm_num [W, V, L, h, delta, theta, phi, a, epsilon]

theorem W_pos : 0 < W := (mul_pos (by norm_num) (pow_pos h_pos 5)).trans mass_slack

theorem scalar_depth_bound : gamma * h ^ 5 / W < gamma / (2 : ℝ) ^ 12 := by
  apply (div_lt_div_iff₀ W_pos (by positivity)).2
  calc
    gamma * h ^ 5 * (2 : ℝ) ^ 12 = gamma * (4096 * h ^ 5) := by ring
    _ < gamma * W := mul_lt_mul_of_pos_left mass_slack gamma_pos

end
end SharpOC.Selector17
