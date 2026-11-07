"""Exact certificates for iid-averaging auxiliary statements (not OC)."""
from fractions import Fraction as F
from math import comb, factorial

# K={0<=x<=1,0<=y<=h(x)}, h(x)=1+x up to1/2, then3(1-x).
area=F(1,2)+F(1,8)+F(3,2)-F(3,8)-F(3,4)
assert area==1
# First x moment from integrating x+x² and 3x-3x² on the two intervals.
m=F(1,8)+F(1,24)+(F(3,2)-1)-(F(3,8)-F(1,8))
assert m==F(5,12)
single=1-m-m*m/2
assert single==F(143,288)

# For 1/2<=s<=1, exact convolution CDF from truncated-power convolution.
s=2*m
cdf=s*s/2+s**3/3+s**4/24-F(4,3)*(s-F(1,2))**3-F(1,3)*(s-F(1,2))**4
double=1-cdf
assert double==F(15343,31104)
assert double-single==-F(101,31104)
assert double>F(4,9)

def simplex_iid_cap(d):
    a=F(2,d+1)
    cdf=F(0)
    for i in range(d):
        for j in range(d):
            cdf+=(-1)**(i+j)*comb(d-1,i)*comb(d-1,j)*a**(i+j+2)*F(factorial(i)*factorial(j),factorial(i+j+2))
    return 1-d*d*cdf

assert simplex_iid_cap(1)==F(1,2)
assert simplex_iid_cap(2)==F(115,243)
print('All exact checks passed.')
print('Directional single/double cap masses:',single,double)
for d in range(1,7):
    print('Simplex iid cap, d=',d,':',simplex_iid_cap(d))
