"""Exact supplementary checks for the base Gaussian localization note.

The analytic posterior and martingale claims are proved in the source.
Here every actual interval cap is integrated exactly, all slope cells
are exhausted, and the finite rational counterposterior is checked.
"""
from fractions import Fraction as F
from itertools import product

checks = 0

def tail(threshold):
    return min(F(1), max(F(0), (1-threshold)/2))

def middle_one_orientation(p, y):
    # Cap X+a z>=y. Breakpoints are precisely endpoint support contacts.
    slopes = {y-1, y+1, -y-1, -y+1}
    slopes |= {min(slopes)-1, max(slopes)+1}
    return min(p[0]*tail(y+a) + p[1]*tail(y) + p[2]*tail(y-a)
               for a in slopes)

def middle_depth(p,y):
    return min(middle_one_orientation(p,y),
               middle_one_orientation(p,-y),
               p[1]+min(p[0],p[2]))

def formula(p):
    return max(p[0]/2,p[2]/2,p[1]/2+min(p[0],p[2]))

for i in range(1,24):
    for j in range(1,24-i):
        p=(F(i,24),F(j,24),F(24-i-j,24))
        mid=p[1]/2+min(p[0],p[2])
        assert middle_depth(p,F(0))==mid
        checks+=1
        for yy in range(-9,10):
            y=F(yy,10)
            assert middle_depth(p,y)<=mid
            checks+=1
        R=p[0]+p[2]
        D=p[2]-p[0]
        assert formula(p)==F(1,2)-abs(D)/2+max(R+3*abs(D)-2,F(0))/4
        assert formula(p)<=F(1,2)
        assert (formula(p)==F(1,2)) == (p[0]==p[2])
        checks+=3

prior=(F(1,3),)*3
assert formula(prior)==F(1,2)
assert prior[2]/2==F(1,6)<F(1,4)
counter=(F(1,81),F(16,81),F(64,81))
assert middle_depth(counter,F(0))==F(1,9)
assert counter[0]/2==F(1,162)
assert formula(counter)==counter[2]/2==F(32,81)>F(1,4)
# e^a=8, e^(-t/2)=1/2, so the unnormalized weights are 1/16,1,4.
raw=(F(1,16),F(1),F(4))
assert tuple(x/sum(raw) for x in raw)==counter
checks+=6

# Verify the finite generator cancellation for arbitrary fixed fiber
# statistics, without evaluating an exponential or using floating point.
z=(-1,0,1)
for p in [(F(1,3),)*3,counter,(F(1,9),F(4,9),F(4,9))]:
    mean=sum(p[i]*z[i] for i in range(3))
    ez2=sum(p[i]*z[i]**2 for i in range(3))
    for g in product((F(0),F(1,3),F(1)),repeat=3):
        G=sum(p[i]*g[i] for i in range(3))
        grad=sum(p[i]*(g[i]-G)*(z[i]-mean) for i in range(3))
        dt=-sum(p[i]*(g[i]-G)*(z[i]**2-ez2) for i in range(3))/2
        hess=sum(p[i]*(g[i]-G)*(z[i]-mean)**2 for i in range(3))
        assert dt+mean*grad+hess/2==0
        checks+=1

# Exact closest-point parity calibration on a complete two-dimensional box.
P=list(product(range(-2,3),repeat=2))
for ci,cj in product(range(-11,12),repeat=2):
    c=(F(ci,4),F(cj,4))
    dist={v:sum((F(v[j])-c[j])**2 for j in range(2)) for v in P}
    dmin=min(dist.values())
    near=[v for v in P if dist[v]==dmin]
    assert len({(v[0]%2,v[1]%2) for v in near})==len(near)<=4
    checks+=1

print(f'{checks} exact checks PASS; all interval slope cells and rational posterior retained')
