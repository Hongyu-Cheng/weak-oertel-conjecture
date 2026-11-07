"""Explore three balanced cuts on a tetrahedron, then simplex joins.

Numerical discovery only. Common origin is the tetrahedron centroid.
"""
import itertools,json,math
from pathlib import Path
import numpy as np
from scipy.optimize import differential_evolution
from triangle_fan_search import ideal_cost

actives=list(itertools.combinations(range(6),3))


def cap_fraction(v):
    if min(abs(v[i]-v[j]) for i in range(4) for j in range(i))<1e-9:
        return None
    return sum(v[i]**3/np.prod([v[i]-v[j] for j in range(4) if j!=i]) for i in range(4) if v[i]>0)


def geometry(x):
    r0=np.array([1.,*x[:3]]);r0-=r0.mean()
    r1=np.array(x[3:7]);r1-=r1.mean()
    f=np.array([r0,r1,-r0-r1])
    if min(np.linalg.norm(v) for v in f)<1e-5:return None
    if np.linalg.svd(f[:2])[1][-1]<1e-5:return None
    beta=[cap_fraction(row) for row in f]
    if None in beta or min(beta)<=0 or max(beta)>=1:return None
    p=np.ones(4)/4
    kernel=[]
    for j in range(4):
        try:v=np.linalg.solve(np.vstack([np.ones(4),f[0],f[1],np.eye(4)[j]]),[1,0,0,0])
        except np.linalg.LinAlgError:continue
        if min(v)>-1e-9 and all(np.linalg.norm(v-w)>1e-7 for w in kernel):kernel.append(v)
    if len(kernel)!=2:return None
    theta=[];sources=[]
    for a in range(3):
        A=np.vstack([np.eye(4),-np.delete(f,a,axis=0)])
        verts=[]
        for ids in actives:
            try:v=np.linalg.solve(np.vstack([np.ones(4),A[list(ids)]]),[1,0,0,0])
            except np.linalg.LinAlgError:continue
            if min(A@v)>-1e-9 and all(np.linalg.norm(v-w)>1e-7 for w in verts):verts.append(v)
        mats=[]
        for tup in itertools.combinations(verts,3):mats.append(np.column_stack([p,*tup]))
        for tup in itertools.combinations(verts,2):mats.append(np.column_stack([*kernel,*tup]))
        if not mats:return None
        ds=abs(np.linalg.det(np.array(mats)));j=int(np.argmax(ds))
        theta.append(ds[j]);sources.append(mats[j].tolist())
    return np.array(theta),np.array(beta),f,sources


def evaluate(x,detail=False):
    g=geometry(x)
    if g is None:return 1e7
    theta,beta,f,sources=g
    gamma=1/math.e
    m=max(1.000001,max(beta)/gamma,(sum(beta)-1)/(3*gamma-1))+x[7]
    n=ideal_cost(theta,beta,m)
    if detail:return dict(ideal_n=n,theta=theta.tolist(),beta=beta.tolist(),m=m,fan=f.tolist(),sources=sources,parameters=list(x))
    return n


if __name__=='__main__':
    result=differential_evolution(evaluate,[(-2,2)]*7+[(0,3)],popsize=10,maxiter=180,seed=941,workers=1,tol=1e-7,polish=True)
    out=evaluate(result.x,True)
    print(json.dumps(out,indent=2));Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
