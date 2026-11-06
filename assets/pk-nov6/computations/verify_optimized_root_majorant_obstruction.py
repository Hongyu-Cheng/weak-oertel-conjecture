from fractions import Fraction as F

# Exact constants in the analytic q=1 obstruction; no optimizer sampling.
a, b = F(2), F(3)
gamma, c = F(1, 2), F(1, 2)
mass = b + 2 * a
def objective(values):
    return sum(max(F(0), w-c*l) for w, l in zip((a,b,a), values))
assert mass == 7
assert objective((3,3,3)) == F(5,2)
assert objective((2,3,4)) == F(5,2)
assert objective((4,3,2)) == F(5,2)
assert F(5,2)/(gamma*mass) == F(5,7)
assert F(5,4) < F(3,2) < gamma*mass/2 == F(7,4)
budget = F(3,2)
assert gamma*max(a,b) == budget
assert sum(max(F(0), w-budget) for w in (a,b,a)) == F(5,2) <= 2*budget

# A second exact all-q-formula calibration, now q=2.
q, a, b = 2, F(1), F(2)
gamma = F(q,q+1)**q
c = 1-gamma
balanced = 2*max(F(0), a**q-c*b**q)
endpoint = gamma*a**q + max(F(0), a**q-c*(2*b-a)**q)
optimum = gamma*b**q + max(balanced, endpoint)
assert balanced == 0 and endpoint == F(4,9)
assert optimum == F(20,9)
assert optimum < gamma*(b**q+2*a**q) == F(8,3)
assert sum(max(F(0),w-c*l**q)
           for w,l in zip((a**q,b**q,a**q),(a,b,2*b-a))) == optimum
print('PASS: exact optimized-majorant obstruction constants and relaxation')
