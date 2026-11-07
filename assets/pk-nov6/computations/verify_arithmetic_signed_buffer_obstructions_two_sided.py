from fractions import Fraction as F
from itertools import product

checks = 0

def eq(a,b):
    global checks
    assert a == b, (a,b)
    checks += 1

def yes(a):
    global checks
    assert a
    checks += 1

def cap(v,h):
    return min(v,max(F(0),v/2-h))

def pair_formula(a,b,h):
    return min(a,max(F(0),(a+b)/2-2*h))

# Piecewise-linear minimization is attained at a breakpoint or an
# asymptotic constant cell; testing all breakpoints is an exact check.
for a,b in [(F(1,8),F(1)),(F(1),F(1)),(F(2,3),F(7,5)),(F(1,7),F(9,7))]:
    for hn in range(-30,31):
        h=F(hn,16)
        knots=[-a/2-h,a/2-h,h-b/2,h+b/2]
        vals=[cap(a,h+s)+cap(b,h-s) for s in knots]
        eq(min(vals+[a,b]),pair_formula(a,b,h))

V=[F(1,8),F(1),F(1)]
z=[F(-1),F(0),F(1)]
M=sum(V)
g=sum(v*p for v,p in zip(V,z))/M
ell=[F(0),F(17,24),F(17,12)]
eq(M,F(17,8));eq(g,F(7,17))
eq(sum(v*l for v,l in zip(V,ell)),M)
eq(sum(v**3 for v in V)/(12*M),F(1025,13056))
eq(ell[1]/M,F(1,3))
eq(F(24,17),1+F(7,17))
eq(g-F(7,17),0)
eq(F(5,8)-F(39,68),F(7,136))
for v in V: yes(v<M/2)
yes(V[0]+V[1]<M);yes(V[1]+V[2]<M)

for eps in [F(1,10000),F(1,20000),F(1,10**6),F(1,10**9)]:
    delta=[eps+(p-g)/8 for p in z]
    eq(delta,[eps-F(3,17),eps-F(7,136),eps+F(5,68)])
    f=[d/eps for d in delta]
    eq(sum(v*ff for v,ff in zip(V,f))/M,F(1))
    left=max(F(0),min(V[0],V[0]/2+delta[0]))
    right=max(F(0),min(V[2],V[2]/2+delta[2]))
    middle=cap(V[1],-delta[1])+pair_formula(V[0],V[2],-delta[1])
    eq(left,0);eq(right,F(39,68)+eps);eq(middle,right)
    yes(right<F(5,8));yes(-delta[1]<F(7,32))
    for yn in range(-50,51):
        y=F(yn,100)
        up=cap(V[1],y-delta[1])+pair_formula(V[0],V[2],y-delta[1])
        down=cap(V[1],-y-delta[1])+pair_formula(V[0],V[2],-y-delta[1])
        yes(min(up,down,F(9,8))<=middle)
    # Direct positive arithmetic parameter optimum, all-source gaps.
    own=F(5,8)+eps*ell[1]
    yes(F(1,2)+eps*ell[2]<own)
    yes(F(1,2)+34*eps<F(5,8))
    sigma=F(1025,13056)
    yes(2*sigma*eps**2<F(1,8)**2)

# Exact arithmetic normalization after a removal and finite majorants.
for a in [F(1,100),F(1,1000),F(1,10**6)]:
    for t in [F(0),F(1,10),F(1,2)]:
        r=t*a
        eq((M-a)/(M-r),1-(a-r)/(M-r))
for ln in range(1,11):
    l=F(ln,8)
    for an in range(-16,17):
        a=F(an,16)
        for bn in range(-8,9):
            b=F(bn,8)
            if l-a>=abs(b)/16:
                yes(l+a*g<=F(24,17)*l)

print(f"PASS: {checks} exact clipping, normalization, boundary-dual and escape checks")
