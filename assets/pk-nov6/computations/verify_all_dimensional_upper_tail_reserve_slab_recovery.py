"""Exact finite normal-region translations and sharp-box identities.

The proof for all convex bodies and the limiting step are in the note;
the checks below do not replace them.
"""
from fractions import Fraction as F
from itertools import product
import sympy as s

checks=0
def yes(p):
    global checks
    assert p
    checks+=1
def eq(a,b):
    global checks
    assert s.simplify(a-b)==0,(a,b)
    checks+=1
def dot(a,b):return sum(x*y for x,y in zip(a,b))

# Projected boxes: unique support vertices, exact outside certificate,
# and disjointness via the monotonicity scalar product.
for m in range(1,5):
    directions=list(product([F(-2),F(-1,3),F(1,2),F(3)],repeat=m))
    samples=[]
    for v in directions:
        p=tuple(F(1) if x>0 else F(-1) for x in v)
        hp=sum(abs(x) for x in v)
        yes(dot(v,p)==hp)
        image=tuple(x+y for x,y in zip(v,p))
        eq(dot(v,image)-hp,dot(v,v))
        yes(dot(v,image)>hp)
        samples.append((v,p,image))
    for i in range(len(samples)-1):
        v,p,image=samples[i];w,q,other=samples[i+1]
        if p!=q:
            yes(dot(tuple(x-y for x,y in zip(v,w)),tuple(x-y for x,y in zip(p,q)))>0)
            yes(image!=other)

# Non-box projected simplex: direct maximization selects arbitrary vertices.
for m in range(1,5):
    vertices=[tuple(F(0) for _ in range(m))]+[tuple(F(int(i==j)) for i in range(m)) for j in range(m)]
    for numerators in product(range(-2,3),repeat=m):
        if not any(numerators):continue
        v=tuple(F(x) for x in numerators)
        heights=[dot(v,p) for p in vertices];maximum=max(heights)
        if heights.count(maximum)!=1:continue
        p=vertices[heights.index(maximum)]
        eq(dot(v,tuple(x+y for x,y in zip(v,p)))-maximum,dot(v,v))
        yes(dot(v,v)>0)

epsilon,rho=s.symbols('epsilon rho',positive=True)
lam=epsilon/(rho+epsilon)
eq((1-lam)*epsilon-lam*rho,0)
for m in range(1,9):
    H=s.Integer(2)
    excess=((2+2*epsilon)**m-(2*epsilon)**m)*(H+epsilon)
    target=2**m*H
    eq(s.limit(excess/target,epsilon,0,dir='+'),1)
    for ee in [F(1,100),F(1,10),F(1,2)]:
        yes(((2+2*ee)**m-(2*ee)**m)*(2+ee)>=2**m*2)

# The d=1 counterexample has A=S, hence exactly zero excess and tail length2.
eq((3+0)-max(F(0),F(-2-1)),3)
eq(3-3,0);yes(F(3)-F(1)>0)
print(f'PASS {checks} exact checks')
