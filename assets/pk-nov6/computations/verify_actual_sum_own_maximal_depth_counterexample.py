"""Exact rational certificate for the ACTUAL sum-of-own-depth counterexample.
All geometry reductions and all-normal conclusions are proved in the note.
"""
from fractions import Fraction as F
from math import comb, factorial

d=8
N=d+1
b=F(1,N)
Gamma=F(d,N)**d
V=F(1,factorial(d))

# D is centrally symmetric: coordinate pairs and the total-sum pair
# are interchanged by x -> 2c_D-x. Its center is strictly interior.
cD=(F(11,36),)+(F(1,18),)*7
assert 2*cD[0]==F(11,18)
assert all(2*x==b for x in cD[1:])
assert 2*sum(cD)==F(7,18)+1
assert 0<cD[0]<F(11,18)
assert all(0<x<b for x in cD[1:])
assert F(7,18)<sum(cD)<1
# The extreme base sums still give positive x1 section length.
assert F(11,18)-F(7,18)==F(2,9)>0

# Inclusion-exclusion for E|sum_1^7 U_i-7/2| and the Fubini volume.
absmean=2*sum((-1)**k*comb(7,k)*(F(7,2)-k)**8
              for k in range(4))/factorial(8)
assert absmean==F(113149,184320)
VD=b**7*(F(11,18)-b*absmean)
assert VD==F(900611,7934371614720)
ratio=2**7*VD/(Gamma*V)
assert ratio==F(6304277,4194304)>F(3,2)

scale=F(49,50)
q=Gamma*V/(2**7*scale**8*VD)
assert q==F(163840000000000000000,209509599832532483477)
assert scale**8>=1-8*F(1,50)==F(21,25)
assert ratio*scale**8>F(63,50)>1
assert 0<q<1 and 0<scale<1
VC=(2*scale)**8*q*VD
assert VC==2*Gamma*V
cC=(2*scale*q*cD[0],)+tuple(2*scale*x for x in cD[1:])
assert cC[0]==F(11,18)*scale*q
assert all(x==scale/9 for x in cC[1:])
assert 0<cC[0]<1

eps=F(1,1000)
a=eps**8
alpha=a/V
assert alpha==F(40320,10**24)<F(1,1000)
assert scale+d*eps/2==F(123,125)<1
# Nonnegative coordinates plus this sum bound certify (A+C)/2 subset B.

ownA=a/2
ownB=Gamma*V
ownC=VC/2
assert ownC==ownB
tau=(ownA+ownB+ownC)/2
assert tau==Gamma*V+a/4

k=F(7)/(81*Gamma)
ell=F(2)/(81*Gamma)
bh=b+k*alpha
bl=b-ell*alpha
assert F(1,3)<Gamma<F(2,5)
assert 0<k<F(1,3) and 0<ell<F(1,3)
assert 0<bl<bh<1
assert 2*bh+7*bl==1

# Exact middle cap volumes, and both endpoints' strict incidence margins.
beta=eps/2-scale/9
assert eps-beta==2*scale/9+beta==eps/2+scale/9
assert bl-(eps/2+scale/9)>F(1,720)>0
# The high caps use base tilt -2: all A is in, and all C is out.
assert 2>bh and 3-d*eps>bh
assert 1-2<bh and 2*scale-2<bh
high=V*(1-bh)**8+a
low=V*(1-bl)**8
U=Gamma*V+F(2,9)*a+F(28,9)*a*a/V
assert high<=U and low<=U
assert high<tau and low<tau
assert tau-U>F(37,1500)*a>0

# Algebra behind the dimensionless Taylor estimate.
c=F(8,9)
assert 8*c**7==9*Gamma
assert 9*Gamma*k==F(7,9) and 9*Gamma*ell==F(2,9)
assert 0<c-k*alpha<c+ell*alpha<1
assert F(1,4)-F(2,9)-F(28,9)*alpha>F(37,1500)

# Endpoint A's two x1 half-caps, each of mass a/2.
# At B and C respectively, these are upper bounds on both margins.
assert 1-eps/2-2<0
assert eps/2-2<0
assert 2*scale-eps/2-4<0
assert eps/2-4<0
# Endpoint C's two x1 half-caps, each of mass Gamma V.
c1=cC[0]
assert 1-c1-2<0 and c1-2<0
assert eps-c1-4<0 and c1-4<0
assert ownA<ownC<U<tau

# The same source satisfies OC using the C centroid alone.
M=a+V+VC
OC=Gamma*M/2
assert alpha<1-2*Gamma
assert ownC>OC

print('PASS: exact rational centrally symmetric endpoint volume and scaling,')
print('actual midpoint compatibility, all thirteen cap volumes/incidences,')
print('strict actual sum-of-own-depth violation, and a separate OC certificate.')
