"""Exact two-cut polygon and overlap checks for the pentagon theorem."""
from fractions import Fraction as F
from itertools import product


def clip(P,u,c):
    out=[]
    for p,q in zip(P,P[1:]+P[:1]):
        a=sum(x*y for x,y in zip(u,p))+c
        b=sum(x*y for x,y in zip(u,q))+c
        if a>=0:
            out.append(p)
        if a*b<0:
            t=a/(a-b)
            out.append(tuple(p[i]+t*(q[i]-p[i]) for i in range(2)))
    # Drop repeated and collinear vertices, retaining the actual polygon.
    P=[]
    for p in out:
        if not P or p!=P[-1]:
            P.append(p)
    if len(P)>1 and P[0]==P[-1]:
        P.pop()
    changed=True
    while changed and len(P)>2:
        changed=False
        for i in range(len(P)):
            a,b,c0=P[i-1],P[i],P[(i+1)%len(P)]
            if (b[0]-a[0])*(c0[1]-b[1])==(b[1]-a[1])*(c0[0]-b[0]):
                P.pop(i);changed=True;break
    return P


def area(P):
    if len(P)<3:
        return F(0)
    return abs(sum(p[0]*q[1]-p[1]*q[0]
                   for p,q in zip(P,P[1:]+P[:1])))/2


def cut_data(vertex,short_neighbor,rs,rl):
    long_neighbor=3-vertex-short_neighbor
    coeff=[F(0)]*3
    coeff[short_neighbor]=1/rs
    coeff[long_neighbor]=1/rl
    u=(coeff[1]-coeff[0],coeff[2]-coeff[0]);c=coeff[0]-1
    return {'vertex':vertex,'short':short_neighbor,'long':long_neighbor,
            'u':u,'c':c,'mass':rs*rl}


T=[(F(0),F(0)),(F(1),F(0)),(F(0),F(1))]
V=F(1,2);G=F(4,9);partial=F(3,20)
assert F(9,29)-F(1,1550)>F(309,1000)
assert (1-F(309,501))**2==F(64,167)**2<partial
assert partial-F(64,167)**2==F(1747,557780)
normals=[(F(i),F(j)) for i,j in product(range(-8,9),repeat=2) if i or j]
profiles=[]
for e in [F(1,1000000),F(1,2000000),F(1,10000000)]:
    for L in [F(1,5),F(2,5),F(499,1000)]:
        # Distinct vertices, long directions facing each other.
        profiles.append([cut_data(0,2,e,L),cut_data(1,2,e/2,F(1,2))])
        # Distinct vertices, long directions both toward the third vertex.
        profiles.append([cut_data(0,1,e,L),cut_data(1,0,e/2,F(1,2))])
        # Same vertex, opposed thin directions.
        profiles.append([cut_data(0,2,e,L),cut_data(0,1,e/2,F(1,2))])
    # Same vertex and same long direction: large overlap, both cuts active.
    profiles.append([cut_data(0,2,e,F(2,5)),cut_data(0,2,F(9,10)*e,F(1,2))])

cap_checks=0;overlap_checks=0
for cuts in profiles:
    Q=T
    removed=[]
    for C in cuts:
        Q=clip(Q,C['u'],C['c'])
        removed.append(clip(T,tuple(-x for x in C['u']),-C['c']))
        assert area(removed[-1])/V==C['mass']
    assert len(Q)==5
    tau=1-area(Q)/V
    assert 0<tau<F(1,10000)
    intersection=clip(removed[0],tuple(-x for x in cuts[1]['u']),-cuts[1]['c'])
    assert tau==sum(C['mass'] for C in cuts)-area(intersection)/V
    loss=[F(0)]*3
    if cuts[0]['vertex']!=cuts[1]['vertex']:
        assert area(intersection)==0
        for C in cuts:
            loss[C['vertex']]+=C['mass']
            loss[C['long']]+=partial*C['mass']
        assert sum(loss)==F(23,20)*tau
    else:
        loss[cuts[0]['vertex']]=tau
        for C in cuts:
            loss[C['long']]+=partial*C['mass']
        assert sum(C['mass'] for C in cuts)<=2*tau
        overlap_checks+=1
    assert all(0<=L<=tau for L in loss)
    assert sum(loss)<=F(13,10)*tau
    mean=sum(loss)/3
    lam=[F(1,3)+F(3,4)*(mean-L) for L in loss]
    assert sum(lam)==1
    assert all(abs(x-F(1,3))<=F(1,10000) for x in lam)
    y=(lam[1],lam[2])
    assert all(sum(C['u'][i]*y[i] for i in range(2))+C['c']>0 for C in cuts)
    low=G-F(13,30)*tau-F(9,4)*tau*tau
    assert low/(1-tau)-G-tau/180==tau*(1-404*tau)/(180*(1-tau))
    assert low/(1-tau)>=G+tau/180
    for u in normals:
        c=-sum(u[i]*y[i] for i in range(2))
        full=area(clip(T,u,c))/V
        actual=area(clip(Q,u,c))/V
        assert actual>=low
        if full<=G+F(1,10000):
            signs=[sum(u[i]*p[i] for i in range(2))+c>0 for p in T]
            assert sum(signs)==1
            index=signs.index(True)
            assert full-actual<=loss[index]
        cap_checks+=1

# Exact high-overlap calibration where naive entire-piece summation fails.
e=F(1,1000000)
t1,t2=F(2,5)*e,F(9,20)*e
intersection=F(27,70)*e
tau=t1+t2-intersection
assert tau==F(13,28)*e
assert (t1+t2)/tau==F(119,65)
assert F(23,20)*(t1+t2)>F(4,3)*tau
assert (tau+partial*(t1+t2))/tau==F(1657,1300)<F(13,10)

normalization_checks=0
for delta in [F(1,1000000*i) for i in range(1,101)]:
    assert (5*delta+40*delta**2)/(1-64*delta**2)<=6*delta
    assert 25*delta/(1-17*delta)<=26*delta
    assert 5*delta+8*delta*(1+26*delta)<=14*delta
    assert F(43)*delta/(1-72*delta)<=44*delta
    assert F(1,2)+44*delta<F(501,1000)
    assert (80*delta+2576*delta**2)/(1+72*delta+2592*delta**2)<=81*delta
    assert 81*delta<F(1,10000)
    assert 1-16*delta-64*delta**2>0
    normalization_checks+=1

print(f'PASS: {len(profiles)} actual pentagons, {cap_checks} rational cap checks, '
      f'{overlap_checks} same-vertex unions, {normalization_checks} normalization '
      'constant cases; exact high-overlap obstruction and union repair.')
