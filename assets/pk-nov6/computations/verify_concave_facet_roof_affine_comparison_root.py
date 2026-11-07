"""Exact piecewise-linear roofs and actual polygon comparisons."""
from fractions import Fraction as Q
import random

def area(P):
    return abs(sum(x*v-y*u for (x,y),(u,v) in zip(P,P[1:]+P[:1])))/2

def clip(P,u,v,c):
    out=[]
    for p,q in zip(P,P[1:]+P[:1]):
        a=u*p[0]+v*p[1]-c; b=u*q[0]+v*q[1]-c
        if a>=0: out.append(p)
        if a*b<0:
            t=a/(a-b)
            out.append((p[0]+t*(q[0]-p[0]),p[1]+t*(q[1]-p[1])))
    return out

rng=random.Random(819573)
count=0
for k in range(200):
    c0=Q(rng.randrange(6),7); c1=Q(rng.randrange(6),7)
    tents=[(Q(rng.randrange(1,24),24),Q(rng.randrange(1,10),7))
           for _ in range(rng.randrange(1,7))]
    def psi(s):
        return c0*(1-s)+c1*s+sum(w*min((1-p)*s,p*(1-s)) for p,w in tents)
    cuts=sorted({Q(0),Q(1,3),Q(2,3),Q(1),*(p for p,w in tents)})
    def integral(f,lo=Q(0),hi=Q(1)):
        q=[x for x in cuts if lo<=x<=hi]
        assert q[0]==lo and q[-1]==hi
        return sum((b-a)*(f(a)+f(b))/2 for a,b in zip(q,q[1:]))
    b=3*(psi(Q(2,3))-psi(Q(1,3)))
    a=psi(Q(1,3))-b/3
    ell=lambda s:a+b*s
    assert min(a,a+b)>=0
    assert all((psi(s)-ell(s)>=0 if Q(1,3)<=s<=Q(2,3)
                else psi(s)-ell(s)<=0) for s in cuts)
    Z=integral(psi); Zi=integral(psi,Q(1,3),Q(2,3))
    E=Zi-Z/3
    A=integral(lambda s:psi(s)-ell(s),Q(1,3),Q(2,3))
    B=integral(lambda s:ell(s)-psi(s),Q(0),Q(1,3))+integral(lambda s:ell(s)-psi(s),Q(2,3),Q(1))
    assert E==(2*A+B)/3>0 and A+B<=3*E
    assert (Z+Zi)/3-Q(4,9)*Z==E/3
    for eps in [Q(1,1000),Q(1,500),Q(1,250)]:
        K=[(Q(0),Q(-1)),(Q(1),Q(0))]+[(s,eps*psi(s)) for s in reversed(cuts)]
        sp=(1+eps*a)/(1-eps*b)
        L=[(Q(0),Q(-1)),(sp,sp-1),(Q(0),eps*a)]
        intersect=clip(K,eps*b,Q(-1),-eps*a)
        tail=eps**2*(a+b)**2/(2*(1-eps*b))
        assert sp>=1
        assert area(K)==Q(1,2)+eps*Z
        assert area(L)==(1+eps*a)**2/(2*(1-eps*b))
        assert area(K)-area(intersect)==eps*A
        assert area(L)-area(intersect)==eps*B+tail
        assert 1-area(intersect)/max(area(K),area(L))==max(eps*A,eps*B+tail)/max(area(K),area(L))
        count+=1

for a in [Q(0),Q(1,2),Q(1),Q(2)]:
    for end in [Q(0),Q(1,3),Q(1),Q(3)]:
        if a+end==0: continue
        b=end-a
        for eps in [Q(1,1000),Q(1,500),Q(1,100)]:
            sp=(1+eps*a)/(1-eps*b)
            total=(1+eps*a)**2/(2*(1-eps*b))
            tail=eps**2*end**2/(2*(1-eps*b))
            tau=(eps*end/(1+eps*a))**2
            assert tail/total==tau==((sp-1)/sp)**2
            count+=1
print(f"PASS {count} exact roof-deficit and convex-polygon comparison checks")
