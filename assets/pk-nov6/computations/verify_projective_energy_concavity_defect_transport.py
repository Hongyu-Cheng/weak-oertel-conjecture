from fractions import Fraction as F
from itertools import product
import sympy as s

checks = 0
def check(q):
    global checks
    assert q
    checks += 1

L, R = s.symbols('L R', positive=True)
a = (R-L)/(2*L*R)
energy = (L+R)/((1-a*L)*(1+a*R))
check(s.simplify(energy-4*L*R/(L+R)) == 0)
x, aa = s.symbols('x aa', real=True)
# Exact derivative of the interval denominator product at its maximizer.
check(s.simplify(s.diff((1-aa*L)*(1+aa*R), aa).subs(aa, a)) == 0)
check(s.diff((1-aa*L)*(1+aa*R), aa, 2) == -2*L*R)

# Exact two-interval joint concavity, including independent shape/mark data.
def E(l,r): return 4*l*r/(l+r)
for l1,r1,l2,r2 in product(range(1,5), repeat=4):
    for lam in (F(1,4),F(1,2),F(3,4)):
        left=E(lam*l1+(1-lam)*l2,lam*r1+(1-lam)*r2)
        right=lam*E(F(l1),F(r1))+(1-lam)*E(F(l2),F(r2))
        check(left>=right)
        check((left==right)==(l1*r2==l2*r1))

# Escort exponents and simplex normalization in every displayed dimension.
for d in range(1,21):
    p=F(d+1,d+2)
    check(p/(1-p)==d+1)
    check((d+2)*p==d+1)
    check(F(d+2,d)>1)
    N=d+1
    bary=[F(2*j,N*(N+1)) for j in range(1,N+1)]
    denom=[1/(N*b) for b in bary]
    check(sum(b*v for b,v in zip(bary,denom))==1)
    check(1/s.prod(denom)==N**N*s.prod(bary))

print(f'{checks} exact checks PASS')
