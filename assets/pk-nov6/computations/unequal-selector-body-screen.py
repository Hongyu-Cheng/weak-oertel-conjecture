"""Falsify the unequal endpoint moment-body selector; numerical only."""
import numpy as np, json
from scipy.optimize import linprog
exec(open('./conditional-centroid-three-fiber-screen.py').read().split('best=1.')[0])

def clip(poly,n,t):
    out=[]
    for p,q in zip(poly,np.roll(poly,-1,axis=0)):
        sp=n@p-t; sq=n@q-t
        if sp<=0:out.append(p)
        if (sp<0<sq) or (sq<0<sp):out.append(p+(q-p)*sp/(sp-sq))
    return np.asarray(out)

def lower_mean(C,n,a):
    l,r=min(C@n),max(C@n)
    for _ in range(42):
        t=(l+r)/2
        cc=clip(C,n,t)
        ar=area_centroid(cc)[0] if len(cc)>=3 else 0
        if ar<a:l=t
        else:r=t
    cc=clip(C,n,(l+r)/2)
    return area_centroid(cc)[1]

def thresholds(A,B,C,tau,angles):
    out=[]
    for theta in angles:
        n=np.array([np.cos(theta),np.sin(theta)])
        l,r=min(B@n)-1e-4,max(B@n)+1e-4
        for _ in range(32):
            t=(l+r)/2
            val=eval_dir(A,B,C,n*t,theta)
            if val>tau:l=t
            else:r=t
        out.append((l+r)/2)
    return np.array(out)

rng=np.random.default_rng(6299138)
B=np.array([[0.,0.],[1.,0.],[0.,1.]])
b,gB=area_centroid(B)
angles=np.linspace(0,2*np.pi,48,endpoint=False)+.0041
normals=np.array([[np.cos(t),np.sin(t)] for t in angles])
worst=-1.
for case in range(100):
    rr=rng.uniform(1.01,1.999)
    lo=1/(rr*rr+(2-rr)**2)
    hi=min(1.,1/(4*(rr-1)))
    v=rng.uniform(lo,hi)
    P=np.exp(rng.uniform(np.log(v),0)); Q=v/P
    sh=rng.dirichlet([1.,1.,1.])[:2]*(1-max(P,Q))
    D=np.array([[0.,0.],[P,0.],[0.,Q]])+sh
    A=(2-rr)*D;C=rr*D
    a,gA=area_centroid(A);c,gC=area_centroid(C);M=a+b+c
    tau=(2/9)*M
    q=thresholds(A,B,C,tau,angles)
    low=[]
    for n in normals:
        gs=lower_mean(C,n,a)
        low.append(n@(b*gB+a*gA+a*gs)/(b+2*a))
    # Minimum uniform violation of the finite depth halfplanes, over an OUTER
    # approximation of Y. Positive optimum suggests a robust obstruction.
    mat=np.r_[np.c_[normals,-np.ones(len(normals))],np.c_[-normals,np.zeros(len(normals))]]
    rhs=np.r_[q,-np.array(low)]
    lp=linprog([0.,0.,1.],A_ub=mat,b_ub=rhs,bounds=[(None,None)]*3,method='highs')
    if not lp.success:raise RuntimeError(lp.message)
    margin=float(lp.fun)
    if margin>worst:
        worst=margin
        data={'case':case,'margin':margin,'A':A.tolist(),'B':B.tolist(),'C':C.tolist(),'mass':M,'center':lp.x[:2].tolist(),'r':rr,'v':v}
        print(json.dumps(data),flush=True)
        with open('./unequal-selector-body-screen-best.json','w') as ff:json.dump(data,ff,indent=2)
    if margin>1e-6:break
print('finished worst',worst,flush=True)
