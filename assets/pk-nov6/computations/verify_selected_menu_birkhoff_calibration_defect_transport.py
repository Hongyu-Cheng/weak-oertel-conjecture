"""Exact actual cap incidences, all 27 response vertices, and six pushed flows."""
from fractions import Fraction as F
from itertools import product, permutations
from pathlib import Path
import json

checks = 0
def require(value):
    global checks
    assert value
    checks += 1

def ell(z):
    x, y = z
    return (-x-y, 2*x-y, 2*y-x)

def quadratic(z):
    x, y = z
    return x*x-x*y+y*y

P = [(x,y) for x in range(-4,5) for y in range(-4,5)
     if min(ell((x,y))) >= -4]
beta = F(40,93)
require(len(P) == 31)
require(sum(quadratic(z) for z in P) == 165)
for i, expected in enumerate(((-21,-21),(21,0),(0,21))):
    positive = [z for z in P if ell(z)[i] > 0]
    zero = [z for z in P if ell(z)[i] == 0]
    require(len(positive) == 12 and len(zero) == 3)
    require(tuple(sum(z[j] for z in positive) for j in (0,1)) == expected)
    require(tuple(sum(z[j] for z in zero) for j in (0,1)) == (0,0))
    require(sum(quadratic(z) for z in positive) == 60)
    require(sum(quadratic(z) for z in zero) == 6)

# Each response vertex assigns one integer row to every continuous column.
balanced = []
for assignment in product(range(3), repeat=3):
    rows = [F(assignment.count(i),3) for i in range(3)]
    is_balanced = rows == [F(1,3)]*3
    if is_balanced:
        balanced.append(assignment)
    for facet in range(3):
        other = [j for j in range(3) if j != facet]
        source_mass = F(0)
        source_first = [F(0), F(0)]
        source_second = F(0)
        for z in P:
            for tier in range(3):
                t = F(2*tier+1,6)
                lam = [F(0)]*3
                lam[other[0]], lam[other[1]] = t, 1-t
                cap_count = sum(lam[j]-F(1,3)+ell(z)[assignment[j]] >= 0
                                for j in range(3))
                mass = F(cap_count,9)/beta  # normalized facet length 1
                source_mass += mass
                for c in (0,1):
                    source_first[c] += mass*z[c]
                source_second += mass*quadratic(z)
        require(source_mass == 31)
        require(source_first == [21*(rows[1]-rows[0])/beta,
                                 21*(rows[2]-rows[0])/beta])
        require((source_first == [0,0]) == is_balanced)
        require(165-source_second == F(193,10))
require(set(balanced) == set(permutations(range(3))))

canonical_hinges = [[F(98,45),F(1129,720),F(1129,720)],
                    [F(32,9),F(707,240),F(2183,720)],
                    [F(32,9),F(2183,720),F(707,240)]]
for assignment in permutations(range(3)):
    for facet in range(3):
        other = [j for j in range(3) if j != facet]
        hinges = [[F(0)]*3 for _ in range(3)]
        for z in P:
            for tier in range(3):
                t = F(2*tier+1,6)
                lam = [F(0)]*3
                lam[other[0]],lam[other[1]] = t,1-t
                W = F(sum(lam[j]-F(1,3)+ell(z)[assignment[j]] >= 0
                          for j in range(3)),3)
                for i in range(3):
                    for j in range(3):
                        hinges[i][j] += (1-W/beta)*max(ell(z)[i]+lam[j]-F(1,3),0)/3
        for row in hinges:
            for value in row:
                require(value >= F(1129,720))
        if facet == 0 and assignment == (0,1,2):
            require(hinges == canonical_hinges)

root = Path(__file__).resolve().parent
data = json.loads((root/'r4_facet_martingale_exact_slab_recovery.json').read_text())
high, low = data['high'], data['low']
for assignment in permutations(range(3)):
    # ell_assignment[j](M z) = ell_j(z).
    inverse = [assignment.index(i) for i in range(3)]
    def push(z):
        old = ell(z)
        new = [old[inverse[i]] for i in range(3)]
        x, y = F(new[1]-new[0],3), F(new[2]-new[0],3)
        require(x.denominator == y.denominator == 1)
        return (int(x),int(y))
    e1, e2 = push((1,0)), push((0,1))
    require(abs(e1[0]*e2[1]-e1[1]*e2[0]) == 1)
    require({push(z) for z in P} == set(P))
    H = [(*push(v[:2]),v[2]) for v in high]
    L = [(*push(v[:2]),v[2]) for v in low]
    for expected_count, points in ((2,H),(1,L)):
        for xx,yy,tier in points:
            lam = (F(0),F(2*tier+1,6),1-F(2*tier+1,6))
            require(sum(lam[j]-F(1,3)+ell((xx,yy))[assignment[j]] >= 0
                        for j in range(3)) == expected_count)
    out = [F(0)]*len(H)
    incoming = [F(0)]*len(L)
    drift = [[F(0)]*3 for _ in H]
    energy = F(0)
    for i,j,num,den in data['edges']:
        mass = F(num,den)
        require(mass > 0)
        out[i] += mass
        incoming[j] += mass
        for c in range(3):
            drift[i][c] += mass*(L[j][c]-H[i][c])
        energy += mass*quadratic((L[j][0]-H[i][0],L[j][1]-H[i][1]))/120
    require(out == [22]*len(H))
    require(incoming == [9]*len(L))
    require(drift == [[0]*3 for _ in H])
    require(energy == F(193,10))

print(f'PASS: {checks} exact nine-cap response and pushed-martingale checks')
