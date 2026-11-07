"""Falsification only. No numerical result is a proof."""
import numpy as np
from scipy.optimize import differential_evolution

def profile(coeff,w):
    N=len(coeff)-1
    x=np.linspace(0,w,N+1)
    t=x/w
    h=coeff[0]*(1-t)+coeff[-1]*t
    for i in range(1,N):
        p=i/N
        h+=coeff[i]*np.minimum(t/p,(1-t)/(1-p))
    dx=np.diff(x)
    mass=np.sum(dx*(h[:-1]+h[1:])/2)
    h=h/mass
    mean=np.sum(dx*((2*x[:-1]+x[1:])*h[:-1]+(x[:-1]+2*x[1:])*h[1:])/6)
    return x-mean,h

def tail(x,h,a):
    if a<=x[0]:return 1.
    if a>=x[-1]:return 0.
    i=np.searchsorted(x,a,side='right')-1
    height=h[i]+(h[i+1]-h[i])*(a-x[i])/(x[i+1]-x[i])
    return (x[i+1]-a)*(height+h[i+1])/2+np.sum(np.diff(x[i+1:])*(h[i+1:-1]+h[i+2:])/2)

def own(x,h,y,k):
    edges=[]
    for X,H in [(x,h),(y,k)]:
        edges.extend([(dh/dx,dx/2,dh/2)for dx,dh in zip(np.diff(X),np.diff(H))])
    edges.sort(reverse=True)
    pos=(x[0]+y[0])/2;hh=(h[0]+k[0])/2;area=0.
    for _,dx,dh in edges:
        nex=pos+dx;nh=hh+dh
        if pos>=0:area+=dx*(hh+nh)/2
        elif nex>0:
            cut=hh+dh*(-pos/dx)
            area+=nex*(cut+nh)/2
        pos,hh=nex,nh
    return area

def pair_min(x,h,y,k):
    br=sorted(set(list(x)+list(-y)))
    def P(a):return tail(x,h,a)+tail(y,k,-a)
    best=1.
    for lo,hi in zip(br,br[1:]):
        mid=(lo+hi)/2;flo,fhi,fmid=P(lo),P(hi),P(mid)
        best=min(best,flo,fhi)
        aa=2*(flo+fhi-2*fmid)/(hi-lo)**2
        if aa>1e-10:
            star=mid-(fhi-flo)/(2*aa*(hi-lo))
            if lo<star<hi:best=min(best,P(star))
    return best

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--pieces',type=int,default=4);p.add_argument('--seed',type=int,default=5);p.add_argument('--iterations',type=int,default=180);args=p.parse_args()
    size=args.pieces+1
    def fun(v):
        R=v[-1];x,h=profile(v[:size],1.);y,k=profile(v[size:2*size],R)
        return own(x,h,y,k)+pair_min(x,h,y,k)
    bounds=[(0,1)]*(2*size)+[(1,4.5)]
    res=differential_evolution(fun,bounds,seed=args.seed,popsize=8,maxiter=args.iterations,tol=1e-8,polish=True)
    print('SCREEN ONLY',res.fun,res.x.tolist(),flush=True)
