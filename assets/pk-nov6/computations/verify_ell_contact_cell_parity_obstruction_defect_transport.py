"""Exact finite certificate, including every proper closed-minor quota."""
from fractions import Fraction as F
import sympy as s

P=[(x,y) for x in range(-1,3) for y in range(-1,2)]
def q(p):return 2*p[0]+p[1]-1
def ell(p):return 5-abs(q(p))
def reflect(p):return (1-p[0],-p[1])
def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
def hull(ps):
    ps=sorted(ps)
    if len(ps)<=1:return ps
    lo=[];up=[]
    for p in ps:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=0:lo.pop()
        lo.append(p)
    for p in reversed(ps):
        while len(up)>=2 and cross(up[-2],up[-1],p)<=0:up.pop()
        up.append(p)
    return lo[:-1]+up[:-1]
def inside(p,h):
    if len(h)==1:return p==h[0]
    if len(h)==2:
        return (cross(h[0],h[1],p)==0
                and min(h[0][0],h[1][0])<=p[0]<=max(h[0][0],h[1][0])
                and min(h[0][1],h[1][1])<=p[1]<=max(h[0][1],h[1][1]))
    return all(cross(h[i],h[(i+1)%len(h)],p)>=0 for i in range(len(h)))
def closed_minors():
    ans=[]
    for mask in range(1,(1<<len(P))-1):
        S=[P[j] for j in range(len(P)) if mask>>j&1]
        H=hull(S)
        if all(inside(P[j],H)==bool(mask>>j&1) for j in range(len(P))):
            ans.append(mask)
    return ans

def main():
    checks=0
    for p in P:
        assert ell(p)>0 and reflect(p) in P and ell(reflect(p))==ell(p)
        checks+=3
    J=[(0,0),(1,0)]
    assert [p for p in P if inside(p,hull(J))]==J
    checks+=1
    L=[p for p in P if q(p)<=0];R=[p for p in P if q(p)>=0]
    assert [p for p in P if inside(p,hull(L))]==L
    assert [p for p in P if inside(p,hull(R))]==R
    assert all(cross(hull(L)[i],hull(L)[(i+1)%4],J[0])>0 for i in range(4))
    assert all(cross(hull(R)[i],hull(R)[(i+1)%4],J[1])>0 for i in range(4))
    checks+=4
    parities=lambda S:{(x%2,y%2) for x,y in S}
    assert len(parities(P))==len(parities(L))==len(parities(R))==4
    assert len(parities([p for p in P if q(p)<0]))==4
    assert len(parities([p for p in P if q(p)>0]))==4
    checks+=3

    order=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1)]
    left=dict(zip(order,[F(v,12) for v in [1,1,1,1,1,4,3]]))
    right={reflect(p):v for p,v in left.items()}
    target={p:left.get(p,0)+right.get(p,0) for p in P}
    for source,row in zip(J,[left,right]):
        assert sum(row.values())==1
        assert tuple(sum(v*p[c] for p,v in row.items()) for c in range(2))==source
        assert sum(v*ell(p) for p,v in row.items())==ell(source)
        checks+=3
    assert all(v>0 for v in target.values()) and sum(target.values())==2
    checks+=1

    # Exact canonical 3D radius construction modulo its defining polynomial.
    r=s.symbols('r')
    poly=67*r**3-735*r**2+2685*r-3365
    assert poly.subs(r,4)==-97 and poly.subs(r,5)==60
    assert s.diff(poly,r).subs(r,4)==21
    assert s.diff(poly,r,2).subs(r,4)==138
    checks+=3
    a=(r-4)**3;b=(r-3)**3/2;c=(r-2)**3/3;d=(r-1)**3/4;g=r**3/5
    assert s.expand(g-3*a-2*b-2*c+poly/15)==0
    row=dict(zip(order,[a,b,c,c,d,2*a+b+c,a+b+c]))
    m=4*a+3*b+4*c+d
    assert s.expand(sum(row.values())-m)==0
    assert all(s.expand(sum(v*p[c0] for p,v in row.items()))==0 for c0 in range(2))
    checks+=3
    for p in P:
        prescribed=(r-abs(q(p)))**3/ell(p)
        observed=row.get(p,0)+row.get(reflect(p),0)
        assert s.rem(s.together(observed-prescribed),poly,r)==0
        checks+=1
    volume=sum((r-abs(q(p)))**3 for p in P)
    assert s.rem(volume-8*m,poly,r)==0
    lo,hi=F(24,5),F(481,100)
    assert poly.subs(r,s.Rational(lo.numerator,lo.denominator))<0
    assert poly.subs(r,s.Rational(hi.numerator,hi.denominator))>0
    lowergap=7*(lo-4)**3+2*(lo-3)**3+F(2,3)*(lo-2)**3-F(1,2)*(hi-1)**3
    assert lowergap==F(13376977,6000000)>0
    checks+=4

    # Stronger pure-weight certificate: all strict closed-minor quotas.
    numerators=[1,2,600,600,1772,2025,2025,1772,600,600,2,1]
    V=dict(zip(P,[F(v,10000) for v in numerators]))
    assert sum(V.values())==1
    a=b=F(1,10000);c=d=F(1,50);e=F(443,10000)
    row=dict(zip(order,[a,b,c,d,e,2*a+b+d,a+b+c]))
    m=sum(row.values())
    assert m==F(1,8)
    for source,rr in [(J[0],row),(J[1],{reflect(p):v for p,v in row.items()})]:
        assert tuple(sum(v*p[c0] for p,v in rr.items()) for c0 in range(2))==tuple(m*t for t in source)
        assert sum(v*ell(p) for p,v in rr.items())==m*ell(source)
        checks+=2
    for p in P:
        assert row.get(p,0)+row.get(reflect(p),0)==V[p]/ell(p)>0
        checks+=1
    minimum={k:None for k in range(1,5)}
    minors=closed_minors()
    assert len(minors)==704
    for mask in minors:
        indices=[j for j in range(len(P)) if mask>>j&1]
        k=len(parities([P[j] for j in indices]))
        gap=2500*k-sum(numerators[j] for j in indices)
        assert gap>0
        minimum[k]=gap if minimum[k] is None else min(minimum[k],gap)
        checks+=1
    # Explicitly not an interval-radius realization of these rational V.
    assert V[(-1,0)]<(V[(-1,-1)]+V[(-1,1)])/2
    checks+=1
    print(f'{checks} exact checks PASS; all {len(minors)} proper closed minors')
    print('Minimum quota slacks, in units 1/10000, by parity count:',minimum)

    # Final stronger rational certificate: an actual canonical interval
    # roof, all strict quotas, and the exact V/ell target simultaneously.
    nums=[2,2,2,136,203,270,270,203,136,2,2,2]
    volumes=dict(zip(P,[F(v,1230) for v in nums]))
    def planes(p):
        x,y=p
        return [270+67*q(p),270-67*q(p),270+268*x,538-268*x]
    assert sum(volumes.values())==1
    for p in P:
        assert volumes[p]==F(min(planes(p)),1230)>0
        checks+=1
    triangles=[([(-1,-1),(-1,1),(0,1)],2),
               ([(-1,-1),(0,1),(1,-1)],0),
               ([(0,1),(1,-1),(2,1)],1),
               ([(1,-1),(2,-1),(2,1)],3)]
    assert sum(abs(cross(*tri)) for tri,plane in triangles)==12
    for tri,plane in triangles:
        # Affine inequalities at all triangle vertices certify the same
        # supporting affine plane is minimal on the entire triangle.
        for p in tri:
            assert p in P and planes(p)[plane]==min(planes(p))
            checks+=1
    row=dict(zip(order,[F(v,14760) for v in [24,12,8,544,609,604,44]]))
    assert sum(row.values())==F(1,8)
    assert all(sum(v*p[c0] for p,v in row.items())==0 for c0 in range(2))
    checks+=2
    for p in P:
        assert row.get(p,0)+row.get(reflect(p),0)==volumes[p]/ell(p)>0
        checks+=1
    gapmin={k:None for k in range(1,5)}
    for mask in minors:
        indices=[j for j in range(len(P)) if mask>>j&1]
        k=len(parities([P[j] for j in indices]))
        gap=1230*k-4*sum(nums[j] for j in indices)
        assert gap>0
        gapmin[k]=gap if gapmin[k] is None else min(gapmin[k],gap)
        checks+=1
    print(f'{checks} total exact checks PASS including canonical interval/strict-quota certificate')
    print('Interval quota slacks, in units 1/4920, by parity count:',gapmin)

if __name__=='__main__':main()
