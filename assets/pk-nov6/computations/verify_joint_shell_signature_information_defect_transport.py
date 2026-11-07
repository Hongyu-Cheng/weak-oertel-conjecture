"""Exact actual cone-signature law and all eight retained-source minima."""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict

checks = 0
def require(value):
    global checks
    assert value
    checks += 1

theta = (F(3,10),F(3,10),F(2,5))
alpha = (F(35),F(35),F(8))
actual_tilted = ((0,0,0),(1,1,1),(1,1,1))
normals = ((1,1),(-1,1),(0,-1))

def bits(x,y):
    return tuple(int(nx*x+ny*y>0) for nx,ny in normals)

# Each face has probability1/4 and its free coordinate is uniform[-1,1].
# Split at all actual source and target cap zeros before using midpoints.
law = defaultdict(F)
cyl_losses = [F(0)]*3
tilt_losses = [F(0)]*3
for fixed_coordinate in (0,1):
    for fixed_value in (-1,1):
        faces = []
        if fixed_coordinate == 0:
            x_aff, y_aff = (F(0),F(fixed_value)),(F(1),F(0))
        else:
            x_aff, y_aff = (F(1),F(0)),(F(0),F(fixed_value))
        cuts = {F(-1),F(1)}
        for sx,sy in ((F(5,2),F(7,4)),(F(2),F(3,2)),(F(1),F(1))):
            for nx,ny in normals:
                slope=nx*sx*x_aff[0]+ny*sy*y_aff[0]
                offset=nx*sx*x_aff[1]+ny*sy*y_aff[1]
                if slope and -1 < -offset/slope < 1:
                    cuts.add(-offset/slope)
        cuts = sorted(cuts)
        for lo,hi in zip(cuts,cuts[1:]):
            t=(lo+hi)/2
            xx=x_aff[0]*t+x_aff[1]
            yy=y_aff[0]*t+y_aff[1]
            weight=(hi-lo)/8
            target1=bits(F(5,2)*xx,F(7,4)*yy)
            target2=bits(2*xx,F(3,2)*yy)
            source_b=bits(xx,yy)
            law[target1,target2] += weight
            for j in range(3):
                cyl_losses[j] += weight*(70*target1[j]+8*source_b[j])
                tilt_losses[j] += weight*43
require(sum(law.values()) == 1)
require(cyl_losses == [39]*3)
require(tilt_losses == [43]*3)
for j in range(3):
    require(sum(mass*x[j] for (x,y),mass in law.items()) == F(1,2))
    require(sum(mass*y[j] for (x,y),mass in law.items()) == F(1,2))
    require(sum(mass*x[j]*y[j] for (x,y),mass in law.items())
            == (F(79,160) if j<2 else F(1,2)))

all_bits=list(product((0,1),repeat=3))
expected={():F(1753,100),(0,):F(43,2),(1,):F(39),(2,):F(51,2),
          (0,1):F(39),(0,2):F(51,2),(1,2):F(43),(0,1,2):F(43)}
for retained,expect in expected.items():
    total=F(0)
    omitted=[i for i in range(3) if i not in retained]
    for (target1,target2),mass in law.items():
        costs=[]
        for choice in product(all_bits,repeat=len(omitted)):
            sources=[None]*3
            for i in retained:
                sources[i]=actual_tilted[i]
            for i,value in zip(omitted,choice):
                sources[i]=value
            if not all(target1[j]<=sources[0][j]+sources[1][j]
                       and target2[j]<=sources[0][j]+sources[2][j]
                       for j in range(3)):
                continue
            costs.append(sum(theta[j]*sum(alpha[i]*sources[i][j] for i in range(3))
                             for j in range(3)))
        require(bool(costs))
        total += mass*min(costs)
    require(total == expect)

# Actual geometry: concavity survives the stated one-sided interval.
eps=F(1,7)
require(all(value<=0 for value in (-1+5*eps,-1-5*eps,-1+4*eps)))
require(all(value<=0 for value in (-F(1,2)+F(7,2)*eps,
                                  -F(1,2)-F(7,2)*eps,
                                  -F(1,2)+F(5,2)*eps)))
require(F(67,2)-F(43,2)*(1-(1-eps)**2)>F(51,4))
require(F(43)>F(39)>F(1753,100))
print(f'PASS: {checks} exact joint-signature and retained-information checks; {len(law)} target atoms')
