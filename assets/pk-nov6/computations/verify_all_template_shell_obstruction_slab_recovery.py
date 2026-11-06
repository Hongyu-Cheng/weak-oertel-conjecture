from fractions import Fraction as F
from math import comb
checks=0
def check(v):
 global checks
 assert v
 checks+=1
d=200;m=100;a=F(21,20);eps=F(1,1000)
k=((a+1)**2/(4*a))**m;t=a**(-m);g=F(d,d+1)**d
check((a+1)**2/(4*a)==F(1681,1680))
check(1<k<F(84,79)<F(16,15))
check(sum(F(comb(100,j),20**j) for j in range(7))==F(4209933,40000)>100)
check(0<t<F(1,100))
check(g>F(4,11))
check(sum(F(1,z) for z in [1,1,2,6])==F(8,3))
check(F(8,3)+F(5,96)==F(87,32)<F(11,4))
L1=(a+1)/2;facet=k/L1;height=d*eps/facet
check(facet*height/d==eps)
check(k/2+eps+t<F(1633,3000))
check(g*(2+k+eps)/2>F(6,11))
check(F(6,11)-F(1633,3000)==F(37,33000))
check(g*(2+k+eps)/2-(k/2+eps+t)>F(37,33000))
check((k+1)/2>(k+eps+2)/4>=g*(k+eps+2)/2)
for n in range(1,13):
 check(g*(2**(n-1)*(2+k+eps))/2**n==g*(2+k+eps)/2)
print(f'{checks} exact checks PASS')
