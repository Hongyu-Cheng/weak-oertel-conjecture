"""Actual symbolic clipping and exact full-interval coefficient certificates."""
from submission_text import read_submission
import ast
from fractions import Fraction
from functools import reduce
from math import gcd
from pathlib import Path
import re
import sympy as s

checks=0
def ck(value):
    global checks
    assert value
    checks+=1

source=read_submission('e917eba155dec2d6')
printed={label:ast.literal_eval(re.search(r'\b'+label+r' = (\[[^\]]*\])',source).group(1))
         for label in ('LE','LR','UE','UR')}
t,z=s.symbols('t z')
P=[s.Matrix([7-17*t,-6+15*t]),s.Matrix([1,-5]),
   s.Matrix([7,-6]),s.Matrix([2,4])]
normals=[s.Matrix([1,0]),s.Matrix([0,1]),s.Matrix([-1,-1])]
det=lambda a,b:s.det(s.Matrix.hstack(a,b))
area=lambda points:s.factor(sum(det(a,b) for a,b in zip(points,points[1:]+points[:1]))/2)
ck(area(P)==84*t)
for i,expected in enumerate((73*t,55,95*t,168*t-55)):
    ck(s.expand(det(P[(i+1)%4]-P[i],P[(i+2)%4]-P[(i+1)%4]))==expected)
for i,expected in enumerate((70*t-29,29,40,98*t-40)):
    ck(s.expand(det(P[i],P[(i+1)%4]))==expected)
ck(s.Rational(29,70)>s.Rational(55,168))
ck(s.Rational(29,70)>s.Rational(20,49))
ck(s.Rational(29,70)>s.Rational(7,17))
ck(s.Rational(29,70)>s.Rational(2,5))

expectedQ=[(24463*t*t-16282*t+2695)/(2*(17*t-6)*(17*t-5)),
           (2520*t*t-1313*t+198)/(2*(15*t-1))]
expectedS=[(17*t-7)*(168*t-55)/((17*t-6)*(17*t-5)),
           (130*t-33)/(15*t-1)]
data={}
for branch,sample in [('L',s.Rational(3,7)),('U',s.Rational(1))]:
    Q=[];sigma=[]
    for i,v in enumerate(normals):
        out=[];end=[]
        for p,q in zip(P,P[1:]+P[:1]):
            a=v.dot(p);b=v.dot(q)
            if a.subs(t,sample)>0:out.append(p)
            if a.subs(t,sample)*b.subs(t,sample)<0:
                w=s.simplify(p+a/(a-b)*(q-p))
                out.append(w);end.append(w)
        ck(len(end)==2)
        Q.append(area(out))
        sig=s.factor(end[1][1]-end[0][1]) if i==0 else s.factor(end[1][0]-end[0][0])
        sig*=s.sign(sig.subs(t,sample))
        sigma.append(sig)
        if i<2:
            ck(s.cancel(Q[i]-expectedQ[i])==0)
            ck(s.cancel(sigma[i]-expectedS[i])==0)
    if branch=='L':
        ck(s.cancel(Q[2]-584*t/(5*(5-2*t)))==0)
        ck(s.cancel(sigma[2]-292*t/(5*(5-2*t)))==0)
    else:
        ck(s.cancel(Q[2]-(1680*t*t+802*t+55)/(10*(2*t+5)))==0)
        ck(s.cancel(sigma[2]-(548*t-55)/(5*(2*t+5)))==0)
    k=84*t
    M=s.factor(sum(q/v for q,v in zip(Q,sigma)))
    T=sum(q/v**2 for q,v in zip(Q,sigma))
    U=s.prod(q/v**2 for q,v in zip(Q,sigma))
    E=s.factor(M*M-k*T)
    R=s.factor(M*M*E*E-4*k**3*U)
    data[branch]=(Q,sigma,M,T,U,E,R)
    for name,function,degree,low in [('E',E,5 if branch=='L' else 7,0 if branch=='L' else 1),
                                     ('R',R,18 if branch=='L' else 23,0 if branch=='L' else 3)]:
        numerator,denominator=s.fraction(function)
        poly=s.Poly(numerator,t)
        ck(min(m[0] for m,c in poly.terms())==low)
        poly=s.Poly(poly.as_expr()/t**low,t)
        ck(poly.degree()==degree)
        if branch=='L':
            substitution=(s.Rational(29,70)+z/2)/(1+z)
            transformed=s.Poly(s.cancel(poly.as_expr().subs(t,substitution)*(1+z)**degree),z)
            D=(17*t-7)*(130*t-33)**2*(168*t-55) if name=='E' else (17*t-7)**4*(130*t-33)**6*(168*t-55)**4
        else:
            transformed=s.Poly(s.expand(poly.as_expr().subs(t,(1+z)/2)),z)
            D=(17*t-7)*(130*t-33)**2*(168*t-55)*(548*t-55)**2 if name=='E' else (17*t-7)**4*(130*t-33)**6*(168*t-55)**4*(548*t-55)**6
        ratio=s.cancel(denominator/D)
        ck(ratio.is_Rational and ratio>0)
        coeff=[transformed.nth(i) for i in range(degree+1)]
        lcm=s.ilcm(*[x.q for x in coeff])
        integers=[int(x*lcm) for x in coeff]
        factor=reduce(gcd,integers)
        integers=[x//factor for x in integers]
        ck(integers==printed[branch+name])
        for x in integers:ck(x>0)

for i in range(3):
    ck(s.cancel(data['L'][0][i]-data['U'][0][i]).subs(t,s.Rational(1,2))==0)
    ck(s.cancel(data['L'][1][i]-data['U'][1][i]).subs(t,s.Rational(1,2))==0)

# Check the previously certified subcritical peak within the same family.
r=s.Rational(9353,10000)
Q,S,M,T,U,E,R=data['U']
for value in (s.Rational(9,10),s.Rational(1),s.Rational(11,10)):
    er=(r*r*M*M-84*t*T).subs(t,value)
    rr=(r*r*M*M*(r*r*M*M-84*t*T)**2-4*(84*t)**3*U).subs(t,value)
    ck(er>0)
    ck(rr<0 if value==1 else rr>0)
print(f'PASS: {checks} exact symbolic, geometric and coefficient checks')
