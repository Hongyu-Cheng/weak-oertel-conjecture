#!/usr/bin/env python3
"""Exact finite algebra for the all-D tensor stress construction."""
from fractions import Fraction as F
from itertools import product

checks = 0

def check(condition):
    global checks
    assert condition
    checks += 1

def add(x,y):
    return tuple(a+b for a,b in zip(x,y))

def scale(a,x):
    return tuple(a*b for b in x)

def dot(x,y):
    return sum(a*b for a,b in zip(x,y))

def vsum(vectors):
    result=(F(0),)*3
    for v in vectors:
        result=add(result,v)
    return result

def matvec(M,v):
    return tuple(dot(row,v) for row in M)

def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
            -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
            +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

vertices=((1,0,0),(0,1,0),(0,0,1),(-1,-1,-1))
normals=((3,-1,-1),(-1,3,-1),(-1,-1,3),(-1,-1,-1))
origin=(0,0,0)
check(vsum(vertices)==origin)
check(vsum(normals)==origin)
for j in range(4):
    for i in range(4):
        check(dot(normals[j],vertices[i])==(3 if i==j else -1))

points=[p for p in product(range(-3,4),repeat=3)
        if all(dot(u,p)>=-1 for u in normals)]
check(set(points)==set(vertices+(origin,)))
edges=tuple(add(vertices[j],scale(-1,vertices[3])) for j in range(3))
check(abs(det3(edges))==4)
volume=F(abs(det3(edges)),6)
check(volume==F(2,3))

R=((0,0,-1),(1,0,-1),(0,1,-1))
check(det3(R)==-1)
for j in range(4):
    check(matvec(R,vertices[j])==vertices[(j+1)%4])
for base in vertices[:3]:
    powers=[base]
    for j in range(3):
        powers.append(matvec(R,powers[-1]))
    check(vsum(powers)==origin)

theta=F(3,4)
gamma=theta**3
beta=(1+gamma)/5
lam=1/(4*beta)
check(gamma==F(27,64))
check(beta==F(91,320))
check(lam==F(80,91))
check(4*lam==1/beta)
check(4*lam>3)
check(4*lam-3==F(47,91))
check(lam*(4+3*theta**2)==5)
check(lam*(4+4*gamma)==5)

for j in range(4):
    section_vertices=[add(scale(F(1,4),vertices[j]),scale(F(3,4),vertices[i]))
                      for i in range(4) if i!=j]
    check(vsum(section_vertices)==origin)
    for p in section_vertices:
        check(dot(normals[j],p)==0)
    cap_centroid=scale(F(1,4),vertices[j])
    check(dot(normals[j],cap_centroid)==F(3,4))

for ell in range(4):
    face_centroid=scale(F(1,3),vsum(vertices[j] for j in range(4) if j!=ell))
    cap_centroids=[add(scale(1-theta,vertices[j]),scale(theta,face_centroid))
                   for j in range(4) if j!=ell]
    central_moment=scale(theta**2,vsum(cap_centroids))
    check(central_moment==scale(3*theta**2,face_centroid))
    weighted=scale(lam,add(scale(4,face_centroid),central_moment))
    check(weighted==scale(5,face_centroid))
    check(scale(lam,vsum(vertices))==origin)

# Unnormalized coarea: -d/ds A((3-s)/4)^3 at s=0.
coarea=volume*F(3,4)*F(3,4)**2
check(coarea==volume*gamma)
for D in range(3,101):
    check(4*lam>1/F(D,D+1)**D)
    if D>=4:
        k=D-3
        check(4*(k+1)>D+1)

print(f"PASS: {checks} exact rational checks")
