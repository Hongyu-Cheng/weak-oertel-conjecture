"""Exact rational checks; the note proves the uniform all-epsilon inequalities."""
from fractions import Fraction as F

def h(w):return (w+1/w)/2
def low(w):return (w-1/w)/2
def m(w):return w/2+1/(6*w**3)
def L(w):return h(w)-m(w)

bracket=4/(3*F(51,50)**4)-F(201,100)**3/9
assert bracket-F(1,4)==F(1613599914733,20295603000000)>0
assert 1+F(1,100)+2*F(1,100)**2<F(51,50)
assert F(403,600)<1

for N in [100,101,125,200,1000,10000,10**6]:
    e=F(1,N);v=1+e;u=v+2*e*e
    for w in (u,v):
        assert h(w)**2-low(w)**2==1
        assert F(2,3)*(h(w)**3-low(w)**3)==m(w)
        t0=2*m(w)-h(w)
        assert h(w)**2-t0*t0==F(8,9)+(w*w-1)**3/(9*w**6)
    hm=(h(u)+h(v))/2;lm=(low(u)+low(v))/2
    delta=hm*hm-lm*lm-1
    assert delta==(u-v)**2/(4*u*v)==e**4/(u*v)
    shift=L(u);t=m(v)-shift;t0=2*m(v)-h(v)
    Delta=L(v)-L(u)
    assert shift>0 and low(v)<t<h(v)
    assert t==t0+Delta
    assert t0>=F(1,3)
    assert low(v)<=e
    assert Delta>=e**3*(2+e)/u**4
    cost=h(v)**2-t*t
    S=F(8,9)-cost
    assert S==2*t0*Delta+Delta*Delta-(v*v-1)**3/(9*v**6)
    assert S>=bracket*e**3>e**3/4
    assert delta<=e**4
    assert S/delta>1/(4*e)
    g=(m(u)+m(v))/2;common_shift=h(u)-g
    assert common_shift>0
    assert g+common_shift==h(u) and g-common_shift==t

# Polynomial identities behind the symbolic rational formulas.
def add(a,b):
    return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
            for i in range(max(len(a),len(b)))]
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c
def scale(a,c):return [c*x for x in a]
def equal(a,b):
    while len(a)>1 and a[-1]==0:a.pop()
    while len(b)>1 and b[-1]==0:b.pop()
    assert a==b

# h²-t0²-8/9=(w²-1)³/(9w⁶), common denominator36w⁶.
hnum=[1,0,1]           # h=(w²+1)/(2w)
tnum=[2,0,-3,0,3]      # t0=(3w⁴-3w²+2)/(6w³)
lhs=add(scale(mul([0,0,0,0,1],mul(hnum,hnum)),9),
        scale(mul(tnum,tnum),-1))
lhs=add(lhs,[0,0,0,0,0,0,-32])
rhs=scale(mul(mul([-1,0,1],[-1,0,1]),[-1,0,1]),4)
equal(lhs,rhs)

print('PASS: rational planar linear-BM compensation obstruction')
print('uniform shortfall coefficient minus1/4 =',bracket-F(1,4))
