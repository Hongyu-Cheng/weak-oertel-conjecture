from fractions import Fraction as F
import sympy as s
checks=0
K=[(F(47,50),F(26,25)),(-F(11,10),F(1)),(-F(23,25),F(23,25)),(-F(9,100),F(9,100))]
V=[hi-lo for lo,hi in K]; M=sum(V); gb=sum(z*V[z] for z in range(4))/M
Sigma=sum(v**3 for v in V)/(12*M)
E1,E2=F(44,21),F(46,25)
bstar=F(14137,108948)
lo,hi=-F(211,317),F(211,316)
def ell(b,z): return 1+b*(z-gb)
assert gb==F(316,211)
assert lo<bstar<hi
assert [ell(bstar,z) for z in range(4)]==[F(21944,27237),F(4853,5188),F(58025,54474),F(130187,108948)]
assert E1*ell(bstar,1)==E2*ell(bstar,2)==F(53383,27237)
assert F(106,211)+2*F(105,211)==gb
checks+=5
for j in range(501):
    b=lo+(hi-lo)*F(j,500)
    L=[ell(b,z) for z in range(4)]
    assert min(L)>=0
    assert L[1]>0 and L[2]>0
    assert sum(V[z]*L[z] for z in range(4))==M
    assert all(L[z]*V[z]<=M for z in range(4))
    products=[E1*L[1],E2*L[2]]
    assert max(products)>=F(53383,27237)
    assert (products[0]>=products[1])==(b<=bstar)
    checks+=6
# Check complete tilted-cap breakpoints at the two original marks.
def clamp(v,w): return max(F(0),min(v,w))
def mass(p,t,delta,sign):
    if sign==1:
        return sum(clamp(ub-(t*(z-p)-delta),ub-lb) for z,(lb,ub) in enumerate(K))
    return sum(clamp(t*(z-p)+delta-lb,ub-lb) for z,(lb,ub) in enumerate(K))
for p in (1,2):
    for sign in (-1,1):
        for j in range(101):
            de=F(j,10**6)
            knots=sorted({(end+sign*de)/(z-p) for z,ends in enumerate(K) if z!=p for end in ends})
            ts=[knots[0]-1]+knots+[knots[-1]+1]
            assert min(mass(p,t,de,sign) for t in ts)==F(11,10)+de
            checks+=1
# Local derivative bounds, exact after squaring, uniformly in normalized ell.
eta=F(1,1000)
for i in (1,2):
    lb,ub=K[i]
    for y in (-eta,eta):
        E=4*(y-lb)*(ub-y)/(ub-lb)
        Ep=-8*(y-(lb+ub)/2)/(ub-lb)
        assert E>1 and abs(Ep)<1
        assert Sigma/(4*V[i])*Ep*Ep/E<F(1,4)
        checks+=2
# Exponent and base-weight alignment algebra.
e,r,n,m,l=s.symbols('e r n m l',positive=True)
a=s.symbols('a',real=True)
assert s.simplify(s.diff((e/m)**r,e)*(n*e*a)-n*r*(e/m)**r*a)==0
assert s.simplify(s.diff((l*e/m)**(1/n),e)*(n*e*a)-(l*e/m)**(1/n)*a)==0
checks+=2
print(f'{checks} exact algebra/actual-interval checks PASS')
# Actual three-interval boundary optimum supplied by Two-sided.
Ksmall=[(-F(1,16),F(1,16)),(-F(1,2),F(1,2)),(-F(1,2),F(1,2))]
Vs=[h-l for l,h in Ksmall]; Ms=sum(Vs)
gs=sum((j-1)*Vs[j] for j in range(3))/Ms
Ss=sum(v**3 for v in Vs)/(12*Ms)
assert Ms==F(17,8) and gs==F(7,17)
assert Ss==F(1025,13056) and Ss/Ms==F(1025,27744)
assert all(v<Ms/2 for v in Vs)
assert [1+F(17,24)*(z-gs) for z in (-1,0,1)]==[0,F(17,24),F(17,12)]
checks+=4
for j in range(501):
    b=-F(17,10)+(F(17,24)+F(17,10))*F(j,500)
    L=[1+b*(z-gs) for z in (-1,0,1)]
    assert min(L)>=0 and L[1]>=F(17,24)
    assert sum(L[j]*Vs[j] for j in range(3))==Ms
    assert all(L[j]*Vs[j]<=Ms for j in range(3))
    checks+=3
for j in range(101):
    de=F(j,10**6)
    for sign in (-1,1):
        knots=sorted({(e+sign*de)/z for z,ends in zip((-1,0,1),Ksmall) if z for e in ends})
        ts=[knots[0]-1]+knots+[knots[-1]+1]
        def mm(t):
            if sign==1:return sum(clamp(ub-(t*z-de),ub-lb) for z,(lb,ub) in zip((-1,0,1),Ksmall))
            return sum(clamp(t*z+de-lb,ub-lb) for z,(lb,ub) in zip((-1,0,1),Ksmall))
        assert min(mm(t) for t in ts)==F(5,8)+de
        checks+=1
print(f'{checks} exact checks PASS including boundary optimum')
