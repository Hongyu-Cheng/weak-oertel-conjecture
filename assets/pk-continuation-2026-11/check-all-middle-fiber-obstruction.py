#!/usr/bin/env python3
"""Exact certificates for the actual d=15 all-middle-fiber obstruction.
All assertions use integers or fractions; no numerical optimization or roots.
"""
from fractions import Fraction as F
from math import comb

d,N,m,k=15,16,13,3
R=sum((-1)**l*comb(m,l)*(N-l)**d for l in range(m+1))
assert R==59717129472000
p=F(R,N**d)
assert p==F(29158754625,562949953421312)
rho_power=F(1,2)**d/p
assert rho_power==F(17179869184,29158754625)
assert 0<rho_power<F(63,64)**d<1
certificate=R*63**15-2**135
assert certificate==14816205358430717469293609548549415237632>0
assert m*F(1,32)+k*F(19,96)==1

Gamma=F(15,16)**15
assert F(379,1000)<Gamma<F(1,2)
assert Gamma>F(3,8)
epsilon=F(1,2)**12
a=epsilon**15
assert a==F(1,2)**180
assert epsilon<F(1,64)
assert epsilon<F(1,1920)  # < (1-rho)/(2d), using 1-rho>1/64.
assert a<Gamma/2
assert 2*a/Gamma<F(1,4096) # Strict localization inside all 13 threshold gaps.
c=F(189,1000)
first_derivative=(16*c-3)/(16*Gamma)
assert first_derivative>F(3,1000)
assert Gamma/2-c>F(1,2000)
assert 13*c*c+3*(1-c)**2<4
assert F(13,16)+3<4
assert F(256,9)<29
assert F(4*29,15)<8
assert a<F(3,4000)
assert F(3,1000)*a-4*a*a>0
# A pyramid apex would meet 28 facets. Every vertex instead meets 15.
assert N+m==29 and m+k-1==15 and (N+m)-(m+k-1)==14
print('All exact rational and combinatorial certificates passed.')
print('Volume numerator:',R)
print('Positive root-bound certificate:',certificate)
