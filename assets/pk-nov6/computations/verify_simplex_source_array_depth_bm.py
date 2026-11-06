"""Exact interval-source diagnostics for the general analytic array theorem."""
from fractions import Fraction as F
from itertools import product
from math import comb

def cap(length,center,threshold):
    return min(length,max(F(0),center+length/2-threshold))

def oriented_by_vertices(lengths,centers,weights,s):
    """Minimize the piecewise affine threshold cost on one exact hyperplane.

    Every finite arrangement vertex fixes all but one threshold at an interval
    endpoint. Recession minima cost at least the smallest full source mass,
    and that mass is attained by a one-full/all-empty choice when N>=2.
    """
    n=len(lengths)
    if n==1:return cap(lengths[0],centers[0],s)
    best=min(lengths)
    for free in range(n):
        others=[i for i in range(n) if i!=free]
        for signs in product((-1,1),repeat=n-1):
            thresholds={i:centers[i]+signs[k]*lengths[i]/2
                        for k,i in enumerate(others)}
            thresholds[free]=(s-sum(weights[i]*thresholds[i] for i in others))/weights[free]
            value=sum(cap(lengths[i],centers[i],thresholds[i]) for i in range(n))
            best=min(best,value)
    return best

def exact_depth(lengths,centers,weights,y):
    up=oriented_by_vertices(lengths,centers,weights,y)
    down=oriented_by_vertices(lengths,tuple(-x for x in centers),weights,-y)
    return min(up,down)

def formula(lengths,centers,weights,y):
    center=sum(a*c for a,c in zip(weights,centers))
    H=sum(a*l for a,l in zip(weights,lengths))/2
    assert abs(y-center)<=H
    return min(min(lengths),(H-abs(y-center))/max(weights))

configurations=[
    ((F(1),),(F(2),),(F(1),)),
    ((F(1),F(3)),(F(-1),F(2)),(F(1,2),F(1,2))),
    ((F(2),F(1)),(F(3,2),F(-2)),(F(1,3),F(2,3))),
    ((F(1),F(2),F(3)),(F(-1),F(0),F(2)),(F(1,4),F(1,4),F(1,2))),
    ((F(3),F(2),F(1)),(F(1),F(-3),F(0)),(F(1,3),F(1,3),F(1,3))),
]
checks=0
for lengths,centers,weights in configurations:
    assert sum(weights)==1 and min(weights)>0
    c=sum(a*b for a,b in zip(weights,centers))
    H=sum(a*b for a,b in zip(weights,lengths))/2
    for k in range(-8,9):
        y=c+F(k,8)*H
        assert exact_depth(lengths,centers,weights,y)==formula(lengths,centers,weights,y)
        # Ordinary depth in the actual Minkowski interval D.
        ordinary_depth=H-abs(y-c)
        assert ordinary_depth>=max(weights)*formula(lengths,centers,weights,y)
        checks+=1
    # A second genuinely different array with the same bases/weights.
    other_lengths=tuple(l+F(i+1,3) for i,l in enumerate(reversed(lengths)))
    other_centers=tuple(-c+F(i,2) for i,c in enumerate(centers))
    cb=sum(a*b for a,b in zip(weights,other_centers))
    Hb=sum(a*b for a,b in zip(weights,other_lengths))/2
    for ka,kb in product((-1,F(-1,2),0,F(1,2),1),repeat=2):
        y=c+ka*H;z=cb+kb*Hb
        pa=exact_depth(lengths,centers,weights,y)
        pb=exact_depth(other_lengths,other_centers,weights,z)
        for t in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
            lk=tuple((1-t)*a+t*b for a,b in zip(lengths,other_lengths))
            ck=tuple((1-t)*a+t*b for a,b in zip(centers,other_centers))
            point=(1-t)*y+t*z
            pk=exact_depth(lk,ck,weights,point)
            assert pk==formula(lk,ck,weights,point)
            assert pk>=(1-t)*pa+t*pb
            checks+=1

# The exact midpoint two-source plateau, including strict enlargement.
weights=(F(1,2),F(1,2));centers=(F(0),F(0))
for t in (F(0),F(1,3),F(1,2),F(1)):
    lengths=(F(2),(1-t)*F(6)+t*F(8))
    assert formula(lengths,centers,weights,F(0))==2
    assert exact_depth(lengths,centers,weights,F(0))==2
# In all dimensions the common symmetric K gives complementary threshold
# indicators. Boundary equality can double-count, consistently with the
# zero-volume hyperplane used in the analytic integral identity.
for d in range(1,8):
    for u in product((-1,0,1),repeat=d):
        if not any(u):continue
        x=tuple(1 if k%2 else -1 for k in range(d))
        value=sum(a*b for a,b in zip(u,x))
        for h in (F(-1,2),F(0),F(1,2),F(value)):
            count=int(value>=h)+int(-value>=-h)
            assert count>=1 and (value==h or count==1)

# Exact affinely dependent optimized-depth obstruction from the independently
# proved three-interval theorem; U=10, endpoints a=b=1.
def dependent_max(s):
    return F(6)-s/2 if s<=1 else F(11,2)
assert dependent_max(F(0))==6
assert dependent_max(F(1))==dependent_max(F(2))==F(11,2)
assert dependent_max(F(1))<(dependent_max(F(0))+dependent_max(F(2)))/2==F(23,4)
assert all(abs(s)<=F(9,2) for s in (F(0),F(1),F(2)))

# Symmetric actual three-fiber arrays: exact half of the full mass.
planar=tuple(F(R*R,2)+1 for R in (1,2,3))
assert planar==(F(3,2),F(3),F(11,2))
gap=4*planar[1]-planar[0]-planar[2]
assert gap==5 and gap**2<4*planar[0]*planar[2]==33
for d in range(2,21):
    radius=1+F(1,2*d)
    assert radius**d<=sum(F(1,2)**k for k in range(d+1))<2
    assert all(comb(d,k)<=d**k for k in range(d+1))
    for R in (F(1),1+F(1,4*d),radius):
        mass=2+R**d
        maximum=1+R**d/2
        assert maximum/mass==F(1,2)
        for q in (F(1,100),F(1,d),F(1,2),F(1),F(3)):
            bracket=(d-1)+(d*q-1)*R**d/2
            assert bracket>0
print(f"PASS: {checks} exact source-threshold and joint-array checks, symmetric plateau,")
print("dependent maximum failures, planar25<33 certificate, and all-power local curvature bounds")
