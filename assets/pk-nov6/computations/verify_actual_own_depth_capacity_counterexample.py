"""Exact actual own-depth capacity countercertificate."""
from fractions import Fraction as F

eta=F(1,2**20)
s=F(3,128)+eta
e=F(32,125)*s*s
delta=F(128,125)*eta
c=F(1,2)
gamma=F(4,9)
area_A=F(1,2)*F(4,5)*F(8,25)
a=(2-s)**2*area_A
b=s*s*area_A
M=a+b+c
assert b/c==e
assert a/c==1+e-delta
assert M/c==2+2*e-delta
assert e>delta>0
assert a>c>b>0
assert max(a,b,c)<M/2
assert gamma*(M/2-a)==F(1,9216000)

k=F(2,3)-eta
p=F(1,3)+eta
h=F(13,40)
B=F(8,25)*(1-s)
assert 0<k<F(2,3)
assert p==1-k
assert k-p-h==F(1,120)-2*eta>0
assert F(8,25)<h<F(1,3)

# A: exact endpoint maxima and middle-centroid incidence.
assert (2-s)*F(8,25)-B==F(8,25)<h
assert s*F(8,25)+B==F(8,25)<h
assert F(1,3)>=h
# B: left excluded, right included.
assert 2>k
assert F(4,5)*s-2<k
# C: left excluded, right included.
assert F(4,5)*(2-s)-2<p
assert 2>p

cap_A=gamma*c
cap_B=cap_C=c*k*k+gamma*b
assert (gamma*a-cap_B)/c==F(988,1125)*eta-eta*eta>0
assert cap_A<gamma*a
assert cap_B<gamma*a<gamma*M/2

# The larger centroidal triangle witnessing each constrained own-depth max.
r=F(3,2)*k
assert 0<r<1
assert gamma*c*r*r==c*k*k
q_B=(k/2,k/2)
q_C=(1-k,k/2)
assert sum(q_B)==k
assert q_C[0]==p and sum(q_C)<=1

print("Exact actual own-depth capacity counterexample verified; deficit = 1/9216000.")
