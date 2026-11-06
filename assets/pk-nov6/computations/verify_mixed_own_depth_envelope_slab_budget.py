from fractions import Fraction as F

checks=0
def ck(v,msg):
    global checks
    assert v,msg
    checks+=1

def clip(x): return min(F(1),max(F(0),x))
def depth(x):
    return min(x+min(2*x,F(1)),3-x+min(2*max(1-x,0),F(1)))
def own(x): return min(x,3-x)
def envelope(lam): return max(2+lam,F(3,2)*(1+lam))
# Exact formula and objective checks on rational samples supplement,
# rather than replace, the full interval proof in the source.
for i in range(49):
    x=F(i,16)
    for j in range(33):
        lam=F(j,8)
        ck(depth(x)+lam*own(x)<=envelope(lam),'actual potential envelope')
    if F(1)<=x<=F(3,2):
        ck(depth(x)==3-x and own(x)==x,'ridge formulas')
        ck(depth(x)+own(x)==3,'continuum of maximizers')
for j in range(33):
    lam=F(j,8)
    x=F(1) if lam<1 else F(3,2)
    ck(depth(x)+lam*own(x)==envelope(lam),'envelope attained')
    ck((1+lam)/2<envelope(lam),'endpoint fibers do not win')
for count in range(1,18):
    xs=[F(1)+F(i,2*count) for i in range(count+1)]
    tsum=F(0)
    for x0,x1 in zip(xs,xs[1:]):
        xm=(x0+x1)/2
        slab=x1-xm
        delta=own(x1)-own(x0)
        midpoint_gain=own(xm)-(own(x0)+own(x1))/2
        drop=depth(x0)-depth(x1)
        ck(slab+midpoint_gain==drop/2==delta/2,'sharp actual slab charge')
        tsum+=slab
    ck(tsum==F(1,4),'sharp summed actual slab charge')
# General exact chord algebra at rational abstract endpoint data.
for l0 in [F(0),F(1,4),F(1)]:
    for width in [F(1,3),F(1),F(3)]:
        l1=l0+width
        for t in [F(0),F(1,5),F(1,2),F(4,5),F(1)]:
            star=l0+t*width
            delta=F(2,3)
            bound=delta*(star-l0)*(l1-star)/width
            ck(0<=bound<=width*delta/4,'convex envelope gap bound')
ck(F(1)*(F(3,2)-1)==F(2)-F(3,2),'Stieltjes atom/intercept identity')
# The full tied-source segment is an actual continuum in this body.
for i in range(1,20):
    t=F(i,20)
    xt=1+t/2
    ck(depth(xt)==2-t/2 and own(xt)==1+t/2, 'ordered segment values')
    ck(depth(xt)-depth(F(3,2))==(1-t)/2, 'sharp remaining-segment charge')
    for j in range(i+1,21):
        ss=F(j,20)
        xs=1+ss/2
        ck(depth(xt)-depth(xs)==xs-xt>0, 'adjacent actual slab and strict monotonicity')
        ck(own(xs)>own(xt), 'strict own-root order')
print(f'{checks} exact rational checks passed.')
