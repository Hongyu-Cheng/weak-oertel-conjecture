from fractions import Fraction as F
from itertools import combinations
import sympy as s
checks=0
def check(x):
    global checks
    assert bool(x)
    checks+=1
def clip(x,l,h):return max(l,min(h,x))
def tail(x):return clip(1-x,F(0),F(2))
def J(x):return min(F(2),2*max(1-x,F(0)))
for k in range(-600,601):
    h=F(k,100)
    candidates={F(0),h-1,h+1,-h-1,-h+1,abs(h)+2,-abs(h)-2}
    vals=[tail(h-a)+tail(h+a) for a in candidates]
    check(min(vals)==J(h))
weights={-1:F(2),0:F(3),1:F(2)}
for m in (1,2):
    for I in combinations((-1,0,1),m):
        if I==(-1,1):continue
        check(sum(weights[i] for i in I)<F(7,2)*len({i%2 for i in I}))
check(F(2**3+3**3+2**3,12*7)==F(43,84))
check(F(43,84)/7==F(43,588))
check(F(43,196)<F(1,4))
def depth(y):
    return min(F(5),clip(2-y,F(0),F(3))+J(y),clip(y+1,F(0),F(3))+J(-y))
for k in range(-400,801):
    y=F(k,400)
    if not -1<=y<=2:continue
    check(depth(y)<=F(13,4))
    check((depth(y)==F(13,4))==(y==F(1,4)))
    if abs(y-F(1,4))>=F(1,100):check(depth(y)<=F(13,4)-F(1,100))
d,t=s.symbols('d t',positive=True)
y=s.Rational(1,4)+d/2
E=3-s.Rational(4,3)*(y-s.Rational(1,2))**2
check(s.expand(E-(s.Rational(35,12)+d/3-d*d/3))==0)
check(s.expand(d*d-3*t*E-((1+t)*d*d-t*d-s.Rational(35,4)*t))==0)
root=(t+s.sqrt(35*t+36*t*t))/(2*(1+t))
check(s.simplify((1+t)*root**2-t*root-s.Rational(35,4)*t)==0)
check(F(13,28)>F(1,4))
check(F(3,7)<F(1,2))
print(f'PASS: {checks} exact checks')
