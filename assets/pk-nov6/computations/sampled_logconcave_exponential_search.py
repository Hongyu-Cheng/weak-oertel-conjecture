"""Exploratory sampled exp(-polyhedral-convex) densities; no proof claims."""
import json
import numpy as np
from scipy.optimize import brentq,linprog
from logconcave_exact_polygon_search import clip,mass

T=[np.array(p,float) for p in [(0,0),(1,0),(0,1)]]

def fibers_for(coeff):
    out=[]
    for z in range(4):
        aff=np.column_stack([coeff[:,1],coeff[:,2],coeff[:,3]+z*coeff[:,0]])
        cs=[]
        for i,c in enumerate(aff):
            P=T
            for j,cc in enumerate(aff):
                if i!=j: P=clip(P,c[:2]-cc[:2],cc[2]-c[2])
            if len(P)>2:cs.append((P,c))
        out.append(cs)
    return out

def evaluate(coeff, normals, tilt):
    fs=fibers_for(coeff)
    fs=[[(P,c+np.array([0,0,-tilt*z])) for P,c in cs] for z,cs in enumerate(fs)]
    ww=np.array([sum(mass(P,c) for P,c in cs) for cs in fs])
    M=float(np.sum(ww))
    if M<1e-8 or np.max(ww)>=M/2-1e-8:return None
    qq=[]
    for n in normals:
        vals=[n[0]*z+float(np.sum(n[1:]*p)) for z,cs in enumerate(fs) for P,c in cs for p in P]
        def upper(t):return sum(mass(clip(P,n[1:],t-n[0]*z),c) for z,cs in enumerate(fs) for P,c in cs)
        qq.append(brentq(lambda t:upper(t)-2*M/9,min(vals)-1e-8,max(vals)+1e-8,xtol=1e-9))
    margins=[]
    for z in range(4):
        A=np.vstack([np.column_stack([normals[:,1:],np.ones(len(normals))]),[[-1,0,0],[0,-1,0],[1,1,0]]])
        b=np.r_[np.array(qq)-normals[:,0]*z,[0,0,1]]
        opt=linprog([0,0,-1],A_ub=A,b_ub=b,bounds=[(None,None)]*3,method='highs')
        margins.append(float(opt.x[2]) if opt.success else float('-inf'))
    return margins,ww.tolist(),qq

if __name__=='__main__':
    rng=np.random.default_rng(97422)
    normals=[]
    for iz in range(-4,5):
        for a in np.linspace(0,2*np.pi,24,endpoint=False):
            n=np.array([iz/2,np.cos(a),np.sin(a)])
            normals.append(n/np.linalg.norm(n))
    normals=np.array(normals)
    best=None;checked=0
    for trial in range(100):
        k=int(rng.integers(2,7))
        coeff=np.column_stack([rng.integers(-3,4,k),rng.integers(-12,13,k),rng.integers(-12,13,k),rng.integers(-4,5,k)])
        fs=fibers_for(coeff)
        raw=np.array([sum(mass(P,c) for P,c in cs) for cs in fs])
        # Bring mass into the middle, then vary the tilt to include unequal ends.
        if np.min(raw)<=0:continue
        base=np.log(raw[0]/raw[-1])/3
        tilt=base+float(rng.uniform(-.6,.6))
        result=evaluate(coeff,normals,tilt)
        if result is None:continue
        checked+=1
        margins,weights,qq=result
        score=max(margins)
        if best is None or score<best:
            best=score
            print('trial',trial,'checked',checked,'best',best,'weights',weights,flush=True)
        if score < -1e-6:
            with open('./sampled_logconcave_exponential_candidate.json','w') as stream:
                json.dump({'coeff':coeff.tolist(),'tilt':tilt,'weights':weights,'margins':margins,'normals':normals.tolist(),'bounds':qq},stream,indent=2)
            print('UNCERTIFIED candidate saved',flush=True)
            break
    print('finished',checked,'best',best,flush=True)
