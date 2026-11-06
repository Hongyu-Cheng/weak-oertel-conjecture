"""Exact certificate checks; the note proves the all-n/local statements."""
from fractions import Fraction as F
from itertools import product


def cross(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def hull(points):
    points = sorted(set(points))
    lower, upper = [], []
    for p in points:
        while len(lower)>1 and cross(lower[-2], lower[-1], p)<=0:
            lower.pop()
        lower.append(p)
    for p in reversed(points):
        while len(upper)>1 and cross(upper[-2], upper[-1], p)<=0:
            upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]


def area(P):
    return abs(sum(p[0]*q[1]-p[1]*q[0]
                   for p,q in zip(P,P[1:]+P[:1])))/2


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def clip(P,u):
    result=[]
    for p,q in zip(P,P[1:]+P[:1]):
        a,b=dot(u,p),dot(u,q)
        if a>=0:
            result.append(p)
        if a*b<0:
            theta=a/(a-b)
            result.append(tuple(p[i]+theta*(q[i]-p[i]) for i in range(2)))
    return hull(result)


def fibers(t):
    A=hull([(F(-1,3)+t,F(-1,3)-t),
            (F(2,3),F(-1,3)+t),(F(-1,3)-t,F(2,3))])
    B=hull([(F(-1,3)-t,F(-1,3)+t),
            (F(2,3),F(-1,3)-t),(F(-1,3)+t,F(2,3))])
    D=hull([tuple((a[i]+b[i])/2 for i in range(2)) for a in A for b in B])
    return A,D,B


normals=[(-1,-1),(1,0),(0,1)]
Gamma=F(4,9); M0=F(42,25); cap0=F(6811,8910)
rho2=F(6811,1980)
assert rho2==2*cap0/Gamma and rho2<4


def mass(t):
    return F(3,2)*(1+t+2*t*t)


def cap(t):
    return (6+7*t+12*t*t-9*t**3)/(9*(1-t*t))


path_checks=0
for t in [F(9,100),F(19,200),F(99,1000),F(999,10000)]:
    bodies=fibers(t)
    assert sum(area(P) for P in bodies)==mass(t)
    for u in normals:
        assert sum(area(clip(P,u)) for P in bodies)==cap(t)
        assert all(max(dot(u,x) for x in P)==F(2,3) for P in bodies)
        path_checks+=1
    q=(M0/mass(t)+cap0/cap(t))/2
    assert 1<q<9
    assert q*mass(t)>M0 and q*cap(t)<cap0
    assert q*mass(t)==M0/2+cap0*mass(t)/(2*cap(t))
    assert q*cap(t)==M0*cap(t)/(2*mass(t))+cap0/2
    path_checks+=5

t=F(9,100); L=F(1007,1000); q=L*L
bodies=[[(L*x,L*y) for x,y in P] for P in fibers(t)]
newmass=sum(area(P) for P in bodies)
newcap=sum(area(clip(P,normals[0])) for P in bodies)
delta=newmass-M0
assert newmass==F(16826115057,10000000000)
assert delta==F(26115057,10000000000)>0
assert newcap==F(2271685752437,2975700000000)
assert cap0-newcap==F(892421526211,883782900000000)>0
assert newmass<2*cap0/Gamma
assert all(max(dot(u,x) for x in P)==2*L/3<2
           for u in normals for P in bodies)
K=[(F(-1,3),F(-1,3)),(F(2,3),F(-1,3)),(F(-1,3),F(2,3))]
for k,u in zip(K,normals):
    witness=(L*k[0],L*k[1])
    assert dot(u,witness)>0
    assert all(dot(v,witness)<0 for v in normals if v!=u)
    assert all(cross(bodies[1][i],bodies[1][(i+1)%len(bodies[1])],witness)>=0
               for i in range(len(bodies[1])))

# Verify the Farkas certificate independently.
w=F(103,200); W=F(13,20); f=F(400,891); f0=F(46,99)
for a,c,m in zip([F(-1,3),F(2,3),F(-1,3)],
                 [w*f,W*f0,w*f],[w,W,w]):
    assert a==F(142560,1339)*c-F(194600,4017)*m

isolation_checks=0
for n in range(2,8):
    zero=(0,)*(n-1)
    binary=list(product([0,1],repeat=n-1))
    P=[(z,b) for b in binary for z in range(3 if b==zero else 2)]
    regular=[p for p in P if p[1]!=zero]
    assert len(P)==2**n+1 and len(regular)==2**n-2
    assert 1+len(regular)==2**n-1
    for target_z,v in regular:
        for z,b in P:
            dist=sum(bb if vv==0 else 1-bb for bb,vv in zip(b,v))
            ell=2*dist+z if target_z==0 else 2*dist+1-z
            if (z,b)==(target_z,v):
                assert ell==0
            else:
                assert ell>=1
                if b==zero:
                    assert 2*L/3<2*ell
                else:
                    # Regular support 2sqrt(rho2)/3 < 4/3 < 2ell.
                    assert F(4,3)<2*ell
            isolation_checks+=1
    M=M0+len(regular)*cap0/Gamma
    Mnew=newmass+len(regular)*cap0/Gamma
    beta=cap0/Mnew
    assert Mnew==M+delta and beta<cap0/M
    assert beta==Gamma/(2**n-F(4978,4865)+Gamma*delta/cap0)
    assert beta>Gamma/2**n
    scale2=M/Mnew
    assert scale2*Mnew==M
    assert scale2*cap0<cap0 and scale2*newcap<cap0
    assert scale2*cap0/M==beta

print(f'PASS: {path_checks} exact near-path checks; rational core hull, '
      f'cap and strict-witness formulas; {isolation_checks} binary isolators; '
      'matching global-depth and fixed-mass normalization identities for n=2..7.')
