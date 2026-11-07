from fractions import Fraction as F
from itertools import product
import sympy as s

checks=0
def ck(x):
    global checks
    assert x
    checks+=1

t,r,k=s.symbols('t r k', real=True)
z=s.symbols('z', real=True)
h=1-t
A=(2-t)*r+k
B=(1+t)*r-k
for C,l,sign,den in [(A*A/(2*h),A/h,1,h),(s.Rational(9,2)*r*r-B*B/(2*t),B/t,-1,t)]:
    ck(s.simplify(s.diff(C,k)-l)==0)
    ck(s.simplify(s.diff(C,t)-(l*l/2-r*l))==0)
    ck(s.simplify(s.diff(C,k,2)-sign/den)==0)
    ck(s.simplify(s.diff(C,k,t)-sign*(l-r)/den)==0)
    ck(s.simplify(s.diff(C,t,2)-sign*(l-r)**2/den)==0)
    ck(s.simplify(l.subs(k,(1-2*t)*r)-3*r)==0)
a,b,l,c,L=s.symbols('a b l c L',real=True)
v=s.Matrix([-1,l-a]);w=s.Matrix([1,l-b])
E=v*v.T/h-w*w.T/t
ck(s.simplify(E.det()+(a+b-2*l)**2/(h*t))==0)
H=E-s.diag(0,(L-c)**2/t)
ck(s.simplify(H.det()+(a+b-2*l)**2/(h*t)+(L-c)**2/t*(1/h-1/t))==0)
ck(s.simplify(E[0,1].subs(t,s.Rational(1,2))-2*(a+b-2*l))==0)
ck(s.simplify(H[1,1].subs({t:s.Rational(1,2),a:l,b:l,L:3*c})+8*c*c)==0)
D=a+b
ck(s.expand(D*D/8+s.Rational(9,2)*a*a-(2*a-b)**2/2-D*D-D*(13*a-11*b)/8)==0)
ck(s.expand(D*D/8-(2*a-b)**2/2-3*(b-a)*(5*a-b)/8)==0)


def clip(poly,u,k):
    out=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        fp=u[0]*p[0]+u[1]*p[1]+k
        fq=u[0]*q[0]+u[1]*q[1]+k
        if fp>=0:out.append(p)
        if (fp<0<fq) or (fq<0<fp):
            tau=fp/(fp-fq)
            out.append(tuple(p[j]+tau*(q[j]-p[j]) for j in (0,1)))
    return out

def area(poly):
    if not poly:return F(0)
    return abs(sum(p[0]*q[1]-p[1]*q[0] for p,q in zip(poly,poly[1:]+poly[:1])))/2

def cap(r,theta,k):
    if k<=-(2-theta)*r:return F(0)
    if k<=(1-2*theta)*r:return ((2-theta)*r+k)**2/(2*(1-theta))
    if k<=(1+theta)*r:return F(9,2)*r*r-((1+theta)*r-k)**2/(2*theta)
    return F(9,2)*r*r

def f(r,k):
    if k<=-2*r:return F(0)
    if k>=r:return F(9,2)*r*r
    return (2*r+k)**2/2

for r,theta in product([F(1,3),F(1),F(7,4)],[F(1,5),F(1,2),F(4,5)]):
    poly=[(-r,-r),(2*r,-r),(-r,2*r)]
    breaks=[-(2-theta)*r,(1-2*theta)*r,(1+theta)*r]
    values=breaks+[x-F(1,7) for x in breaks]+[x+F(1,7) for x in breaks]
    for k in values:
        ck(area(clip(poly,(F(1),theta),k))==cap(r,theta,k))

for a,b in product([F(i,5) for i in range(1,11)],repeat=2):
    bp=sorted(set([-a,2*a,-2*b,b]))
    candidates=bp+[bp[0]-1,bp[-1]+1]
    if a/F(2)<=b<=2*a:candidates.append(a-b)
    vals=[f(a,-al)+f(b,al) for al in candidates]
    mn=min((a+b)**2,F(9,2)*a*a,F(9,2)*b*b)
    mx=max(F(9,2)*a*a+max(2*b-a,F(0))**2/2,F(9,2)*b*b+max(2*a-b,F(0))**2/2)
    ck(min(vals)==mn)
    ck(max(vals)==mx)
    c=(a+b)/2
    plus=2*c*c+mn
    minus=F(5,2)*c*c+F(9,2)*(a*a+b*b)-mx
    ck(minus>plus)
    for theta in [F(1,4),F(1,2),F(3,4)]:
        for al in [F(-2),F(-1,3),F(0),F(2,3),F(3)]:
            actual=cap(a,theta,-al)+cap(c,theta,F(0))+cap(b,theta,al)
            ck(actual>=plus)
    glob=max(2*a*a,2*b*b,plus)
    ck(glob>=a*a+b*b+c*c)
print(f'PASS: {checks} exact checks')
