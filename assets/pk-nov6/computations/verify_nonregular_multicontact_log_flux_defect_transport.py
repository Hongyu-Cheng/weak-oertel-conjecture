"""Exact algebra checks only: no synthetic stationary menu is asserted."""
from fractions import Fraction as F
from itertools import product
import sympy as sp

checks=0
def check(v):
    global checks
    assert v
    checks+=1

branches=list(product([0,1],repeat=3))
rho=[F(1,5),F(1,3),F(7,15)]
S=[F(1),F(3,2),F(4,3)]
area=[F(2),F(1,2),F(7,3)]
epsilon=F(1,9)
for n in range(1,51):
    raw=[[F(n+2*a+b+1) for b in range(8)] for a in range(3)]
    den=sum(sum(r) for r in raw)
    lam=[[x/den for x in r] for r in raw]
    T=[[S[j]+area[j]*bits[j] for j in range(3)] for bits in branches]
    B=[sum(rho[j]/T[b][j] for j in range(3)) for b in range(8)]
    theta=[[rho[j]/T[b][j]/B[b] for j in range(3)] for b in range(8)]
    kc=[sum(lam[a][b]/B[b] for b in range(8)) for a in range(3)]
    ki=sum(kc)
    f=[F(2,3),F(5,4),F(7,6)]
    e=[epsilon*f[a]*kc[a] for a in range(3)]
    ei=sum(e)
    om=[sum(lam[a][b]*theta[b][j] for a in range(3) for b in range(8)) for j in range(3)]
    tau=[sum(lam[a][b]*theta[b][j]*branches[b][j] for a in range(3) for b in range(8))/om[j]
         for j in range(3)]
    te=[S[j]+area[j]*tau[j] for j in range(3)]
    check(sum(om)==1)
    for j in range(3):
        check(om[j]*te[j]==ki*rho[j])
        check(0<=tau[j]<=1)
    check(ei==epsilon*sum(f[a]*kc[a] for a in range(3)))
    check(sum(rho[j]/te[j] for j in range(3))==1/ki)
    # Contact weights differ from e-weights when f is not constant.
    pos=[F(-2),F(1),F(4)]
    center=sum(kc[a]*pos[a] for a in range(3))/ki
    for j in range(3):
        check(om[j]*te[j]*center==rho[j]*sum(kc[a]*pos[a] for a in range(3)))

# Symbolic contactwise source balance and all three summed flux moments.
eps=sp.Rational(2,7)
N=3
u=[sp.Matrix([1,0]),sp.Matrix([0,1]),sp.Matrix([-sp.Rational(3,5),-sp.Rational(4,5)])]
rh=[sp.Rational(1,5),sp.Rational(1,3),sp.Rational(7,15)]
U=sum((rh[j]*u[j] for j in range(3)),sp.zeros(2,1))
Cu=sum((rh[j]*u[j]*u[j].T for j in range(3)),sp.zeros(2))
Sigma=sp.eye(2)
for j in range(3): check((u[j].T*Sigma*u[j])[0]==1)
for n in range(1,31):
    kc=[sp.Rational(n+1,n+9),sp.Rational(2,n+9),sp.Rational(3,n+9)]
    ki=sum(kc)
    f=[sp.Rational(2,3),sp.Rational(5,4),sp.Rational(7,6)]
    L=[sp.Rational(4,3),sp.Rational(3,2),sp.Rational(5,2)]
    y=[sp.Matrix([1,-2]),sp.Matrix([3,1]),sp.Matrix([-1,4])]
    p=[sp.Matrix([-2,1]),sp.Matrix([1,0]),sp.Matrix([3,2])]
    c=[sp.Matrix([1,2]),sp.Matrix([-2,3]),sp.Matrix([3,-1])]
    e=[eps*f[a]*kc[a] for a in range(3)]
    ei=sum(e)
    aE=[U/(eps*f[a])-c[a]/(N*L[a]) for a in range(3)]
    for a in range(3):
        check(kc[a]*U==e[a]*(aE[a]+c[a]/(N*L[a])))
    ybar=sum((kc[a]*y[a] for a in range(3)),sp.zeros(2,1))/ki
    pbar=sum((kc[a]*p[a] for a in range(3)),sp.zeros(2,1))/ki
    sec=[ybar-ei/ki*Sigma*u[j] for j in range(3)]
    capforce=ki*U
    ownforce=sum((e[a]*(aE[a]+c[a]/(N*L[a])) for a in range(3)),sp.zeros(2,1))
    check(capforce==ownforce)
    capbase=sum((ki*rh[j]*pbar*u[j].T for j in range(3)),sp.zeros(2))
    ownbase=sum((e[a]*p[a]*(aE[a]+c[a]/(N*L[a])).T for a in range(3)),sp.zeros(2))
    check(capbase==ownbase)
    captensor=sum((ki*rh[j]*sec[j]*u[j].T for j in range(3)),sp.zeros(2))
    expected=sum((e[a]*y[a]*(aE[a]+c[a]/(N*L[a])).T for a in range(3)),sp.zeros(2))-ei*Sigma*Cu
    check(captensor==expected)
    energy=ei*sp.eye(2)/N-sum((e[a]*y[a]*aE[a].T for a in range(3)),sp.zeros(2))
    covariance=ei*sp.eye(2)/2+ei*Sigma*Cu
    constant=-(N+2)*ei*sp.eye(2)/(2*N)
    logarithm=-sum((e[a]*y[a]*c[a].T/(N*L[a]) for a in range(3)),sp.zeros(2))
    check(captensor+energy+covariance+constant+logarithm==sp.zeros(2))

print(f'PASS: {checks} exact aggregation and moment checks')
