"""Bounded higher-dimensional falsification screen; numerical evidence only."""
import random, math

def hull(points):
    out=[]
    for x,y in points:
        while len(out)>1 and (out[-1][1]-out[-2][1])*(x-out[-1][0]) <= (y-out[-1][1])*(out[-1][0]-out[-2][0]):out.pop()
        out.append((x,y))
    return out

def examine(P,d):
    p=d-1; M=0.; J=0.
    for (a,fa),(b,fb) in zip(P,P[1:]):
        w=b-a;dh=fb-fa
        if dh:
            ar=w*(fb**(p+1)-fa**(p+1))/(dh*(p+1))
            mo=w*w*((fb**(p+2)-fa**(p+2))/(p+2)-fa*(fb**(p+1)-fa**(p+1))/(p+1))/(dh*dh)
        else:ar=w*fa**p;mo=w*w*fa**p/2
        M+=ar;J+=a*ar+mo
    if M<=0:return None
    mean=J/M;Q=[(x-mean,y) for x,y in P]
    def root(x):
        for (a,fa),(b,fb) in zip(Q,Q[1:]):
            if a<x<b:return fa+(fb-fa)*(x-a)/(b-a)
        return 0.
    def cdf(x):
        out=0.
        for (a,fa),(b,fb) in zip(Q,Q[1:]):
            if x<=a:break
            e=min(x,b);w=e-a;sl=(fb-fa)/(b-a)
            if sl:out+=((fa+sl*w)**(p+1)-fa**(p+1))/(sl*(p+1))
            else:out+=w*fa**p
        return out
    ev=sorted({0.}|{abs(x) for x,y in Q});can=ev[:];q=2**(-1/p)
    for a,b in zip(ev,ev[1:]):
        x=(2*a+b)/3;y=(a+2*b)/3
        dx=root(x)-q*root(-x);dy=root(y)-q*root(-y)
        if abs(dx-dy)>1e-15:
            t=x-dx*(y-x)/(dy-dx)
            if a<t<b:can.append(t)
    f0=M-cdf(0)
    val,t=min((f0+M-cdf(s)+(M-cdf(-s))/2,s) for s in can)
    return val/M,t,mean,P

random.seed(9141621)
for d in [3,4,5,8,20,100]:
    best=(10.,None);goal=(d/(d+1))**d+.5
    for it in range(10000):
        n=random.randrange(2,12)
        P=hull([(i,random.randrange(0,31)/30) for i in range(n+1)])
        for Q in [P,[(-x,y) for x,y in P[::-1]]]:
            res=examine(Q,d)
            if res is None:continue
            if res[0]<best[0]:best=(res[0],res)
            if res[0]<goal-1e-9:
                print('POTENTIAL FAILURE',d,goal,res,flush=True);raise SystemExit
    print('NO FAILURE d',d,'minimum',best,'target',goal,flush=True)
