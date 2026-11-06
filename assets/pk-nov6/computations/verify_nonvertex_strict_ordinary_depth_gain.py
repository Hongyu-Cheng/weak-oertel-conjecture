"""Exact rational calibration of the proved all-normal gain, d=1."""
from fractions import Fraction as F
R=F(5,2);nu=F(1);Gamma=F(1,2);omega=F(1);k=2
L0=omega;r=Gamma*nu/L0;rho=r;L=(k+1)*L0
delta=nu*rho/(4*R)
epsilon=min(F(1,2),r/(4*R),delta/(4*R*L))
c=omega;G=min(delta/2,c*epsilon*rho/2)
g=F(5,2);m=F(1,2);y=g+epsilon*(m-g)
assert (r,delta,epsilon,G,y)==(F(1,2),F(1,20),F(1,600),F(1,2400),F(749,300))
# For endpoints [0,1], middle [0,5], exact infima over all finite tilts:
lower=y+min(2*y,1)
upper=5-y+min(2*max(1-y,0),1)
assert min(lower,upper)==F(751,300)>g+G
assert epsilon*abs(m-g)<=r/2
assert L*epsilon*abs(m-g)<=delta/2
assert g<=F(5,2) and G<=F(5,2)
# Scaled exact three-fiber formula b=1/t >=3: local (1+t)/2.
for t in (F(1,3),F(1,10),F(1,1000)):
 b=1/t
 A=t*(b+1)/2
 assert A==(1+t)/2>F(1,2)
print('PASS: exact all-normal gain calibration, threshold/slab inequalities, and vanishing-source limitation.')
