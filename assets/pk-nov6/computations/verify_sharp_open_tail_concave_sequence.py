"""Exact polynomial coefficient certificate; no numerical sign sampling."""
import sympy as S
L,a,j,x,t,u=S.symbols('L a j x t u')
R=L-a;b=2*L+1-3*a;A=4*L*(L+1)-7*a*a-a
P0=4*L**3-28*L**2*a-4*L**2+63*L*a*a+13*L*a-42*a**3-6*a*a
P=(R*(7*R-1)-3*L*(L-j))*(L+1)*b-(L-j)*A*(L+j-3*a)
Pplus=(4*L*j-a*(7*a+1))*(L+1)*b-j*A*(L+j-3*a)
lam=3*A/(L*(L+1)*b)
FA=R*(7*R-1)/(2*L)-S.Rational(3,2)*(L+1)
DA=(L+1)*(L-1-3*a)/6
assert S.factor((FA-lam*DA)*2*L*b-P0)==0
FB=2*(L+1)-a*(7*a+1)/(2*L)
DB=(L+1)*(2*L+1-3*a)/6
assert S.factor(FB-lam*DB)==0
G=4*L*L-14*L*a+2*L+14*a*a-5*a-1
assert S.expand(G-14*(a-L/2-S.Rational(5,28))**2-(28*L*L-28*L-81)/56)==0
assert S.factor(Pplus.subs(j,a)-a*(R+1)*G)==0
assert S.factor(Pplus.subs(j,L-1)-2*(4*L**3-4*L-3*a*(L-a)*(7*a+1)))==0

def minima(E):
 pp=S.Poly(E,t,u,x);dt,du,dx=pp.degree(t),pp.degree(u),pp.degree(x)
 out=[]
 for k in range(dx+1):
  bs=[]
  for I in range(dt+1):
   for J in range(du+1):
    v=sum(pp.coeff_monomial(t**ii*u**jj*x**k)*S.binomial(I,ii)/S.binomial(dt,ii)*S.binomial(J,jj)/S.binomial(du,jj) for ii in range(I+1) for jj in range(J+1))
    assert v>=0
    bs.append(v)
  out.append(min(bs))
 return out

aa=(L-1+(L+2)*t)/3;jj=1+(aa-1)*u
assert minima(S.expand(P0.subs(a,aa).subs(L,11+x)))==list(map(S.Rational,['65/9','161/9','25/9','1/9']))
base=S.expand(P.subs(j,jj).subs(a,aa).subs(L,11+x))
rows=[('0','1/4','0','1/2',['4904269/9216','1345403/6912','24071/768','7715/3456','221/3456']),('1/4','1/2','0','1/2',['6713755/13824','1617115/6912','196775/4608','8057/2304','8051/82944']),('0','1/2','1/2','1',['496429/864','196495/864','10501/288','2317/864','1/16']),('1/2','1','0','1/2',['99693/64','20861/32','807/8','219/32','11/64']),('1/2','1','1/2','1',['61281/64','5867/16','1677/32','53/16','5/64'])]
for t0,t1,u0,u1,expected in rows:
 t0,t1,u0,u1=map(S.Rational,[t0,t1,u0,u1])
 E=S.expand(base.subs({t:t0+(t1-t0)*t,u:u0+(u1-u0)*u},simultaneous=True))
 assert minima(E)==list(map(S.Rational,expected))
finite=[(2,0),(5,0),(5,0),(7,0),(12,12),(12,18),(15,76),(22,54),(22,72)]
for LL,expect in zip(range(2,11),finite):
 vals=[]
 for aa0 in range(1,LL):
  if not(LL-1<=3*aa0<2*LL+1):continue
  vals.append(P0.subs({L:LL,a:aa0}))
  vals.extend(P.subs({L:LL,a:aa0,j:jj0}) for jj0 in range(1,aa0+1))
 assert (len(vals),min(vals))==expect and min(vals)>=0
w=[4,3,2,1];z=[-1,0,1,2]
assert sum(i*v for i,v in zip(z,w))==0
assert S.Rational(3,7)==S.Rational(sum(v for i,v in zip(z,w) if i>0),sum(v for i,v in zip(z,w) if i!=0))
assert S.Rational(3,7)-S.Rational(1,2)*S.Rational(3,7)**2==S.Rational(33,98)
assert S.Rational(33,98)-S.Rational(1,3)==S.Rational(1,294)
print('PASS: generator identities, every Bernstein coefficient, finite integer cases, sharpness, and central-only cap bound.')
