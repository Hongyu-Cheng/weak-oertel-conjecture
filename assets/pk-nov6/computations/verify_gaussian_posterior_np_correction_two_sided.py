"""Exact knapsack/dual, interval correction region and cube calibration."""
from fractions import Fraction as F
from itertools import product

checks=0

def B(p,pi,q):
    order=sorted(range(len(p)),key=lambda i: pi[i]/p[i])
    cost=F(0)
    left=q
    for i in order:
        take=min(left,p[i])
        cost+=take*pi[i]/p[i]
        left-=take
        if not left:
            break
    assert not left
    return cost

def dual(p,pi,q):
    eta={F(0)}|{pi[i]/p[i] for i in range(len(p))}
    return max(e*q-sum(max(e*p[i]-pi[i],F(0)) for i in range(len(p)))
               for e in eta)

def triples(den):
    return [(F(i,den),F(j,den),F(den-i-j,den))
            for i in range(1,den) for j in range(1,den-i)]

for p,pi in product(triples(8),repeat=2):
    for q in (F(0),F(1,7),F(1,4),F(4,9),F(3,4),F(1)):
        assert B(p,pi,q)==dual(p,pi,q)
        assert B(p,pi,q)>=q/max(p[i]/pi[i] for i in range(3))
        checks+=2
    for gamma in (F(1,2),F(4,9),F(27,64)):
        assert B(p,pi,gamma*max(p))<=gamma*max(pi)
        checks+=1

pi=(F(1,3),)*3
for bi in range(1,17):
    b=F(bi,16)
    for ri in range(16,129):
        r=F(ri,16)
        raw=(b/r,F(1),b*r)
        p=tuple(x/sum(raw) for x in raw)
        middle=p[1]/2+p[0]
        endpoint=p[2]/2
        dep=max(middle,endpoint)
        criterion=(2+4*b/r>=3*max(F(1),b*r))
        assert (B(p,pi,dep)>=F(1,4))==criterion
        assert criterion==((r<=4*b) and (3*b*r*r<=2*r+4*b))
        assert (middle>endpoint)==(b*r<1+2*b/r)
        osc=max(p)/min(p)
        if endpoint>middle:
            assert osc==r*r>4
        assert B(p,pi,F(1,2)*max(p))==F(1,6)
        checks+=5

for b in [F(j,20) for j in range(1,11)]:
    p=(b/(1+2*b),1/(1+2*b),b/(1+2*b))
    assert B(p,pi,F(1,2))==(1+2*b)/6
    checks+=1

p=(F(1,9),F(4,9),F(4,9))
assert B(p,pi,F(1,3))==F(1,4)
p=(F(1,81),F(16,81),F(64,81))
assert B(p,pi,F(32,81))==F(1,6)
checks+=2

for n in range(1,5):
    P=list(product((0,1),repeat=n))
    for odds in product((F(1,3),F(1),F(4)),repeat=n):
        raw=[]
        for z in P:
            v=F(1)
            for j in range(n):
                if z[j]:
                    v*=odds[j]
            raw.append(v)
        p=tuple(v/sum(raw) for v in raw)
        pi=tuple(F(1,len(P)) for _ in P)
        for d in range(1,5):
            gamma=F(d,d+1)**d
            assert B(p,pi,gamma*max(p))==gamma/len(P)
            checks+=1

print(f'{checks} exact checks PASS; NP dual, all interval branches and cube calibration')
