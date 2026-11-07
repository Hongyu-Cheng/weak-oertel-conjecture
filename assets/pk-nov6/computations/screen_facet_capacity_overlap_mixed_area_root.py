import numpy as np
from scipy.spatial import ConvexHull

def area(p):
    if len(p)<3:return 0.
    p=np.asarray(p);return .5*abs(np.dot(p[:,0],np.roll(p[:,1],-1))-np.dot(p[:,1],np.roll(p[:,0],-1)))
def clip(p,u,t):
    out=[]
    for a,b in zip(p,np.roll(p,-1,axis=0)):
        fa=np.dot(u,a)-t;fb=np.dot(u,b)-t
        if fa>=0:out.append(a)
        if (fa>=0)!=(fb>=0):out.append(a+fa/(fa-fb)*(b-a))
    return np.array(out)
def section(p,u,t):
    pts=[]
    for a,b in zip(p,np.roll(p,-1,axis=0)):
        fa=np.dot(u,a)-t;fb=np.dot(u,b)-t
        if fa*fb<0:pts.append(a+fa/(fa-fb)*(b-a))
        if abs(fa)<1e-10:pts.append(a)
    if len(pts)<2:return 0
    # horizontal or vertical coordinate length, dividing sqrt2 on diagonal
    return max(np.linalg.norm(a-b) for a in pts for b in pts)/np.linalg.norm(u)
U=np.array([[1.,0],[0,1],[-1,-1]])
rng=np.random.default_rng(271828)
best=None; count=0
for j in range(60000):
    v=rng.normal(size=(rng.integers(3,12),2))
    try:p=v[ConvexHull(v).vertices]
    except Exception:continue
    th=rng.uniform(0,np.pi);R=np.array([[np.cos(th),-np.sin(th)],[np.sin(th),np.cos(th)]])
    scales=np.exp(rng.uniform(-2,3,size=2));p=(p*scales)@R.T+rng.normal(size=2)*rng.uniform(0,3)
    vals=p@U.T
    if not np.all((vals.min(0)<-1)&(vals.max(0)>-1)):continue
    sections=np.array([section(p,u,-1) for u in U])
    if np.max(sections)>3+1e-8:continue
    a=area(p);caps=np.array([area(clip(p,u,-1)) for u in U]);k=3-sum(caps)/a
    if k<=1.25:continue
    S=sum(vals.max(0));gap1=(4/9)*(a+4.5)-max(caps);gap2=a+4.5-S
    score=min(gap1,gap2)
    count+=1
    if best is None or score>best[0]:best=(score,p,a,caps,k,S,sections)
    if gap1>1e-5 and gap2>1e-5:
        print('COUNTER',j,'a',a,'caps',caps,'kappa',k,'S',S,'sec',sections,'p',p.tolist(),flush=True);break
else: print('no counter')
print('tested bad overlap',count,'best',best,flush=True)
