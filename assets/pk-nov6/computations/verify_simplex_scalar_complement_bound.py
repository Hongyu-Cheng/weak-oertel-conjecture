from submission_text import read_submission
import sys,re

import sympy as s
from fractions import Fraction as F
from math import prod
from random import Random
t,r,U,V,W=s.symbols('t r U V W');u=(1+t+r)/2;h=1-t;v=1-r;N=u*v*(h-t*u)/h;D=5-1/h-1/u-1/v
P=t**4*(r-1)**2+t**3*(3*r**3-r*r-7*r+5)+t*t*(3*r**4+4*r**3-12*r*r+10*r-3)+t*(r**5+3*r**4-6*r**3+8*r*r-5*r+1)-2*r**4-4*r*r+2*r
assert s.factor(D-2*N-P/(2*(1-r)*(1-t)*(1+t+r)))==0
rows={tuple(map(int,m[:3])):tuple(map(int,m[3:])) for m in re.findall(r'\| \((\d+),(\d+),(\d+)\) \| (\d+) \| (\d+) \|',read_submission('2fb5e3a3730b144e'))}
assert len(rows)==27
for index,scale,ts,rs in [(0,41472,U/3+V/4,V/4),(1,124416,V/4,U/3+V/4)]:
 pp=s.Poly(P,t,r);H=s.Poly(s.expand(scale*sum(c*ts**i*rs**j*(U+V+W)**(6-i-j) for (i,j),c in pp.terms())),U,V,W)
 assert {m:int(c) for m,c in H.terms()}=={m:values[index] for m,values in rows.items()}
 assert min(H.coeffs())>0
A=1-t-t*t;B=2-3*t;C=3-4*t;Q=(1-r)**2*(A-t*r)/(B-C*r);R=(1-t)**2*(2*t-1)*(2*t*t+3*t-3)/C**3
assert s.factor(s.diff(Q,r,2)-2*t/C-2*C*C*R/(B-C*r)**3)==0
assert s.factor(s.Rational(5,9)-Q.subs(r,0)-(3*t-1)**2/(9*(2-3*t)))==0
assert s.factor(Q.subs(r,1-2*t)-s.Rational(1,2)+(2*t-1)*(4*t**3-6*t*t+5*t-1)/(2*(8*t*t-7*t+1)))==0
rng=Random(832)
for d in range(2,15):
 gamma=F(d,d+1)**d
 for _ in range(300):
  xx=[F(rng.randint(1,20)) for j in range(d+1)];xx=[x/sum(xx) for x in xx];la=[(1-x)/d for x in xx]
  E=d*(d+1)-sum(1/x for x in sorted(la)[1:-1]);c=F(d+1)/E
  for i in range(d+1):
   p=d**d*prod(la[j] for j in range(d+1) if j!=i);ss=p*(d-sum(1/la[j] for j in range(d+1) if j!=i)/(d+1));qq=p-c*ss
   assert gamma<=qq<=F(5,9)
 la=[F(1,3*d),F(1,d),F(2,3*d)]+[F(1,d)]*(d-2);E=d*(d+1)-sum(1/x for x in sorted(la)[1:-1]);c=F(d+1)/E;i=2
 p=d**d*prod(la[j] for j in range(d+1) if j!=i);ss=p*(d-sum(1/la[j] for j in range(d+1) if j!=i)/(d+1))
 assert p-c*ss==F(5,9)
print('PASS: exact positive-coefficient identities, one-variable convexity and endpoint identities, all-dimensional equality family, and rational spot checks.')
