from fractions import Fraction as F
from math import comb, prod

# d=4 five-fiber certificate.
w={z:z**4 for z in range(1,6)}
t={1:1,2:16,3:81,4:18,5:0}
assert all(0<=t[z]<=w[z] for z in w)
assert sum(t.values())==116
assert sum((z-3)*t[z] for z in w)==0
assert sum(w[z]*max(0,4-z) for z in w)==116
cs=[comb(4,z-1) for z in range(1,6)]
assert sum(cs)==16 and sum(z*c for z,c in zip(range(1,6),cs))==48
P=prod(F(16*z**4,c)**c for z,c in zip(range(1,6),cs))
assert P==2**90*3**18*5**4
assert 2**42*3**18*5**4>29**16
assert P>232**16
assert 2**4<18<3**4

# d=40 three-fiber rational formula and strict gap.
T=1+2*F(9,10)**40
E=1+2*F(99,100)**20
assert 8*9**20<10**20
assert E>=F(13,5)>F(5,2)>2*T

# Finite explicit member of the all-dimension construction.
N,L=2,10
S2=sum(k*k for k in range(1,N+1))
assert L>=2*S2
E_lower=F(2*N+1,2)
T_upper=1+F(N*(N+3),2*2**L)
assert E_lower>2*T_upper
print('PASS: exact five-fiber and three-fiber gaps; finite unbounded-family certificate')
