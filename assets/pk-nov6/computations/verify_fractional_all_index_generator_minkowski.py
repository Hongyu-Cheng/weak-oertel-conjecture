#!/usr/bin/env python3
"""Independent finite symbolic checks of the proved all-index identities."""
import sympy as s

p,z,t,m=s.symbols('p z t m')
checks=0
def zero(expr):
    global checks
    assert s.cancel(expr)==0
    checks+=1

for k in range(2,8):
    q=k-1;c=1-p;C=p+q;A=q+(m+1)*p;B=m+p+q
    D=q*p**2+((k+1)*m+k*k-k+2)*p+q*(m+k+1)
    coeff=[s.expand(sum(2**j*s.binomial(m+j+1,j).expand(func=True)
                 *s.binomial(j,ell)*(-p)**(j-ell)*c**(q-j)
                 for j in range(ell,k))) for ell in range(k)]
    S=sum(coeff[j]*t**j for j in range(k))
    G=s.Poly(s.expand((A-(m+k)*t)*S),t)
    Q=sum(G.nth(j)*t**j/(m+j) for j in range(k+1))
    neg=((m+1)*q+(m*k+1)*p)/(2**k*m*(1+p)**2)
    low=neg-(m+1)*Q.subs(t,p)/(2**k*c**(k+1))
    zero(low-(-1)**k*p**k*D/(m*c**(k+1)*(1+p)**2))
    F=coeff[0]*B**q
    for ell in range(1,k):
        F+=s.cancel(m*(m+1)*coeff[ell]*A**(ell-1)*B**(q-ell)
                    *(A-ell*c)/((m+ell)*(m+ell+1)))
    F=s.cancel((-1)**q*F)
    zero(Q.subs(t,A/B)-(-1)**q*A*A*F/(m*(m+1)*B**k))
    # Coefficient extraction using finite convolution, independently of Q.
    generator=0
    for i in range(q+1):
        # (1+2Bc z)/(1+Bc z) has constant1 and higher coefficient(-1)^(i-1)(Bc)^i.
        ai=1 if i==0 else (-1)**(i-1)*(B*c)**i
        for j in range(q-i+1):
            ell=q-i-j
            generator+=ai*(j+1)*(2*p*B)**j*(-1)**ell*s.binomial(m+ell,ell).expand(func=True)*(2*c*C)**ell
    zero(F-generator)
    zero(F.subs(p,1)-k*2**(k-1)*(m+k)**(k-1))
    L=s.expand(D*F*((m+k)*(1+p)*B*A+(m+k)*p*(1+p)*A
                -(m+2)*(m+1)*p*(1+p)*B-2*p*B*A)
                +p*(1+p)*B*A*(s.diff(D,p)*F-D*s.diff(F,p)))
    quotient,remainder=s.div(L,(p-1)**k,p)
    zero(remainder)
    assert s.Poly(quotient,p).degree()<=k+3
    checks+=1
    print(f'k={k}: symbolic m identities checked',flush=True)

print(f'PASS: {checks} symbolic identity checks')
