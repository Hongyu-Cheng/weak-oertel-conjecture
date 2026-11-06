"""Exact finite checks for the arbitrary-union planar stability proof.

The analytic source proves arbitrary (including infinite) unions and
all halfspaces. This verifier uses exact rational union integration,
overlapping finite cap families, and actual many-cut polygons.
"""
from fractions import Fraction as F
from itertools import product


def area(P):
    if len(P)<3:
        return F(0)
    return abs(sum(p[0]*q[1]-p[1]*q[0]
                   for p,q in zip(P,P[1:]+P[:1])))/2


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
    return out


def union_area(cuts,lower=F(0)):
    """Area above v=lower of union {u/a+v/b<=1}; exact max-line integral."""
    if not cuts:
        return F(0)
    upper=max(b for a,b in cuts)
    if lower>=upper:
        return F(0)
    knots={lower,upper}
    lines=[(a,-a/b) for a,b in cuts]
    for a,b in cuts:
        if lower<b<upper:
            knots.add(b)
    for (c,m),(d,n) in product(lines,repeat=2):
        if m!=n:
            v=(d-c)/(m-n)
            if lower<v<upper:
                knots.add(v)
    knots=sorted(knots)
    total=F(0)
    for lo,hi in zip(knots,knots[1:]):
        mid=(lo+hi)/2
        c,m=max([(F(0),F(0))]+lines,key=lambda cm:cm[0]+cm[1]*mid)
        total+=c*(hi-lo)+m*(hi*hi-lo*lo)/2
    return total


B=F(501,1000);s=F(309,1000);r=F(64,167);kappa=F(3,20)
assert r==1-s/B and r*r<kappa
assert F(9,29)-F(1,1550)>s
assert kappa-r*r==F(1747,557780)
U=F(30000,9997);P=F(90000,40009)
assert P-F(29,20)*(U-F(29,20))==F(110147293,159987989200)
assert P-F(31,20)*(U-F(31,20))==F(95744053,159987989200)

families=[]
for scale in [F(1,100),F(1,10000),F(1,1000000)]:
    for count in range(1,13):
        # Crossing roofs and nested roofs, all at one vertex orientation.
        families.append([(scale*F(count+2-i,count+2),
                          B*F(i+2,count+2)) for i in range(count)])
        families.append([(scale*F(i+2,count+2),
                          B*F(i+2,count+2)) for i in range(count)])
        families.append([(scale*F(2+(7*i)%13,15),
                          B*F(2+(11*i)%17,19)) for i in range(count)])
union_checks=point_checks=0
for cuts in families:
    total=union_area(cuts)
    tail=union_area(cuts,s)
    assert 0<total<=sum(a*b/2 for a,b in cuts)
    assert tail<=r*r*total
    for a,b in cuts:
        for i,j in product(range(11),repeat=2):
            if i+j>10:
                continue
            u,v=a*F(i,10),b*F(j,10)
            if v>=s:
                up,vp=u/r,(v-s)/r
                assert up>=0 and vp>=0
                assert up/a+vp/b<=(1-s/b)/r<=1
                point_checks+=1
    union_checks+=1

T=[(F(0),F(0)),(F(1),F(0)),(F(0),F(1))]
V=F(1,2);Gamma=F(4,9)
normals=[(F(i),F(j)) for i,j in product(range(-5,6),repeat=2) if i or j]
poly_checks=cap_checks=0
for seed in range(1,25):
    cuts=[]
    epsilon=F(1,1000000*(1+seed%3))
    for vertex in range(3):
        for index in range(2+seed%5):
            short=(vertex+1+index%2)%3
            long=3-vertex-short
            a=epsilon*F(2+(7*index+seed)%11,13)
            b=F(2+(5*index+vertex+seed)%13,30) # <=14/30<1/2
            coeff=[F(0)]*3
            coeff[short]=1/a;coeff[long]=1/b
            cuts.append((vertex,short,long,a,b,coeff))
    Q=T
    for vertex,short,long,a,b,coeff in cuts:
        Q=clip(Q,(coeff[1]-coeff[0],coeff[2]-coeff[0]),coeff[0]-1)
    tau=1-area(Q)/V
    assert 0<tau<F(1,10000)
    masses=[];orient={}
    for vertex in range(3):
        neighbors=[j for j in range(3) if j!=vertex]
        local=[]
        for v,short,long,a,b,coeff in cuts:
            if v!=vertex:
                continue
            intercept=(1/coeff[neighbors[0]],1/coeff[neighbors[1]])
            local.append(intercept)
        masses.append(union_area(local)/V)
        for long in neighbors:
            short=3-vertex-long
            group=[(1/coeff[short],1/coeff[long])
                   for v,sh,lo,a,b,coeff in cuts
                   if v==vertex and 1/coeff[short]<=F(1,100)]
            orient[vertex,long]=union_area(group)/V
            assert union_area(group,s)<=r*r*union_area(group)
    assert sum(masses)==tau
    loss=[masses[i]+kappa*sum(orient[j,i] for j in range(3) if j!=i)
          for i in range(3)]
    assert all(0<=li<=tau for li in loss)
    assert sum(loss)<=F(13,10)*tau
    mean=sum(loss)/3
    lam=[F(1,3)+F(3,4)*(mean-li) for li in loss]
    assert sum(lam)==1
    assert all(abs(x-F(1,3))<F(1,10000) for x in lam)
    y=(lam[1],lam[2])
    assert all(sum(coeff[i]*lam[i] for i in range(3))>1
               for v,short,long,a,b,coeff in cuts)
    low=Gamma-F(13,30)*tau-F(9,4)*tau*tau
    assert low/(1-tau)-Gamma-tau/180==tau*(1-404*tau)/(180*(1-tau))
    assert low/(1-tau)>=Gamma+tau/180
    for u in normals:
        c=-sum(u[i]*y[i] for i in range(2))
        full=area(clip(T,u,c))/V
        actual=area(clip(Q,u,c))/V
        assert actual>=low
        if full<=Gamma+F(1,10000):
            signs=[sum(u[i]*p[i] for i in range(2))+c>0 for p in T]
            assert sum(signs)==1
            assert full-actual<=loss[signs.index(True)]
        cap_checks+=1
    poly_checks+=1

print(f'PASS: {union_checks} exact overlapping union integrals, '
      f'{point_checks} constituent-preserving tail maps, '
      f'{poly_checks} actual many-cut polygons and {cap_checks} rational caps; '
      'all loss, candidate, and coefficient constants exact.')
