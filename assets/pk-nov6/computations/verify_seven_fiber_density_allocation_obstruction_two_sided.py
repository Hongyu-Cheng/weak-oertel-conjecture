from submission_text import read_submission
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import ast
import re
import sympy as sp

checks=0
def check(value):
    global checks
    assert value
    checks+=1

source=read_submission('b04c74715df6cea2')
x,t=sp.symbols('x t')
cells=[
    ('I',sp.Rational(9,25),sp.Rational(9,16),16*x/9),
    ('II',sp.Rational(9,16),sp.Rational(13,16),4*x-sp.Rational(5,4)),
    ('III',sp.Rational(13,16),sp.Rational(7,8),16*x-11),
]
for name,lo,hi,ell in cells:
    block=source.split(f'Cell {name}:',1)[1].split('Cell ',1)[0].split('These are polynomial',1)[0]
    arrays={}
    for label in ['c','p']:
        arrays[label]=ast.literal_eval(re.search(rf'\b{label} = (\[[\s\d,]+\])',block).group(1))
    denC=int(re.search(r'D_C = (\d+)',block).group(1))
    denP=int(re.search(r'D_P = (\d+)',block).group(1))
    J=x+8*ell/27
    R=x+4*ell/9-sp.Rational(4,25)
    C=sp.expand(ell*J*J-R**3-sp.Rational(64,15625))
    PP=sp.expand(15625*C*C-256*R**3)
    for poly,nums,den,degree in [(C,arrays['c'],denC,3),(PP,arrays['p'],denP,6)]:
        check(len(nums)==degree+1)
        check(den>0)
        for num in nums: check(num>0)
        bern=sum(sp.Rational(nums[i],den)*sp.binomial(degree,i)*t**i*(1-t)**(degree-i) for i in range(degree+1))
        check(sp.expand(poly.subs(x,lo+(hi-lo)*t)-bern)==0)
    # All band and sign conditions are affine and checked at BOTH endpoints.
    for at in [lo,hi]:
        lv=ell.subs(x,at)
        check(lv>0)
        check(J.subs(x,at)>0)
        check(R.subs(x,at)>0)
        check(sp.Rational(4,25)<=lv*sp.Rational(4,9))
        check(at-sp.Rational(4,25)<=lv*sp.Rational(5,9))
        check(at>=sp.Rational(4,25))

gamma=F(4,9)
areas={z:(1-F(abs(z),4))**2 for z in range(-3,4)}
check(sum(areas.values())==F(11,4))
check(gamma*sum(areas.values())/2==F(11,18))
check(F(4,9)+F(4,25)==F(136,225))
check(F(11,18)-F(136,225)==F(1,150))
check(gamma*(1+F(9,25))==F(136,225))
check(3*gamma*F(9,16)==F(3,4))
check(F(3,4)-F(11,18)==F(5,36))

for p in range(-3,4):
    pairs=[(z,2*p-z) for z in areas if z<2*p-z and 2*p-z in areas]
    if p==0:
        check(pairs==[(-3,3),(-2,2),(-1,1)])
        check(sorted([areas[z] for z,w in pairs],reverse=True)==[F(9,16),F(1,4),F(1,16)])
    else:
        maximum=areas[p]+sum(min(areas[z],areas[w]) for z,w in pairs)
        check(maximum==sum(areas[j] for j in range(abs(p),4)))
        check(gamma*maximum<=F(7,18)<F(11,18))

# Independently inspect all vertices of the central allocation cube and
# rational lines within it; the universal proof is the exact knapsack
# argument plus the Bernstein identities, not this finite calibration.
B=[F(9,16),F(1,4),F(1,16)]
for e in product([F(j,8) for j in range(9)],repeat=3):
    alpha=sum(ej*bj for ej,bj in zip(e,B))
    L=sum(e)
    if alpha<=F(9,16): lmin=16*alpha/9
    elif alpha<=F(13,16): lmin=4*alpha-F(5,4)
    else: lmin=16*alpha-11
    check(0<=alpha<=F(7,8))
    check(alpha<=L)
    check(L>=lmin)

# Actual rational fibers and their midpoint compatibility.
tri=[(F(-2,3),F(-1,3)),(F(4,3),F(-1,3)),(F(-2,3),F(2,3))]
apex=tri[2]
fiber={z:[((1-F(abs(z),4))*v[0]+F(abs(z),4)*apex[0],
           (1-F(abs(z),4))*v[1]+F(abs(z),4)*apex[1]) for v in tri] for z in areas}
def area(poly):
    return abs(sum(poly[i][0]*poly[(i+1)%len(poly)][1]-poly[i][1]*poly[(i+1)%len(poly)][0] for i in range(len(poly))))/2
def inside_tri(point,poly):
    return all((poly[(i+1)%3][0]-poly[i][0])*(point[1]-poly[i][1])-(poly[(i+1)%3][1]-poly[i][1])*(point[0]-poly[i][0])>=0 for i in range(3))
for z,poly in fiber.items():
    check(area(poly)==areas[z])
    check(tuple(sum(v[i] for v in poly)/3 for i in range(2))==tuple(F(abs(z),4)*u for u in apex))
for z,w in product(areas,repeat=2):
    if (z+w)%2: continue
    for v,q in product(fiber[z],fiber[w]):
        check(inside_tri(tuple((v[i]+q[i])/2 for i in range(2)),fiber[(z+w)//2]))

# Binary padding supplies no extra reflected pair at any actual anchor.
for n in range(1,6):
    binary=list(product([0,1],repeat=n-1))
    for e,f,g in product(binary,repeat=3):
        if all(e[i]+f[i]==2*g[i] for i in range(n-1)):
            check(e==f==g)
    check(gamma*(2**(n-1)*F(11,4))/2**n==F(11,18))

print(f'{checks} exact checks PASS')
