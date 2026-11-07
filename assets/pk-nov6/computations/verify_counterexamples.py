from fractions import Fraction as Q

def interval_cap_mass(fibers, slope, intercept):
 return sum(max(Q(0), min(hi-lo, hi-slope*k-intercept)) for k,(lo,hi) in fibers.items())

# Weighted-median midpoint counterexample.
f={-1:(Q(0),Q(2)),0:(Q(0),Q(5)),1:(Q(0),Q(10,3)),2:(Q(0),Q(5,3)),3:(Q(0),Q(0))}
assert sum(hi-lo for lo,hi in f.values())==12
assert interval_cap_mass(f,Q(1,2),Q(5,2))==Q(17,6)
assert Q(17,72)<Q(1,4)

# Every midpoint counterexample.
f={0:(Q(0),Q(2)),1:(Q(0),Q(6)),2:(Q(0),Q(10)),3:(Q(0),Q(3))}
assert sum(hi-lo for lo,hi in f.values())==21
for k,y,a,b,mass in [(0,Q(1),Q(11),Q(1),Q(1)),(1,Q(3),Q(11),Q(-8),Q(5)),(2,Q(5),Q(-2),Q(9),Q(5)),(3,Q(3,2),Q(-11),Q(69,2),Q(3,2))]:
 assert y==a*k+b
 assert interval_cap_mass(f,a,b)==mass
 assert mass<Q(21,4)

# B,T,B triangular centroid counterexample.
gamma2=Q(2,3)**2
assert gamma2==Q(4,9)
assert gamma2/(1+2*(1-gamma2))==Q(4,19)<gamma2/2
assert ((1-gamma2)/2)/(1+2*(1-gamma2))==Q(5,38)<gamma2/2

# Exact marginal lifting root certificate.
eps=Q(1,10000); gamma4=Q(4,5)**4; target=gamma4*(1+eps)
a=Q(8000199,10**7);b=Q(7999223,10**7)
assert target==Q(160016,390625)
assert target-a**4==Q(2032792963819263760799,10**28)>0
assert target-2*eps-b**4==Q(664183074753367294559,10**28)>0
assert 4*a+b-4==Q(19,10**7)>0
assert target<Q(9,10)**4

# Split rounding's dimensional strict inequality.
assert gamma2<Q(1,2)
print('All exact rational certificates verified.')
