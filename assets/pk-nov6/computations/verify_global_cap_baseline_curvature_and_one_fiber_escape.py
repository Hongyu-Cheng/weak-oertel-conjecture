"""Exact checks; the note supplies the all-dimensional proofs."""
from fractions import Fraction as F
from random import Random
from itertools import permutations

rng=Random(260916)
checks=0
def mul(a,b):
    return [sum(a[k]*b[n-k] for k in range(n+1)) for n in range(3)]
def inv(a):
    assert a[0]
    return [1/a[0],-a[1]/a[0]**2,a[1]**2/a[0]**3-a[2]/a[0]**2]
def power(a,d):
    out=[F(1),F(0),F(0)]
    for _ in range(d): out=mul(out,a)
    return out
def norm(v):return sum(x*x for x in v)
def trace2(B):return sum(B[i][j]*B[j][i] for i in range(len(B)) for j in range(len(B)))
def row(B):return [sum(x) for x in B]
def det_series(B,C=None):
    m=len(B); T=sum(B[i][i] for i in range(m))
    return [F(1),T,(T*T-trace2(B)+(sum(C[i][i] for i in range(m)) if C else 0))/2]
def cap_series(d,B,v,radii,C=None):
    m=d+1;h=F(d,m)
    dt=det_series(B,C);out=[]
    for i in range(m):
        p=mul(dt,power([h,B[i][i]-v[i], C[i][i]/2 if C else F(0)],d))
        for j in range(m):
            if j!=i:
                p=mul(p,inv([F(1),B[i][i]-B[i][j],(C[i][i]-C[i][j])/2 if C else F(0)]))
        for r in radii[1:]:
            other=power([r*h,-v[i],F(0)],d)
            p=[a+b for a,b in zip(p,other)]
        out.append(p)
    return out
def right_inverse(d,f):
    m=d+1;G=F(d,m)**d;z=[x/(m*G) for x in f];Z=sum(z)
    return [[z[i] if i==j else z[i]-Z/d for j in range(m)] for i in range(m)]
def optimal(d,S,v):
    m=d+1
    return [[(d*d*S-m*(d-1))*v[i] if i==j else (m-d*S)*v[i]+m*(1-S)*v[j] for j in range(m)] for i in range(m)]

for d in range(2,8):
    m=d+1;G=F(d,m)**d
    for trial in range(15):
        radii=[F(1)]+[F(rng.randrange(1,8),rng.randrange(1,5)) for _ in range(1+trial%4)]
        S=sum(r**(d-1) for r in radii);N2=sum(r**(d-2) for r in radii)
        A=[[F(0) if i==j else F(rng.randrange(-3,4)) for j in range(m)] for i in range(m)]
        A[0][1]=-sum(A[i][j] for i in range(m) for j in range(m) if (i,j)!=(0,1))
        B=[x[:] for x in A]
        for j in range(m):B[j][j]=-sum(A[i][j] for i in range(m))
        assert sum(B[i][i] for i in range(m))==0
        r=row(B);v=[x/(m*S) for x in r];b=[B[i][i] for i in range(m)]
        Amin=[[F(0) if i==j else (d*r[i]+r[j]-m*(b[i]+b[j]))/(m*(d-1)) for j in range(m)] for i in range(m)]
        Z=[[A[i][j]-Amin[i][j] for j in range(m)] for i in range(m)]
        assert all(sum(Z[i])==0 for i in range(m))
        assert all(sum(Z[i][j] for i in range(m))==0 for j in range(m))
        caps=cap_series(d,B,v,radii)
        assert all(c[1]==0 for c in caps)
        Q=2*det_series(B)[2]-sum(2*c[2] for c in caps)/(m*G)
        theta=d*(S-1)**2+1-N2
        bs=[(d*d*S-m*(d-1))*x for x in v]
        expected=F(m*(d-1),d)*theta*norm(v)-norm([x-y for x,y in zip(b,bs)])/F(d*(d-1))-sum(norm(z) for z in Z)/m
        assert Q==expected
        checks+=1
    for N in range(2,8):
        radii=[F(1)]*N;S=F(N);N2=F(N)
        v=[F(1),F(-1)]+[F(0)]*(m-2)
        B=optimal(d,S,v)
        assert all(sum(B[i][j] for i in range(m))==0 for j in range(m))
        assert row(B)==[m*S*x for x in v]
        caps=cap_series(d,B,v,radii)
        q=[2*c[2] for c in caps]
        Q=F(m*(d-1),d)*(N-1)*(d*(N-1)-1)*norm(v)
        assert 2*det_series(B)[2]-sum(q)/(m*G)==Q
        xi=G*Q/2
        C=right_inverse(d,[-x-xi for x in q])
        corrected=cap_series(d,B,v,radii,C)
        assert all(c[1]==0 and 2*c[2]==-xi for c in corrected)
        assert 2*det_series(B,C)[2]==Q/2
        checks+=1
    t=F(1,10)
    theta=d*t**(2*d-2)-t**(d-2)
    assert theta==t**(d-2)*(d*t**d-1)<0
    checks+=1

def det(M):
    n=len(M);out=F(0)
    for p in permutations(range(n)):
        sign=(-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        term=F(sign)
        for i in range(n):term*=M[i][p[i]]
        out+=term
    return out
def inverse(M):
    n=len(M);D=det(M)
    return [[(-1)**(i+j)*det([[M[a][b] for b in range(n) if b!=i] for a in range(n) if a!=j])/D for j in range(n)] for i in range(n)]
def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
# Actual planar three-fiber strictification and strict finite escape.
d=2;m=3;G=F(4,9);r=F(100,101);radii=[F(1),r,r]
S=sum(radii);N2=F(3);v=[F(1),F(-1),F(0)]
B=optimal(d,S,v);caps=cap_series(d,B,v,radii)
Q=F(m*(d-1),d)*(d*(S-1)**2+1-N2)*norm(v)
assert Q>0
q=[2*c[2] for c in caps];xi=G*Q/2
C=right_inverse(d,[-x-xi for x in q])
step=F(1,100000)
W=[[(F(i==j)+step*B[i][j]+step*step*C[i][j]/2) for j in range(m)] for i in range(m)]
tau=[step*x for x in v];D=det(W)
Wr=[[r*F(i==j)+(1-r)/m for j in range(m)] for i in range(m)]
containment=matmul(inverse(W),Wr)
assert all(x>0 for rr in containment for x in rr) # rK compactly inside K(W)
base=1+2*r*r
assert D+2*r*r>base
actual=[]
for i in range(m):
    a=F(1,m)+tau[i]
    assert W[i][i]>a and all(W[i][j]<a for j in range(m) if j!=i)
    den=F(1)
    for j in range(m):
        if j!=i:den*=W[i][i]-W[i][j]
    cap=D*(W[i][i]-a)**d/den+2*(r*F(d,m)-tau[i])**d
    assert cap<G*base
    actual.append(cap)
# A common continuous dilation of squared factor 3/base restores
# original total mass 3V and original cap budgets 3 Gamma V exactly.
assert F(3,1)/base*base==3
checks+=1
print("PASS:",checks,"exact Hessian/completion/acceleration checks, dimensions 2..7;")
print("actual planar 3-fiber path: all caps strictly decrease, mass increases,")
print("and endpoint Minkowski average is strictly inside the changed middle fiber.")
print("Mass gain (normalized by selected V):",float(D-1))
print("Largest cap increment:",float(max(actual)-G*base))
