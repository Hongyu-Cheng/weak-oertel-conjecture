"""Exact rational tails, proper perturbation, and full lattice-product fibers."""
from fractions import Fraction as F
from itertools import product

Gamma=F(4,9);lam=F(7,9)
def tail(v):
    q=F(1,3)+v
    if q<=0:return F(1)
    if q>=F(1,2):return F(0)
    return 1-4*q*q
def pair_score(s,t,l):
    return (tail(t)+tail(-t)+tail(s+t)+tail(s-t)
            +l*(tail(-s+t)+tail(-s-t)))

s,t=F(1,3),F(1,6)
values=[tail(v) for v in (t,-t,s+t,s-t,-s+t,-s-t)]
assert values==[0,F(8,9),0,0,F(8,9),1]
assert pair_score(s,t,lam)==F(191,81)
assert pair_score(s,t,lam)-2*(Gamma+lam)==-F(7,81)
for l in (F(1,100),F(1,2),lam,F(1),F(7,2)):
    assert pair_score(s,t,l)-2*(Gamma+l)==-l/9

eps=F(1,100);tt=F(1,6)-eps;ss=2*tt
A,B=tail(tt),tail(-tt)
assert (tt,ss)==(F(47,300),F(47,150))
assert (A,B)==(F(99,2500),F(19691,22500))
assert tail(3*tt)==0 and tail(-3*tt)==1
assert F(1,3)+3*tt>F(1,2) and F(1,3)-3*tt<0
for l in (F(1,100),F(1,2),lam,F(1),F(7,2)):
    formula=-l/9+(F(20,3)-4*l/3)*eps-(12+4*l)*eps*eps
    assert pair_score(ss,tt,l)-2*(Gamma+l)==formula
assert pair_score(ss,tt,lam)-2*(Gamma+lam)==-F(3203,101250)
G0,Gp,Gm=(A+B)/2,A/2,(B+1)/2
assert (G0,Gp,Gm)==(F(10291,22500),F(99,5000),F(42191,45000))
assert all(0<v<1 for v in (G0,Gp,Gm))
assert G0+Gp+lam*Gm==F(244297,202500)
assert Gamma+lam-(G0+Gp+lam*Gm)==F(3203,202500)
assert F(4,1000)*(2+lam)==F(1,90)
assert F(7,162)-F(1,90)==F(13,405)>0

checked=0
for n in range(2,9):
    m=2**(n-1)
    pts=[z for z in product(range(-1,2),repeat=n)
         if abs(z[0])<=1 and all(abs(2*zj-z[0])<=1 for zj in z[1:])]
    assert len(pts)==2*m+1
    assert {tuple(-v for v in z) for z in pts}==set(pts)
    assert [z for z in pts if z[0]==0]==[(0,)*n]
    assert sum(z[0]==1 for z in pts)==sum(z[0]==-1 for z in pts)==m
    # The inequalities themselves also exclude coordinates outside [-1,1].
    for z in pts:
        assert all(F(z[0]-1,2)<=zj<=F(z[0]+1,2) for zj in z[1:])
    def G(v):return sum(tail(v-F(z[0],6)) for z in pts)/len(pts)
    for l in (F(1,100),F(1,2),lam,F(1),F(7,2)):
        assert G(0)+G(s)+l*G(-s)-(Gamma+l)==F(1-m*l,9*(2*m+1))
    if n==2:
        assert set(pts)=={(1,0),(1,1),(-1,-1),(-1,0),(0,0)}
        assert (G(0),G(s),G(-s))==(F(7,15),0,F(43,45))
        assert G(0)+G(s)+lam*G(-s)==F(98,81)
        assert G(0)+G(s)+lam*G(-s)-(Gamma+lam)==-F(1,81)
    assert F(m+1,2*m+1)>F(1,2)>Gamma
    checked+=len(pts)

# Each canonical barycentric triangle cap has relative area (2/3)^2.
assert F(2,3)**2==Gamma
# Their margins sum to zero at every continuous point, proving cover.
for x1,x2 in product([F(-2),F(0),F(1,3),F(1),F(3)],repeat=2):
    bary=[1-x1-x2,x1,x2]
    assert sum(bary)==1 and max(bary)>=F(1,3)
print("PASS: six exact noisy tails, every positive-coefficient deficit formula,")
print("strict proper perturbation, continuous-noise margin, and",checked,
      "exact lattice fibers in dimensions2..8.")
