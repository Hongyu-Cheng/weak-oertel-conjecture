"""Exact actual clipping and positive polynomial identities for a finite ear."""
from submission_text import read_submission
import ast
from fractions import Fraction as F
from pathlib import Path
import re
import sympy as s

checks=0
def ck(v):
    global checks
    assert v
    checks+=1

source=read_submission('7ea1c8120620b951')
r,p=s.symbols('r p')
X,Y=s.symbols('X Y',positive=True)
P=[s.Matrix([-1,-1]),s.Matrix([2,-1]),s.Matrix([X,Y]),s.Matrix([-1,2])]
normals=[s.Matrix([1,0]),s.Matrix([0,1]),s.Matrix([-1,-1])]
det=lambda a,b:s.det(s.Matrix.hstack(a,b))
area=lambda ps:s.factor(sum(det(a,b) for a,b in zip(ps,ps[1:]+ps[:1]))/2)
ck(s.expand(area(P)-s.Rational(3,2)*(X+Y+2))==0)
for i,e in enumerate([3*(Y+1),3*(X+Y-1),3*(X+1),9]):
    ck(s.expand(det(P[(i+1)%4]-P[i],P[(i+2)%4]-P[(i+1)%4])-e)==0)
for i,e in enumerate([3,X+2*Y,2*X+Y,3]):ck(det(P[i],P[(i+1)%4])==e)
S=[2+(X+Y-1)/(X+1),2+(X+Y-1)/(Y+1),s.Integer(2)]
Q=[(3*(X+Y-1)+6-S[0])/2,(3*(X+Y-1)+6-S[1])/2,s.Integer(2)]
for i,v in enumerate(normals):
    out=[];cuts=[]
    for x,y in zip(P,P[1:]+P[:1]):
        a=v.dot(x);b=v.dot(y)
        sa=s.sign(a.subs({X:2,Y:3}));sb=s.sign(b.subs({X:2,Y:3}))
        if sa>0:out.append(x)
        if sa*sb<0:
            w=x+a/(a-b)*(y-x);out.append(w);cuts.append(w)
    ck(len(cuts)==2)
    ck(s.cancel(area(out)-Q[i])==0)
    d=cuts[1]-cuts[0]
    # For the chosen balanced normals, coarea lengths are coordinate differences.
    sig=d[1] if i==0 else d[0]
    sig*=s.sign(sig.subs({X:2,Y:3}))
    ck(s.cancel(sig-S[i])==0)

D=4*p+3*r*r+10*r+8;c=s.Rational(3,2)*(r+2);k=s.Rational(3,2)*(r+3)
h=(4*p+r*r+7*r+8)/D;q=(p+r+2)/D
actual={r:X+Y-1,p:X*Y}
ck(s.cancel(h.subs(actual)-(1/S[0]+1/S[1]))==0)
ck(s.cancel(q.subs(actual)-1/(S[0]*S[1]))==0)
M=c*h;T=c*(h*h-2*q)-h/2+s.Rational(1,2);U=q*(c*c*q-c*h/2+s.Rational(1,4))/2
for f,g in [(M,sum(a/b for a,b in zip(Q,S))),(T,sum(a/b**2 for a,b in zip(Q,S))),(U,s.prod(a/b**2 for a,b in zip(Q,S)))]:
    ck(s.cancel(f.subs(actual)-g)==0)
E=M*M-k*T;R=M*M*E*E-4*k**3*U
E0=(r+2)*(9*r**4+73*r**3+198*r*r+228*r+96)+2*p*(9*r**4+71*r**3+186*r*r+210*r+96)+24*p*p*(r+1)*(r+2)
ck(s.cancel(E-3*E0/(4*D**2))==0)
poly=[]
for j in range(6):
    values=ast.literal_eval(re.search(r'\bP'+str(j)+r' = (\[[^\]]*\])',source).group(1))
    for v in values:ck(isinstance(v,int) and v>0)
    poly.append(sum(v*r**i for i,v in enumerate(values)))
A=[(r+2)**4*poly[0],12*(r+2)**3*poly[1],12*(r+2)**2*poly[2],32*(r+2)**2*poly[3],192*(r+2)**2*poly[4],1536*(r+2)**2*poly[5],1024*(3*r*r+11*r+9)*(9*r**3+54*r*r+109*r+72)]
R0=sum(A[j]*p**j for j in range(7))
ck(s.cancel(R-27*r*R0/(64*D**6))==0)
for f in [E0,R0]:
    for term,coef in s.Poly(f,r,p).terms():ck(coef>0)

# Independent rational clipping also includes tip-on-line seams and vanishing ears.
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def ar(ps):return sum(cross(a,b) for a,b in zip(ps,ps[1:]+ps[:1]))/2
def clip(ps,v):
    out=[]
    for a,b in zip(ps,ps[1:]+ps[:1]):
        fa=sum(x*y for x,y in zip(a,v));fb=sum(x*y for x,y in zip(b,v))
        if fa>=0:out.append(a)
        if fa*fb<0:
            t=fa/(fa-fb);out.append(tuple(a[j]+t*(b[j]-a[j]) for j in range(2)))
    return out
for x in [F(0),F(1,100),F(1,3),F(1),F(3),F(20)]:
    for y in [F(0),F(1,100),F(1,3),F(1),F(3),F(20)]:
        if x+y<1:continue
        ps=[(F(-1),F(-1)),(F(2),F(-1)),(x,y),(F(-1),F(2))]
        rr=x+y-1;pp=x*y;kk=F(3,2)*(rr+3)
        ss=[2+rr/(x+1),2+rr/(y+1),F(2)]
        qq=[(3*rr+6-ss[0])/2,(3*rr+6-ss[1])/2,F(2)]
        ck(ar(ps)==kk)
        for i,v in enumerate([(1,0),(0,1),(-1,-1)]):ck(ar(clip(ps,v))==qq[i])
        mm=sum(a/b for a,b in zip(qq,ss));tt=sum(a/b**2 for a,b in zip(qq,ss));uu=F(1)
        for a,b in zip(qq,ss):uu*=a/b**2
        ee=mm*mm-kk*tt;rrr=mm*mm*ee*ee-4*kk**3*uu
        ck(ee>0);ck(rrr>0 if rr>0 else rrr==0)


# Adjacent unique-tip branches and their exact factored coefficient bounds.
a=s.symbols('a'); V=r+a+2; W=3*r+2*a+4
Su=[2*V/(a+2),W/V,s.Integer(2)]
Qu=[Su[0],(3*r+6-Su[1])/2,s.Integer(2)]
Pu=[s.Matrix([-1,-1]),s.Matrix([2,-1]),s.Matrix([-a,r+1+a]),s.Matrix([-1,2])]
ck(s.expand(area(Pu)-k)==0)
for i,v in enumerate(normals):
    out=[];cuts=[]
    for x,y in zip(Pu,Pu[1:]+Pu[:1]):
        aa=v.dot(x);bb=v.dot(y)
        sa=s.sign(aa.subs({a:s.Rational(1,2),r:1}));sb=s.sign(bb.subs({a:s.Rational(1,2),r:1}))
        if sa>0:out.append(x)
        if sa*sb<0:
            w=x+aa/(aa-bb)*(y-x);out.append(w);cuts.append(w)
    ck(s.cancel(area(out)-Qu[i])==0)
    diff=cuts[1]-cuts[0];sig=diff[1] if i==0 else diff[0]
    sig*=s.sign(sig.subs({a:s.Rational(1,2),r:1}))
    ck(s.cancel(sig-Su[i])==0)
Mu=sum(x/y for x,y in zip(Qu,Su));Tu=sum(x/y**2 for x,y in zip(Qu,Su));Uu=s.prod(x/y**2 for x,y in zip(Qu,Su))
Eu=Mu**2-k*Tu;Ru=Mu**2*Eu**2-4*k**3*Uu
E1=12*(a+2)**3+3*(a+2)**2*(a+19)*r+3*(a+2)*(4*a+33)*r*r+(17*a+73)*r**3+9*r**4
ck(s.cancel(Eu-3*E1/(4*V*W**2))==0)
brackets=[205-182*a-17*a*a,18799-14241*a-3057*a*a-97*a**3,
903803-546492*a-211566*a*a-14684*a**3-165*a**4,
889157-376278*a-257322*a*a-29756*a**3-729*a**4,
801871-164870*a-253382*a*a-44598*a**3-1809*a**4,
381053+21565*a-112186*a*a-29895*a**3-1823*a**4,
510977+189486*a-100415*a*a-46894*a**3-4217*a**4,
59686+14249*a-6352*a*a-1325*a**3,9365+1403*a-319*a*a]
B=[5184*(1-a)*(a+2)**7,288*(a+2)**6*brackets[0],16*(a+2)**5*brackets[1],
(a+2)**4*brackets[2],2*(a+2)**3*brackets[3],3*(a+2)**2*brackets[4],
6*(a+2)*brackets[5],3*brackets[6],6*brackets[7],6*brackets[8],216*(2*a+25),s.Integer(243)]
R1=sum(x*r**j for j,x in enumerate(B))
ck(s.cancel(Ru-27*r*R1/(64*V**2*W**6))==0)
for polynomial,lower in zip(brackets,[6,1404,130896,225072,337212,237149,359451,52009,9046]):
    pp=s.Poly(polynomial,a)
    actual_lower=pp.nth(0)+sum(c for (j,),c in pp.terms() if j>0 and c<0)
    ck(actual_lower==lower and lower>0)
for aa in [F(0),F(1,100),F(1,3),F(3,4),F(99,100),F(1)]:
    for rr in [F(0),F(1,100),F(1,3),F(2),F(20)]:
        for reflect in [False,True]:
            ps=[(F(-1),F(-1)),(F(2),F(-1)),(-aa,rr+1+aa),(F(-1),F(2))]
            if reflect:ps=[(y,x) for x,y in reversed(ps)]
            kk=F(3,2)*(rr+3);ss=[2*(rr+aa+2)/(aa+2),(3*rr+2*aa+4)/(rr+aa+2),F(2)]
            qq=[ss[0],(3*rr+6-ss[1])/2,F(2)]
            if reflect:ss[0],ss[1]=ss[1],ss[0];qq[0],qq[1]=qq[1],qq[0]
            ck(ar(ps)==kk)
            for i,v in enumerate([(1,0),(0,1),(-1,-1)]):ck(ar(clip(ps,v))==qq[i])
            mm=sum(x/y for x,y in zip(qq,ss));tt=sum(x/y**2 for x,y in zip(qq,ss));uu=F(1)
            for x,y in zip(qq,ss):uu*=x/y**2
            ee=mm*mm-kk*tt;rrr=mm*mm*ee*ee-4*kk**3*uu
            ck(ee>0);ck(rrr>0 if rr>0 else rrr==0)
print(f'PASS: {checks} exact symbolic, coefficient and actual clipping checks')
