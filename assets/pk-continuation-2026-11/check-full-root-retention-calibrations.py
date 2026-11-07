#!/usr/bin/env python3
"""Exact arithmetic checks for the full-root scalar obstruction and two-cut gain.
No floating-point results are mathematical premises.
"""
from fractions import Fraction as F

# d=2 asymmetric (1/10,1,1) table.
G=F(4,9); Q=1-G; W=F(21,10); target=G*W/2
assert target==F(7,15)
assert F(1,10)<F(1,9)  # sqrt(1/10)<1/3, hence M<4/9<5/9.
assert F(4,9)<Q
assert (F(3,4)+F(1,10))/2==F(17,40)<G
assert F(11,10)/3==F(11,30)<G
assert F(3,8)<G and F(1,3)<G
assert target-G==F(1,45)

# All-dimensional elementary polynomial comparison used at s>=1/2.
assert 2*F(7,11)**4+(1-F(7,11))**2==F(6738,14641)
assert F(1,2)-F(6738,14641)==F(1165,29282)>0
assert F(65,24)+F(1,100)<F(11,4)

# d=50 quantitative improvement; all certificates are rational.
G=F(50,51)**50
assert F(37,100)<G<F(3,8)
L=F(4,5)-F(63,100)**2/2-F(5,6)*F(63,100)**4
assert L==F(9,20)+F(811013,40000000)>F(47,100)
assert F(6,5)*G<F(9,20)
assert 2+F(51,50)*(1+F(11,12))<4
assert F(3,4*3**50)<F(1,1000)

# Exact failure of the two-cut all-subset full-Psi overlap consumer
# on an actual triangle target for the asymmetric table.
# First retained side lambda_1<=1/3, second lambda_2<=19/45.
a1=F(4,9); a2=F(26,45)**2
intersection=F(11,45)**2
remaining=1-a1-a2+intersection
assert remaining==F(38,135)
assert a2+F(1,10)<a1
assert 1-a1>F(4,9) and 1-a2>F(4,9)
print('All exact rational assertions passed.')
