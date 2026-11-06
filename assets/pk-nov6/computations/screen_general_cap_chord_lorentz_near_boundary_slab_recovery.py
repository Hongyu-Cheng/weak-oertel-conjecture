# Falsification only; actual rational polygons.
exec(open('./verify_fixed_endpoint_sector_polygon_replacement_slab_recovery.py').read().split('def verify(')[0])
import math,json
rng=Random(581913)
for it in range(15000):
 K=hull([(F(rng.randint(-30,30)),F(rng.randint(-30,30))) for _ in range(rng.randint(4,14))]+[(F(1),F(0)),(F(0),F(1)),(F(-1),F(-1))])
 ww=[F(1,1000) for _ in K]; ww[rng.randrange(len(K))]+=rng.choice([F(1),F(1,10),F(1,100)]); yy=tuple(sum(w*p[j] for w,p in zip(ww,K))/sum(ww) for j in range(2)); K=[sub(p,yy) for p in K]
 k=area(K);q=[area(clip(K,n))/k for n in [(1,0),(0,1),(-1,-1)]]
 ps=[ray_endpoint(K,d)[0] for d in rays]
 sig=[ps[1][1]-ps[4][1],ps[0][0]-ps[3][0],ps[5][0]-ps[2][0]]
 ht=[q[i]/sig[i] for i in range(3)];a=[x/sum(ht) for x in ht];f=[2*float(a[i])/math.sqrt(float(q[i])) for i in range(3)]
 vals=[f[i]+(sum(f)-f[i])**2/4 for i in range(3)]
 if max(vals)>2+1e-8:
  print(json.dumps({'iteration':it,'vertices':[[str(x),str(y)] for x,y in K],'q':list(map(str,q)),'sigma':list(map(str,sig)),'a':list(map(str,a)),'values':vals}),flush=True);break
else:print('none',flush=True)
