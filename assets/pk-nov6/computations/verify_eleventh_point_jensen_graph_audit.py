"""Independent exact certificate for the eleven-point integral Jensen graph."""
from fractions import Fraction as F
from itertools import product

P=[(0,0,1),(1,0,0),(1,0,1),(1,0,2),(1,1,0),(1,1,1),
   (2,0,1),(2,1,0),(2,1,1),(2,1,2),(2,2,0)]
g=[F(1),F(1),F(1,2)]+[F(0)]*8
facets=[(-1,0,-1,-1),(-1,1,0,0),(-1,1,1,1),(-1,2,1,2),
        (0,-1,0,0),(0,0,-1,0),(1,-1,-1,1),(1,-1,1,3),(1,0,0,2)]
dot=lambda u,p:sum(x*y for x,y in zip(u,p))
assert all(dot(row[:3],p)<=row[3] for row in facets for p in P)
assert [p for p in product(range(3),repeat=3)
        if all(dot(row[:3],p)<=row[3] for row in facets)]==P
assert all(any(dot(row[:3],p)==row[3] for row in facets) for p in P)

faces={}
for j,p in enumerate(P):
    active=[row for row in facets if dot(row[:3],p)==row[3]]
    face=[i for i,q in enumerate(P)
          if all(dot(row[:3],q)==row[3] for row in active)]
    if len(face)>1:
        faces[j]=face
    else:
        u=tuple(sum(row[c] for row in active) for c in range(3))
        assert all(dot(u,p)>dot(u,q) for q in P if q!=p)
assert faces=={2:[0,1,2,3,6],8:[6,7,8,9,10]}
for i in faces[2]:
    assert g[i]==F(3-P[i][0]-P[i][2],2)
for i in faces[8]:
    assert g[i]==0

relations=[{0:1,6:1,2:-2},{1:1,3:1,2:-2},
           {7:1,9:1,8:-2},{6:1,10:1,7:-1,8:-1}]
for row in relations:
    assert sum(row.values())==0
    assert all(sum(c*P[i][j] for i,c in row.items())==0 for j in range(3))
    assert sum(c*g[i] for i,c in row.items())==0
# Columns 0,1,9,10 give independent pivots for the four relation rows.
for r,pivot in enumerate([0,1,9,10]):
    assert relations[r].get(pivot,0)!=0
    assert all(row.get(pivot,0)==0 for j,row in enumerate(relations) if j!=r)

W=[0,1,3,4,5,6,7,8,10]
certificate={0:((-3,1,0),0,2),1:((0,-2,-3),0,2),
             3:((0,1,3),6,2),4:((-2,1,-2),-1,1),
             5:((-2,3,2),3,1),6:((3,-2,0),6,2),
             7:((2,-1,-2),3,1),8:((2,1,2),7,1),
             10:((0,2,0),4,2)}
for i,(u,value,gap) in certificate.items():
    assert dot(u,P[i])==value
    assert min(value-dot(u,P[j]) for j in W if j!=i)==gap>0
assert max(P[i][1]+P[i][2] for i in W)==2
assert P[9][1]+P[9][2]==3
for pair in [(0,6),(1,3)]:
    assert tuple(F(P[pair[0]][j]+P[pair[1]][j],2) for j in range(3))==P[2]
    assert (g[pair[0]]+g[pair[1]])/2==g[2]==F(1,2)
assert not set((0,6))&set((1,3))

T=[i for i in range(11) if g[i].denominator==1]
assert T==[0,1,3,4,5,6,7,8,9,10]
q=[(*p,g[i]) for i,p in enumerate(P)]
assert tuple((q[7][j]+q[9][j])/2 for j in range(4))==q[8]
print('PASS: exact P, two minimal faces, all Jensen relations, '
      'sole fractional deletion-kernel point, lattice-convex graph, h(T)=9>8')
