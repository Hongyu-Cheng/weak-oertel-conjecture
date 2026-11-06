"""Exact scalar checks for the independent logarithmic-tail audit."""
from fractions import Fraction as F
import sympy as s

checks=0
def truth(v):
    global checks
    assert v
    checks+=1

a,b,T=s.symbols('a b T',positive=True)
G=a*s.log(a/b)-T*a
H=s.hessian(G,(a,b))
truth(s.simplify(H[0,0]-1/a)==0)
truth(s.simplify(H[0,1]+1/b)==0)
truth(s.simplify(H[1,1]-a/b**2)==0)
truth(s.simplify(H.det())==0)
truth(s.simplify(s.diff(G,a)-(s.log(a/b)-T+1))==0)
truth(s.simplify(s.diff(G,b)+a/b)==0)

for ni in range(-20,61):
    ell=F(ni,10)
    ep=max(ell,F(0))
    truth(ep*ep <= ep*max(ep-1,F(0))+ep)
    for ci in range(1,31):
        c=F(ci,10)
        p=max(ell-c,F(0))
        truth(p == ep-min(ep,c))
        truth(abs(ell*p-ep*ep) <= c*ep)

print(f'{checks} exact logarithmic-tail audit checks PASS')
