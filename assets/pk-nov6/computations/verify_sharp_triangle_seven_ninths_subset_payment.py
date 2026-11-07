"""Exact symbolic certificate for all triangle directions/threshold cells."""
import sympy as S
from fractions import Fraction as F

x,q,t=S.symbols('x q t',real=True)
D=x*(1-x)*(1-2*x)
cap=[S.Integer(1),1-q*q/(x*(1-x)),
     (1-x-q)**2/((1-x)*(1-2*x)),S.Integer(0)]
def branch(v,xx):
    if v<=0:return 0
    if v<=xx:return 1
    if v<=1-xx:return 2
    return 3
def eq(a,b):
    assert S.factor(a-b)==0,(a,b,S.factor(a-b))

tables=[]
for lo,hi in [(S.Rational(0),S.Rational(1,3)),
              (S.Rational(1,3),S.Rational(1,2))]:
    xx=(lo+hi)/2
    breaks=sorted([S.Integer(0),x,1-x,S.Rational(2,3),
                   S.Rational(2,3)-x,x-S.Rational(1,3)],
                  key=lambda a:a.subs(x,xx))
    own=cap[branch(S.Rational(1,3),xx)].subs(q,S.Rational(1,3))
    rows=[]
    for L,H in zip(breaks,breaks[1:]):
        qq=((L+H)/2).subs(x,xx)
        i,j=branch(qq,xx),branch(S.Rational(2,3)-qq,xx)
        N=S.cancel(D*(9*cap[i]+7*cap[j].subs(q,S.Rational(2,3)-q)+9*own-11))
        P=S.Poly(N,q)
        assert P.degree()<=2
        A,B,C=(P.nth(k) for k in (2,1,0))
        rows.append((L,H,N,A,B,C))
    tables.append(rows)

ends1=[x*(5*x*x-6*x+2),x*(108*x*x-96*x+25)/9,
       x*(207*x*x-135*x+25)/9,x*(15*x*x-7*x+1),
       x*(10*x*x-6*x+1),x**3]
ends2=[(2*x-1)*p for p in
       [7*x*x-7*x+1,16*x*x-13*x+2,30*x*x-26*x+5,
        (270*x*x-210*x+37)/9,(108*x*x-87*x+16)/9,
        5*x*x-5*x+1]]
As=[[7*x,25*x-9,16*x,23*x-7,9*x],
    [9*(2*x-1),25*x-9,16*(2*x-1),23*x-7,7*(2*x-1)]]
for rows,ends,expectedA in zip(tables,[ends1,ends2],As):
    for k,(L,H,N,A,B,C) in enumerate(rows):
        eq(A,expectedA[k]);eq(N.subs(q,L),ends[k]);eq(N.subs(q,H),ends[k+1])

L,H,N,A,B,C=tables[0][2]
eq(4*A*C-B*B,176*x**4)
L,H,N,A,B,C=tables[0][3]
eq(H+B/(2*A),3*x*(3*x-1)/(23*x-7))
P1=238*x**3-280*x*x+95*x-9
P2=178*x**3-192*x*x+65*x-7
for index,p in [(1,P1),(3,P2)]:
    L,H,N,A,B,C=tables[1][index]
    eq(4*A*C-B*B,4*(2*x-1)*p)
L,H,N,A,B,C=tables[1][1]
eq(-B/(2*A)-L,-3*(2*x-1)*(3*x-1)/(25*x-9))
eq(H+B/(2*A),-2*(2*x-1)*(8*x-3)/(25*x-9))
L,H,N,A,B,C=tables[1][3]
eq(-B/(2*A)-L,-2*(2*x-1)*(24*x-7)/(3*(23*x-7)))
eq(H+B/(2*A),-7*(2*x-1)*(3*x-1)/(3*(23*x-7)))

def bern(p,a,b):
    P=S.Poly(S.expand(p.subs(x,a+(b-a)*t)),t);n=P.degree()
    return [S.factor(sum(P.nth(i)*S.binomial(k,i)/S.binomial(n,i)
                         for i in range(k+1))) for k in range(n+1)]
assert bern(P1,S.Rational(3,8),S.Rational(1,2))==[
    -S.Rational(51,256),-S.Rational(155,192),-S.Rational(71,48),-S.Rational(7,4)]
assert bern(P2,S.Rational(1,3),S.Rational(1,2))==[
    -S.Rational(2,27),-S.Rational(5,18),-S.Rational(11,18),-S.Rational(1,4)]
for p in [108*x*x-96*x+25,207*x*x-135*x+25,
          15*x*x-7*x+1,10*x*x-6*x+1]:
    assert S.discriminant(p,x)<0
for N in ends2:
    p=S.cancel(N/(2*x-1))
    assert S.diff(p,x,2)>0
    assert p.subs(x,S.Rational(1,3))<0 and p.subs(x,S.Rational(1,2))<0

def f(xx,qq):
    if qq<=0:return F(1)
    if qq>=1-xx:return F(0)
    if xx==0:return (1-qq)**2
    if xx==F(1,2):return 1-4*qq*qq
    if qq<=xx:return 1-qq*qq/(xx*(1-xx))
    return (1-xx-qq)**2/((1-xx)*(1-2*xx))
count=0
for ix in range(101):
    xx=F(ix,200)
    breaks=sorted({F(0),xx,1-xx,F(2,3),F(2,3)-xx,xx-F(1,3)})
    candidates=list(breaks)
    for L,H in zip(breaks,breaks[1:]):
        mid=(L+H)/2
        def W(z):return 9*f(xx,z)+7*f(xx,F(2,3)-z)+9*f(xx,F(1,3))-11
        # Exact interpolation identifies the quadratic on this interval.
        z0,z1,z2=(3*L+H)/4,mid,(L+3*H)/4
        y0,y1,y2=W(z0),W(z1),W(z2);step=z1-z0
        A=(y2-2*y1+y0)/(2*step*step)
        B=(y2-y0)/(2*step)-2*A*z1
        if A>0:
            v=-B/(2*A)
            if L<v<H:candidates.append(v)
    for qq in candidates:
        assert 9*f(xx,qq)+7*f(xx,F(2,3)-qq)+9*f(xx,F(1,3))>=11
        count+=1
assert f(F(0),F(1,3))==F(4,9)
assert f(F(0),F(5,12))==F(49,144)
assert f(F(0),F(1,4))==F(9,16)
assert F(4,9)+F(49,144)==F(4,9)+F(7,9)*F(7,16)==F(113,144)
print("PASS: all ten symbolic threshold cells, endpoint and stationary signs,")
print("two exact Bernstein certificates,",count,"rational extremum checks, and sharp actual cap.")
