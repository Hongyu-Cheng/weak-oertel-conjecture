#!/usr/bin/env python3
"""Independent exact polygon clipping audit of the projected-count example."""
from fractions import Fraction as F

count = 0


def check(x):
    global count
    assert x
    count += 1


def area(poly):
    if len(poly) < 3:
        return F(0)
    return abs(sum(a[0]*b[1]-a[1]*b[0]
                   for a,b in zip(poly,poly[1:]+poly[:1])))/2


def clip(poly, normal, threshold):
    def margin(p):
        return sum(x*y for x,y in zip(normal,p))-threshold
    out = []
    for p,q in zip(poly,poly[1:]+poly[:1]):
        mp,mq = margin(p),margin(q)
        if mp >= 0:
            out.append(p)
        if (mp < 0 < mq) or (mq < 0 < mp):
            t = mp/(mp-mq)
            out.append(tuple((1-t)*x+t*y for x,y in zip(p,q)))
    return out


b,c,gamma = F(1,3),F(2,3),F(4,9)
T = [(F(0),F(0)),(F(1),F(0)),(F(0),F(1))]
V = area(T)
for eps in (F(1,100),F(1,137),F(3,1000),F(7,10000)):
    E = [(F(0),F(0)),(b+eps,b),(b,b+eps)]
    e = eps*(c+eps)
    check(area(E)/V == e)
    check(all(x>=0 and y>=0 and x+y<=1 for x,y in E))
    for N in (3,4,5,8,21,100):
        theta = e/(4*N)
        p = (b-theta,b-theta)
        q1,q2 = p[0]/(c+eps),p[1]/(c+eps)
        check(q1>0 and q2>0 and q1+q2<1)
        check(tuple(q1*E[1][i]+q2*E[2][i] for i in range(2)) == p)
        cuts = [((-F(1),-F(1)),-c+2*theta),
                ((F(1),F(0)),b-theta),
                ((F(0),F(1)),b-theta)]
        formulas = [N*(c-2*theta)**2+e*((c-2*theta)/(c+eps))**2,
                    N*(c+theta)**2+e*(1-(b-theta)**2/(b*(b+eps)))]
        for i,(normal,threshold) in enumerate(cuts):
            check(sum(x*y for x,y in zip(normal,p)) == threshold)
            ta,ea = area(clip(T,normal,threshold)),area(clip(E,normal,threshold))
            check(0<ta<V and 0<ea<area(E))
            budget = (N*ta+ea)/V
            check(budget == formulas[0 if i==0 else 1])
            check(budget <= gamma*(N+e)-F(4447,57600)*e)
        check((b+2*theta)+2*(b-theta)==1)
        if N%2:
            k=(N-1)//2
            for sign in (-1,0,1):
                check(sum(sign*(z-k)>=0 for z in range(N)) >= k+1)
            check(gamma*(k+1)/(N+e)>gamma/2)

print(f"PASS {count} independent exact polygon/source checks")
