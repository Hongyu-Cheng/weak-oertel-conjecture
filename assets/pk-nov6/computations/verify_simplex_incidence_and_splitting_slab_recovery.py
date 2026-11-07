"""Exact checks supplement the written proofs; screens are separate files."""
from fractions import Fraction as F
import sympy as s
import numpy as np
from scipy.spatial import ConvexHull

checks=0
def check(v):
    global checks
    assert v
    checks+=1
def determinant(cols):
    return F(s.Matrix.hstack(*[s.Matrix(c) for c in cols]).det())

# Generic two-versus-two normalization loss, independently simplified.
p,q,r,z=s.symbols('p q r z',positive=True)
al=p*z/((p+r)*(p+z)*(q+z));de=q*r/((p+r)*(q+z)*(q+r))
Q=p*(al+de)+q*q/((q+z)*(q+r));S=3*(al+de)
N=p*q*(r+z)+r*z*(p+q)
check(s.factor((p+q)/3-Q/S-p*q*(r*z-p*q)/(3*N))==0)

# The actual balanced circuit, source, and exact cap clipping.
vertices=[(F(0),F(0),F(0)),(F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(1))]
y=(F(1,6),)*3
normals=[(-1,-5,-6),(1,0,0),(0,5,0),(0,0,6)]
dot=lambda a,b:sum(x*z for x,z in zip(a,b))
sub=lambda a,b:tuple(x-z for x,z in zip(a,b))
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def exact_cap(n):
    vals=[dot(n,sub(v,y)) for v in vertices]
    points=[v for v,t in zip(vertices,vals) if t>=0]
    for i in range(4):
        for j in range(i):
            if vals[i]*vals[j]<0:
                frac=vals[i]/(vals[i]-vals[j])
                points.append(tuple(vertices[i][l]+frac*(vertices[j][l]-vertices[i][l]) for l in range(3)))
    points=list(dict.fromkeys(points));cen=tuple(sum(v[l] for v in points)/len(points) for l in range(3))
    hull=ConvexHull(np.array(points,dtype=float))
    volume=F(0);coarea=F(0)
    for face in hull.simplices:
        a,b,c=[points[int(i)] for i in face]
        cr=cross(sub(b,a),sub(c,a))
        side=[dot(cr,sub(v,a)) for v in points]
        check(all(x>=0 for x in side) or all(x<=0 for x in side))
        volume+=abs(dot(sub(a,cen),cr))/6
        if all(dot(n,sub(v,y))==0 for v in [a,b,c]):
            j=next(i for i in range(3) if n[i])
            coarea+=abs(cr[j]/n[j])/2
    return volume*6,coarea*6,vals
expected_Q=[F(13,60)]+[F(125,216)]*3
expected_S=[F(1,4),F(25,12),F(5,12),F(25,72)]
check(all(sum(n[j] for n in normals)==0 for j in range(3)))
check(determinant(normals[1:])!=0)
capdata=[exact_cap(n) for n in normals]
for i,(Q,S,t) in enumerate(capdata):
    check(Q==expected_Q[i]);check(S==expected_S[i])
check(capdata[0][2]==[F(2),F(1),F(-3),F(-4)])
M=sum(Q/S for Q,S,_ in capdata)
check(M==F(21,5))
X=[[Q/(S*M)-v/(3*M) for v in t] for Q,S,t in capdata]
check(all(x>=0 for row in X for x in row))
check(all(sum(row[j] for row in X)==1 for j in range(4)))
lam=[F(1,2)]+[F(1,6)]*3
for row,(Q,S,t) in zip(X,capdata):check(sum(a*b for a,b in zip(lam,row))==Q/(S*M))
splits=[(F(2),F(0),F(-18,7),F(-24,7)),(F(0),F(1),F(-3,7),F(-4,7))]
check(all(sum(v[j] for v in splits)==capdata[0][2][j] for j in range(4)))
check(all(sum(a*b for a,b in zip(lam,v))==0 for v in splits))
check(sum(max(v)/3 for v in splits)-F(13,15)==F(2,15))

# All-dimensional incidence family, including both sides of its excluded
# affine-degeneracy parameter and true simplex determinants.
for d in range(2,9):
    for ai in [1,3,5,9]:
        A=F(ai,10);t=(1-A)/d
        for ci in [1,3,10,30]:
            C=F(-ci,20)
            if C==-t:continue
            B=t-(d-1)*C;D=A-d*C
            P0=(-A/d,)*d
            P=[P0]+[tuple((t+C if i==j else 0)-C for i in range(d)) for j in range(d)]
            det=determinant([sub(v,P0) for v in P[1:]])
            check(det==(t+C)**(d-1)*(A+B));check(det!=0)
            la=[B/(A+B)]+[A/(d*(A+B))]*d
            check(sum(la)==1);check(min(la)>0)
            check(all(sum(la[j]*P[j][i] for j in range(d+1))==0 for i in range(d)))
            Q0=(A/(A+B))**d;S0=d*A**(d-1)/(A+B)**d
            Q=1-A**d/D**(d-1);S=d*d*A**(d-1)/D**(d-1)
            M=Q0/S0+d*Q/S
            check(M==D**(d-1)/(d*A**(d-1)))
            check(S*M==d)
            phi0=d-1+A**(d-1)*(1-d*(d-1)*C)/D**(d-1)
            check(phi0<d);check(0<Q<1)
            u=-d*C/A
            check((1+u)**(d-1)>1+(d-1)*A*u)

# Rational polynomial estimates in the two-level-vector derivative proof.
for d in range(2,20):
    for j in range(41):
        w=F(j,40*d);r=1-w
        U=1+F(d-1,d)*r**(d-1)*(1-r)
        check(U*(1-d*w)**(d-1)<=1)

print(f'PASS: {checks} exact determinant, clipping, identity and inequality checks')
