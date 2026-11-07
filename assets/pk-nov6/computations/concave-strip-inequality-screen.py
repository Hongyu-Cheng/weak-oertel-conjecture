import random
random.seed(761342)
def screen(lines):
    knots={0.0,1.0}
    for p,s in lines:
        for c,t in [(0,0),(1,0),(2,-1),(1.5,0),(3,-3)]:
            if s!=t:
                y=(c-p)/(s-t)
                if 0<y<1:knots.add(y)
    for j,(p,s) in enumerate(lines):
        for q,t in lines[:j]:
            if s!=t:
                y=(q-p)/(s-t)
                if 0<y<1:knots.add(y)
    xs=sorted(knots)
    prefix=best=low=0.0; low_x=0; best_span=(0,0)
    for a,b in zip(xs,xs[1:]):
        wa=min(p+s*a for p,s in lines); wb=min(p+s*b for p,s in lines)
        if (wa+wb)/2<0:
            prefix=low=0.0;low_x=b;continue
        def f(y,w):return w-3*min(1-y,max(w-1,0))
        prefix+=(b-a)*(f(a,wa)+f(b,wb))/2
        if prefix-low>best:best=prefix-low;best_span=(low_x,b)
        if prefix<low:low=prefix;low_x=b
    return best,best_span
best=(1.,None)
for j in range(150000):
    lines=[(3.,-1.)]+[(random.uniform(-5,8),random.uniform(-10,10)) for k in range(random.randrange(1,5))]
    val,span=screen(lines)
    if val>best[0]+1e-9:
        best=(val,(lines,span));print(j,best,flush=True)
    if val>1.000001:break
print('FINAL',best)
