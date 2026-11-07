"""Falsification screen only; output is not a theorem or exact certificate."""
import random
import math

rng = random.Random(20260929)


def cross(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def hull(points):
    points = sorted(set(points))
    low, up = [], []
    for p in points:
        while len(low)>1 and cross(low[-2],low[-1],p)<=0:
            low.pop()
        low.append(p)
    for p in points[::-1]:
        while len(up)>1 and cross(up[-2],up[-1],p)<=0:
            up.pop()
        up.append(p)
    return low[:-1]+up[:-1]


def area(p):
    return abs(sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(p,p[1:]+p[:1])))/2


def val(p, i):
    return (p[0],p[1],-p[0]-p[1])[i]


def data(p, i):
    out, sec = [], []
    for a,b in zip(p,p[1:]+p[:1]):
        u,v=val(a,i),val(b,i)
        if u>=0:
            out.append(a)
        if u==0:
            sec.append(a)
        if u*v<0:
            t=u/(u-v)
            z=(a[0]+t*(b[0]-a[0]),a[1]+t*(b[1]-a[1]))
            out.append(z)
            sec.append(z)
    axis=1 if i==0 else 0
    return area(out), max(x[axis] for x in sec)-min(x[axis] for x in sec)


best=(-1,None)
for iteration in range(100000):
    points=[(rng.randint(-100,100),rng.randint(-100,100))
            for _ in range(rng.randint(4,14))]
    p=hull(points)
    if len(p)<3 or not all(cross(a,b,(0,0))>0 for a,b in zip(p,p[1:]+p[:1])):
        continue
    k=area(p)
    dat=[data(p,i) for i in range(3)]
    q=[x[0]/k for x in dat]
    cone=[x[0]/x[1] for x in dat]
    f=[2*cone[i]/(sum(cone)*math.sqrt(q[i])) for i in range(3)]
    gap=max(f[i]+sum(f[j] for j in range(3) if j!=i)**2/4-2 for i in range(3))
    if gap>best[0]:
        best=(gap,(p,q,f))
    if gap>1e-8:
        print('VIOLATION',iteration,best)
        break
else:
    print('NO VIOLATION',best)
