from fractions import Fraction as F
import sympy as s
checks=0
def ck(x):
    global checks
    assert x
    checks+=1

u,v=s.symbols('u v',positive=True)
h=lambda w:(w+1/w)/2
ell=lambda w:(w-1/w)/2
mu=lambda w:w/2+1/(6*w**3)
H=(h(u)+h(v))/2;L=(ell(u)+ell(v))/2
m=(H**2-L**2)/2
g=(H**3-L**3)/(3*m)
ck(s.factor(m-(u+v)**2/(8*u*v))==0)
ck(s.factor(g-(u+v)*(3*u*u*v*v+1)/(12*u*u*v*v))==0)
ck(s.factor(g-(mu(u)+mu(v))/2+(u-v)**2*(u+v)/(12*u**3*v**3))==0)
e=s.symbols('e',positive=True)
ue=1+e+2*e*e;ve=1+e
tau=2*g-h(u)
D=s.factor((s.Rational(4,9)-(h(v)**2-tau**2)/2).subs({u:ue,v:ve}))
P=4+30*e+132*e**2+374*e**3+735*e**4+1035*e**5+1033*e**6+710*e**7+300*e**8+56*e**9
ck(s.factor(D-e**3*P/(18*(1+e)**4*ue**4))==0)
ck(s.factor((m-s.Rational(1,2)).subs({u:ue,v:ve})-e**4/(2*(1+e)*ue))==0)
ck(all(x>0 for x in s.Poly(P,e).all_coeffs()))
ck(s.limit(D/e**3,e,0)==s.Rational(2,9))


def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
def hull(points):
    points=sorted(set(points));lo=[];hi=[]
    for p in points:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=0:lo.pop()
        lo.append(p)
    for p in reversed(points):
        while len(hi)>=2 and cross(hi[-2],hi[-1],p)<=0:hi.pop()
        hi.append(p)
    return lo[:-1]+hi[:-1]
def area_centroid(poly):
    terms=[p[0]*q[1]-p[1]*q[0] for p,q in zip(poly,poly[1:]+poly[:1])]
    a=sum(terms)/2
    c=[sum((p[j]+q[j])*t for p,q,t in zip(poly,poly[1:]+poly[:1],terms))/(6*a) for j in (0,1)]
    return a,tuple(c)
def strip(w):
    a=(w-1/w)/2;b=(w+1/w)/2
    return [(a,-a/2),(b,-b/2),(b,b/2),(a,a/2)]
def clip(poly,threshold):
    out=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        fp=p[0]-threshold;fq=q[0]-threshold
        if fp>=0:out.append(p)
        if (fp<0<fq) or (fq<0<fp):
            t=fp/(fp-fq)
            out.append((p[0]+t*(q[0]-p[0]),p[1]+t*(q[1]-p[1])))
    return out
for ee in [F(1,100),F(1,101),F(1,200),F(1,1000),F(1,10000)]:
    uu=1+ee+2*ee*ee;vv=1+ee
    A=strip(uu);B=strip(vv)
    aa,ga=area_centroid(A);bb,gb=area_centroid(B)
    ck(aa==bb==F(1,2))
    M=hull([((p[0]+q[0])/2,(p[1]+q[1])/2) for p in A for q in B])
    mm,gm=area_centroid(M)
    ck(mm==(uu+vv)**2/(8*uu*vv))
    gg=(uu+vv)*(3*uu*uu*vv*vv+1)/(12*uu*uu*vv*vv)
    ck(gm==(gg,F(0)))
    hh=(uu+1/uu)/2;tb=2*gg-hh
    ck((vv-1/vv)/2<tb<(vv+1/vv)/2)
    # A's closed supporting edge is retained as a set, with zero area.
    ca=clip(A,hh);ck(len(set(ca))==2)
    cb=clip(B,tb);cc,_=area_centroid(cb)
    expected=(((vv+1/vv)/2)**2-tb*tb)/2
    ck(cc==expected)
    ck(cc<F(8,9)*(1-mm))
    shift=(ga[0]+gb[0])/2-gg
    ck(shift>0)
    oldt=ga[0]+gb[0]-hh
    oldc=(((vv+1/vv)/2)**2-oldt*oldt)/2
    ck(cc>oldc)
    if ee==F(1,100):
        ck(F(8,9)*(1-mm)-cc==F(13214404325059960523,60958950114838265933040900))
        ck(mm==F(102030201,204060400))

# Exact endpoint-minimum root inequality in the residual proof for d=2.
# (sqrt(x)+sqrt(y))^2 >= (sqrt(a)+sqrt(x+y-a))^2 reduces to xy>=a(x+y-a).
for aa in [F(1),F(2),F(7,3)]:
    for ix in range(1,11):
        for iy in range(1,11):
            xx=aa*ix/10;yy=aa*iy/10
            if xx+yy>=aa:ck(xx*yy>=aa*(xx+yy-aa))
print(f'PASS: {checks} exact checks')
