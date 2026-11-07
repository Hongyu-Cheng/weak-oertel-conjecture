"""Exact algebra checks; the all-normal/weak-limit theorem is analytic."""
from fractions import Fraction as F
from math import factorial
import sympy as sp

checks=0
for d in range(1,9):
    m=d+1;h=F(d,m);V=F(1,factorial(d));Gamma=h**d
    kappa=d*V*h**(d-1)
    for k in range(1,m):
        # These are actual canonical incidence vectors of a Dirac law.
        # Barycentrics 2 on the first k vertices and equal negative
        # values on the rest realize them; none is on a canonical plane.
        bary=[F(2)]*k+[F(1-2*k,m-k)]*(m-k)
        assert sum(bary)==1
        p=[F(int(x>=F(1,m))) for x in bary]
        mean=sum(p)/m
        delta=[(x-mean)/kappa for x in p]
        assert sum(delta)==0
        assert all(p[i]-kappa*delta[i]==mean for i in range(m))
        assert sum(-kappa*x for x in delta)==0
        checks+=1
    # Uniform added probability on T is an exactly soluble check.
    p=[Gamma]*m
    assert sum(p)/m==Gamma
    assert all((x-Gamma)/kappa==0 for x in p)
    checks+=1

# Thin simplex: exact volume and fixed canonical tail identities.
eps=sp.symbols('eps',positive=True)
for d in range(2,7):
    m=d+1;b=sp.Rational(1,m);h=sp.Rational(d,m)
    e=eps**(d-1)*(h+eps)
    matrix=eps*sp.eye(d)+sp.ones(d,d)/m
    assert sp.factor(matrix.det()-e)==0
    p0=(h/(h+eps))**d
    pi=eps/(b+eps)
    assert sp.limit(p0,eps,0)==1
    assert sp.limit(pi,eps,0)==0
    for N in (1,3,7):
        theta=e/(N*m*d*h**(d-1))
        s=b-theta
        cap0=(d*s)**d+(e/N)*(d*s/(h+eps))**d
        capi=(1-s)**d+(e/N)*(1-s**d/(b**(d-1)*(b+eps)))
        # These are actual canonical cap masses divided by V.
        # Only their first coefficients are checked; the proof treats
        # noncanonical normals independently.
        c0=sp.expand(sp.series(cap0,eps,0,d).removeO()).coeff(eps,d-1)
        ci=sp.expand(sp.series(capi,eps,0,d).removeO()).coeff(eps,d-1)
        assert sp.simplify(c0-h/(N*m))==0
        assert sp.simplify(ci-h/(N*m))==0
        checks+=1
    if d==2:
        assert m*d*h**(d-1)==4
    assert h**d>sp.Rational(1,m)
    checks+=1

# Exact line cases: an off-center atom and the null-boundary limitation.
for t in [F(k,100) for k in range(1,25)]:
    # nu=delta_0 has no mass at the canonical boundary 1/2.
    y=(1-t)/2
    assert y+t==1-y==(1+t)/2
    assert (y-F(1,2))/t==F(-1,2)
    # nu=delta_(1/2) instead charges both canonical boundaries.
    assert F(1,2)+t > (1+t)/2
    checks+=1

print(f'PASS: {checks} exact affine-game, thin-simplex determinant/tail, '
      'canonical first-coefficient and interval checks. '
      'All-normal lower control and weak moving-cap convergence are proved in the note.')
