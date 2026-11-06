#!/usr/bin/env python3
from fractions import Fraction as F
from random import Random

checks=0


def check(x):
    global checks
    assert x
    checks+=1


def prod(xs):
    result=F(1)
    for x in xs:result*=x
    return result


rng=Random(891457)
for d in range(2,16):
    m=d+1
    gamma=F(d,m)**d
    coefficient=gamma-F(1,m)
    check(coefficient>0)
    for scale in (1,2,7,19):
        t=gamma*coefficient/F(8*scale)
        check(t<=gamma/4)
        for trial in range(16):
            weights=[rng.randrange(11) for _ in range(m)]
            if sum(weights)==0:weights[0]=1
            ti=[t*F(w,sum(weights)) for w in weights]
            bi=[x-t/m for x in ti]
            lambdas=[(1-x/gamma)/m for x in bi]
            check(sum(bi)==0)
            check(sum(abs(x) for x in bi)<=2*t)
            check(sum(lambdas)==1 and all(x>0 for x in lambdas))
            values=[]
            for i in range(m):
                xx=[-bi[j]/gamma for j in range(m) if j!=i]
                S=sum(abs(x) for x in xx)
                check(S<=F(1,2))
                check(abs(prod(1+x for x in xx)-1-sum(xx))<=S*S)
                value=d**d*prod(lambdas[j] for j in range(m) if j!=i)-ti[i]
                check(value>=gamma-t/m-4*t*t/gamma)
                values.append(value)
            lower=min(values)/(1-t)-gamma
            check(lower>=(coefficient*t-4*t*t/gamma)/(1-t))
            check(lower>=coefficient*t/2)


def area(poly):
    if len(poly)<3:return F(0)
    return abs(sum(p[0]*q[1]-p[1]*q[0]
                   for p,q in zip(poly,poly[1:]+poly[:1])))/2


def clip(poly,normal,threshold):
    def f(p):return sum(a*x for a,x in zip(normal,p))-threshold
    out=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        fp,fq=f(p),f(q)
        if fp>=0:out.append(p)
        if fp*fq<0:
            r=fp/(fp-fq)
            out.append(tuple((1-r)*x+r*y for x,y in zip(p,q)))
    return out


for h in (F(1,100),F(1,200),F(3,1000),F(7,10000)):
    for k in (F(1,100),F(1,300),F(2,1000),F(11,10000)):
        p=(1+h-k,k)
        b=1+h/(1-k)
        Q=[(F(0),F(0)),(F(1),F(0)),p,(F(0),F(1))]
        S=[(F(0),F(0)),(b,F(0)),(F(0),F(1))]
        tau=h*k/(1+h-k)
        r1=h/(1+h-k)
        check(area(Q)==(1+h)/2)
        check(area(S)==b/2)
        check(1-area(Q)/area(S)==tau)
        check(tau==r1*k)
        check(p[0]/b+p[1]==1)
        normal=(k,k-h)
        check(area(clip(S,normal,k))/area(S)==tau)
        check(area(clip(Q,normal,k))==0)
        check(1/b>=1-max(r1,k))
        check(p[0]/b>=1-max(r1,k))

# Rational square roots make exact depth and the quantitative gap checkable.
for u in (F(1,100),F(1,200),F(1,300),F(1,500)):
    a=2*u/(1-3*u*u)
    root=(1+3*u*u)/(1-3*u*u)
    tau=a*a
    k=2*a
    h=tau*(1-k)/(k-tau)
    check(root*root==1+3*tau)
    check(h>0 and 0<k<1)
    check(h*k/(1+h-k)==tau)
    check(tau<=F(1,162))
    absolute=2*(1+root)/9-2*tau/3
    depth=absolute/(1-tau)
    check(depth-F(4,9)>=tau/18)
    check(depth-F(4,9)>0)

print(f"PASS {checks} exact checks")
