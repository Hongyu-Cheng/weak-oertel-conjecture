"""Exact certificate; no numerical optimization or floating-point premises."""
from fractions import Fraction as F
from itertools import product, combinations

checks = 0
def check(test):
    global checks
    assert test
    checks += 1

vertices = [(1, 0), (0, 1), (-1, -1)]
def in_Q(p):
    x, y = p
    return x+y <= 1 and -2*x+y <= 1 and x-2*y <= 1
B = [(0, 0)] + vertices
check(set(p for p in product(range(-1, 2), repeat=2) if in_Q(p)) == set(B))
check(len({tuple(t % 2 for t in b) for b in B}) == 4)
P = [b+(j,) for b in B for j in range(3)]
check(len(P) == 12)
check(len({tuple(t % 2 for t in p) for p in P}) == 8)
check(F(1) < F(len(P), 8))

edges = []
for p, q in combinations(P, 2):
    if all((a+b) % 2 == 0 for a, b in zip(p, q)):
        m = tuple((a+b)//2 for a, b in zip(p, q))
        check(m in P)
        edges.append((p, q, m))
check(len(edges) == 4)
for p, q, m in edges:
    check(p[:2] == q[:2] == m[:2])
    check({p[2], q[2]} == {0, 2} and m[2] == 1)

phi = lambda p: p[0]**2+p[1]**2
for p, q, m in edges:
    check(F(phi(p)+phi(q), 2)-phi(m) == 0)

nu = {p: F(2) if p[:2] == (0, 0) else F(2, 3) for p in P}
coupling = {(p, q): F(0) for p in P for q in P}
for j in range(3):
    a = (0, 0, j)
    coupling[a, a] = F(1)
    for v in vertices:
        b = v+(j,)
        coupling[a, b] = F(1, 3)
        coupling[b, b] = F(2, 3)
for p in P:
    check(sum(coupling[p, q] for q in P) == nu[p])
    for k in range(3):
        check(sum(coupling[p, q]*q[k] for q in P) == nu[p]*p[k])
for q in P:
    check(sum(coupling[p, q] for p in P) == 1)
check(sum(nu.values()) == 12)
check(sum((1-nu[p])*phi(p) for p in P) == 4)
for p, q in coupling:
    if coupling[p, q]:
        check(p[2] == q[2])

normals = [(2, -1, 0), (-1, 2, 0), (-1, -1, 0)]
dot = lambda a, b: sum(x*y for x, y in zip(a, b))
check(tuple(sum(a[k] for a in normals) for k in range(3)) == (0, 0, 0))
for p in P:
    check(sum(F(2, 3) for a in normals if dot(a, p) >= 0) == nu[p])
for i, a in enumerate(normals):
    check(sum(dot(a, p) >= 0 for p in P) == 6)
    for j, v in enumerate(vertices):
        check((dot(a, v+(0,)) > 0) == (i == j))
check(3*F(2, 3) == 1/F(1, 2))

# Exact binary-padding combinatorics for representative additional dimensions.
for extra in range(5):
    PP = [p+t for p in P for t in product((0, 1), repeat=extra)]
    check(len(PP) == 12*2**extra)
    check(len({tuple(a % 2 for a in p) for p in PP}) == 8*2**extra)
    check(F(1) < F(len(PP), 8*2**extra))
    count = 0
    for p, q in combinations(PP, 2):
        if all((a+b) % 2 == 0 for a, b in zip(p, q)):
            m = tuple((a+b)//2 for a, b in zip(p, q))
            check(m in PP)
            check(p[3:] == q[3:])
            check(F(phi(p)+phi(q), 2) == phi(m))
            count += 1
    check(count == 4*2**extra)
print(f"PASS: {checks} exact midpoint, martingale, cap, and padding checks")
