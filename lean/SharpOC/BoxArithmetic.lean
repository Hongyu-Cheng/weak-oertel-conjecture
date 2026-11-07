import SharpOC.BoxPowerCertificates

/-! Exact volume inequalities and the finite simplex-padding comparison. -/
noncomputable section
namespace SharpOC.BoxParameters

theorem m_bounds : (1458094201550/10^12 : ℝ) < m ∧ m < 1458094201551/10^12 := by
  have hc : (2*s)^3*theta = (375000225000045000003/4000000000000000000000 : ℝ) := by
    norm_num [s,theta]
  have hq : 2*q = (500001/500000 : ℝ) := by norm_num [q]
  rw [m,h,hq,hc]
  constructor
  · calc
      _ < (375000225000045000003/4000000000000000000000 : ℝ) *
          (15552995484735130232184183374589/1000000000000000000000000000000) := by norm_num
      _ ≤ _ := mul_le_mul_of_nonneg_left growth_power_bounds.1 (by norm_num)
  · calc
      _ ≤ (375000225000045000003/4000000000000000000000 : ℝ) *
          (777649774236756511609209419441/50000000000000000000000000000) :=
        mul_le_mul_of_nonneg_left growth_power_bounds.2 (by norm_num)
      _ < _ := by norm_num

theorem alpha_bounds : (6027739233/10^12 : ℝ) < alpha ∧ alpha < 6027739234/10^12 := by
  have hc : t^3*theta = (2999997300000809999919/32000000000000000000000 : ℝ) := by
    norm_num [t,theta]
  have hu : u = (499999/500000 : ℝ) := by norm_num [u,q]
  rw [alpha,h,hu,hc]
  constructor
  · calc
      _ < (2999997300000809999919/32000000000000000000000 : ℝ) *
          (64295943021685503624000143307/1000000000000000000000000000000) := by norm_num
      _ ≤ _ := mul_le_mul_of_nonneg_left decay_power_bounds.1 (by norm_num)
  · calc
      _ ≤ (2999997300000809999919/32000000000000000000000 : ℝ) *
          (32147971510842751812000082061/500000000000000000000000000000) :=
        mul_le_mul_of_nonneg_left decay_power_bounds.2 (by norm_num)
      _ < _ := by norm_num

theorem alpha_lt_m : alpha < m := by
  have hm := m_bounds.1; have ha := alpha_bounds.2
  norm_num at hm ha
  linarith

theorem mass_margin : m / (2:ℝ)^17 < 1+76*alpha-m := by
  have hm := m_bounds.2; have ha := alpha_bounds.1
  norm_num at hm ha ⊢
  linarith

theorem middle_margin : 27/64+19*alpha < m / Real.exp 1 := by
  have hmid : 27/64+19*alpha < m/eUpper := by
    apply (lt_div_iff₀ (show 0 < eUpper by norm_num [eUpper])).mpr
    have hm := m_bounds.1; have ha := alpha_bounds.2
    norm_num [eUpper] at hm ha ⊢
    linarith
  exact lt_trans hmid (div_lt_div_of_pos_left m_pos (Real.exp_pos 1) exp_one_lt_eUpper)

def paddingGamma : ℝ := ((ell : ℝ)/(ell+1))^ell

theorem exp_gamma_bound (k : ℕ) (hk : 0 < k) :
    Real.exp 1 * ((k : ℝ)/(k+1))^k < 1+1/(k:ℝ) := by
  have hk' : (0 : ℝ) < k := Nat.cast_pos.mpr hk
  let y : ℝ := (k : ℝ)/(k+1)
  have hy : 0 < y := div_pos hk' (by positivity)
  have hy1 : y < 1 := (div_lt_one (by positivity)).mpr (by linarith)
  have hlog := Real.log_lt_sub_one_of_pos hy hy1.ne
  have hmul := mul_lt_mul_of_pos_left hlog (show 0 < (k:ℝ)+1 by positivity)
  have hid : ((k:ℝ)+1)*(y-1) = -1 := by dsimp [y]; field_simp <;> ring
  rw [hid] at hmul
  have hcompare : 1 + (k:ℝ)*Real.log y < -Real.log y := by nlinarith
  have he := Real.exp_lt_exp.mpr hcompare
  rw [Real.exp_add,Real.exp_nat_mul,Real.exp_log hy,Real.exp_neg,Real.exp_log hy] at he
  have hinv : y⁻¹ = 1+1/(k:ℝ) := by dsimp [y]; field_simp <;> ring
  rwa [hinv] at he

theorem paddingGamma_pos : 0 < paddingGamma := by
  have he : (0 : ℝ) < ell := Nat.cast_pos.mpr ell_pos
  unfold paddingGamma
  positivity

def normalizedTotal : ℝ := (2:ℝ)^76*m+(1+76*alpha-m)
def uniformNumerator : ℝ := max (27/64+19*alpha) (paddingGamma*m)

theorem normalizedTotal_pos : 0 < normalizedTotal := by
  have hm := m_pos
  have hd := mass_margin
  have hdelta : 0 < 1+76*alpha-m := lt_trans (by positivity) hd
  unfold normalizedTotal
  positivity

theorem uniformNumerator_pos : 0 < uniformNumerator :=
  lt_of_lt_of_le (mul_pos paddingGamma_pos m_pos) (le_max_right _ _)

theorem scalar_depth_bound :
    uniformNumerator/normalizedTotal < 1/(Real.exp 1*(2:ℝ)^76) := by
  have hm := m_pos
  have he := Real.exp_pos 1
  have hp : (0:ℝ) < 2^76 := by positivity
  have hd := mass_margin
  have hW : (2:ℝ)^76*m < normalizedTotal := by
    unfold normalizedTotal
    have : (0:ℝ) < m/2^17 := by positivity
    linarith
  have hmid := (lt_div_iff₀ he).mp middle_margin
  have hmid' : (27/64+19*alpha)*(Real.exp 1*(2:ℝ)^76) < normalizedTotal := by
    have hh := mul_lt_mul_of_pos_right hmid hp
    nlinarith
  have hg := mul_lt_mul_of_pos_right (exp_gamma_bound ell ell_pos) hm
  have hmW : (1+1/(ell:ℝ))*m < normalizedTotal/(2:ℝ)^76 := by
    apply (lt_div_iff₀ hp).mpr
    norm_num [normalizedTotal,ell] at hd ⊢
    linarith
  have hend : paddingGamma*m*(Real.exp 1*(2:ℝ)^76) < normalizedTotal := by
    have hh : Real.exp 1 * paddingGamma*m < normalizedTotal/(2:ℝ)^76 :=
      lt_trans hg hmW
    have hh' := (lt_div_iff₀ hp).mp hh
    nlinarith
  unfold uniformNumerator
  rw [← max_div_div_right (le_of_lt normalizedTotal_pos)]
  apply max_lt
  · exact (div_lt_div_iff₀ normalizedTotal_pos (mul_pos he hp)).mpr (by simpa using hmid')
  · exact (div_lt_div_iff₀ normalizedTotal_pos (mul_pos he hp)).mpr (by simpa using hend)

end SharpOC.BoxParameters
