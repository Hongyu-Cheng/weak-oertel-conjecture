"""Falsification only, with an exact affine correction of marginal mean.

Every sampled family has convex lower and concave upper interval endpoints.
An affine upper-roof correction enforces the TRUE volume mean at an integer.
"""
import json, random
import numpy as np

random.seed(2911007)
best=1.0
for case in range(30000):
    n=random.randint(4,17)
    z=np.arange(n,dtype=float)
    j=random.randint(max(0,n//2-2),min(n-1,n//2+2))
    ls=us=0
    l=[0];u=[0]
    for i in range(1,n):
        ls+=random.randint(0,9)
        us-=random.randint(0,9)
        l.append(l[-1]+ls)
        u.append(u[-1]+us)
    l=np.array(l,dtype=float);u=np.array(u,dtype=float)
    # The correction parameter delta is enlarged until every fiber is positive.
    rawu=u.copy()
    den=np.dot(z-j,z)
    if den==0: continue
    offset=1.0
    for trial in range(15):
        shift=max(l-u)+offset
        affine=-np.dot(z-j,u+shift-l)/den
        uu=u+shift+affine*z
        if min(uu-l)>0: break
        offset*=2
    else: continue
    w=uu-l;M=w.sum()
    gx=np.dot(w,(l+uu)/2)/M
    if abs(np.dot(z-j,w))>1e-8*M: raise AssertionError('mean')
    if not l[j]-1e-8<=gx<=uu[j]+1e-8: raise AssertionError('center membership')
    zz=z-j
    ids=zz!=0
    breaks=np.r_[(gx-l[ids])/zz[ids],(gx-uu[ids])/zz[ids]]
    far=1+max(abs(breaks))
    slopes=np.r_[breaks,-far,far]
    masses=np.clip(uu[None,:]-gx+slopes[:,None]*zz[None,:],0,w).sum(axis=1)
    idxlo=int(np.argmin(masses));idxhi=int(np.argmax(masses))
    if masses[idxlo]<M-masses[idxhi]:
        value=float(masses[idxlo]/M); slope=float(slopes[idxlo]);sign=1
    else:
        value=float(1-masses[idxhi]/M);slope=float(slopes[idxhi]);sign=-1
    if value<best:
        best=value
        data=dict(case=case,n=n,j=j,depth=value,lower=l.tolist(),raw_upper=rawu.tolist(),
                  shift=shift,affine=affine,upper=uu.tolist(),gx=gx,slope=slope,sign=sign)
        print(json.dumps(data),flush=True)
        with open('./actual_integer_centroid_interval_screen_best.json','w') as f:
            json.dump(data,f,indent=2)
    if best<.25-1e-8: break
print('finished',case+1,'best',best,flush=True)
