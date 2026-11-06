"""Exact actual clippings and identities; analytic proof is in the note."""
from fractions import Fraction as F
from itertools import product
import sympy as sp

checks=0
def check(v):
    global checks
    assert v
    checks+=1

def cap(a,c,radii):
    # The actual centered intervals; either continuous orientation has this mass.
    return sum(max(F(0),min(2*r,r-c+a*z)) for z,r in zip((-1,0,1),radii))

deltas=[F(1,20),F(1,10),F(1,4),F(2,5)]
for delta in deltas:
    q=3+delta
    check(q<4)
    check(cap(1+delta,-delta,[F(1)]*3)==q)
    check(cap(F(4),-delta,[F(1)]*3)==q)
    for a in [F(i,13) for i in range(-100,101)]:
        check(cap(a,-delta,[F(1)]*3)>=q)
    for h,r in product([F(-3),F(-1),F(-1,7),F(0),F(1,7),F(1),F(3)],
                       [F(i,3) for i in range(-12,13)]):
        t=F(1,10000)/(1+abs(h)+abs(r))
        radii=[1-h*t,1-h*t/2,F(1)]
        check(radii[1]==(radii[0]+radii[2])/2)
        check(min(radii)>0)
        rp=h/2+r-max(-r-h,F(0))
        rm=h/2+r
        check(cap(1+delta,-delta+t*r,radii)==q-t*rp)
        check(cap(F(4),-delta+t*r,radii)==q-t*rm)
    for h in [F(i,5) for i in range(-20,21)]:
        alpha=delta*h/2
        ell=(1+delta)*h/2 if h>=0 else (5+4*delta)*h/6
        rminus=ell-h/2
        rplus=ell-h/2 if h>=0 else (ell-3*h/2)/2
        check((rplus+rminus)/2==alpha)
        check(h/2+rplus-max(-rplus-h,F(0))==ell)
        check(h/2+rminus==ell)
        check((rplus>=-h) if h>=0 else (rplus<=-h))
        improvement=ell-(3+delta)*h/2
        check(improvement==(-h if h>=0 else (delta-4)*h/6))
    check(-((1+delta)/2-(5+4*delta)/6)/2==(2+delta)/12)

# Symbolic full invariant normalization, not a fixed physical buffer.
t,h,delta=sp.symbols('t h delta', real=True)
r=[1-h*t,1-h*t/2,sp.Integer(1)]
mass=2*sum(r)
energy=2*r[1]
cov=sum(x**3 for x in r)/(3*sum(r))
check(sp.simplify(energy/mass-sp.Rational(1,3))==0)
check(sp.simplify(sp.diff(cov,t).subs(t,0)+h/3)==0)
check(sp.simplify(sp.diff(delta*sp.sqrt(3*cov),t).subs(t,0)+delta*h/2)==0)
check(sp.diff(mass,t)==-3*h)

# Exact effective-selector/harmonic aggregation for several outside branches.
rho=[F(1,3),F(2,3)]
proper=[F(1),F(2)]
facet=[F(2),F(3)]
branches=list(product([0,1],repeat=2))
for k in range(1,30):
    lam=[F(k+1,4*k+10),F(k+2,4*k+10),F(k+3,4*k+10),F(k+4,4*k+10)]
    check(sum(lam)==1)
    S=[[proper[j]+facet[j]*b[j] for j in range(2)] for b in branches]
    B=[sum(rho[j]/s[j] for j in range(2)) for s in S]
    theta=[[rho[j]/S[b][j]/B[b] for j in range(2)] for b in range(4)]
    w=[sum(lam[b]*theta[b][j] for b in range(4)) for j in range(2)]
    kappa=sum(lam[b]/B[b] for b in range(4))
    eff=[sum(lam[b]*theta[b][j]*branches[b][j] for b in range(4))/w[j] for j in range(2)]
    T=[proper[j]+facet[j]*eff[j] for j in range(2)]
    check(sum(w)==1)
    check(all(0<=e<=1 for e in eff))
    check(all(w[j]*T[j]==kappa*rho[j] for j in range(2)))
    check(sum(rho[j]/T[j] for j in range(2))==1/kappa)
    # The same selector aggregates first moments, not only scalar coarea.
    proper_moment=[F(2,7),F(-3,5)]
    facet_point=[F(-2),F(3)]
    mbranch=[[proper_moment[j]+facet[j]*branches[b][j]*facet_point[j]
              for j in range(2)] for b in range(4)]
    meff=[proper_moment[j]+facet[j]*eff[j]*facet_point[j] for j in range(2)]
    check(all(w[j]*meff[j]==sum(lam[b]*theta[b][j]*mbranch[b][j] for b in range(4))
              for j in range(2)))

# Co-moving affine cap margins: every supporting hinge vanishes pointwise.
ux,uy,xx,yy,z=sp.symbols('ux uy xx yy z', real=True)
A=sp.Matrix([[2,-3],[5,1]])
B=sp.Matrix([3,-2])
c=sp.Matrix([-4,7])
u=sp.Matrix([ux,uy])
X=sp.Matrix([xx,yy])
V=A*X+B*z+c
du=-A.T*u
da=-(B.dot(u))
threshold=u.dot(c)
margin=da*z+du.dot(X)-threshold
check(sp.expand(margin+u.dot(V))==0)
v_inside=u.dot(V) # b=1; n=-u
v_outside=-u.dot(V)
check(sp.expand(-margin-v_inside)==0)
check(sp.expand(margin-v_outside)==0)

print(f'PASS: {checks} exact checks')
