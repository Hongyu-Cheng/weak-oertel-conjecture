import json, random
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import linprog

def fibers(poly):
    ans={}
    for z in range(int(min(x for x,y in poly)),int(max(x for x,y in poly))+1):
        ys=[]
        for i,(x,y) in enumerate(poly):
            x1,y1=poly[(i+1)%len(poly)]
            if x==x1:
                if z==x: ys.extend([y,y1])
            elif min(x,x1)<=z<=max(x,x1):
                ys.append(y+(y1-y)*(z-x)/(x1-x))
        if ys: ans[z]=(min(ys),max(ys))
    return ans

def caps(f):
    pts=[(z,x) for z,ends in f.items() for x in ends]
    out=[];seen=set();M=sum(v-u for u,v in f.values())
    for j,(z,x) in enumerate(pts):
        for zz,xx in pts[j+1:]:
            if z==zz: continue
            s=(xx-x)/(zz-z);t=x-s*z
            key=(round(s,9),round(t,9))
            if key in seen:continue
            seen.add(key)
            mass=sum(max(0,min(v-u,s*k+t-u)) for k,(u,v) in f.items())
            if mass<M/2-1e-8:out.append((s,t,mass,1))
            elif mass>M/2+1e-8:out.append((s,t,M-mass,-1))
    # Additional caps close to half mass detect support-span constraints
    # absent from the endpoint arrangement vertices alone.
    slopes=[s for s,t,m,side in out]
    slopes=sorted(set(slopes))
    sample=slopes+[(a+b)/2 for a,b in zip(slopes,slopes[1:])]
    for s in sample:
        levels=sorted(set(e-s*k for k,ends in f.items() for e in ends))
        vals=[sum(max(0,min(v-u,s*k+t-u)) for k,(u,v) in f.items()) for t in levels]
        for target in [.001*M,.1*M,.2499*M,.49999*M,.50001*M,.7501*M,.9*M,.999*M]:
            for j,(a,b) in enumerate(zip(vals,vals[1:])):
                if a<=target<=b and b>a:
                    t=levels[j]+(target-a)/(b-a)*(levels[j+1]-levels[j])
                    side=1 if target<M/2 else -1
                    out.append((s,t,min(target,M-target),side))
                    break
    return out

def constraints(f,k,cc):
    M=sum(v-u for u,v in f.values())
    u,v=f[k]
    rows=[([u,1],0,{'support':'left'}),([-v,-1],-1,{'support':'right'})]
    for s,t,m,side in cc:
        x=s*k+t
        rhs=2*m/M if side==1 else 2*m/M-1
        rows.append(([side*x,side],rhs,{'slope':s,'intercept':t,'mass':m,'side':side}))
    return rows

def feasible(rows):
    return linprog([0,0],A_ub=[r[0] for r in rows],b_ub=[r[1] for r in rows],
                   bounds=[(None,None),(None,None)],method='highs').success

def minimize(rows):
    i=0
    while i<len(rows):
        rr=rows[:i]+rows[i+1:]
        if not feasible(rr): rows=rr
        else:i+=1
    return rows

random.seed(70914)
for it in range(5000):
    pts=list(set((random.randint(0,random.choice([3,4,5,7])),random.randint(-12,12)) for _ in range(random.randint(5,16))))
    if len(pts)<3: continue
    try:poly=[pts[i] for i in ConvexHull(pts).vertices]
    except:continue
    f=fibers(poly);M=sum(v-u for u,v in f.values())
    if M<=0:continue
    med=[k for k,(u,v) in f.items() if v>u and sum(vv-uu for j,(uu,vv) in f.items() if j<k)<=M/2+1e-8
         and sum(vv-uu for j,(uu,vv) in f.items() if j>k)<=M/2+1e-8]
    cc=caps(f);bad=[]
    for k in med:
        rows=constraints(f,k,cc)
        if feasible(rows):break
        bad.append((k,minimize(rows)))
    else:
        out={'iteration':it,'polygon':poly,'fibers':f,'mass':M,'certificates':bad}
        print(json.dumps(out,indent=2),flush=True)
        with open('./uniform_interval_target_counterexample.json','w') as ff:json.dump(out,ff,indent=2)
        break
    if it%500==0:print('tested',it,flush=True)
