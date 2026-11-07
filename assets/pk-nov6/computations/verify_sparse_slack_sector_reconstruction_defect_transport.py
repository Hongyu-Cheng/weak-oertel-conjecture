"""Exact actual polygon reconstructions; no quadrilateral row inequality asserted."""
from fractions import Fraction as F
import random
import sympy as sp

checks = 0
cases = 0
def check(value):
    global checks
    assert value
    checks += 1
def det(p, q): return p[0]*q[1]-p[1]*q[0]
def sub(p, q): return (p[0]-q[0], p[1]-q[1])
def dot(p, q): return p[0]*q[0]+p[1]*q[1]
def area(P):
    return abs(sum(det(p,q) for p,q in zip(P,P[1:]+P[:1])))/2
def hull(P):
    P = sorted(set(P))
    L=[]
    for p in P:
        while len(L)>1 and det(sub(L[-1],L[-2]),sub(p,L[-1]))<=0:L.pop()
        L.append(p)
    U=[]
    for p in reversed(P):
        while len(U)>1 and det(sub(U[-1],U[-2]),sub(p,U[-1]))<=0:U.pop()
        U.append(p)
    return L[:-1]+U[:-1]
def clip(P,n):
    out=[]
    for p,q in zip(P,P[1:]+P[:1]):
        vp,vq=dot(p,n),dot(q,n)
        if vp>=0:out.append(p)
        if (vp<0<vq) or (vq<0<vp):
            z=vp/(vp-vq)
            out.append((p[0]+z*(q[0]-p[0]),p[1]+z*(q[1]-p[1])))
    return out
e=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
def raypoint(P,r):
    candidates=[]
    for a,b in zip(P,P[1:]+P[:1]):
        z=sub(b,a);den=det(r,z)
        if den:
            t=det(a,z)/den;s=det(a,r)/den
            if t>0 and 0<=s<=1:candidates.append(t)
    assert candidates and len(set(candidates))==1
    t=candidates[0]
    return(t*r[0],t*r[1])
def sectors(P):
    return [area(clip(clip(P,(-u[1],u[0])),(v[1],-v[0])))
            for u,v in zip(e,e[1:]+e[:1])]
def rat(x):return sp.Rational(x.numerator,x.denominator)
def fraction(x):return F(int(x.p),int(x.q))

def reconstruct(P):
    global cases
    P=hull(P)
    if any(det(sub(q,p),(-p[0],-p[1]))<=0 for p,q in zip(P,P[1:]+P[:1])):return
    endpoints=[raypoint(P,r) for r in e]
    W=sectors(P)
    D=[det(p,q) for p,q in zip(endpoints,endpoints[1:]+endpoints[:1])]
    excess=[F(1)/D[i]-F(1)/(2*W[i]) for i in range(6)]
    if all(excess):return
    L=sp.zeros(6)
    for i in range(6):
        prev=(i-1)%6
        kappa=D[prev]+D[i]-det(endpoints[prev],endpoints[(i+1)%6])
        L[i,i]=rat(kappa/(D[prev]*D[i])-excess[prev]-excess[i])
        j=(i+1)%6
        L[i,j]=L[j,i]=-rat(excess[i])
    remaining=set(range(6));blocks=[]
    while remaining:
        C={min(remaining)};todo=list(C)
        while todo:
            i=todo.pop()
            for j in remaining:
                if j not in C and L[i,j]<0:C.add(j);todo.append(j)
        remaining-=C;blocks.append(sorted(C))
    w=sp.zeros(6,1);singular=0;pd=0;chosen=[]
    for C in blocks:
        block=L.extract(C,C)
        null=block.nullspace()
        if null:
            check(len(null)==1);v=null[0]
            if v[0]<0:v=-v
            check(all(z>0 for z in v));singular+=1
        else:
            # Every leading principal minor is positive, exactly.
            check(all(block[:j,:j].det()>0 for j in range(1,len(C)+1)))
            j=(cases+len(C))%len(C);unit=sp.zeros(len(C),1);unit[j]=1
            v=block.inv()*unit
            check(all(z>0 for z in v));pd+=1;chosen.append(C[j])
            check(block*v==unit)
        for i,z in zip(C,v):w[i]=z
    forced=L*w
    check(all(forced[i]>0 if i in chosen else forced[i]==0 for i in range(6)))
    Q=[];aux=[]
    for i in range(6):
        j=(i+1)%6;t=rat(2*W[i]/D[i])
        if excess[i]:u=t*w[j]/(w[i]+w[j]);v=t*w[i]/(w[i]+w[j])
        else:u=v=sp.Rational(1,2)
        p=endpoints[i];q=endpoints[j]
        z=(fraction(u)*p[0]+fraction(v)*q[0],fraction(u)*p[1]+fraction(v)*q[1])
        aux.append(z);Q.extend([p,z])
        check(det(sub(z,p),sub(q,z))==(2*W[i]/D[i]-1)*D[i])
    Q=hull(Q)
    positive=sum(z>0 for z in excess)
    check(len(Q)==positive+pd==6-singular==L.rank())
    check([raypoint(Q,r) for r in e]==endpoints)
    check(sectors(Q)==W)
    check(area(Q)==area(P))
    for i in range(6):
        prev=(i-1)%6;next=(i+1)%6
        tp=rat(2*W[prev]/D[prev]);ti=rat(2*W[i]/D[i])
        up=tp*w[i]/(w[prev]+w[i]) if excess[prev] else sp.Rational(1,2)
        vi=ti*w[i]/(w[i]+w[next]) if excess[i] else sp.Rational(1,2)
        actual=det(sub(endpoints[i],aux[prev]),sub(aux[i],endpoints[i]))
        expected=fraction(up*vi*rat(D[prev]*D[i])*forced[i]/w[i])
        check(actual==expected)
    cases+=1

calibrations=[
    [(-1,2),(2,-1),(-1,-1)],
    [(-F(1),F(2)),(F(5,4),-F(1,4)),(F(5,3),-F(3,4)),(F(5,4),-F(1)),(-F(1),-F(1))],
    [(0,1),(-F(63,100),F(63,50)),(-1,1),(0,-F(11,10)),(F(61,110),-F(61,55)),(F(11,10),-F(11,10))],
    [(2,0),(0,3),(-1,0),(0,-2)],
]
for P in calibrations:reconstruct([(F(x),F(y)) for x,y in P])
random.seed(65321)
for _ in range(300):
    P=[(F(random.randrange(-12,13)),F(random.randrange(-12,13))) for __ in range(random.randrange(3,9))]
    if len(set(P))>=3:reconstruct(P)
check(cases>=100)
print(f'PASS: {checks} exact checks across {cases} actual polygon reconstructions')
