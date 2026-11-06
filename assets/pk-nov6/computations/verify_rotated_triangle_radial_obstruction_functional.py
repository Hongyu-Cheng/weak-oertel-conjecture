from fractions import Fraction as F
from itertools import product


def cross(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def hull(points):
    pts=sorted(set(points))
    lo=[]
    for p in pts:
        while len(lo)>1 and cross(lo[-2],lo[-1],p)<=0:
            lo.pop()
        lo.append(p)
    hi=[]
    for p in reversed(pts):
        while len(hi)>1 and cross(hi[-2],hi[-1],p)<=0:
            hi.pop()
        hi.append(p)
    return lo[:-1]+hi[:-1]


def area(P):
    return abs(sum(P[i][0]*P[(i+1)%len(P)][1]-P[i][1]*P[(i+1)%len(P)][0]
                   for i in range(len(P))))/2


def clip(P,u):
    out=[]
    dot=lambda x: sum(a*b for a,b in zip(x,u))
    for i,p in enumerate(P):
        q=P[(i+1)%len(P)]; a=dot(p);b=dot(q)
        if a>=0:
            out.append(p)
        if (a<0<b) or (b<0<a):
            t=a/(a-b)
            out.append(tuple(p[k]+t*(q[k]-p[k]) for k in range(2)))
    return hull(out)


def lin(P,L):
    return hull([tuple(sum(L[i][j]*p[j] for j in range(2)) for i in range(2)) for p in P])


def supp(P,u):
    return max(sum(a*b for a,b in zip(p,u)) for p in P)


def inside(P,x):
    return all(cross(P[i],P[(i+1)%len(P)],x)>=0 for i in range(len(P)))


K=hull([(F(-1,3),F(-1,3)),(F(2,3),F(-1,3)),(F(-1,3),F(2,3))])
J=[[-1,-2],[2,1]]
Iplus=[[F(int(i==j))+F(J[i][j],10) for j in range(2)] for i in range(2)]
Iminus=[[F(int(i==j))-F(J[i][j],10) for j in range(2)] for i in range(2)]
A=lin(K,Iplus);B=lin(K,Iminus)
D=hull([tuple((a[i]+b[i])/2 for i in range(2)) for a in A for b in B])
expected=[(F(-13,30),F(13,60)),(F(-1,3),F(-1,3)),(F(13,60),F(-13,30)),
          (F(2,3),F(-1,3)),(F(13,60),F(13,60)),(F(-1,3),F(2,3))]
assert D==hull(expected)
w=F(103,200);W=F(13,20);M=F(42,25);budget=F(6811,8910)
assert area(A)==area(B)==w and area(D)==W and 2*w+W==M
normals=[(-1,-1),(1,0),(0,1)]
for u in normals:
    assert area(clip(A,u))==area(clip(B,u))==F(206,891)
    assert area(clip(D,u))==F(299,990)
    assert supp(A,u)==supp(B,u)==supp(D,u)==F(2,3)
    assert area(clip(A,u))+area(clip(B,u))+area(clip(D,u))==budget
assert budget/M==F(4865,10692)<F(1,2)
assert F(299,990)/W-F(206,891)/w==F(14,891)
assert supp(A,(1,-1))==supp(B,(2,1))==F(9,10)
assert supp(B,(1,-1))==supp(A,(2,1))==F(11,10)
assert supp(D,(1,-1))==supp(D,(2,1))==1
R=[[-1,-1],[1,0]]
assert lin(A,R)==A and lin(B,R)==B and lin(D,R)==D
assert all(inside(D,p) for p in K)

scales=[F(v,100) for v in [91,94,97,100,103,106,109]]
feasible=0
for rm,r0,rp in product(scales,repeat=3):
    Ds=[(r0*x,r0*y) for x,y in D]
    points=[((rm*a[0]+rp*b[0])/2,(rm*a[1]+rp*b[1])/2) for a in A for b in B]
    if not all(inside(Ds,x) for x in points):
        continue
    feasible+=1
    a=(rm+rp)/2; b=(rm-rp)/2
    assert r0>=a+abs(b)/10
    mass=w*(rm**2+rp**2)+W*r0**2
    cap=F(206,891)*(rm**2+rp**2)+F(299,990)*r0**2
    assert cap==F(400,891)*mass+W*F(14,891)*r0**2
    if mass>=M and cap<=budget:
        assert rm==r0==rp==1

gamma=F(4,9)
assert gamma*(W+w)/M==F(233,756)>gamma/2
assert gamma*M/budget==F(4752,4865)
assert 2*budget/gamma==F(6811,1980)<4
base_checks=0
for n in range(2,8):
    binary=list(product([0,1],repeat=n-1))
    zero=(0,)*(n-1)
    P=[(z,b) for b in binary for z in range(3 if b==zero else 2)]
    assert len(P)==2**n+1
    regular=[p for p in P if p[1]!=zero]
    assert len(regular)==2**n-2
    for z,v in regular:
        for zz,b in P:
            delta=sum(bb if vv==0 else 1-bb for bb,vv in zip(b,v))
            ell=2*delta+zz if z==0 else 2*delta+1-zz
            assert ell==0 if (zz,b)==(z,v) else ell>=1
            base_checks+=1
    total=M+len(regular)*budget/gamma
    beta=budget/total
    assert beta==gamma/(2**n-F(4978,4865))
    assert beta>gamma/(2**n)

print(f'PASS: exact rotated polygons, all clipped caps/supports, {feasible} compatible radial-grid arrays, {base_checks} binary isolation inequalities and exact global-budget ratios.')
