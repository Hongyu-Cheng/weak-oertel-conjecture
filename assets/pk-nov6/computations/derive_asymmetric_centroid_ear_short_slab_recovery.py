import sympy as s
r,p=s.symbols('r p');v=r+2+p;D=4*v+3*r*r+6*r
c=s.Rational(3,2)*(r+2);k=s.Rational(3,2)*(r+3)
q=v/D;h=(4*v+r*r+3*r)/D
M=c*h;T=c*(h*h-2*q)-h/2+s.Rational(1,2);U=q*(c*c*q-c*h/2+s.Rational(1,4))/2
E=s.factor(M*M-k*T);R=s.factor(M*M*E*E-4*k**3*U)
for name,f in [('E',E),('R',R)]:
 print(name,s.factor(f))
 n,d=s.fraction(f);P=s.Poly(n,r,p)
 print('degrees',P.degree(r),P.degree(p),'terms',len(P.terms()),'neg',[(m,c) for m,c in P.terms() if c<0])
RP=s.cancel(R*64*D**6/(27*r))
EP=s.cancel(E*4*D**2/3)
for name,P in [('EP',EP),('RP',RP)]:
 for j in range(s.degree(P,p)+1):print(name,j,s.factor(s.expand(P).coeff(p,j)))
