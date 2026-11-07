"""Exact planar arithmetic; the note proves every dimension and direction."""
from fractions import Fraction as Q
from itertools import product

def area(poly):
    if len(poly) < 3:
        return Q(0)
    return abs(sum(x*v-y*u for (x,y),(u,v)
                   in zip(poly,poly[1:]+poly[:1])))/2

def clip(poly, u, v, c):
    out=[]
    if not poly:
        return out
    for P,R in zip(poly,poly[1:]+poly[:1]):
        a=u*P[0]+v*P[1]-c
        b=u*R[0]+v*R[1]-c
        if a>=0:
            out.append(P)
        if (a<0<b) or (b<0<a):
            t=a/(a-b)
            out.append((P[0]+t*(R[0]-P[0]),P[1]+t*(R[1]-P[1])))
    return out

T=[(Q(0),Q(0)),(Q(1),Q(0)),(Q(0),Q(1))]
V=Q(1,2); G=Q(4,9); g=(Q(1,3),Q(1,3)); h=Q(2,3)
core=[(0,0),(0,1),(1,0),(1,1)]
extra=[(-1,0),(-1,1),(1,-1)]
support=core+extra
assert sorted(support)==sorted((x,y) for x in range(-2,3) for y in range(-2,3)
                              if -1<=x<=1 and y<=1 and x+2*y>=-1)
for p,(u,v) in zip(extra,[(-2,-1),(-1,1),(1,-2)]):
    assert all(u*p[0]+v*p[1]>u*z[0]+v*z[1] for z in support if z!=p)

def source(scale, symmetric, rscale=None):
    A=([(g[0]+scale/2,g[1]),(g[0],g[1]+scale/2),
        (g[0]-scale/2,g[1]),(g[0],g[1]-scale/2)] if symmetric
       else [(g[0]+scale*(x-g[0]),g[1]+scale*(y-g[1])) for x,y in T])
    if rscale is None:
        R=A
    else:
        R=[(g[0]+rscale*(x-g[0]),g[1]+rscale*(y-g[1])) for x,y in T]
    S={z:T for z in core}
    S.update({extra[0]:R,extra[1]:A,extra[2]:A})
    return S,area(A),area(R)

def cap(S,u,v,b1,b2,c):
    return sum(area(clip(K,u,v,c-b1*z[0]-b2*z[1])) for z,K in S.items())

def barycap(S,i,b1,b2,threshold):
    u,v,k=[(-1,-1,1),(1,0,0),(0,1,0)][i]
    return cap(S,u,v,b1,b2,threshold-k)

checks=0
for symmetric in [False,True]:
    theta=Q(1) if symmetric else 2*G
    for scale in [Q(1,100),Q(1,80),Q(1,60)]:
        S,a,w=source(scale,symmetric)
        value=G*V+w+theta*a
        # A sufficient rational smallness certificate: rho_2>1/30.
        assert a<=V/30 and w+theta*a<=V/30
        for i in range(3):
            assert barycap(S,i,-h,-h,Q(1,3))==value
            # delta01=z1+2-2z2, delta10=1-z1+z2, delta11=2-z1-z2
            assert barycap(S,i,-2,4,Q(1,3)+4)==G*V+a
            assert barycap(S,i,2,-2,Q(1,3)+2)==G*V+a
            assert barycap(S,i,2,2,Q(1,3)+4)==G*V
            checks+=4
        coeffs=[Q(-2),Q(-1),-h,-Q(1,3),Q(0),Q(1,3),h,Q(1),Q(2)]
        normals=[(u,v) for u,v in product(range(-2,3),repeat=2) if u or v]
        for u,v in normals:
            c=u*g[0]+v*g[1]
            for b1,b2 in product(coeffs,repeat=2):
                assert cap(S,u,v,b1,b2,c)>=value
                checks+=1
        for b1,b2 in product(range(-2,3),repeat=2):
            if b1 or b2:
                assert cap(S,0,0,b1,b2,0)>=value
                checks+=1
        for x,y in [(Q(i,12),Q(j,12)) for i in range(13)
                    for j in range(13-i) if (i,j)!=(4,4)]:
            lam=[1-x-y,x,y]
            i=max(range(3),key=lambda k:lam[k])
            assert lam[i]>Q(1,3)
            assert barycap(S,i,-h,-h,lam[i])<value
            checks+=1

# Distinct owned masses on both sides of the simplex transition.
for scale in [Q(1,100),Q(1,80)]:
    for ratio in [Q(1,5),Q(1,2),Q(1),Q(2)]:
        S,a,w=source(scale,False,scale*ratio)
        qvalue=G*V+w+2*G*a
        globalvalue=G*V+max(a,w+2*G*a)
        assert qvalue<=globalvalue and w+2*G*a<V/30
        for i in range(3):
            assert barycap(S,i,-h,-h,Q(1,3))==qvalue
            assert barycap(S,i,-2,4,Q(1,3)+4)==G*V+a
            checks+=2

assert (Q(8)-3*G)/16-(Q(4)+5*G)/16==(1-2*G)/4>0
print(f"PASS {checks} exact coupled-cap, finite-cover, uniqueness, and transition checks")
