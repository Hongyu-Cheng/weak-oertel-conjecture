import sympy as s
p,t,z,m,r=s.symbols('p t z m r', positive=True)
A=(2*r+3)*p**2+(3*r+1)*p-r
D=p**2+(3*r+1)*p+r+2
K=(-r**4-3*r**3-2*r**2+(-3*r**4-9*r**3-8*r**2-4*r)*p
 +(r**4-5*r**3-25*r**2-9*r+2)*p**2
 +(11*r**4-5*r**3-21*r**2-13*r+4)*p**3
 +(6*r**4+4*r**3-13*r**2-3*r)*p**4
 +(2*r**3+r**2-3*r)*p**5)
logD=(r+1)*(1/p+1/(r+p)-r/(1+r*p))+s.diff(D,p)/D-2/(1+p)-s.diff(A,p)/A
assert s.cancel(logD-(p-1)**2*K/(p*(1+p)*(r+p)*(1+r*p)*D*A))==0
# Start from the actual positive density f_Z. After factoring
# ((p+z)/(1+z))^(m-1), its remaining differential factor is rational.
zof=(t-p)/(1-t)
assert s.cancel(((p+z)/(1+z)).subs(z,zof)-t)==0
actual=(m+1)*(1-(m+1)*z)*(1+(2*m+5)*z)/(4*(1+z)**4)
actual=s.cancel(actual.subs(z,zof)*s.diff(zof,t))
prod=(1+(m+1)*p-(m+2)*t)*(1-(2*m+5)*p+(2*m+4)*t)
assert s.cancel(actual-(m+1)*prod/(4*(1-p)**3))==0
# Negative-z substitution u=-z/(1-z), after factoring its power,
# gives the exact primitive stated in the proof.
u=s.symbols('u',positive=True)
zneg=-u/(1-u)
assert s.cancel(((p+z)/(1-z)).subs(z,zneg)-(p-(1+p)*u))==0
neg=(m+1)*(1-(m+1)*z)/(4*(1-z)**3)
assert s.cancel(neg.subs(z,zneg)*(-s.diff(zneg,u))-(m+1)*(1+m*u)/4)==0
# Integral of (p-(1+p)u)^(m-1)*(1+m*u), 0<=u<=p/(1+p).
negcoeff=(m+1)/4*(1/(m*(1+p))+p/((m+1)*(1+p)**2))
assert s.cancel(negcoeff-((m+1)+(2*m+1)*p)/(4*m*(1+p)**2))==0
C=[s.expand(prod).coeff(t,j) for j in range(3)]
Q=lambda v:sum(C[j]*v**j/(m+j) for j in range(3))
T=(1+(m+1)*p)/(m+1+p)
assert s.factor(Q(T)+T**2*A.subs(r,m+1)/(m*(m+1)))==0
low=((m+1)+(2*m+1)*p)/(4*m*(1+p)**2)-(m+1)*Q(p)/(4*(1-p)**3)
assert s.factor(low-p**2*D.subs(r,m+1)/(m*(1-p)**3*(1+p)**2))==0
x=s.symbols('x',nonnegative=True)
assert s.expand(K.coeff(p,3).subs(r,3+x))==11*x**4+127*x**3+528*x**2+914*x+532
assert s.expand(K.coeff(p,4).subs(r,3+x))==6*x**4+76*x**3+347*x**2+675*x+468
assert s.expand(K.coeff(p,5).subs(r,3+x))==2*x**3+19*x**2+57*x+54
# Independent direct phase-type construction for two small m checks the
# entire actual probability derivative, not only the transform algebra.
for mm in [2,3]:
 ps=[s.Integer(1),s.Integer(1),p];v=[s.Integer(1)]*3
 for b in [s.Integer(1)]+[(1+p)/mm]*mm:
  for i in reversed(range(3)):
   v[i]=s.cancel((ps[i]*v[i]+(b*v[i+1] if i<2 else 0))/(ps[i]+b))
 rr=mm+1
 L=4*p**(rr+1)*(rr+p)**(rr+1)*D.subs(r,rr)-(1+p)**2*(1+rr*p)**(rr+1)*A.subs(r,rr)
 Ip=L/(4*mm*(1-p)**3*(1+p)**2*(rr+p)**(rr+1))
 assert s.cancel(s.diff(v[0],p)-Ip/(p+(1+p)/mm)**(mm+1))==0
print('PASS: actual-density substitutions, symbolic primitive and log-derivative identities, coefficient certificates, and direct probability checks')
