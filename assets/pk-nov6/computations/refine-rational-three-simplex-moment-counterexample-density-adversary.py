import numpy as np
from scipy.optimize import brentq

def clip(poly,u,t):
    out=[]
    for i,p in enumerate(poly):
        q=poly[(i+1)%len(poly)];fp=np.dot(u,p)-t;fq=np.dot(u,q)-t
        if fp>=0:out.append(p)
        if (fp>0 and fq<0) or (fp<0 and fq>0):out.append(p+(q-p)*fp/(fp-fq))
    return np.asarray(out)

def moments(poly):
    if len(poly)<3:return 0.,np.zeros(2)
    nxt=np.roll(poly,-1,axis=0);cross=poly[:,0]*nxt[:,1]-poly[:,1]*nxt[:,0]
    area=sum(cross)/2
    return area,np.sum((poly+nxt)*cross[:,None],axis=0)/6

def cutoff(poly,u,m):
    w=moments(poly)[0];p=np.clip(m/w,0,1)
    a,b,c=np.sort(poly@u)
    if p<=(c-b)/(c-a):return c-np.sqrt(p*(c-a)*(c-b))
    return a+np.sqrt((1-p)*(b-a)*(c-a))

def support(polys,u,q):
    ws=np.array([moments(p)[0] for p in polys]);lo=max(0,(q-ws[1])/2);hi=min(ws[0],ws[2],q/2)
    def der(m):return cutoff(polys[0],u,m)+cutoff(polys[2],u,m)-2*cutoff(polys[1],u,q-2*m)
    if der(lo)<=0:m=lo
    elif der(hi)>=0:m=hi
    else:m=brentq(der,lo,hi,xtol=1e-12)
    masses=[m,q-2*m,m];pt=np.zeros(2)
    for p,ma in zip(polys,masses):
        cut=cutoff(p,u,ma);pt+=moments(clip(p,u,cut))[1]
    return pt/q

def centroid_body(polys,q,N):
    ps=np.array([support(polys,np.array([np.cos(t),np.sin(t)]),q) for t in np.linspace(0,2*np.pi,N,endpoint=False)])
    area,m=moments(ps)
    return m/area

def depth_direction(polys,u,y):
    yy=np.dot(u,y)
    br=sorted(set([float((np.dot(u,p)-yy)/z) for z,poly in zip([-1,0,1],polys) if z for p in poly]))
    def fun(v):return sum(moments(clip(p,u,yy+v*z))[0] for z,p in zip([-1,0,1],polys))
    best=(1e9,None)
    for v in br:
        f=fun(v)
        if f<best[0]:best=(f,v)
    for a,b in zip(br[:-1],br[1:]):
        fa=fun(a);fb=fun(b);fm=fun((a+b)/2)
        A=2*(fa+fb-2*fm);B=fb-fa-A
        if A>1e-14:
            h=-B/(2*A)
            if 0<h<1:
                v=a+(b-a)*h;f=fun(v)
                if f<best[0]:best=(f,v)
    return best

K=np.array([[-1/3,-1/3],[2/3,-1/3],[-1/3,2/3]])

a,c=1/8,257/256
s=(1-(a+c)/2)*K[0]
polys=[s+a*K,K,s+c*K]
M=sum(moments(p)[0] for p in polys);q=M/2
for N in [96,384,1536]:
 y=centroid_body(polys,q,N);dd=depth_direction(polys,np.array([-1.,-1.]),y)
 print(N,'M',M,'s',s,'y',y,'depth',dd,'ratio',dd[0]/M,'target',2*M/9,flush=True)
