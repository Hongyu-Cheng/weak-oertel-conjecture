from fractions import Fraction as F
from itertools import product
checks=0
def check(b):
 global checks
 assert b
 checks+=1
V=[(-3,0),(-1,-1),(0,-1),(3,1),(2,1)]
def cross(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def inside(x,y):return -1<=y<=1 and x+2*y>=-3 and 2*x-3*y<=3 and x-5*y>=-3
P={(-1,-1),(0,-1),(-3,0),(-2,0),(-1,0),(0,0),(1,0),(2,1),(3,1)}
for z in product(range(-6,7),repeat=2):
 polygon=all(cross(V[i],V[(i+1)%5],z)>=0 for i in range(5))
 check(polygon==inside(*z))
 check(inside(*z)==(z in P))
check(len(P)==9)
anchors=[(-1,0),(0,0),(1,0)]
expected=[{(-3,0),(-2,0),(-1,0),(0,0),(1,0)}, {(-1,0),(0,0),(1,0)}, {(-1,-1),(0,-1),(1,0),(2,1),(3,1)}]
for p,E in zip(anchors,expected):
 star={z for z in P if tuple(2*p[i]-z[i] for i in range(2)) in P}
 check(star==E)
 check(p in star)
 check(all(tuple(2*p[i]-z[i] for i in range(2)) in star for z in star))
P3={(x,y,0) for x,y in P}|{(x,y,1) for x,y in product(range(5),repeat=2)}
check(len(P3)==34)
check(len({tuple(x%2 for x in z) for z in P3})==8)
for p,E in zip(anchors,expected):
 a=(*p,0)
 star={z for z in P3 if tuple(2*a[i]-z[i] for i in range(3)) in P3}
 check(star=={(*z,0) for z in E})
good=(2,2,1)
check({z for z in P3 if tuple(2*good[i]-z[i] for i in range(3)) in P3}=={(x,y,1) for x,y in product(range(5),repeat=2)})
check(tuple((anchors[0][i]+anchors[2][i])//2 for i in range(2))==anchors[1])
check(all((anchors[0][i]-anchors[2][i])%2==0 for i in range(2)))
for n in range(3,9):
 for d in range(1,9):
  gamma=F(d,d+1)**d
  mass=34*2**(n-3)
  target=gamma*mass/2**n
  check(target==F(17,4)*gamma)
  check(3*gamma<target<5*gamma)
  check(25*gamma>target)
print(f'{checks} exact checks PASS')
