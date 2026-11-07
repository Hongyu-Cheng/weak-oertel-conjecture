"""Exact algebra underlying the level integration, not a numerical proof."""
import sympy as S
p,A,B,N=S.symbols('p A B N',positive=True)
left=2*A/((p-1)*p*(p+1))-S.Rational(2,3)*(B/(p*(p-1))-A/(p*(p+1)))
assert S.factor(left-2*((p+2)*A-(p+1)*B)/(3*(p-1)*p*(p+1)))==0
from fractions import Fraction as F
# One-sided finite quadratic identities and their Green pairings.
for h in range(1,31):
 v=[1-F(2*i,2*h+1) for i in range(h+1)]
 r=[x-F(1,3) for x in v]
 assert sum(i*r[i] for i in range(h+1))==0
 assert sum(x*x-F(2,3)*x for x in v)==F(h+1,3*(2*h+1))
 for t in range(1,h):
  G=[F(min(i,t))-F(i*t,h) for i in range(h+1)]
  assert sum(r[i]*G[i] for i in range(h+1))==F(t*(h-t)*(h+1-t),3*(2*h+1))
# Independent exact integration checks at integer powers; the note evaluates
# the three antiderivatives directly for every real p>1.
for pp in range(2,21):
 for f in [F(1,7),F(2,3),F(1)]:
  I=f*f*f**(pp-1)/(pp-1)-2*f*f**pp/pp+f**(pp+1)/(pp+1)
  assert I==2*f**(pp+1)/((pp-1)*pp*(pp+1))
  J=f*f**(pp-1)/(pp-1)-(f+1)*f**pp/pp+f**(pp+1)/(pp+1)
  assert J==f**pp/(pp*(pp-1))-f**(pp+1)/(pp*(pp+1))
print('PASS: finite quadratic identities, exact integral formulas, and all-real-p algebra.')
