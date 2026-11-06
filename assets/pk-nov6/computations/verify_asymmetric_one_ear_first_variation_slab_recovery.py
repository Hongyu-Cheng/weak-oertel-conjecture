"""Exact symbolic derivative and actual rational polygon checks."""
import sympy as S
exec(open('./verify_fixed_endpoint_sector_polygon_replacement_slab_recovery.py').read().split('def verify(')[0])
x,s,v,w,t,d=S.symbols('x s v w t d', positive=True)
b=x+s;c=x+s+w;e=s+w;L=x+w+2*v;H=x+s+w+v;B=x+2*s+w
k=L*B/2;kd=(L+d)*B/2
q=[(2*v+w)**2*B/(2*L), L*b*b/(2*H), L*c*c/(2*H)]
sig=[(2*v+w)*B/L,L*b/H,L*c/H]
qd=[q[0],q[1]+d*(B-e*e/(e+t))/2,q[2]+d*(B-s*s/(b+d-t))/2]
sd=[sig[0],sig[1]+d*e/(e+t),sig[2]+d*s/(b+d-t)]
Md=sum(qd[i]/sd[i] for i in range(3))
hp=B*H/(2*L)*(t/(b*(e+t))+(x-t)/(c*(b-t)))
check(S.factor(Md.subs(d,0)-H)==0)
check(S.factor(S.diff(Md,d).subs(d,0)-hp)==0)
logs=[S.diff(kd,d)/(2*kd)+S.diff(qd[i],d)/(2*qd[i])-S.diff(sd[i],d)/sd[i]-S.diff(Md,d)/Md for i in range(3)]
actual_der=S.factor((L/H)*logs[0].subs(d,0)+(B/H)*(logs[1]+logs[2]).subs(d,0))
claimed=(4-L/H)*(1/(2*L)-hp/H)+B/(2*L)*((B*t-b*e)/(b*b*(e+t))+(B*(x-t)-c*s)/(c*c*(b-t)))
check(S.factor(actual_der-claimed)==0)
P0=2*s*s*v+s*s*w+s*s*x+2*s*v*w+2*s*v*x+2*s*w*w+4*s*w*x+2*s*x*x+v*w*w+2*v*w*x+v*x*x+w**3+3*w*w*x+3*w*x*x+x**3
P1=4*s**4*v+2*s**4*w+2*s**4*x+8*s**3*v*w+4*s**3*v*x+6*s**3*w*w+6*s**3*w*x+8*s**3*x*x+6*s*s*v*w*w+6*s*s*v*w*x+6*s*s*w**3+7*s*s*w*w*x+12*s*s*w*x*x+11*s*s*x**3+2*s*v*w**3+2*s*v*w*w*x+2*s*w**4+3*s*w**3*x+6*s*w*w*x*x+11*s*w*x**3+6*s*x**4+w**3*x*x+3*w*w*x**3+3*w*x**4+x**5
P2=2*s*s*v+s*s*w+s*s*x+2*s*v*w+2*s*v*x+2*s*w*w+2*s*x*x+v*w*w+v*x*x+w**3+x**3
C0=(s+w)**2*(s+x)**2*P0
C1=(s+x)*(s+w+x)*P1/2
C2=s*s*(s+w+x)**2*P2
den=2*(s+x)**2*(s-t+x)*(s+t+w)*(s+w+x)**2*(2*v+w+x)*(s+v+w+x)
bern=C0*(1-t/x)**2+2*C1*(t/x)*(1-t/x)+C2*(t/x)**2
check(S.factor(-den*actual_der-bern)==0)
for poly in (P0,P1,P2):
    check(all(a>0 for a in S.Poly(poly,x,s,v,w).coeffs()))
z=S.symbols('z')
check(S.expand(4*(2-z-((2-z*z)+z)**2/4)-(4-z*z)*(z-1)**2)==0)

rng=Random(835927)
for it in range(150):
    X,SS,V=[F(rng.randint(1,20),rng.randint(1,10)) for _ in range(3)]
    W=F(0) if it%5==0 else F(rng.randint(1,20),rng.randint(1,10))
    TT=X*F(it%11,10)
    DD=min(X,SS,V)/(100*(1+X+SS+V+W))
    LL=X+W+2*V;HH=X+SS+W+V;BB=X+2*SS+W
    bb=X+SS;cc=X+SS+W;ee=SS+W
    K=hull([(2*V+W,-V-W),(-X,X+SS),(-X-DD,TT),(-X,-SS-W)])
    check(len(K)==4);check(area(K)==(LL+DD)*BB/2)
    qq=[(2*V+W)**2*BB/(2*LL),LL*bb*bb/(2*HH)+DD*(BB-ee*ee/(ee+TT))/2,LL*cc*cc/(2*HH)+DD*(BB-SS*SS/(bb+DD-TT))/2]
    sg=[(2*V+W)*BB/LL,LL*bb/HH+DD*ee/(ee+TT),LL*cc/HH+DD*SS/(bb+DD-TT)]
    for n,Q in zip([(1,0),(0,1),(-1,-1)],qq):check(area(clip(K,n))==Q)
    pp=[ray_endpoint(K,e)[0] for e in rays]
    check(pp[1][1]-pp[4][1]==sg[0]);check(pp[0][0]-pp[3][0]==sg[1]);check(pp[5][0]-pp[2][0]==sg[2])
print(f'PASS: {checks:,} exact derivative, polynomial, and actual-polygon checks')
