from fractions import Fraction as F
W={(-1,-1):F(1,2),(-1,0):F(1,2),(-1,1):F(-1,2),
   (0,-1):F(2),(0,0):F(-5),(0,1):F(2),
   (1,-1):F(-1,2),(1,0):F(1,2),(1,1):F(1,2)}
assert sum(W.values())==0
assert sum(w*x for (x,y),w in W.items())==0
assert sum(w*y for (x,y),w in W.items())==0
assert sum(w*x*x for (x,y),w in W.items())==1
assert sum(w*x*y for (x,y),w in W.items())==2
assert sum(w*y*y for (x,y),w in W.items())==4
for a in range(-2,3):
 for b in range(-2,3):
  for c in range(-2,3):
   assert sum(w*(a+b*x+c*y)**2 for (x,y),w in W.items())==(b+2*c)**2
for z in W:
 collinear=[p for p in W if (p[1]-z[1])==2*(p[0]-z[0])]
 assert len(collinear)<=2
print('Exact PSD stress and unavailable variance direction verified.')

W2={(-1,-1):F(5,4),(-1,0):F(-1),(-1,1):F(1,4),
    (0,-1):F(1,2),(0,0):F(-2),(0,1):F(1,2),
    (1,-1):F(1,4),(1,0):F(-1),(1,1):F(5,4)}
for exponents in [(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]:
 i,j=exponents
 assert sum(w*x**i*y**j for (x,y),w in W2.items())==sum(w*x**i*y**j for (x,y),w in W.items())
assert all(W2[(x,y)]>0 for x in [-1,1] for y in [-1,1])
print('Positive-extreme-vertex variant verified.')
