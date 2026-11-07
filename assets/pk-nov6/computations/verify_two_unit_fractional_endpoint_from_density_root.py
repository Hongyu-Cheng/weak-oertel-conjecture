"""Independent k=2 derivation, beginning at the actual density substitutions."""
import sympy as s
p,t,y,z,m,r=s.symbols('p t y z m r',positive=True)
zp=(t-p)/(1-t)
zn=(y-p)/(1+y)
# Factor the universal (p+z)/(1+z) power before making the substitution.
assert s.cancel((p+zp)/(1+zp)-t)==0
positive_rest=(m+1)*(1-(m+1)*z)*(1+(2*m+5)*z)/(4*(1+z)**4)
actual_positive=s.cancel(positive_rest.subs(z,zp)*s.diff(zp,t))
product=(1+(m+1)*p-(m+2)*t)*(1-(2*m+5)*p+(2*m+4)*t)
assert s.cancel(actual_positive-(m+1)*product/(4*(1-p)**3))==0
assert s.cancel((p+zn)/(1-zn)-y)==0
negative_rest=(m+1)*(1-(m+1)*z)/(4*(1-z)**3)
actual_negative=s.cancel(negative_rest.subs(z,zn)*s.diff(zn,y))
assert s.cancel(actual_negative-(m+1)*(1+(m+1)*p-m*y)/(4*(1+p)**2))==0
C=[s.expand(product).coeff(t,j) for j in range(3)]
Q=lambda v:sum(C[j]*v**j/(m+j) for j in range(3))
T=(1+(m+1)*p)/(m+1+p)
A=(2*r+3)*p**2+(3*r+1)*p-r
B=p**2+(3*r+1)*p+r+2
assert s.cancel(Q(T)+(1+(m+1)*p)**2*A.subs(r,m+1)/(m*(m+1)*(m+1+p)**2))==0
low=((m+1)+(2*m+1)*p)/(4*m*(1+p)**2)-(m+1)*Q(p)/(4*(1-p)**3)
assert s.cancel(low-p**2*B.subs(r,m+1)/(m*(1-p)**3*(1+p)**2))==0
logR=(r+1)*(1/p+1/(r+p)-r/(1+r*p))+s.diff(B,p)/B-2/(1+p)-s.diff(A,p)/A
K=(-r**2*(r+1)*(r+2)-r*(r+2)*(3*r**2+3*r+2)*p
  +(r**4-5*r**3-25*r**2-9*r+2)*p**2
  +(11*r**4-5*r**3-21*r**2-13*r+4)*p**3
  +r*(6*r**3+4*r**2-13*r-3)*p**4+r*(2*r**2+r-3)*p**5)
assert s.cancel(logR-(p-1)**2*K/(p*(1+p)*(r+p)*(1+r*p)*A*B))==0
x=s.symbols('x',nonnegative=True)
for j in [3,4,5]:
    poly=s.Poly(s.expand(K).coeff(p,j).subs(r,3+x),x)
    assert all(c>0 for c in poly.all_coeffs())
assert s.cancel(4*B.subs(p,1)-4*A.subs(p,1))==0
print('PASS: both actual-density substitutions, both integrated endpoints, corrected quintic identity, coefficient signs and R(1)')
