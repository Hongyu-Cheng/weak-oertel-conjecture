"""Exact arithmetic checks for affine-selector region obstruction."""
from fractions import Fraction as F

L=F(257,2)
indices=list(range(10))
lengths=[L-j*j for j in indices]
assert all(length>0 for length in lengths)
assert sum(lengths)==1000
assert sum(lengths[:4])==500
assert sum(lengths[4:])==500
assert max(lengths)/sum(lengths)==F(257,2000)<F(1,2)

def center(z):return 130*z-382

for j in indices:
    lower,upper=F(j*j),L
    p_low,p_high=center(j)-F(1,2),center(j)+F(1,2)
    if j<=3:
        assert p_high<lower
        # Inward selector center is forced to the lower endpoint.
        assert lower>center(j)+F(1,2)
    else:
        assert upper<p_low
        assert upper<center(j)-F(1,2)

assert (center(3)-F(1,2),center(3)+F(1,2))==(F(15,2),F(17,2))
assert center(4)-F(1,2)==F(275,2)>L

for a in range(4):
    for b in range(a+1,4):
        for z in range(4,10):
            secant=(a+b)*z-a*b
            assert secant<=5*z-6<=39<L

# The maximum of consecutive secant affine functions interpolates z^2.
for z in indices:
    lower=max((2*j+1)*z-j*(j+1) for j in range(9))
    assert lower==z*z

# P inequalities x-130z<=-763/2 and -x+130z<=765/2.
# Equal positive multipliers cancel both continuous and integer normals.
assert F(-763,2)+F(765,2)==1>0

def lambdas(z1,z2,x):
    return [F(5-3*z1-3*z2-x,6),
            F(3*z1-3*z2+x+1,6),
            F(-3*z1+3*z2+x+1,6),
            F(3*z1+3*z2-x-1,6)]

tetra_vertices=[(0,0,-1),(1,0,2),(0,1,2),(1,1,-1)]
for index,vertex in enumerate(tetra_vertices):
    values=lambdas(*vertex)
    assert values==[F(int(index==j)) for j in range(4)]

for z1,z2,cap_index in [(0,0,3),(1,0,2),(0,1,1),(1,1,0)]:
    # Each barycentric coordinate is affine in x; endpoint checks suffice.
    for x in [0,1]:
        values=lambdas(z1,z2,x)
        assert sum(values)==1
        assert values[cap_index]<0
        assert all(value>0 for j,value in enumerate(values) if j!=cap_index)

print("PASS: exact cap masses, circuit term, region obstruction, and exterior-center obstruction")
