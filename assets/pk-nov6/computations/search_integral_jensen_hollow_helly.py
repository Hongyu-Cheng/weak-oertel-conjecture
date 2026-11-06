"""Bounded exploratory search. Numerical geometry only screens; candidates require exact audit.
Runs reproducibly with --seconds, --seed. An emitted candidate includes a rational height vector.
"""
import argparse,itertools,json,random,time
from collections import deque
from fractions import Fraction
from math import lcm
import numpy as np
import sympy as sp
from scipy.spatial import ConvexHull,QhullError
from sympy.matrices.normalforms import hermite_normal_form

parser=argparse.ArgumentParser();parser.add_argument('--seconds',type=float,default=180);parser.add_argument('--seed',type=int,default=77119)
args=parser.parse_args();rng=random.Random(args.seed);started=time.monotonic()
box=list(itertools.product(range(3),repeat=3))
simplex=[p for p in itertools.product(range(4),repeat=3) if sum(p)<=3]
old=[(0,0,1),(0,0,3),(0,1,3),(0,2,1),(1,0,0),(1,2,0),(2,0,0)]
seen=set();stats=dict(generated=0,hollow=0,nonaffine=0,nine=0,forced=0,character_reject=0)


def lattice_hull(V):
    V=np.array(V,dtype=int)
    try:H=ConvexHull(V)
    except QhullError:return None
    lo=V.min(axis=0);hi=V.max(axis=0)
    if np.prod(hi-lo+1)>300:return None
    candidates=np.array(list(itertools.product(*(range(int(a),int(b)+1) for a,b in zip(lo,hi)))))
    residual=(candidates[:,None,:]*H.equations[None,:,:3]).sum(axis=2)+H.equations[:,3]
    inside=np.max(residual,axis=1)<=1e-8
    if any(np.max(residual[inside],axis=1)<-1e-8):return None
    P=candidates[inside]
    if not 9<=len(P)<=22:return None
    return P,ConvexHull(P)


def features(P,H):
    active=np.abs((P[:,None,:]*H.equations[None,:,:3]).sum(axis=2)+H.equations[:,3])<1e-8
    faces={tuple(np.flatnonzero(np.all(active[:,active[i]],axis=1))) for i in range(len(P))}
    E=sp.Matrix([[1,*map(int,p)] for p in P])
    relations=[]
    for F in faces:
        if len(F)<=2:continue
        for v in E[list(F),:].T.nullspace():
            row=[0]*len(P)
            for i,c in zip(F,v):row[i]=c
            relations.append(row)
    R=sp.Matrix(relations) if relations else sp.zeros(0,len(P))
    basis=R.nullspace()
    if len(basis)<=4:return None
    cols=[]
    for v in basis:
        D=sp.ilcm(*[x.q for x in v]);cols.append(v*D)
    return sp.Matrix(sp.Matrix.hstack(*cols).tolist()).applyfunc(sp.Integer)


def kernel(P,W):
    keep=np.ones(len(P),dtype=bool)
    for removed in W:
        V=P[[i for i in W if i!=removed]]
        try:H=ConvexHull(V)
        except QhullError:return None
        keep &= np.max((P[:,None,:]*H.equations[None,:,:3]).sum(axis=2)+H.equations[:,3],axis=1)<=1e-8
    return tuple(np.flatnonzero(keep))


def character(A,W,K):
    if not K:return [sp.Integer(0)]*A.cols  # already critical unfiltered: should not occur
    B=hermite_normal_form(A[list(W),:].T)
    pivots=tuple(B.T.rref()[1]); square=B[list(pivots),:]
    V=square.inv()*A[list(K),list(pivots)].T
    assert B*V==A[list(K),:].T
    if any(all(v.q==1 for v in V[:,j]) for j in range(V.cols)):return None
    den=int(sp.ilcm(*[v.q for v in V])); gens=[tuple(int(v*den)%den for v in V[i,:]) for i in range(V.rows)]
    zero=(0,)*len(K);queue=deque([(zero,(0,)*V.rows)]);seen_char={zero}
    while queue and len(seen_char)<=20000:
        x,k=queue.popleft()
        for i,g in enumerate(gens):
            y=tuple((a+b)%den for a,b in zip(x,g))
            if y in seen_char:continue
            kk=list(k);kk[i]+=1;kk=tuple(kk)
            if all(y):
                alpha=[sp.Integer(0)]*A.cols
                coeff=square.T.inv()*sp.Matrix(kk)
                for j,c in zip(pivots,coeff):alpha[j]=c
                return alpha
            seen_char.add(y);queue.append((y,kk))
    return False

last=started
while time.monotonic()-started<args.seconds:
    stats['generated']+=1
    kind=stats['generated']%4
    if kind==0:vertices=rng.sample(box,rng.randint(7,15))
    elif kind==1:vertices=rng.sample(simplex,rng.randint(8,17))
    elif kind==2:
        vertices=[tuple(p[i]+(rng.choice([-1,0,0,0,1]) if rng.random()<.3 else 0) for i in range(3)) for p in old]
    else:
        normals=[(rng.randint(0,4),rng.randint(0,4),rng.randint(0,4),rng.randint(3,10)) for _ in range(3)]
        vertices=[p for p in itertools.product(range(4),repeat=3) if all(sum(a*x for a,x in zip(n[:3],p))<=n[3] for n in normals)]
    if len(vertices)<4:continue
    data=lattice_hull(vertices)
    if data is None:continue
    P,H=data;key=tuple(map(tuple,P))
    if key in seen:continue
    seen.add(key);stats['hollow']+=1
    # Cheap sufficient global affine case: some integer interior point was already excluded.
    A=features(P,H)
    if A is None:continue
    stats['nonaffine']+=1
    possible=[]
    if len(P)<=16:subsets=itertools.combinations(range(len(P)),9)
    else:subsets=(tuple(sorted(rng.sample(range(len(P)),9))) for _ in range(350))
    for W in subsets:
        try:
            if len(ConvexHull(P[list(W)]).vertices)!=9:continue
        except QhullError:continue
        stats['nine']+=1
        K=kernel(P,W)
        if K is None:continue
        alpha=character(A,W,K)
        if alpha is None:stats['forced']+=1;continue
        if alpha is False:stats['character_reject']+=1;continue
        values=A*sp.Matrix(alpha)
        print('CANDIDATE',json.dumps(dict(P=P.tolist(),W=list(map(int,W)),K=list(map(int,K)),g=list(map(str,values)),ell=A.cols,stats=stats)),flush=True)
        raise SystemExit
    if time.monotonic()-last>15:
        print('progress',json.dumps(stats),flush=True);last=time.monotonic()
print('DONE',json.dumps(stats),'seconds',time.monotonic()-started,flush=True)
