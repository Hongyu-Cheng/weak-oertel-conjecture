"""Exact scalar certificates; geometric and all-normal proofs are in the note."""
import sympy as S

v = S.symbols('v', real=True)
c = S.Rational(77, 100)
gamma = S.Rational(27, 64)
q1 = 1 - c**3 / (1-v**2)**2
q2 = (1+v-S.Rational(3, 2)*c+c**3/(2*(1+v)**2))/(2*v)
assert S.factor((q1-q2).subs(v, 1-c)) == 0
assert S.factor(q1.subs(v, 1-c)-gamma) == S.Rational(66973, 968256)
polynomial = S.cancel(4*v*(1+v)**2*(q2-gamma))
expected = (S.Rational(5, 16)*v**3+S.Rational(63, 200)*v**2
            -S.Rational(123, 400)*v+S.Rational(146533, 1000000))
assert S.expand(polynomial-expected) == 0
quadratic = expected-S.Rational(5, 16)*v**3
assert S.discriminant(quadratic, v) == -S.Rational(9007533, 100000000)
assert S.diff(q1, v) == -4*c**3*v/(1-v**2)**3
assert c**3-gamma == S.Rational(17329, 500000)
assert 2*c**3 < 1
paired = 1-(2*c-1)**3
assert paired == S.Rational(105317, 125000)
assert 2*gamma-paired == S.Rational(607, 500000)
assert 2*gamma-paired-3*S.Rational(1, 10000) == S.Rational(457, 500000)

# Exact interval checks of the complete fixed-normal minimization formula.
# Here the centered body is [-1,1]; no numerical optimization is used.
def tail(s):
    return min(S.Integer(1), max(S.Integer(0), (1-s)/2))

count = 0
for numerator in range(-8, 9):
    s = S.Rational(numerator, 4)
    floor = 2*tail(s) if s >= 0 else S.Integer(1)
    for shift in range(-16, 17):
        t = S.Rational(shift, 4)
        assert tail(s+t)+tail(s-t) >= floor
        count += 1
    attaining_shift = S.Integer(0) if s >= 0 else S.Integer(4)
    assert tail(s+attaining_shift)+tail(s-attaining_shift) == floor
print(f'PASS: exact pyramid polynomials, all rational gaps, and {count} interval pair checks')
