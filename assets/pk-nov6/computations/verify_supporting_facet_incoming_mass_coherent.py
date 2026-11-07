"""Exact positive boundary-density obstruction; all checks use Fraction."""
from fractions import Fraction as F

count = 0
def check(value):
    global count
    assert value
    count += 1

P = range(5)
h = {z: min(z, 4-z) for z in P}
points = {z: (F(z), F(h[z])) for z in P}
nu = {0:F(3,4), 1:F(3,2), 2:F(1,2), 3:F(3,2), 4:F(3,4)}
pi = {(p,q): F(0) for p in P for q in P}
for p in (0,2,4):
    pi[p,p] = nu[p]
for p in (1,3):
    pi[p,p-1], pi[p,p], pi[p,p+1] = F(1,4), F(1), F(1,4)
for p in P:
    check(nu[p] > 0)
    check(sum(pi[p,q] for q in P) == nu[p])
    for j in (0,1):
        check(sum(pi[p,q]*points[q][j] for q in P) == nu[p]*points[p][j])
for q in P:
    check(sum(pi[p,q] for p in P) == 1)
check(sum(nu.values()) == 5)

# Facet affine slacks. Both are nonnegative at every upper endpoint.
slacks = [
    {p: F(p-h[p]) for p in P},
    {p: F(4-p-h[p]) for p in P},
]
facets = [{0,1,2}, {2,3,4}]
for slack, facet in zip(slacks, facets):
    check(all(t >= 0 for t in slack.values()))
    check({p for p in P if slack[p] == 0} == facet)
    for p in facet:
        check(all(pi[p,q] == 0 for q in P if q not in facet))
    eta0 = {q:sum(pi[p,q] for p in facet) for q in facet}
    zeta = {q:F(1)-eta0[q] for q in facet}
    check(sum(nu[p] for p in facet) == F(11,4))
    check(sum(zeta.values()) == F(1,4))
    check(zeta[2] == F(1,4))
    check(all(zeta[q] == 0 for q in facet if q != 2))
    check(sum(pi[p,q] for p in P if p not in facet for q in facet) == F(1,4))
    corrected_source = {p:nu[p]+zeta[p] for p in facet}
    check(sum(corrected_source.values()) == 3)
    for j in (0,1):
        check(sum(corrected_source[p]*points[p][j] for p in facet)
              == sum(points[p][j] for p in facet))

# The lower boundary and all other continuous facets are fixed identically.
# Cartesian product with a unit (d-1)-cube keeps each upper fiber-face area 1;
# hence the same exact calculation holds for every d>=1.
check([1+h[z] for z in P] == [1,2,3,2,1])
print(f"PASS: {count} exact facet, mass, barycenter, and correction checks")
