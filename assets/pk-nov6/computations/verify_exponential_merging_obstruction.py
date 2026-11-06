"""Exact certificate; no floating-point or external packages."""
from fractions import Fraction as F

def race_probability(x, y):
    """P(sum Exp(mean x_i) >= sum Exp(mean y_j)), by memorylessness."""
    p, q = len(x), len(y)
    table = [[F(0) for _ in range(q + 1)] for _ in range(p + 1)]
    for i in range(p):
        table[i][q] = F(1)
    for i in range(p - 1, -1, -1):
        for j in range(q - 1, -1, -1):
            table[i][j] = (y[j] * table[i + 1][j]
                           + x[i] * table[i][j + 1]) / (x[i] + y[j])
    return table[0][0]

def erlang_two_comparison(x):
    laplace = F(1)
    logarithmic_derivative = F(0)
    for a in x:
        laplace /= 1 + 2*a
        logarithmic_derivative += a/(1 + 2*a)
    return 1-laplace*(1+2*logarithmic_derivative)

x = [F(1,20), F(1,20), F(18,20)]
merged = [F(2,20), F(18,20)]
y = [F(1,2), F(1,2)]
p = race_probability(x,y)
pm = race_probability(merged,y)
assert p == erlang_two_comparison(x) == F(30094,65219)
assert pm == erlang_two_comparison(merged) == F(407,882)
assert p-pm == F(-25,1173942)
assert p > F(4,9) and pm > F(4,9)
print('PASS: arbitrary merging increases the probability by', pm-p)
