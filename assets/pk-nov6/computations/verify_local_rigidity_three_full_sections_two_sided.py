import sympy as S
p,q,r,u,v,w,z=S.symbols('p q r u v w z')
def cent(p,q,r,w):
 X,Y,Z,W=[1/S.sympify(k) for k in [p,q,r,w]]
 L=X+Y+Z+W
 return S.Matrix([(X/(X+Z)+X/(X+W)-X/L)/3,(Y/(Y+Z)+Y/(Y+W)-Y/L)/3,(Z/(Z+X)+Z/(Z+Y)-Z/L)/3,(W/(W+X)+W/(W+Y)-W/L)/3])
b1=cent(p,q,r,1);b2=cent(u,v,w,z);b3=cent(p+u,q+v,r+w,1+z)
E=S.Matrix(list(b1-b2)[:3]+[(b1-b3)[i] for i in [0,2]])
pt={p:S.Rational(1,5),q:S.Rational(1,2),r:1,u:S.Rational(1,2),v:S.Rational(1,5),w:1,z:1}
M=E.jacobian([r,u,v,w,z]).subs(pt)
assert M.det()==-S.Rational(1625,7029357352416)
assert E.subs(pt)==S.zeros(5,1)
assert b1.subs(pt)==S.Matrix([S.Rational(10,27)]*2+[S.Rational(7,54)]*2)
assert S.factor(sum(b1)-1)==0
assert S.factor(S.Matrix([p,q,-r,-1]).dot(b1))==0
B=S.Rational(7,54);D=0
F=3*(2*B-D-1)**2*p**3+6*(6*B**2-5*B*D-3*B+D**2+D)*p**2+(36*B**2-24*B*D-8*B+3*D**2+1)*p+2*B*(6*B-3*D-1)
assert S.factor(F-S.Rational(400,243)*(p-S.Rational(1,5))*(p-S.Rational(7,20))*(p-S.Rational(1,2)))==0
for root in [S.Rational(1,5),S.Rational(7,20),S.Rational(1,2)]:
 assert S.diff(F,p).subs(p,root)!=0
k1,k2,k3=S.symbols('k1 k2 k3')
K=S.Matrix([[k1+k2,k2],[k2,k3+k2]])
assert S.factor(K.det()-(k1*k3+k2*(k1+k3)))==0
assert S.factor(K.det()-k1*k3*(1+k2*(1/k1+1/k3)))==0
print('PASS: 11 exact identities; rational and family-wide transverse Jacobians.')
