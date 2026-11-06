"""Exact triangle chords, strip extremizers, and roof algebra."""
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
def clip(poly,u,c):
    out=[]
    for i,P in enumerate(poly):
        Q=poly[(i+1)%len(poly)]
        f=u[0]*P[0]+u[1]*P[1]+c;g=u[0]*Q[0]+u[1]*Q[1]+c
        if f>=0:out.append(P)
        if (f>0 and g<0) or (f<0 and g>0):
            v=f/(f-g);out.append(tuple(x+v*(y-x) for x,y in zip(P,Q)))
    return out
def area(poly):
    if len(poly)<3:return F(0)
    return abs(sum(poly[i][0]*poly[(i+1)%len(poly)][1]-poly[(i+1)%len(poly)][0]*poly[i][1] for i in range(len(poly))))/2
T=[(F(-2),F(1)),(F(1),F(-2)),(F(1),F(1))]
def chord(c,ss):
    pts=[(-x-y,x+c*(x+y)) for x,y in T]
    vals=[]
    for i,(t0,s0) in enumerate(pts):
        t1,s1=pts[(i+1)%3]
        if s0==s1:
            if ss==s0:vals.extend([t0,t1])
        elif min(s0,s1)<=ss<=max(s0,s1):
            vals.append(t0+(ss-s0)*(t1-t0)/(s1-s0))
    return min(vals),max(vals)
for c in [F(-1),F(-3,4),F(-1,2),F(-1,4),F(0)]:
    for vv in [F(1,5),F(1),F(2),F(14,5)]:
        if c>-1:
            L,U=chord(c,-2-c+(1+c)*vv);eq(U,1);eq(U-L,vv)
        if c<0:
            L,U=chord(c,1-c+c*vv);eq(U,1);eq(U-L,vv)
    for v0 in [F(0),F(1,3),F(1),F(5,2)]:
        left=-2-c+(1+c)*v0;right=1-c+c*v0
        u=(1+c,c)
        B=clip(clip(T,u,-left),tuple(-q for q in u),right)
        eq(area(B),(9-v0*v0)/2)
        eq(right-left,3-v0)
for c in [F(1,5),F(1),F(5,2),F(7)]:
    m=1+c
    for fraction in [F(1,5),F(1,2),F(4,5)]:
        vv=3*fraction/m
        L,U=chord(c,-2-c+m*vv);eq(U,1);eq(U-L,vv)
        L,U=chord(c,1+2*c-c*m*vv);eq(U,-2+m*vv);eq(U-L,vv)
    for H in [F(7,2),F(4),F(17,4),F(9)]:
        for multiplier in [F(1),F(5,4),F(2),F(7)]:
            lam=H*m*multiplier/3
            Fc=F(9,2)-m*H*H/(2*lam*lam)-c*m*(H-3)**2/(2*(lam-m)**2)
            F0=F(9,2)-H*H/(2*lam*lam)
            yes(0<=Fc<=F0<=F(9,2))
            if multiplier==1:eq(Fc,0)

h,U,L=s.symbols('h U L',real=True)
eq(h+U-(h+1)*(U-L)/3,((h-2)*(1-U)+(h+1)*(L+2))/3)
H,v0=s.symbols('H v0',positive=True)
lam=H/v0;b=(9-v0*v0)/2
eq(lam*b-(s.Rational(9,2)*lam+H*H/(2*lam)-3*H),H*(3-v0))
eq((9-s.Rational(3,8)**2)/2,s.Rational(567,128))
eq((9-(9*s.sqrt(3)/4-3)**2)/2,s.Rational(27,32)*(8*s.sqrt(3)-9))
print(f'PASS {checks} exact checks')
