from fractions import Fraction as F
import sympy as s
count=0
def check(x):
    global count
    assert x
    count+=1
for den in range(1,21):
    for num in range(-den,den+1):
        x=F(num,den);x1=max(F(-1),2*x-1);x2=2*x-x1
        check(-1<=x1<=1 and -1<=x2<=1)
        check((x1+x2)/2==x)
        check((1+x1+1-x2)/2==abs(x))
x,e=s.symbols('x e',real=True)
check(s.integrate(1+x,(x,-1,0))==s.Rational(1,2))
check(s.integrate(1-x,(x,-1,0))==s.Rational(3,2))
check(s.integrate(-x,(x,-1,0))==s.Rational(1,2))
check(s.integrate(s.Abs(x),(x,-1,1))==1)
check(s.Rational(4,3)*(2-s.Rational(3,4)*e)==s.Rational(8,3)-e)
check(s.Rational(2)/(4+s.Rational(8,3))==s.Rational(3,10))
check(1-s.Rational(3,10)*3==s.Rational(1,10))
check(s.Rational(1,2)-s.Rational(3,10)*2==-s.Rational(1,10))
for ee in [F(1,1000),F(1,100),F(1,10)]:
    check((2-ee)/(F(20,3)-3*ee)<F(3,10))
    check(F(4,3)-ee/2<2-ee)
print(f'{count} exact checks PASS')
