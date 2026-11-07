import sympy as S
m=3; d=2
coords=S.symbols('b0:12')
A=[];B=[]
for z in range(2):
 a=S.zeros(3); k=6*z
 for i in range(3):
  for j in range(3):
   if i!=j:a[i,j]=coords[k];k+=1
 b=a-S.diag(*[sum(a[i,j] for i in range(3)) for j in range(3)])
 A.append(a);B.append(b)
hcoords=S.symbols('h0:8');h={};k=0
for g in range(2):
 for z in range(2):
  h[g,z]=[hcoords[k],hcoords[k+1],-hcoords[k]-hcoords[k+1]];k+=2
xs=list(coords)+list(hcoords)
ell=S.Rational(5,11)
capfirst=[0]*6
q=0
for z in range(2):
 b=B[z]; T=S.trace(b); tr2=S.trace(b*b)
 q+=T*T-tr2
 for g in range(2):
  a=S.Rational(1,10) if g==z else S.Rational(4,5)
  X=1/(1-a);gamma=(1-a)**2
  for i in range(3):
   row=sum(A[z][i,j] for j in range(3))
   first=T+row+2*(X-1)*b[i,i]-2*X*h[g,z][i]
   second=-tr2-2*X*X*(b[i,i]-h[g,z][i])**2+sum((b[i,i]-A[z][i,j])**2 for j in range(3) if j!=i)
   capfirst[3*g+i]+=gamma*first
   q-=ell*gamma*(first*first+second)
q=S.expand(q)
G=S.Matrix([[S.diff(v,x) for x in xs] for v in capfirst])
Q=S.hessian(q,xs)/2
K=S.Matrix.hstack(*G.nullspace())
QK=K.T*Q*K
print('rank G',G.rank(),'Kdim',K.cols,'QKrank',QK.rank())
l=S.symbols('l')
print(S.factor(QK.charpoly(l).as_expr()))
print('eigen approximations', [e.evalf() for e in QK.eigenvals()])
u,v,hl,hh=S.symbols('u v hl hh')
c=S.Matrix([1,-1,0]); Alift=S.Matrix(3,3,lambda i,j:0 if i==j else (3*c[j]+c[i])/5)
sub={};k=0
for factor in (u,v):
 for i in range(3):
  for j in range(3):
   if i!=j:sub[coords[k]]=factor*Alift[i,j];k+=1
# h-coordinates are (L0 firsttwo,L1 firsttwo,H0 firsttwo,H1 firsttwo).
HL1=(-S.Rational(171,500)*u-S.Rational(41,125)*v-S.Rational(9,5)*hl)/S.Rational(2,5)
HH1=(-S.Rational(41,125)*u-S.Rational(171,500)*v-S.Rational(2,5)*hh)/S.Rational(9,5)
for k,factor in enumerate((hl,HL1,hh,HH1)):
 sub[hcoords[2*k]]=factor;sub[hcoords[2*k+1]]=-factor
qq=S.factor(q.subs(sub, simultaneous=True))
opt=S.solve([S.diff(qq,hl),S.diff(qq,hh)],(hl,hh))
print('opt h',opt)
print('Qeff',S.factor(qq.subs(opt)))
for uv in [(1,1),(1,-1)]:
 print('uv',uv,'Q',S.factor(qq.subs(opt).subs({u:uv[0],v:uv[1]})), 'h', [S.factor(sub[hcoords[k]].subs(opt).subs({u:uv[0],v:uv[1]})) for k in (0,2,4,6)])
for val in [S.Rational(-1,10),S.Rational(-1,9),S.Rational(-1,8),S.Rational(-1,12)]:
 hv=-S.Rational(7,200)-S.Rational(9,2)*val
 qv=S.factor(qq.subs({u:1,v:-1,hl:val,hh:-hv}))
 print('simple',val,hv,'Q',qv)
