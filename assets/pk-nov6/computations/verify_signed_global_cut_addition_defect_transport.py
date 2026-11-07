from fractions import Fraction as F
from itertools import product
checks=0
# Product maxima of nonempty signed active sets: no auxiliary zero is inserted.
sets=[(F(-3),),(F(-2),F(-1)),(F(-1),F(2)),(F(0),F(3)),(F(1),F(2),F(4))]
for xs,ys,a,b in product(sets,sets,[F(0),F(1,3),F(2)],[F(0),F(2,5),F(3)]):
    assert max(a*x+b*y for x in xs for y in ys)==a*max(xs)+b*max(ys)
    checks+=1
# Complete baseline arrays for actual interval fibers of radii (1,2,1).
P=(-1,0,1)
h={-1:F(1),0:F(2),1:F(1)}
ell={-1:lambda z:F(1)+2*(z+1),0:lambda z:F(2),1:lambda z:F(1)-2*(z-1)}
for z in P:
    assert min(ell[q](z) for q in P)==h[z]
    for q in P:
        assert ell[q](z)>=h[z]
        assert (ell[q](z)==h[z])==(q==z)
        checks+=1
# Fields only on source-zero right-normal plane. New endpoints are exact minima.
t=F(1,10000)
for v1,v2,a,b in product([F(-2),F(-1,3),F(0),F(1),F(3)],repeat=4):
    if a<0 or b<0: continue
    v=a*v1+b*v2
    # Positive baseline weights independent of desired coefficients.
    for z in P:
        newright=min(F(2,5)*ell[q](z)+F(3,5)*ell[r](z)
                     -t*(a*(v1 if q==0 else 0)+b*(v2 if r==0 else 0))
                     for q in P for r in P)
        assert newright==h[z]-t*(v if z==0 else 0)
        checks+=1
# Signed speed addition does not add a fixed outside-support loss.
def support_loss(v): return min(v,F(0))
assert support_loss(F(1))+support_loss(F(-1))==-1
assert support_loss(F(1)+F(-1))==0
checks+=2
print(f'{checks} exact signed-cut/actual-interval checks PASS')
