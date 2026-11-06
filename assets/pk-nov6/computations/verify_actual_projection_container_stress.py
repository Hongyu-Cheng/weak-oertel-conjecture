"""Exact relative-volume identities and positive boundary-fiber masses."""
from fractions import Fraction as Q
import sympy as s

eps=s.symbols('eps', positive=True)
area=1-2*eps**2
outer=2-4*eps
new=4*eps*(1-eps)
assert s.simplify(2*area-new-outer)==0
assert area.subs(eps,s.Rational(3,10))==s.Rational(41,50)
assert s.diff(area,eps).subs(eps,0)==0
assert outer.subs(eps,0)==2

q=(Q(1,2),Q(1,2))
faces=[((-1,0),(Q(0),Q(1,2))),((1,0),(Q(1),Q(1,2))),
       ((0,-1),(Q(1,2),Q(0))),((0,1),(Q(1,2),Q(1)))]
assert tuple(sum(n[j] for n,c in faces) for j in range(2))==(0,0)
matrix=[[sum(n[i]*(c[j]-q[j]) for n,c in faces) for j in range(2)]
        for i in range(2)]
assert matrix==[[1,0],[0,1]]
assert sum(sum(n[j]*(c[j]-q[j]) for j in range(2)) for n,c in faces)==2

vertices=[(0,0),(0,1),(1,0),(1,1)]
def dist_affine(v,z):
    return sum((1-v[j])*z[j]+v[j]*(1-z[j]) for j in range(2))
for e in (Q(1,100),Q(1,10),Q(3,10)):
    assert not any(all(dist_affine(v,z)>=e for v in vertices) for z in vertices)
    for v in vertices:
        assert sum(2 for z in vertices if dist_affine(v,z)<e)==2

M=Q(8)
alpha=Q(1,5)
assert Q(4)==M/2 > 2*alpha*M
assert Q(2)/M > alpha
assert sum(2 for z in vertices)==M
print('PASS: exact relative Euler identity, complete outer stress, and nonvanishing boundary-fiber jumps')
