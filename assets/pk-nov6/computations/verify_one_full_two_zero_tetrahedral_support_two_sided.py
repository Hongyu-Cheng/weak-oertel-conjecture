"""Exact supplementary checks for the regular one-full/two-zero theorem.

The symbolic identities plus positivity arguments in the note prove the
theorem. These finite checks verify its transcription and actual matrix
construction; no numerical optimization is used.
"""
from fractions import Fraction as Q
from math import comb
import sympy as s

checks = 0

def check(cond):
    global checks
    assert cond
    checks += 1

def zero(expr):
    check(s.factor(expr) == 0)

X,Y,Z,W=s.symbols('X Y Z W', positive=True)
T=X+Y+Z+W
qr=X*(1/(X+Z)+1/(X+W)-1/T)/3
qs=Y*(1/(Y+Z)+1/(Y+W)-1/T)/3
zero((3*qr-1)*(X+Z)*(X+W)*T - (Y*X**2-Z*W*(T+X)))
zero((3*qs-1)*(Y+Z)*(Y+W)*T - (X*Y**2-Z*W*(T+Y)))
zero(Y*(Z*W*(T+X)-Y*X**2)-X*(Z*W*(T+Y)-X*Y**2)-Z*W*T*(Y-X))

u,v,tau,z,w=s.symbols('u v tau z w', positive=True)
S=u+v
P=u*v
A=(S*S-P)/(3*S)
C=(1-u)*(2*u+v)/(3*S)
D=(1-v)*(u+2*v)/(3*S)
V=(1-u)*(1-v)
F=V*(1+S)
l=v+(u-v)*tau
den=s.integrate(l,(tau,0,1))
zero(den-S/2)
zero(s.integrate(l*l,(tau,0,1))/(2*den)-A)
zero(s.integrate((1-u)*tau*l,(tau,0,1))/den-C)
zero(s.integrate((1-v)*(1-tau)*l,(tau,0,1))/den-D)
cap_int=s.integrate(s.integrate(6*(1-z-w),(w,0,(1-v)*(1-z/(1-u)))),(z,0,1-u))
zero(cap_int-F)
zero(C+D+2*A-1)
zero(C*D-V*(2*S*S+P)/(9*S*S))
zero(C-D-(u-v)*(1-2*S)/(3*S))
zero(3*S*(C-s.Rational(1,3))-u*(1-S-u))
zero(3*S*(D-s.Rational(1,3))-v*(1-S-v))

# Reconstruct the cap-product polynomial dependency from actual diagonal
# centroids and the determinant cap formula, rather than trust its printout.
R=Z+W
b0=Z*W
cc=b0*(T+Y)-X*Y*Y
BB=R*(X+Y)+X*X+X*Y+Y*Y
EE=R**3+2*R*R*X+3*R*R*Y+R*X*X+5*R*X*Y+3*R*Y*Y+2*X*X*Y+2*X*Y*Y+Y**3
lb1=Y*(1/(Y+Z)+1/(Y+W)-1/T)/3
lb2=Z*(1/(X+Z)+1/(Y+Z)-1/T)/3
lb3=W*(1/(X+W)+1/(Y+W)-1/T)/3
ff=b0*((X+Y)*T-X*Y+b0)/((X+Z)*(X+W)*(Y+Z)*(Y+W))
zero(ff-27*lb1*lb2*lb3-b0*(cc*BB+b0*EE+b0*b0*Y)/(T**3*(Y+Z)**2*(Y+W)**2))

r,ss,zz=s.symbols('r ss zz', real=True)
N=3+(1+2*r)*ss-r*(1-r*r)*ss*ss
zero(3*(1+ss)-2*ss*(1+ss)*(1-r)+ss*ss*(1-r)**2*(2+r)-N)
upperpoly=r*r*(r**4+4*r**3-15*r*r-6*r+28)
zero((1-r)**4*(2+r)**2-(2+r-r*r)**2*(1-4*r)-upperpoly)
Bn=[r**4,r*r*(7-4*r)/2,((1-4*r)**2+18*r*r*(1-r))/6,
    (1-r)*(1-2*r)*(1-4*r)/2,(1-r)**2*(1-4*r)]
J=(1-r)**2*(N*N-4*(1+ss)*(2+r))
Bern=sum(comb(4,i)*Bn[i]*zz**i*(1-zz)**(4-i) for i in range(5))
zero(J.subs(ss,(1-zz)/(1-r))-Bern)
check(Q(28)-Q(15,16)-Q(6,4)==Q(409,16))

# Rational section families, including equal excluded heights (u=v), and
# parameters with a central-coordinate equality C=1/3 or D=1/3.
samples=set()
for den0 in range(3,16):
    for i in range(1,den0):
        for j in range(1,den0):
            samples.add((Q(i,den0),Q(j,den0)))
for den0 in range(3,20):
    for i in range(1,den0):
        uu=Q(i,den0)
        vv=1-2*uu
        if 0<vv<1:
            samples.add((uu,vv))
            samples.add((vv,uu))

accepted=0
stationary_matrices=0
for uu,vv in sorted(samples):
    ss=uu+vv
    aa=(uu*uu+uu*vv+vv*vv)/(3*ss)
    cc=(1-uu)*(2*uu+vv)/(3*ss)
    dd=(1-vv)*(uu+2*vv)/(3*ss)
    if not (aa<Q(1,3) and cc<=Q(1,3) and dd<=Q(1,3)):
        continue
    accepted+=1
    rr=uu*vv/(ss*ss)
    ff=(1-uu)*(1-vv)*(1+ss)
    gg=27*aa*aa
    check(0<rr<=Q(1,4))
    check(Q(2,3)<=ss<1/(1-rr))
    check(ff>27*aa*cc*dd)
    check(gg*cc*dd<ff*(cc+dd))
    check(ff*abs(cc-dd)<gg*cc*dd)
    ee=[gg*cc*dd,ff*cc,ff*dd]
    total=sum(ee)
    hsq=total*total/(4*ff*cc*dd)
    check(hsq>1)
    nn=3+(1+2*rr)*ss-rr*(1-rr*rr)*ss*ss
    check(hsq==nn*nn/(4*(1+ss)*(2+rr)))
    zz=1-(1-rr)*ss
    bns=[rr**4,rr*rr*(7-4*rr)/2,((1-4*rr)**2+18*rr*rr*(1-rr))/6,
         (1-rr)*(1-2*rr)*(1-4*rr)/2,(1-rr)**2*(1-4*rr)]
    check(all(x>=0 for x in bns))
    check((1-rr)**2*(nn*nn-4*(1+ss)*(2+rr))==sum(Q(comb(4,i))*bns[i]*zz**i*(1-zz)**(4-i) for i in range(5)))

    # Actual zero-diagonal 4x4 competitor. Active labels are 0,1,2;
    # fourth row is zero. All entries are rational despite algebraic weights.
    mat=[[Q(0) for _ in range(4)] for _ in range(4)]
    theta=[(total-2*x)/total for x in ee]
    for i in range(3):
        for j in range(3):
            if i!=j:
                mat[i][j]=(total/2-ee[i])/ee[j]
        mat[i][3]=theta[i]
    check(all(x>=0 for row in mat for x in row))
    check(all(sum(mat[i][j] for i in range(4))==1 for j in range(4)))
    check(all(mat[i][i]==0 for i in range(4)))
    c_cubes=[ff,gg*dd,gg*cc]
    for i in range(3):
        prod=Q(1)
        for j in range(4):
            if j!=i:
                prod*=mat[i][j]
        check(c_cubes[i]*prod==hsq*theta[i]**3)
    check(sum(theta)==1)

    # When all heights are <1, reconstruct the actual original stationary
    # matrix and verify its section and column equations exactly. This does
    # not assert global capacity minimality or maximality for these examples.
    alpha=(1-ss+rr*ss)/(1+rr*ss)
    tt=(1+ss)*alpha
    hh=ss*alpha
    beta=alpha+hh/(1-uu)
    gamma=alpha+hh/(1-vv)
    if not (0<alpha<tt<min(beta,gamma) and max(beta,gamma)<1):
        continue
    stationary_matrices+=1
    bx=[aa,aa,cc,dd]
    xx=[alpha,alpha,beta,gamma]
    check(sum(a*b for a,b in zip(bx,xx))==tt)
    check(tt*3*ss/(hh*(1+ss))==3)
    qq=[(1-x)*b/(1-tt) for x,b in zip(xx,bx)]
    check(qq[0]==qq[1]==Q(1,3))
    check(0<qq[2]<Q(1,3) and 0<qq[3]<Q(1,3))
    mu=(1-tt)/3
    mus=[Q(0),Q(0),mu-bx[2]*(1-beta),mu-bx[3]*(1-gamma)]
    check(sum(mus)==mu)
    original=[xx,[Q(0)]*4,[Q(0)]*4,[Q(0)]*4]
    for i in [2,3]:
        for j in range(4):
            if i!=j:
                original[i][j]=mus[i]/bx[j]
    check(all(sum(original[i][j] for i in range(4))==1 for j in range(4)))

check(accepted>100)
check(stationary_matrices>100)
print(f'PASS: {checks:,} exact checks; {accepted} central sections; {stationary_matrices} actual stationary matrices.')
