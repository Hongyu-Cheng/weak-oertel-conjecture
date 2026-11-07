from fractions import Fraction as Q
from itertools import product, combinations

checks = 0
def check(c):
    global checks
    assert c
    checks += 1

def feasible(p):
    x,y,z=p
    return min(p)>=0 and y+z<=2 and x+y-z<=2 and x-y+z<=2

def interval(p):
    x,y,z=map(Q,p)
    return max(Q(0),(x+y+z-2)/2), min(x/2,y,z)

P={p for p in product(range(3),repeat=3) if feasible(p)}
old={p for p in product(range(3),repeat=3) if sum(p)<=2}
a=(1,1,1); r=(2,1,1)
check(len(P)==12)
check(P==old|{a,r})
b={p:Q(0) for p in old}; b[a]=Q(1,2); b[r]=Q(1)
for p in product(range(-2,5),repeat=3):
    lo,hi=interval(p)
    check(feasible(p)==(lo<=hi))
for p in P:
    check(interval(p)==(b[p],b[p]))
    x,y,z=map(Q,p); t=b[p]
    lam=[1-(x+y+z)/2+t,x/2-t,y/2-t/2,z/2-t/2,t]
    check(min(lam)>=0 and sum(lam)==1)
check(interval((Q(1,2),)*3)==(Q(0),Q(1,4)))

def parity(p): return tuple(x%2 for x in p)
check(len({parity(p) for p in P})==8)
zero=(0,0,0); v1=(2,0,0); v2=(0,2,0); v3=(0,0,2)
F={p for p in P if p[1]+p[2]==2}
check(F=={v2,v3,(0,1,1),a,r})
edges=[(zero,v1),(zero,v2),(zero,v3),(v1,v2),(v1,v3)]
pieces=[F]
for u,v in edges:
    m=tuple((u[i]+v[i])//2 for i in range(3))
    E={u,m,v}; pieces.append(E)
    check(E<=P)
    check(all(b[p]==0 for p in E))
check(set.union(*pieces)==P)
check(all(b[p]==Q(p[0],2) for p in F))
seen={0}
while True:
    new=seen|{j for j in range(len(pieces)) if any(pieces[i]&pieces[j] for i in seen)}
    if new==seen:break
    seen=new
check(len(seen)==len(pieces))
# Enumerate relative interior lattice points of each facet, using all
# other displayed inequalities strictly. Facet intersections are edges.
slacks=lambda p:[p[0],p[1],p[2],2-p[1]-p[2],2-p[0]-p[1]+p[2],2-p[0]+p[1]-p[2]]
for i in range(6):
    interior={p for p in P if slacks(p)[i]==0 and all(v>0 for j,v in enumerate(slacks(p)) if j!=i)}
    check(interior==({a} if i==3 else set()))
# Full integer-output support compatibility follows from singleton hull;
# explicitly check all midpoint relations as a finite independent test.
for u,v in combinations(P,2):
    if parity(u)==parity(v):
        m=tuple((u[i]+v[i])//2 for i in range(3))
        check(m in P)
        check(b[m]==(b[u]+b[v])/2)
# Exact cost-nine partition.
partition=[F,{zero,(1,0,0),v1}]+[{p} for p in [(0,1,0),(0,0,1),(1,1,0),(1,0,1)]]
check(sum(map(len,partition))==12 and set.union(*partition)==P)
check(sum(len({parity(p) for p in E}) for E in partition)==9)
for j in [12,13,100,1000]:
    eps=Q(1,12*j); M=24*eps**2; alpha=1/(M*j)
    check(M==Q(1,6*j*j))
    check(alpha==6*j and alpha*2*eps==1)
    check(Q(j**3,6)>12*j)
check({p for p in P if p[0]-3*(p[1]+p[2])>=1}=={(1,0,0),v1})
check(b[(1,0,0)]==(b[zero]+b[v1])/2)
print(f'PASS: {checks} exact rational/integer checks')
