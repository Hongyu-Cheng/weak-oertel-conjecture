import sympy as s
from fractions import Fraction
from math import comb
a,b,x,y=s.symbols('a b x y');q=s.Rational
c=1/(3*a);rho=1/(3*(1-a));A=a/(2*a-1);L=(1-a)**2/((2*a-1)*(2-3*a));B=(2*a-1)/(2-3*a)
g=(2-3*a)/(9*(1-a));lam=(18*a**3-24*a*a+8*a-1)/(27*a*a*(a-1));v=(3*a-1)*(6*a-1)/(27*a*a)
M={'M0':q(9,2)-1/(2*a*(1-a)),'M1':g/(q(2,9)-v),'M2':q(3,2)+b+q(5,2)*b*b,'M6':s.Integer(6)}
k=[0,A*(b-c)**2,A*(b-c)**2-L*(b-rho)**2]
E=[(1-rho)**2/2-(1-rho)**3/(3*(1-b))]*2+[(1-b)**2/6]
bb=[c*y,c+(rho-c)*y,rho+(1-rho)*y]
J=3*a*a+2*a*y-4*a-y+1;D=12*a*a-9*a+1
Ds={(0,'M1'):-729*a**4*(-3*a+y)*(a-1)**3*D,(1,'M0'):1458*a**4*(a-1)**3*J,(1,'M2'):1458*a**4*(a-1)**3*J,(2,'M0'):-1458*a**3*(a-1)**3,(0,'M6'):729*a**4*(-3*a+y)*(a-1)**3,(1,'M6'):729*a**4*(a-1)**3*J,(2,'M6'):-729*a*a*(a-1)**3}
rows=[(0,'M1',q(1,2),q(3,5),0,1,9,3,q(3,512)),(1,'M0',q(1,2),q(11,20),0,q(1,2),9,3,q(3,256)),(1,'M0',q(1,2),q(11,20),q(1,2),1,9,3,q(3,256)),(1,'M2',q(11,20),q(3,5),0,q(1,2),9,3,q(13082,1953125)),(1,'M0',q(11,20),q(3,5),q(1,2),1,9,3,q(15032430113,256000000000)),(2,'M0',q(1,2),q(3,5),0,1,6,2,q(3,32)),(0,'M6',q(3,5),q(2,3),0,1,8,3,q(148954,390625)),(1,'M6',q(3,5),q(2,3),0,1,9,3,q(0)),(2,'M6',q(3,5),q(2,3),0,1,5,2,q(12664,3125))]
count=0
for i,m,l,h,yl,yh,nx,ny,want in rows:
 F=g+(lam-q(2,9))*M[m]+k[i]-lam*(b*b+(1-b)**2/3)-2*B*E[i]
 P=s.cancel(Ds[i,m]*F.subs(b,bb[i]))
 assert s.fraction(P)[1]==1 or s.fraction(P)[1].is_Number
 P=s.Poly(s.expand(P.subs({a:l+(h-l)*x,y:yl+(yh-yl)*y},simultaneous=True)),x,y)
 assert P.degree(x)<=nx and P.degree(y)<=ny
 coeff=P.as_dict(); vals=[]
 for ii in range(nx+1):
  for jj in range(ny+1):
   z=sum(vv*q(comb(ii,kk),comb(nx,kk))*q(comb(jj,ll),comb(ny,ll)) for (kk,ll),vv in coeff.items() if kk<=ii and ll<=jj)
   vals.append(z)
 assert min(vals)==want,(i,m,min(vals),want)
 assert min(vals)>=0
 count+=len(vals)
print('PASS',len(rows),'exact scalar rectangles and',count,'Bernstein coefficients')
