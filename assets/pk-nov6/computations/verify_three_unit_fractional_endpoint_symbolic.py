import sympy as s
p,t,z,m=s.symbols('p t z m',positive=True)
A=(2*m*m+12*m+17)*p**4+(10*m*m+52*m+62)*p**3+(9*m*m+36*m+45)*p*p-(12*m*m+36*m+20)*p+3*m*m+8*m+4
D=p*p+(2*m+4)*p+m+4;N=(m+1)*p+2
K=(-6*m**5-70*m**4-308*m**3-632*m*m-592*m-192
 +(-15*m**5-173*m**4-762*m**3-1588*m*m-1512*m-480)*p
 +(3*m**5-7*m**4-260*m**3-1006*m*m-1308*m-480)*p*p
 +(34*m**5+249*m**4+594*m**3+369*m*m-298*m-240)*p**3
 +(22*m**5+189*m**4+558*m**3+643*m*m+180*m-60)*p**4
 +(4*m**5+44*m**4+164*m**3+241*m*m+111*m-6)*p**5
 +(2*m**4+14*m**3+29*m*m+17*m)*p**6)
logD=(m+3)/p+(m+3)/(m+p+2)-(m+2)*(m+1)/N+s.diff(D,p)/D-2/(1+p)-s.diff(A,p)/A
assert s.cancel(logD-(p-1)**3*K/(p*(1+p)*(m+p+2)*N*D*A))==0
zof=(t-p)/(1-t)
cs=[1,2*(m+2),2*(m+2)*(m+3)]
actual=(m+1)/8*(2-(m+1)*z)*sum(cs[j]*z**j/(1+z)**(j+3) for j in range(3))
actual=s.cancel(actual.subs(z,zof)*s.diff(zof,t))
S=(1-p)**2+2*(m+2)*(1-p)*(t-p)+2*(m+2)*(m+3)*(t-p)**2
prod=(2+(m+1)*p-(m+3)*t)*S
assert s.cancel(actual-(m+1)*prod/(8*(1-p)**4))==0
C=[s.expand(prod).coeff(t,j) for j in range(4)]
Q=lambda v:sum(C[j]*v**j/(m+j) for j in range(4))
T=N/(m+p+2)
assert s.factor(Q(T)-N*N*A/(m*(m+1)*(m+p+2)**3))==0
low=(2*(m+1)+(3*m+1)*p)/(8*m*(1+p)**2)-(m+1)*Q(p)/(8*(1-p)**4)
assert s.factor(low+2*p**3*D/(m*(1-p)**4*(1+p)**2))==0
F=2*p**4+10*p**3+9*p*p-12*p+3
G=12*p**4+52*p**3+36*p*p-36*p+8
H=17*p**4+62*p**3+45*p*p-20*p+4
assert s.expand(A-m*m*F-m*G-H)==0
assert F.subs(p,s.Rational(3,8))-s.diff(F,p).subs(p,s.Rational(3,8))**2/36==s.Rational(5279,16384)
assert G.subs(p,s.Rational(1,4))-s.diff(G,p).subs(p,s.Rational(1,4))**2/144==s.Rational(55,32)
assert 4-s.Rational(400,180)==s.Rational(16,9)
for mm in [3,4]:
 ps=[s.Integer(1)]*3+[p];v=[s.Integer(1)]*4
 for b in [s.Integer(1)]+[(2+p)/mm]*mm:
  for i in reversed(range(4)):
   v[i]=s.cancel((ps[i]*v[i]+(b*v[i+1] if i<3 else 0))/(ps[i]+b))
 Ip=N**(m+2)*A/(8*m*(1-p)**4*(m+p+2)**(m+3))-2*p**(m+3)*D/(m*(1-p)**4*(1+p)**2)
 assert s.cancel(s.diff(v[0],p)-Ip.subs(m,mm)/(p+(2+p)/mm)**(mm+1))==0
print('PASS: actual-density substitution, free-m primitive and ratio identities, positivity bounds, and independent probability derivatives')
