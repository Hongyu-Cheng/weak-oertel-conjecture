"""Exact full-space contact transport and forced positive-volume ties.

Analytic separation/coupling existence is proved in the companion note;
this verifier checks the actual rational family and continuous hinge data.
"""
from fractions import Fraction as F
from itertools import product

checks = 0
P = list(product(range(-1, 3), range(-1, 2)))
q = lambda z: 2*z[0]+z[1]-1
ell = lambda z: 5-abs(q(z))
reflect = lambda z: (1-z[0], -z[1])
V = dict(zip(P, (F(v, 1230) for v in
    [2,2,2,136,203,270,270,203,136,2,2,2])))
order = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1)]
rows = [dict(zip(order, (F(v,14760) for v in
    [24,12,8,544,609,604,44])))]
rows.append({reflect(z):v for z,v in rows[0].items()})
sources = [(0,0),(1,0)]
assert sum(V.values()) == 1
checks += 1
nu = {z:V[z]/ell(z) for z in P}
for source, row in zip(sources, rows):
    assert sum(row.values()) == F(1,8)
    assert all(sum(m*z[c] for z,m in row.items()) == F(1,8)*source[c]
               for c in range(2))
    assert sum(m*ell(z) for z,m in row.items()) == F(1,2)
    assert all(q(z)<=0 for z in row) if source==(0,0) else all(q(z)>=0 for z in row)
    # Within each target fiber, uniform and all symmetric split pieces
    # have continuous mean exactly zero.
    checks += 4
for z in P:
    assert sum(row.get(z,0) for row in rows) == nu[z] > 0
    checks += 1
assert sum(nu.values()) == F(1,4)
assert sum(ell(z)*nu[z] for z in P) == 1
checks += 2

strict = {z:m for z,m in rows[0].items() if q(z)<0}
assert sum(z[0]*m for z,m in strict.items()) == -F(44,14760)
assert sum(z[1]*m for z,m in strict.items()) == -F(560,14760)
b = -sum(z[0]*m for z,m in strict.items())
a = b-sum(z[1]*m for z,m in strict.items())
assert a==F(604,14760) and b==F(44,14760)
assert a/nu[(0,1)]==F(151,162)
assert b/nu[(1,-1)]==F(11,162)
checks += 5
for z, fraction in [((0,1),F(151,162)),((1,-1),F(11,162))]:
    half=V[z]/2
    assert half==F(9,82)
    # A centered subinterval occupies the desired fraction and both
    # complementary symmetric pieces have zero continuous first moment.
    inner=fraction*half
    assert (2*inner)/ell(z)==rows[0][z]
    assert (2*(half-inner))/ell(z)==rows[1][z]
    first_inner=(inner**2-(-inner)**2)/2
    first_outer=(((-inner)**2-(-half)**2)+(half**2-inner**2))/2
    assert first_inner==first_outer==0
    checks += 4

def hinge_integral(A,b,length):
    """Lebesgue integral of (A+bX)_+ on [-length/2,length/2]."""
    if b==0:
        return length*max(A,0)
    b=abs(b)
    lo=A-b*length/2
    hi=A+b*length/2
    return (max(hi,0)**2-max(lo,0)**2)/(2*b)

for a1,a2,b,c in product(range(-2,3),repeat=4):
    lhs=sum(F(1,8)*max(a1*z[0]+a2*z[1]+c,0) for z in sources)
    rhs=sum(hinge_integral(F(a1*z[0]+a2*z[1]+c),F(b),V[z])/ell(z) for z in P)
    assert lhs<=rhs
    checks += 1

print(f'{checks} exact rational checks PASS, including 625 continuous hinge tests')
