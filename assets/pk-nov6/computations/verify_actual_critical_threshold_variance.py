"""All caps and actual physical endpoint variation in the critical example."""
from fractions import Fraction as F


def area(poly):
    return abs(sum(poly[i][0]*poly[(i+1)%len(poly)][1]
                   -poly[i][1]*poly[(i+1)%len(poly)][0]
                   for i in range(len(poly))))/2 if poly else F(0)


def clip(poly,u,constant):
    out=[]
    def value(x):
        return u[0]*x[0]+u[1]*x[1]+constant
    for i,p in enumerate(poly):
        q=poly[(i+1)%len(poly)]
        a,b=value(p),value(q)
        if a>=0:
            out.append(p)
        if (a<0<b) or (b<0<a):
            t=a/(a-b)
            out.append(tuple(p[k]+t*(q[k]-p[k]) for k in range(2)))
    return out


def det3(a):
    return sum(a[0][i]*(a[1][(i+1)%3]*a[2][(i+2)%3]
                      -a[1][(i+2)%3]*a[2][(i+1)%3]) for i in range(3))


q=F(1,3)
K=[(-q,-q),(1-q,-q),(-q,1-q)]
C=[(-x,-y) for x,y in K]
B=[(F(1),F(0)),(F(0),F(1)),(F(-1),F(1)),
   (F(-1),F(0)),(F(0),F(-1)),(F(1),F(-1))]
assert (area(K),area(C),area(B))==(F(1,2),F(1,2),F(3))
M=area(K)+area(B)+area(C)
assert M==4
normal=[(-F(1),-F(1)),(F(1),F(0)),(F(0),F(1))]
groups=[]
for g in range(3):
    rows=[]
    for i,u in enumerate(normal):
        a=F(4,5) if i==g else F(1,10)
        ell=F(5,6) if i==g else F(5,27)
        beta=a-q
        rows.append((i,a,ell,beta,u))
        left=area(clip(K,u,-beta))
        right=area(clip(C,u,beta))
        middle=area(clip(B,u,F(0)))
        assert left==(1-a)**2*area(K)
        assert left+right==area(K)
        assert middle==area(B)/2
        assert left+middle+right==M/2==2
    assert sum(x[1] for x in rows)==1
    assert sum(x[3] for x in rows)==0
    assert all(sum(x[4][k] for x in rows)==0 for k in range(2))
    groups.append(rows)

# Combined normal rank is the full ambient dimension, unlike one group.
chosen=[groups[0][0],groups[0][1],groups[1][0]]
assert det3([[row[3],*row[4]] for row in chosen])!=0


def physical_derivatives(velocity):
    T=sum(velocity[i][i] for i in range(3))
    tr2=sum(velocity[i][j]*velocity[j][i] for i in range(3) for j in range(3))
    lag1=T
    lag2=T*T-tr2
    for rows in groups:
        for i,a,ell,beta,u in rows:
            b=velocity[i][i]
            s=sum(velocity[i][j] for j in range(3) if j!=i)
            X=1/(1-a)
            first=T+s+2*(X-1)*b
            second=-tr2-2*X*X*b*b+sum((b-velocity[i][j])**2
                                                for j in range(3) if j!=i)
            lag1-=ell*(1-a)**2*first
            lag2-=ell*(1-a)**2*(first*first+second)
    return lag1,lag2


velocities=[]
for i in range(3):
    for j in range(3):
        if i!=j:
            v=[[F(0)]*3 for _ in range(3)]
            v[i][j]=1;v[j][j]=-1
            velocities.append(v)
velocities.append([[sum((k+1)*v[i][j] for k,v in enumerate(velocities))
                    for j in range(3)] for i in range(3)])
checks=0
for velocity in velocities:
    lag1,lag2=physical_derivatives(velocity)
    c=[sum(velocity[i][j] for i in range(3) if i!=j) for j in range(3)]
    s=[sum(velocity[i][j] for j in range(3) if i!=j) for i in range(3)]
    norm=sum(velocity[i][j]**2 for i in range(3) for j in range(3) if i!=j)
    expected=-F(11,27)*sum(x*x for x in c)-F(1,3)*(sum(x*x for x in s)+norm)
    assert lag1==0 and lag2==expected<0
    t=F(1,1000)
    W=[[F(i==j)+t*velocity[i][j] for j in range(3)] for i in range(3)]
    moving=[(W[1][j]-q,W[2][j]-q) for j in range(3)]
    assert area(moving)>0
    assert all(sum(W[i][j] for i in range(3))==1 for j in range(3))
    for x in moving:
        for y in C:
            p=((x[0]+y[0])/2,(x[1]+y[1])/2)
            assert abs(p[0])<1 and abs(p[1])<1 and abs(sum(p))<1
    for rows in groups:
        for i,a,ell,beta,u in rows:
            own=area(clip(moving,u,-beta))
            own0=area(clip(K,u,-beta))
            total=own+area(clip(B,u,F(0)))+area(clip(C,u,beta))
            assert total==M/2+own-own0
            checks+=1

assert F(1,2)>F(2,9)  # Actual normalized critical value versus OC target.

# Complete binary support and explicit exposing functional. Its completeness
# is proved by conditioning on binary coordinates in the note.
from itertools import product
for n in range(2,9):
    vertices=list(product((0,1),repeat=n-1))
    zero=(0,)*(n-1)
    P=[(z,*w) for w in vertices for z in ((-1,0,1) if w==zero else (0,1))]
    assert len(P)==2**n+1
    for qbase in P:
        z0,v=qbase[0],qbase[1:]
        if v==zero:
            continue
        def expose(p):
            z,w=p[0],p[1:]
            return 3*sum(x if bit else -x for x,bit in zip(w,v))+(2*z0-1)*z
        assert all(expose(qbase)-expose(p)>=1 for p in P if p!=qbase)
    Gamma=F(4,9)
    D=F(2)
    Mn=2*D+(2**n-2)*D/Gamma
    assert D/(Gamma*Mn/2**n)==F(2**n)/(2**n-2+2*Gamma)>1
print('PASS: all nine actual critical caps, whole-space group balance, full combined rank;')
print(checks,'exact global budget-transfer checks, strict actual midpoint slack, and positive stationary negative Hessian')
print('binary support sizes, every explicit isolation functional, and exact near-OC ratios')
