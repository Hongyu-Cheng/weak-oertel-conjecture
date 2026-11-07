"""Numerical discovery only; every candidate needs a separate exact certificate."""
import random
import json
from pathlib import Path


def at_anchor(r,j):
    radius=[(r[j],1)]+[(min(r[j-h],r[j+h]),2)
                       for h in range(1,min(j,len(r)-1-j)+1)]
    events={}
    for v,w in radius:
        e=events.setdefault(v/3,[0,0]);e[0]-=12*w;e[1]+=4*w*v
        e=events.setdefault(v/2,[0,0]);e[0]+=8*w;e[1]-=4*w*v
    A=4*sum(w for _,w in radius);B=0
    lo=0.0;best=(0.0,0.0)
    for hi,(da,db) in sorted(events.items()):
        if A<0:
            t=-B/(2*A)
            if lo<=t<=hi:
                best=max(best,(A*t*t+B*t,t))
        best=max(best,(A*hi*hi+B*hi,hi))
        A+=da;B+=db;lo=hi
    return best


def screen(r,partial=False):
    target=2*sum(x*x for x in r)/9
    mass=sum(x*x for x in r)
    acc=0;jmed=0
    for j,x in enumerate(r):
        acc+=x*x
        if acc>=mass/2:
            jmed=j;break
    order=sorted(range(len(r)),key=lambda j:abs(j-jmed))
    vals=[]
    for j in order:
        v,a=at_anchor(r,j)
        vals.append((v,j,a))
        if partial and v>=target:
            return False,max(vals),target
    return max(vals)[0]<target,max(vals),target


if __name__=='__main__':
    rng=random.Random(736623)
    least=(float('inf'),None)
    for it in range(100000):
        N=rng.choice([4,5,6,7,8,10,12,16,20,25,33,40,50,64,80,100])
        slope=sorted([rng.randrange(-50,51) for _ in range(N-1)],reverse=True)
        r=[0]
        for s in slope:
            r.append(r[-1]+s)
        offset=1-min(r)+rng.randrange(max(r)-min(r)+1)//rng.choice([1,2,5,20,100])
        r=[x+offset for x in r]
        assert min(r)>0
        bad,best,target=screen(r,partial=True)
        ratio=best[0]/target
        if ratio<least[0]:
            least=(ratio,(it,r,best,target))
            print('BEST PARTIAL',least,flush=True)
        if bad:
            print('CANDIDATE',it,r,best,target,flush=True)
            Path('./triangle_chain_inner_pair_candidate.json').write_text(
                json.dumps({'iteration':it,'radii':r,'best':best,'target':target}))
            break
    else:
        print('NO COUNTER:100000 partial-rejection screens; least stopping ratio',least,flush=True)
