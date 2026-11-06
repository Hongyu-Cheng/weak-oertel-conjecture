"""A bounded falsification screen, never a proof of the proposed bound."""
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import minimize

verts=np.array([[4.,-3.],[-3.,4.],[-1.,-1.]])
directions=[]
for j in range(3):
    for t in [0.,.2,.4,.6,.8]:
        directions.append((1-t)*verts[j]+t*verts[(j+1)%3])
directions=np.array(directions)
normals=np.array([[1.,0.],[0.,1.],[-1.,-1.]])

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
def data(logr):
    points=directions*np.exp(logr[:,None])
    p=points[ConvexHull(points).vertices]
    k=area(p)
    qs=np.array([area(clip(p,v))/k for v in normals])
    sig=np.array([section(p,v) for v in normals])
    weights=(1/sig)/np.sum(1/sig)
    return p,qs,weights
def objective(logr):return data(logr)[2][2]
def constraints(logr):
    p,q,w=data(logr)
    return np.r_[128/279-q,1-(q.sum()-.75*q.max())]

rng=np.random.default_rng(73017)
best=1.
for j in range(36):
    seed=np.zeros(len(directions)) if j==0 else rng.normal(0,.18,len(directions))
    fit=minimize(objective,seed,method='SLSQP',bounds=[(-1.5,1.5)]*len(seed),
                 constraints=[{'type':'ineq','fun':constraints}],
                 options={'maxiter':450,'ftol':1.e-11})
    p,q,w=data(fit.x);err=constraints(fit.x).min()
    if err>=-2.e-8 and w[2]<best:
        best=w[2]
        print('candidate',j,'min_constraint',err,'weights',w.tolist(),'fractions',q.tolist(),
              'profile',float(q.sum()-.75*q.max()),'vertices',p.tolist(),flush=True)
    if err>=-1.e-10 and w[2]<2/9-1.e-7:
        print('NUMERICAL FALSIFICATION CANDIDATE; exact certificate required',flush=True)
        break
print('completed; best feasible screened inverse weight',best,flush=True)
