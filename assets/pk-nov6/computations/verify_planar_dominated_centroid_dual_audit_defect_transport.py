"""Independent exact arithmetic for the proved planar dual certificate."""
from fractions import Fraction as F
from random import Random
c=F(6144,22745)
assert F(1,3)*(3*F(3,2)**3+2*F(9,16)**3)==F(7155,2048)
assert 2*(F(7155,2048)-F(2,3))==F(17369,3072)
assert (F(17369,3072)-2+F(15,4))/2==1/c
assert 5*c-F(4,3)==F(1180,68235)
assert (2*c-F(1,3))/(F(1,3)-c)==F(14119,4313)
phi=lambda r:r*r-F(2,3)*r**3
rng=Random(300929);checks=5;feasible=0
for _ in range(5000):
 x=F(rng.randint(10,35),10);y=F(rng.randint(10,35),10);z=F(rng.randint(0,20),20)
 for r,b in [(x,F(3,2)),(y,F(3,2)),(z,F(9,16))]:
  assert b**3/3-phi(r)-(b-1)*r*r==(r-b)**2*(2*r+b)/3>=0
  checks+=1
 if phi(x)+2*phi(y)+2*phi(z)>=F(2,3):
  feasible+=1
  assert (x*x+2*y*y+2*z*z-2)/(1+z*z)<=1/c
  checks+=1
print(f'PASS: {checks:,} exact dual checks, including {feasible} feasible scalar samples')
