"""Exact independent certificates; the all-dimensional proof is in the audit."""
from fractions import Fraction as F
from itertools import product
import sympy as s
checks=0
def ck(x):
 global checks
 assert x
 checks+=1

for d in range(2,13):
 m=d+1
 outer=[tuple([-1]*d)]+[tuple(int(i==j) for j in range(d)) for i in range(d)]
 zero=(0,)*d;P=[zero]+outer
 ell=lambda z:[-sum(z)]+[m*z[i]-sum(z) for i in range(d)]
 for j,v in enumerate(outer):
  ck(ell(v)==[d if i==j else -1 for i in range(m)])
 ck(all(sum(v[i] for v in outer)==0 for i in range(d)))
 ck(len({tuple(a%2 for a in z) for z in P})==d+2)
 ck(abs(s.Matrix([[outer[j+1][i]-outer[0][i] for j in range(d)] for i in range(d)]).det())==m)
 if d<=8:
  found=[]
  for z in product((-1,0,1),repeat=d):
   if min(ell(z))>=-1:found.append(z)
  ck(set(found)==set(P))
 alpha=F(d,m);gamma=alpha**d;beta=(1+gamma)/F(d+2)
 ck(gamma>F(1,m));ck(beta<gamma);ck(d+2<=2**d)
 ck(gamma/F(d+2)>=gamma/F(2**d))
 # Every canonical continuous cap has the claimed actual vertices and volume.
 vertices=[tuple([F(0)]*d)]+[tuple(F(int(i==j)) for j in range(d)) for i in range(d)]
 for j in range(m):
  p=vertices[j]
  section=[tuple(F(1,m)*p[i]+alpha*vertices[l][i] for i in range(d)) for l in range(m) if l!=j]
  centroid=tuple(sum(v[i] for v in section)/d for i in range(d))
  ck(centroid==(F(1,m),)*d)
  capverts=[p]+section
  volume_ratio=abs(s.Matrix([[s.Rational(capverts[l+1][i]-p[i]) for l in range(d)] for i in range(d)]).det())
  ck(volume_ratio==s.Rational(gamma))
  # Strict full/empty statuses at each outer fiber checked at every K vertex.
  for b in range(m):
   margins=[F(int(j==k))-F(1,m)+ell(outer[b])[j] for k in range(m)]
   ck(min(margins)>0 if b==j else max(margins)<0)
 ck(F(d,m)*alpha**(d-1)==gamma)
 # Cyclic vertex permutation is exactly volume preserving.
 destinations=vertices[1:]+vertices[:1]
 matrix=s.Matrix([[s.Rational(destinations[j+1][i]-destinations[0][i]) for j in range(d)] for i in range(d)])
 ck(abs(matrix.det())==1)
 # A nonsymmetric barycentric sample has exact cyclic average g.
 weights=[F(j+1,m*(m+1)//2) for j in range(m)]
 points=[]
 for shift in range(m):
  points.append(tuple(sum(weights[(j+shift)%m]*vertices[j][i] for j in range(m)) for i in range(d)))
 ck(all(sum(p[i] for p in points)==1 for i in range(d)))
 # Closed-halfspace argument: full sums vanish, including all-zero margins.
 for a,u in [(zero,zero),(tuple(range(1,d+1)),zero),(zero,tuple(range(d,0,-1))),
             (tuple((-1)**i*(i+1) for i in range(d)),tuple(2*i-1 for i in range(d)))]:
  margins=[sum(F(a[i])*outer[j][i]+F(u[i])*(points[j][i]-F(1,m)) for i in range(d)) for j in range(m)]
  ck(sum(margins)==0);ck(any(t>=0 for t in margins))
 # Exact potential-bound gap, without a floating-point optimizer.
 for r in [F(0),F(1,2*m),F(1,m)]:
  R=(gamma*r+F(1,m))/(1+r)
  ck(beta-R==(m*gamma-1)*(1-m*r)/(m*(m+1)*(1+r)))
  ck(R<=beta)

ck(F(4,9)-F(13,36)==F(1,12))
print(f'PASS: {checks} exact lattice, simplex clipping, section, coupling and profile checks')
