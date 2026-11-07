"""Exact simplex/cube section-measure and containment certificates."""
from fractions import Fraction as F
import sympy as s

checks=0
def eq(v):
    global checks
    assert s.simplify(v)==0, v
    checks+=1
def truth(v):
    global checks
    assert v
    checks+=1

for d in range(2,21):
    N=d+1
    r=F(d,N)
    beta=r**d
    jpower=r**(d-1)/N
    truth(r**(d-1)-beta==jpower)
    truth(r*jpower==beta/N)
    # (d*s)^(d-1) > beta, precisely reflected scale-correct failure.
    lhs=(d**(d-1))*jpower
    truth(lhs==beta if d==2 else lhs>beta)
    if d>=3:
        truth(F(d,d-1)**(d-1)>2)

t=s.symbols('t',positive=True)
r1=(1-t)/4
r3=t/2
Jx=s.sqrt(r3)
Jz=r1/s.sqrt(r3)
eq(Jx*Jz-r1)
eq(Jx**2-r3)
a1=(3-t)/4
a3=(1+t)/2
Ax=s.sqrt(a3)
Az=a1/s.sqrt(a3)
eq(Ax*Az-a1)
eq(Ax**2-a3)
eq(Az-(3-t)/(2*s.sqrt(2*(1+t))))

# Fixed rational weights; full cap facets, body traces and section weights.
w=[s.Rational(12,25),s.Rational(12,25),s.Rational(1,25)]
eq(sum(w)-1)
AA=[(1+v)/2 for v in w]
RR=[v/2 for v in w]
for i in range(3):
    full=sum(w[k]*(1 if i==k else s.Rational(1,2)) for k in range(3))
    eq(full-AA[i])
    eq(AA[i]-s.Rational(1,2)-RR[i])

Al=[s.sqrt(13)/5,s.sqrt(13)/5,37/(10*s.sqrt(13))]
Jl=[s.sqrt(2)/10,s.sqrt(2)/10,6*s.sqrt(2)/5]
for i in range(3):
    eq(s.prod(Al[k] for k in range(3) if k!=i)-AA[i])
    eq(s.prod(Jl[k] for k in range(3) if k!=i)-RR[i])
eq(Al[2]**2-s.Rational(1369,1300))
eq(Jl[2]**2-s.Rational(72,25))
truth(Al[2]**2>1)
truth(Jl[2]**2>s.Rational(1,2))
eq(s.prod(Al)-37*s.sqrt(13)/250)
eq(s.prod(Jl)-3*s.sqrt(2)/125)

# W=1/2 on every rational boundary point not on a coordinate halfplane.
grid=[F(k,10) for k in range(11) if k!=5]
wf=[F(12,25),F(12,25),F(1,25)]
for x in grid:
    for y in grid:
        for z in grid:
            if not any(v in (0,1) for v in (x,y,z)):
                continue
            load=sum(wf[i]/2*((v<F(1,2))+(v>F(1,2)))
                     for i,v in enumerate((x,y,z)))
            truth(load==F(1,2))

print(f'{checks} exact Blaschke section-containment checks PASS')
