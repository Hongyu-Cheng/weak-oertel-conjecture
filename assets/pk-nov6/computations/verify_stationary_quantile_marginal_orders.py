import sympy as s

z = [-1, 0, 1]
families = [
    ([s.Integer(2), s.Integer(8), s.Integer(2)], [1, 2, 1], [1, 1, 1], [2, 4, 2], s.Rational(1, 3)),
    ([s.Integer(2)] * 3, [s.Rational(1, 2), s.Integer(1), s.sqrt(7) / 2], [1, 1, s.sqrt(7)], [1, 2, 1], s.Rational(2, 3)),
]
for w, c, beta, area, expected in families:
    assert sum(i * v for i, v in zip(z, w)) == 0
    assert sum(i * v for i, v in zip(z, area)) == 0
    assert all(s.simplify(2 * s.sympify(cc) / bb - aa) == 0 for cc, bb, aa in zip(c, beta, area))
    assert s.Rational(1, 1) * sum(i * i * v for i, v in zip(z, w)) / sum(w) == expected
    assert s.Rational(1, 1) * sum(i * i * v for i, v in zip(z, area)) / sum(area) == s.Rational(1, 2)
    assert s.simplify(sum(cc * cc for cc in c) - sum(w) / 2) == 0

t = s.symbols('t', real=True)
moment = s.integrate(2 * t * (1 - t), (t, 0, 1)) + s.integrate(2 * t * (-1 + s.sqrt(2 - t*t)), (t, 1, s.sqrt(2)))
assert s.simplify(moment) == 0
assert 800 > 729
assert 56700 > 50176
for (w, c, beta, area, expected), volheight, secheight in zip(families, [10*s.sqrt(2)/9, 2*s.sqrt(2)/3], [s.Rational(3, 2), (5+s.sqrt(7))/8]):
    assert s.simplify(s.Rational(2, 3) * sum(ww**s.Rational(3, 2) for ww in w) / sum(w) - volheight) == 0
    assert s.simplify(sum(s.sympify(aa)*cc for aa, cc in zip(area, c)) / sum(area) - secheight) == 0
for i, c in zip(z, families[1][1]):
    U = 1 - c if c <= 1 else -1 + s.sqrt(2 - c*c)
    assert s.simplify(s.Rational(i, 2) + U) == 0
z5 = [-2, -1, 0, 1, 2]
R = [s.Rational(1, 10), 1, 1, 1, s.Rational(1, 10)]
h = [0, -s.Rational(9, 20), 0, s.Rational(9, 20), 0]
A = [rr+hh for rr, hh in zip(R, h)]
B = [rr-hh for rr, hh in zip(R, h)]
assert all(v[j-1]-2*v[j]+v[j+1] <= 0 for v in (A, B) for j in range(1, 4))
w5 = [2*s.sympify(rr)**2 for rr in R]
a5 = [2*(rr-abs(hh)) for rr, hh in zip(R, h)]
c5 = [s.Rational(1, 10), s.Rational(11, 20), 1, s.sqrt(679)/20, s.Rational(1, 10)]
beta5 = [1, 1, 1, s.sqrt(679)/11, 1]
assert all(s.simplify(2*s.sympify(cc)/bb-aa)==0 for cc, bb, aa in zip(c5, beta5, a5))
assert sum(w5)==s.Rational(151, 25) and sum(a5)==s.Rational(23, 5)
for values, expected in [(list(map(abs,z5)),s.Rational(81,3473)),([max(abs(i)-1,0)for i in z5],-s.Rational(279,3473))]:
    assert s.simplify(sum(v*ww for v,ww in zip(values,w5))/sum(w5)-sum(v*aa for v,aa in zip(values,a5))/sum(a5)-expected)==0
print('PASS: opposite exact marginal convex-order obstructions and quantile moment identities')
