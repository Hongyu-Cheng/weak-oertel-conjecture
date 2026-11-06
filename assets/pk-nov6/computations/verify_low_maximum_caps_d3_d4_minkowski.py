"""Independent exact checks for the proved d=3 and d=4 cap bounds."""

from fractions import Fraction as F
from itertools import combinations_with_replacement
from math import comb


def cap(nodes):
    nodes = sorted(nodes)
    d = len(nodes) - 1
    values = [F(max(0, x) ** d) for x in nodes]
    for j in range(1, d + 1):
        values = [
            (F(comb(d, j) * nodes[i] ** (d - j)) if nodes[i] > 0 else F(0))
            if nodes[i] == nodes[i + j]
            else (values[i + 1] - values[i]) / (nodes[i + j] - nodes[i])
            for i in range(d + 1 - j)]
    return values[0]


checks = 0
for d, target in [(3, F(1, 2)), (4, F(13, 27))]:
    smallest = F(1)
    for scale in range(2, 13):
        for aa in combinations_with_replacement(range(-scale, scale + 1), d):
            if sum(aa) != scale:
                continue
            probability = cap([-scale] + list(aa))
            assert probability >= target
            smallest = min(smallest, probability)
            checks += 1
            positives = [F(x, scale) for x in aa if x > 0]
            negatives = [F(-x, scale) for x in aa if x < 0]
            if len(positives) == 2 and len(negatives) <= 1:
                p, q = positives
                c = sum(negatives)
                rhs = F(1, 2) + (p*q-c)*(p*q+c) / \
                    (2*(p+1)*(q+1)*(p+c)*(q+c))
                assert probability == rhs
                checks += 1
            if len(positives) == 3:
                p, q, r = positives
                c = sum(negatives)
                e2, e3 = p*q+p*r+q*r, p*q*r
                A = (1+p)*(1+q)*(1+r)
                B = (c+p)*(c+q)*(c+r)
                rhs = F(1, 2) + (e3**2+(1+c)*(e2-c)*e3+
                                  c*(e2-c)*(e2+c))/(2*A*B)
                assert probability == rhs
                checks += 1
            if len(positives) == 2 and len(negatives) == 2:
                p, q = positives
                c, e = negatives
                C, Q, P, S = c+e, c*e, p*q, p+q
                N = P**3+(S**2-C-Q)*P**2 + \
                    ((C+Q)*S**2-2*Q*S)*P+Q*S**3
                D = (P+C+2)*(P**2+(C+2*C**2-2*Q)*P+
                               Q*S*(S+C)+Q**2)
                assert probability == N/D
                checks += 1
    assert smallest == target

for denominator in range(1, 14):
    for numerator in range(denominator + 1):
        C = F(numerator, denominator)
        for X in [F(0), F(1, 13), F(1, 3), F(1), F(2)]:
            P, Q, S = C+X, C**2/4, 1+C
            N = P**3+(S**2-C-Q)*P**2 + \
                ((C+Q)*S**2-2*Q*S)*P+Q*S**3
            D = (P+C+2)*(P**2+(C+2*C**2-2*Q)*P+
                           Q*S*(S+C)+Q**2)
            expanded = 14*X**3+(1+43*C+F(3,4)*C**2)*X**2 + \
                (3*C+36*C**2-F(3,4)*C**3-F(9,16)*C**4)*X + \
                F(9,8)*C**2*(1-C)*(C**2+6*C+2)
            assert 27*N-13*D == expanded >= 0
            checks += 1

assert F(1,2)-F(7,6)*F(3,4)**3 == F(1,128)
assert F(13,27)-F(7,6)*F(4,5)**4 == F(61,16875)
checks += 2
print(f'PASS: {checks} exact d3/d4 cap, identity, boundary, and constant checks')
