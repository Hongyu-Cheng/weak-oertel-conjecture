"""Exact symbolic identities for the saturated-strip heavy-middle theorem."""
import sympy as s
L,p,t=s.symbols('L p t')
U=(4*L+11)/8;V=(4*L-7)/8;W=(4*L+7)/8;J=(4*L+1)/8
PH=(s.Rational(9,2)*L+s.Rational(57,16))/(L+s.Rational(3,2))
P=16384*L**6+4096*L**5-410624*L**4+864192*L**3+3318576*L**2+2700228*L+671769
checks=0
def eq(a,b):
    global checks
    assert s.factor(a-b)==0
    checks+=1
eq((PH**2-9)*(V+PH)**2-U**2*PH**2,-9*P/(4096*(2*L+3)**4))
assert all(x>0 for x in s.Poly(P.subs(L,t+5).expand(),t).all_coeffs());checks+=1
eq(PH-3,3*(8*L-5)/(8*(2*L+3)))
eq(L+1-PH,(4*L-11)*(4*L+3)/(8*(2*L+3)))
vertices=[(-U,-V),(-V,-U),(p,0),(W,J),(J,W),(0,p)]
shoelace=sum(vertices[i][0]*vertices[(i+1)%6][1]-vertices[i][1]*vertices[(i+1)%6][0] for i in range(6))/2
eq(shoelace,(L+s.Rational(3,2))*p+s.Rational(3,2)*L+s.Rational(15,16))
eq(shoelace.subs(p,PH),6*L+s.Rational(9,2))
turns=[9*(2*L+2*p+1)/8,(16*L*p-24*L+24*p-21)/16,3*(L+1-p)/4]
for i in range(6):
    a,b,c=vertices[i],vertices[(i+1)%6],vertices[(i+2)%6]
    v=(b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    eq(v,turns[min(i,5-i)])
eq(2*(L-1)/(2*L)+(L-s.Rational(1,2))/(2*L),s.Rational(3,2)-s.Rational(5,4)/L)
print('PASS',checks,'exact symbolic checks')
