"""Exact arithmetic for the four oblique caps and both surgery paths."""
from fractions import Fraction as F
caps=((F(1),F(-1,2),F(0)),(-F(1),F(-1,2),F(1)),(F(1),F(1,2),F(-3,2)),(-F(1),F(1,2),F(-1,2)))
def length_cap(z,I,L):
 lo,hi=I;u,a,b=L;cut=-(a*z+b)/u
 return max(F(0),hi-max(lo,cut)) if u>0 else max(F(0),min(hi,cut)-lo)
def masses(I):return tuple(sum(length_cap(z,I[z],L) for z in range(4)) for L in caps)
unit=(F(0),F(1))
assert masses([unit]*4)==(F(3,2),)*4
for t in (F(0),F(1,10),F(1,2),F(1)):
 for lo in (F(0),(1-t)/2,1-t):
  J=(lo,lo+t)
  assert masses([J,unit,unit,unit])==(t+F(1,2),t+F(1,2),F(3,2),F(3,2))
  assert F(3,2)/(3+t)>=F(3,8)
  if t<1:assert F(3,2)/(3+t)>F(3,8)
 J=((1-t)/2,(1+t)/2)
 assert masses([J,unit,unit,J])==(t+F(1,2),)*4
 assert (t+F(1,2))/(2+2*t)==(1+2*t)/(4*(1+t))
print('PASS: exact cap traces, location-independent endpoint shrink, and paired-endpoint deletion formulas.')

for m in range(2,12):
 n=2*m;jl=m-1;jr=m
 C=((F(1),F(-1),F(jl)-F(1,2)),(-F(1),F(-1),F(jl)+F(1,2)),(F(1),F(1),-F(jr)-F(1,2)),(-F(1),F(1),-F(jr)+F(1,2)))
 for t in (F(0),F(1,5),F(1)):
  J=((1-t)/2,(1+t)/2)
  intervals=[J]+[unit]*(n-1)
  costs=tuple(sum(length_cap(z,intervals[z],cap) for z in range(n)) for cap in C)
  assert max(costs)==m-F(1,2)
  intervals[-1]=J
  costs=tuple(sum(length_cap(z,intervals[z],cap) for z in range(n)) for cap in C)
  assert costs==(m-F(3,2)+t,)*4
  assert (m-F(3,2)+t)/(n-2+2*t)==(2*m-3+2*t)/(2*(2*m-2+2*t))
print('PASS: general even-count cap formulas and both exact normalized paths.')
