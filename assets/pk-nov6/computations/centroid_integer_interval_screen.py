import random, math
import numpy as np

random.seed(5819)
best=(1.,None)
for _ in range(80000):
    N=random.randrange(2,18)
    z=np.arange(N+1,dtype=float)
    k=random.randrange(1,N)
    curv=np.array([random.expovariate(1) if random.random()<.3 else 0 for j in range(N-1)])
    g=-np.array([sum(curv[j-1]*max(0,i-j) for j in range(1,N)) for i in range(N+1)])
    aa=random.uniform(0,30)
    D=np.dot(z-k,z)
    if abs(D)<1e-9:continue
    bb=-np.dot(z-k,g+aa)/D
    f=g+aa+bb*z
    if min(f)<-1e-9 or sum(f)<1e-8:continue
    bottom_curv=curv*np.array([random.random() for _ in curv])
    bottom=np.array([sum(bottom_curv[j-1]*max(0,i-j) for j in range(1,N)) for i in range(N+1)])
    mass=sum(f);x=np.dot(f,bottom+f/2)/mass
    slopes=[0.]
    for i in range(N+1):
        if i!=k: slopes +=[(bottom[i]-x)/(i-k),(bottom[i]+f[i]-x)/(i-k)]
    value=1.
    for s in slopes:
        threshold=x+s*(z-k)
        upper=np.maximum(0,bottom+f-np.maximum(bottom,threshold)).sum()/mass
        value=min(value,upper,1-upper)
    if value<best[0]:best=(value,(N,k,aa,bb,f.tolist(),bottom.tolist(),x))
print(best)
