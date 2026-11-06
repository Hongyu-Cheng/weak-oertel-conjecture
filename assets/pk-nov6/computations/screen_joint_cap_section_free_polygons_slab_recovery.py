"""Independent finite falsification screen only; all output is numerical."""
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import minimize

normals=np.array([[1.,0.],[0.,1.],[-1.,-1.]])
fixed=np.array([[.001,0.],[0.,.001],[-.001,-.001]])
seed0=np.array([[4.,-3.],[-3.,4.],[-1.,-1.],[.5,.5],[-2.,1.5],[1.5,-2.]])
def area(p):
    if len(p)<3:return 0.
    return abs(np.sum(p[:,0]*np.roll(p[:,1],-1)-p[:,1]*np.roll(p[:,0],-1)))/2
def clip(p,v):
    out=[]
    for a,b in zip(p,np.roll(p,-1,axis=0)):
        fa=a@v;fb=b@v
        if fa>=0:out.append(a)
        if fa*fb<0:out.append(a+(b-a)*fa/(fa-fb))
    return np.array(out)
def section(p,v):
    out=[]
    for a,b in zip(p,np.roll(p,-1,axis=0)):
        fa=a@v;fb=b@v
        if abs(fa)<1.e-12:out.append(a)
        if fa*fb<0:out.append(a+(b-a)*fa/(fa-fb))
    jv=np.array([-v[1],v[0]])
    vals=np.array(out)@jv/(v@v)
    return vals.max()-vals.min()
def data(flat):
    pts=np.vstack([flat.reshape((-1,2)),fixed])
    p=pts[ConvexHull(pts).vertices]
    k=area(p)
    qs=np.array([area(clip(p,v))/k for v in normals])
    sig=np.array([section(p,v) for v in normals])
    return p,k,qs,(1/sig)/np.sum(1/sig)
def obj(flat):return data(flat)[3][2]
def con(flat):
    p,k,q,w=data(flat)
    return np.r_[128/279-q,1-(q.sum()-.75*q.max()),k-1]
rng=np.random.default_rng(529017)
best=1.
for j in range(32):
    seed=seed0.copy()
    if j:seed+=rng.normal(0,.25,seed.shape)
    fit=minimize(obj,seed.ravel(),method='SLSQP',bounds=[(-9.,9.)]*seed.size,
                 constraints=[{'type':'ineq','fun':con}],
                 options={'maxiter':650,'ftol':1.e-11})
    p,k,q,w=data(fit.x);err=con(fit.x).min()
    if err>=-2.e-8 and w[2]<best:
        best=w[2]
        print('candidate',j,'min_constraint',err,'weights',w.tolist(),'fractions',q.tolist(),
              'profile',q.sum()-.75*q.max(),'vertices',p.tolist(),flush=True)
    if err>=-1.e-10 and w[2]<2/9-1.e-7:
        print('NUMERICAL FALSIFICATION CANDIDATE; exact proof needed',flush=True)
        break
print('completed numerical screen; best',best,flush=True)
