"""Exact cubic identities and actual simultaneous corner truncations."""
from fractions import Fraction as F
import random
import sympy as sp
checks=0
def check(x):
    global checks
    assert x
    checks+=1
u,v,w=sp.symbols('u v w');U=[u,v,w]
square=[4*U[i]*(1-U[(i+1)%3]) for i in range(3)]
P=u*v*w;Q=(1-u)*(1-v)*(1-w)
check(sp.expand(4-sum(square)-4*(P+Q))==0)
check(sp.expand(sp.prod(square)-64*P*Q)==0)
x,p=sp.symbols('x p',positive=True);C=8+p;E=2*x*x+p
check(sp.expand(4*E-C*x*x-p*(4-x*x))==0)
d1,d2,d3=sp.symbols('d1 d2 d3');d=[d1,d2,d3]
sq=[(1-d[(i+1)%3]+d[(i+2)%3])**2-d[i]**2 for i in range(3)]
R=4-sum(sq);J=8*d1*d2*d3-(d1+d2+d3)*R
check(sp.factor(R*R-sp.prod(sq)-J*J)==0)

def det(a,b):return a[0]*b[1]-a[1]*b[0]
def sub(a,b):return(a[0]-b[0],a[1]-b[1])
def dot(a,b):return a[0]*b[0]+a[1]*b[1]
def hull(P):
    P=sorted(set(P));lo=[];up=[]
    for p in P:
        while len(lo)>1 and det(sub(lo[-1],lo[-2]),sub(p,lo[-1]))<=0:lo.pop()
        lo.append(p)
    for p in reversed(P):
        while len(up)>1 and det(sub(up[-1],up[-2]),sub(p,up[-1]))<=0:up.pop()
        up.append(p)
    return lo[:-1]+up[:-1]
def area(P):return abs(sum(det(p,q) for p,q in zip(P,P[1:]+P[:1])))/2
def clip(P,n,b=F(0)):
    out=[]
    for p,q in zip(P,P[1:]+P[:1]):
        vp,vq=dot(p,n)-b,dot(q,n)-b
        if vp>=0:out.append(p)
        if vp*vq<0:
            z=vp/(vp-vq);out.append((p[0]+z*(q[0]-p[0]),p[1]+z*(q[1]-p[1])))
    return out
e=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
normals=[(1,0),(0,1),(-1,-1)]
def raypoint(P,r):
    vals=[]
    for a,b in zip(P,P[1:]+P[:1]):
        q=sub(b,a);den=det(r,q)
        if den:
            t=det(a,q)/den;s=det(a,r)/den
            if t>0 and 0<=s<=1:vals.append(t)
    assert vals and len(set(vals))==1
    return(vals[0]*r[0],vals[0]*r[1])
def raw(P):
    k=area(P);q=[area(clip(P,n)) for n in normals]
    r=[raypoint(P,t) for t in e]
    sigma=[r[1][1]-r[4][1],r[0][0]-r[3][0],r[5][0]-r[2][0]]
    m=sum(a/b for a,b in zip(q,sigma))
    fsq=[4*k*a/(b*b*m*m) for a,b in zip(q,sigma)]
    return k,q,sigma,fsq,r
random.seed(60017)
for _ in range(150):
    dd=[F(random.randrange(-8,9),30) for __ in range(3)]
    eps=1-sum(abs(z) for z in dd)
    if eps<=0:continue
    ss=[abs(z)+eps/3 for z in dd]
    gg=[1-dd[(i+1)%3]+dd[(i+2)%3] for i in range(3)]
    aa=[(gg[i]-ss[i])/2 for i in range(3)]
    matrix=[[F(0) for __ in range(3)] for ___ in range(3)]
    for i in range(3):
        matrix[i][i]=aa[i]
        matrix[i][(i+1)%3]=-(ss[i]+dd[i])/2
        matrix[i][(i+2)%3]=-(ss[i]-dd[i])/2
    vertices=[(matrix[0][j],matrix[1][j]) for j in range(3)]
    T=hull(vertices);K=T[:];k0,q0,sigma0,fsq0,rays=raw(T)
    rr=4-sum(fsq0)
    check(rr>0 and rr*rr>=fsq0[0]*fsq0[1]*fsq0[2])
    losses=[]
    for i,(a,b) in enumerate([(5,0),(1,2),(3,4)]):
        V=vertices[i];A=rays[a];B=rays[b];t=F(random.randrange(1,10),10)
        U=(V[0]+t*(A[0]-V[0]),V[1]+t*(A[1]-V[1]))
        W=(V[0]+t*(B[0]-V[0]),V[1]+t*(B[1]-V[1]))
        edge=sub(W,U);n=(-edge[1],edge[0]);level=dot(U,n)
        if level>0:n=(-n[0],-n[1]);level=-level
        K=clip(K,n,level)
        losses.append(area([V,U,W]))
    k,q,sigma,fsq,rayK=raw(K)
    check(k==k0-sum(losses))
    check(q==[q0[i]-losses[i] for i in range(3)])
    check(sigma==sigma0 and rayK==rays)
    R=4-sum(fsq)
    check(R>0 and R*R>fsq[0]*fsq[1]*fsq[2])
print(f'PASS: {checks} exact cubic and actual simultaneous-truncation checks')
