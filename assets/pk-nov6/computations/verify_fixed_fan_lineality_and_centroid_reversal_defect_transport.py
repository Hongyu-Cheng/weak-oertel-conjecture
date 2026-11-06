"""Exact checks for the fixed-fan reversal refinement; no sampled proof."""
from fractions import Fraction as F
from itertools import combinations
import sympy as sp

checks = 0
def check(v):
    global checks
    assert v
    checks += 1

def moments(poly):
    cross = [x*v-u*y for (x,y),(u,v) in zip(poly,poly[1:]+poly[:1])]
    twice = sum(cross)
    area = abs(twice)/2
    gx = sum((poly[i][0]+poly[(i+1)%len(poly)][0])*c for i,c in enumerate(cross))/(3*twice)
    gy = sum((poly[i][1]+poly[(i+1)%len(poly)][1])*c for i,c in enumerate(cross))/(3*twice)
    return area, gx, gy

A = [(F(-1),F(0)),(F(1),F(0)),(F(1),F(-3)),(F(-1),F(-3))]
K = [(F(-2),F(0)),(F(2),F(0)),(F(2),F(-1)),(F(1),F(-3)),(F(-1),F(-3)),(F(-2),F(-1))]
check(moments(A)==(F(6),F(0),F(-3,2)))
check(moments(K)==(F(10),F(0),F(-4,3)))

P=(-1,0,1)
masses={-1:F(6),0:F(10),1:F(6)}
for j in range(1,3):
    for sub in combinations(P,j):
        closed=tuple(z for z in P if min(sub)<=z<=max(sub))==sub
        if closed:
            parity=len({z%2 for z in sub})
            check(sum(masses[z] for z in sub)<parity*F(22,2))

s=sp.symbols('s', nonnegative=True)
R=[(-2*(1+s),4*s/3),(2*(1+s),4*s/3),
   (2*(1+s),-1+s/2),(1+s,-3-3*s/2),
   (-1-s,-3-3*s/2),(-2*(1+s),-1+s/2)]
normals=[(0,1),(1,0),(2,-1),(0,-1),(-2,-1),(-1,0)]
def dot(n,v): return n[0]*v[0]+n[1]*v[1]
def nn_poly(p):
    p=sp.Poly(sp.expand(p),s)
    return all(c>=0 for c in p.all_coeffs())
for i,n in enumerate(normals):
    h=max(dot(n,v) for v in K)
    hd=max(dot(n,v) for v in [(F(0),F(-3,2)),(F(0),F(-4,3))])
    target=(1+s)*sp.Rational(h.numerator,h.denominator)-s*sp.Rational(hd.numerator,hd.denominator)
    # Edge i and all vertices: an exact support certificate for all s>=0.
    check(sp.expand(dot(n,R[i])-target)==0)
    check(sp.expand(dot(n,R[(i+1)%6])-target)==0)
    for v in R:
        check(nn_poly(target-dot(n,v)))

check(sp.expand((4*s/3)-(-1+s/2)-(1+5*s/6))==0)
check(sp.expand(4*s/3-3*s/2+s/6)==0)

# Exact finite reverse-radius formula for every row, tested on rational arrays.
for ah in [F(0),F(1,7),F(1),F(3)]:
    for ad in [F(0),F(1,5),F(1),F(4)]:
        if ad>ah:
            bound=ah/(ad-ah)
            check((1+bound)*ah-bound*ad==0)
            check((1+bound+F(1,13))*ah-(bound+F(1,13))*ad<0)
        else:
            check(ah-ad>=0)

# Individual reverse endpoint supports, and the pure anchored failure.
for rat in [F(0),F(1,100),F(1,6),F(1),F(7)]:
    ar=[(x*(1+rat),F(-3,2)+(y+F(3,2))*(1+rat)) for x,y in A]
    check(max(y for x,y in ar)==3*rat/2)
    check(min(y for x,y in ar)==-3-3*rat/2)
    check(moments(ar)[0]==6*(1+rat)**2)
    check(4*rat/3-max(y for x,y in ar)==-rat/6)

print(f'PASS: {checks} exact checks')
