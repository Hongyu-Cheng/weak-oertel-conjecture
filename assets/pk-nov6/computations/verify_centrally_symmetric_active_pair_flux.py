"""Exact rational certificate for the active balanced-pair flux example."""
from fractions import Fraction as F

def cross(o,a,b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])

def hull(points):
    points=sorted(set(points))
    lo=[]
    for p in points:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=0:lo.pop()
        lo.append(p)
    hi=[]
    for p in reversed(points):
        while len(hi)>=2 and cross(hi[-2],hi[-1],p)<=0:hi.pop()
        hi.append(p)
    return lo[:-1]+hi[:-1]

def area_centroid(poly):
    twice=F(0);mx=F(0);my=F(0)
    for a,b in zip(poly,poly[1:]+poly[:1]):
        c=a[0]*b[1]-a[1]*b[0]
        twice+=c;mx+=(a[0]+b[0])*c;my+=(a[1]+b[1])*c
    if twice==0:return F(0),None
    return twice/2,(mx/(3*twice),my/(3*twice))

def clip_right(poly,t):
    out=[]
    for a,b in zip(poly,poly[1:]+poly[:1]):
        ina=a[0]>=t;inb=b[0]>=t
        if ina:out.append(a)
        if ina!=inb:
            r=(t-a[0])/(b[0]-a[0])
            out.append((t,a[1]+r*(b[1]-a[1])))
    return out

def section_length(poly,t):
    vals=[]
    for a,b in zip(poly,poly[1:]+poly[:1]):
        if a[0]==t:vals.append(a[1])
        if (a[0]<t<b[0]) or (b[0]<t<a[0]):
            vals.append(a[1]+(t-a[0])*(b[1]-a[1])/(b[0]-a[0]))
    return max(vals)-min(vals)

K=[(F(-1),F(-1)),(F(9,4),F(0)),(F(-1),F(1))]
negK=hull([(-x,-y) for x,y in K])
B=hull([((x-u)/2,(y-v)/2) for x,y in K for u,v in K])
expected=[(F(-13,8),F(-1,2)),(F(0),F(-1)),
          (F(13,8),F(-1,2)),(F(13,8),F(1,2)),
          (F(0),F(1)),(F(-13,8),F(1,2))]
assert B==expected
w,g=area_centroid(K);b,gb=area_centroid(B)
assert (w,g)==(F(13,4),(F(1,12),F(0)))
assert (b,gb)==(F(39,8),(F(0),F(0)))
assert area_centroid(negK)==(w,(-g[0],F(0)))
M=2*w+b
assert M==F(91,8)
kp=area_centroid(clip_right(K,F(0)))[0]
km=area_centroid(clip_right(negK,F(0)))[0]
bp=area_centroid(clip_right(B,F(0)))[0]
assert kp==F(81,52) and kp/w==F(81,169)
assert km/w==F(88,169) and bp==b/2
assert kp+km+bp==M/2
J=g[0]*kp-g[0]*km
assert J==F(-7,624) and J/M==F(-1,1014)
assert -g[0]*km+g[0]*kp==J
assert section_length(K,F(0))==section_length(negK,F(0))==F(18,13)
assert section_length(B,F(0))==2
assert 2*F(18,13)+2==F(62,13)
for t in [F(-1),F(-1,2),F(0),F(1,2),F(1)]:
    assert section_length(K,t)==(18-8*t)/13
    assert section_length(negK,t)==(18+8*t)/13
    assert section_length(B,t)==2-8*abs(t)/13
    pp=area_centroid(clip_right(K,t))[0]/w
    pm=area_centroid(clip_right(negK,t))[0]/w
    assert pp==(9-4*t)**2/169
    assert pm==1-(9+4*t)**2/169
    assert w*g[0]*(pp-pm)==(32*t*t-7)/624
assert F(-16,62)==F(-8,31)
print('PASS: M=',M,'; both active fluxes=',J,'; normalized=',J/M)
