import random,json

def overlap(intervals,j,x):
    return sum(max(0,min(u,2*x-intervals[2*j-i][0])-max(l,2*x-intervals[2*j-i][1]))
               for i,(l,u) in enumerate(intervals) if 0<=2*j-i<len(intervals))

def maxima(intervals):
    best=-1; pieces=[]
    for j,(l,u) in enumerate(intervals):
        bp=sorted(set([l,u]+[(a+b)/2 for i,I in enumerate(intervals) if 0<=2*j-i<len(intervals)
                           for a in I for b in intervals[2*j-i] if l<=(a+b)/2<=u]))
        vals=[overlap(intervals,j,x) for x in bp]
        for i,(x,v) in enumerate(zip(bp,vals)):
            if v>best+1e-8:best=v;pieces=[(j,x,x)]
            elif abs(v-best)<1e-8:pieces.append((j,x,x))
            if i and abs(v-vals[i-1])<1e-8 and abs(v-best)<1e-8:pieces.append((j,bp[i-1],x))
    # Filter earlier obsolete recorded segments against the final best.
    return best,[p for p in pieces if abs(overlap(intervals,p[0],(p[1]+p[2])/2)-best)<1e-8]

def depth(intervals,j,x):
    N=len(intervals);M=sum(u-l for l,u in intervals)
    best=(M,None)
    for sign in (-1,1):
        Js=[(l,u) if sign==1 else (-u,-l) for l,u in intervals]; xx=sign*x
        bp=[(v-xx)/(j-i) for i,I in enumerate(Js) if i!=j for v in I]
        scale=max([1]+[abs(t) for t in bp]);bp +=[-scale-100,scale+100]
        for a in bp:
            mass=sum(max(0,min(u-l,u-xx-a*(j-i))) for i,(l,u) in enumerate(Js))
            if mass<best[0]:best=mass,(sign,a,xx+a*j)
    return best[0]/M,best[1]

random.seed(2034)
best=1
for step in range(30000):
    m=random.randint(2,9)
    fl=[0];up=[0];sf=random.uniform(-3,0);su=random.uniform(0,3)
    for i in range(m):
        sf+=random.random()*2;su-=random.random()*2
        fl.append(fl[-1]+sf);up.append(up[-1]+su)
    shift=max(l-u for l,u in zip(fl,up))+random.uniform(.001,3)
    Is=list(zip(fl,[u+shift for u in up]));M=sum(u-l for l,u in Is)
    R,ps=maxima(Is);ratio=R/M
    if ratio<best:
        best=ratio
        print(step,'overlap ratio',ratio,'maximizers',ps,flush=True)
        with open('./overlap_interval_best.json','w') as f:json.dump(dict(Is=Is,ratio=ratio,maxima=ps),f)
    if ratio<.5-1e-5:
        ds=[depth(Is,j,(l+u)/2)[0] for j,l,u in ps]
        print('LOW',ratio,ds,flush=True)
        if max(ds)<.25:
            print('POTENTIAL SELECTOR COUNTEREXAMPLE',flush=True);break
