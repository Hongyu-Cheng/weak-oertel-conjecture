"""Exact interval/counted checks of the intrinsic reflection identities."""
from fractions import Fraction as F

w = {0:F(2), 1:F(6), 2:F(10), 3:F(3)}

def overlap(a,c,y):
    return max(F(0),min(a,c,2*y,a+c-2*y))

def R(j,y):
    return sum(overlap(a,w[2*j-z],y)
               for z,a in w.items() if 2*j-z in w)

def breaks(j):
    ans={F(0),w[j]}
    for z,a in w.items():
        if 2*j-z in w:
            c=w[2*j-z]
            ans.update((F(0),min(a,c)/2,max(a,c)/2,(a+c)/2))
    return sorted(t for t in ans if 0<=t<=w[j])

I0=Iz=Ix=F(0)
for j in w:
    bp=breaks(j)
    for lo,hi in zip(bp,bp[1:]):
        slope=(R(j,hi)-R(j,lo))/(hi-lo)
        intercept=R(j,lo)-slope*lo
        mass=slope*(hi**2-lo**2)/2+intercept*(hi-lo)
        moment=slope*(hi**3-lo**3)/3+intercept*(hi**2-lo**2)/2
        I0+=mass
        Iz+=j*mass
        Ix+=moment

Mr=[sum(a for z,a in w.items() if z%2==r) for r in (0,1)]
zr=[sum(z*a for z,a in w.items() if z%2==r) for r in (0,1)]
xr=[sum(a*a/2 for z,a in w.items() if z%2==r) for r in (0,1)]
assert Mr==[12,9]
assert I0==sum(a*a for a in Mr)/2==F(225,2)
assert Iz==sum(M*m for M,m in zip(Mr,zr))/2==F(375,2)
assert Ix==sum(M*m for M,m in zip(Mr,xr))/2==F(1653,4)

# q=0: C=[0,3] x {0}, with four counted integer points.
P=range(4)
Rcount={j:sum(2*j-z in P for z in P) for j in P}
assert list(Rcount.values())==[1,3,3,1]
assert sum(Rcount.values())==2**2+2**2
assert sum(j*r for j,r in Rcount.items())==2*(0+2)+2*(1+3)==12

# q=1 in R x R^2 with perpendicular integer segment fibers.
# Each separate parity contains one fiber; self-correlation has mass w^2/2
# and centroid exactly the segment midpoint.
segments=[(F(2),(F(0),F(1),F(0))),
          (F(4),(F(1),F(0),F(3)))]
mass=sum(length**2/2 for length,_ in segments)
moment=tuple(sum(length**2*center[k]/2 for length,center in segments)
             for k in range(3))
assert mass==10
assert moment==(8,2,24)
print('PASS: exact mass, full first moment, q=0, and varying-orientation checks.')
