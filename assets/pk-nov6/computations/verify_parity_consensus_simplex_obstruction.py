from fractions import Fraction as F

beta=F(199,1000)
q=F(199,100)
r=F(1,100)
m=q**-4
a=F(1,199**4)
assert q+r==2
assert 0<m<beta*(1-beta)**3
assert r**4*m==a
assert q**4*m==1
assert 0<a<F(1,1000)
gL=4*beta/5
h=(F(1,5)+2*a*gL)/(1+2*a)
assert h==F(1,5)-F(51,625)*a/(1+2*a)
assert h>beta
assert r*beta-(1-q)*beta==beta
assert q*beta+(1-q)*beta==beta
assert F(51,125)*F(1001,1000)**3<F(1,2)
gamma=F(4,5)**4
assert (1-h)**4<gamma*(1+a/2)
assert gamma<gamma*(1+a/2)
assert (1-h)**4<gamma*(1+2*a)
am,bm,cm=a,F(1),F(1)
for _ in range(7):
    assert cm-am==1-a
    assert am+bm+cm==2+a
    an=am**2/(am+cm)
    bn=bm+2*am*cm/(am+cm)
    cn=cm**2/(am+cm)
    assert an<=am/2
    am,bm,cm=an,bn,cn
print('PASS: all algebraic defining comparisons, both strict cap certificates, and consensus recurrence invariants')
