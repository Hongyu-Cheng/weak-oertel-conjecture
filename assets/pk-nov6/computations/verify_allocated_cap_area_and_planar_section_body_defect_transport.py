"""Exact polygon checks for the allocated planar section-body theorem."""
from fractions import Fraction as F
from math import gcd, lcm

checks = 0


def check(cond):
    global checks
    assert cond
    checks += 1


def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])


def hull(points):
    pts = sorted(set((F(x),F(y)) for x,y in points))
    if len(pts) <= 1:
        return pts
    lower, upper = [], []
    for p in pts:
        while len(lower)>=2 and cross(lower[-2],lower[-1],p)<=0:
            lower.pop()
        lower.append(p)
    for p in reversed(pts):
        while len(upper)>=2 and cross(upper[-2],upper[-1],p)<=0:
            upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]


def area(poly):
    return abs(sum(poly[i][0]*poly[(i+1)%len(poly)][1]
                   -poly[i][1]*poly[(i+1)%len(poly)][0]
                   for i in range(len(poly))))/2 if poly else F(0)


def scale(poly, a):
    return hull([(a*x,a*y) for x,y in poly])


def add(A, B):
    return hull([(x+u,y+v) for x,y in A for u,v in B])


def support(poly, u):
    return max(u[0]*x+u[1]*y for x,y in poly)


def clip(poly, u, c):
    out = []
    for i,p in enumerate(poly):
        q=poly[(i+1)%len(poly)]
        fp=u[0]*p[0]+u[1]*p[1]-c
        fq=u[0]*q[0]+u[1]*q[1]-c
        if fp>=0:
            out.append(p)
        if fp*fq<0:
            a=fp/(fp-fq)
            out.append((p[0]+a*(q[0]-p[0]),p[1]+a*(q[1]-p[1])))
    return hull(out)


def primitive(n):
    den=lcm(n[0].denominator,n[1].denominator)
    x,y=int(n[0]*den),int(n[1]*den)
    g=gcd(abs(x),abs(y))
    return (x//g,y//g),F(g,den)


def surf(poly):
    """Store mass at primitive n as rational coefficient times |n|."""
    ans={}
    if len(poly)<2:
        return ans
    for i,p in enumerate(poly):
        q=poly[(i+1)%len(poly)]
        n,c=primitive((q[1]-p[1],p[0]-q[0]))
        ans[n]=ans.get(n,F(0))+c
    return ans


def measures(*terms):
    ans={}
    for c,m in terms:
        for n,v in m.items():
            ans[n]=ans.get(n,F(0))+c*v
    return {n:v for n,v in ans.items() if v}


T=hull([(2,-1),(-1,2),(-1,-1)])
us=[(1,0),(0,1),(-1,-1)]
caps=[clip(T,u,F(0)) for u in us]
comps=[clip(T,(-u[0],-u[1]),F(0)) for u in us]
beta,a=F(4,9),F(2,3)
check(area(T)==F(9,2))
for C in caps:
    check(area(C)==2)
    check(surf(C)==measures((a,surf(T))))
A=add(add(scale(caps[0],F(1,3)),scale(caps[1],F(1,3))),scale(caps[2],F(1,3)))
Ac=add(add(scale(comps[0],F(1,3)),scale(comps[1],F(1,3))),scale(comps[2],F(1,3)))
J=scale(T,F(2,9))
check(surf(A)==measures((beta,surf(T)),(1,surf(J))))
check(surf(Ac)==measures((1-beta,surf(T)),(1,surf(scale(J,-1)))))
check(A==scale(T,a))
check(surf(J)=={(-1,0):F(2,3),(0,-1):F(2,3),(1,1):F(2,3)})
for u in surf(T):
    check(support(scale(J,-1),u)<=beta*support(T,u))
    check(support(scale(J,-1),u)==beta*support(T,u))
check(2*(a-beta)==beta)
check(area(J)==F(4,81)*area(T))

# Exact all-status identities at a rectangle's right supporting edge.
K=hull([(-2,-1),(2,-1),(2,1),(-2,1)])
SK=surf(K)
for den in range(1,31):
    for num in range(den+1):
        alpha=F(num,den)
        m=2*alpha
        selected_out={(1,0):m} if m else {}
        sec_out={(-1,0):m} if m else {}
        effective=surf(hull([(2,-alpha),(2,alpha)]))
        check(effective==measures((1,selected_out),(1,sec_out)))
        inside_body=measures((1,SK),(-1,selected_out))
        inside_sec={(1,0):m} if m else {}
        check(measures((1,inside_body),(1,inside_sec))==SK)
        check(effective=={(1,0):m,(-1,0):m} if m else effective=={})

# The anchored three-fiber conversion is exact and its M-constant tends9.
last=F(0)
for R in range(1,101):
    rr=F(R)
    Km=hull([(-rr,-1/rr),(rr,-1/rr),(rr,1/rr),(-rr,1/rr)])
    Kp=hull([(-1/rr,-rr),(1/rr,-rr),(1/rr,rr),(-1/rr,rr)])
    K0=scale(add(Km,Kp),F(1,2))
    B=add(add(Km,K0),Kp)
    check(B==scale(K0,3))
    check(surf(B)==measures((1,surf(Km)),(1,surf(K0)),(1,surf(Kp))))
    M=area(Km)+area(K0)+area(Kp)
    ratio=area(B)/M
    check(ratio==9*(rr+1/rr)**2/((rr+1/rr)**2+8))
    check(ratio<9)
    check(ratio>=last)
    last=ratio

# Nonnegative affine weights on the three-site chain have middle mean
# exactly when their slope vanishes. Normalizing then scales J by1/3.
for aa in range(1,16):
    for bb in range(-aa,aa+1):
        omega={z:F(aa+bb*z) for z in [-1,0,1]}
        total=sum(omega.values())
        mean=sum(z*omega[z] for z in omega)/total
        check(mean==F(2*bb,3*aa))
        check((mean==0)==(bb==0))
        if mean==0:
            check(all(omega[z]/total==F(1,3) for z in omega))

print(f'PASS: {checks} exact allocated area-measure and section-body checks')
