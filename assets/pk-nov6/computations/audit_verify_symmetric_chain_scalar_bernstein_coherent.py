#!/usr/bin/env python3
"""Independent exact reconstruction, including reverse Bernstein expansion."""
import sympy as s
import json
from pathlib import Path
u,t,X,Y=s.symbols('u t X Y')
Q=s.Rational
c=1/(3*u); rho=1/(3*(1-u))
A=u/(2*u-1); L=(1-u)**2/((2*u-1)*(2-3*u)); B=(2*u-1)/(2-3*u)
lam=(18*u**3-24*u*u+8*u-1)/(27*u*u*(u-1))
g=(2-3*u)/(9*(1-u)); v=(3*u-1)*(6*u-1)/(27*u*u)
M0=Q(9,2)-1/(2*u*(1-u)); M1=g/(Q(2,9)-v)
J=3*u*u+2*u*t-4*u-t+1; D=12*u*u-9*u+1
rows=[
(0,'M1',Q(1,2),Q(3,5),0,1,-729*u**4*(-3*u+t)*(u-1)**3*D,Q(3,512)),
(1,'M0',Q(1,2),Q(11,20),0,Q(1,2),1458*u**4*(u-1)**3*J,Q(3,256)),
(1,'M0',Q(1,2),Q(11,20),Q(1,2),1,1458*u**4*(u-1)**3*J,Q(3,256)),
(1,'M2',Q(11,20),Q(3,5),0,Q(1,2),1458*u**4*(u-1)**3*J,Q(13082,1953125)),
(1,'M0',Q(11,20),Q(3,5),Q(1,2),1,1458*u**4*(u-1)**3*J,Q(15032430113,256000000000)),
(2,'M0',Q(1,2),Q(3,5),0,1,-1458*u**3*(u-1)**3,Q(3,32)),
(0,'six',Q(3,5),Q(2,3),0,1,729*u**4*(-3*u+t)*(u-1)**3,Q(148954,390625)),
(1,'six',Q(3,5),Q(2,3),0,1,729*u**4*(u-1)**3*J,Q(0)),
(2,'six',Q(3,5),Q(2,3),0,1,-729*u**2*(u-1)**3,Q(12664,3125)),
]
cert=[]; count=0
for region,name,lo,hi,yl,yh,mult,expected in rows:
    b=[c*t,c+(rho-c)*t,rho+(1-rho)*t][region]
    k=[s.Integer(0),A*(b-c)**2,A*(b-c)**2-L*(b-rho)**2][region]
    E=((1-rho)**2/2-(1-rho)**3/(3*(1-b))) if region<2 else (1-b)**2/6
    M={'M0':M0,'M1':M1,'M2':Q(3,2)+b+Q(5,2)*b*b,'six':s.Integer(6)}[name]
    F=g+(lam-Q(2,9))*M+k-lam*(b*b+(1-b)**2/3)-2*B*E
    P=s.cancel(mult*F)
    assert s.fraction(P)[1]==1
    P=s.Poly(P,u,t)
    transformed=s.Poly(s.expand(P.as_expr().subs({u:lo+(hi-lo)*X,t:yl+(yh-yl)*Y},simultaneous=True)),X,Y)
    m=transformed.degree(X); n=transformed.degree(Y)
    coefficients={}
    reconstructed=s.Integer(0)
    for i in range(m+1):
        for j in range(n+1):
            b_ij=sum(transformed.coeff_monomial(X**k*Y**l)*s.binomial(i,k)*s.binomial(j,l)/(s.binomial(m,k)*s.binomial(n,l)) for k in range(i+1) for l in range(j+1))
            b_ij=s.cancel(b_ij)
            assert b_ij>=0
            coefficients[i,j]=b_ij
            reconstructed+=b_ij*s.binomial(m,i)*X**i*(1-X)**(m-i)*s.binomial(n,j)*Y**j*(1-Y)**(n-j)
            count+=1
    assert s.Poly(s.expand(reconstructed-transformed.as_expr()),X,Y).is_zero
    assert min(coefficients.values())==expected
    cert.append({'branch':region,'M':name,'a':[str(lo),str(hi)],'y':[str(yl),str(yh)],'degree':[m,n],
                 'minimum':str(expected),'coefficients':[[str(coefficients[i,j]) for j in range(n+1)] for i in range(m+1)]})
    print(region,name,(m,n),'minimum',expected,'zero coefficients',[ij for ij,vv in coefficients.items() if vv==0])
# Independently check the exact six-bound relation and its four coefficients.
P=s.expand(-(27*u**3-44*u*u+20*u-2))
assert s.cancel(g-6*(Q(2,9)-v)+P/(9*u*u*(u-1)))==0
p=s.Poly(P.subs(u,Q(3,5)+X/15),X)
bs=[sum(p.coeff_monomial(X**k)*s.binomial(i,k)/s.binomial(3,k) for k in range(i+1)) for i in range(4)]
assert bs==[Q(1,125),Q(4,45),Q(22,135),Q(2,9)]
assert s.expand(sum(bs[i]*s.binomial(3,i)*X**i*(1-X)**(3-i) for i in range(4))-p.as_expr())==0
Path('./symmetric-chain-scalar-independent-bernstein-coefficients.json').write_text(json.dumps(cert,indent=2)+'\n')
print(f'PASS {count} nonnegative bivariate Bernstein coefficients, nine reverse polynomial identities, and four six-bound coefficients')
