import random

def cross(o,a,b): return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
def hull(points):
    points=sorted(set(points)); lo=[]; hi=[]
    for p in points:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=0: lo.pop()
        lo.append(p)
    for p in reversed(points):
        while len(hi)>=2 and cross(hi[-2],hi[-1],p)<=0: hi.pop()
        hi.append(p)
    return lo[:-1]+hi[:-1]
def points_in(h):
    return [(x,y) for x in range(min(p[0] for p in h),max(p[0] for p in h)+1)
                  for y in range(min(p[1] for p in h),max(p[1] for p in h)+1)
                  if all(cross(h[i],h[(i+1)%len(h)],(x,y))>=0 for i in range(len(h)))]
def depth(pts,p):
    ds=[(q[0]-p[0],q[1]-p[1]) for q in pts if q!=p]
    m=1+sum(abs(dx)+abs(dy) for dx,dy in ds)**2
    best=len(pts)
    for dx,dy in ds:
        for sig in (-1,1):
            a=(-dy*m+sig*dx,dx*m+sig*dy)
            best=min(best,1+sum(a[0]*u+a[1]*v>=0 for u,v in ds))
    return best

random.seed(1133)
for it in range(10000):
    h=hull([(random.randrange(-5,6),random.randrange(-5,6)) for _ in range(random.randrange(3,9))])
    if len(h)<3: continue
    pts=points_in(h)
    target=max(sum((x%2,y%2)==(a,b) for x,y in pts) for a in (0,1) for b in (0,1))
    candidates=[(depth(pts,p),p) for p in pts]
    best=max(candidates)
    if best[0]<target:
        print('COUNTEREXAMPLE',h,'N',len(pts),'parity',target,'best',best,'depths',candidates,flush=True)
        break
    if it%1000==0: print('checked',it,flush=True)
else: print('none found',flush=True)
