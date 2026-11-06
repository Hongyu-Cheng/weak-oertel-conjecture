"""Exact checks of the proved formulas, not a proof by finite search."""
import sympy as S
from itertools import product

checks = 0
def check(v):
    global checks
    assert v
    checks += 1

a,b,r,w=S.symbols('a b r w', positive=True)
left=1-S.exp(w/r)*r*r/((a+r)*(b+r))
right=(a*a*S.exp(-w/a)/(a+r)-b*b*S.exp(-w/b)/(b+r))/(a-b)
for j in range(3):
    check(S.factor(S.diff(left,w,j).subs(w,0)-S.diff(right,w,j).subs(w,0))==0)

# General Schur cancellation, after g.v=0 and sum(g)=dP.
d,P,B,e,h,lam=S.symbols('d P B e h lam', positive=True)
Q=-h-e*e/B+2*lam*d*P*e/B-lam*lam*d*d*P*P/B
check(S.factor(Q.subs(lam,e/(d*P))+h)==0)

# Exact tetrahedral two-positive / two-negative data, distinct coordinates.
c=S.symbols('c0:4')
prob=sum(c[i]**3/S.prod(c[i]-c[j] for j in range(4) if j!=i) for i in [0,1])
grad=S.Matrix([S.diff(prob,z) for z in c])
hess=S.hessian(prob,c)
one=S.ones(4,1)
central=0
for p1,p2,n1,n2 in product([1,2,3],[1,2,4],[1,3,5],[2,4,6]):
    if p1==p2 or n1==n2: continue
    raw={c[0]:S.Rational(p1),c[1]:S.Rational(p2),c[2]:-S.Rational(n1),c[3]:-S.Rational(n2)}
    pp=S.factor(prob.subs(raw))
    gg=grad.subs(raw)
    f0=sum(gg)/3
    threshold=S.factor(pp/f0)
    if threshold<=max(p1,p2): continue
    vals={z:raw[z]/threshold for z in c}
    g=grad.subs(vals).applyfunc(S.factor)
    H=hess.subs(vals).applyfunc(S.factor)
    check(S.factor(sum(g)-3*pp)==0)
    eta=H*one
    beta=S.factor(6*pp-(one.T*H*one)[0])
    check(beta>0)
    M=S.Rational(4,3)/pp*(g*g.T)-H-(eta-3*g)*(eta-3*g).T/beta
    v=S.Matrix([g[1]/pp,-g[0]/pp,0,0])
    vc=v+((eta.T*v)[0]/(3*pp))*one
    check(S.factor((vc.T*M*vc)[0]+(v.T*H*v)[0])==0)
    if g[0]<=pp and g[1]<=pp:
        central+=1
        check(S.factor((v.T*H*v)[0])<0)
        check(S.factor((vc.T*M*vc)[0])>0)

# Independent tetrahedral B=0 face identities.
t,x,F=S.symbols('t x F',positive=True)
Fp=3*F/t; Fpp=6*F/t**2
face=F+(x-t)*Fp/3
facep=S.Rational(2,3)*Fp+(x-t)*Fpp/3
check(S.factor(face-x*F/t)==0)
check(S.factor(t*facep-2*face)==0)
print(f'PASS: {checks} exact checks; {central} central-pair samples.')
