"""Exact rational dual certificate and feasible scalar calibrations."""
from fractions import Fraction as F
import sympy as s
checks=0
def check(a):
    global checks
    assert a
    checks+=1

c=F(6144,22745)
rhs=(3*F(3,2)**3+2*F(9,16)**3)/3
check(rhs==F(7155,2048))
bound=2*(rhs-F(2,3))
check(bound==F(17369,3072))
check(bound-2==F(11225,3072))
check(((bound-2)+F(15,4))/2==1/c)
check(c>F(4,15))
check(5*c-F(4,3)==F(1180,68235))

U,E,Q,ss,rr,alpha=s.symbols('U E Q ss rr alpha',positive=True)
check(s.factor((1+2*alpha)/ss-(1/ss+2*(ss+alpha-rr)/ss+2*rr/ss-2))==0)
check(s.factor((U+2*Q+2*E-2)-(U+2*Q-s.Rational(7,4)*E+s.Rational(15,4)*E-2))==0)
e=s.symbols('e',nonnegative=True)
check(s.factor(s.diff((s.Rational(11225,3072)+s.Rational(15,4)*e)/(1+e),e)-s.Rational(295,3072)/(1+e)**2)==0)

# Rational-square arguments make phi values exact fractions.
def phi_from_root(r):return r*r-F(2,3)*r**3
roots={F(i,j) for j in range(1,9) for i in range(0,5*j+1)}
for r in roots:
    for a in [F(1,2),-F(7,16)]:
        check(phi_from_root(r)+a*r*r<=max(F(0),1+a)**3/3)

for ud in range(1,9):
    for un in range(ud,4*ud+1):
        ur=F(un,ud);u=ur*ur
        for qr in [F(1),ur,(1+ur)/2]:
            q=qr*qr
            for en in range(0,13):
                er=F(en,12);ee=er*er
                lhs=phi_from_root(ur)+2*phi_from_root(qr)+2*phi_from_root(er)
                if lhs<F(2,3):continue
                S=1/u;R=ee/u;A=(q+ee-1)/u
                check(0<=A<=1 and 0<=R<=S)
                check((S+R)/(1+2*A)>=c)
                check(u+2*q-F(7,4)*ee<=bound)

print(f'PASS: {checks:,} exact dual and scalar checks')
