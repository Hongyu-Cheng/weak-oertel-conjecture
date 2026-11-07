"""Exact certificates for Sections 6--7; no floating point."""
from fractions import Fraction as F

g=F(50,51)**50
q=1-g
T=F(11,10)*g
assert F(102,275)<g<F(2,5)
assert g<F(41,110)
assert T<F(41,100)<F(11,25)
assert q>F(3,5) and q<F(173,275) and q*q<F(2,5)
assert F(49,50)**50>F(9,25)
assert F(39,40)**50>F(7,25)
assert F(128,275)>F(11,25)>T
assert F(117,275)>F(41,100)>T
c=F(1,51)+g/(51**2*q)
cp=F(1,51)-50*g/(51**2*q)
assert F(1,51)<c<F(1,50)
assert F(1,153)<cp<F(1,102)
assert F(101,102)**50>F(1,2)
assert F(152,153)**50<F(3,4)
assert 3*(153**2+50*153+1275)-4*153**2==3366>0
assert g+F(1,20)>T
assert F(5,8)*F(253,255)**50>F(41,100)
assert (F(1,51)-F(41,100)*F(125,10404))/F(59,100)==F(15275,613836)<F(1,40)
assert F(1,40)-F(15275,613836)==F(709,6138360)
assert F(2,3)*F(101,102)**50<T
assert 33*100**50-20*101**50==1073635631223620015615759523134059447637507157430412158495462006059818435467410182961787007754899980>0
print('PASS: exact facet-normal and oblique-family calibration inequalities verified.')
