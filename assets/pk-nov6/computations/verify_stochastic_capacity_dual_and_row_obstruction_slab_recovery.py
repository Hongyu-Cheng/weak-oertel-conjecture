from fractions import Fraction as Q
from itertools import product
import sympy as s
checks=0

def ck(v):
 global checks
 assert v
 checks+=1

# Exact probability-only obstruction.
a=[Q(200,273),Q(100,273),Q(100,273)]
p=[Q(200,273),Q(1),Q(1)]
ck(sum(x*x for x in a)+2*a[0]*a[1]*a[2]-1==Q(33583,20346417))
ck(sum(x*x for x in p)-2*sum(a[i]*p[(i+1)%3]*p[(i+2)%3] for i in range(3))==Q(-142,74529))

# Exact dual optimizer matrices in dimensions one through eight.
for d in range(1,9):
 m=d+1
 for den in range(m,m+7):
  # Symmetric lambda, and exact asymmetric feasible lambda up to its face.
  for eps in [Q(0),Q(1,den*m*10),Q(1,den*m*5)]:
   lam=[Q(1,m)]*m
   lam[0]+=eps;lam[-1]-=eps
   T=sum(lam)/d
   if max(lam)>T:continue
   Y=[[Q(0) if i==j else (T-lam[i])/lam[j] for j in range(m)] for i in range(m)]
   for j in range(m):ck(sum(Y[i][j] for i in range(m))==1)
   for i in range(m):
    ck(Y[i][i]==0 and min(Y[i])>=0)
    # Raising the support equality to the d-th power removes all radicals.
    prod_l=Q(1);prod_y=Q(1)
    for j in range(m):
     if i!=j:prod_l*=lam[j];prod_y*=Y[i][j]
    ck(prod_l*prod_y==(T-lam[i])**d)

# Direct tetrahedral CDF and derivative factorization.
t=s.symbols('t')
F=s.Rational(4096,675)*(t-s.Rational(1,16))**3-s.Rational(256,27)*(t-s.Rational(1,4))**3
ck(s.factor(F-t*s.diff(F,t)/3-(8*t-3)*(56*t-11)/225)==0)
ck(F.subs(t,s.Rational(3,8))==s.Rational(1,6))
ck(s.diff(F,t).subs(t,s.Rational(3,8))==s.Rational(4,3))
ck((s.Rational(3,8)**3/F.subs(t,s.Rational(3,8)))==s.Rational(81,256))
ck(s.Rational(81,256)-s.Rational(19,64)==s.Rational(5,256))
# Compare all rational thresholds on a grid using cubic ratios, including
# the first interval and the top boundary; the derivative proof is universal.
for den in range(16,80):
 for num in range(1,den+1):
  q=Q(num,den)
  if q<=Q(1,16):continue
  val=(q-Q(1,16))**3/Q(675,4096) if q<Q(1,4) else Q(-(256*q**3-448*q**2+128*q-11),75)
  ck(q**3>=Q(81,256)*val)
print(f'PASS: {checks} exact checks.')
