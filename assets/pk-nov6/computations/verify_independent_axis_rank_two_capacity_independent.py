"""Exact certificates for the independent-axis triangle-guard obstruction."""
from fractions import Fraction as F
import sympy as s

checks = 0


def check(a, b):
    global checks
    assert s.simplify(a-b) == 0, (a,b)
    checks += 1


def pos(x):
    return max(F(0),x)


sig,w,eta,x,b = s.symbols('sig w eta x b', positive=True)
kappa=(1+6*sig**4)/(1+6*sig**2)
check(kappa.subs(sig,s.Rational(1,4)),s.Rational(131,176))
check((kappa/18).subs(sig,s.Rational(1,4)),s.Rational(131,3168))

# Own cap mass and every-angle comparisons.
A=1+eta*s.sqrt(1+x/3)+(eta**2/3)*(1+x/3)
cap=4*A/(9-x)
check(s.diff(cap,x),4*((9-x)*s.diff(A,x)+A)/(9-x)**2)
check(cap.subs({x:0,eta:3*w/2}),s.Rational(4,9)+2*w/3+w*w/3)
two=1-(1+b)**2/((2+b)*(1+2*b))
check(two-s.Rational(1,2),b/(2*(2+b)*(1+2*b)))
gap=s.Rational(16,35)-(s.Rational(4,9)+s.Rational(1,150)+s.Rational(1,30000))
assert gap>0
checks+=1

# Exact ramp profile integral and capacity simplification.
profile_mean=s.Rational(1,3)+s.Rational(1,9)+w/3
check(profile_mean,s.Rational(4,9)+w/3)
upper=(s.Rational(4,9)+w/3+4*sig/3)/(1+4*sig)
check(s.Rational(4,9)-upper,(4*sig/9-w/3)/(1+4*sig))
check(upper.subs({sig:s.Rational(1,4),w:s.Rational(1,1000)}),
      s.Rational(7,18)+s.Rational(1,6000))
assert s.Rational(7,18)+s.Rational(1,6000)<s.Rational(4,9)
checks+=1

# All cross-polytope integer points, exact guard containment and canonical margins.
from itertools import product
P={z for z in product(range(-1,2),repeat=3) if sum(abs(t) for t in z)<=1}
assert len(P)==7
checks+=1
vertices=[(F(2),F(-1)),(F(-1),F(2)),(F(-1),F(-1))]
sigma=F(1,4)
width=F(1,1000)
guards=[]
for vx,vy in vertices:
    D=[((1-sigma)*vx+sigma*x,(1-sigma)*vy+sigma*y) for x,y in vertices]
    guards.append(D)
    for xx,yy in D:
        assert xx>=-1 and yy>=-1 and xx+yy<=1
        checks+=1
normals=[(F(1,3),F(0)),(F(0),F(1,3)),(F(-1,3),F(-1,3))]
for i,u in enumerate(normals):
    for j,D in enumerate(guards):
        for xx,yy in D:
            margin=u[0]*xx+u[1]*yy
            if i==j:
                assert margin+1>0 and margin-1<=-width
            else:
                assert margin<=-width
            checks+=1

# Global max-vertex quota support inequality for many exact normals.
for aa in range(-10,11):
    for bb in range(-10,11):
        if aa==bb==0: continue
        vals=[aa*xx+bb*yy for xx,yy in vertices]
        M=max(vals)
        assert M>0 and min(vals)>=-2*M
        i=vals.index(M)
        for xx,yy in guards[i]:
            assert aa*xx+bb*yy>=(1-3*sigma)*M>0
            checks+=1

# Hinge tests of the exact end-strip convex-order inequality (the proof in
# the note covers every convex function, not just this finite set).
def integral_hinge(lo,hi,k):
    return (pos(hi-k)**2-pos(lo-k)**2)/2

for sigma in [F(1,100),F(1,20),F(1,4),F(1,2)]:
    for kk in range(-10,31):
        k=F(kk,20)
        ends=integral_hinge(F(0),sigma,k)+integral_hinge(1-sigma,F(1),k)
        whole=integral_hinge(F(0),F(1),k)
        assert ends>=2*sigma*whole
        checks+=1

print(f'PASS: {checks} exact rank-two quota, all-angle, field-cost, and capacity certificates')
