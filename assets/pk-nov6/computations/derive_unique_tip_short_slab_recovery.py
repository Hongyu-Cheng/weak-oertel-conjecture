import sympy as s
r,a=s.symbols('r a')
X=-a;Y=r+1+a;k=s.Rational(3,2)*(r+3)
S=[2*(Y+1)/(2-X),2+r/(Y+1),s.Integer(2)]
Q=[S[0],(3*r+6-S[1])/2,s.Integer(2)]
M=s.factor(sum(q/v for q,v in zip(Q,S)));T=sum(q/v**2 for q,v in zip(Q,S));U=s.prod(q/v**2 for q,v in zip(Q,S))
E=s.factor(M*M-k*T);R=s.factor(M*M*E*E-4*k**3*U)
for name,f in [('E',E),('R',R)]:
 n,d=s.fraction(f);P=s.Poly(n,r,a)
 print(name,'factor',s.factor(f));print('negative',[(m,c) for m,c in P.terms() if c<0])
 for j in range(s.degree(n,r)+1):print(j,s.factor(s.expand(n).coeff(r,j)))
