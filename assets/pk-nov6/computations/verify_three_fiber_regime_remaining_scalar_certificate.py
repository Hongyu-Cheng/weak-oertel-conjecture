"""Exact scalar and realization checks; no assertion of a bad critical cover.

The below-target row is ONLY necessary scalar data. The actual convex-body
realization has a different, rigorously larger depth, proved in the note.
"""
from fractions import Fraction as F
checks=0

def check(statement):
    global checks
    assert statement
    checks+=1

a=F(1,4);c=F(1);b=F(121,100);m=a+c+b;gamma=F(4,9)
check(m==F(123,50))
check(max(a,c,b)<m/2)
check(a>F(1,8))
ra=F(1,2);rb=F(11,10)
check(ra**2==a and rb**2==b)
check((ra+rb)/2==F(4,5)<1)
R=((ra+rb)/2)**2
check(R+a==F(89,100)<m/2)
q=F(4,9);U=F(1,10);V=F(1,1800);Q=F(109,200)
check(q+U+V==Q)
check(gamma*b==F(121,225)<Q<gamma*m/2==F(41,75))
check(U+V==F(181,1800)<a)
check(Q<3*q)
check(U<q and V<q)
check((U+V)/q==F(181,800)<(a+b-1)/2==F(23,100))
l=a-U;r=b-V
check(l==F(3,20)>0)
check(r==F(2177,1800)>0)
gap=4*(1-q)-l-r
check(gap==F(1553,1800)>0)
check(gap**2-4*l*r==F(60649,3240000)>0)
# Thus sqrt(l)+sqrt(r)<2sqrt(1-q), proved by two legal squarings.

T=[(F(-1,3),F(-2,3)),(F(2,3),F(-2,3)),(F(-1,3),F(4,3))]
def bary(p):
    x,y=p
    return F(1,3)-x-y/2,x+F(1,3),y/2+F(1,3)
def area(poly):
    return abs(sum(poly[i-1][0]*poly[i][1]-poly[i-1][1]*poly[i][0] for i in range(len(poly))))/2
check(area(T)==1)
check(sum(p[0] for p in T)==sum(p[1] for p in T)==0)
for p in T:
    check(min(bary(tuple(-ra*v for v in p)))>=0) # -A subset T
    check(min(bary(tuple(F(4,5)*v for v in p)))>0) # midpoint subset int T
    check(min(bary(tuple(v/rb for v in p)))>0) # T subset int B
for scale in [ra,rb]:
    ell_values=[[bary(tuple(scale*v for v in p))[i]-F(1,3) for p in T] for i in range(3)]
    for values in ell_values:
        check(min(values)>-1 and max(values)<1) # tilt L=1 saturates endpoint captures
Qactual=gamma+a
check(Qactual==F(25,36))
check(max(gamma*a,gamma*b)<Qactual)
check(1-ra/(2*F(2,3))==F(5,8)>F(1,3))
check(Qactual/m==F(625,2214)>gamma/2)
check(Qactual>Q)
print(f'PASS: {checks} exact rational checks. Formal row and actual realization remain explicitly distinct.')
