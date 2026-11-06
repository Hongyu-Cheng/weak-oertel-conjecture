"""Independent exact actual cap-area and normalization checks."""
from fractions import Fraction as F
import sympy as s

checks=0
def eq(a,b):
    global checks
    assert s.simplify(a-b)==0,(a,b)
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
        f=u[0]*P[0]+u[1]*P[1]+c;g=u[0]*Q[0]+u[1]*Q[1]+c
        if f>=0:out.append(P)
        if (f>0 and g<0) or (f<0 and g>0):
            t=f/(f-g)
            out.append((P[0]+t*(Q[0]-P[0]),P[1]+t*(Q[1]-P[1])))
    return out
T=[(F(-1),F(-1)),(F(2),F(-1)),(F(-1),F(2))]
js=[-2,-1,0,1,2]
rs=[F(4,5),F(19,20),F(1),F(19,20),F(4,5)]
es=[F(1),F(0),F(-8,5),F(0),F(1)]
us=[(F(1),F(0)),(F(0),F(1)),(F(-1),F(-1))]
R=sum(r*r for r in rs);E=sum(e*e for e in es);Q=2*R
eq(R,F(817,200));eq(E,F(114,25));eq(Q,F(817,100))
eq(2*sum(r*r for r in rs[:4]),F(689,100))
eq(2*rs[3]**2+F(9,2)*rs[4]**2,F(937,200))
yes(F(689,100)>F(937,200))
for a in [F(-1,500),F(0),F(1,500)]:
    for b in [F(-1,500),F(0),F(1,500)]:
        radii=[r+a*j+b*e for r,j,e in zip(rs,js,es)]
        yes(min(radii)>0)
        for i in range(1,4):yes(radii[i-1]-2*radii[i]+radii[i+1]<0)
        RR=sum(r*r for r in radii);JJ=sum(j*r for j,r in zip(js,radii))
        eq(RR,R+10*a*a+E*b*b);eq(JJ,10*a)
        for th in [F(-1,50),F(0),F(1,50)]:
            for al in [F(-1,50),-2*a,F(0),F(1,50)]:
                for i in range(3):
                    u=tuple(us[i][k]+th*us[(i+1)%3][k] for k in range(2))
                    val=sum(area(clip([(r*x,r*y) for x,y in T],u,al*j)) for j,r in zip(js,radii))
                    formula=((2-th)**2*RR+2*al*(2-th)*JJ+10*al*al)/(2*(1-th))
                    eq(val,formula)
                    yes(val>=Q+2*E*b*b)
        for direction in [-1,1]:
            # Right ownership needs al<=0; left ownership al>=0.
            al=-2*a if direction*a>=0 else F(0)
            yes(direction*al<=0)
            value=sum(area(clip([(r*x,r*y) for x,y in T],us[0],al*j)) for j,r in zip(js,radii))
            eq(value,Q+2*E*b*b+20*min(direction*a,0)**2)
        kk=R/(R+E*b*b)
        eq(F(9,2)*RR*kk-F(9,2)*R,45*R*a*a/(R+E*b*b))
        yes(F(9,2)*RR*kk>=F(9,2)*R)

a,b,al,th=s.symbols('a b al th',real=True)
rr=s.Rational(R.numerator,R.denominator);ee=s.Rational(E.numerator,E.denominator)
phi=(2-th)**2*(rr+ee*b*b)/(2*(1-th))+5*(al+(2-th)*a)**2/(1-th)
K=s.hessian(phi,(al,th)).subs({al:-2*a,th:0})
eq(K.det(),10*(rr+ee*b*b))
eq(K[0,0],10);eq(K[0,1],-10*a)
eq(K[1,1],rr+ee*b*b+10*a*a)
eq(s.diff(phi.subs({al:0,th:0}),a,2),40)
eq(s.diff(phi.subs({al:0,th:0}),b,2),s.Rational(456,25))
eq(s.Rational(3,4)*3*40,90)
print(f'PASS {checks} exact checks')
