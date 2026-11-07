from fractions import Fraction as F

# Check finite index bookkeeping and exact parameter coefficients.
# The note proves all s symbolically and all real halfspace parameters
# by the explicit transport injection, not by these sample checks.
for s in range(1,101):
 r,R,L=4*s+2,7*s+4,4*s+2
 M=2*(2*R+1)+4*(2*r+1)+6*(2*s+1)
 T=2*(2*r+1)+4*(2*s+1)
 assert M==72*s+44 and T==24*s+14
 assert 2*R+1<T and 3*(2*s+1)<T
 lower={2*j for j in range(2*s+1)}
 middle={2*j+1 for j in range(2*s+1)}
 upper={j+L for j in range(2*s+1)}
 assert not(lower&middle or lower&upper or middle&upper)
 assert lower|middle|upper==set(range(6*s+3))
 assert -R-s<=0 and 6*s+2<=R-s
 assert sum(range(3*s+3,5*s+3))==s*(8*s+5)
 assert (2*s+1)*L-s*(8*s+5)==3*s+2
 assert 12*s+10+6*(2*s+1)==T+2
 assert F(T,M)==F(1,3)-F(2,3*M)>F(1,8)
print('PASS: exact index injection, coefficient identities, and depth constants')
