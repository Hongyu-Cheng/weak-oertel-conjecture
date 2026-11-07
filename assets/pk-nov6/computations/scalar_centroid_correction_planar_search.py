"""Exact rational screening of a proposed scalar correction, not of OC."""
from fractions import Fraction as F
import random
import json

def cross(p,q): return p[0]*q[1]-p[1]*q[0]
def sub(p,q): return (p[0]-q[0],p[1]-q[1])
def dot(p,q): return p[0]*q[0]+p[1]*q[1]
def hull(points):
    pts=sorted(set(points)); chains=[]
    for seq in (pts,list(reversed(pts))):
        out=[]
        for p in seq:
            while len(out)>1 and cross(sub(out[-1],out[-2]),sub(p,out[-1]))<=0: out.pop()
            out.append(p)
        chains.append(out[:-1])
    return chains[0]+chains[1]
def clip(P,u):
    out=[]
    for p,q in zip(P,P[1:]+P[:1]):
        a,b=dot(u,p),dot(u,q)
        if a>=0: out.append(p)
        if a*b<0: out.append(tuple(p[i]+a/(a-b)*(q[i]-p[i]) for i in range(2)))
    return out
def area(P): return sum(cross(p,q) for p,q in zip(P,P[1:]+P[:1]))/2 if P else F(0)
def centroid(P):
    A=area(P)
    return tuple(sum((p[i]+q[i])*cross(p,q) for p,q in zip(P,P[1:]+P[:1]))/(6*A) for i in range(2))
def crossings(P):
    Q=[(-p[0],-p[1]) for p in P]; out=set()
    for a,b in zip(P,P[1:]+P[:1]):
        r=sub(b,a)
        for c,d in zip(Q,Q[1:]+Q[:1]):
            s=sub(d,c); den=cross(r,s)
            if not den: continue
            t=cross(sub(c,a),s)/den; v=cross(sub(c,a),r)/den
            if 0<=t<=1 and 0<=v<=1: out.add((a[0]+t*r[0],a[1]+t*r[1]))
    return out

if __name__=='__main__':
    rng=random.Random(21719); gamma=F(4,9); tested=0
    for trial in range(30000):
        P=hull([(F(rng.randrange(-40,41)),F(rng.randrange(-40,41))) for _ in range(rng.randrange(4,13))])
        if len(P)<3 or any(cross(sub(b,a),(-a[0],-a[1]))<=0 for a,b in zip(P,P[1:]+P[:1])): continue
        V=area(P); g=centroid(P); lo=(F(0),None); hi=None; rows=[]
        for p in crossings(P):
            u=(-p[1],p[0]); f=area(clip(P,u))/V; s=2*dot(u,g)/V
            row=(p,f,s); rows.append(row)
            if s<0:
                q=(f-gamma)/s
                if q>lo[0]:lo=(q,row)
            elif s>0:
                q=(f-gamma)/s
                if hi is None or q<hi[0]:hi=(q,row)
            elif f<gamma: raise AssertionError(('zero projection obstruction',P,row))
        tested+=1
        if hi is not None and lo[0]>hi[0]:
            result=dict(P=P,V=V,g=g,lower=lo,upper=hi,rows=rows,trial=trial)
            print('CERTIFIED SCALAR OBSTRUCTION',str(result),flush=True)
            with open('./scalar_centroid_planar_obstruction.json','w') as f: json.dump(result,f,default=str,indent=2)
            break
    else: print('No scalar obstruction in',tested,'exact polygons; this is only a screen.')
