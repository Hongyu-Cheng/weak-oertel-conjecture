"""Exact polygon/cap certificate; disproves the arbitrary-finite-base target only."""
from fractions import Fraction as F

A = [(F(1,100),F(1,100)), (F(27,100),F(1,100)),
     (F(27,100),F(26,100)), (F(1,100),F(26,100))]
B = [(F(0),F(0)),(F(1),F(0)),(F(0),F(1))]
D = [(F(0),F(0)),(F(21,20),F(0)),(F(0),F(21,20))]
t = F(1,100)
fibers = [(F(0), A), (t, B), (F(1), D)]

def area(poly):
    if not poly:
        return F(0)
    return abs(sum(poly[i][0]*poly[(i+1)%len(poly)][1]
                   -poly[i][1]*poly[(i+1)%len(poly)][0]
                   for i in range(len(poly))))/2

def clip(poly,z,cap):
    az,ax,ay,b = cap
    def margin(p):
        return az*z+ax*p[0]+ay*p[1]-b
    out=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        mp,mq=margin(p),margin(q)
        if mp>=0:
            out.append(p)
        if (mp<0<mq) or (mq<0<mp):
            f=mp/(mp-mq)
            out.append((p[0]+f*(q[0]-p[0]),p[1]+f*(q[1]-p[1])))
    return out

def mass(cap):
    return sum(area(clip(poly,z,cap)) for z,poly in fibers)

# az*z+ax*x+ay*y>=b. All entries and operations stay rational.
central = [(-F(2),-F(1),-F(1),-F(3,5)-2*t),
           (-F(2),F(1),F(0),F(3,10)-2*t),
           (-F(2),F(0),F(1),F(3,10)-2*t)]
left = [(-F(100),F(1),F(0),F(7,50)),
        (-F(100),-F(1),F(0),-F(7,50))]
right = [(F(2),-F(1),-F(1),2-F(7,10)),
         (F(2),F(1),F(0),2+F(7,20)),
         (F(2),F(0),F(1),2+F(7,20))]

for ap in A:
    for dp in D:
        p=tuple((1-t)*a+t*d for a,d in zip(ap,dp))
        assert p[0]>0 and p[1]>0 and sum(p)<1
assert max(sum((1-t)*a+t*d for a,d in zip(ap,dp))
           for ap in A for dp in D)==F(669,1250)

Q=F(49,200)
M=sum(area(poly) for z,poly in fibers)
assert [area(poly) for z,poly in fibers]==[F(13,200),F(1,2),F(441,800)]
assert M==F(893,800)

for z, group, expected in [(F(0),left,F(13,400)),
                           (t,central,Q),(F(1),right,Q)]:
    # The margins sum identically to zero on this entire anchor plane.
    assert sum(cap[1] for cap in group)==0
    assert sum(cap[2] for cap in group)==0
    assert sum(cap[0]*z-cap[3] for cap in group)==0
    for cap in group:
        assert mass(cap)==expected, (cap,mass(cap),expected)

Gamma=F(4,9)
assert Gamma*area(D)==Q
assert Q/M==F(196,893)
assert Gamma/2-Q/M==F(22,8037)>0
# Exact OC-safe source on consecutive integer bases and its projective map.
scales=[F(198),F(100),F(2)]
source_mass=sum(scale*scale*area(poly) for scale,(_,poly) in zip(scales,fibers))
assert source_mass==F(1510093,200)<F(10000)
for original_z,scale,(image_z,_) in zip([F(0),F(1),F(2)],scales,fibers):
    assert 198-98*original_z==scale>0
    assert original_z/scale==image_z
print("PASS: actual middle section, all 8 cap masses and full-plane covers")
print("PASS: OC-safe consecutive-integer source and exact projective image")
print("Exact finite-base maximum depth: 196/893; target gap: 22/8037")
print("Not an OC counterexample: omitted positive integer fibers after rescaling")
