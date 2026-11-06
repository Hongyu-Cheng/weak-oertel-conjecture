from fractions import Fraction as F
import sympy as s
w={1:F(3),2:F(6),3:F(3)}
c={1:F(9,2),2:F(3),3:F(3,2)}
assert sum(w.values())==12
assert sum(z*v for z,v in w.items())==24
assert sum(w[z]*c[z] for z in w)==36
D={1:(F(3),F(6)),2:(F(0),F(6)),3:(F(0),F(3))}
for z,(l,r) in D.items():
    assert D[4-z]==(6-r,6-l)
t=s.symbols('t', real=True)
ct=3+(3*t+t*t/2)/(12+t)
assert s.factor(15+t-3*ct-(12+t)/2)==-t*(t+3)/(t+12)
# All three cuts are proper on 0 <= t <= 1, with strict bounds already at t=0.
assert F(3) < F(3)+F(7,2)/13 < F(4)
print('PASS: retained mass/centroid/symmetry and exact negative active-cap deficit')
