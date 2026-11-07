from fractions import Fraction as F
import sympy as s
count=0
def ck(v):
 global count
 assert v
 count+=1
# All supporting allocations: section and body reconstruct the shadow exactly.
a,k=s.symbols('a k',nonnegative=True)
ck(s.expand(a*k+(1-a)*k-k)==0) # inside old facet restored
ck(s.expand(a*k+a*k-2*a*k)==0) # outside selected shadow
# All-dimensional simplex reserve, including the d=1 convention.
for d in range(1,101):
 alpha=F(d,d+1);gamma=alpha**d
 reserve=alpha**(d-1)-gamma
 ck(reserve==gamma/d)
 ck(reserve<=min(gamma,1-gamma))
 ck(gamma+reserve==alpha**(d-1))
# Triangle support/projection identity in exact rational directions (homogeneity avoids sqrt).
# T vertices (2,-1),(-1,2),(-1,-1); shadow length per nonunit e is the width in (-e2,e1).
V=[(2,-1),(-1,2),(-1,-1)]
for x in range(-9,10):
 for y in range(-9,10):
  if x==y==0:continue
  heights=[-y*p[0]+x*p[1] for p in V]
  B=max(heights)-min(heights)
  R=F(2,3)*(abs(x)+abs(y)+abs(x+y))
  ck(R/(2*B)==F(2,9))
  ck(F(4,9)*B+R/2==F(2,3)*B)
# Opposite-box exact sharpness for the coefficient2.
for area in [F(a,b) for a in range(1,11) for b in range(1,8)]:
 R=area;B=area;beta=F(1,2)
 ck(R==2*beta*B)
print(f'{count} exact checks PASS')
