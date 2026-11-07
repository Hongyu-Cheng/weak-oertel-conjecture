from fractions import Fraction as F
from itertools import product
import sympy as s

checks=0
def yes(a):
    global checks
    assert a
    checks+=1

# Exact irreducible full-rank canonical circuits: their only null vector
# is strictly positive, so no proper subcollection has dependence.
for d in range(2,12):
    U=s.eye(d).row_join(-s.ones(d,1))
    yes(U.rank()==d)
    yes(U*s.ones(d+1,1)==s.zeros(d,1))
    for i in range(d+1):
        yes(U[:,[j for j in range(d+1) if j!=i]].det()!=0)

# Projected flux/variation lower weight bound, varied exact scalar data.
for te,other,r,theta,beta,q in product(
        [F(0),F(1,3),F(2,3),F(1)], repeat=6):
    if theta==0 or beta==0: continue
    # Radial inside status: load_e=te-r and load_other=other.
    if not 0<=r<=te: continue
    load=theta*(te-r)+(1-theta)*other
    if load+q>beta: continue
    captured=theta*te+(1-theta)*other
    yes((1-theta)*other+q<=beta)
    yes(theta*r>=max(F(0),captured+q-beta))
    if te:
        yes(theta>=max(F(0),captured+q-beta)/te)
    # The weaker no-angle bound uses r <= te+1.
    yes(theta>=max(F(0),captured+q-beta)/(te+1))

# Outside status never reduces captured defect.
for te,other,r,theta,beta,q in product(
        [F(0),F(1,2),F(1)], repeat=6):
    if not 0<=r<=1-te: continue
    captured=theta*te+(1-theta)*other
    if captured+theta*r+q<=beta:
        yes(captured+q<=beta)

# Atom calibration, canceling exactly the same section term.
u=s.Matrix([1,1]);c=s.symbols('c',positive=True)
M=s.Rational(1,2);Z=2*s.log(2)/c;S=s.log(2)
yes(s.simplify(M*c*u*Z-u*S)==s.zeros(2,1))
yes(s.simplify(M*c*u*0-(-u)*S)==u*s.log(2))
yes(s.Rational(1,2)*u*S+s.Rational(1,2)*(-u)*S==s.zeros(2,1))
print(f'PASS: {checks} exact circuit, status, weight and flux checks')
