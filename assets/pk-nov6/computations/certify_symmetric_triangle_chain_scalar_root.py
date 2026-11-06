"""Exact rational Bernstein certificate search for a bounded scalar lemma.

This is not a proof of OC. The mathematical use of the lemma is audited
separately. No floating point arithmetic enters the certificates.
"""
import sympy as s
from math import comb
from fractions import Fraction

a, b, x, y = s.symbols('a b x y')
q=s.Rational
A=a/(2*a-1)
L=(1-a)**2/((2*a-1)*(2-3*a))
rho=1/(3*(1-a)); c=1/(3*a)
v=(3*a-1)*(6*a-1)/(27*a*a)
beta=(18*a**3-24*a*a+8*a-1)/(27*a*a*(a-1))
g=(2-3*a)/(9*(1-a)); B=(2*a-1)/(2-3*a)
M0=q(9,2)-1/(2*a*(1-a))
M1=s.factor(g/(q(2,9)-v))
Mb=q(3,2)+b+q(5,2)*b*b
ks=[s.Integer(0),A*(b-c)**2,A*(b-c)**2-L*(b-rho)**2]
Es=[(1-rho)**2/2-(1-rho)**3/(3*(1-b))]*2+[(1-b)**2/6]
bm=[c*y,c+(rho-c)*y,rho+(1-rho)*y]

def coeff(poly):
    P=s.Poly(poly,x,y)
    nx,ny=P.degree(x),P.degree(y)
    C={ij:Fraction(val) for ij,val in P.terms()}
    out=[]
    for i in range(nx+1):
        for j in range(ny+1):
            z=sum((v*Fraction(comb(i,k),comb(nx,k))*Fraction(comb(j,l),comb(ny,l))
                   for (k,l),v in C.items() if k<=i and l<=j), Fraction(0))
            out.append(z)
    return min(out),nx,ny

polys={}
for region,(k,E) in enumerate(zip(ks,Es)):
    for name,M in [('M0',M0),('M1',M1),('Mb',Mb),('six',s.Integer(6))]:
        F=s.factor(g+(beta-q(2,9))*M+k-beta*(b*b+(1-b)**2/3)-2*B*E)
        num,den=s.fraction(s.factor(F.subs(b,bm[region])))
        polys[region,name]=(num,den)

# Positive denominators on each stated parameter box. Their signs are
# proved in the companion note, not inferred by floating-point sampling.
J=3*a*a+2*a*y-4*a-y+1
Dpoly=12*a*a-9*a+1
positive_denominators={
 (0,'M1'):-729*a**4*(-3*a+y)*(a-1)**3*Dpoly,
 (1,'M0'):1458*a**4*(a-1)**3*J,
 (1,'Mb'):1458*a**4*(a-1)**3*J,
 (2,'M0'):-1458*a**3*(a-1)**3,
 (0,'six'):729*a**4*(-3*a+y)*(a-1)**3,
 (1,'six'):729*a**4*(a-1)**3*J,
 (2,'six'):-729*a**2*(a-1)**3,
}

def test(region,an,ad,al,ah,yl,yh,names):
    aa=al+(ah-al)*x; yy=yl+(yh-yl)*y
    for name in names:
        num,den=polys[region,name]
        dd=s.factor(den.subs({a:(al+ah)/2,y:(yl+yh)/2}))
        sign=1 if dd>0 else -1
        p=s.Poly(s.expand(sign*num.subs({a:aa,y:yy},simultaneous=True)),x,y)
        mn,nx,ny=coeff(p.as_expr())
        if mn>=0:
            return name,str(mn),(nx,ny)
    return None

if __name__=='__main__':
    rows=[
      (0,'M1',q(1,2),q(3,5),q(0),q(1)),
      (1,'M0',q(1,2),q(11,20),q(0),q(1,2)),
      (1,'M0',q(1,2),q(11,20),q(1,2),q(1)),
      (1,'Mb',q(11,20),q(3,5),q(0),q(1,2)),
      (1,'M0',q(11,20),q(3,5),q(1,2),q(1)),
      (2,'M0',q(1,2),q(3,5),q(0),q(1)),
      (0,'six',q(3,5),q(2,3),q(0),q(1)),
      (1,'six',q(3,5),q(2,3),q(0),q(1)),
      (2,'six',q(3,5),q(2,3),q(0),q(1)),
    ]
    for region,name,al,ah,yl,yh in rows:
        num,den=polys[region,name]
        P=s.cancel(num*positive_denominators[region,name]/den)
        assert s.fraction(P)[1]==1
        P=s.Poly(P,a,y).as_expr()
        P=s.expand(P.subs({a:al+(ah-al)*x,y:yl+(yh-yl)*y},simultaneous=True))
        mn,nx,ny=coeff(P)
        assert mn>=0,(region,name,mn)
        print(region,name,al,ah,yl,yh,(nx,ny),mn,flush=True)
    six_numerator=s.expand(-(27*a**3-44*a*a+20*a-2))
    mn,nx,ny=coeff(six_numerator.subs(a,q(3,5)+q(1,15)*x))
    assert mn==Fraction(1,125)
    print('PASS all nine exact Bernstein certificates; six-bound certificate',mn)
