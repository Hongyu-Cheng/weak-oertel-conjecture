"""Independent exact vertex-enumeration checks for the affine-overlap formula.
The theorem is proved in the companion Markdown source; this is a finite audit.
"""
from fractions import Fraction as F
from itertools import combinations
import random
import sympy as sp

rng = random.Random(74191)
checks = 0

def vertices_of_original_overlap(r, beta, lam):
    d = len(r)-1
    # q_0=1-sum x_j; q_j=x_j. Every original and inverse-image
    # barycentric inequality is represented as const + row.x >= 0.
    bary = [(F(1), tuple(F(-1) for _ in range(d)))]
    bary += [(F(0), tuple(F(int(j==i)) for j in range(d))) for i in range(d)]
    constraints = list(bary)
    for ri, (constant, row) in zip(r, bary):
        # q_i - ri/(lambda-1)*(beta-q_0) >= 0.
        rate = ri/(lam-1)
        constraints.append((constant-rate*(beta-1), tuple(z-rate for z in row)))
    vertices = set()
    for ids in combinations(range(len(constraints)), d):
        mat = sp.Matrix([[sp.Rational(z.numerator,z.denominator) for z in constraints[i][1]] for i in ids])
        if mat.det() == 0:
            continue
        rhs = sp.Matrix([-sp.Rational(constraints[i][0].numerator,constraints[i][0].denominator) for i in ids])
        out = tuple(F(z) for z in mat.inv()*rhs)
        if all(c+sum(z*x for z,x in zip(row,out)) >= 0 for c,row in constraints):
            vertices.add(out)
    return sorted(vertices)

for d, count in [(2,16),(3,12),(4,6)]:
    for j in range(count):
        mid = [F(rng.randint(-4,4),2) for _ in range(d-1)]
        r = [F(1),*mid,-F(1)-sum(mid)]
        sigma = sum(max(z,F(0)) for z in r)
        beta = F(rng.randint(5,9),4)
        threshold = sigma*beta
        levels = [F(5,4), threshold, threshold+F(1,3), threshold+F(7,4)]
        if threshold-F(1,4)>1:
            levels.append(threshold-F(1,4))
        for lam in levels:
            pts = vertices_of_original_overlap(r,beta,lam)
            if lam < threshold:
                assert not pts, (d,r,beta,lam,pts)
            elif lam == threshold:
                assert len(pts)==1, (d,r,beta,lam,pts)
            else:
                assert len(pts)==d+1, (d,r,beta,lam,len(pts))
                base = pts[0]
                det = abs(F(sp.Matrix([[sp.Rational((p[i]-base[i]).numerator,(p[i]-base[i]).denominator) for i in range(d)] for p in pts[1:]]).det()))
                expected = (lam-1)/(lam-sigma)*(1-sigma*beta/lam)**d
                assert det==expected, (d,r,beta,lam,det,expected)
                assert expected <= (1-beta/lam)**d
            checks += 1

# Exact symbolic scalar comparisons and chosen eta dual identity.
lamb,sigma,beta = sp.symbols('lambda sigma beta',positive=True)
d,eta,V = sp.symbols('d eta V',positive=True)
for dd in range(2,12):
    for ee in [F(1,9),F(1,3),F(2,3),F(8,9)]:
        vol = dd*ee**(dd-1)-(dd-1)*ee**dd
        for be in [F(5,4),F(3,2),F(5,2)]:
            la=be/(1-ee)
            assert la*(vol-(1-be/la)**dd)==dd*be*ee**(dd-1)
            checks+=1
print(f'PASS: {checks} exact checks; original-inequality vertex enumeration in d=2,3,4.')
