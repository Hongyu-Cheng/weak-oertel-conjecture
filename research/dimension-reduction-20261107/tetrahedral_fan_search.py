"""Floating-point exploration of cyclic tetrahedral fans; not certification."""
import itertools,json,math
import numpy as np
from scipy.optimize import differential_evolution
from pathlib import Path


def data(a,b):
    c=1-a-b
    if min(a,b,c)<0: return None
    f=np.array([np.roll([1.,-a,-b,-c],j) for j in range(4)])
    # Cone paid in row 0. Barycentric vertices from 3 active inequalities.
    A=np.vstack([np.eye(4),-f[1:]])
    verts=[]
    for ids in itertools.combinations(range(7),3):
        mat=np.vstack([np.ones(4),A[list(ids)]])
        try: v=np.linalg.solve(mat,np.array([1.,0,0,0]))
        except np.linalg.LinAlgError:continue
        if min(A@v)>=-1e-9 and all(np.linalg.norm(v-w)>1e-8 for w in verts):verts.append(v)
    p=np.ones(4)/4
    theta=0.; triple=None
    for comb in itertools.combinations(verts,3):
        val=abs(np.linalg.det(np.column_stack([p,*comb])))
        if val>theta:theta=val;triple=comb
    beta=1/((1+a)*(1+b)*(1+c))
    m=(4*beta-1)/(4/math.e-1)
    if theta<=1e-12 or m<=1: return None
    cost=4*math.log1p((m-1)/(4*theta))/math.log1p(theta/m)
    return dict(a=a,b=b,c=c,theta=theta,beta=beta,m=m,ideal_n=cost,vertices=np.array(triple).tolist())


def fun(x):
    d=data(x[0],(1-x[0])*x[1]);return d['ideal_n'] if d else 1e7


if __name__=='__main__':
    res=differential_evolution(fun,[(0,1),(0,1)],popsize=10,maxiter=80,seed=17,tol=1e-7)
    report=data(res.x[0],(1-res.x[0])*res.x[1])
    print(json.dumps(report,indent=2))
    Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n')
