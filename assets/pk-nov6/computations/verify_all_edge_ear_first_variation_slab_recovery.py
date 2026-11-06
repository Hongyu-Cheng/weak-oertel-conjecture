"""Read displayed certificates; verify actual two-edge ear cap/section data."""
from submission_text import read_submission
from pathlib import Path
import re
import sympy as S
exec(open('./verify_fixed_endpoint_sector_polygon_replacement_slab_recovery.py').read().split('def verify(')[0])
x,s,v,w,u,h=S.symbols('x s v w u h',positive=True)
p=2*v+w;L=x+p;H=x+s+w+v;B=x+2*s+w;b=x+s;c=x+s+w
source=read_submission('146226205b30285c')
def printed_poly(name):
    raw=re.search(r'    '+name+r'=(.*?)(?:;\n|\.\n)',source,re.S).group(1)
    raw=''.join(raw.split()).replace('^','**').replace('[','(').replace(']',')')
    raw=re.sub(r'(?<=[0-9a-z)])(?=[a-z(])','*',raw)
    return S.sympify(raw,locals={'x':x,'s':s,'v':v,'w':w,'p':p})
Pstar=printed_poly('Pstar');Pplus=printed_poly('Pplus');Pminus=printed_poly('Pminus')
for pol in (Pplus,Pminus):check(all(a>0 for a in S.Poly(pol,x,s,v,w).coeffs()))
for j,n,z,last in [(2,v,c,Pplus),(3,v+w,b,Pminus)]:
    E,Fj,G=[printed_poly(a+str(j))for a in ('E','F','G')]
    for pol in (E,Fj,G):check(all(a>0 for a in S.Poly(pol,x,s,v,w).coeffs()))
    R=2*s**3*p*p*L+s*s*E+s*Fj+G
    Z=p*H-n*L;A=n*L+u*Z;Bb=L*z-u*Z;theta=A/(H*L)
    q1=p*p*B/(2*L);sig1=p*B/L;ql=L*z*z/(2*H);sigl=L*z/H
    dq1=1-x*x/(L*L*(1-h));ds1=2*x/(L*L*(1-h))
    dql=1-n*n/(H*H*h);dsl=2*n/(H*H*h)
    dm=(dq1-p*ds1/2)/sig1+(dql-z*dsl/2)/sigl
    expected_dm=(p-L*h)/((1-h)*p*B)+(H*h-n)/(h*L*z)
    check(S.factor(dm-expected_dm)==0)
    deriv=(4-L/H)*(1/(L*B)-dm/H)+(L/H)*(dq1/(2*q1)-ds1/sig1)+(B/H)*(dql/(2*ql)-dsl/sigl)
    den=p*p*z*z*B*L*H*H*A*Bb
    coeff=[n*n*z*z*L*L*Pstar,p*z*L*H*R/2,x*x*p*p*H**3*last]
    bern=coeff[0]*(1-u)**2+2*coeff[1]*u*(1-u)+coeff[2]*u*u
    check(S.factor(-den*deriv.subs(h,theta)-bern)==0)

rng=Random(167523)
for it in range(100):
    X,SS,V=[F(rng.randint(1,15),rng.randint(1,10)) for _ in range(3)]
    W=F(0) if it%5==0 else F(rng.randint(1,15),rng.randint(1,10))
    PP=2*V+W;LL=X+PP;HH=X+SS+W+V;BB=X+2*SS+W;kk=LL*BB/2
    pts=[(PP,-V-W),(-X,X+SS),(-X,-SS-W)]
    baseq=[PP*PP*BB/(2*LL),LL*(X+SS)**2/(2*HH),LL*(X+SS+W)**2/(2*HH)]
    basesig=[PP*BB/LL,LL*(X+SS)/HH,LL*(X+SS+W)/HH]
    eps=kk*F(rng.randint(1,10),100)
    for j,n,z in [(1,V,X+SS+W),(2,V+W,X+SS)]:
        ell=3-j;tt=n/HH+F(it%11,10)*(PP/LL-n/HH)
        qzero=tuple((1-tt)*pts[0][a]+tt*pts[ell][a]for a in range(2))
        tip=tuple(qzero[a]+eps/kk*(qzero[a]-pts[j][a])for a in range(2))
        K=hull(pts+[tip]);check(len(K)==4);check(area(K)==kk+eps)
        ns=[(1,0),(0,1),(-1,-1)]
        height=lambda ind:tip[0]*ns[ind][0]+tip[1]*ns[ind][1]
        check(height(j)<0 and height(0)>0 and height(ell)>0)
        qq=baseq.copy();sg=basesig.copy()
        qq[0]+=eps*(1-X*X/(LL*(X+height(0))))
        sg[0]+=2*eps*X/(LL*(X+height(0)))
        qq[ell]+=eps*(1-n*n/(HH*(n+height(ell))))
        sg[ell]+=2*eps*n/(HH*(n+height(ell)))
        for nn,Q in zip(ns,qq):check(area(clip(K,nn))==Q)
        rr=[ray_endpoint(K,ee)[0]for ee in rays]
        check(rr[1][1]-rr[4][1]==sg[0]);check(rr[0][0]-rr[3][0]==sg[1]);check(rr[5][0]-rr[2][0]==sg[2])
print(f'PASS: {checks:,} exact printed-certificate and actual-ear checks')
