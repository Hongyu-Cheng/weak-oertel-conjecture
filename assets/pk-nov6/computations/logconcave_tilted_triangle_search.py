import numpy as np
from math import exp,expm1,cos,sin,pi
from scipy.optimize import minimize_scalar

def clip(poly,n,c):
    out=[]
    for i,p in enumerate(poly):
        q=poly[(i+1)%len(poly)]
        a=np.dot(p,n)-c;b=np.dot(q,n)-c
        if a>=0:out.append(p)
        if (a<0<b) or (b<0<a):out.append(p+a/(a-b)*(q-p))
    return out

def mass(poly,theta):
    ans=0
    if not poly:return 0
    for i,p in enumerate(poly):
        q=poly[(i+1)%len(poly)]
        z=theta*(q[0]-p[0])
        v=expm1(z)/z if abs(z)>1e-8 else 1+z/2+z*z/6
        ans+=(q[1]-p[1])*exp(theta*p[0])*v/theta
    return ans

T=[np.array(p,dtype=float) for p in [(0,0),(1,0),(0,1)]]
for theta in [.1,.5,1,2,5,10,-1,-5]:
    total=mass(T,theta)
    def depth(t,details=False):
        pt=np.array([t,(1-t)/2])
        def cap(a):
            n=np.array([cos(a),sin(a)])
            return mass(clip(T,n,np.dot(n,pt)),theta)/total
        ang=np.linspace(0,2*pi,121)
        vals=[cap(a) for a in ang]
        minima=[]
        for j in range(120):
            if vals[j]<=vals[(j-1)%120] and vals[j]<=vals[(j+1)%120]:
                opt=minimize_scalar(cap,bounds=(ang[j]-.07,ang[j]+.07),method='bounded')
                minima.append((opt.fun,opt.x))
        return sorted(minima) if details else min(v for v,a in minima)
    op=minimize_scalar(lambda t:-depth(t),bounds=(.001,.999),method='bounded',options={'xatol':1e-12})
    print(theta,op.x,-op.fun,depth(op.x,True),flush=True)
