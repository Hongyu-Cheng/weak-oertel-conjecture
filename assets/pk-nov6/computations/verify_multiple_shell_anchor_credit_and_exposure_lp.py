"""Exact auxiliary checks; the accompanying note proves all dimensions."""
from fractions import Fraction as F
from itertools import product, combinations, permutations


def clip(poly, u, c):
    result = []
    for p, q in zip(poly, poly[1:] + poly[:1]):
        v = sum(a*b for a, b in zip(u, p)) + c
        w = sum(a*b for a, b in zip(u, q)) + c
        if v >= 0:
            result.append(p)
        if v*w < 0:
            t = v/(v-w)
            result.append(tuple(p[i]+t*(q[i]-p[i]) for i in range(2)))
    return result


def area(poly):
    if len(poly) < 3:
        return F(0)
    return abs(sum(p[0]*q[1]-p[1]*q[0]
                   for p, q in zip(poly, poly[1:]+poly[:1])))/2


def feasible_2d(rows):
    # All systems include the two independent coordinate lower bounds.
    # Hence a nonempty polyhedron is pointed and has a finite vertex.
    for (a, b, c), (d, e, f) in combinations(rows, 2):
        determinant = a*e-b*d
        if not determinant:
            continue
        x, y = F(c*e-b*f, determinant), F(a*f-c*d, determinant)
        if all(u*x+v*y >= w for u, v, w in rows):
            return (x, y)
    return None


T = [(F(0), F(0)), (F(1), F(0)), (F(0), F(1))]
V = F(1, 2)
Gamma = F(4, 9)
b, h = F(1, 3), F(2, 3)
cube = list(product([0, 1], repeat=2))
outside = [(-1, 1), (1, -1)]
all_bases = cube+outside
assert [(x, y) for x, y in product(range(-2, 3), repeat=2)
        if x <= 1 and y <= 1 and x+y >= 0] == sorted(all_bases)

normals = set()
for v in [F(0), F(1, 4), F(1, 2), F(3, 4), F(1)]:
    normals.update(permutations([F(0), v, F(1)]))

cap_checks = 0
lp_checks = 0
for r in [F(1, 20), F(1, 10), F(3, 20)]:
    A = [(b+r*(x-b), b+r*(y-b)) for x, y in T]
    a = r*r*V
    alpha = a/V
    assert 81*alpha*alpha+108*alpha-4 < 0
    fibers = [(z, T) for z in cube]+[(z, A) for z in outside]
    for values in normals:
        u = (values[1]-values[0], values[2]-values[0])
        constant, mean = values[0], sum(values)/3
        for beta in product([F(i, 2) for i in range(-4, 5)], repeat=2):
            for anchor, target in [((0, 0), Gamma*(V+2*a)),
                                   ((0, 1), Gamma*V+a),
                                   ((1, 0), Gamma*V+a)]:
                mass = sum(area(clip(K, u, constant-mean
                            +sum(beta[i]*(z[i]-anchor[i]) for i in range(2))))
                           for z, K in fibers)
                assert mass >= target
                cap_checks += 1
    for u, constant in [((-1, -1), F(1)), ((1, 0), F(0)),
                         ((0, 1), F(0))]:
        masses = [area(clip(K, u, constant-b-h*sum(z))) for z, K in fibers]
        assert masses == [Gamma*V, 0, 0, 0, Gamma*a, Gamma*a]
        for anchor in [(0, 1), (1, 0)]:
            def delta(z):
                return z[0]+1-z[1] if anchor == (0, 1) else 1-z[0]+z[1]
            masses = [area(clip(K, u, constant-b-2*delta(z))) for z, K in fibers]
            assert sum(masses) == Gamma*V+a
            assert masses[cube.index(anchor)] == Gamma*V
        assert sum(area(clip(K, u, constant-b-2*(2-sum(z))))
                   for z, K in fibers) == Gamma*V
    for q in cube:
        transformed = [tuple(1-p[i] if q[i] else p[i] for i in range(2))
                       for p in outside]
        costs = []
        directional_costs = []
        for mask in product([0, 1], repeat=2):
            rows = [(1, 0, 1), (0, 1, 1)]
            directional_rows = [(1, 0, h), (0, 1, h)]
            for selected, p in zip(mask, transformed):
                if selected:
                    rows.append((*p, F(1)))
                    directional_rows.append((*p, r*h))
            cost = (2-sum(mask))*a
            if feasible_2d(rows) is not None:
                costs.append(cost)
            if feasible_2d(directional_rows) is not None:
                directional_costs.append(cost)
            lp_checks += 2
        expected = 0 if q == (1, 1) else a
        assert min(costs) == expected
        assert min(directional_costs) == expected
    assert 2*Gamma*a < a
    # Exact binary full/empty optimum: opposite shifts +/- r h.
    assert area(clip(A, (1, 0), -b+r*h)) == a
    assert area(clip(A, (1, 0), -b-r*h)) == 0

# Aggregate-anchor lower bound in all seven nonempty negative-square subsets.
negative = [(-1, -1), (-1, 0), (0, -1)]
r = F(1, 20)
small = [T, [(F(0), F(0)), (r, F(0)), (F(0), r)]]
added = {
    negative[0]: [(F(0), F(0)), (r, F(0)), (F(0), r)],
    negative[1]: [(1-r, F(0)), (F(1), F(0)), (1-r, r)],
    negative[2]: [(F(0), 1-r), (r, 1-r), (F(0), F(1))],
}
aggregate_checks = 0
for mask in product([0, 1], repeat=3):
    if not any(mask):
        continue
    chosen = [p for p, flag in zip(negative, mask) if flag]
    E = sum(area(added[p]) for p in chosen)
    alpha = E/V
    assert 81*alpha*alpha+108*alpha-4 < 0
    fibers = [(z, T) for z in cube]+[(p, added[p]) for p in chosen]
    for values in normals:
        u = (values[1]-values[0], values[2]-values[0])
        constant, mean = values[0], sum(values)/3
        for beta in product([F(i) for i in range(-2, 3)], repeat=2):
            mass = sum(area(clip(K, u, constant-mean
                        +sum(beta[i]*z[i] for i in range(2)))) for z, K in fibers)
            assert mass >= Gamma*V+E
            aggregate_checks += 1

# The explicit exposing directions for ALL negative-cube additions.
exposure_checks = 0
for n in range(1, 7):
    Q = list(product([0, 1], repeat=n))
    P = [tuple(-x for x in v) for v in Q if any(v)]
    for p in P:
        S = [i for i, x in enumerate(p) if x == -1]
        u = tuple(-(n+1) if i in S else 1 for i in range(n))
        top = sum(u[i]*p[i] for i in range(n))
        for z in Q+P:
            if z != p:
                assert top-sum(u[i]*z[i] for i in range(n)) >= 1
                exposure_checks += 1
    for w in Q:
        if not any(w):
            continue
        def delta(z):
            return ((n+1)*sum(1-z[i] for i in range(n) if w[i])
                    +sum(z[i] for i in range(n) if not w[i]))
        assert delta(w) == 0
        for z in Q+P:
            if z != w:
                assert delta(z) >= 1
                exposure_checks += 1

print(f'PASS: {cap_checks} exact six-base cap checks, {lp_checks} LP tests, '
      f'{aggregate_checks} aggregate-anchor caps, {exposure_checks} exposures; '
      'exact partial-trace first-order gap and finite matching covers.')
