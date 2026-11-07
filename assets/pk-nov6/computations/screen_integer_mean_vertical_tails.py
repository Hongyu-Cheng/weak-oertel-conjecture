"""Numerical falsification screen only: concave height functions on lattice polygons."""
import json, math, random, pathlib
import numpy as np
from scipy.optimize import linprog
from scipy.spatial import ConvexHull
from scipy.sparse import coo_matrix

rng=random.Random(39129)
best=1.0
best_record=None
for trial in range(55):
    raw=np.array(list(set([(rng.randrange(-4,5),rng.randrange(-4,5)) for _ in range(9)])),float)
    try: hull=ConvexHull(raw)
    except Exception: continue
    if max(hull.equations[:,-1])>=-1e-8: continue
    points=np.array([(i,j) for i in range(-4,5) for j in range(-4,5)
                     if np.max(hull.equations[:,:2]@np.array([i,j])+hull.equations[:,2])<1e-8],float)
    N=len(points)
    rows=[];cols=[];vals=[];rr=0
    for i in range(N):
        for j in range(N):
            if i==j: continue
            rows.extend([rr,rr,rr,rr]);cols.extend([j,i,N+2*i,N+2*i+1])
            vals.extend([1,-1,-(points[j,0]-points[i,0]),-(points[j,1]-points[i,1])]);rr+=1
    mat=coo_matrix((vals,(rows,cols)),shape=(rr,3*N)).tocsr()
    eq=np.zeros((3,3*N));eq[0,:N]=1;eq[1,:N]=points[:,0];eq[2,:N]=points[:,1]
    angles=sorted(set(round(math.atan2(p[1],p[0])+math.pi/2,12)%(2*math.pi)
                      for p in points if any(p)))
    dirs=[]
    for k in range(len(angles)):
        t=(angles[k]+(angles[(k+1)%len(angles)]+(2*math.pi if k+1==len(angles) else 0)))/2
        dirs.append(np.array([math.cos(t),math.sin(t)]))
    rng.shuffle(dirs)
    for normal in dirs[:18]:
        obj=np.zeros(3*N);obj[:N]=(points@normal>=-1e-10)
        out=linprog(obj,A_ub=mat,b_ub=np.zeros(rr),A_eq=eq,b_eq=[1,0,0],
                    bounds=[(0,None)]*N+[(None,None)]*(2*N),method='highs')
        if out.success and out.fun<best-1e-7:
            best=out.fun
            best_record=dict(trial=trial,value=best,vertices=raw[hull.vertices].tolist(),
                             points=points.tolist(),normal=normal.tolist(),
                             heights=out.x[:N].tolist(),supergradients=out.x[N:].reshape(N,2).tolist())
            pathlib.Path('./integer_mean_vertical_tail_screen_best.json').write_text(json.dumps(best_record,indent=2))
            print('best',trial,N,best,raw[hull.vertices].astype(int).tolist(),flush=True)
print('done',best,flush=True)
