"""Exact printed certificates and algebra for the all-dimensional dual."""
from submission_text import read_submission
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import re
import sympy as s

checks=0
def check(a):
    global checks
    assert a
    checks+=1

src=read_submission('660db01ed45063dd')
rows={int(d):int(r) for d,r in re.findall(r'^\| (\d+) \| (\d+) \|$',src,re.M)}
check(set(rows)==set(range(1,14)))
for d in range(1,101):
    A=F(d+1,d)**d;L=4*A/3-1
    delta=2+F(d+1,d)*(1+A/3)-2*(1+F(1,2*d))**(d+1)-2*max(F(0),1-L/(2*d))**(d+1)
    check(delta>0)
    if d<14:
        J=6*d**(d+1);B=3*(2*d+1)*d**d;N=B-4*(d+1)**d
        Z=6*d**(d+1)+3*(d+1)*d**d+(d+1)**(d+1)
        rem=16*(Z*J**d-B**(d+1)-N**(d+1))-J**(d+1)
        check(N>0 and rem>0)
        check(rows[d]==rem)
        check(delta==F(1,8)+F(rem,8*J**(d+1)))
    else:
        check(A>F(21,8))
    # Exact one-variable Fenchel checks at rational d-th roots.
    for root in [F(j,5) for j in range(31)]:
        phi=root**d-F(d,d+1)*root**(d+1)
        for a in [F(1,d),F(1,2*d),-L/(2*d)]:
            check(phi+a*root**d<=max(F(0),1+a)**(d+1)/(d+1))

check(8*15**14>21*14**14)
check(F(87,32)<F(33,20)**2)
taylor=sum(F(5,4)**j/factorial(j) for j in range(7))
check(taylor==F(2058029,589824)>F(80,23))
check(F(33,10)+F(23,40)==F(31,8))
check(F(15,8)>F(33,20))

U,Q,E,A,ss,alpha,rr=s.symbols('U Q E A ss alpha rr',positive=True)
L=4*A/3-1
check(s.expand((U+Q+E-1)-(1+4*A/3+(1+L)*E-1)-(U+Q-L*E-(1+4*A/3)))==0)
check(s.factor((1+alpha)/ss-(1/ss+(ss+alpha-rr)/ss+rr/ss-1))==0)
v,k,G=s.symbols('v k G',positive=True)
check(s.expand(s.Rational(3,4)*G*(k+v)-G*(k+2*v)/2-G*(k-v)/4)==0)

print(f'PASS: {checks:,} exact printed-certificate, dual, and scalar checks')
