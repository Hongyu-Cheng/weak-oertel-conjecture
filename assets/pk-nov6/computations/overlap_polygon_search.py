import random,math,json
exec(open('./tilt_search.py').read().split('random.seed')[0])

def symmetric_overlap(K,y):
    P=K[:]
    R=[(2*y[0]-p[0],2*y[1]-p[1]) for p in K]
    for p,q in zip(R,R[1:]+R[:1]):
        b=(-(q[1]-p[1]),q[0]-p[0]);t=b[0]*p[0]+b[1]*p[1]
        out=[]
        for v,w in zip(P,P[1:]+P[:1]):
            sv=b[0]*v[0]+b[1]*v[1]-t;sw=b[0]*w[0]+b[1]*w[1]-t
            if sv>=0:out.append(v)
            if sv*sw<0:
                r=sv/(sv-sw);out.append((v[0]+r*(w[0]-v[0]),v[1]+r*(w[1]-v[1])))
        P=out
        if len(P)<3:return 0
    return ac(P)[0]

def max_overlap(K):
    A,y=ac(K);best=symmetric_overlap(K,y);step=max(max(p[j] for p in K)-min(p[j] for p in K) for j in (0,1))/4
    dirs=[(math.cos(i*math.pi/4),math.sin(i*math.pi/4)) for i in range(8)]
    while step>1e-8:
        opts=[(symmetric_overlap(K,(y[0]+step*a,y[1]+step*b)),(y[0]+step*a,y[1]+step*b)) for a,b in dirs]
        v,p=max(opts)
        if v>best+1e-12:best,y=v,p
        else:step/=2
    return best,y

random.seed(901)
record=1
for i in range(5000):
    K=hull([(random.randint(-30,30),random.randint(-30,30)) for _ in range(random.randint(3,10))])
    if len(K)<3:continue
    A,c=ac(K);R,y=max_overlap(K)
    best=(1,None)
    for j in range(360):
        th=2*math.pi*j/360;b=(math.cos(th),math.sin(th));p=cap(K,b,sum(a*v for a,v in zip(b,y)))/A
        best=min(best,(p,b))
    if best[0]<record:
        record=best[0]
        print(i,'depth',record,'R',R/A,'K',K,'y',y,flush=True)
        with open('./overlap_polygon_best.json','w') as f:json.dump(dict(K=K,A=A,R=R,y=y,best=best),f)
    if best[0]<4/9-1e-5:
        print('FOUND',flush=True);break
