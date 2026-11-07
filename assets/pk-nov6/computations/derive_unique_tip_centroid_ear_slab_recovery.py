import sympy as s
r,z=s.symbols('r z',nonnegative=True)
a=z/(1+z);X=-a;Y=r+1+a;k=s.Rational(3,2)*(r+3)
S=[2*(Y+1)/(2-X),2+r/(Y+1),s.Integer(2)]
Q=[S[0],(3*r+6-S[1])/2,s.Integer(2)]
M=s.factor(sum(q/v for q,v in zip(Q,S)))
T=sum(q/v**2 for q,v in zip(Q,S));U=s.prod(q/v**2 for q,v in zip(Q,S))
E=s.factor(M*M-k*T);R=s.factor(M*M*E*E-4*k**3*U)
for name,f in [('M',M),('E',E),('R',R)]:
 print(name,s.factor(f))
 n,d=s.fraction(f);p=s.Poly(n,r,z)
 print('degrees',p.degree(r),p.degree(z),'terms',len(p.terms()),'negative',[(m,c) for m,c in p.terms() if c<0])
