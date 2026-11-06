from fractions import Fraction as F
from itertools import product
from collections import Counter

checks=0
def check(value):
    global checks
    assert value
    checks+=1

def area(poly):
    if len(poly)<3: return F(0)
    return abs(sum(poly[i][0]*poly[(i+1)%len(poly)][1]-poly[i][1]*poly[(i+1)%len(poly)][0] for i in range(len(poly))))/2

def clip(poly,u,threshold=F(0)):
    out=[]
    for i,A in enumerate(poly):
        B=poly[(i+1)%len(poly)]
        fa=sum(u[j]*A[j] for j in range(2))-threshold
        fb=sum(u[j]*B[j] for j in range(2))-threshold
        if fa>=0: out.append(A)
        if (fa<0<fb) or (fb<0<fa):
            t=fa/(fa-fb)
            out.append(tuple(A[j]+t*(B[j]-A[j]) for j in range(2)))
    return out

J=[(F(-2,3),F(-1,3)),(F(4,3),F(-1,3)),(F(-2,3),F(2,3))]
P=J[2]
check(area(J)==1)
check(tuple(sum(v[i] for v in J)/3 for i in range(2))==(0,0))
gamma=F(4,9)

# The shell identity is exact in every tested centered direction.
for r,s,u in product([F(1,2),F(1),F(3,2),F(2)], [F(0),F(1,4),F(1,2)], [(1,0),(0,1),(1,1),(1,-2),(-3,2)]):
    if s>r: continue
    large=[tuple(r*x for x in v) for v in J]
    small=[tuple(s*x for x in v) for v in J]
    cap=area(clip(large,u))-area(clip(small,u))
    check(cap==(r*r-s*s)*area(clip(J,u)))
    check(cap>=gamma*(r*r-s*s))

base=[(x,y) for x in range(-3,4) for y in range(-3,4) if x+y<=3 and y-2*x<=3 and x-2*y<=3]
listed=[(-3,-3),(-2,-2),(-2,-1),(-1,-2),(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(0,2),(0,3),(1,-1),(1,0),(1,1),(1,2),(2,0),(2,1),(3,0)]
check(base==listed)
S=set(base)
lam={z:min(F(3+2*z[0]-z[1],9),F(3-z[0]+2*z[1],9),F(3-z[0]-z[1],9)) for z in base}
check(Counter(lam.values())==Counter({F(0):9,F(1,9):6,F(2,9):3,F(1,3):1}))
radii={z:1+F(13,2)*lam[z] for z in base}
fibers={z:[tuple(P[i]+radii[z]*(v[i]-P[i]) for i in range(2)) for v in J] for z in base}
for z,poly in fibers.items():
    check(area(poly)==radii[z]**2)
    check(area(clip(poly,(0,1)))==gamma)
    check(tuple(sum(v[i] for v in poly)/3 for i in range(2))==tuple((1-radii[z])*x for x in P))

M=sum(r*r for r in radii.values())
check(M==F(219,4))
check(max(r*r for r in radii.values())==F(361,36)<M/4)
check(gamma*M/4==F(73,12))
check(M-19==F(143,4))

pairs=[(z,(-z[0],-z[1])) for z in base if z<(0,0) and (-z[0],-z[1]) in S]
check(len(pairs)==6)
res=[z for z in base if (-z[0],-z[1]) not in S]
check(res==[(-3,-3),(-2,-2),(0,2),(0,3),(2,0),(3,0)])
for scale in [2,3]:
    triple=[(-scale,-scale),(0,scale),(scale,0)]
    check(all(z in res for z in triple))
    check(tuple(sum(z[i] for z in triple) for i in range(2))==(0,0))
generic=[]
for u in product(range(-9,10),repeat=2):
    if u==(0,0):continue
    mass=sum(u[0]*z[0]+u[1]*z[1]>=0 for z in base)
    residual=sum(u[0]*z[0]+u[1]*z[1]>=0 for z in res)
    check(mass>=9)
    check(residual>=2)
    if all(u[0]*z[0]+u[1]*z[1]!=0 for z in base if z!=(0,0)):
        generic.append((mass,residual))
        check(mass==7+residual)
check(min(x[0] for x in generic)==9)
check(min(x[1] for x in generic)==2)
check(gamma*9==4)
check(gamma*13==F(52,9)<F(73,12))
check(gamma*15==F(20,3)>F(73,12))
check(F(20,3)-F(73,12)==F(7,12))
check(F(20,3)/M==F(80,657))

# Actual oblique caps of the nineteen-fiber source: supplementary exact
# checks of the stated universal bound, not a replacement for its proof.
for b1,b2,u1,u2 in product(range(-2,3),repeat=4):
    if (b1,b2,u1,u2)==(0,0,0,0):continue
    total=F(0)
    for z,poly in fibers.items():
        shift=b1*z[0]+b2*z[1]
        if u1==u2==0:
            if shift>=0: total+=area(poly)
        else:
            total+=area(clip(poly,(u1,u2),-shift))
    check(total>=F(20,3))

# The seven-chain calibration and empty-residual values.
check(gamma*(F(18,16)+F(9,16))==F(3,4))
check(F(3,4)>F(11,18))
print(f'{checks} exact checks PASS')
