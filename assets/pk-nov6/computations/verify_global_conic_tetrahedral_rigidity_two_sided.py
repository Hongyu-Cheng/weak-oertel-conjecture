"""Exact actual-centroid conic and degeneracy identities, with no root-screen proof."""
import sympy as s
A,B,G,p,q,r,R=s.symbols('A B G p q r R')
D=1+A+B-G;U=A+B;V=A*B;W=G*D
c0=(G-A)**2*(G-U)
c3=(A-B)*(1+A)*(G-D)
c5=(G-1)*(G-1-B)**2
c1=-2*A**3-A*A*B+5*A*A*G-2*A*A+A*B*B-3*A*G*G+3*A*G-B*B*G+B*G*G+B*G-2*G*G
c4=-c1.subs(G,D)
c2=-(G-D)*(V+2*A-W)
conic=c0+c1*p+c2*r+c3*p*p+c4*p*r+c5*r*r
checks=0
def zero(x):
 global checks
 assert s.factor(x)==0
 checks+=1
# The conic determinant and full A=B factorization.
M=s.Matrix([[c3,c4/2,c1/2],[c4/2,c5,c2/2],[c1/2,c2/2,c0]])
zero(M.det()-(A-B)*(1+B)*(G-D)*(V-W)**2/4)
zero(conic.subs(B,A)-(2*(1+A)*p+(G-1)*r+2*A-G)*((1+A-G)**2*r-(A-G)**2))
# Direct identity for EVERY actual proper 2+2 section, not only generic inverse roots.
X,Y,Z,W0=1/p,1/q,1/r,s.Integer(1);T=X+Y+Z+W0
avec=X/(X+Z)+X/(X+W0)-X/T-1
bvec=Y/(Y+Z)+Y/(Y+W0)-Y/T-1
gvec=1-Z/(Z+X)-Z/(Z+Y)+Z/T
zero(conic.subs({A:avec,B:bvec,G:gvec},simultaneous=True))
# Through-plane incidence in the same actual coordinates.
last=1-W0/(W0+X)-W0/(W0+Y)+W0/T
zero((1+avec)*p+(1+bvec)*q-(1-gvec)*r-(1-last))
# Horizontal component, repeated-root status, and exact ratio identity.
g=A+R/(1+R);rr=R*R
ss=(R-A*(R*R+1))/(A+1);vv=ss*ss/4
v0=rr*(R-ss)/(rr+R+1)
actual=(rr*ss+2*vv)/(rr*rr+rr*ss+vv)-vv/(rr*ss+vv*(rr+1))
C=4*(1+A)**2*(R-1)*(A*(R+1)**2+R)/((R+1)*(A*R*R-A+2*R*R+R)*(A*(R*R-1)**2-R**3-4*R*R-R))
zero(actual-(1-g)-C*(vv-v0))
zero(A*R*R-A+2*R*R+R-(1+A)*(2*R*R+ss))
zero((R*(R*R-1)**2/(R*R+1)-R**3-4*R*R-R)+4*R*R*(R*R+R+1)/(R*R+1))
zero((g-2*A+(1-g)*rr)/(1+A)-ss)
# Normalized diagonal sign formula used before taking a square root.
x,y,z=s.symbols('x y z');w=1-x-y-z;K=x*y-z*w
bfirst=x/(x+z)+x/(x+w)-x
zero(bfirst-1-(K*x-z*w)/(x-K))
# Reciprocal centroid difference identity, without a diagonal-coordinate normalization assumption.
x,y,z,w=s.symbols('x y z w');tt=x+y+z+w
bb1=(x/(x+z)+x/(x+w)-x/tt)/3
bb2=(y/(y+z)+y/(y+w)-y/tt)/3
dd=(x+z)*(x+w)*(y+z)*(y+w)
zero(3*(bb1-bb2)-(x-y)*(z*w*tt*tt-(x*y-z*w)**2)/(tt*dd))
# Exact raw-height samples calibrate the conic for positive and negative pair differences.
for pi in range(1,5):
 for qi in range(1,5):
  for ri in range(1,5):
   ps=s.Rational(pi,5);qs=s.Rational(qi,6);rs=s.Rational(ri,3)
   vals={p:ps,q:qs,r:rs}
   aa=avec.subs(vals);bb=bvec.subs(vals);gg=gvec.subs(vals)
   zero(conic.subs({A:aa,B:bb,G:gg,p:ps,r:rs}))
t1,t2=s.symbols('t1 t2')
zero(2*(t1+t2-1)-(4*t1*t2-1)+(2*t1-1)*(2*t2-1))
# Actual section of the OTHER split has strictly negative conic value.
N=2*p*p*q*q*r+p*p*q*q+p*p*q*r*r+2*p*p*q*r+p*p*r*r+p*q*q*r*r+2*p*q*q*r+p*q*r*r+q*q*r*r
H=p**4*q**4*r*r+2*p**4*q**4*r+p**4*q**4+4*p**4*q**3*r*r+2*p**4*q**3*r+3*p**4*q*q*r*r+2*p**3*q**4*r*r+4*p**3*q**4*r+6*p**3*q**3*r*r+4*p**3*q*q*r*r+3*p*p*q**4*r*r+4*p*p*q**3*r**3+3*p*p*q*q*r**4+6*p*p*q*q*r**3+3*p*p*q*q*r*r+4*p*p*q*r**4+2*p*p*q*r**3+p*p*r**4+2*p*q*q*r**4+4*p*q*q*r**3+2*p*q*r**4+q*q*r**4
cross=(c0+c1*p-c2*q+c3*p*p-c4*p*q+c5*q*q).subs({A:avec,B:-gvec,G:-bvec},simultaneous=True)
zero(cross+N*H/((p+r)**2*(q+1)*(q+r)*(p*q*r+p*q+p*r+q*r)**3))
assert all(v>0 for v in s.Poly(N,p,q,r).coeffs())
assert all(v>0 for v in s.Poly(H,p,q,r).coeffs())
checks+=2
print('PASS:',checks,'exact identities and actual-section checks; conic, degeneracies, same-split roots, and cross-split sign.')
