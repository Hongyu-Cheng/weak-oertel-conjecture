"""Exact finite checks for the all-normal response theorem in the note."""
from fractions import Fraction as F
from itertools import permutations, product


def clip(P,u,c):
    out=[]
    for p,q in zip(P,P[1:]+P[:1]):
        a=sum(x*y for x,y in zip(u,p))+c
        b=sum(x*y for x,y in zip(u,q))+c
        if a>=0:
            out.append(p)
        if a*b<0:
            r=a/(a-b)
            out.append(tuple(p[i]+r*(q[i]-p[i]) for i in range(2)))
    return out


def area(P):
    if len(P)<3:
        return F(0)
    return abs(sum(p[0]*q[1]-p[1]*q[0]
                   for p,q in zip(P,P[1:]+P[:1])))/2


def pair_min(P,u,c,threshold):
    # On each interval between vertex events, the polygon cap sum is quadratic.
    values=[sum(u[i]*p[i] for i in range(2))+c for p in P]
    events=sorted(set([F(-3),F(3)]+[x-threshold for x in values]
                      +[threshold-x for x in values]))
    def cost(s):
        return area(clip(P,u,c-threshold-s))+area(clip(P,u,c-threshold+s))
    best=min((cost(s),s) for s in events)
    for left,right in zip(events,events[1:]):
        mid=(left+right)/2; width=(right-left)/2
        fl,fm,fr=cost(left),cost(mid),cost(right)
        A=(fl+fr-2*fm)/(2*width*width)
        B=(fr-fl)/(2*width)
        for fraction in [F(1,4),F(3,4)]:
            s=left+fraction*(right-left)
            assert cost(s)==A*(s-mid)**2+B*(s-mid)+fm
        if A>0:
            s=mid-B/(2*A)
            if left<s<right:
                best=min(best,(cost(s),s))
    return best


T=[(F(0),F(0)),(F(1),F(0)),(F(0),F(1))]
g=(F(1,3),F(1,3)); V=F(1,2); Gamma=F(4,9)
canonical=[((-1,-1),F(1)),((1,0),F(0)),((0,1),F(0))]
vstar=(F(-1,6),F(-2,3))
Js=[F(1),F(1,3),F(0)]; Jbar=F(4,9); kappa=F(2,3)
assert sum(Js)/3==Jbar
assert [sum(u[i]*vstar[i] for i in range(2)) for u,c in canonical] \
       == [(J-Jbar)/kappa for J in Js]

uniform_checks=0
def tail(threshold,center,width):
    return min(F(1),max(F(0),(center+width-threshold)/(2*width)))
for width in [F(1,16),F(1,8),F(3,16),F(1,2)]:
    for delta in [F(i,32) for i in range(-24,25)]:
        center=F(0); threshold=delta
        shifts=[F(0),width-delta,-width-delta,
                delta-width,delta+width,F(-3),F(3)]
        minimum=min(tail(threshold+s,center,width)+tail(threshold-s,center,width)
                    for s in shifts)
        assert minimum==min(F(1),max(F(0),1-delta/width))
        uniform_checks+=1

canonical_checks=0
motion_checks=0
normals=set()
for r in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
    normals.update(permutations([F(0),r,F(1)]))
for t in [F(1,256),F(1,512),F(1,1024),F(1,2048),F(1,4096)]:
    center=(F(1,4),F(1,4)); v=(F(1,8),F(1,16)); w=(0,1)
    A=[tuple(center[i]+s*v[i]+2*t*r*w[i] for i in range(2))
       for s,r in [(-1,-1),(1,-1),(1,1),(-1,1)]]
    assert area(A)==t
    assert all(x>0 and y>0 and x+y<1 for x,y in A)
    y=tuple(g[i]+t*vstar[i] for i in range(2))
    desired=[Gamma*V+F(4,9)*t+F(25,72)*t*t,
             Gamma*V+F(4,9)*t+F(97,72)*t*t,
             Gamma*V+F(4,9)*t+F(2,9)*t*t]
    for index,(u,c) in enumerate(canonical):
        threshold=sum(u[i]*y[i] for i in range(2))+c
        pair,shift=pair_min(A,u,c,threshold)
        mass=area(clip(T,u,c-threshold))+pair
        assert mass==desired[index]
        canonical_checks+=1
    # At the original g, the y-coordinate cap misses both added bodies.
    assert max(p[1] for p in A)<g[1]
    assert area(clip(A,(0,1),-g[1]))==0
    for values in normals:
        u=(values[1]-values[0],values[2]-values[0]); c=values[0]
        threshold=sum(u[i]*y[i] for i in range(2))+c
        pair,s=pair_min(A,u,c,threshold)
        own=area(clip(T,u,c-threshold))
        # Auxiliary finite normal check. The proof gives the all-normal limit.
        assert own+pair>=Gamma*V+F(4,9)*t-10*t*t
        # Uniform strict base isolation realizes the exact pair cost.
        K=F(10)
        beta=(-K+s/2,-K-s/2)
        total=F(0)
        for z in product([0,1],repeat=2):
            val=area(clip(T,u,c-threshold+sum(beta[i]*z[i] for i in range(2))))
            if z!=(0,0):
                assert val==0
            total+=val
        for z in [(-1,1),(1,-1)]:
            total+=area(clip(A,u,c-threshold+sum(beta[i]*z[i] for i in range(2))))
        assert total==own+pair
        motion_checks+=1

# Same point-mass limits, different exact local response coefficients.
microscopic_checks=0
for r in [F(1,20),F(1,10),F(1,5)]:
    simplex=[tuple(g[i]+r*(p[i]-g[i]) for i in range(2)) for p in T]
    square=[(g[0]+s*r/4,g[1]+z*r/4) for s,z in [(-1,-1),(1,-1),(1,1),(-1,1)]]
    for P,factor in [(simplex,2*Gamma),(square,F(1))]:
        a=area(P)
        for u,c in canonical:
            cost,s=pair_min(P,u,c,F(1,3))
            assert cost==factor*a
            microscopic_checks+=1

print(f'PASS: {uniform_checks} uniform-tail identities, '
      f'{canonical_checks} exact moving canonical expansions, '
      f'{motion_checks} proper-pair/strict-isolation checks, '
      f'{microscopic_checks} boundary-mass response certificates.')
