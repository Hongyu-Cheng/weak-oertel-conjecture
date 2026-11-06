"""Exact rational/polynomial certificates; numerical roots are not used."""
from fractions import Fraction as F
import sympy as sp

A, B = sp.symbols("A B")
Q = 61281*B**4 + 15298*B**3 - 8940*B**2 - 1944*B + 504
b_lo, b_hi = sp.Rational(1883682, 10**7), sp.Rational(1883684, 10**7)
assert Q.subs(B, b_lo) > 0 > Q.subs(B, b_hi)
assert 245124*F(1,5)**3 + 45894*F(1,5)**2 - 17880*F(9,50) - 1944 == -F(170706,125)
assert 3676860*F(9,50)**2 + 489358*F(9,50) - 138654 == F(8570088,125)
a_of_b = (1225620*B**3 + 244679*B**2 - 138654*B + 86268)/96110
al, ah = F(801411,10**6), F(801412,10**6)
bl, bh = F(188368,10**6), F(188369,10**6)
assert a_of_b.subs(B,b_lo) > sp.Rational(al.numerator,al.denominator)
assert a_of_b.subs(B,b_hi) < sp.Rational(ah.numerator,ah.denominator)
assert ah + bh < 1

points = [(x,y,z) for x in range(3) for y in range(5-2*x)
          for z in range(9-4*x-2*y)]
assert len(points) == 35
weight = lambda x,y,z: (1+A*(x-1)+B*(y-1))**2
moments = [sp.expand(sum((p[j]-1)*weight(*p) for p in points)) for j in range(3)]
expected = [
    -24*A**2+8*A*B+52*A-34*B**2-12*B-24,
    4*A**2-68*A*B-12*A+42*B**2+84*B,
    44*A**2+52*A*B-92*A+26*B**2-60*B+48,
]
assert moments == expected
assert sp.expand(moments[2] + 2*moments[0] + moments[1]) == 0
for polynomial in moments[:2]:
    numerator = sp.together(polynomial.subs(A,a_of_b)).as_numer_denom()[0]
    assert sp.rem(numerator,Q,B) == 0
mass = sp.expand(sum(weight(*p) for p in points))
cap = sp.expand(sum(weight(*p) for p in points if 5*(p[0]-1)+2*(p[1]-1)+4*(p[2]-1)>=0))
assert mass == 26*A**2-12*A*B-48*A+42*B**2+35
assert cap == 14*A**2+2*A*B-28*A+16*B**2-8*B+19
g = F(3125,7776)
terms = [(26*g-14,al*al,ah*ah),(-12*g-2,al*bl,ah*bh),
         (-48*g+28,al,ah),(42*g-16,bl*bl,bh*bh),
         (F(8),bl,bh),(35*g-19,F(1),F(1))]
lower = sum(c*(lo if c>=0 else hi) for c,lo,hi in terms)
assert lower == F(132828450791459,486000000000000) > 0

strip = [(x,y) for x in range(-2,3) for y in range(-3,4)
         if abs(F(y)-F(x,2)) <= F(3,5)]
assert strip == [(-2,-1),(-1,-1),(-1,0),(0,0),(1,0),(1,1),(2,1)]
assert all(sum(p[j] for p in strip)==0 for j in range(2))
assert [sum(p[0]==x for p in strip) for x in range(-2,3)] == [1,2,1,2,1]
assert [sum(p[0]>=x for p in strip) for x in range(-2,3)] == [7,6,4,3,1]

# A second exact parameter definition: an interior quartic minimum, d=3.
al, ah = F(6013366,10**7), F(6013370,10**7)
bl, bh = F(15061245,10**8), F(15061267,10**8)
assert ah+bh<1
weight3 = lambda x,y,z: (1+A*(x-1)+B*(y-1))**3
mom3 = [sp.expand(sum((p[j]-1)*weight3(*p) for p in points)) for j in range(3)]
assert sp.expand(mom3[2]+2*mom3[0]+mom3[1]) == 0
cross = -18*A**2+216*A*B+24*A-144*B**2-204*B-18
assert sp.diff(mom3[0],B)==cross==sp.diff(mom3[1],A)
cross_upper = (216*F(602,1000)*F(151,1000)+24*F(602,1000)
               -18*F(6,10)**2-144*F(15,100)**2-204*F(15,100)-18)
assert cross_upper == -F(1514823,62500)<0
rat = lambda x:sp.Rational(x.numerator,x.denominator)
values=[mom3[0].subs({A:rat(al),B:rat(bl)}),
        mom3[0].subs({A:rat(ah),B:rat(bh)}),
        mom3[1].subs({A:rat(al),B:rat(bl)}),
        mom3[1].subs({A:rat(ah),B:rat(bh)})]
assert values == [
    -sp.Rational(337514033207339,125000000000000000000),
    sp.Rational(13678807882229509,15625000000000000000000),
    -sp.Rational(4293268153408029,4000000000000000000000),
    sp.Rational(13222083910627821,4000000000000000000000),
]
assert values[0]<0<values[1] and values[2]<0<values[3]
mass3=sp.expand(sum(weight3(*p) for p in points))
cap3=sp.expand(sum(weight3(*p) for p in points if 5*(p[0]-1)+2*(p[1]-1)+4*(p[2]-1)>=0))
gap3=sp.Poly(sp.Rational(367,1000)*mass3-cap3,A,B)
lower3=F(0)
for (i,j),coefficient in gap3.terms():
    c=F(int(coefficient.p),int(coefficient.q))
    lower3+=c*((al**i*bl**j) if c>=0 else (ah**i*bh**j))
assert lower3==F(8681336352206248242879,4000000000000000000000000)>0
assert F(163,60)+F(7,4320)==F(11743,4320)<F(68,25)
assert F(367,1000)*F(68,25)<1
print("PASS: exact integer means, both closed-cap inequalities, and aggregation obstruction")
