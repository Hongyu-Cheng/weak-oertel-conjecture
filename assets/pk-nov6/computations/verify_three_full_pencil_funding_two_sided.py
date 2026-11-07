"""Exact rational and symbolic verification of the three-full-row family."""
import sympy as S
from fractions import Fraction as Q

n=0
def check(v):
    global n
    assert v
    n+=1
def zero(v):
    check(S.factor(v)==0)

p,q,r,w,s=S.symbols('p q r w s',positive=True)
P=(p*p*q*q+p*q*(p+q)*(r+w)+(p*p+p*q+q*q)*r*w)/((p+r)*(p+w)*(q+r)*(q+w))
g=S.Matrix([S.diff(P,p),S.diff(P,q),-S.diff(P,r),-S.diff(P,w)])
H=S.Matrix(4,4,lambda i,j:S.diff(g[i],[p,q,r,w][j])*(-1 if j>=2 else 1))
one=S.ones(4,1)
f0=sum(g)/3
e=S.Matrix([1,-1,0,0]);z=S.Matrix([0,0,1,-1])

def symmetric_reduce(expr):
    expr=S.factor(expr.subs({r:1,w:1}))
    num,den=S.fraction(expr)
    nr=S.symmetrize(num,[p,q],formal=True)
    dr=S.symmetrize(den,[p,q],formal=True)
    zero(nr[1]);zero(dr[1])
    U,V=nr[2][0][0],nr[2][1][0]
    return S.factor((nr[0]/dr[0]).subs({U:s,V:(1-s)/3}))

zero(symmetric_reduce(P)-(4*s-1)/(4*(s+2)))
zero(symmetric_reduce(f0)-3/(4*(s+2)))
zero(symmetric_reduce((e.T*H*e)[0])-27*(3*s-2)/(8*(s+2)**2))
zero(symmetric_reduce((z.T*H*z)[0])-3/(8*(s+2)))
zero((e.T*H*z)[0].subs({r:1,w:1}))
zero(symmetric_reduce(-(z.T*H*z)[0]/(3*f0))+S.Rational(1,6))

qp=(1-p)/(1+3*p);sp=p+qp
sub={q:qp,r:1,w:1}
for j,desired in enumerate([1/(sp+2),1/(sp+2),sp/(2*(sp+2)),sp/(2*(sp+2))]):
    zero((g[j]/(3*f0)).subs(sub)-desired)
zero(3*p*qp+p+qp-1)
zero((1/p-1)*(1/qp-1)-4)

sub3={p:2,q:2,r:s,w:s}
zero(P.subs(sub3)-4*(3*s+2)/(s+2)**3)
zero(f0.subs(sub3)-4*s/(s+2)**3)
zero(-(e.T*H*e)[0].subs(sub3)/(3*f0.subs(sub3))-s*(6-s)/(6*(s+2)**2))
zero(s*(6-s)/(6*(s+2)**2)-S.Rational(1,12)-(3*s-2)*(2-s)/(12*(s+2)**2))
T=(4*s-1)/3;U=(3*s+2)/s;lam=3*s/(8*s*s+7*s+6)
zero(lam*(2*T+U)-1)
zero((T-s/2)**2-(s*s-4*(1-s)/3)/4-4*(1-s)**2/9)
zero((U-2)/(U+s)-1/(s+1))

# Actual weighted optimized Hessian, including threshold Schur term.
def weighted_hessian(raw):
    sub=dict(zip([p,q,r,w],raw))
    pp=S.factor(P.subs(sub));gg=g.subs(sub);hh=H.subs(sub)
    tt=S.factor(3*pp/sum(gg));eta=hh*one
    BB=S.factor(6*pp/tt**2-(one.T*hh*one)[0])
    check(BB>0)
    MM=tt/(3*pp)*(-hh+4*gg*gg.T/(3*pp)-(eta-3*gg/tt)*(eta-3*gg/tt).T/BB)
    return S.simplify(MM),pp,tt

perm=S.zeros(4)
for i,j in enumerate([2,3,0,1]):
    perm[i,j]=1

for denom in range(4,21):
    pp=S.Rational(1,denom);qq=(1-pp)/(1+3*pp);ss=pp+qq
    tt=(4*ss-1)/3;uu=(3*ss+2)/ss;ll=1/(2*tt+uu)
    c1=S.Matrix([pp,qq,-1,-1]);c2=S.Matrix([qq,pp,-1,-1]);c3=S.Matrix([-ss,-ss,2,2])
    rows=[ll*(tt*one-c1),ll*(tt*one-c2),ll*(uu*one-c3)]
    check(all(0<x<1 for row in rows for x in row))
    check(sum(rows,S.zeros(4,1))==one)
    check(S.Matrix.hstack(*rows).rank()==3)
    bb=S.Matrix([1/(ss+2),1/(ss+2),ss/(2*(ss+2)),ss/(2*(ss+2))])
    for ci in [c1,c2,c3]:
        zero((bb.T*ci)[0])
    check(min(bb)>S.Rational(1,10))
    m1,P1,t1=weighted_hessian([pp,qq,1,1])
    m2,P2,t2=weighted_hessian([qq,pp,1,1])
    m3,P3,t3=weighted_hessian([2,2,ss,ss]);m3=perm.T*m3*perm
    zero(t1-tt);zero(t2-tt);zero(t3-uu)
    zero((z.T*m1*z)[0]+S.Rational(1,6))
    zero((z.T*m2*z)[0]+S.Rational(1,6))
    zero((z.T*m3*z)[0]-ss*(6-ss)/(6*(ss+2)**2))
    funded=S.factor((z.T*(m3+(m1+m2)/4)*z)[0]/ll)
    check(funded>0)
    zero(funded-(3*ss-2)*(2-ss)/(12*(ss+2)**2*ll))
    # The z direction has no Hessian cross terms with the entire
    # pair-symmetric complement in either funding row.
    for M in [m1,m2]:
        for v in [S.Matrix([1,0,0,0]),S.Matrix([0,1,0,0]),S.Matrix([0,0,1,1])]:
            zero((z.T*M*v)[0])

check(Q(371,4374)-Q(1,12)==Q(13,8748))
check(Q(247,35)*Q(13,8748)==Q(3211,306180))

# Full equal-pair centroid classification, with all denominators retained.
X,Y,Z,W=S.symbols('X Y Z W',positive=True)
TT=X+Y+Z+W; DD=(X+Z)*(Y+Z)*(X+W)*(Y+W)
bx=X*(1/(X+Z)+1/(X+W)-1/TT)/3
by=Y*(1/(Y+Z)+1/(Y+W)-1/TT)/3
bz=Z*(1/(X+Z)+1/(Y+Z)-1/TT)/3
bw=W*(1/(X+W)+1/(Y+W)-1/TT)/3
zero(3*(bx-by)*TT*DD-(X-Y)*(Z*W*TT**2-(X*Y-Z*W)**2))
zero(3*(bz-bw)*TT*DD-(Z-W)*(X*Y*TT**2-(X*Y-Z*W)**2))
zero((X*Y*TT**2-(X*Y-Z*W)**2)-(Z*W*TT**2-(X*Y-Z*W)**2)-(X*Y-Z*W)*TT**2)
aa=S.symbols('aa',positive=True)
LL=3*(1-2*aa)/(3*aa-1)
zero((LL+3)/(3*(LL+2))-aa)
zero(LL-6-(9-24*aa)/(3*aa-1))

# Independent reconstruction of the root's alternative global payment.
ss,tt=S.symbols('ss tt')
pp=(4*ss-1)/(4*(ss+2));qq=4*(3*ss+2)/(ss+2)**3
NN=16*ss**6+120*ss**5+321*ss**4-1400*ss**3+1176*ss**2+672*ss-496
zero((pp+2*qq)**2-4*qq-NN/(16*(ss+2)**6))
bern=[S.Rational(102400,729),S.Rational(5120,27),S.Rational(10624,45),S.Integer(280),S.Rational(1611,5),S.Rational(1093,3),S.Integer(409)]
zero(NN.subs(ss,(2+tt)/3)-sum(S.binomial(6,i)*bern[i]*tt**i*(1-tt)**(6-i) for i in range(7)))
check(all(b>0 for b in bern))
print(f'PASS: {n:,} exact symbolic/rational checks, including full threshold-Schur funding matrices.')
