from fractions import Fraction as F
from math import comb

assert F(4)**3/F(14)**2-F(2)**3/F(5)**2==F(8,1225)>0
def choose(n,k):return comb(n,k) if n>=k else 0
def seq(m):
    return sum(w*choose(m+3-j,3) for j,w in enumerate([F(1,4),F(1,2),F(1,4)]))
assert [seq(m) for m in range(3)]==[F(1,4),F(3,2),F(19,4)]
for m in range(12):
    x=F(m+1)
    assert seq(m)==(x**3+x/2)/6
    P=x**3+x/2;P1=3*x*x+F(1,2);P2=6*x
    assert P*P2-F(2,3)*P1**2==x*x-F(1,6)>0
assert F(19)>F(8,3)**3
assert F(11,3)**3>48
print('PASS: derivative-shift and Poisson-binomial concavity shortcuts are false')
