"""Bounded numerical search only; any finding needs a separate exact proof."""
from itertools import product, combinations
from fractions import Fraction
import numpy as np
from scipy.optimize import linprog
from scipy.spatial import ConvexHull, QhullError

rng=np.random.default_rng(1729)

def sample_polygon():
    seeds=np.unique(rng.integers(-2,4,size=(rng.integers(4,9),2)),axis=0)
    try: hull=ConvexHull(seeds)
    except QhullError:return None
    P=[p for p in product(range(-2,4),repeat=2)
       if np.max(hull.equations[:,:2]@p+hull.equations[:,2])<1e-8]
    return P if 6<=len(P)<=19 else None

def setup(P):
    N=len(P);P=np.array(P,dtype=int)
    roots={}
    for i,p in enumerate(P):
        c=tuple(p%2)
        if c not in roots or (p@p,tuple(p))<(P[roots[c]]@P[roots[c]],tuple(P[roots[c]])):
            roots[c]=i
    ids={tuple(p):i for i,p in enumerate(P)}
    eq=[];ub=[]
    for i,p in enumerate(P):
        v=roots[tuple(p%2)];w=ids[tuple((p+P[v])//2)]
        row=np.zeros(3*N);row[i]+=1;row[v]+=1;row[w]-=2
        eq.append(row)
        row=np.zeros(3*N);row[i]+=1;row[v]-=1
        ub.append(row)
    for i,p in enumerate(P):
        for j,q in enumerate(P):
            row=np.zeros(3*N);row[j]+=1;row[i]-=1
            row[N+2*i:N+2*i+2]-=q-p
            ub.append(row)
    return P,roots,np.array(eq),np.array(ub)

def empty_five(P,f):
    G=np.column_stack((P,f))
    if np.linalg.matrix_rank(G[1:]-G[0],tol=1e-7)<3:return None
    try:full=ConvexHull(G)
    except QhullError:return None
    if len(full.vertices)<5:return None
    # First favor actual global vertices; then arbitrary five-subsets.
    choices=list(combinations(full.vertices,5))
    if len(G)<=13:choices+=list(combinations(range(len(G)),5))
    rng.shuffle(choices)
    for I in choices[:10000]:
        try:h=ConvexHull(G[list(I)])
        except QhullError:continue
        if len(h.vertices)!=5:continue
        inside=np.max(G@h.equations[:,:3].T+h.equations[:,3],axis=1)<1e-7
        if np.flatnonzero(inside).tolist()==sorted(I):return tuple(map(int,I))
    return None

seen=set();trials=0
for case in range(200):
    P=sample_polygon()
    if P is None or tuple(P) in seen:continue
    seen.add(tuple(P));P,roots,eq,ub=setup(P);N=len(P)
    for step in range(12):
        objective=np.r_[rng.normal(size=N),np.zeros(2*N)]
        res=linprog(objective,A_ub=ub,b_ub=np.zeros(len(ub)),
                    A_eq=eq,b_eq=np.zeros(len(eq)),
                    bounds=[(1,2)]*N+[(None,None)]*(2*N),method='highs')
        assert res.success
        trials+=1
        I=empty_five(P,res.x[:N])
        if I is not None:
            print('CANDIDATE',flush=True)
            print('P=',P.tolist(),flush=True)
            print('roots=',roots,flush=True)
            print('r=',[str(Fraction(float(v)).limit_denominator(100000)) for v in res.x[:N]],flush=True)
            print('W=',I,flush=True)
            raise SystemExit
print('No candidate in bounded screen:',len(seen),'base polygons,',trials,'LP solutions',flush=True)
