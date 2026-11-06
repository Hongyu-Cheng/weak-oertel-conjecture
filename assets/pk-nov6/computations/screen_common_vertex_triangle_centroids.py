"""Numerical discovery only: full positive triangle normal and shared-tilt cells."""
import numpy as np
from random import Random


def cap(r,t,a):
    if t<=0:return r*r
    if t>=a*r:return 0.
    if a==1:return (r-t)**2
    if t<=(1-a)*r:return r*r-t*t/(a*(1-a))
    return (a*r-t)**2/(a*(2*a-1))


def tilt_opt(rs,j,a):
    q=rs[j]/3
    z=np.arange(len(rs))-j
    breaks={0.}
    for zi,r in zip(z,rs):
        if zi:
            breaks.update([(q-x)/zi for x in (0,(1-a)*r,a*r)])
    br=sorted(breaks)
    def cost(b):return sum(cap(r,q-b*zi,a)for zi,r in zip(z,rs))
    best=min((cost(b),b)for b in br)
    for l,h in zip(br,br[1:]):
        mid=(l+h)/2; A=B=0.
        for zi,r in zip(z,rs):
            t=q-mid*zi
            if zi==0 or t<=0 or t>=a*r:continue
            if a<1 and t<=(1-a)*r:
                den=a*(1-a);A-=zi*zi/den;B+=2*q*zi/den
            else:
                den=1 if a==1 else a*(2*a-1)
                A+=zi*zi/den;B+=2*(a*r-q)*zi/den
        if A>0:
            b=-B/(2*A)
            if l<b<h:best=min(best,(cost(b),b))
    return best


if __name__=='__main__':
    rng=Random(713123);best=(2,None)
    normals=[.5,.55,.6,.65,.7,.75,.8,.85,.9,.95,1.]
    for trial in range(6000):
        N=rng.choice([4,5,6,7,8,10,12])
        slopes=sorted([rng.randrange(-30,31)/30 for _ in range(N-1)],reverse=True)
        raw=[0.]
        for slope in slopes:raw.append(raw[-1]+slope)
        base=rng.choice([.03,.1,.25,.5,1.,2.])-min(raw)
        rs=np.array(raw)+base;rs/=max(rs)
        M=sum(rs*rs);target=2*M/9
        if max(rs*rs)>=M/2:continue
        witnesses=[]
        success=True
        for j in range(N):
            if j in (0,N-1):v=(4*rs[j]**2/9,1.,0.)
            else:v=min((cost,a,b)for a in normals for cost,b in [tilt_opt(rs,j,a)])
            witnesses.append(v)
            if v[0]>=target:
                success=False
                break
        ratio=max(v[0]for v in witnesses)/target
        if ratio<best[0]:
            best=(ratio,(trial,rs.tolist(),target,witnesses))
            print('BEST',best,flush=True)
        if success:
            print('COUNTER',best,flush=True);break
    else:print('NO COUNTER; best partial stopping ratio',best,flush=True)
