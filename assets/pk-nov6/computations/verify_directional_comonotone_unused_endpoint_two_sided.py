from fractions import Fraction as F
from itertools import product
import sympy as sp

checks = 0

def check(condition):
    global checks
    assert condition
    checks += 1

def clamp(t):
    return max(F(0), min(F(1), t))

# The explicit actual compatible triangle certificate.
e = F(1, 100)
a = e * e
gK = F(1, 3)
gA = 1 - e + e * gK
gM = (gA + gK) / 2
g = (gK + 2*a*gM)/(1 + 2*a)
check(g == F(166733, 500100))
check(2*g - 1 == -F(83317, 250050))
check(2*g - 1 < 1-e)
cap = (1-g)**2 + a
target = F(2, 9)*(2+a)
check(cap == F(11115856669, 25010001000))
check(target == F(6667, 15000))
check(target-cap == F(159443, 15631250625))
check(target > cap)

# Exact d=2 cone-profile minimization: all candidate proper stationary
# points, support transitions, and saturated limiting states.
for aa, bb, wa, wb, mr in product(
    [F(1,4),F(1),F(2)], [F(1),F(2),F(5)],
    [F(1,3),F(1),F(3)], [F(1,2),F(2),F(4)],
    [F(0),F(1,5),F(1,2),F(4,5),F(1)]):
    if aa > bb:
        continue
    c=(wa+wb)*mr
    den=wa*wa/aa+wb*wb/bb
    const=(wa+wb)**2/den
    expected=min(aa,const*mr*mr)
    dstar=c*(wa*wa/aa)/den
    candidates=[F(0),wa,c,c-wb,dstar,min(0,c-wb)-1,max(wa,c)+1]
    values=[aa*clamp(x/wa)**2+bb*clamp((c-x)/wb)**2 for x in candidates]
    check(min(values)==expected)
    if const*mr*mr < aa:
        check(0 <= dstar < wa)
        check(0 <= c-dstar < wb)

# Exact all-d homothetic-width coefficient: no radicals are needed when
# the endpoint volumes are d-th powers and widths scale with their roots.
for d, r, s in product(range(2,15),[F(1,10),F(1,2),F(1)],[F(1),F(2)]):
    aa,bb=r**d,s**d
    vstar=((r+s)/2)**d
    # Holder equality splits the support deficit equally in physical
    # height when widths are r,s and volumes are r^d,s^d.
    for mr in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
        c=(r+s)*mr
        proper=(c/2)**d*2
        check(proper==2*vstar*mr**d)
        if proper < aa:
            check(c/2 < r and c/2 < s)
        check(min(aa,proper) <= aa)

# The rank-coordinate power mean has the printed rank-one Hessian.
vv,ww,rr,ll=sp.symbols('v w r l', positive=True)
SS=(1-ll)*vv**rr+ll*ww**rr
PP=SS**(1/rr)
factor=(rr-1)*ll*(1-ll)*SS**(1/rr-2)*vv**(rr-2)*ww**(rr-2)
for actual,expected in [
    (sp.diff(PP,vv,2),factor*ww**2),
    (sp.diff(PP,ww,2),factor*vv**2),
    (sp.diff(PP,vv,ww),-factor*vv*ww),
]:
    check(sp.simplify(actual-expected)==0)

# Uniform actual simplex family, including exact source and support status.
for d in range(2,41):
    for scale in [1,2,5]:
        eps=F(1,10*d*scale)
        aa=eps**d
        gamma=F(d,d+1)**d
        gg=(1+aa*(d+2-d*eps))/((d+1)*(1+2*aa))
        check(0<gg<F(1,2))
        check(2*gg-1<1-eps)
        qq=(1-gg)**d+aa
        check(qq==gamma*((1+aa*(1+eps))/(1+2*aa))**d+aa)
        check(gamma*(1+aa/2)-qq>=F(3,50)*aa)
        check(gamma*(d+F(77,200))-1>=F(3,50))

print(f'{checks} exact checks PASS')
