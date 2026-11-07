"""Exact actual polygon caps and algebra for the independent Schur audit."""
from fractions import Fraction as F
import sympy as s

checks=0
def eq(a,b):
    global checks
    assert s.simplify(a-b)==0, (a,b)
    checks+=1
def yes(p):
    global checks
    assert p
    checks+=1
def area(poly):
    if len(poly)<3:return F(0)
    return abs(sum(poly[i][0]*poly[(i+1)%len(poly)][1]-poly[(i+1)%len(poly)][0]*poly[i][1] for i in range(len(poly))))/2
def clip(poly,u,c):
    out=[]
    for i,P in enumerate(poly):
        Q=poly[(i+1)%len(poly)]
        f=u[0]*P[0]+u[1]*P[1]+c
        g=u[0]*Q[0]+u[1]*Q[1]+c
        if f>=0:out.append(P)
        if (f>0 and g<0) or (f<0 and g>0):
            t=f/(f-g)
            out.append((P[0]+t*(Q[0]-P[0]),P[1]+t*(Q[1]-P[1])))
    return out
T=[(F(-1),F(-1)),(F(2),F(-1)),(F(-1),F(2))]
normals=[(F(1),F(0)),(F(0),F(1)),(F(-1),F(-1))]
eq(area(T),F(9,2))
for j in [-1,0,1]:
    for theta in [F(-1,10),F(0),F(1,10)]:
        for alpha in [F(-1,8),F(0),F(1,8)]:
            for r,p,q in [(F(9,10),F(1,20),F(-1,30)),(F(1),F(0),F(0)),(F(11,10),F(-1,40),F(1,50))]:
                poly=[(p+r*x,q+r*y) for x,y in T]
                actual=area(clip(poly,(F(1),theta),alpha*j))
                formula=(2*r+p+alpha*j+theta*(q-r))**2/(2*(1-theta))
                eq(actual,formula)

for a in [F(-1,10),F(-1,20),F(0),F(1,20),F(1,10)]:
    for theta in [F(-1,10),F(0),F(1,10)]:
        for al in [(F(0),F(0),F(0)),(F(-1,10),F(1,20),F(1,20)),(F(-1,5),F(-1,10),F(0))]:
            yes(sum(al)<=0)
            masses=[]
            for i in range(3):
                u=tuple(normals[i][k]+theta*normals[(i+1)%3][k] for k in range(2))
                actual=F(0)
                for j in [-1,0,1]:
                    r=1+a*j
                    poly=[(r*x,r*y) for x,y in T]
                    actual+=area(clip(poly,u,al[i]*j))
                formula=6+F(3,2)*theta**2/(1-theta)+(2*a+al[i]-a*theta)**2/(1-theta)
                eq(actual,formula)
                masses.append(actual)
            yes(max(masses)>=6+4*min(a,0)**2)
    optalpha=-2*a if a>=0 else F(0)
    yes(3*optalpha<=0)
    for i in range(3):
        actual=sum(area(clip([((1+a*j)*x,(1+a*j)*y) for x,y in T],normals[i],optalpha*j)) for j in [-1,0,1])
        eq(actual,6+4*min(a,0)**2)
        # Actual finite right-endpoint isolation, not a limiting cap.
        iso=sum(area(clip([((1+a*j)*x,(1+a*j)*y) for x,y in T],normals[i],F(10)*(j-1))) for j in [-1,0,1])
        eq(iso,2*(1+a)**2)
        yes(iso<6)

a,al,th=s.symbols('a al th',real=True)
phi=sum((2*(1+a*j)+al*j-th*(1+a*j))**2 for j in [-1,0,1])/(2*(1-th))
expr=6+s.Rational(3,2)*th**2/(1-th)+(2*a+al-a*th)**2/(1-th)
eq(phi,expr)
K=s.hessian(phi,(al,th)).subs({al:-2*a,th:0})
eq(K[0,0],2);eq(K[0,1],-2*a);eq(K[1,1],3+2*a*a);eq(K.det(),6)
eq(expr.subs(al,0),6+4*a*a+(s.Rational(3,2)+a*a)*th*th/(1-th))
eq(s.Rational(4,9)*(s.Rational(27,2)+9*a*a),6+4*a*a)
eq(sum(2*(2*a)**2 for _ in range(3)),24*a*a)
eq(s.Rational(3,4)*24*a*a,18*a*a)
eq(2+s.Rational(9,2)*s.Rational(1,2)**2,s.Rational(25,8))
yes(F(25,8)<F(9,2))
# General exact equality-constrained square completion with redundant rows.
KM=s.diag(2,3,5); b=s.Matrix([2,-3,5]); R=s.Matrix([[1,1,0],[2,2,0]])
d=s.Matrix([1,2]); e=d+R*KM.inv()*b
w0=-KM.inv()*b
wstar=w0+KM.inv()*R.T*(R*KM.inv()*R.T).pinv()*e
eq((R*wstar-d).dot(R*wstar-d),0)
eq((wstar-w0).dot(KM*(wstar-w0)),e.dot((R*KM.inv()*R.T).pinv()*e))
print(f'PASS {checks} exact checks')
