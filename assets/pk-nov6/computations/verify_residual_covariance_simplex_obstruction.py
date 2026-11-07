from fractions import Fraction as F

S0 = [[F(8,144), F(-4,144)], [F(-4,144), F(8,144)]]
S1 = [[F(32,144), F(-4,144)], [F(-4,144), F(2,144)]]
S = [[(S0[i][j]+S1[i][j])/2 for j in range(2)] for i in range(2)]
assert S == [[F(20,144), F(-4,144)], [F(-4,144), F(5,144)]]
assert S[0][0] * S[1][1] - S[0][1]**2 == F(7,1728) > 0
assert S[0][0] / S0[0][0] != S[0][1] / S0[0][1]

c = F(2,9)
cap_shift = [F(2,9), F(-1,9)]
left = [c*x for x in cap_shift]
# Eliminate the square-root normalizing factor exactly:
# Psi Sigma u = c*d Sigma beta / ((d+1)^2 beta^T Sigma beta).
right = [c*F(2,9)*S[j][0]/S[0][0] for j in range(2)]
assert left == [F(4,81), F(-2,81)]
assert right == [F(4,81), F(-4,405)]
assert left[1]-right[1] == F(-2,135)
assert F(2,3)**2 * F(1,2) == c
print('PASS: residual covariance, canonical cap constants, nonzero normal-stress defect')
