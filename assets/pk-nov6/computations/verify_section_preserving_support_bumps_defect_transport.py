"""Exact support-bump calibration and full-circuit response algebra."""
import sympy as s
from fractions import Fraction as F

checks=0
p,t,z=s.symbols('p t z',real=True)
psi=s.cos(6*p)**4
curvature=psi+s.diff(psi,p,2)
assert s.simplify(curvature-(432*s.cos(6*p)**2-575*s.cos(6*p)**4))==0
assert s.expand((432*z-575*z*z)+143-(1-z)*(575*z+143))==0
checks+=2
limits=(p,-s.pi/12,s.pi/12)
I=s.integrate(psi,limits)
I2=s.integrate(psi**2,limits)
Ip=s.integrate(s.diff(psi,p)**2,limits)
assert I==s.pi/16 and I2==35*s.pi/768 and Ip==15*s.pi/4
checks+=3
V=s.pi+t*I+t*t*(I2-Ip)/2
DV=V-s.pi
assert s.expand(DV-(s.pi*t/16-2845*s.pi*t*t/1536))==0
Phi=(3*s.pi/2+DV)/(3*V)
assert s.factor(Phi-(s.Rational(1,2)-DV/(6*V)))==0
assert s.diff(Phi,t).subs(t,0)==-s.Rational(1,96)
checks+=3
for k in range(1,101):
    tt=F(k,100000)
    assert 1-143*tt>0
    assert tt/F(16)-F(2845,1536)*tt*tt>0
    assert 25*tt<=F(1,40)<F(1,4)
    checks+=3

# Full minimal circuit with unit directions e_i and -ones/sqrt(d),
# coareas 1,...,1,sqrt(d), weights all 1/(d+1). The Jacobian has
# exact rational entries after multiplying each unit normal by coarea.
for d in range(2,13):
    rows=[]
    for i in range(d):
        rows.append([-int(i==j) for j in range(d)]+[-1])
    rows.append([1]*d+[-1])
    A=s.Matrix(rows)
    assert A.det()!=0
    checks+=1
    for pattern in ([1]+[0]*d,[0]*d+[1],[int(j%2==0) for j in range(d+1)]):
        # A*(y',q')=-indicator*V', using V'=1.
        sol=A.inv()*(-s.Matrix(pattern))
        expected=s.Rational(sum(pattern),d+1)
        assert sol[-1]==expected
        checks+=1

print(f'{checks} exact symbolic/rational checks PASS')
