from itertools import product
P=[(1,1),(2,0),(2,1),(3,-2),(3,-1),(3,0),(3,1),(3,2),(4,3)]
t=[14,14,13,14,14,14,12,10,7];w=[21+x for x in t];G=[p+(v,) for p,v in zip(P,t)]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
U=sorted([u for u in product(range(-12,13),repeat=3) if any(u)],key=lambda u:(sum(abs(x) for x in u),u))
for i,g in enumerate(G):
 best=sum(w);bu=None;inds=None
 for u in U:
  cap=[j for j,q in enumerate(G) if dot(u,q)>=dot(u,g)];mass=sum(w[j] for j in cap)
  if mass<best:best=mass;bu=u;inds=cap
 print(i,g,bu,'threshold',dot(bu,g),'cap',inds,'mass',best)
print('T',sum(w))
