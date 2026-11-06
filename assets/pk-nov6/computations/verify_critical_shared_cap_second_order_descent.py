"""Exact all-d second derivatives and actual rational planar critical budgets."""
import sympy as S
from fractions import Fraction as Q

d = S.symbols("d", integer=True, positive=True)
t = S.symbols("t")
A = (d-1)/3
B = (d-1)*(2*d+3)/(6*(d+1))
L = 1+B*t*t
h = d/(d+1)
g = 1/(d+1)
s = A*t*t+t
m = L**(d-1)*(L-d*s)
f0 = L**(d-1)*((h-d*s)/h)**d/(L-d*s)**(d-1)
fi = (L-d*s)*((L-g)/h)**d/(L-s)
expected = [d*(d-1)/(6*(d+1)), -d*(d-1)/6, -(d-1)/6]
for expression, coefficient in zip((m,f0,fi), expected):
    assert S.simplify(expression.subs(t,0)-1) == 0
    assert S.simplify(S.diff(expression,t,2).subs(t,0)/2-coefficient) == 0
assert S.simplify(S.diff(f0,t).subs(t,0)+2*d) == 0
assert S.simplify(S.diff(fi,t).subs(t,0)+(d-1)) == 0

# The planar witness includes every actual original fiber and fixed cap.
r = Q(1,2)
step = Q(1,10)
q = step*step/3
length = 1+Q(7,18)*step*step
vertices = [
    [(q+step,q+step),(length,Q(0)),(Q(0),length)],
    [(q-step,q-step),(length,Q(0)),(Q(0),length)],
]
for triangle in vertices:
    for v in triangle:
        image = tuple((1-r)*Q(1,3)+r*x for x in v)
        assert min(image)>0 and sum(image)<1
pair_mass = length*(length-2*q)
pair0 = sum(length*(Q(2,3)-2*s)**2/(2*(length-2*s))
            for s in (q+step,q-step))
pair1 = sum((length-2*s)*(length-Q(1,3))**2/(2*(length-s))
            for s in (q+step,q-step))
mass = Q(1,2)+r*r*pair_mass
cap0 = Q(2,9)+r*r*pair0
cap1 = Q(2,9)+r*r*pair1
assert mass == Q(1944713,2592000) > Q(3,4)
assert cap0 == Q(18538760053,55663650000) < Q(1,3)
assert cap1 == Q(2772709845551,8323432992000) < Q(1,3)
assert cap1 > cap0
assert cap1/mass == Q(2772709845551,6244864330313)
assert Q(4,9)-cap1/mass == Q(25068711293,56203778972817) > 0
assert Q(1,2)>mass/2

# Exact rational diagnostics beyond d=2. The analytic proof gives a positive
# neighborhood for every d and r; these tests do not replace that argument.
count = 0
for dim in range(2,13):
    ad = Q(dim-1,3)
    bd = Q((dim-1)*(2*dim+3),6*(dim+1))
    shift = Q(1,100*dim)
    aa = ad*shift*shift
    ll = 1+bd*shift*shift
    hh = Q(dim,dim+1)
    gg = Q(1,dim+1)
    vols=[];caps0=[];capsi=[]
    for ss in (aa+shift,aa-shift):
        assert ss<gg<ll and ll-dim*ss>0
        vols.append(ll**(dim-1)*(ll-dim*ss))
        caps0.append(ll**(dim-1)*(hh-dim*ss)**dim/(ll-dim*ss)**(dim-1))
        capsi.append((ll-dim*ss)*(ll-gg)**dim/(ll-ss))
        # Actual endpoints at r=1/2 remain inside the centered middle simplex.
        for v in [tuple([ss]*dim)]+[
                tuple(ll if j==i else Q(0) for j in range(dim))
                for i in range(dim)]:
            image = tuple(gg/2+x/2 for x in v)
            assert min(image)>0 and sum(image)<1
    assert sum(vols)>2
    assert sum(caps0)<2*hh**dim
    assert sum(capsi)<2*hh**dim
    count += 1
print(f"PASS: symbolic all-d coefficients, every planar critical budget, "
      f"actual midpoint compatibility, and {count} higher-dimensional rational paths")
