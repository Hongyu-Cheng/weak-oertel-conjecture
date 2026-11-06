"""Exploratory only: sampled jointly concave polygonal tents, n=1,d=2.

The source density is 1_{[0,2] x T} max(0,min_i(A_i z+B_i x+C_i y+D_i)).
On its convex positive support it is concave, hence jointly log-concave.
Numerical infeasibility is only a lead and must receive an exact certificate.
"""
import json
import numpy as np
from scipy.optimize import brentq, linprog

T = [np.array(p,dtype=float) for p in [(0,0),(1,0),(0,1)]]

def clip(poly,n,c):
    if not poly: return []
    out=[]
    for i,p in enumerate(poly):
        q=poly[(i+1)%len(poly)]
        a=float(np.sum(p*n))-c
        b=float(np.sum(q*n))-c
        if a>=-1e-11: out.append(p)
        if (a<0<b) or (b<0<a): out.append(p+a/(a-b)*(q-p))
    return out

def mass(poly,co):
    if len(poly)<3: return 0.
    out=0.
    p=poly[0]
    for q,r in zip(poly[1:-1],poly[2:]):
        area=((q[0]-p[0])*(r[1]-p[1])-(q[1]-p[1])*(r[0]-p[0]))/2
        out+=area*(float(np.sum((p+q+r)*co[:2]))/3+co[2])
    return out

def cells(coeff,z):
    aff=np.column_stack([coeff[:,1],coeff[:,2],coeff[:,3]+z*coeff[:,0]])
    out=[]
    for i,c in enumerate(aff):
        P=clip(T,c[:2],-c[2])
        for j,other in enumerate(aff):
            if i!=j:
                P=clip(P,other[:2]-c[:2],c[2]-other[2])
        if len(P)>2 and mass(P,c)>1e-11: out.append((P,c))
    return out

def evaluate(coeff,normals,alpha=2/9):
    fibers=[cells(coeff,z) for z in range(3)]
    weights=np.array([sum(mass(P,c) for P,c in cs) for cs in fibers])
    total=float(np.sum(weights))
    if total<1e-8 or max(weights)>total/2-1e-8: return None
    bounds=[]
    for n in normals:
        values=[n[0]*z+float(np.sum(n[1:]*p)) for z,cs in enumerate(fibers) for P,c in cs for p in P]
        def upper(t):
            return sum(mass(clip(P,n[1:],t-n[0]*z),c) for z,cs in enumerate(fibers) for P,c in cs)
        q=brentq(lambda t:upper(t)-alpha*total,min(values)-1e-8,max(values)+1e-8,xtol=1e-10)
        bounds.append(q)
    margins=[]
    for z in range(3):
        # Positive minimum slack signals feasible finite depth constraints.
        co=np.column_stack([normals[:,1:],np.ones(len(normals))])
        rhs=np.array(bounds)-normals[:,0]*z
        extra=np.array([[-1,0,0],[0,-1,0],[1,1,0]],float)
        rr=np.array([0,0,1],float)
        for row in coeff:
            extra=np.vstack([extra,[-row[1],-row[2],0]])
            rr=np.r_[rr,row[3]+row[0]*z]
        opt=linprog([0,0,-1],A_ub=np.vstack([co,extra]),b_ub=np.r_[rhs,rr],bounds=[(None,None)]*3,method='highs')
        margins.append(float(opt.x[2]) if opt.success else float('-inf'))
    return margins,weights.tolist(),bounds

if __name__=='__main__':
    rng=np.random.default_rng(89133)
    normals=[]
    for iz in range(-4,5):
        for theta in np.linspace(0,2*np.pi,28,endpoint=False):
            v=np.array([iz/2,np.cos(theta),np.sin(theta)])
            normals.append(v/np.linalg.norm(v))
    normals=np.array(normals)
    checked=0
    best=None
    for trial in range(120):
        # Random intersecting planes, including a constant roof.
        k=int(rng.integers(3,8))
        coeff=np.column_stack([rng.integers(-5,6,k),rng.integers(-8,9,k),rng.integers(-8,9,k),rng.integers(1,11,k)])
        coeff=np.vstack([coeff,[0,0,0,int(rng.integers(2,8))]])
        result=evaluate(coeff,normals)
        if result is None: continue
        checked+=1
        margins,weights,qq=result
        score=max(margins)
        if best is None or score<best:
            best=score
            print('trial',trial,'checked',checked,'best margin',score,'weights',weights,flush=True)
        if score < -1e-7:
            with open('./sampled_logconcave_tent_candidate.json','w') as stream:
                json.dump({'coeff':coeff.tolist(),'weights':weights,'margins':margins,'normals':normals.tolist(),'bounds':qq},stream,indent=2)
            print('UNCERTIFIED candidate saved',flush=True)
            break
    print('finished',checked,'nonheavy cases; best',best,flush=True)
