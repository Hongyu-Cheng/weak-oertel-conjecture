"""Falsification only: test a proposed three-cap/chord balance inequality."""
import random, math

def cross(o,a,b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])

def hull(points):
    ps=sorted(set(points))
    lo=[]
    for p in ps:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=0: lo.pop()
        lo.append(p)
    hi=[]
    for p in reversed(ps):
        while len(hi)>=2 and cross(hi[-2],hi[-1],p)<=0: hi.pop()
        hi.append(p)
    return lo[:-1]+hi[:-1]

def area(p):
    return abs(sum(x[0]*y[1]-x[1]*y[0] for x,y in zip(p,p[1:]+p[:1])))/2 if p else 0

def clip(p,u):
    out=[]
    for a,b in zip(p,p[1:]+p[:1]):
        va=sum(x*y for x,y in zip(a,u)); vb=sum(x*y for x,y in zip(b,u))
        if va>=0: out.append(a)
        if (va<0<vb) or (vb<0<va):
            t=va/(va-vb)
            out.append(tuple(a[j]+t*(b[j]-a[j]) for j in range(2)))
    return out

def chord(p,u):
    pts=[]
    for a,b in zip(p,p[1:]+p[:1]):
        va=sum(x*y for x,y in zip(a,u)); vb=sum(x*y for x,y in zip(b,u))
        if va==0: pts.append(a)
        if (va<0<vb) or (vb<0<va):
            t=va/(va-vb)
            pts.append(tuple(a[j]+t*(b[j]-a[j]) for j in range(2)))
    if len(pts)<2:return 0,0
    rs=[math.hypot(*pt) for pt in pts]
    return math.dist(pts[0],pts[-1])/math.hypot(*u),min(rs)/max(rs)

def run():
    rng=random.Random(628161)
    normals=[(1,0),(0,1),(-1,-1)]
    best=(0,None)
    accepted=0
    for it in range(500000):
        ps=[(rng.randint(-25,25),rng.randint(-25,25)) for _ in range(rng.randrange(3,14))]
        p=hull(ps)
        if len(p)<3 or any(cross(a,b,(0,0))<=0 for a,b in zip(p,p[1:]+p[:1])):continue
        k=area(p)
        qs=[area(clip(p,u))/k for u in normals]
        rho=max(qs)
        if rho>=.5:continue
        data=[chord(p,u) for u in normals]
        if min(x[1] for x in data)<1/math.sqrt(3):continue
        ss=[x[0] for x in data]
        ratio=max(ss)/min(ss)
        proposed=min(.5,(ratio+1)**2/(9*ratio))
        gap=proposed-rho
        accepted+=1
        if gap>best[0]:
            best=(gap,dict(poly=p,ratios=qs,sections=ss,chord_ratio=ratio,radial_ratios=[x[1] for x in data],proposed=proposed,iteration=it))
    print('accepted',accepted,'best violation',best)

if __name__=='__main__':run()
