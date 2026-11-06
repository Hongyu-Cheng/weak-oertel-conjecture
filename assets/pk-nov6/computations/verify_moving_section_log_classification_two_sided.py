from fractions import Fraction as F
import sympy as s

checks=0
def yes(x):
    global checks
    assert x
    checks+=1
def zero(x):
    global checks
    assert s.simplify(x)==0,x
    checks+=1

# Exact homothetic sublevel bound, all sampled dimensions/ratios.
for m in range(1,31):
    for k in range(1,40):
        q=F(k,40)
        yes(1-(1-q)**m<=m*q)
        yes((1-q)**m>=0)

x,a,e=s.symbols('x a e',positive=True)
primitive=x+(a-e)*s.log(x-a+e)
zero(s.diff(primitive,x)-x/(x-a+e))
I=1-a+(a-e)*s.log((1-a+e)/e)
zero(primitive.subs(x,1)-primitive.subs(x,a)-I)
log_primitive=((x-a+e)**2/s.Integer(2)*s.log(x-a+e)
               -(x-a+e)**2/s.Integer(4)
               +(a-e)*((x-a+e)*s.log(x-a+e)-(x-a+e)))
zero(s.diff(log_primitive,x)-x*s.log(x-a+e))

for m in range(2,501):
    aa=F(1,m);ee=F(1,2**m)
    yes(0<ee<=aa)
    yes(1-aa+ee<=1)
    yes(aa<aa+ee*ee<1)
    # coefficient multiplying log2 in the proper-section formula
    yes((aa+ee*ee)*m>=1)
    yes((aa+ee*ee)*m-1==m*ee*ee)

# Relative-entropy perspective Hessian used in the independent root audit.
aa,bb=s.symbols('aa bb',positive=True)
f=aa*s.log(aa/bb)
H=s.hessian(f,(aa,bb))
zero(H.det())
zero(H[0,0]-1/aa)
zero(H[1,1]-aa/bb**2)
print(f'PASS: {checks} exact anchor, inverse/log primitive and collapse checks')
