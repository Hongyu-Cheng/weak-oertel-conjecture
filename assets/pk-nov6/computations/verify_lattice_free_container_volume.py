"""Exact arithmetic for the container-volume examples and contact stress."""
from fractions import Fraction as Q
import sympy as s

alpha=Q(1,5)
assert Q(1,8)<alpha<Q(1,4)
assert Q(1,2)-Q(1,4)/2 == Q(3,8) > alpha
assert (1+2*Q(3,10))/8 == alpha

P0=[(Q(0),Q(3,10)),(Q(3,10),Q(0)),(Q(7,10),Q(0)),
    (Q(1),Q(3,10)),(Q(1),Q(7,10)),(Q(7,10),Q(1)),
    (Q(3,10),Q(1)),(Q(0),Q(7,10))]
for x,y in P0:
    assert 0<=x<=1 and 0<=y<=1
    assert Q(3,10)<=x+y<=Q(17,10)
    assert Q(-7,10)<=x-y<=Q(7,10)
area=sum(P0[i][0]*P0[(i+1)%8][1]-P0[i][1]*P0[(i+1)%8][0]
         for i in range(8))/2
assert area==Q(41,50)

# The inscribed quadrilateral has area exactly R.
R=s.symbols('R', positive=True)
quad=[(0,s.Rational(1,2)),(s.Rational(1,2),-R),
      (1,s.Rational(1,2)),(s.Rational(1,2),R)]
quad_area=sum(quad[i][0]*quad[(i+1)%4][1]-quad[i][1]*quad[(i+1)%4][0]
              for i in range(4))/2
assert s.simplify(quad_area-R)==0

# Unit-normal weight sqrt(2) times unit normal is the displayed raw normal.
contacts=[((0,0),(-1,-1),0),((1,0),(1,-1),1),
          ((0,1),(-1,1),1),((1,1),(1,1),2)]
assert all(sum(n[j]*p[j] for j in range(2))==b for p,n,b in contacts)
assert tuple(sum(n[j] for p,n,b in contacts) for j in range(2))==(0,0)
matrix=[[sum(n[i]*p[j] for p,n,b in contacts) for j in range(2)]
        for i in range(2)]
assert matrix==[[2,0],[0,2]]
assert sum(b for p,n,b in contacts)==4

t=s.symbols('t')
vol=2/(1-t*t)
assert s.diff(vol,t).subs(t,0)==0
assert s.diff(vol,t,2).subs(t,0)==4
assert s.simplify(vol-2-2*t*t/(1-t*t))==0
assert vol.subs(t,s.Rational(1,2))==s.Rational(8,3)

# The already-certified basin gap is unchanged by these container equations.
assert Q(4,9)*Q(3,25)-Q(103,2500)==Q(91,7500)

print('PASS: rational depth thresholds, unbounded-area family, exact contact matrix, and volume second variation')
