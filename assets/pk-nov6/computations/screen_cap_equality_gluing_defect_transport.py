"""Exact nullspace screen of possible polygon cap-equality deformations."""
import random
import sympy as s
from scipy.spatial import ConvexHull
import numpy as np

random.seed(94721)
normals=[(1,0),(0,1),(-1,-1)]
tested=0
for trial in range(1000):
    points=list({(random.randint(-8,8),random.randint(-8,8)) for _ in range(12)})
    try:
        hull=ConvexHull(np.array(points))
    except Exception:
        continue
    P=[points[i] for i in hull.vertices]
    # Permit either interior or exterior origin; the latter still must pass proper cuts.
    vals=[[u[0]*p[0]+u[1]*p[1] for p in P] for u in normals]
    if any(min(v)>=0 or max(v)<=0 for v in vals):
        continue
    if any(0 in v for v in vals):
        continue
    m=len(P)
    nvar=2*m+9
    rows=[]
    for i,u in enumerate(normals):
        # lambda_i, vx_i, vy_i at 2m+3i.
        o=2*m+3*i
        row=[0]*nvar
        row[o+1],row[o+2]=u
        rows.append(row)
        for j,p in enumerate(P):
            if vals[i][j]>0:
                for dim in range(2):
                    row=[0]*nvar
                    row[2*j+dim]=1
                    row[o]=-p[dim]
                    row[o+1+dim]=-1
                    rows.append(row)
    for j,p in enumerate(P):
        k=(j+1)%m
        dx,dy=P[k][0]-p[0],P[k][1]-p[1]
        row=[0]*nvar
        row[2*k],row[2*j]=dy,-dy
        row[2*k+1],row[2*j+1]=-dx,dx
        rows.append(row)
    ns=s.Matrix(rows).nullspace()
    hom=s.Matrix([[p[0],1,0,p[1],0,1] for p in P]) if False else s.Matrix(2*m,3,lambda i,j: P[i//2][i%2] if j==0 else int(j==i%2+1))
    bad=[]
    for vec in ns:
        q=vec[:2*m,:]
        if hom.row_join(q).rank()>3:
            bad.append(vec)
    tested+=1
    if bad:
        print('POTENTIAL NONHOMOTHETIC MODE',P)
        print('inside',all(row[-1]<0 for row in hull.equations))
        print('dimension',len(ns),'mode',list(bad[0]))
        break
else:
    print('NO NONHOMOTHETIC MODE in',tested,'exact nullspace cases')
