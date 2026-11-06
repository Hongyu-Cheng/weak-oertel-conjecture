import numpy as np,json,random
from scipy.spatial import ConvexHull

def fibers(poly):
    ans={}
    for z in range(int(min(x for x,y in poly)),int(max(x for x,y in poly))+1):
        yy=[]
        for i,(x,y) in enumerate(poly):
            X,Y=poly[(i+1)%len(poly)]
            if x==X:
                if z==x:yy.extend([y,Y])
            elif min(x,X)<=z<=max(x,X):yy.append(y+(Y-y)*(z-x)/(X-x))
        if yy and max(yy)>min(yy):ans[z]=(min(yy),max(yy))
    return ans

def bands(f,k,N=121):
    zz=np.array(list(f))
    ends=np.array(list(f.values()))
    lo,hi=ends[:,0],ends[:,1]
    lengths=hi-lo;M=lengths.sum()
    tt=np.linspace(*f[k],N)
    j=zz!=k
    slopes=np.concatenate([(lo[j,None]-tt)/(zz[j,None]-k),
                           (hi[j,None]-tt)/(zz[j,None]-k)],axis=0)
    cuts=tt[None,:,None]+slopes[:,:,None]*(zz[None,None,:]-k)
    cap=np.maximum(0,np.minimum(lengths,cuts-lo)).sum(axis=2)
    own=tt-f[k][0]
    extremes=np.array([own+lengths[zz<k].sum(),own+lengths[zz>k].sum()])
    cap=np.concatenate([cap,extremes],axis=0)
    L=cap.min(axis=0);R=M-cap.max(axis=0)
    return tt,np.maximum(0,1-2*R/M),np.minimum(1,2*L/M)

random.seed(351082)
for iteration in range(20000):
    pts=list(set((random.randint(0,random.choice([3,5,9,15])),random.randint(-20,20)) for _ in range(random.randint(4,20))))
    if len(pts)<3:continue
    try:poly=[pts[i] for i in ConvexHull(pts).vertices]
    except:continue
    f=fibers(poly);M=sum(v-u for u,v in f.values())
    if M<=0:continue
    med=[k for k in f if sum(v-u for j,(u,v) in f.items() if j<k)<=M/2+1e-9
         and sum(v-u for j,(u,v) in f.items() if j>k)<=M/2+1e-9]
    bad=[]
    for k in med:
        t,A,B=bands(f,k)
        cert=None
        for step in range(1,40):
            # Three adjacent equal-length intervals.
            low=A[step:]-B[:-step]
            high=B[step:]-A[:-step]
            count=len(t)-3*step
            aa=low[:count];bb=high[step:step+count];cc=low[2*step:2*step+count]
            indices=np.flatnonzero((aa>0)&(cc>0)&(aa*cc>bb**2+1e-10))
            if len(indices):
                j=int(indices[0]);cert={'fiber':k,'times':[float(t[j+i*step]) for i in range(4)],
                      'lower_left':float(aa[j]),'upper_middle':float(bb[j]),'lower_right':float(cc[j])}
                break
        if cert is None:break
        bad.append(cert)
    else:
        out={'polygon':poly,'fibers':f,'certificates':bad}
        print(json.dumps(out,indent=2),flush=True)
        with open('./logconcave_shadow_increment_candidate.json','w') as ff:json.dump(out,ff,indent=2)
        break
    if iteration%1000==0:print('tested',iteration,flush=True)
