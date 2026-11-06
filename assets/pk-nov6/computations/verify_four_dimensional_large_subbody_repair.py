from fractions import Fraction as F

alpha=F(17,100)
beta=F(199999,1000000)
m=F(83,100)**4-F(800001,1000000)**4
assert F(1,16)<m<F(101,200)**4
# Hence 0<h=2*m^(1/4)-1<1/100, a=h^4<10^-8,
# and r=2-m^(-1/4)<2/101, with all quantities positive.
eps=F(1,10**8)
v1=F(37,200)
vo=F(163,800)
assert v1+4*vo==1
assert 2*vo-F(2,101)*F(83,100)>0
assert 2*(v1-alpha)-F(2,101)*(beta-alpha)>0
assert 2*(beta-v1)-F(2,101)*(beta-alpha)>0
assert F(411,2000)/(1+eps)>F(1,5)
assert F(83,400)<F(1,4)

Gamma=F(4,5)**4
for t in (F(6,25),F(13,50)):
    ratio=256*t*((1-t)/3)**3
    assert ratio<F(999,1000)
assert 256*F(6,25)*(F(19,25)/3)**3==F(3511808,3515625)
assert 256*F(13,50)*(F(37,50)/3)**3==F(10535824,10546875)
far_gap=F(1000,999)*Gamma*(1-20*eps)-eps-Gamma*(1+eps)
assert far_gap==F(25593999881,62437500000000)>0
assert 3*Gamma-1==F(143,625)>0

v_margin=F(6,25)*v1/(F(1,5)-eps)+F(19,25)*vo/F(1,5)
assert v_margin==F(79699996903,79999996000)<1
assert F(5,6)<F(99,100)
assert 36*eps+88*eps**2+64*eps**3<F(1,80)
assert F(83,80)+F(1,80)==F(21,20)
assert 1-F(41,20)*Gamma==F(501,3125)>0

# Exact expansion of (1-4t)(1+t)^3.
coeff=[F(0)]*5
for i,a in enumerate((1,-4)):
    for j,b in enumerate((1,3,3,1)):
        coeff[i+j]+=a*b
assert coeff==[1,-1,-9,-11,-4]

multi_gap=F(3,4)**3-41*eps-Gamma*(1+eps)
assert multi_gap==F(767161619,62500000000)>0
assert 1-eps>Gamma*(1+eps)
print('PASS: exact all-cap repair constants, reflection containment, and centroid bounds')
