"""Falsification screen only: no numerical result proves an inequality."""
import numpy as np
from scipy.spatial import ConvexHull
from pathlib import Path
import json
rng=np.random.default_rng(938133)
normals=np.vstack((np.eye(3),-np.ones(3)))
best=1e9
for it in range(3000):
    p=rng.normal(size=(int(rng.integers(5,23)),3))
    p*=np.exp(rng.normal(size=(len(p),1)))
    h=ConvexHull(p);p=p[h.vertices]
    weights=rng.dirichlet(np.ones(len(p))*rng.uniform(.05,3))
    y=weights@p;p=p-y
    h=ConvexHull(p);volume=h.volume
    edges=set()
    for tri in h.simplices:
        for a,b in ((0,1),(1,2),(0,2)):
            edges.add(tuple(sorted((int(tri[a]),int(tri[b])))))
    qs=[];ss=[]
    for v in normals:
        vals=p@v
        cross=[p[a]+vals[a]/(vals[a]-vals[b])*(p[b]-p[a]) for a,b in edges if vals[a]*vals[b]<0]
        c=np.array(cross)
        q=ConvexHull(np.vstack((p[vals>=0],c))).volume/volume
        _,_,vh=np.linalg.svd(v.reshape(1,3),full_matrices=True)
        area=ConvexHull(c@vh[1:].T).volume/np.linalg.norm(v)
        qs.append(q);ss.append(area)
    q=np.array(qs);s=np.array(ss)
    a=q/s;a/=a.sum();f=3*a/q**(1/3)
    deficits=3-f-2*((f.sum()-f)/3)**1.5
    z=deficits.min()
    if z<best:
        best=z
        np.savez('./general_body_joint_rows_d3_best_root.npz',points=p,normal=normals,q=q,sigma=s,f=f,deficit=deficits)
    if z< -1e-7:
        print('CANDIDATE COUNTEREXAMPLE',it,z,q,f,flush=True);break
    if it%250==0:print(it,'minimum deficit',best,flush=True)
else: print('SCREEN COMPLETE minimum deficit',best,flush=True)
