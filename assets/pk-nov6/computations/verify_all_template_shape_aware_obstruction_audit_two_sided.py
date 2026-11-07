from fractions import Fraction as F
from math import comb

checks=0
def check(x):
    global checks
    assert x
    checks+=1

d=200; m=100; a=F(21,20)
k=((a+1)**2/(4*a))**m
t=a**(-m)
g=F(d,d+1)**d
epsilon=F(1,1000)
check(((a+1)**2/(4*a))==F(1681,1680))
check(k>1)
check(k<F(84,79))
check(F(84,79)<F(16,15))
check(sum(F(comb(m,j),20**j) for j in range(7))==F(4209933,40000))
check(F(4209933,40000)>100)
check(t<F(1,100))
check(F(8,3)+F(5,96)==F(87,32))
check(F(87,32)<F(11,4))
check(g>F(4,11))
check(k/2+epsilon+t<F(1633,3000))
check(g*(k+epsilon+2)/2>F(6,11))
check(F(6,11)-F(1633,3000)==F(37,33000))
check((k+1)/2>g*(k+epsilon+2)/2)
for n in range(1,20):
    M=2**(n-1)*(k+epsilon+2)
    check(g*M/F(2**n)==g*(k+epsilon+2)/2)

# Algebraic middle-anchor simplification for arbitrary admissible weights
# and sample shape constants; not used to assert geometric realizability.
for wm in [F(0),F(1,5),F(3,2)]:
  for wp in [F(0),F(1,7),F(2)]:
    for w0 in [F(0),F(4,3)]:
      for beta in [F(2,5),F(1,2)]:
        for kappa in [F(3,8),F(2,5),F(1,2)]:
          pair=min(wm,wp);D=w0+pair
          check(beta*(D-w0)+(2*kappa-beta)*pair==2*kappa*pair)
print(f"PASS: {checks} exact checks")
