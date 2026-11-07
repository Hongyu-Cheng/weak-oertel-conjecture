from fractions import Fraction as F
import sympy as s
from itertools import product
checks=0
def ck(v):
    global checks
    assert v
    checks+=1
rho,c,ep,h1,h2,x,y,al,th=s.symbols('rho c ep h1 h2 x y al th', real=True)
R=c*c+2*rho*rho;W=c+2*rho;la=c/W;D=2*R/W**2
q=D*(h1*h1+h1*h2+h2*h2)/3
y21=(D*h1*h1/2-q)/(2*W);y22=(D*h2*h2/2-q)/(2*W)
E=(2-th)*rho-x-th*y
O=(2-th)*c+ep*(h1+th*h2)-x-th*y
Q=((E-al)**2+(E+al)**2+O*O)/(2*(1-th))
base={ep:0,x:0,y:0,al:0,th:0}
ck(s.simplify(Q.subs(base)-2*R)==0)
ck(s.simplify(s.diff(Q,al)-2*al/(1-th))==0)
ck(s.simplify(s.diff(Q,al,2).subs(base)-2)==0)
ck(s.simplify(s.diff(Q,al,th).subs(base))==0)
ck(s.simplify(s.diff(Q,th,2).subs(base)-R)==0)
ck(s.simplify(s.diff(Q,x).subs(base)+2*W)==0)
path={x:ep*la*h1+ep*ep*y21,y:ep*la*h2+ep*ep*y22,al:0}
J=s.diff(Q,th).subs(th,0).subs(path)
ck(s.simplify(s.diff(J,ep).subs(ep,0))==0)
ck(s.simplify(2*la**2+(1-la)**2-D)==0)
for u in [(1,0),(0,1),(-1,-1)]:
    dot=u[0]*h1+u[1]*h2
    yp=ep*la*dot+ep*ep*(u[0]*y21+u[1]*y22)
    qi=(2*(2*rho-yp)**2+(2*c+ep*dot-yp)**2)/2
    ck(s.simplify(s.diff(qi,ep).subs(ep,0))==0)
    ck(s.simplify(s.diff(qi,ep,2).subs(ep,0)/2-q)==0)
ck(s.expand(h1*h1+h1*h2+h2*h2-((h1+h2/2)**2+s.Rational(3,4)*h2*h2))==0)


def clip(poly,u,k):
    out=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        fp=sum(u[j]*p[j] for j in (0,1))+k
        fq=sum(u[j]*q[j] for j in (0,1))+k
        if fp>=0:out.append(p)
        if (fp<0<fq) or (fq<0<fp):
            tau=fp/(fp-fq)
            out.append(tuple(p[j]+tau*(q[j]-p[j]) for j in (0,1)))
    return out

def area(poly):
    if not poly:return F(0)
    return abs(sum(p[0]*q[1]-p[1]*q[0] for p,q in zip(poly,poly[1:]+poly[:1])))/2

for rv,cv,hv,epsv,tv in product([F(1),F(3,2)],[F(2),F(5,2)],[(F(1),F(0)),(F(1),F(-2)),(F(-2),F(-1))],[F(-1,100),F(1,100)],[F(-1,10),F(0),F(1,10)]):
    if cv<=rv:continue
    w=cv+2*rv;ll=cv/w;dd=2*(cv*cv+2*rv*rv)/w**2
    qq=dd*(hv[0]**2+hv[0]*hv[1]+hv[1]**2)/3
    yy=[epsv*ll*hv[j]+epsv**2*(dd*hv[j]**2/2-qq)/(2*w) for j in (0,1)]
    total=F(0);formula=F(0)
    for z in (-1,0,1):
        rr=cv if z==0 else rv
        shift=[epsv*hv[j] if z==0 else F(0) for j in (0,1)]
        poly=[(shift[0]-rr,shift[1]-rr),(shift[0]+2*rr,shift[1]-rr),(shift[0]-rr,shift[1]+2*rr)]
        kk=-yy[0]-tv*yy[1]
        total+=area(clip(poly,(F(1),tv),kk))
        ht=(2-tv)*rr+shift[0]+tv*shift[1]+kk
        formula+=ht*ht/(2*(1-tv))
    ck(total==formula)
    # Exact actual containment: -epsilon*h belongs (c-rho)T.
    v=[-epsv*h for h in hv];delta=cv-rv
    ck(v[0]>=-delta and v[1]>=-delta and v[0]+v[1]<=delta)
print(f'PASS: {checks} exact checks')
