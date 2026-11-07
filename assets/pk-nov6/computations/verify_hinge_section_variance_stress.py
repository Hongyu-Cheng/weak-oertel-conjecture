from fractions import Fraction as F
z=(-1,0,1); w=(F(1),F(2),F(1)); c=tuple(v/2 for v in w)
S=F(3); C=sum(c); hinge=sum(v*v/2 for v in c)
delta=c; mean=C/S; variance=sum((v-mean)**2 for v in delta)/S
assert C==2 and hinge==F(3,4) and variance==F(1,18)
assert sum(i*v for i,v in zip(z,c))==0
assert sum(F(i)*(v-mean) for i,v in zip(z,delta))/S==0
assert hinge==F(1,2)*(C*C/S+S*variance)
assert hinge-F(1,2)*C*C/S==F(1,12)
eta=w
assert sum(v/2 for v in eta)==C
assert sum(F(i)*v/2 for i,v in zip(z,eta))==0
assert sum(v*v/4 for v in w)==2*hinge
print('PASS: sharp variance and exact normal global-minimizer stress')
