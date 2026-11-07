import sys

import sympy as s
p,q,r,t=s.symbols('p q r s', positive=True)
a=p*t/((p+r)*(p+t)*(q+t))
b=q*r/((p+r)*(q+t)*(q+r))
h=a/(a+b)
l0=(r/(p+r)+h*t/(p+t))/3
l1=(t/(q+t)+(1-h)*r/(q+r))/3
l2=(p/(p+r)+(1-h)*q/(q+r))/3
l3=(q/(q+t)+h*p/(p+t))/3
print('positive difference=',s.factor(l0-l1))
print('negative difference=',s.factor(l2-l3))
print('cross difference01=',s.factor(l0-l2))
print('cross difference23=',s.factor(l1-l3))
