"""Independent rational vertex-volume and strict-comparison audit.
The arbitrary-dimensional proof is in the audited source, not these checks.
"""
from fractions import Fraction as F
from itertools import product
checks=0
def check(b):
    global checks
    assert b
    checks+=1

def det(A):
    A=[row[:] for row in A]; n=len(A); out=F(1)
    for j in range(n):
        pivot=next((i for i in range(j,n) if A[i][j]),None)
        if pivot is None:return F(0)
        if pivot!=j:A[j],A[pivot]=A[pivot],A[j];out=-out
        q=A[j][j];out*=q
        for i in range(j+1,n):
            fac=A[i][j]/q
            for k in range(j+1,n):A[i][k]-=fac*A[j][k]
    return out

for d in range(2,11):
    raw_patterns=[(F(1),)+tuple(-F(1,d) for _ in range(d)),
                  (F(1),F(-1))+tuple(F(0) for _ in range(d-1)),
                  (F(1),F(1,2),F(-3,2))+tuple(F(0) for _ in range(d-2)),
                  (F(1),)+tuple(F(1,3) for _ in range(d-1))+(F(-1)-F(d-1,3),)]
    for r in raw_patterns:
        check(len(r)==d+1 and sum(r)==0 and r[0]==1)
        p=tuple(max(F(0),v) for v in r);sigma=sum(p)
        for beta in (F(7,6),F(3,2),F(7,3)):
            for increment in (F(1,7),F(1),F(5)):
                lam=sigma*beta+increment;a=1/(lam-1)
                D=1-sigma*beta/lam;coef=1-sigma/lam
                qs=[]
                for vertex in range(d+1):
                    mu=[F(0)]*(d+1)
                    if vertex==0:mu[0]=D/coef
                    else:mu[vertex]=D
                    q0=(mu[0]+a*beta)/(1+a)
                    q=[q0]+[mu[i]+a*p[i]*(beta-q0) for i in range(1,d+1)]
                    check(sum(q)==1 and min(q)>=0)
                    # Direct inverse F_lambda facet inequalities, all signs.
                    q_inverse=[q[i]+a*r[i]*q[0]-a*r[i]*beta for i in range(d+1)]
                    check(sum(q_inverse)==1 and min(q_inverse)>=0)
                    check(q0<beta)
                    qs.append(q)
                edges=[[qs[col+1][row+1]-qs[0][row+1] for col in range(d)] for row in range(d)]
                actual_ratio=abs(det(edges))
                stated=(lam-1)/(lam-sigma)*(1-sigma*beta/lam)**d
                check(actual_ratio==stated)
                reference=(1-beta/lam)**d
                check(actual_ratio<=reference)
                check((actual_ratio==reference)==(sigma==1))
    for beta,eta in product((F(6,5),F(3,2),F(2)),(F(1,10),F(1,3),F(2,3),F(9,10))):
        b=d*eta**(d-1)-(d-1)*eta**d
        lam=beta/(1-eta)
        check(lam*(b-(1-beta/lam)**d)==d*beta*eta**(d-1))
        check(0<b<1)
    check(d*(F(3,2))*F(5,4)-(F(5,4)-1)>d*F(3,2))

for eta in (F(1,10),F(1,3),F(2,3),F(9,10),F(1)):
    b=F(9,2)*(2*eta-eta*eta)
    check(9-2*b==(3*(1-eta))**2)
    for H in (F(7,2),F(4),F(11,2)):
        check(H*(F(9,2)*F(2,3))*eta==H*(3-3*(1-eta)))
print(f'PASS {checks} independent exact reconstructed-vertex, determinant, strictness, and optimization checks')
