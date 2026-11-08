import Mathlib.Analysis.Complex.ExponentialBounds
import Mathlib.Data.Finset.Interval
import Mathlib.Data.Fintype.Sum
import Mathlib.Tactic

/-! Rational parameters of the separated-sentinel witness. All masses use the
product-simplex volume as their common unit. -/

namespace SharpOC.Witness1387

open scoped BigOperators

def poolSize (k : Fin 16) : ℕ := 55 + k.val

def radiusGrid : ℕ := 100000000000000

def radiusNumerator : Fin 16 → ℕ :=
  ![99747122939317, 99746701695008, 99746285530361, 99745874318052,
    99745467935602, 99745066265133, 99744669193131, 99744276610237,
    99743888411039, 99743504493883, 99743124760694, 99742749116808,
    99742377470814, 99742009734401, 99741645822221, 99741285651757]

def radius (k : Fin 16) : ℚ := radiusNumerator k / (radiusGrid : ℚ)

def tau : ℚ := 3 / 32

def beta : ℚ := 27 / 64

def gamma : ℚ := (1178 / 1179) ^ 1178

def capBound : ℚ := (1175 / 1176) ^ 1175 * tau

def inactiveMassGrid : ℕ := 10000000000000000

def inactiveMass : ℚ := 937501014816724 / (inactiveMassGrid : ℚ)

def lightMass (k : Fin 16) : ℚ := tau * (2 * radius k - 1) ^ 1178

def oldCount (k : ℕ) : ℕ :=
  if k = 55 then (2047 ^ 19 - 1827 ^ 19) / 220
  else if k ≤ 70 then ((2047 - 4 * (k - 1)) ^ 19 - (2047 - 4 * k) ^ 19) / 4
  else 0

def newCount (k : ℕ) : ℕ :=
  if k = 55 then
    ∑ t ∈ Finset.Icc 3 19, (t - 1) * Nat.choose 19 t * 220 ^ (t - 2) * 1827 ^ (19 - t)
  else if k ≤ 70 then
    ∑ m ∈ Finset.Icc 1 17, (m + 1) * 220 * 1827 ^ (17 - m) *
      ((1827 - 4 * (k - 56)) ^ m - (1827 - 4 * (k - 55)) ^ m) / 4
  else 0

def centerCount (k : Fin 16) : ℕ :=
  oldCount (poolSize k) - oldCount (poolSize k + 1) +
    (newCount (poolSize k) - newCount (poolSize k + 1))

def resetCount : ℕ := 19 * 2047 ^ 18 - oldCount 55

def inactiveCount : ℕ := 2048 ^ 19 - 2047 ^ 19 - resetCount - oldCount 55 - newCount 55

def normalizedTotal : ℚ :=
  ((2047 ^ 19 + resetCount : ℕ) : ℚ) * tau + (inactiveCount : ℚ) * inactiveMass +
    ∑ k : Fin 16, (centerCount k : ℚ) *
      (radius k ^ 1178 + 4 * (poolSize k : ℚ) * lightMass k)

def eUpper : ℚ := (∑ j ∈ Finset.range 33, (1 : ℚ) / j.factorial) +
  1 / (32 * (32 : ℕ).factorial)

def activeCapAt (k : Fin 16) (r : ℚ) : ℚ :=
  beta * r ^ 1178 + (poolSize k : ℚ) * (tau * (2 * r - 1) ^ 1178)

set_option maxRecDepth 8192
set_option maxHeartbeats 10000000

theorem radius_half_lt (k : Fin 16) : 1 / 2 < radius k := by
  fin_cases k <;> decide +kernel

theorem radius_lt_one (k : Fin 16) : radius k < 1 := by
  fin_cases k <;> decide +kernel

theorem activeCapAt_strictMonoOn (k : Fin 16) :
    StrictMonoOn (activeCapAt k) (Set.Ici (1 / 2)) := by
  intro x hx y _ hxy
  change (1 / 2 : ℚ) ≤ x at hx
  unfold activeCapAt
  apply add_lt_add_of_lt_of_le
  · exact mul_lt_mul_of_pos_left (pow_lt_pow_left₀ hxy (by linarith) (by decide))
      (by norm_num [beta])
  · apply mul_le_mul_of_nonneg_left _ (by positivity)
    apply mul_le_mul_of_nonneg_left _ (by norm_num [tau])
    exact pow_le_pow_left₀ (by linarith) (by linarith) _

/-- The last passing grid numerator is one more than the chosen numerator. -/
theorem radius_grid_crossing (k : Fin 16) :
    activeCapAt k (radius k + 1 / (radiusGrid : ℚ)) ≤ capBound ∧
      capBound < activeCapAt k (radius k + 2 / (radiusGrid : ℚ)) := by
  fin_cases k <;> decide +kernel

/-- The two grid points bracketing the ratio certify the floor minus one rule. -/
theorem inactive_mass_grid_crossing :
    gamma * (inactiveMass + 1 / (inactiveMassGrid : ℚ)) ≤ capBound ∧
      capBound < gamma * (inactiveMass + 2 / (inactiveMassGrid : ℚ)) := by
  decide +kernel

theorem tau_lt_inactiveMass : tau < inactiveMass := by decide +kernel

theorem capBound_pos : 0 < capBound := by
  unfold capBound tau
  positivity

theorem centerMass_lt_tau (k : Fin 16) : radius k ^ 1178 < tau := by
  fin_cases k <;> decide +kernel

theorem lightMass_lt_capBound (k : Fin 16) : lightMass k < capBound := by
  fin_cases k <;> decide +kernel

theorem activeCap_lt_capBound (k : Fin 16) :
    beta * radius k ^ 1178 + (poolSize k : ℚ) * lightMass k < capBound := by
  fin_cases k <;> decide +kernel

theorem inactiveCap_lt_capBound : gamma * inactiveMass < capBound := by
  decide +kernel

theorem poolCounts_nonincreasing (k : Fin 16) :
    oldCount (poolSize k + 1) ≤ oldCount (poolSize k) ∧
      newCount (poolSize k + 1) ≤ newCount (poolSize k) := by
  fin_cases k <;> decide +kernel

theorem sum_centerCount :
    (∑ k : Fin 16, centerCount k) = oldCount 55 + newCount 55 := by
  decide +kernel

theorem resetCount_pos : 0 < resetCount := by decide +kernel

theorem inactiveCount_pos : 0 < inactiveCount := by decide +kernel

theorem eUpper_pos : 0 < eUpper := by decide +kernel

theorem normalizedTotal_pos : 0 < normalizedTotal := by decide +kernel

theorem strict_raw_margin :
    (capBound + 15 / 10 ^ 11) * (eUpper * (2 : ℚ) ^ 209) < normalizedTotal := by
  decide +kernel

theorem numerical_depth_bound :
    capBound * (2 : ℚ) ^ 209 < (36787944 / 10 ^ 8) * normalizedTotal := by
  decide +kernel

theorem numerical_bound_lt_inv_eUpper : (36787944 / 10 ^ 8 : ℚ) < 1 / eUpper := by
  decide +kernel

theorem exp_one_le_eUpper : Real.exp 1 ≤ (eUpper : ℝ) := by
  have h := Real.exp_bound' (x := 1) (n := 32) (by norm_num) (by norm_num) (by decide)
  simp only [one_pow, one_mul] at h
  rw [eUpper]
  push_cast
  rw [show 33 = 32 + 1 by decide, Finset.sum_range_succ, add_assoc]
  convert h using 1
  norm_num [Nat.factorial]

theorem capBound_lt_target :
    (capBound : ℝ) / (normalizedTotal : ℝ) < 1 / (Real.exp 1 * (2 : ℝ) ^ 209) := by
  have hr : capBound * (eUpper * (2 : ℚ) ^ 209) < normalizedTotal :=
    (mul_lt_mul_of_pos_right (by linarith : capBound < capBound + 15 / 10 ^ 11)
      (mul_pos eUpper_pos (by positivity))).trans strict_raw_margin
  have h : (capBound : ℝ) * ((eUpper : ℝ) * (2 : ℝ) ^ 209) < (normalizedTotal : ℝ) := by
    exact_mod_cast hr
  apply (div_lt_div_iff₀ (by exact_mod_cast normalizedTotal_pos)
    (mul_pos (Real.exp_pos 1) (by positivity))).2
  rw [one_mul]
  exact lt_of_le_of_lt (by
    have hc : 0 ≤ (capBound : ℝ) := by exact_mod_cast capBound_pos.le
    gcongr
    exact exp_one_le_eUpper) h

end SharpOC.Witness1387
