import Mathlib

/-! Exact parameters and scalar certificates for the 76-coordinate counterexample.
All numerical certificates are checked by Lean's kernel. -/

noncomputable section
namespace SharpOC.BoxParameters

def epsilon : ℝ := 1 / 10000000000
def s : ℝ := 5000001 / 10000000
def t : ℝ := 9999997 / 10000000
def eta : ℝ := 3999999 / 4000000
def q : ℝ := 500001 / 1000000
def u : ℝ := 2 * (1 - q)
def h : ℕ := 1372128
def ell : ℕ := 2 ^ 93
def theta : ℝ := 3 / 32
def m : ℝ := (2 * s)^3 * theta * (2 * q)^h
def alpha : ℝ := t^3 * theta * u^h
def eUpper : ℝ := 27182819 / 10000000
def continuousDimension : ℕ := 3 + h + ell

theorem epsilon_pos : 0 < epsilon := by norm_num [epsilon]
theorem epsilon_lt_quarter : epsilon < 1/4 := by norm_num [epsilon]
theorem s_pos : 0 < s := by norm_num [s]
theorem half_lt_s : 1/2 < s := by norm_num [s]
theorem s_lt_one : s < 1 := by norm_num [s]
theorem t_pos : 0 < t := by norm_num [t]
theorem t_lt_eta : t < eta := by norm_num [t, eta]
theorem eta_pos : 0 < eta := lt_trans t_pos t_lt_eta
theorem eta_lt_two_sub_two_s : eta < 2 * (1-s) := by norm_num [eta,s]
theorem eta_lt_one : eta < 1 := by norm_num [eta]
theorem q_pos : 0 < q := by norm_num [q]
theorem half_lt_q : 1/2 < q := by norm_num [q]
theorem q_lt_one : q < 1 := by norm_num [q]
theorem u_pos : 0 < u := by norm_num [u,q]
theorem u_lt_two_q : u < 2*q := by norm_num [u,q]
theorem h_pos : 0 < h := by norm_num [h]
theorem ell_pos : 0 < ell := by unfold ell; positivity
theorem theta_pos : 0 < theta := by norm_num [theta]
theorem m_pos : 0 < m := by
  have := s_pos; have := q_pos; have := theta_pos
  unfold m
  positivity
theorem alpha_pos : 0 < alpha := by
  have := t_pos; have := u_pos; have := theta_pos
  unfold alpha
  positivity
theorem mixed_type_margin :
    2 * ((1/4 + 3*epsilon)/(1/4-epsilon)) * t < 3-2*s := by
  norm_num [epsilon,t,s]
theorem mixed_type_margin_mul :
    2 * (1/4 + 3*epsilon) * t ≤ (3-2*s)*(1/4-epsilon) := by
  norm_num [epsilon,t,s]
theorem exp_one_lt_eUpper : Real.exp 1 < eUpper :=
  lt_trans Real.exp_one_lt_d9 (by norm_num [eUpper])

end SharpOC.BoxParameters
