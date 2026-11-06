"""Exact tests of the proved sharp E/T comparison and its profile identities."""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial

checks=0
def check(ok):
    global checks
    assert ok
    checks+=1

def integrate_polynomial(coeff,left,right,extra=0):
    return sum(c*(right**(j+extra+1)-left**(j+extra+1))/F(j+extra+1)
               for j,c in enumerate(coeff))

def power_line(slope,intercept,power):
    return [F(comb(power,j))*slope**j*intercept**(power-j)
            for j in range(power+1)]

def rational_kernel_integral(coeff,left,right,C,D,d):
    """Integral poly(t)/(C-D*t)^(d+1); degree poly <= d-1."""
    def primitive(t):
        v=C-D*t
        result=F(0)
        for i,c in enumerate(coeff):
            for j in range(i+1):
                result-=c*comb(i,j)*C**(i-j)*(-1)**j*v**(j-d)/(D**(i+1)*F(j-d))
        return result
    return primitive(right)-primitive(left)

# Exact infinite-cone positive-cap normalization; full weighted integral
# uses r=t/(1+t), which becomes integral_0^1 r^(d-1)=1/d.
for d in range(2,21):
    B=F(d+1)
    c=F(d)/B**d
    poly=power_line(F(-1),B,d-1)
    check(c*integrate_polynomial(poly,F(0),B)==1)
    check(c*integrate_polynomial(poly,F(0),B,1)==1)
    check(c/F(d)==1/B**d)
    check(B**(d+1)*c/F(d)==B)

# Actual convex bodies of revolution with four-knot concave section roots.
# Their common (d-1)-ball factor cancels from every comparison.
profiles=0
for L,V in product((1,2),(2,3)):
    knots=list(map(F,(-L,0,1,V)))
    for h0,h1,h2,h3 in product(range(4),range(1,4),range(1,4),range(4)):
        heights=list(map(F,(h0,h1,h2,h3)))
        slopes=[(heights[i+1]-heights[i])/(knots[i+1]-knots[i]) for i in range(3)]
        if not (slopes[0]>=slopes[1]>=slopes[2]):
            continue
        profiles+=1
        for d in range(2,8):
            polys=[power_line(slopes[i],heights[i]-slopes[i]*knots[i],d-1)
                   for i in range(3)]
            T=sum(integrate_polynomial(polys[i],knots[i],knots[i+1]) for i in (1,2))
            first=sum(integrate_polynomial(polys[i],knots[i],knots[i+1],1) for i in (1,2))
            mu=first/T
            B=F(d+1)
            check(T>0 and 0<mu<V)
            check(F(V)/mu<=B)
            check(B+1-F(V)/mu>=1)
            energy_trial=B**(d+1)*sum(
                rational_kernel_integral(polys[i],knots[i],knots[i+1],B+1,1/mu,d)
                for i in range(3))
            check(0<energy_trial<B*T)

# Interval formulas and their positive optimal denominators.
for l,r in product([F(j,3) for j in range(1,25)],repeat=2):
    a=(r-l)/(2*l*r)
    E=4*l*r/(l+r)
    T=2*min(l,r)
    check(1-a*l>0 and 1+a*r>0)
    check((l+r)/((1-a*l)*(1+a*r))==E)
    check(T<=E<2*T)
    check((E==T)==(l==r))

# Every dimension of the exact simplex boundary family.
for d in range(1,18):
    V=F(1,factorial(d))
    for j in range(1,25):
        eps=F(1,(d+1)*j)
        lam=[1-d*eps]+[eps]*d
        L=[1/((d+1)*x) for x in lam]
        check(sum(x*y for x,y in zip(lam,L))==1)
        # Sum of transformed vertices is zero in every coordinate.
        for k in range(d):
            transformed=sum((F(1 if i==k+1 else 0)-eps)/L[i] for i in range(d+1))
            check(transformed==0)
        det_ratio=F(1)
        for ell in L:
            det_ratio/=ell
        E=V*det_ratio
        T=V*((d+1)*eps)**d
        check(E/T==(d+1)*(1-d*eps))
        check(T<=E<(d+1)*T)
        check((E==T)==(j==1))

print(f"PASS: {checks:,} exact checks across {profiles} actual concave profiles")
