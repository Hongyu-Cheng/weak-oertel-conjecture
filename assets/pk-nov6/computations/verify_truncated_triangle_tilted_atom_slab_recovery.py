"""Exact algebra/geometry checks; the weak-limit argument is analytic in the note."""
from fractions import Fraction as F
import sympy as s

checks = 0
def check(q):
    global checks
    assert q
    checks += 1

t, b, a, eta = s.symbols('t b a eta', positive=True)
G = t*t*s.log(t)/2-t*t/4+b*(t*s.log(t)-t)
check(s.simplify(s.diff(G,t)-(t+b)*s.log(t)) == 0)
Z = 1-a+b*s.log((1-b)/eta)
V = (1-a*a)/2
I = V+b*(1-a)+b*b*s.log((1-b)/eta)
check(s.simplify(I-b*Z-V) == 0)
check(s.simplify(s.diff(t+b*s.log(t-b),t)-t/(t-b)) == 0)
check(s.simplify(s.diff(t*t/2+b*t+b*b*s.log(t-b),t)-t*t/(t-b)) == 0)
cm, zm, vm = s.symbols('c Z V', positive=True)
li = cm*vm/zm
check(s.simplify(1/(zm*t*li)-1/(vm*cm*t)) == 0)
check(s.simplify((cm*t/li)/(zm*t)-1/vm) == 0)

for m in range(8,201):
    aa=F(1,m); ee=F(1,2**m); bb=aa-ee; vv=(1-aa*aa)/2
    check(0 < ee < aa <= F(1,8))
    check(0 < bb < aa)
    check(1-aa >= F(7,8))
    check(1-aa+bb*m < 2)  # Z is smaller, using log(U/eta)<m.
    check(vv >= F(63,128))
    check(F(1,2)+2*aa <= F(3,4))  # upper bound for I.
    check(vv/4 >= F(63,512))
    check(F(3,4)/(2*F(7,8)) == F(3,7))
    check(2*F(63,512)-aa >= F(31,256))
    check(1-2*F(3,7) == F(1,7))
    # sqrt(2)<2, so dividing diagonal slacks by 2 suffices.
    check(F(31,512) > F(1,32))
    check(F(1,14) > F(1,32))
    check(F(63,512) > F(1,32))
    check(vv/2 >= F(63,256))
    check(2/vv <= F(256,63))
    check(bb*m == 1-m*ee)

print(f'PASS: {checks} exact checks')
