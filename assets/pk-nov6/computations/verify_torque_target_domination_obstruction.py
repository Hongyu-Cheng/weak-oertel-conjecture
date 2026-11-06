from fractions import Fraction as F
N=25
fib={z:F(N-z) for z in range(N)}
M=sum(fib.values())
gz=sum(z*a for z,a in fib.items())/M
gx=sum(a*a/2 for a in fib.values())/M
assert (M,gz,gx)==(325,8,F(17,2))
cap=sum(a for z,a in fib.items() if z>=gz)
noncentral=M-fib[int(gz)]
assert cap==153 and noncentral==308>2*cap
for k in range(8,30):
 N=3*k+1
 M=F(N*(N+1),2)
 assert (M-(2*k+1))-2*(2*k+1)*(k+1)==F(k*k-7*k-4,2)>0
print('Exact coupling-independent torque domination obstruction verified.')
