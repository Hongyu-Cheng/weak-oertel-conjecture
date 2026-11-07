"""Independent exact rational nonhomothetic strictification examples."""
from fractions import Fraction as Q


def cross(o,a,b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])


def hull(points):
    points=sorted(set(points))
    lower=[]
    for p in points:
        while len(lower)>1 and cross(lower[-2],lower[-1],p)<=0: lower.pop()
        lower.append(p)
    upper=[]
    for p in reversed(points):
        while len(upper)>1 and cross(upper[-2],upper[-1],p)<=0: upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]


def area(poly):
    return abs(sum(poly[i][0]*poly[(i+1)%len(poly)][1]-poly[i][1]*poly[(i+1)%len(poly)][0]
                   for i in range(len(poly))))/2


def scale(poly,s): return [(s*x,s*y)for x,y in poly]


def clip(poly,u):
    out=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        a=sum(x*y for x,y in zip(p,u)); b=sum(x*y for x,y in zip(q,u))
        if a>=0: out.append(p)
        if (a<0<b) or (b<0<a):
            t=a/(a-b)
            out.append(tuple(p[i]+t*(q[i]-p[i])for i in range(2)))
    return out


def midpoint(a,b): return hull([((x+u)/2,(y+v)/2)for x,y in a for u,v in b])


def main():
    square=list(map(lambda p:tuple(map(Q,p)),[(-1,-1),(1,-1),(1,1),(-1,1)]))
    diamond=list(map(lambda p:tuple(map(Q,p)),[(0,-2),(2,0),(0,2),(-2,0)]))
    middle=midpoint(square,diamond)
    assert list(map(area,[square,middle,diamond])) == [Q(4),Q(7),Q(8)]
    eps=Q(64,831); delta=Q(1,4); kappa=(1-delta)*delta
    lam=Q(277,283); factors=[lam,Q(293,283),lam]
    assert lam*(1+eps*(1-delta))==factors[1]
    final=[scale(p,s)for p,s in zip([square,middle,diamond],factors)]
    assert sum(map(area,final))==19
    assert lam*eps*kappa==Q(4,283)
    assert factors[1]-lam==Q(16,283)
    assert Q(1,566)<min(Q(4,283)/4,lam/2)
    for u in [(Q(1),Q(0)),(Q(0),Q(1)),(Q(3,5),Q(4,5)),(Q(-5,13),Q(12,13))]:
        assert all(area(clip(p,u))==area(p)/2 for p in [square,middle,diamond]+final)
        assert sum(area(clip(p,u))for p in final)==Q(19,2)
    triangle=list(map(lambda p:tuple(map(Q,p)),[(-2,-1),(2,-1),(0,2)]))
    middle=midpoint(square,triangle)
    assert list(map(area,[square,middle,triangle]))==[Q(4),Q(6),Q(6)]
    eps=Q(12,43); delta=Q(1,6); kappa=(1-delta)*delta
    lam=Q(43,47); factors=[lam,Q(53,47),lam]
    assert lam*(1+eps*(1-delta))==factors[1]
    original=[square,middle,triangle]
    final=[scale(p,s)for p,s in zip(original,factors)]
    assert sum(map(area,final))==16
    assert lam*eps*kappa==Q(5,141)
    assert factors[1]-lam==Q(10,47)
    assert Q(1,200)<min(Q(5,141)/4,lam/2)
    assert all(area(clip(p,(1,0)))==area(p)/2 for p in original+final)
    assert sum(area(clip(p,(1,0)))for p in final)==8
    assert [area(clip(p,(0,1)))/area(p)for p in original]==[Q(1,2),Q(1,2),Q(4,9)]
    assert sum(area(clip(p,(0,1)))for p in original)==Q(23,3)
    assert sum(area(clip(p,(0,1)))for p in final)==Q(23,3)+Q(120,2209)
    # All extreme excluded-target representations on a complete 5-point interval.
    P=list(range(-2,3)); layer={z:2-abs(z)for z in P}
    reps=[]
    for z in P[1:-1]:
        for left in P:
            for right in P:
                if left<z<right:
                    a=Q(right-z,right-left)
                    reps.append((z,{left:a,right:1-a}))
    alpha=min(v for _,rep in reps for v in rep.values())
    assert alpha==Q(1,4)
    delta=alpha/6; kappa=(1-delta)*delta**2
    assert delta==Q(1,24) and kappa==Q(23,13824)
    barriers={z:1-delta**layer[z]for z in P}
    checks=0
    for z,rep in reps:
        assert any(layer[p]<layer[z]for p in rep)
        ell=layer[z]
        assert delta*(1-delta**(ell-1))+(1-delta)*(1-delta**2)==barriers[z]-kappa
        for u in [(Q(1),Q(0)),(Q(3,5),Q(4,5)),(Q(5,13),Q(12,13))]:
            h={p:abs(u[0])+abs(u[1])+(4-p*p)*max(map(abs,u))for p in P}
            assert all(1<=h[p]<=6 for p in P)
            H=sum(a*h[p]for p,a in rep.items())
            assert any(layer[p]<ell and a*h[p]/H>=delta for p,a in rep.items())
            assert sum(a*h[p]*barriers[p]/H for p,a in rep.items())<=barriers[z]-kappa
            original_gap=h[z]-H
            assert original_gap>=0
            gap=barriers[z]*h[z]-sum(a*barriers[p]*h[p]for p,a in rep.items())
            assert gap>=barriers[z]*original_gap+kappa
            for self_weight in [Q(1,3),Q(9,10),Q(99,100)]:
                augmented_gap=h[z]-(self_weight*h[z]+(1-self_weight)*H)
                assert augmented_gap==(1-self_weight)*original_gap
            checks+=1
    print(f"PASS: two rational nonhomothetic normalized families, exact cap budgets, "
          f"and {checks} multi-layer representation/barrier checks.")


if __name__=='__main__': main()
