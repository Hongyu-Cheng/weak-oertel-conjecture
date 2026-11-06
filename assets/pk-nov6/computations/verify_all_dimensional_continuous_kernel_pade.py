"""Exact algebra checks for the uniform Padé/Descartes proof.

The proof for arbitrary integer d is in the companion markdown file.
The finite dimension loop audits identities and does not prove uniformity.
"""
import sympy as s

d=s.symbols('d',integer=True,positive=True)
x,z,v=s.symbols('x z v')
theta=d/(d+1)
c=(2*d+1)/(3*(d+1))
e=(d-1)/(6*(d+1))
Q=(d-1)*x**2+2*(d+2)*x+3*(d+1)
R=(d-1)*(2*d+1)*x**2+2*(d+2)*(3*d+1)*x-(d-1)*(2*d+3)
g=1+(1+theta)*z+theta*z*z/(2*(1+c*z+e*z*z))
assert s.cancel((1+c*z+e*z*z)-Q.subs(x,1+z)/(6*(d+1)))==0
assert s.cancel(g.subs(z,x-1)-x*R/((d+1)*Q))==0
assert s.cancel(c*c-e-e*e-s.Rational(1,4))==0
D=(1+e*v*v)**2-c*c*v*v
pair=s.cancel(g.subs(z,v)+g.subs(z,-v)-2-theta*v*v)
claimed=theta*v**4*(s.Rational(1,4)+e*e*(1-v*v))/D
assert s.cancel(pair-claimed)==0
assert s.cancel(D-1-v*v*(e-s.Rational(1,4)-e*e*(1-v*v)))==0

# Symbolic derivatives at zero for arbitrary positive integer d.
f=(1+z)**(d+1)/(1+theta*z)**d
for order,value in enumerate([1,1+theta,theta,-3*theta*c]):
    assert s.simplify(s.diff(f,z,order).subs(z,0)-value)==0
    assert s.cancel(s.diff(g,z,order).subs(z,0)-value)==0

def variations(coefficients):
    nonzero=[s.sign(c) for c in coefficients if c!=0]
    return sum(a!=b for a,b in zip(nonzero,nonzero[1:]))

for dim in range(2,41):
    qq=Q.subs(d,dim);rr=R.subs(d,dim)
    pp=s.Poly((dim+1)**(dim+1)*x**dim*qq-(1+dim*x)**dim*rr,x)
    assert pp.nth(0)==(dim-1)*(2*dim+3)>0
    quotient,remainder=s.div(pp,s.Poly((x-1)**4,x))
    assert remainder.is_zero
    assert variations(list(reversed(pp.all_coeffs())))==4
    assert quotient.eval(1)>0
    for j in range(dim):
        norm=s.Rational(pp.nth(j),s.binomial(dim,j)*dim**j)
        formula=((dim-1)*(2*dim+3)
                 -s.Rational(2*(dim+2)*(3*dim+1),dim)*s.Rational(j,dim-j+1)
                 -s.Rational((dim-1)*(2*dim+1),dim**2)
                     *s.Rational(j*(j-1),(dim-j+1)*(dim-j+2)))
        assert norm==formula

print('PASS: arbitrary-d rational identities and four derivative matches; exact coefficientresearch-agent audits d=2,...,40')
