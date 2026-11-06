"""Bounded exact planar screening; evidence only unless a rational failure appears."""
from fractions import Fraction as F
import random

def upper_hull(points):
    out=[]
    for x,y in sorted((F(x),F(y)) for x,y in points):
        while len(out)>1 and (out[-1][1]-out[-2][1])*(x-out[-1][0]) <= (y-out[-1][1])*(out[-1][0]-out[-2][0]):
            out.pop()
        out.append((x,y))
    return out

def examine(P):
    M=F(0); J=F(0)
    for (a,fa),(b,fb) in zip(P,P[1:]):
        w=b-a; M+=w*(fa+fb)/2
        J+=a*w*(fa+fb)/2+w*w*(fa+2*fb)/6
    if M==0:return None
    mean=J/M; Q=[(x-mean,y) for x,y in P]
    def density(x):
        for (a,fa),(b,fb) in zip(Q,Q[1:]):
            if a<x<b:return fa+(fb-fa)*(x-a)/(b-a)
        return F(0)
    def cdf(x):
        out=F(0)
        for (a,fa),(b,fb) in zip(Q,Q[1:]):
            if x<=a:break
            e=min(x,b); w=e-a
            out+=fa*w+(fb-fa)*w*w/(2*(b-a))
        return out
    events=sorted({F(0)}|{abs(x) for x,y in Q})
    candidates=events[:]
    for a,b in zip(events,events[1:]):
        p=(2*a+b)/3; q=(a+2*b)/3
        dp=density(p)-density(-p)/2
        dq=density(q)-density(-q)/2
        if dp!=dq:
            root=p-dp*(q-p)/(dq-dp)
            if a<root<b:candidates.append(root)
    f0=M-cdf(0)
    val,shift=min((f0+M-cdf(s)+(M-cdf(-s))/2,s) for s in candidates)
    return val/M,shift,mean,M,P

if __name__=='__main__':
    random.seed(150921)
    best=(F(10),None)
    for it in range(20000):
        count=random.randrange(2,10)
        points=[(i,random.randrange(0,40)) for i in range(count+1)]
        P=upper_hull(points)
        for Q in [P,[(-x,y) for x,y in P[::-1]]]:
            ans=examine(Q)
            if ans is None:continue
            if ans[0]<best[0]:
                best=(ans[0],ans)
            if ans[0]<F(17,18):
                print('EXACT FAILURE',ans,flush=True)
                raise SystemExit
    print('NO FAILURE in bounded planar screen; minimum',best,flush=True)
