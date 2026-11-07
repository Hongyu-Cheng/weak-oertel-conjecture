"""Exact full polynomial certificate for the vertex-pencil classification.

Requires SymPy and python-flint. All determinant arithmetic is over Z[p,q,r].
The coefficient transcription is optionally regenerated from the displayed
geometric formulas with --regenerate (this step is slower).
"""
import json,sys
from pathlib import Path
import sympy as S
from flint import fmpz_mpoly as F
BASE=Path(__file__).resolve().parent
p,q,r,T=S.symbols('p q r T')
gens=F.gens(3);zero=F(0,3);one=F(1,3)
def fp(terms):
    out=zero
    for mon,coef in terms:
        z=F(coef,3)
        for g,k in zip(gens,mon):z*=g**k
        out+=z
    return out
def sym(terms):
    return sum(S.Integer(c)*p**m[0]*q**m[1]*r**m[2] for m,c in terms)
def cent(p,q,r,s):
    D=p*q*(r+s)+r*s*(p+q);tau=p*s*(q+r)/D
    return [(r/(p+r)+tau*s/(p+s))/3,
            (s/(q+s)+(1-tau)*r/(q+r))/3,
            (p/(p+r)+(1-tau)*q/(q+r))/3,
            (q/(q+s)+tau*p/(p+s))/3]
data=json.loads((BASE/'tetrahedral_vertex_pencil_quartic_coefficients.json').read_text())
polys=[[fp(z) for z in data[str(i)]] for i in [1,2]]
if '--regenerate' in sys.argv:
    b=[S.factor(z) for z in cent(p,q,r,S.Integer(1))]
    m=[S.Integer(3)]+[S.factor(3-1/z) for z in b[1:]]
    dd=[S.factor(z) for z in (p+3*T,q+T*m[1],r-T*m[2],1-T*m[3])]
    bb=[S.factor(z) for z in cent(*dd)]
    for i in [1,2]:
        n=S.factor(S.together(bb[i]-b[i])).as_numer_denom()[0]
        assert S.Poly(n,T).eval(0)==0
        pp=S.Poly(n/T,T,domain=S.ZZ.poly_ring(p,q,r)).primitive()[1]
        assert pp.degree()==4
        expected=sum(sym(z)*T**(4-j) for j,z in enumerate(data[str(i)]))
        assert S.Poly(pp.as_expr()-expected,T,p,q,r).is_zero or S.Poly(pp.as_expr()+expected,T,p,q,r).is_zero
        print('geometric quartic reconstruction',i,'PASS',flush=True)
# Sylvester determinant, with row/column contents removed after every step.
A=[[zero for _ in range(8)] for __ in range(8)]
for row in range(4):
    for j,c in enumerate(polys[0]):A[row][row+j]=c
    for j,c in enumerate(polys[1]):A[row+4][row+j]=c
num=[];den=[];sign=1
for n in range(8,1,-1):
    _,i,j=min((len(str(A[i][j])),i,j) for i in range(n) for j in range(n) if A[i][j])
    if i:A[0],A[i]=A[i],A[0];sign=-sign
    if j:
        for row in A:row[0],row[j]=row[j],row[0]
        sign=-sign
    piv=A[0][0]
    B=[[piv*A[i][j]-A[i][0]*A[0][j] for j in range(1,n)] for i in range(1,n)]
    den.extend([piv]*(n-2))
    for row in B:
        g=zero
        for z in row:g=g.gcd(z)
        assert g
        num.append(g)
        for j in range(n-1):row[j]=row[j]//g
    for j in range(n-1):
        g=zero
        for row in B:g=g.gcd(row[j])
        assert g
        num.append(g)
        for row in B:row[j]=row[j]//g
    A=B
num.append(A[0][0]*sign)
fac=json.loads((BASE/'tetrahedral_vertex_pencil_resultant_factors.json').read_text())
den.append(F(fac['constant'],3))
for rec in fac['factors']:den.extend([fp(rec['terms'])]*rec['exponent'])
for i in range(len(num)):
    for j in range(len(den)):
        g=num[i].gcd(den[j]);num[i]//=g;den[j]//=g
assert all(len(z)==1 and z.exponent_tuple(0)==(0,0,0) for z in num+den)
assert S.prod(int(z.coefficient(0)) for z in num)==S.prod(int(z.coefficient(0)) for z in den)
print('FULL three-variable quartic resultant identity PASS',flush=True)
# Boundary b1=1/3: reconstruct the cubics independently and compute resultant.
pb=r*(r-q*q)/(q*((r+1)*q+2*r))
b2=(q**3+r)/(3*r*(q+1)**2);b3=(q**3+r*r)/(3*(q+r)**2)
b=[S.Rational(2,3)-b2-b3,S.Rational(1,3),b2,b3]
bb=cent(pb+3*T,q,r+(1/b2-3)*T,1+(1/b3-3)*T)
J=[]
for i in [1,2]:
    n=S.factor(S.together(bb[i]-b[i])).as_numer_denom()[0]
    J.append(S.Poly(n/T,T,domain=S.QQ.poly_ring(q,r)).primitive()[1])
    assert J[-1].degree()==3
H1=2*q**4*r+q**4+2*q**3*r+q**3-2*q*q*r*r+2*q*q*r+q*r**3+2*q*r*r+3*r**3
H2=q**4*r+2*q**4+q**3*r*r+2*q**3*r+2*q*q*r*r-2*q*q*r+2*q*r*r+q*r+3*r*r
expected=-3**9*(r-1)**2*r*q**21*(q*r+q+2*r)*(q+1)**6*(q+r)**10*(q*q-r)**2*(q*q-q-2*r)**2*(q*q-q*r-2*r)**4*(q**3+r)*H1*H2**2
assert S.Poly(J[0].resultant(J[1])-expected,q,r).is_zero
print('FULL boundary cubic resultant identity PASS',flush=True)
# The displayed positivity endpoint identity, before imposing inequalities.
P,Q,R=S.symbols('P Q R')
g=(R*R+1)*P**3*Q**3+3*R*P**3*Q*Q+2*P**3*Q+R*P*P*Q**3-2*R*R*P*P*Q*Q-5*R*P*P*Q-3*P*P-3*R*P*Q*Q-3*P*Q-Q*Q
qm=(1-P*P)/(P*(R*P+2))
assert S.cancel(g.subs(Q,qm)+(P*P+2)*(P*P+R*P+1)**3/(P*P*(R*P+2)**3))==0
print('noncentral endpoint sign identity PASS',flush=True)
