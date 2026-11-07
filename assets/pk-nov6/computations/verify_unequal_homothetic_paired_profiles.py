"""Exact arithmetic calibrations; the general finite-candidate proof is in the note."""
from fractions import Fraction as F

def profile(d,a,r,s):
 m=F(d,d+1)*(1-a**(d+1))/(1-a**d)
 def tail(q):return (1-min(F(1),max(a,m+q))**d)/(1-a**d)
 def cost(t):return r**d*tail(t/r)+s**d*tail(-t/s)
 events=[r*(a-m),r*(1-m),s*(m-1),s*(m-a),m*(s-r)/2]
 vals=[r**d,s**d]+list(map(cost,events))
 return min(min(vals),r**d+s**d-max(vals)),cost,tail,events
# Exact failed inequality, including a fully proper perturbation.
d=2;r=F(1);s=F(11,10);t=F(-11,30)
minimum,cost,tail,events=profile(d,F(0),r,s)
assert tail(F(1,3))==0
assert cost(t)==F(91,100)
gamma=F(2,3)**2
target=min(r**2,s**2,2*gamma*((r+s)/2)**2)
assert target==F(49,50) and cost(t)<target
proper=F(-109,300)
assert F(-2,3)<proper/r<F(1,3) and F(-2,3)<-proper/s<F(1,3)
assert r**2*tail(proper/r)==F(81719,90000)
assert s**2*tail(-proper/s)==F(659,90000)
assert cost(proper)==F(41189,45000)
assert target-cost(proper)==F(2911,45000)
# The two-orientation untruncated closed profile on exact rational calibrations.
for d in range(1,9):
 for r in (F(1),F(2,3),F(7,5)):
  for ratio in (F(1),F(11,10),F(3,2),F(2),F(d+1),F(17,7)):
   s=r*ratio
   result,_,_,_=profile(d,F(0),r,s)
   reflected=r**d-(max(F(0),d*r-s)/(d+1))**d
   balanced=2*F(d,d+1)**d*((r+s)/2)**d
   assert result==min(reflected,balanced),(d,r,s,result,reflected,balanced)
# Every rational frustum profile's candidates dominate direct sample values.
# This is a guard calibration, not the completeness proof.
for d in range(1,6):
 for a in (F(0),F(1,5),F(2,3),F(9,10)):
  for r,s in ((F(1),F(11,10)),(F(3,2),F(2,3))):
   minimum,cost,_,events=profile(d,a,r,s)
   for q in list(events)+[F(k,10) for k in range(-30,31)]:
    assert cost(q)>=minimum and r**d+s**d-cost(q)>=minimum
print('PASS:91/100<49/50; proper-cap counter; exact facet-profile and frustum calibrations')
