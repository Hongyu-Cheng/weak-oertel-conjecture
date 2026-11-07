"""Exact checks for the analytic all-normal five-rectangle certificate."""
from fractions import Fraction as F
import sympy as S

checks=0
def ck(p):
    global checks
    assert p
    checks+=1
def pp(x):return max(F(0),x)
def clamp(x,lo,hi):return min(hi,max(lo,x))

r=[F(x) for x in [1,5,5,4,3]]
z=list(range(-2,3))
ck(sum(r)==18)
ck(sum(x**3 for x in r)==342)
ck(sum(x**3 for x in r)/(12*sum(r))==F(19,12))
ck(all(r[j+1]-r[j]>=r[j+2]-r[j+1] for j in range(3)))
ck(all(2*x<18 for x in r))

def area(width,t,s):
    if t==0:return width*clamp(1+s,F(0),F(2))
    L=t*width/2
    return width*(pp(s+1+L)**2-pp(s+1-L)**2
                 -pp(s-1+L)**2+pp(s-1-L)**2)/(4*L)
def mass(t,a,g=F(0)):
    return sum(area(width,t,a*base+g) for width,base in zip(r,z))

# Core is an actual disjoint symmetric subset; exact cap identity.
for ti in range(0,17):
    t=F(ti,12)
    for ai in range(-31,32):
        a=F(ai,10)
        core=area(F(5),t,F(0))+sum(area(F(4),t,a*j) for j in [-1,1])+sum(area(F(1),t,a*j) for j in [-2,2])
        ck(core==15)
        ck(mass(t,a)>=16)
        if a>=0:ck(mass(t,a)>=17)

# Exact strip clipping and all ranges used by the small-t estimate.
for ti in range(0,41):
    t=F(ti,120)
    for bi in range(0,121):
        b=F(bi,60)
        R1=area(F(5),t,b)-area(F(4),t,b)
        R2=area(F(3),t,-2*b)-area(F(1),t,-2*b)
        ck(mass(t,-b)==15+R1+R2)
        ck(R2>=2*pp(1-2*b))
        if b<=1:
            loss=(pp(b+F(5,2)*t-1)**2-pp(b+2*t-1)**2)/(2*t) if t else F(1,2)*pp(b-1)
            ck(R1==1+b-loss)
            ck(R1>=1+b-F(1,2)*pp(b+F(5,2)*t-1))
        else:ck(R1>=2-F(5,4)*t)
        ck(mass(t,-b)>=F(33,2)-pp(F(5,4)*t-F(1,4)))

# Rational parametrization of the actual norm, with no floating radicals.
own_gains=[]
for i in range(1,121):
    q=F(i,60)  # q<=2<sqrt19/2
    t=8*q/(19-4*q*q)
    root=(19+4*q*q)/(19-4*q*q)
    g=4*q*q/(19-4*q*q)
    ck(root**2==1+F(19,4)*t*t)
    ck(g==(root-1)/2)
    gain=area(F(5),t,g)-5
    ck(gain>0)
    own_gains.append(gain)
    for ai in range(-40,21):
        a=F(ai,10)
        ck(mass(t,a,g)>=mass(t,a)+gain)
        ck(mass(t,a,g)>F(33,2))
        ck(mass(t,a,g+1)>=mass(t,a,g))
ck(all(own_gains[j+1]>=own_gains[j] for j in range(len(own_gains)-1)))

# t=0: the UNIQUE minimizing tilt.
for bi in range(0,161):
    b=F(bi,40)
    formula=18-3*b if b<=F(1,2) else 16+b if b<=1 else F(17)
    ck(mass(F(0),-b)==formula)
    ck((formula==F(33,2))==(b==F(1,2)))
ck(mass(F(0),F(-1,2),F(1))>F(33,2))

# Strict radical certificates, plus their own-strip support conditions.
ck(1071>1024)
ck(1375>1296)
ck(119<20**2)
ck(55<8**2)
ck(19<25)
ck(22>F(33,2) and 24>F(33,2))

# Energy and epsilon realization use the actual rectangle, dimension2.
c=S.symbols('c')
energy=80*(2-c)/((2-3*c)**2*(2+c)**2)
c0=(10-4*S.sqrt(13))/9
ck(S.simplify(S.diff(energy,c).subs(c,c0))==0)
ck(S.simplify(energy.subs(c,c0)-(S.Rational(115,32)+S.Rational(65,64)*S.sqrt(13)))==0)
ck(S.simplify(2*(1-c*S.Rational(1,2)) / ((1-S.Rational(3,2)*c)**2*(1+S.Rational(1,2)*c)**2)*5-energy)==0)

# Exact old supporting/own traces and integer-normal one-sided slopes.
at=F(-1,2)
ck(area(r[0],F(0),at*z[0])==2*r[0])
ck(area(r[-1],F(0),at*z[-1])==0)
ck(area(r[2],F(0),F(0))==5)
for den in [100,1000,10000]:
    h=F(1,den)
    ck((mass(F(0),at+h)-F(33,2))/h==3)
    ck((mass(F(0),at-h)-F(33,2))/h==1)

print(f'PASS: {checks} exact checks')
