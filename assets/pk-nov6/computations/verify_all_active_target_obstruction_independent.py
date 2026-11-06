"""Exact certificates for the full-menu triangle obstruction and its free-facet payment."""
from fractions import Fraction as F
import sympy as s

checks=0
def eq(a,b):
    global checks
    assert s.simplify(a-b)==0,(a,b)
    checks+=1
def lt(a,b):
    global checks
    assert a<b,(a,b)
    checks+=1

sigma=F(1,100); h=F(1,100000); V=F(9,2)
v=V*sigma*sigma; delta=v+4*h
eq(delta,F(49,100000))
lt(13*delta,F(2,143))
lt(2*sigma*sigma+4*sigma*h,2)
lt(-F(3,4)*(1-sigma)+2*sigma+4*delta,-F(7,10))
lt(F(19,10),2*(1-sigma)-F(5,4)*sigma-4*delta)
lt(F(19,10),2-4*delta)
lt(9*(2+4*delta+h)/F(143,16),F(21,10))
lt(F(105,257),F(4,9))

z=s.symbols('z',real=True)
UA=s.Matrix([1+z/3,2*z/3]); UB=s.Matrix([2*z/3,1+z/3]); UC=s.Matrix([-1+z/3,-1-z/3])
A=s.Matrix([2,-1]); B=s.Matrix([-1,2]); C=s.Matrix([-1,-1])
Sigma=s.Matrix([[s.Rational(1,2),-s.Rational(1,4)],[-s.Rational(1,4),s.Rational(1,2)]])
for u,vertex in [(UA,A),(UB,B),(UC,C)]:
    eq(u.dot(vertex),2)
    eq((u.T*Sigma*u)[0],(1+z*z/3)/2)

t=s.symbols('t',positive=True)
thA=(4*t-1)/(6*t-1); thB=t/(6*t-1)
eq(thA+2*thB,1)
eq(2*t*(2*thB),4*t*t/(6*t-1))
eq(4*t*t/(6*t-1)-s.Rational(4,9),4*(3*t-1)**2/(9*(6*t-1)))
alpha=s.symbols('alpha',positive=True)
tval=(1+s.sqrt(1-3*alpha))/6
eq(12*tval*tval-4*tval+alpha,0)

# General simplex facet identity, tested exactly for varied rational barycentrics.
for d in range(2,9):
    # Positive r of length d+1, giving all y_i<1/d.
    for seed in range(1,20):
        raw=[(seed*(j+2)%13)+1 for j in range(d+1)]
        rr=[F(x,sum(raw)) for x in raw]
        yy=[(1-r)/d for r in rr]
        prod=F(1)
        for y in yy:prod*=y
        qq=[d**d*prod/y for y in yy]
        BB=sum(r/q for r,q in zip(rr,qq))
        theta=[(r/q)/BB for r,q in zip(rr,qq)]
        eq(sum(theta),1)
        for i in range(d+1):
            eq(sum(theta[j]*qq[j]/(d*yy[i]) for j in range(d+1) if j!=i),1/BB)
        prod_r=F(1)
        for r in rr:prod_r*=1-r
        eq(1/BB,prod_r/(1-sum(r*r for r in rr)))
        assert 1/BB>=F(d,d+1)**d
        checks+=1

print(f'PASS: {checks} exact full-menu, smoothing-bound, and simplex-facet certificates')
