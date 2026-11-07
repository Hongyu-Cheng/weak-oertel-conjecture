"""Exact scalar checks for the projective weighted-facet credit.
The general geometric and BBL arguments are in the Markdown source.
"""
from fractions import Fraction as F
import sympy as s

checks = 0
def check(q):
    global checks
    assert q
    checks += 1

a,b,R,S=s.symbols("a b R S")
check(s.expand(b*(S-b)-a*(S-a)-(b-a)*(S-a-b)) == 0)
credit=a-R*b/(2*b-R)
check(s.simplify(a+b-2*b*b/(2*b-R)-credit) == 0)
check(s.simplify(credit.subs(R,2*a*b/(a+b))) == 0)
res=R*b/(2*b-R)
check(s.simplify(2*res*b/(res+b)-R) == 0)

def harm(x,y):
    return 2*x*y/(x+y) if x+y else F(0)

for ai in range(1,8):
    for bi in range(ai,9):
        av,bv=F(ai,5),F(bi,5)
        for si in range(13):
            sv=av*F(si,12)
            for ti in range(13):
                tv=bv*F(ti,12)
                rv=harm(sv,tv)
                cap=av+bv-sv-tv
                if rv<harm(av,bv):
                    bound=av-rv*bv/(2*bv-rv)
                else:
                    bound=F(0)
                check(cap>=bound)
        for j in range(13):
            rv=harm(av,bv)*F(j,12)
            sv=rv*bv/(2*bv-rv)
            check(0<=sv<=av)
            check(harm(sv,bv)==rv)
            check(av-sv==av-rv*bv/(2*bv-rv))

# The continued inverse power has matching value and slope at its join.
t,delta=s.symbols("t delta", positive=True)
for dim in range(2,12):
    g=delta*(dim+1-dim*t/delta)**(-s.Rational(1,dim))
    check(s.simplify(g.subs(t,delta)-delta)==0)
    check(s.simplify(s.diff(g,t).subs(t,delta)-1)==0)
    expected=(dim+1)/delta*(dim+1-dim*t/delta)**(-s.Rational(2*dim+1,dim))
    check(s.simplify(s.diff(g,t,2)-expected)==0)
    k=dim-1
    p=-F(1,dim)
    check(p/(1+k*p)==-1)

print(f"PASS: {checks} exact weighted-facet residual-credit checks")
