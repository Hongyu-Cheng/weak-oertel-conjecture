exec(open('./open_tail_dual_bernstein.py').read().split('for N0 in')[0])
aa=(L-1+(L+2)*t)/3;jj=1+(aa-1)*u
base=S.expand(P.subs(j,jj).subs(a,aa).subs(L,11+x))
rects=[(0,S.Rational(1,4),0,S.Rational(1,2)),(S.Rational(1,4),S.Rational(1,2),0,S.Rational(1,2)),(0,S.Rational(1,2),S.Rational(1,2),1),(S.Rational(1,2),1,0,S.Rational(1,2)),(S.Rational(1,2),1,S.Rational(1,2),1)]
def bydegree(poly):
 pp=S.Poly(poly,t,u,x);dt,du,dx=pp.degree(t),pp.degree(u),pp.degree(x)
 arr=[]
 for k in range(dx+1):
  vals=[]
  for I in range(dt+1):
   for J in range(du+1):
    v=sum(pp.coeff_monomial(t**i*u**h*x**k)*S.binomial(I,i)/S.binomial(dt,i)*S.binomial(J,h)/S.binomial(du,h) for i in range(I+1) for h in range(J+1))
    vals.append(v)
  arr.append(min(vals))
 return arr
for rect in rects:
 t0,t1,u0,u1=map(S.Rational,rect)
 e=S.expand(base.subs({t:t0+(t1-t0)*t,u:u0+(u1-u0)*u},simultaneous=True))
 print(rect,bydegree(e))
print('Pl',bydegree(S.expand(Pl.subs(a,aa).subs(L,11+x))))
for LL in range(2,11):
 vals=[]
 for aa0 in range(1,LL):
  if not(LL-1<=3*aa0<2*LL+1):continue
  vals.append(Pl.subs({L:LL,a:aa0}))
  vals.extend(P.subs({L:LL,a:aa0,j:jj0}) for jj0 in range(1,aa0+1))
 print('finite',LL,len(vals),min(vals))
