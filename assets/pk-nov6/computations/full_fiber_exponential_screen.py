import random,json,numpy as np
from scipy.spatial import ConvexHull

src=open('./logconcave_shadow_increment_screen.py').read().split('random.seed(351082)')[0]
exec(src)
random.seed(79937)
for iteration in range(20000):
    pts=list(set((random.randint(0,random.choice([3,5,9,15])),random.randint(-20,20)) for _ in range(random.randint(4,20))))
    if len(pts)<3:continue
    try:poly=[pts[i] for i in ConvexHull(pts).vertices]
    except:continue
    f=fibers(poly);M=sum(v-u for u,v in f.values())
    if M<=0:continue
    med=[k for k in f if sum(v-u for j,(u,v) in f.items() if j<k)<=M/2+1e-9
         and sum(v-u for j,(u,v) in f.items() if j>k)<=M/2+1e-9]
    cert=[]
    for k in med:
        t,A,B=bands(f,k)
        unif=(t-f[k][0])/(f[k][1]-f[k][0])
        j=int(np.argmax(A-unif));ii=int(np.argmax(unif-B))
        if A[j]-unif[j]>1e-6 and unif[ii]-B[ii]>1e-6:
            cert.append({'fiber':k,'cdf_above_uniform':[float(t[j]),float(A[j]),float(unif[j])],
                         'cdf_below_uniform':[float(t[ii]),float(B[ii]),float(unif[ii])]})
        else:break
    else:
        out={'polygon':poly,'fibers':f,'certificates':cert}
        print(json.dumps(out,indent=2),flush=True)
        with open('./full_fiber_exponential_candidate.json','w') as ff:json.dump(out,ff,indent=2)
        break
    if iteration%1000==0:print('tested',iteration,flush=True)
