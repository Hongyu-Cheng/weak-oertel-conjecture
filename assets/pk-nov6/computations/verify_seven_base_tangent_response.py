"""Exact checks for the microscopic global-response example."""
from fractions import Fraction as F
from itertools import permutations, product
from math import factorial, comb


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
normals=set()
for r in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
    normals.update(permutations([F(0),r,F(1)]))

isolation_checks=0; canonical_checks=0
for epsilon in [F(1,50),F(1,100),F(1,200),F(1,400)]:
    t=epsilon**2
    A=[(g[0]+epsilon*s,g[1]+epsilon*r)
       for s,r in [(0,0),(1,0),(1,1),(0,1)]]
    assert area(A)==t
    assert all(x>=0 and y>=0 and x+y<1 for x,y in A)
    assert 81*(2*t/V)**2+108*(2*t/V)-4<0
    y=tuple(x+t/2 for x in g)
    for index,(u,c) in enumerate(canonical):
        threshold=sum(u[i]*y[i] for i in range(2))+c
        pair,s=pair_min(A,u,c,threshold)
        desired_pair=t*t if index==0 else t
        assert pair==desired_pair
        seven=area(clip(T,u,c-threshold))+pair+t
        desired=(Gamma*V+F(5,3)*t
                 +(F(3,2) if index==0 else F(1,8))*t*t)
        assert seven==desired
        canonical_checks+=1
    # Every old prescribed core centroid has depth Gamma V+t or less.
    assert area(clip(A,(-1,-1),1-F(1,3)))==0
    for values in normals:
        u=(values[1]-values[0],values[2]-values[0]); c=values[0]
        threshold=sum(u[i]*y[i] for i in range(2))+c
        pair,s=pair_min(A,u,c,threshold)
        six=area(clip(T,u,c-threshold))+pair
        beta=(F(-10)+s/2,F(-10)-s/2)
        seven=F(0)
        for z in product([0,1],repeat=2):
            mass=area(clip(T,u,c-threshold+sum(beta[i]*z[i] for i in range(2))))
            if z!=(0,0):
                assert mass==0
            seven+=mass
        for z in [(-1,0),(-1,1),(1,-1)]:
            mass=area(clip(A,u,c-threshold+sum(beta[i]*z[i] for i in range(2))))
            if z==(-1,0):
                assert mass==t
            seven+=mass
        assert seven==six+t
        assert seven>=Gamma*V+F(5,3)*t-10*t*t
        isolation_checks+=1

dimension_checks=0
for d in range(2,31):
    m=d+1; V=F(1,factorial(d)); h=F(d,m)
    Gamma=h**d; kappa=d*V*h**(d-1)
    Jbar=F(d,m); v=F(1,m)/kappa
    assert -d*v==(0-Jbar)/kappa
    assert v==(1-Jbar)/kappa
    # Own canonical derivatives plus tangent pair cost and owned mass.
    assert kappa*d*v+1==1+Jbar
    assert -kappa*v+1+1==1+Jbar
    assert 1+Jbar>1
    # Normalized first-order coefficient with total added mass 3t.
    derivative=(4*(1+Jbar)-3*Gamma)/(16*V)
    assert derivative>0
    dimension_checks+=1

print(f'PASS: {canonical_checks} exact moving seven-base canonical expansions, '
      f'{isolation_checks} proper-pair/owned-full isolation checks, '
      f'{dimension_checks} exact all-dimension response balances.')
