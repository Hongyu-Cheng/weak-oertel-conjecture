import numpy as np
from scipy.optimize import minimize

def upper(z,l,u,q,z0):
    def objective(tv):
        t,v=tv; cut=t+v*z
        mass=np.clip(u-cut,0,u-l)
        val=q*(t+v*z0)+np.sum(((np.maximum(u-cut,0))**2-(np.maximum(l-cut,0))**2)/2)
        grad=np.array([q-np.sum(mass),q*z0-np.dot(z,mass)])
        return val,grad
    ans=minimize(objective,[np.mean((l+u)/2),0],jac=True,method='BFGS',options={'gtol':1e-9,'maxiter':500})
    cut=np.clip(ans.x[0]+ans.x[1]*z,l,u)
    m=u-cut
    err=max(abs(sum(m)-q),abs(np.dot(z,m)-q*z0))
    if err>1e-6:
        return None
    x=np.sum((u*u-cut*cut)/2)/q
    return x,ans.x,m

def depth(z,l,u,z0,x):
    dz=z-z0
    ts=[0]
    for j in range(len(z)):
        if dz[j]: ts += [(l[j]-x)/dz[j],(u[j]-x)/dz[j]]
    ret=(1e99,None,None)
    for t in ts:
        down=np.sum(np.clip(x+t*dz-l,0,u-l)); up=np.sum(u-l)-down
        if down<ret[0]:ret=(down,t,'down')
        if up<ret[0]:ret=(up,t,'up')
    return ret

rng=np.random.default_rng(712803)
best=1
for it in range(20000):
    N=int(rng.integers(3,10)); z=np.arange(N,dtype=float)
    l=np.r_[0,np.cumsum(np.sort(rng.integers(-12,13,N-1)))]
    u=np.r_[0,np.cumsum(np.sort(rng.integers(-12,13,N-1))[::-1])]
    u=u-min(u-l)+int(rng.integers(1,30))
    M=sum(u-l); q=M/2
    z0=z[np.searchsorted(np.cumsum(u-l),q)]
    aa=upper(z,l,u,q,z0); bb=upper(z,-u,-l,q,z0)
    if aa is None or bb is None:continue
    x=(aa[0]-bb[0])/2
    dd=depth(z,l,u,z0,x)
    rat=dd[0]/M
    if rat<best:
        best=rat
        print('best',it,rat,'z',z.tolist(),'l',l.tolist(),'u',u.tolist(),'z0',z0,'x',x,'depth',dd,'upper',aa,'minuslower',bb,flush=True)
    if rat<.25-1e-8:break
