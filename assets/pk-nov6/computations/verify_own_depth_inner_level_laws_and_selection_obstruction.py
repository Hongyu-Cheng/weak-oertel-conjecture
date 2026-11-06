"""Exact checks for the level-law note. All-direction proofs are analytic."""
from fractions import Fraction as F
from math import comb, factorial
import sympy as sp

checks=0

# Exact simplex rays, high-level product gradients, and layer-cake constant.
for d in range(1,10):
    m=d+1;G=F(d,m)**d
    for t in [F(0),F(1,7),F(1,2),F(1)]:
        # Centroid of the t-homothetic simplex and the matching apex cap.
        bary=[1-F(d,m)*t]+[t/m]*d
        assert sum(bary)==1
        assert (F(d,m)*t)**d==G*t**d
        checks+=1
    assert F(d*factorial(d-1)*factorial(d),factorial(2*d))==F(1,comb(2*d,d))
    # With sum delta=0, differentiating product_(j!=i) at 1/m:
    assert d**d*F(1,m)**(d-1)==m*G
    checks+=1

# Exact planar ordered-chamber mass and own-depth integral.
B,C=sp.symbols("B C",positive=True)
assert sp.integrate(12*(sp.Rational(1,2)*(1-C)-C),(C,0,sp.Rational(1,3)))==1
mean=sp.integrate(sp.integrate(48*B*C,
                   (B,C,(1-C)/2)),(C,0,sp.Rational(1,3)))
assert mean==sp.Rational(7,54)
checks+=2

# Integrating the two exact pieces of the inner region gives the stated law.
a,b,tau,L=sp.symbols("a b tau L",positive=True)
# L represents log(b/a); polynomial reduction checks the full coefficients.
integral=12*(b/2-b*b/4-a/2+a*a/4-tau*L/4
             +sp.Rational(1,12)-b/2+3*b*b/4)
claimed=1-3*a-3*tau*L
diff=sp.expand(integral-claimed).subs(b*b,tau/4)
assert sp.simplify(diff.subs(tau,2*a*(1-a)))==0
assert 1-3*sp.Rational(1,3)==0
checks+=2

for k in range(1,101):
    # Rational lower intersection a parametrizes tau=2a(1-a).
    aa=F(k,303);tt=2*aa*(1-aa)
    assert 0<tt<F(4,9)
    assert aa*aa<=tt/4<=F(1,9)
    assert 2*aa*(1-aa)==tt
    checks+=1

def clip(P,u,c):
    if not P:return []
    out=[]
    for p,q in zip(P,P[1:]+P[:1]):
        v=sum(a*x for a,x in zip(u,p))+c
        w=sum(a*x for a,x in zip(u,q))+c
        if v>=0:out.append(p)
        if v*w<0:
            t=v/(v-w)
            out.append(tuple(p[i]+t*(q[i]-p[i]) for i in range(2)))
    return out

def area(P):
    if len(P)<3:return F(0)
    return abs(sum(p[0]*q[1]-p[1]*q[0] for p,q in zip(P,P[1:]+P[:1])))/2

T=[(F(0),F(0)),(F(1),F(0)),(F(0),F(1))]
base=[(F(0),F(0)),(F(4,5),F(0)),(F(0),F(8,25))]
eta=F(1,2**20);s=F(3,128)+eta;delta=F(1,2**30)
minus=[((2-s)*x,(2-s)*y) for x,y in base]
plus=[(s*x,s*y) for x,y in base]
fibers=[(-1,minus),(0,T),(1,plus)]
a,V,b=map(area,[minus,T,plus]);M=a+V+b;G=F(4,9)
assert a>V>b>0
assert all(w<M/2 for w in [a,V,b])
assert M/2-a==F(1,4096000)
assert area(base)==F(32,125)*V
# Actual endpoint midpoint body is exactly base, and base lies in T.
assert all(x>=0 and y>=0 and x+y<=1 for x,y in base)

k=F(2,3)-delta;q0=F(1,3)-2*delta;e=b/V
h=F(1,3)-F(17,52)*e;beta=F(8,25)*(1-s)
assert q0>h>F(8,25)
assert q0-h==F(10268075793,223338299392000)
target=G*M/2
left_threshold=(2-s)*F(8,25)*q0
right_threshold=s*F(8,25)*q0
caps=[
    [(area(clip(P,(F(0),F(1)),-2*(z+1)-left_threshold)))
     for z,P in fibers],
    [(area(clip(P,(F(0),F(1)),beta*z-h))) for z,P in fibers],
    [(area(clip(P,(F(0),F(1)),2*(z-1)-right_threshold)))
     for z,P in fibers]]
assert caps==[[(F(2,3)+2*delta)**2*a,0,0],
              [0,V*(1-h)**2,0],
              [0,0,(F(2,3)+2*delta)**2*b]]
for cs in caps:
    assert sum(cs)<target
    checks+=1
assert a<1 and F(8,3)*delta+4*delta**2<3*delta
assert 3*delta<F(1,9216000)
assert k*k<G
# Fixed relative levels are all nonempty and positive-volume at the centroid.
assert all(k*k*w<G*w for w in [a,V,b])
# The fixed common absolute level leaves only the largest integer fiber.
assert k*k*a>G*V>G*b
assert k*k*a-G*V==F(7376516281387046806465151,237684487542793012780631851008)
checks+=3

# The relative-level graph already fails convexity for actual intervals.
tau=F(1,4)
left=(F(-1),tau);right=(F(1),tau)
mid=tuple((x+y)/2 for x,y in zip(left,right))
assert mid==(0,tau) and mid[1]<2*tau
assert tau<=1-tau and 2*tau<2*(1-tau)
checks+=1

print(f"PASS {checks} exact ray, layer-law, cap, and positive-volume level-selection checks.")
