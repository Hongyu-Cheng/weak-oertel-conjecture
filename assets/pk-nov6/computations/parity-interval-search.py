import random
from itertools import combinations,product
from fractions import Fraction
ns={};exec(open('./parity-center-search.py').read().split('random.seed')[0],ns)
hull=ns['hull'];points_in=ns['points_in']

def center_depth(pts,p,certificate=False):
    ds=[(q[0]-p[0],q[1]-p[1]) for q in pts]
    candidates=[(0,0,1)]
    for dx,dy in ds:
        if dx or dy:
            candidates += [(dx,dy,dx*dx+dy*dy),(-dx,-dy,dx*dx+dy*dy)]
    for (x,y),(u,v) in combinations(ds,2):
        det=x*v-y*u
        if not det:continue
        for s,t in product((-1,1),repeat=2):
            aa=s*v-t*y;bb=x*t-u*s
            if det<0:aa=-aa;bb=-bb
            candidates.append((aa,bb,abs(det)))
    bn,bd=len(pts),2;bc=(0,0,1)
    for a,b,c in candidates:
        num=sum(max(0,min(2*c,c+a*x+b*y)) for x,y in ds);den=2*c
        if num*bd<bn*den:bn,bd,bc=num,den,(a,b,c)
    return (Fraction(bn,bd),bc) if certificate else Fraction(bn,bd)

def best(pts):return max(center_depth(pts,p) for p in pts)/len(pts)
random.seed(2177)
for it in range(20000):
 h=hull([(random.randrange(-4,5),random.randrange(-4,5)) for _ in range(random.randrange(3,8))])
 if len(h)<3:continue
 pts=points_in(h)
 if not 5<=len(pts)<=22:continue
 ds=[[(x,y) for x,y in pts if (x%2,y%2)==r] for r in product((0,1),repeat=2)]
 ds=[d for d in ds if d]
 lower=min(best(d) for d in ds)
 upper=best(pts)
 if lower>upper:
  print('FOUND',h,'N',len(pts),'original',upper,'parity',[best(d) for d in ds], 'points',pts,flush=True)
  print('original certificates',[(p,center_depth(pts,p,True)) for p in pts],flush=True)
  print('parity certificates',[[(p,center_depth(d,p,True)) for p in d] for d in ds],flush=True)
  break
 if it%100==0:print('checked',it,flush=True)
else:print('none found',flush=True)
