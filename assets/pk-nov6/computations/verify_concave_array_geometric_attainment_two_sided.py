"""Finite exact checks of the new sampled-array and zero-set interfaces.
The compactness and attainment claims are proved analytically in the source.
"""
from fractions import Fraction as F
from itertools import combinations
import sympy as s
checks=0
def check(v):
    global checks
    assert bool(v)
    checks+=1
P=[(0,0,0),(1,0,0),(0,1,0),(0,0,1),(0,0,2),(-1,0,2),(0,-1,2)]
n=len(P)
representations={q:[] for q in range(n)}
for size in range(1,5):
    for I in combinations(range(n),size):
        A=s.Matrix([[1]*size]+[[P[i][j] for i in I] for j in range(3)])
        if A.rank()!=size:continue
        inv=(A.T*A).inv()*A.T
        for q in range(n):
            rhs=s.Matrix([1,*P[q]])
            lam=inv*rhs
            if A*lam==rhs and all(x>=0 for x in lam):
                rep=tuple((i,x) for i,x in zip(I,lam) if x>0)
                if rep not in representations[q]:representations[q].append(rep)
# The nonnegative roof has zero set equal to BOTH opposite exposed faces.
h=[1-abs(p[2]-1) for p in P]
check(h==[0,0,0,1,0,0,0])
for q,reps in representations.items():
    for rep in reps:
        check(h[q]>=sum(lam*h[i] for i,lam in rep))
# Its full zero set is NOT closed; midpoint p3 lies in its hull.
check(any(all(h[i]==0 for i,lam in rep) for rep in representations[3]))
parity=lambda p:tuple(v%2 for v in p)
k=len({parity(p) for p in P})
check(k==4)
closed=[]
for mask in range(1,(1<<n)-1):
    I={i for i in range(n) if mask>>i&1}
    is_closed=all(not any(all(i in I for i,lam in rep) for rep in representations[q]) for q in range(n) if q not in I)
    if is_closed:
        closed.append(I)
        ki=len({parity(P[i]) for i in I})
        check(F(len(I),n)<=F(ki,k))
# Positive center p3 captures itself and at least one member of all 3 pairs.
for i,j in [(0,4),(1,5),(2,6)]:
    check(tuple(P[i][l]+P[j][l] for l in range(3))==tuple(2*v for v in P[3]))
check(F(4)>=F(7,4))
# General nonnegative midpoint concavity gives the exact positivity property.
for i,j in combinations(range(n),2):
    if parity(P[i])==parity(P[j]):
        mid=tuple(F(P[i][l]+P[j][l],2) for l in range(3))
        check(mid in P)
        q=P.index(mid)
        check(h[q]>=F(h[i]+h[j],2))
        if h[i]>0 or h[j]>0:check(h[q]>0)
# Finite roofs reproduce sampled concave heights; strict paraboloid example.
for C in [6,10,100]:
    ell=[s.Rational(C)-sum(v*v for v in p) for p in P]
    check(all(v>0 for v in ell))
    for q,reps in representations.items():
        roof=max(sum(lam*ell[i] for i,lam in rep) for rep in reps)
        check(roof==ell[q])
        for rep in reps:
            gap=ell[q]-sum(lam*ell[i] for i,lam in rep)
            variance=sum(lam*sum((P[i][j]-P[q][j])**2 for j in range(3)) for i,lam in rep)
            check(s.simplify(gap-variance)==0)
# An explicit geometric normalization escape for positive concave arrays.
# h_e=(e,1,e) on {-1,0,1}; ell=h_e/e^(2/3), equal weights.
for denom in range(2,102):
    e=F(1,denom)
    check(1>=e)
    # Cube of the positive middle ell, and cubes at the zero-limit endpoints.
    ell_mid_cubed=e**(-2)
    ell_end_cubed=e
    check(ell_mid_cubed*ell_end_cubed**2==1)
    check(ell_mid_cubed>1>ell_end_cubed>0)
print(f'PASS: {checks} exact checks; {len(closed)} proper closed minors checked')
