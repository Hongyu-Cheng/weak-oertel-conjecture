"""Exact rational-arithmetic verification of the affine-density certificate.

Square-root factors are represented by rational coefficients of 1/sqrt(3).
No numerical integration is used.
"""
from fractions import Fraction as Q

# x-marginal moments on [-1,1/2].
a,b=Q(-1),Q(1,2)
Z=(b+b*b/2)-(a+a*a/2)
mx=(b*b/2+b*b*b/3)-(a*a/2+a*a*a/3)
assert Z == Q(9,8) and mx == 0

# At u=k/3, sqrt(k) is integral for k=1,4.
def x_primitive(k, rootk):
    return (Q(6,7)*Q(k**3*rootk,27)
            -Q(8,5)*Q(k**2*rootk,9)
            +Q(2,3)*Q(k*rootk,3))

def s_primitive(k, rootk):
    return Q(3,4)*(Q(6,5)*Q(k**2*rootk,9)
                   -Q(2,3)*Q(k*rootk,3))

ball_x=x_primitive(4,2)-x_primitive(1,1)
mean_s=(s_primitive(4,2)-s_primitive(1,1))/Z
assert ball_x == Q(8,105)
assert mean_s == Q(232,135)
ball_y_q2=mean_s/2
assert ball_y_q2 == Q(116,135)
assert -12*ball_x+ball_y_q2 == Q(-52,945)

# Endpoint x'=x sqrt(1+2x/3), squared; signs are opposite.
assert a*a*(1+2*a/3) == b*b*(1+2*b/3) == Q(1,3)

# det D[s(x)(x,y)] = s^2 + x/3 = 1+x.
for x in (Q(-1),Q(-3,4),Q(0),Q(1,2)):
    assert 1+2*x/3+x/3 == 1+x

print('Exact affine-density Ball centroid certificate verified.')
print('g_f(q=1)=(0,0); sqrt(3)*g_B(q=1)=(8/105,0).')
print('u.g_f(q=2)=1/2; sqrt(3)*u.g_B(q=2)=-52/945.')

# A strict sign reversal normal to the centered vertical section.
k=Q(199,100)
b=(k*k-3)/2
Z=(1+b)**2/2
A=lambda t: Q(2,63)*t**7-Q(8,45)*t**5+Q(2,9)*t**3
original_x=(2*b-1)/3
transformed_x_sqrt3=Q(9,8)*(A(k)-A(1))/Z
assert b == Q(9601,20000)
assert original_x == Q(-133,10000)
assert transformed_x_sqrt3 == Q(16184667199,312903500000)>0
print('Strict sign reversal normal to a centered section verified.')
