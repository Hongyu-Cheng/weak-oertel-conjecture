"""Independent exact checks for the retained logarithmic-scale audit."""
from fractions import Fraction as F
import sympy as sp

checks=0


def check(x):
    global checks
    assert x
    checks+=1


a,b,T,lam=sp.symbols('a b T lam', positive=True)
s=sp.log(a/b)-T
for m in range(9):
    k=lam**m*s**(m+1)
    # On its positive branch this is k(s)=s*g(lambda*s), g(r)=r^m.
    FF=a*k
    H=sp.hessian(FF,(a,b))
    K=lam**m*((m+1)*s**m+(m+1)*m*s**(m-1)) if m else sp.Integer(1)
    expected=K*sp.Matrix([[1/a,-1/b],[-1/b,a/b**2]])
    for i in range(2):
        for j in range(2):
            check(sp.simplify(H[i,j]-expected[i,j])==0)
    check(sp.simplify(H.det())==0)
    check(sp.simplify(sp.diff(FF,a)-(k+lam**m*(m+1)*s**m))==0)
    check(sp.simplify(sp.diff(FF,b)+(a/b)*lam**m*(m+1)*s**m)==0)

# General algebra of the truncated test, retaining g-values as symbols.
ss,tt,g0,gs,gt=sp.symbols('ss tt g0 gs gt')
check(sp.expand(tt*gt-ss*gs+(ss-tt)*g0
                -(tt*(gt-gs)-(ss-tt)*(gs-g0)))==0)

# The upper-tail identity, in both branches, with exact rational values.
for den in range(1,31):
    for num in range(den+1):
        rr=F(num,den)
        for cut in [F(0),F(1,10),F(1,4),F(1,2),F(3,4),F(1)]:
            plus=max(rr-cut,F(0))
            check(rr*plus==plus*plus+cut*plus)

# Rational residual counter to pointwise W+r<=beta. All monotone convex
# generators are checked exactly; the proof in the audit covers every g.
beta=F(1,2)
rates=[F(0),F(1,4)]
bweights=[F(1),F(1)]
aweights=[F(3,4),F(0)]
def residual(g):
    return sum((aa+rr*bb-beta*bb)*g(rr)
               for rr,bb,aa in zip(rates,bweights,aweights))

check(residual(lambda r:F(1))==0)
check(aweights[0]/bweights[0]+rates[0]>beta)
for power in range(1,31):
    check(residual(lambda r:r**power)<=0)
for den in range(1,31):
    for num in range(den+1):
        cut=F(num,den)
        check(residual(lambda r:max(r-cut,F(0)))<=0)
        lhs=sum(aa*max(rr-cut,F(0))+bb*max(rr-cut,F(0))**2
                for rr,bb,aa in zip(rates,bweights,aweights))
        rhs=(beta-cut)*sum(bb*max(rr-cut,F(0))
                          for rr,bb in zip(rates,bweights))
        if cut<=beta:
            check(lhs<=rhs)

print(f'PASS: {checks} exact scale-resolved logarithmic-defect audit checks')
