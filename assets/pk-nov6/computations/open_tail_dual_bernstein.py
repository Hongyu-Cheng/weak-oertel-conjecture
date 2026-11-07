import sympy as S
L,a,j=S.symbols('L a j');x,t,u=S.symbols('x t u');R=L-a;B=2*L+1-3*a;A=4*L*(L+1)-7*a*a-a
P=(R*(7*R-1)-3*L*(L-j))*(L+1)*B-(L-j)*A*(L+j-3*a)
Pl=4*L**3-28*L**2*a-4*L**2+63*L*a*a+13*L*a-42*a**3-6*a*a
Pj=(4*L*j-a*(7*a+1))*(L+1)*B-j*A*(L+j-3*a)

def bern(poly):
 p=S.Poly(poly,t,u,x);dt,du,dx=p.degree(t),p.degree(u),p.degree(x)
 vals=[]
 for k in range(dx+1):
  for I in range(dt+1):
   for J in range(du+1):
    b=sum(p.coeff_monomial(t**i*u**h*x**k)*S.binomial(I,i)/S.binomial(dt,i)*S.binomial(J,h)/S.binomial(du,h) for i in range(I+1) for h in range(J+1))
    vals.append((b,(k,I,J)))
 return min(vals),sum(1 if b<0 else 0 for b,_ in vals),(dx,dt,du)
for N0 in [6,10,11,20,50,100]:
 aa=(L-1+(L+2)*t)/3;jj=1+(aa-1)*u
 for name,p in [('left',P),('endleft',Pl),('righta',Pj.subs(j,a)),('rightL',Pj.subs(j,L-1))]:
  e=S.expand(p.subs(j,jj).subs(a,aa).subs(L,N0+x))
  print(N0,name,bern(e),flush=True)
