"""Exact 9-cap certificate for a non-lattice-complete finite base."""
from fractions import Fraction as F

t=F(1,100)
T=[(F(0),F(0)),(F(1),F(0)),(F(0),F(1))]
radii=[F(5,19),F(1),F(39,38)]
bases=[F(0),t,F(1)]
fibers=[(z,[(r*x,r*y) for x,y in T]) for z,r in zip(bases,radii)]

def area(poly):
    if not poly:return F(0)
    return abs(sum(poly[i][0]*poly[(i+1)%len(poly)][1]
                  -poly[i][1]*poly[(i+1)%len(poly)][0]
                  for i in range(len(poly))))/2

def clip(poly,z,cap):
    az,ax,ay,b=cap
    def value(p):return az*z+ax*p[0]+ay*p[1]-b
    out=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        v,w=value(p),value(q)
        if v>=0:out.append(p)
        if (v<0<w) or (w<0<v):
            s=v/(v-w)
            out.append(tuple(a+s*(b-a) for a,b in zip(p,q)))
    return out

def mass(cap):return sum(area(clip(poly,z,cap)) for z,poly in fibers)

central=[(-F(2),-F(1),-F(1),-F(12,19)-2*t),
         (-F(2),F(1),F(0),F(6,19)-2*t),
         (-F(2),F(0),F(1),F(6,19)-2*t)]
left=[(-F(100),-F(1),-F(1),-F(10,57)),
      (-F(100),F(1),F(0),F(5,57)),
      (-F(100),F(0),F(1),F(5,57))]
right=[(F(2),-F(1),-F(1),2-F(13,19)),
       (F(2),F(1),F(0),2+F(13,38)),
       (F(2),F(0),F(1),2+F(13,38))]

assert (1-t)*radii[0]+t*radii[2]==F(1029,3800)<1
assert (radii[1]-radii[0])/t==F(1400,19)
assert (radii[2]-radii[1])/(1-t)==F(50,1881)>0
Q=F(169,722)
M=sum(area(poly) for z,poly in fibers)
assert M==F(3065,2888)
for z,group,expected in [(F(0),left,F(50,3249)),(t,central,Q),(F(1),right,Q)]:
    assert sum(cap[1] for cap in group)==0
    assert sum(cap[2] for cap in group)==0
    assert sum(cap[0]*z-cap[3] for cap in group)==0
    for cap in group:assert mass(cap)==expected,(cap,mass(cap))
assert F(4,9)*area(fibers[-1][1])==Q
assert Q/M==F(676,3065)
assert F(2,9)-Q/M==F(46,27585)>0
print("PASS: 9 exact cap masses and plane covers; actual concave homothetic fibers")
print("Exact finite-base maximum: 676/3065; target gap: 46/27585")
print("Not an OC counterexample: the finite sampling base is not lattice-complete")
