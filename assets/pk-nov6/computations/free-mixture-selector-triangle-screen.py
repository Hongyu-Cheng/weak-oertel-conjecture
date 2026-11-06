"""Falsify the free-mixture selector with endpoint simplices. Numerical only."""
import numpy as np, json
from scipy.optimize import linprog
exec(open('./unequal-selector-body-screen.py').read().split('rng=np.random.default_rng(6299138)')[0])

rng=np.random.default_rng(817239)
B=np.array([[0.,0.],[1.,0.],[0.,1.]])
b,gB=area_centroid(B)
angles=np.unique(np.r_[np.linspace(0,2*np.pi,36,endpoint=False)+.00071,
                       0.,np.pi/2,np.pi,3*np.pi/2,np.pi/4,5*np.pi/4])
normals=np.array([[np.cos(t),np.sin(t)] for t in angles])
worst=-1.
for case in range(160):
    eps=np.exp(rng.uniform(np.log(.002),np.log(.9)))
    A=eps*B
    a,gA=area_centroid(A)
    c=b+rng.uniform(-.98,.98)*a
    for attempt in range(10000):
        # Three nonparallel, generally nonhomothetic endpoint vertices.
        bary=np.array([rng.dirichlet(np.eye(3)[i]*7+np.ones(3)) for i in range(3)])
        D=hull(bary[:,1:])
        D=D/np.max(D.sum(axis=1))
        ar,_=area_centroid(D)
        C=np.sqrt(c/ar)*D
        if np.max(C.sum(axis=1))+eps<2: break
    else: raise RuntimeError('no compatible triangle')
    c,gC=area_centroid(C)
    assert c<a+b and b<a+c and a<b+c
    M=a+b+c; tau=(2/9)*M
    q=thresholds(A,B,C,tau,angles)
    low=[]
    for n in normals:
        gs=lower_mean(C,n,a)
        low.append(min(n@gB,n@(gA+gs)/2))
    mat=np.r_[np.c_[normals,-np.ones(len(normals))],np.c_[-normals,np.zeros(len(normals))]]
    rhs=np.r_[q,-np.array(low)]
    lp=linprog([0.,0.,1.],A_ub=mat,b_ub=rhs,bounds=[(None,None)]*3,method='highs')
    if not lp.success: raise RuntimeError(lp.message)
    margin=float(lp.fun)
    if margin>worst:
        worst=margin
        data={'case':case,'margin':margin,'A':A.tolist(),'B':B.tolist(),'C':C.tolist(),'mass':M,'center':lp.x[:2].tolist(),'epsilon':eps}
        print(json.dumps(data),flush=True)
        with open('./free-mixture-selector-triangle-screen-best.json','w') as ff: json.dump(data,ff,indent=2)
    if margin>2e-7: break
print('finished worst',worst,flush=True)
