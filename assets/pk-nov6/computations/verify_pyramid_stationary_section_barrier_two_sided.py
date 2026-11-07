from fractions import Fraction as F
import sympy as s
checks=0
def check(v):
    global checks
    assert bool(v)
    checks+=1
def primitive(q,d,H):
    L=H+1
    return L/F(d)*(L-q)**(-d)-F(1,d-1)*(L-q)**(1-d)
for d in range(2,15):
    for j in range(1,21):
        H=F((d-1)*j,20)
        check(primitive(F(1),d,H)==F(d-1-H,d*(d-1)*H**d))
        for R in [F(i,10) for i in range(1,51)]+[F(10),F(100),F(1000)]:
            val=primitive(min(R,F(1)),d,H)-primitive(-R,d,H)
            check(val>0)
    check(F(d,d+1)**d<F(1,2))
H,q=s.symbols('H q',positive=True)
for d in range(2,9):
    L=H+1
    prim=L/s.Integer(d)*(L-q)**(-d)-s.Rational(1,d-1)*(L-q)**(1-d)
    check(s.simplify(s.diff(prim,q)-q/(L-q)**(d+1))==0)
    x=s.symbols('x0:'+str(d-1))
    aa=s.symbols('a0:'+str(d-1))
    dot=sum(xx*a for xx,a in zip(x,aa))
    image=s.Matrix([H*xx/(L-dot) for xx in x])
    if d<=4:
        J=image.jacobian(s.Matrix(x))
        check(s.factor(J.det()-H**(d-1)*L/(L-dot)**d)==0)
    adot=sum(a*im for a,im in zip(aa,image))
    for xx,im in zip(x,image):
        check(s.simplify(L*im/(H+adot)-xx)==0)
print(f'PASS: {checks} exact checks')
