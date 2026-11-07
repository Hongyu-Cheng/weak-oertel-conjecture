"""Exact geometry and scalar identities supporting the analytical theorem."""
from fractions import Fraction as F
from itertools import product, combinations
import sympy as s
checks=0
def check(v):
    global checks
    assert bool(v)
    checks+=1
A=[(F(i,2),F(j,2)) for i,j in product((-1,1),repeat=2)]
B=[(F(i,20),F(j,20)) for i,j in product((-1,1),repeat=2)]
K=[(F(1),F(0)),(F(-1,2),F(2,3)),(F(-1,2),F(-2,3))]
def area(poly):
    return abs(sum(poly[i][0]*poly[(i+1)%len(poly)][1]-poly[i][1]*poly[(i+1)%len(poly)][0] for i in range(len(poly))))/2
check(area(K)==1)
for a,b in product(A,B):
    x,y=((a[j]+b[j])/2 for j in (0,1))
    check(x>F(-1,2))
    check(abs(y)<F(4,9)*(1-x))
M=F(201,100)
weights=[F(1),F(1),F(1,100)]
for size in (1,2):
    for I in combinations(range(3),size):
        if I==(0,2):continue
        parity=len({i%2 for i in I})
        check(sum(weights[i] for i in I)<parity*M/2)
SX=(F(1,12)+F(1,8)+F(1,100)*F(1,1200))/M
SY=(F(1,12)+F(2,27)+F(1,100)*F(1,1200))/M
check(SX==F(25001,241200))
check(SY==F(170009,2170800))
check(F(1,16)<SY<SX<F(1,4))
check(F(4,9)+F(1,100)==F(409,900))
check(F(1,2)-F(409,900)==F(41,900))
check(F(409,900)+F(1,10000)<F(1,2))
check(F(4,9)*M/2==F(67,150)<F(1,2))
check(F(41,900)/4==F(41,3600))
for p in K:
    check(p[0]**2+p[1]**2<=1)
for p,q in product(K,K):
    check((p[0]-q[0])**2+(p[1]-q[1])**2<4)
r=s.symbols('r',positive=True)
log0=-(100*s.log(r)+s.log(2*r-1))/201
log1=log0+s.log(r)
log2=log0+s.log(2*r-1)
check(s.simplify(100*log0+100*log1+log2)==0)
check(s.simplify(s.diff(log1,r)-(200*r-101)/(201*r*(2*r-1)))==0)
check(s.simplify(s.diff(log2,r)-(200*r+100)/(201*r*(2*r-1)))==0)
check(F(3)*F(101,100)==F(303,100))
check(1+F(303,100)/3==F(201,100))
for j in range(1,1001):
    rr=F(1)+F(j,100)
    check(200*rr-101>0)
    check(1<2-1/rr<2)
print(f'PASS: {checks} exact checks')
