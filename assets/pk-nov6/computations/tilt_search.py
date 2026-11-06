import math, random, json

def hull(ps):
    ps=sorted(set(ps))
    def cross(o,a,b): return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lo=[]; hi=[]
    for p in ps:
        while len(lo)>1 and cross(lo[-2],lo[-1],p)<=1e-10: lo.pop()
        lo.append(p)
    for p in reversed(ps):
        while len(hi)>1 and cross(hi[-2],hi[-1],p)<=1e-10: hi.pop()
        hi.append(p)
    return lo[:-1]+hi[:-1]

def ac(ps):
    if len(ps)<3: return 0,(0,0)
    area=cx=cy=0
    for p,q in zip(ps,ps[1:]+ps[:1]):
        t=p[0]*q[1]-p[1]*q[0]
        area+=t; cx+=(p[0]+q[0])*t; cy+=(p[1]+q[1])*t
    if abs(area)<1e-15: return 0,(0,0)
    return area/2,(cx/(3*area),cy/(3*area))

def cap(ps,b,t):
    out=[]
    for p,q in zip(ps,ps[1:]+ps[:1]):
        sp=sum(x*y for x,y in zip(p,b))-t
        sq=sum(x*y for x,y in zip(q,b))-t
        if sp>=0: out.append(p)
        if (sp<0 and sq>0) or (sp>0 and sq<0):
            r=sp/(sp-sq); out.append(tuple(x+r*(y-x) for x,y in zip(p,q)))
    return ac(out)[0]

def directed_depth(Ks,j,y,b):
    by=sum(x*v for x,v in zip(y,b))
    def f(u): return sum(cap(K,b,by+u*(j-i)) for i,K in enumerate(Ks))
    breaks=sorted(set((sum(x*v for x,v in zip(p,b))-by)/(j-i) for i,K in enumerate(Ks) if i!=j for p in K))
    m=max(1,breaks[-1]-breaks[0]); breaks=[breaks[0]-m]+breaks+[breaks[-1]+m]
    best=min((f(u),u) for u in breaks)
    for l,r in zip(breaks,breaks[1:]):
        if r-l<1e-12:continue
        fl,fm,fr=f(l),f((l+r)/2),f(r)
        qa=2*(fr+fl-2*fm); qb=fr-fl-qa
        if qa>1e-12:
            s=-qb/(2*qa)
            if 0<s<1:
                u=l+s*(r-l); best=min(best,(f(u),u))
    return best

def random_tri():
    a=random.uniform(-2,2); b=random.uniform(-2,2)
    sx=10**random.uniform(-.5,.5); sy=10**random.uniform(-.5,.5)
    return hull([(a+sx*random.uniform(-1,1),b+sy*random.uniform(-1,1)) for _ in range(4)])

random.seed(1908)
record=1
for iteration in range(1000):
    Ks=[random_tri() for _ in range(3)]
    Ks[1]=hull(Ks[1]+[tuple((a+b)/2 for a,b in zip(p,q)) for p in Ks[0] for q in Ks[2]])
    As,Cs=zip(*(ac(K) for K in Ks))
    if min(As)<1e-7: continue
    total=sum(As)
    if max(As[0],As[2])>=total/2: continue
    w=As[1]*math.sqrt(As[0]/As[2]); den=2*As[0]+w
    y=tuple((As[0]*(Cs[0][k]+Cs[2][k])+w*Cs[1][k])/den for k in range(2))
    best=(float('inf'),0,0)
    for k in range(120):
        th=2*math.pi*k/120; b=(math.cos(th),math.sin(th))
        val,u=directed_depth(Ks,1,y,b)
        best=min(best,(val/total,th,u))
    if best[0]<record:
        record=best[0]
        print(iteration,record,As,flush=True)
        with open('./tilt_best.json','w') as f: json.dump(dict(Ks=Ks,As=As,Cs=Cs,y=y,best=best),f)
    if best[0]<2/9-1e-6:
        print('FOUND',flush=True);break
