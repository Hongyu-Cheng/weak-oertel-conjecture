"""Exact actual simplex cap profiles, covariance ranks and Ito cancellation."""
from fractions import Fraction as F
from itertools import product
import sympy as sp

checks=0

def clip(poly,normal,threshold):
    out=[]
    for a,b in zip(poly,poly[1:]+poly[:1]):
        va=sum(normal[i]*a[i] for i in range(2))-threshold
        vb=sum(normal[i]*b[i] for i in range(2))-threshold
        ina,inb=va>=0,vb>=0
        if ina: out.append(a)
        if ina!=inb:
            t=va/(va-vb)
            out.append(tuple(a[i]+t*(b[i]-a[i]) for i in range(2)))
    return out

def area(poly):
    if not poly:return F(0)
    return abs(sum(a[0]*b[1]-a[1]*b[0]
                   for a,b in zip(poly,poly[1:]+poly[:1])))/2

triangle=[(F(0),F(0)),(F(1),F(0)),(F(0),F(1))]
normals=[(-1,-1),(1,0),(0,1)]
constants=[F(1),F(0),F(0)]
gamma=F(4,9)

for n in range(1,5):
    P=list(product((0,1),repeat=n))
    for v in P:
        expose=tuple(2*x-1 for x in v)
        for z in P:
            base=sum(expose[i]*(z[i]-v[i]) for i in range(n))
            for normal,const in zip(normals,constants):
                frac=2*area(clip(triangle,normal,F(1,3)-const-base))
                assert frac==(gamma if z==v else F(0))
                checks+=1
    raw=[F(1+sum((j+1)*z[j] for j in range(n))) for z in P]
    p=[x/sum(raw) for x in raw]
    m=[sum(p[i]*P[i][j] for i in range(len(P))) for j in range(n)]
    chosen=[(0,)*n]+[tuple(int(i==j) for i in range(n)) for j in range(n-1)]
    indices=[P.index(v) for v in chosen]
    cov=sp.Matrix([[sp.Rational(gamma*p[k]*(P[k][j]-m[j]))
                    for k in indices] for j in range(n)])
    expected=gamma**n*m[-1]
    for k in indices:expected*=p[k]
    assert abs(cov.det())==sp.Rational(expected)>0
    checks+=1
    # Generator on each posterior coordinate with A=vv^T. This exhausts
    # several PSD directions and directly checks the drift cancellation.
    C=[[sum(p[k]*(P[k][i]-m[i])*(P[k][j]-m[j]) for k in range(len(P)))
         for j in range(n)] for i in range(n)]
    for v in product((-1,0,1),repeat=n):
        if not any(v):continue
        A=[[F(v[i]*v[j]) for j in range(n)] for i in range(n)]
        ezAz=sum(p[k]*sum(P[k][i]*A[i][j]*P[k][j]
                         for i in range(n) for j in range(n)) for k in range(len(P)))
        Am=[sum(A[i][j]*m[j] for j in range(n)) for i in range(n)]
        for k,z in enumerate(P):
            diff=[F(z[i])-m[i] for i in range(n)]
            zAz=sum(z[i]*A[i][j]*z[j] for i in range(n) for j in range(n))
            penalty=-p[k]*(zAz-ezAz)/2
            drift=p[k]*sum(diff[i]*Am[i] for i in range(n))
            hessian=p[k]*sum(A[i][j]*(diff[i]*diff[j]-C[i][j])
                             for i in range(n) for j in range(n))/2
            assert penalty+drift+hessian==0
            checks+=1

assert gamma*F(1,3)*(0-1)==-F(4,27)
assert F(4,27)<F(2,9)
checks+=2

# Strictly nonheavy ternary products, with n selected vertices on one facet.
for n in range(1,5):
    P=list(product((-1,0,1),repeat=n))
    selected=[(1,)*n]+[tuple(-1 if i==j else 1 for i in range(n))
                        for j in range(n-1)]
    raw=[F(2+sum((i+1)*(z[i]+1) for i in range(n))) for z in P]
    p=[x/sum(raw) for x in raw]
    m=[sum(p[k]*P[k][j] for k in range(len(P))) for j in range(n)]
    indices=[P.index(v) for v in selected]
    mat=sp.Matrix([[sp.Rational(gamma*p[k]*(P[k][j]-m[j]))
                    for k in indices] for j in range(n)])
    expected=gamma**n*2**(n-1)*(1-m[-1])
    for k in indices:expected*=p[k]
    assert abs(mat.det())==sp.Rational(expected)>0
    assert F(1,3**n)<F(1,2**n)
    assert gamma/F(3**n)<gamma/F(2**n)
    checks+=3
    for v,z in product(selected,P):
        base=sum(v[i]*(z[i]-v[i]) for i in range(n))
        for normal,const in zip(normals,constants):
            frac=2*area(clip(triangle,normal,F(1,3)-const-base))
            assert frac==(gamma if z==v else F(0))
            checks+=1
print(f'{checks} exact checks PASS; actual cap clipping, full rank and PSD Ito directions')
