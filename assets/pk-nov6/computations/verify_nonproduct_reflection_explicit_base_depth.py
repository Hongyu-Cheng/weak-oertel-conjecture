"""Independent exact reflection and complete planar angular-cell certificate."""
from functools import cmp_to_key
from itertools import product
from math import gcd

P = tuple((u, v) for v in range(5) for u in range(-1, 2)
          if 3*u+v >= 0)
weights = {p: (21-p[1])**14 for p in P}
A, B, C, D, E = ((21-v)**14 for v in range(5))
M = sum(weights.values())
assert len(P) == 12

expected_reflection = {
    (0,0): A, (1,0): A,
    (0,1): B+2*C, (1,1): B+2*C,
    (0,2): C+4*D+4*E, (1,2): C+2*D+2*E,
    (-1,3): D, (0,3): 3*D+4*E, (1,3): D+2*E,
    (-1,4): E, (0,4): 3*E, (1,4): E,
}
reflections = {}
for j in product(range(-2,3), range(-1,6)):
    retained = sum(min(w, weights.get((2*j[0]-p[0], 2*j[1]-p[1]), 0))
                   for p,w in weights.items())
    assert retained == expected_reflection.get(j, 0)
    reflections[j] = retained
assert max(reflections.values()) == A
assert M-4*A == 16547088947196739 > 0

def upper_half(v):
    return 0 if v[1] > 0 or (v[1] == 0 and v[0] > 0) else 1

def compare_angle(a, b):
    if upper_half(a) != upper_half(b):
        return upper_half(a)-upper_half(b)
    cross = a[0]*b[1]-a[1]*b[0]
    return -1 if cross > 0 else 1 if cross < 0 else 0

def all_cap_values(j):
    rays = set()
    for p in P:
        x,y = p[0]-j[0], p[1]-j[1]
        if not (x or y):
            continue
        g = gcd(abs(x), abs(y))
        n = (y//g, -x//g)
        rays.add(n)
        rays.add((-n[0], -n[1]))
    rays = sorted(rays, key=cmp_to_key(compare_angle))
    # These rays are every possible sign-change normal. On each intervening
    # open angular cell, all strict signs are constant. Consecutive rays here
    # have angle less than pi, so their sum is an exact interior representative.
    normals = list(rays)
    for a,b in zip(rays, rays[1:]+rays[:1]):
        assert a[0]*b[1]-a[1]*b[0] > 0
        normals.append((a[0]+b[0], a[1]+b[1]))
    values = []
    for n in normals:
        assert n != (0,0)
        captured = tuple(p for p in P
                         if n[0]*(p[0]-j[0])+n[1]*(p[1]-j[1]) >= 0)
        values.append((sum(weights[p] for p in captured), n, captured))
    return values

j = (0,1)
H = B+C+2*D+2*E
assert H == 3523789074065848027
assert 4*H-M == 1102929477230160645 > 0
assert A+B > H
assert 2*(B+C+D+E) > H
values = all_cap_values(j)
assert min(v[0] for v in values) == H
attaining = tuple(p for p in P if -4*p[0]+p[1]-1 >= 0)
assert set(attaining) == {(0,1),(0,2),(0,3),(0,4),(-1,3),(-1,4)}
assert sum(weights[p] for p in attaining) == H

# Verify all other candidate centers as a diagnostic, without needing them in
# the analytic three-case proof of the chosen center.
depths = {q: min(v[0] for v in all_cap_values(q)) for q in P}
assert max(depths.values()) == H
assert {q for q,d in depths.items() if d == H} == {j}
print("PASS: all 12 reflection values, exact halfspace rays/cells,")
print("depth H at (0,1), 4H-M=1102929477230160645, and actual-center certificate constants")
