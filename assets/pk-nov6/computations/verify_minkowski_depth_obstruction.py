from fractions import Fraction as F

A=[(F(0),F(12)),(F(-3),F(24)),(F(-1),F(28)),(F(6),F(32))]
B=[(F(0),F(21)),(F(-9),F(24)),(F(-3),F(21)),(F(7),F(14))]
C=[(a+c,b+d) for (a,b),(c,d) in zip(A,B)]

def compatibility(D):
    lower=[D[i+1][0]-D[i][0] for i in range(len(D)-1)]
    upper=[D[i+1][1]-D[i][1] for i in range(len(D)-1)]
    assert lower==sorted(lower)
    assert upper==sorted(upper,reverse=True)
    assert all(l<u for l,u in D)

def mass(D,slope,intercept,side=1):
    above=sum(max(F(0),min(u-l,u-intercept-slope*i)) for i,(l,u) in enumerate(D))
    return above if side==1 else sum(u-l for l,u in D)-above

def exact_depth(D,k,x):
    M=sum(u-l for l,u in D)
    # The cap mass is affine between consecutive endpoint-crossing slopes.
    slopes={(e-x)/(j-k) for j,I in enumerate(D) if j!=k for e in I}
    values=[]
    for a in slopes:
        t=mass(D,a,x-a*k)
        values.extend([t,M-t])
    # The two limits at infinite slope, in both orientations.
    left=sum(u-l for j,(l,u) in enumerate(D) if j<k)
    right=sum(u-l for j,(l,u) in enumerate(D) if j>k)
    above_self=D[k][1]-x
    for t in [left+above_self,right+above_self]:
        values.extend([t,M-t])
    # Actual vertical halfspaces include the entire candidate fiber.
    values.extend([left+D[k][1]-D[k][0],right+D[k][1]-D[k][0]])
    return min(values)/M

for D in [A,B,C]:compatibility(D)
assert exact_depth(A,2,F(14))==F(20,47)
assert exact_depth(B,1,F(33,4))==F(147,340)
assert exact_depth(C,1,F(18))==F(63,179)
assert F(63,179)<F(20,47)<F(147,340)
# Fixed caps cover each whole candidate fiber, certifying the global upper bound.
# Tuple = (fiber index, split x, low-cap slope, high-cap slope, expected mass).
covers=[(0,F(33,2),F(-100),F(100),F(33,2)),
        (1,F(18),F(-22),F(31),F(63)),
        (2,F(45,2),F(69,2),F(-51,2),F(119,2)),
        (3,F(59,2),F(100),F(-100),F(33,2))]
for k,x,alow,ahigh,m in covers:
    assert C[k][0]<=x<=C[k][1]
    assert mass(C,alow,x-alow*k,-1)==m
    assert mass(C,ahigh,x-ahigh*k,1)==m
    assert m<=63
# Unit central-volume convex combination.
Ac=[(l/27,u/27) for l,u in A]
Bc=[(l/33,u/33) for l,u in B]
assert Ac[1][1]-Ac[1][0]==Bc[1][1]-Bc[1][0]==1
for i in range(4):
    for j in range(2):
        assert F(27,60)*Ac[i][j]+F(33,60)*Bc[i][j]==C[i][j]/60
print('All rational Minkowski-depth obstruction checks passed.')
