"""Exact algebra and actual polygon checks; no floating-point certificates."""
from fractions import Fraction as F
import sympy as s

checks=0
def check(x):
    global checks
    assert x
    checks+=1

def clip(poly,level,positive=True):
    ans=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        a=(p[0]-level)*(1 if positive else -1)
        b=(q[0]-level)*(1 if positive else -1)
        if a>=0:ans.append(p)
        if a*b<0:
            t=a/(a-b)
            ans.append(tuple(p[j]+t*(q[j]-p[j]) for j in range(2)))
    return ans

def moments(poly):
    cross=[p[0]*q[1]-p[1]*q[0] for p,q in zip(poly,poly[1:]+poly[:1])]
    area=sum(cross)/2
    mx=sum((p[0]+q[0])*a for p,q,a in zip(poly,poly[1:]+poly[:1],cross))/6
    my=sum((p[1]+q[1])*a for p,q,a in zip(poly,poly[1:]+poly[:1],cross))/6
    return area,mx,my

k=F(1725,577);c=F(91,345);l=F(22,345)
K=[(F(0),-k),(F(1),F(0)),(F(0),k)]
A=clip(clip(K,l),c,False)
vol,mx,my=moments(A)
check(vol==1 and my==0)
check(mx==F(31807,199065))
check(moments(K)==(k,k/3,F(0)))
check((k/3+2*mx)/(k+2)==c)
P=moments(clip(K,c))[0]
check(P==F(64516,39813))
check(moments(clip(A,c))[0]==0)
check(P/(k+2)==F(64516,198651))
check((k+2)/3-P==F(567,13271))
check(P-(k+1)/3==F(11570,39813))
check(F(1)<k<F(3))

h=s.symbols('h',real=True)
a=(2+4*h**3)/(3-6*h*h);b=a+h
kk=s.factor(1/(b*b-a*a))
rho=s.factor(a*a/(1+2*(b*b-a*a)))
check(s.factor(3*a-2-6*a*h*h-4*h**3)==0)
check(s.factor(kk-3*(1-2*h*h)/(h*(2*h**3+3*h+4)))==0)
check(s.factor(rho-4*(2*h**3+1)**2/(3*(1-2*h*h)*(4*h**4+8*h+3)))==0)
check(s.factor(s.diff(kk,h)-6*(2*h*h+1)*(2*h**3-3*h-2)/(h*h*(2*h**3+3*h+4)**2))==0)
check(s.factor(s.diff(rho,h)-16*(2*h**3+1)*(2*h**3-3*h-2)*(2*h**3-6*h*h-3*h+1)/(3*(2*h*h-1)**2*(4*h**4+8*h+3)**2))==0)
poly0=2*h**4+5*h*h+4*h-1
polystar=2*h**3-6*h*h-3*h+1
check(poly0.subs(h,s.Rational(19,100))<0<poly0.subs(h,s.Rational(1,5)))
check(polystar.subs(h,s.Rational(23,100))>0>polystar.subs(h,s.Rational(7,30)))
check(s.factor(1-b-polystar/(3-6*h*h))==0)
check(s.factor(kk-3+3*poly0/(h*(2*h**3+3*h+4)))==0)
check(a.subs(h,s.Rational(1,5))==s.Rational(254,345))

for den in range(5,81):
    for num in range(1,den):
        hh=F(num,den)
        if not F(19,100)<=hh<=F(7,30):continue
        aa=(2+4*hh**3)/(3-6*hh*hh);bb=aa+hh
        kv=1/(bb*bb-aa*aa)
        if bb>1 or kv>3:continue
        cv=1-aa;lv=1-bb
        body=[(F(0),-kv),(F(1),F(0)),(F(0),kv)]
        end=clip(clip(body,lv),cv,False)
        av,am,an=moments(end)
        check(av==1 and an==0)
        check((kv/3+2*am)/(kv+2)==cv)
        check(moments(clip(body,cv))[0]==kv*aa*aa)
        check(F(1)<kv<=F(3))

print(f'PASS: {checks:,} exact identities and actual-polygon checks')
