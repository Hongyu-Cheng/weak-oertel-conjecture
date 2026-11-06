"""Exact rectangle identities; no numerical evidence enters the proof."""
from fractions import Fraction as F
import sympy as s

R,m=s.symbols('R m',positive=True)
mass=(R+2+1/R)/4
whole=mass/2+s.Rational(1,2)+1/(2*R)
assert s.factor(whole-s.Rational(4,3)-(3*R-5)*(R-3)/(24*R))==0
assert whole.subs(R,2)==s.Rational(21,16)
assert mass.subs(R,2)==s.Rational(9,8)
assert s.factor(s.diff(whole,R)-(R*R-5)/(8*R*R))==0
assert s.factor((7*m-2)**2-36*m*(m-1)-(13*m*m+8*m+4))==0
added=F(1,2)*F(3,4)*(F(17,3)-F(3,4))
k=F(9,8)+added
assert added==F(59,32) and k==F(95,32)
assert (k+1)/3-F(21,16)==F(1,96)
assert (k+1)/3-F(4,9)*k==F(1,288)
assert F(2,9)*(k+2)==F(53,48)
checks=9

def tail(width,threshold):
    return max(F(0),min(F(1),(width/2-threshold)/width))

for den in range(1,17):
    for num in range(den,7*den+1):
        r=F(num,den)
        pair=F(1,2)+1/(2*r)
        assert tail(F(1),F(1,2))+tail(r,-F(1,2))==pair
        checks+=1
        for alpha in [-r,-r/2,-F(1,2),F(0),F(1,2),r/2,r]:
            assert tail(F(1),alpha)+tail(r,-alpha)>=pair
            checks+=1

# The appended pentagon calculation controls every normal analytically;
# these exact identities and rational polygon clips independently check
# each status formula, including its seams.
w,t=s.symbols('w t',positive=True)
T=2*w-1
g=(w*w-s.Rational(1,3))/T
aa=w*(2*g-w)
bb=(w-g)**2
e1=g*g/(1-t*t)
e2=g+(t-1)/2+g*g/(2*(1+t))
e3=T/2+(aa*t-bb)/(2*t*(1+t))
tstar=(w-g)/(2*g-w)
assert s.factor(aa+bb-g*g)==0
assert s.factor(e1.subs(t,1-g)-e2.subs(t,1-g))==0
assert s.factor(e2.subs(t,w-g)-e3.subs(t,w-g))==0
assert s.factor(e3.subs(t,tstar)-(T/2+(2*g-w)**2/2))==0
assert s.factor(T/2-(2*g-w)**2/2-g*g-(w-1)**2*(1-6*(w-1)**2)/(6*T*T))==0
assert s.factor(g*g-s.Rational(4,9)*T-(w-1)**3*(9*w-5)/(9*T*T))==0
assert s.factor(s.diff(e3,t)-(-aa*t*t+2*bb*t+bb)/(2*t*t*(1+t)**2))==0
checks+=7

def clip(poly,tx,threshold):
    out=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        hp=p[0]+tx*p[1]-threshold
        hq=q[0]+tx*q[1]-threshold
        if hp<=0:
            out.append(p)
        if (hp<0<hq) or (hq<0<hp):
            u=hp/(hp-hq)
            out.append(tuple(p[j]+u*(q[j]-p[j]) for j in range(2)))
    return out

def area(poly):
    return abs(sum(p[0]*q[1]-p[1]*q[0] for p,q in zip(poly,poly[1:]+poly[:1])))/2

ws={F(77,59)}
for den in range(1,25):
    for num in range(den,3*den//2+1):
        ww=F(num,den)
        if 6*(ww-1)**2<=1:
            ws.add(ww)
for ww in sorted(ws):
    total=2*ww-1
    gg=(ww*ww-F(1,3))/total
    poly=[(F(0),F(0)),(F(1),F(-1)),(ww,F(-1)),(ww,F(1)),(F(1),F(1))]
    assert area(poly)==total
    crit=(ww-gg)/(2*gg-ww)
    assert 0<1-gg<=ww-gg<=crit
    ts={F(0),1-gg,ww-gg,crit,2*crit}
    for denom in range(1,9):
        for numer in range(0,5*denom):
            ts.add(F(numer,denom))
    for tt in ts:
        if tt<=1-gg:
            expected=gg*gg/(1-tt*tt)
        elif tt<=ww-gg:
            expected=gg+(tt-1)/2+gg*gg/(2*(1+tt))
        else:
            expected=total/2+(ww*(2*gg-ww)*tt-(ww-gg)**2)/(2*tt*(1+tt))
        actual=area(clip(poly,tt,gg))
        assert actual==expected
        assert actual>=gg*gg and total-actual>=gg*gg
        checks+=3
    checks+=2
ww=F(77,59); gg=(ww*ww-F(1,3))/(2*ww-1)
depth=F(59,32)*gg*gg
assert gg==F(14306,16815)
assert F(59,12)*gg-F(17,3)==-F(2537,1710)
assert depth==F(51165409,38338200)
assert depth-F(4,9)*F(95,32)==F(16119,1064950)
assert depth-F(127,96)==F(1788661,153352800)
checks+=5
mm,kk=s.symbols('mm kk',positive=True)
ww=1+mm/(2*(kk-mm))
gg=(ww*ww-s.Rational(1,3))/(2*ww-1)
d1=(8*kk*kk-4*kk*mm-mm*mm)**2/(144*kk*kk*(kk-mm))
d2=(32*kk**3+3*kk*mm*mm+mm**3)/(72*kk*kk)
n1=16*kk**4-16*kk**3*mm-48*kk**3+48*kk*kk*mm+8*kk*mm**3+mm**4
n2=8*kk**3-24*kk*kk+3*kk*mm*mm+mm**3
assert s.factor((kk-mm)*gg*gg-d1)==0
assert s.factor((kk-mm)*((2*ww-1)/2-(2*gg-ww)**2/2)-d2)==0
assert s.factor(d1-(kk+1)/3-n1/(144*kk*kk*(kk-mm)))==0
assert s.factor(d2-(kk+1)/3-n2/(72*kk*kk))==0
assert s.factor(s.diff(n1,mm)-(16*kk*kk*(3-kk)+24*kk*mm*mm+4*mm**3))==0
assert s.factor(s.diff(n1,kk)/8-(kk*kk*(8*kk-18-6*mm)+12*kk*mm+mm**3))==0
assert n1.subs({mm:1,kk:s.Rational(35,12)})==s.Rational(3361,1296)
assert n2.subs({mm:1,kk:s.Rational(35,12)})==s.Rational(881,216)
assert 3*F(8,19)**2<1
assert F(5)>F(20,9)**2
checks+=10
print(f'PASS: {checks:,} exact checks')
